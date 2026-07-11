#!/usr/bin/env python3
"""Prueft generierte Werkstatt- und Schnellstart-Prompts auf Quellenrauschen."""

from __future__ import annotations

import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PROTECTED_LIST = REPO / "scripts" / "handkuratierte-prompts.txt"

NOISE_BITS = (
    "Tragende Normen verifizieren",
    "Fundstellen über",
    "Fundstellen ueber",
    "gesetze-im-internet.de",
    "dejure.org",
    "openJur",
    "openjur",
    "keine Modellwissen-Zitate",
    "live prüfen",
    "live pruefen",
)

PROSE_ASCII_BITS = (
    "Arbeitsverhaeltnis",
    "Schuldverhaeltnis",
    "auslaendisch",
    "Auslaendisch",
    "Bruessel",
    "Kausalitaet",
    "Zulaessig",
    "zulaessig",
    "Rechtmaessig",
    "rechtmaessig",
    "Uebereinkommen",
    "Identitaet",
    "Ermaechtigungsgrundlage",
    "Tatbestaende",
    "Einraeumung",
    "Schoepfung",
    "endgueltig",
    "grundsaetzlich",
    "Menschenwuerde",
    "Loeschung",
    "Verguetung",
    "Aenderung",
    "geschuetzte",
    "Strafhoehe",
    "Faellen",
    "Geschaeftsfuehrer",
    "Verhaeltnismaessigkeit",
    "Insolvensnaehe",
    "Insolvenznaehe",
    "Bargeschaeftsnaehe",
    "Schoepfungshoehe",
    "Heranfuehrung",
    "Begruendung",
    "begruendung",
    "Folgenabschaetzung",
    "Verspaetung",
    "Pfaendung",
    "Gefahrerhoehung",
    "Betriebsgroesse",
    "Auskuenfte",
    "Beiraete",
    "Adhaesion",
    "Klaeger",
    "Versorgungstraeger",
    "Schoeff",
)

COURT_BITS = ("BGH", "BVerfG", "BVerwG", "BAG", "BFH", "BSG", "EuGH", "OLG", "LG", "ArbG", "LAG")
TRUNCATED_CASE_END = re.compile(
    r"(?:\beingeleiteter|\bersetzt|\bstärkt|\bstatt einer|\bnicht der|"
    r"\bQuelle|\bBestandteil der Verpflichtung)\.?\s*(?:\|)?$",
    flags=re.IGNORECASE,
)


def protected_slugs() -> set[str]:
    if not PROTECTED_LIST.exists():
        return set()
    out: set[str] = set()
    for raw in PROTECTED_LIST.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line and not line.startswith("#"):
            out.add(line)
    return out


def prompt_files() -> list[Path]:
    files: list[Path] = []
    marketplace = json.loads(
        (REPO / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8")
    )
    for entry in marketplace.get("plugins", []):
        source = entry.get("source", "")
        if not isinstance(source, str) or not source.startswith("./"):
            continue
        plugin_dir = REPO / source[2:]
        manifest_path = plugin_dir / ".claude-plugin" / "plugin.json"
        if not manifest_path.exists():
            continue
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        slug = manifest.get("name") or plugin_dir.name
        files.extend(
            (
                plugin_dir / f"{slug}-werkstatt.md",
                plugin_dir / f"{slug}-schnellstart.md",
            )
        )
    return sorted(files, key=lambda p: p.as_posix())


def main() -> int:
    protected = protected_slugs()
    problems: list[str] = []
    for path in prompt_files():
        if not path.exists():
            problems.append(f"{path.relative_to(REPO)}: erwarteter Prompt fehlt")
            continue
        plugin_slug = path.parent.name
        if plugin_slug in protected:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for bit in NOISE_BITS:
            if bit in text:
                rel = path.relative_to(REPO)
                problems.append(f"{rel}: Quellenrauschen gefunden: {bit}")
                break
        for bit in PROSE_ASCII_BITS:
            if bit in text:
                rel = path.relative_to(REPO)
                problems.append(f"{rel}: unechter Umlaut in Prosa gefunden: {bit}")
                break
        for line_no, line in enumerate(text.splitlines(), start=1):
            if any(court in line for court in COURT_BITS) and TRUNCATED_CASE_END.search(line):
                rel = path.relative_to(REPO)
                problems.append(
                    f"{rel}:{line_no}: Rechtsprechungsanker endet als Satzfragment"
                )
                break
    if problems:
        print("audit-generated-prompt-hygiene: FEHLER")
        for problem in problems[:80]:
            print(f"- {problem}")
        if len(problems) > 80:
            print(f"- ... {len(problems) - 80} weitere Treffer")
        return 1
    print(f"audit-generated-prompt-hygiene OK ({len(prompt_files())} Prompt-Dateien)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
