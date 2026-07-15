#!/usr/bin/env python3
"""Validiert zentrale Übersichtsangaben gegen Marketplace und Aktenbestand."""

from __future__ import annotations

import json
import re
from pathlib import Path

from testakte_zip_common import working_dump_flat_pairs


REPO = Path(__file__).resolve().parent.parent
PLUGIN_META_DIR = ".cla" + "ude-plugin"
MARKETPLACE = REPO / PLUGIN_META_DIR / "marketplace.json"
SKIP_TESTAKTEN = {"formatvorlagen-paradebeispiele", "megaprompts"}


def load_marketplace() -> dict:
    return json.loads(MARKETPLACE.read_text(encoding="utf-8"))


def plugin_source(plugin: dict) -> Path:
    source = plugin.get("source") or f"./{plugin['name']}"
    return REPO / source.removeprefix("./")


def count_values(marketplace: dict) -> dict[str, int | str]:
    plugins = marketplace["plugins"]
    skill_files = []
    pluginlocal_testakten = []
    for plugin in plugins:
        directory = plugin_source(plugin)
        skill_files.extend((directory / "skills").glob("*/SKILL.md"))
        testakte = directory / "testakte"
        if testakte.is_dir() and working_dump_flat_pairs(testakte, include_gesamt_pdf=False):
            pluginlocal_testakten.append(testakte)

    central_testakten = []
    root = REPO / "testakten"
    if root.is_dir():
        central_testakten = [
            child
            for child in root.iterdir()
            if child.is_dir() and child.name not in SKIP_TESTAKTEN
        ]

    return {
        "plugins": len(plugins),
        "skills": len(skill_files),
        "central_testakten": len(central_testakten),
        "testakten": len(central_testakten) + len(pluginlocal_testakten),
        "version": f"v{marketplace['version']}",
    }


def require(pattern: str, text: str, label: str) -> re.Match[str]:
    match = re.search(pattern, text, re.MULTILINE)
    if not match:
        raise AssertionError(f"{label}: Angabe fehlt")
    return match


def check_root_readme(values: dict[str, int | str]) -> list[str]:
    readme = (REPO / "README.md").read_text(encoding="utf-8")
    errors: list[str] = []

    plugin_count = int(require(r"\| \*\*Plugins\*\* \| (\d+)\b", readme, "README Plugins").group(1))
    if plugin_count != values["plugins"]:
        errors.append(f"README Plugins: {plugin_count} statt {values['plugins']}")

    skill_count = int(require(r"\| \*\*Skills \(SKILL\.md\)\*\* \| (\d+)\b", readme, "README Skills").group(1))
    if skill_count != values["skills"]:
        errors.append(f"README Skills: {skill_count} statt {values['skills']}")

    testakten = require(
        r"\| \*\*Testakten\*\* \| (\d+) zentral / (\d+) gesamt \|",
        readme,
        "README Testakten",
    )
    central = int(testakten.group(1))
    total = int(testakten.group(2))
    if central != values["central_testakten"] or total != values["testakten"]:
        errors.append(
            "README Testakten: "
            f"{central} zentral / {total} gesamt statt "
            f"{values['central_testakten']} zentral / {values['testakten']} gesamt"
        )

    version = require(
        r"\| \*\*Plugin-Version / Arbeitsstand\*\* \| `(v\d+\.\d+\.\d+)`",
        readme,
        "README Version",
    ).group(1)
    if version != values["version"]:
        errors.append(f"README Version: {version} statt {values['version']}")

    return errors


def check_generated_overviews(values: dict[str, int | str]) -> list[str]:
    errors: list[str] = []

    skills = (REPO / "SKILLS.md").read_text(encoding="utf-8")
    skills_match = require(
        r"Gesamtübersicht aller \*\*(\d+) Skills\*\* in \*\*(\d+) Plugins\*\*",
        skills,
        "SKILLS Kopf",
    )
    if int(skills_match.group(1)) != values["skills"]:
        errors.append(f"SKILLS Skills: {skills_match.group(1)} statt {values['skills']}")
    if int(skills_match.group(2)) != values["plugins"]:
        errors.append(f"SKILLS Plugins: {skills_match.group(2)} statt {values['plugins']}")
    skills_version = require(r"Stand: `(v\d+\.\d+\.\d+)`", skills, "SKILLS Version").group(1)
    if skills_version != values["version"]:
        errors.append(f"SKILLS Version: {skills_version} statt {values['version']}")

    skills_index = (REPO / "skills-index" / "README.md").read_text(encoding="utf-8")
    index_version = require(r"Stand: `(v\d+\.\d+\.\d+)`", skills_index, "Skills-Index Version").group(1)
    if index_version != values["version"]:
        errors.append(f"Skills-Index Version: {index_version} statt {values['version']}")

    asset_index = (REPO / "ASSET_INDEX.md").read_text(encoding="utf-8")
    asset_version = require(r"Stand: (v\d+\.\d+\.\d+),", asset_index, "Asset-Index Version").group(1)
    if asset_version != values["version"]:
        errors.append(f"Asset-Index Version: {asset_version} statt {values['version']}")

    testakten = (REPO / "testakten" / "README.md").read_text(encoding="utf-8")
    testakten_match = require(
        r"Stand (v\d+\.\d+\.\d+): (\d+) zentrale Testakten",
        testakten,
        "Testakten-README Stand",
    )
    if testakten_match.group(1) != values["version"]:
        errors.append(f"Testakten-README Version: {testakten_match.group(1)} statt {values['version']}")
    if int(testakten_match.group(2)) != values["central_testakten"]:
        errors.append(
            "Testakten-README Zählung: "
            f"{testakten_match.group(2)} statt {values['central_testakten']}"
        )

    return errors


def main() -> int:
    values = count_values(load_marketplace())
    errors = check_root_readme(values) + check_generated_overviews(values)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(
        "validate-root-readme-overview OK "
        f"({values['plugins']} Plugins, {values['skills']} Skills, "
        f"{values['central_testakten']} zentrale Testakten, Stand {values['version']})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
