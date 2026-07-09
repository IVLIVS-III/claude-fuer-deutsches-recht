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

from themen_profile import EXACT_PROFILE_KEYS, profile_for  # noqa: E402


CRITICAL_ROUTES = dict(EXACT_PROFILE_KEYS)

PROMPT_ASSERTIONS: dict[str, dict[str, tuple[str, ...]]] = {
    "fachanwalt-agrarrecht": {
        "required": ("54.000 EUR", "60 Prozent", "BLw 12/11", "LwVfG"),
        "forbidden": (
            "Dreiwochenfrist",
            "1,4-facher Einheitswert",
            "1,5-facher Einheitswert",
            "IV ZR 256/01",
            "10 W 47/20",
            "LwVG und HöfeVfO",
            "Abfindung, Schriftform und Landwirtschaftsgericht",
        ),
    },
    "fachanwalt-sportrecht": {
        "required": ("1 BvR 2103/16", "7 AZR 312/16"),
        "forbidden": ("Auskunft, Einkommen, Bedarf, Selbstbehalt",),
    },
    "juristische-presseberichterstattung": {
        "required": ("1 BvR 573/25", "VI ZR 1241/20"),
        "forbidden": ("Auskunft, Einkommen, Bedarf, Selbstbehalt",),
    },
    "jveg-kostenpruefer": {
        "required": ("JVEG Paragraf 1 und Paragraf 2", "JVEG Paragraf 4", "dreimonatige Ausschlussfrist"),
        "forbidden": ("Dreiwochenfrist",),
    },
    "schoeffen-handelsrichter-praxis": {
        "required": (
            "StPO Paragraf 240 Absatz 2",
            "StPO Paragraf 261",
            "StPO Paragraf 263",
            "Zweidrittelmehrheit",
            "DRiG Paragraf 43",
        ),
        "forbidden": ("(Geheimhaltung)", "Paragraf 76 GVG (Mitwirkung)"),
    },
}

SOURCE_FORBIDDEN: tuple[tuple[Path, tuple[str, ...]], ...] = (
    (
        REPO / "fachanwalt-agrarrecht",
        (
            "1,4-facher Einheitswert",
            "1,5-facher Einheitswert",
            "1 4-facher Einheitswert",
            "1 5-facher Einheitswert",
            "10.000 EUR Einheitswert",
            "Bewirtschaftungspflicht § 17",
            "Altenteilsleistungen § 14 HöfeO",
            "rueckkaufrecht-30-jahre",
            "Rueckkaufrecht 30 Jahre",
            "Rückkaufrecht 30 Jahre",
            "Rueckkaufpreis = Wert bei Hofuebergang",
            "Wirtschaftswert ab 10.000 EUR",
            "Wirtschaftswert ≥ 10.000 EUR",
            "§ 13 LPachtVG",
            "HöfeO gilt nur in NW, NI, SH, HB",
            "Hofvermerk im Grundbuch Pflicht",
            "BGB § 594a Landpacht-Kündigung 2. Werktag im 3. Pachtjahr",
            "Vorpachtrecht § 588 BGB",
            "Vorpacht / Vorpfand-Recht",
            "Vorpacht-Recht",
            "9 Jahre Standard-Laufzeit",
            "Vertrag verlaengert sich um 9 Jahre",
            "Pacht-Anpassung ohne 3-Jahres-Wartezeit",
            "Landwirtschaftsgericht beim Amtsgericht oder Landgericht je nach Streitwert",
            "4-facher Jahres-Pachtzins",
            "4-facher Jahrespachtzins",
            "Schriftform gewahrt (§ 585a BGB)?",
            "Verlaengerung Schriftform § 585a BGB",
            "LwVG",
            "§ 23 LwVfG",
            "Paragraf 23 LwVfG",
            "Pflichtiger Schlichtungsversuch",
            "Schlichtungsantrag nach § 23",
            "Wert bis 5.000 EUR",
            "§ 41 Abs. 1 ZPO",
            "LPachtVG §§ 2, 4, 13",
            "dreifacher Jahresmehrwert",
            "VwGO § 70 / SGG § 84",
        ),
    ),
    (
        REPO / "testakten" / "megaprompts" / "fachanwalt-agrarrecht.md",
        (
            "LwVG",
            "§ 23 LwVfG",
            "Paragraf 23 LwVfG",
            "Pflichtiger Schlichtungsversuch",
            "Schlichtungsantrag nach § 23",
        ),
    ),
    (
        REPO / "juristische-presseberichterstattung" / "skills",
        ("aktueller Suchanker zur Verdachtsberichterstattung",),
    ),
    (
        REPO / "schoeffen-handelsrichter-praxis" / "skills",
        (
            "§ 76 GVG (Mitwirkung)",
            "§ 263 StPO (Geheimhaltung)",
            "§ 43 DRiG (Eid)",
        ),
    ),
)

GLOBAL_MD_FORBIDDEN: tuple[tuple[re.Pattern[str], str], ...] = (
    (re.compile(r"\bVwG\b"), "VwG statt VwGO oder ausgeschriebenem Verwaltungsgericht"),
    (re.compile(r"\bLwVG\b"), "LwVG statt LwVfG"),
)

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


def source_anchor_problems() -> list[str]:
    problems: list[str] = []
    for root, forbidden_bits in SOURCE_FORBIDDEN:
        files = [root] if root.is_file() else sorted(root.rglob("*.md"))
        for path in files:
            text = path.read_text(encoding="utf-8", errors="ignore")
            for bit in forbidden_bits:
                if bit in text:
                    problems.append(
                        f"{path.relative_to(REPO)}: veralteter oder falscher Anker {bit!r}"
                    )
    for path in sorted(REPO.rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern, label in GLOBAL_MD_FORBIDDEN:
            if pattern.search(text):
                problems.append(
                    f"{path.relative_to(REPO)}: veraltete Gesetzesabkürzung {label}"
                )
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
            assertions = PROMPT_ASSERTIONS.get(slug)
            if assertions:
                for marker in assertions["required"]:
                    if marker not in text:
                        problems.append(
                            f"{path.relative_to(REPO)}: Fachanker {marker!r} fehlt"
                        )
                for marker in assertions["forbidden"]:
                    if marker in text:
                        problems.append(
                            f"{path.relative_to(REPO)}: fachfremder oder falscher Anker {marker!r}"
                        )

    if profile_counts["default"]:
        problems.append(
            f"Plugins ohne Fachprofil: {profile_counts['default']} statt 0"
        )

    problems.extend(source_anchor_problems())

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
