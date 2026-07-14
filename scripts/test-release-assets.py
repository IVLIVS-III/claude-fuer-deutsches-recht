#!/usr/bin/env python3
"""Regressionstest für Asset-Auswahl, Streaming-Hashes und Wiederaufnahme."""

from __future__ import annotations

import importlib.util
import os
import subprocess
import sys
import tempfile
from pathlib import Path
import zipfile

from release_asset_common import expected_asset_metadata, read_checksums, release_assets, sha256_file


UPLOAD_SCRIPT = Path(__file__).resolve().parent / "upload-release-assets.py"
SPEC = importlib.util.spec_from_file_location("upload_release_assets", UPLOAD_SCRIPT)
assert SPEC and SPEC.loader
U = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = U
SPEC.loader.exec_module(U)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="release-assets-") as tmp:
        dist = Path(tmp)
        with zipfile.ZipFile(dist / "plugin.zip", "w", zipfile.ZIP_DEFLATED) as archive:
            archive.writestr("README.md", "Inhalt")
        (dist / "hinweis.md").write_text("Direktdatei\n", encoding="utf-8")
        (dist / "marketplace.json").write_text('{"plugins": []}\n', encoding="utf-8")
        (dist / "intern.txt").write_text("kein Release-Asset\n", encoding="utf-8")

        result = subprocess.run(
            [sys.executable, str(Path(__file__).resolve().parent / "build-release-checksums.py"), str(dist)],
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        require(result.returncode == 0, result.stderr)
        names = [path.name for path in release_assets(dist)]
        require(
            names == ["checksums-sha256.txt", "hinweis.md", "marketplace.json", "plugin.zip"],
            f"unerwartete Asset-Auswahl: {names}",
        )
        checksums = read_checksums(dist / "checksums-sha256.txt")
        require("intern.txt" not in checksums, "interne Textdatei darf nicht in der Prüfsummenliste stehen")
        require(checksums["plugin.zip"] == sha256_file(dist / "plugin.zip"), "ZIP-Hash stimmt nicht")

        metadata = expected_asset_metadata(dist)
        local = metadata["plugin.zip"]
        require(
            U.same_asset(local, {"state": "uploaded", "size": local["size"], "digest": local["digest"]}),
            "identisches Remote-Asset muss übersprungen werden",
        )
        require(
            not U.same_asset(local, {"state": "uploaded", "size": local["size"], "digest": "sha256:" + "0" * 64}),
            "abweichender Hash muss einen Upload auslösen",
        )

        checksum_mtime = (dist / "checksums-sha256.txt").stat().st_mtime_ns
        newer = checksum_mtime + 1_000_000_000
        os.utime(dist / "plugin.zip", ns=(newer, newer))
        try:
            expected_asset_metadata(dist)
        except ValueError as exc:
            require("Prüfsummen erneut erzeugen" in str(exc), "veraltete Prüfsummen müssen auffallen")
        else:
            raise AssertionError("nachträglich geändertes Asset darf nicht akzeptiert werden")

    print("test-release-assets OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
