#!/usr/bin/env python3
"""Schreibt docs/werkstatt-und-schnellstart-coverage.md."""

from __future__ import annotations

import json
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"
DOCS = REPO / "docs"
RAW_BASE = "https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main"


def prompt_stem(plugin_name: str) -> str:
    return plugin_name


def plugin_dir(plugin: dict) -> Path:
    source = plugin.get("source") or f"./{plugin['name']}"
    if source.startswith("./"):
        source = source[2:]
    return REPO / source


def source_label(path: Path) -> str:
    if not path.is_file():
        return "fehlt"
    text = path.read_text(encoding="utf-8", errors="ignore")
    if "Dieser Werkstatt-Prompt verdichtet das Plugin" in text or "Ich bin der kompakte Arbeitsmodus" in text:
        return "auto"
    return "lokal"


def main() -> int:
    DOCS.mkdir(exist_ok=True)
    plugins = json.loads(MARKETPLACE.read_text(encoding="utf-8"))["plugins"]
    ok = 0
    lines = [
        "# Werkstatt- und Schnellstart-Coverage",
        "",
        "Diese Tabelle zeigt, ob jedes Plugin eine ausführliche Werkstatt-Datei und eine kompakte Schnellstart-Datei besitzt. Werkstatt und Schnellstart werden ausschließlich als Markdown-Direkt-Download angeboten (raw.githubusercontent.com), nicht mehr als ZIP.",
        "",
        "| Plugin | Werkstatt-Datei | Werkstatt-Quelle | Werkstatt-Direct-Download | Schnellstart-Datei | Schnellstart-Quelle | Schnellstart-Direct-Download |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for plugin in plugins:
        name = plugin["name"]
        directory = plugin_dir(plugin)
        stem = prompt_stem(name)
        werkstatt = directory / f"{stem}-werkstatt.md"
        schnellstart = directory / f"{stem}-schnellstart.md"
        if werkstatt.is_file() and schnellstart.is_file():
            ok += 1
        werkstatt_rel = werkstatt.relative_to(REPO)
        schnellstart_rel = schnellstart.relative_to(REPO)
        werkstatt_raw = f"{RAW_BASE}/{werkstatt_rel.as_posix()}"
        schnellstart_raw = f"{RAW_BASE}/{schnellstart_rel.as_posix()}"
        lines.append(
            f"| `{name}` | [`{werkstatt.name}`](../{werkstatt_rel.as_posix()}) | {source_label(werkstatt)} | "
            f"[Markdown]({werkstatt_raw}) | "
            f"[`{schnellstart.name}`](../{schnellstart_rel.as_posix()}) | {source_label(schnellstart)} | "
            f"[Markdown]({schnellstart_raw}) |"
        )
    percent = 100 if not plugins else round(ok * 100 / len(plugins), 2)
    lines += [
        "",
        f"Gesamtcoverage: {ok} von {len(plugins)} Plugins, also {percent} Prozent.",
        "",
    ]
    (DOCS / "werkstatt-und-schnellstart-coverage.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Coverage geschrieben: {ok}/{len(plugins)} Plugins")
    return 0 if ok == len(plugins) else 1


if __name__ == "__main__":
    raise SystemExit(main())
