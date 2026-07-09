#!/usr/bin/env python3
"""Prüft Prompt-Vollständigkeit, Dezimalgliederung und kritische Fachrouten."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

from themen_profile import profile_for  # noqa: E402


CRITICAL_ROUTES = {
    "betreuungsrecht": "betreuung",
    "dfg-foerderantrag": "verwaltung",
    "einigungsvertrag-vermoegensrecht": "verwaltung",
    "erbbaurecht-praxis": "immobilien",
    "europarecht-kompass": "eu_recht",
    "fachanwalt-migrationsrecht": "verwaltung",
    "fachanwalt-transport-speditionsrecht": "international",
    "forschungszulage-antragstellung": "steuer",
    "grundbuchamt-praxis": "immobilien",
    "haushaltsrecht-bho-bund-laender": "verwaltung",
    "hoai-leistungsphasen-praxis": "hoai",
    "immobilienrechtspraxis": "immobilien",
    "internal-investigations-praxis": "straf",
    "meinungspruefer": "verfass",
    "methodenlehre-buergerliches-recht": "methodik",
    "notariat-alltag": "immobilien",
    "startup-hr-personalabteilung-berlin": "hr",
    "subsumtions-pruefer": "methodik",
    "verhaeltnismaessigkeitspruefer": "verfass",
    "wahlkampfrecht-praxis": "verfass",
    "weltraumrecht": "weltraum",
}

REQUIRED_WERKSTATT = (
    "Rolle und Auftrag",
    "Rechtsprechungs-Fallkarte",
    "Normenanker, Tatbestandswichtigkeiten und Beweislast",
    "Rechtsprechungsanker, Quellenstatus und Rechtsfolgen",
    "Outputvarianten und Empfängerwunsch",
)
REQUIRED_SCHNELLSTART = (
    "Schnellmodus",
    "Direktstart",
    "Kernroute",
    "Fallkarte",
    "Anker",
    "Antwortform",
    "Stop",
)


def protected_slugs() -> set[str]:
    path = REPO / "scripts" / "handkuratierte-prompts.txt"
    if not path.exists():
        return set()
    return {
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }


def marketplace_plugins() -> list[tuple[str, Path, str]]:
    marketplace = json.loads(
        (REPO / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8")
    )
    plugins: list[tuple[str, Path, str]] = []
    for entry in marketplace.get("plugins", []):
        source = entry.get("source", "")
        if not isinstance(source, str) or not source.startswith("./"):
            raise ValueError(f"Ungültige Marketplace-Quelle: {source!r}")
        plugin_dir = REPO / source[2:]
        manifest_path = plugin_dir / ".claude-plugin" / "plugin.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        slug = manifest.get("name") or plugin_dir.name
        description = manifest.get("description", "")
        plugins.append((slug, plugin_dir, description))
    return plugins


def decimal_h2_problems(text: str) -> list[str]:
    problems: list[str] = []
    numbers: list[int] = []
    for line in text.splitlines():
        if not line.startswith("## "):
            continue
        match = re.match(r"^## (\d+)\.\s+\S", line)
        if not match:
            problems.append(f"nicht dezimal: {line[:100]}")
            continue
        numbers.append(int(match.group(1)))
    if numbers and numbers != list(range(1, len(numbers) + 1)):
        problems.append(f"H2-Folge nicht lückenlos: {numbers}")
    return problems


def main() -> int:
    plugins = marketplace_plugins()
    protected = protected_slugs()
    problems: list[str] = []
    profile_counts: Counter[str] = Counter()
    checked_files = 0

    slugs = [slug for slug, _plugin_dir, _description in plugins]
    if len(slugs) != len(set(slugs)):
        problems.append("Marketplace enthält doppelte Plugin-Slugs")

    for slug, plugin_dir, description in plugins:
        profile = profile_for(slug, description)
        profile_counts[profile.key] += 1
        expected_route = CRITICAL_ROUTES.get(slug)
        if expected_route and profile.key != expected_route:
            problems.append(
                f"{slug}: Fachroute {profile.key!r}, erwartet {expected_route!r}"
            )

        expected = {
            "werkstatt": plugin_dir / f"{slug}-werkstatt.md",
            "schnellstart": plugin_dir / f"{slug}-schnellstart.md",
        }
        actual = set(plugin_dir.glob("*-werkstatt.md")) | set(
            plugin_dir.glob("*-schnellstart.md")
        )
        extras = actual - set(expected.values())
        if extras:
            for path in sorted(extras):
                problems.append(f"{path.relative_to(REPO)}: verwaister Prompt-Dateiname")

        for kind, path in expected.items():
            checked_files += 1
            if not path.exists():
                problems.append(f"{path.relative_to(REPO)}: fehlt")
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            size = len(text.encode("utf-8"))
            if kind == "schnellstart" and size > 7500:
                problems.append(f"{path.relative_to(REPO)}: {size} Bytes statt höchstens 7500")
            if kind == "werkstatt" and not 12 * 1024 <= size <= 22 * 1024:
                problems.append(
                    f"{path.relative_to(REPO)}: {size} Bytes außerhalb 12 bis 22 KiB"
                )
            if slug in protected:
                continue
            required = REQUIRED_WERKSTATT if kind == "werkstatt" else REQUIRED_SCHNELLSTART
            for marker in required:
                if marker not in text:
                    problems.append(f"{path.relative_to(REPO)}: Abschnitt {marker!r} fehlt")
            for issue in decimal_h2_problems(text):
                problems.append(f"{path.relative_to(REPO)}: {issue}")

    if profile_counts["default"] > 24:
        problems.append(
            f"Zu viele Plugins ohne Fachprofil: {profile_counts['default']} statt höchstens 24"
        )

    expected_file_count = len(plugins) * 2
    if checked_files != expected_file_count:
        problems.append(
            f"Prompt-Zählung abweichend: {checked_files} statt {expected_file_count}"
        )

    if problems:
        print("audit-prompt-profile-routing: FEHLER")
        for problem in problems[:120]:
            print(f"- {problem}")
        if len(problems) > 120:
            print(f"- ... {len(problems) - 120} weitere Treffer")
        return 1

    routes = ", ".join(
        f"{key}={count}" for key, count in sorted(profile_counts.items())
    )
    print(
        f"audit-prompt-profile-routing OK ({len(plugins)} Plugins, "
        f"{checked_files} Prompts; {routes})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
