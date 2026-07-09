#!/usr/bin/env python3
"""Prueft generierte Werkstatt- und Schnellstart-Prompts auf Quellenrauschen."""

from __future__ import annotations

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
    for pattern in ("*-werkstatt.md", "*-schnellstart.md"):
        files.extend(REPO.glob(f"*/{pattern}"))
        files.extend(REPO.glob(f"gerichtsplugins/*/{pattern}"))
        files.extend(REPO.glob(f"insolvenzrecht-plugins/*/{pattern}"))
    return sorted(set(files), key=lambda p: p.as_posix())


def main() -> int:
    protected = protected_slugs()
    problems: list[str] = []
    for path in prompt_files():
        plugin_slug = path.parent.name
        if plugin_slug in protected:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for bit in NOISE_BITS:
            if bit in text:
                rel = path.relative_to(REPO)
                problems.append(f"{rel}: Quellenrauschen gefunden: {bit}")
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
