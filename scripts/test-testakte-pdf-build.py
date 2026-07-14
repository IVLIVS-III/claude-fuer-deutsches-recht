#!/usr/bin/env python3
"""Regressionstests fuer strenge und transaktionale Akten-PDF-Erzeugung."""

from __future__ import annotations

import importlib.util
import hashlib
import io
import sys
import tempfile
from pathlib import Path
import zipfile

from odf.opendocument import OpenDocumentText
from odf.text import H, P


SCRIPTS = Path(__file__).resolve().parent


def load_module(filename: str, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, SCRIPTS / filename)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


G = load_module("build-testakte-gesamt-pdf.py", "test_build_testakte_gesamt_pdf")
E = load_module("build-testakten-einzelpdf-zips.py", "test_build_testakten_einzelpdf_zips")
W = load_module("build-testakten-release-zips.py", "test_build_testakten_release_zips")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="testakte-pdf-") as tmp:
        root = Path(tmp)
        odt = root / "akte.odt"
        doc = OpenDocumentText()
        doc.text.addElement(H(outlinelevel=1, text="Sachstand"))
        doc.text.addElement(P(text="Der Antrag liegt vollstaendig vor."))
        doc.save(str(odt))

        flowables = E.odt_to_flowables(odt)
        require(len(flowables) == 2, "ODT-Ueberschrift und Absatz muessen gerendert werden")

        broken = root / "defekt.docx"
        broken.write_bytes(b"kein Office-Dokument")
        try:
            E.render_document_pdf(broken, root)
        except E.G.DocumentRenderError:
            pass
        else:
            raise AssertionError("Defekte DOCX-Datei darf kein Platzhalter-PDF erzeugen")
        broken.unlink()

        pdf_data = E.render_document_pdf(odt, root)
        require(pdf_data is not None and pdf_data.startswith(b"%PDF-"), "ODT muss ein PDF ergeben")
        require(len(list(G.PdfReader(io.BytesIO(pdf_data)).pages)) >= 1, "PDF braucht mindestens eine Seite")

        dist = root / "dist"
        dist.mkdir()
        archive, count = E.build_single(root, dist)
        require(count == 1, "die ODT-Datei muss als Einzel-PDF im ZIP landen")
        first_hash = hashlib.sha256(archive.read_bytes()).hexdigest()
        archive, _ = E.build_single(root, dist)
        second_hash = hashlib.sha256(archive.read_bytes()).hexdigest()
        require(first_hash == second_hash, "wiederholte ZIP-Bauten muessen byteidentisch sein")
        with zipfile.ZipFile(archive) as built:
            require(
                all(info.date_time == E.ZIP_TIMESTAMP for info in built.infolist()),
                "ZIP-Eintraege brauchen stabile Zeitstempel",
            )

        working_case = root / "arbeitsakte"
        working_case.mkdir()
        (working_case / "01_sachstand.txt").write_text(
            "Antrag und Bescheid liegen vor.\n", encoding="utf-8"
        )
        working_dist = root / "working-dist"
        working_dist.mkdir()
        working_archive, working_count = W.build_single(working_case, working_dist)
        require(working_count == 1, "Arbeitsakten-ZIP muss die Unterlage enthalten")
        first_working_hash = hashlib.sha256(working_archive.read_bytes()).hexdigest()
        working_archive, _ = W.build_single(working_case, working_dist)
        second_working_hash = hashlib.sha256(working_archive.read_bytes()).hexdigest()
        require(
            first_working_hash == second_working_hash,
            "Arbeitsakten-ZIPs müssen bei gleichem Bestand byteidentisch sein",
        )
        with zipfile.ZipFile(working_archive) as built:
            require(
                all(info.date_time == W.ZIP_TIMESTAMP for info in built.infolist()),
                "Arbeitsakten-ZIPs brauchen stabile Zeitstempel",
            )

    print("test-testakte-pdf-build OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
