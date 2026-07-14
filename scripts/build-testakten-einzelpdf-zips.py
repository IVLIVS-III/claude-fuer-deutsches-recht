#!/usr/bin/env python3
"""Baut pro Testakte ein ZIP, das jede Unterlage als eigene PDF enthaelt.

Anders als das Gesamt-PDF (alles in einem Dokument) liefert dieses ZIP jede
Akte-Unterlage als separate, sauber gerenderte PDF-Datei. Original-PDFs werden
unveraendert uebernommen, alle anderen Dokumente (MD/TXT/EML/CSV/XLSX/DOCX/ODT
und Bilder) in jeweils eine eigene PDF gerendert. Die Ordnerstruktur der Akte
bleibt erhalten.

Aufruf:
  python3 scripts/build-testakten-einzelpdf-zips.py [dist]            # alle Testakten
  python3 scripts/build-testakten-einzelpdf-zips.py [dist] <name> ... # gezielt

Erzeugt:
  <dist>/testakte-<name>-einzelpdfs.zip   (pro Testakte)
  <dist>/alle-testakten-einzelpdfs.zip    (Sammel-ZIP)
"""

from __future__ import annotations

import importlib.util
import io
import sys
import zipfile
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

from testakte_einzelpdf_common import (
    COPY_EXTS,
    IMAGE_EXTS,
    document_arcname_pairs,
    ext_of,
)

SCRIPTS = Path(__file__).resolve().parent
REPO_ROOT = SCRIPTS.parent
TESTAKTEN = REPO_ROOT / "testakten"


def _load_gesamt_module():
    """Laedt das Gesamt-PDF-Skript (Dateiname mit Bindestrichen) als Modul,
    um dessen erprobte Konverter wiederzuverwenden."""
    path = SCRIPTS / "build-testakte-gesamt-pdf.py"
    spec = importlib.util.spec_from_file_location("build_testakte_gesamt_pdf", path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


G = _load_gesamt_module()
ZIP_TIMESTAMP = (1980, 1, 1, 0, 0, 0)


def write_pdf(zipf: zipfile.ZipFile, arcname: str, data: bytes) -> None:
    """Schreibt ein PDF mit stabilen Metadaten fuer reproduzierbare Archive."""
    info = zipfile.ZipInfo(arcname, ZIP_TIMESTAMP)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    zipf.writestr(info, data)


def odt_to_flowables(path: Path) -> list:
    """Rendert ODT-Text in Flowables oder bricht nachvollziehbar ab."""
    out: list = []
    try:
        from odf.opendocument import load as odf_load
        from odf.element import Element
    except ImportError:
        raise G.DocumentRenderError("odfpy ist nicht installiert")
    try:
        doc = odf_load(str(path))
    except Exception as exc:  # pragma: no cover - defekte Datei
        raise G.DocumentRenderError(f"ODT konnte nicht gelesen werden: {exc}") from exc

    def text_of(node) -> str:
        parts: list[str] = []
        for child in node.childNodes:
            if child.nodeType == child.TEXT_NODE:
                parts.append(child.data)
            elif isinstance(child, Element):
                parts.append(text_of(child))
        return "".join(parts)

    def walk(node) -> None:
        """Durchlaeuft den Baum in Dokumentreihenfolge und gibt Absaetze/
        Ueberschriften aus, sobald sie auftreten (erhaelt die Reihenfolge)."""
        for child in node.childNodes:
            if not isinstance(child, Element):
                continue
            local = child.qname[1]
            if local in ("p", "h"):
                txt = text_of(child).strip()
                if txt:
                    out.append(Paragraph(G.escape(txt), G.s_h3 if local == "h" else G.s_body))
            else:
                walk(child)

    # doc.text kann bei odfpy auf einen Whitespace-Textknoten zeigen. Der
    # Dokumentkoerper enthaelt dagegen das office:text-Element und damit auch
    # Tabellen, Listen, Absaetze und Ueberschriften in richtiger Reihenfolge.
    walk(doc.body)
    if not out:
        raise G.DocumentRenderError("ODT enthält keinen lesbaren Text")
    return out


def render_document_pdf(path: Path, testakte_dir: Path) -> bytes | None:
    """Rendert eine Einzeldatei in eine PDF und liefert die Bytes.

    Original-PDFs werden unveraendert zurueckgegeben.
    """
    ext = ext_of(path)
    if ext in COPY_EXTS:
        data = path.read_bytes()
        try:
            pages = list(G.PdfReader(io.BytesIO(data)).pages)
        except Exception as exc:
            raise G.DocumentRenderError(f"{path.name}: PDF konnte nicht gelesen werden: {exc}") from exc
        if not pages:
            raise G.DocumentRenderError(f"{path.name}: PDF enthält keine Seite")
        return data

    rel = path.relative_to(testakte_dir)
    flow: list = [Paragraph(f"<b>Datei:</b> {G.escape(str(rel))}", G.s_meta), Spacer(1, 6)]
    try:
        if ext == "md":
            rendered = G.md_to_flowables(path.read_text(encoding="utf-8", errors="strict"))
        elif ext == "txt":
            rendered = G.txt_to_flowables(path.read_text(encoding="utf-8", errors="strict"))
        elif ext == "eml":
            rendered = G.eml_to_flowables(path)
        elif ext == "csv":
            rendered = G.csv_to_flowables(path)
        elif ext == "xlsx":
            rendered = G.xlsx_to_flowables(path)
        elif ext == "docx":
            rendered = G.docx_to_flowables(path)
        elif ext == "odt":
            rendered = odt_to_flowables(path)
        elif ext in IMAGE_EXTS:
            rendered = G.image_to_flowables(path)
        else:  # pragma: no cover - durch is_einzelpdf_document ausgeschlossen
            raise G.DocumentRenderError(f"nicht unterstützter Dokumenttyp: {ext}")
    except Exception as exc:
        if isinstance(exc, G.DocumentRenderError):
            raise G.DocumentRenderError(f"{rel}: {exc}") from exc
        raise G.DocumentRenderError(f"{rel}: {type(exc).__name__}: {exc}") from exc
    if not rendered:
        raise G.DocumentRenderError(f"{rel}: Konverter lieferte keine PDF-Inhalte")
    flow.extend(rendered)

    buf = io.BytesIO()
    doc = SimpleDocTemplate(
        buf, pagesize=A4,
        leftMargin=2 * cm, rightMargin=2 * cm, topMargin=2 * cm, bottomMargin=2 * cm,
        title=f"{testakte_dir.name} — {rel}", author="Kanzleiakte",
    )
    hf = G.header_footer_factory(testakte_dir.name)
    try:
        doc.build(flow, onFirstPage=hf, onLaterPages=hf, canvasmaker=G.invariant_canvas)
        data = buf.getvalue()
        if not list(G.PdfReader(io.BytesIO(data)).pages):
            raise G.DocumentRenderError("erzeugtes PDF enthält keine Seite")
        return data
    except Exception as exc:
        if isinstance(exc, G.DocumentRenderError):
            raise
        raise G.DocumentRenderError(f"{rel}: Einzel-PDF konnte nicht gebaut werden: {exc}") from exc


def add_testakte(zipf: zipfile.ZipFile, testakte_dir: Path) -> int:
    return add_testakte_many([zipf], testakte_dir)


def add_testakte_many(zipfiles: list[zipfile.ZipFile], testakte_dir: Path) -> int:
    """Rendert jede Quelle einmal und schreibt sie in mehrere Zielarchive."""
    count = 0
    for path, arcname in document_arcname_pairs(testakte_dir):
        data = render_document_pdf(path, testakte_dir)
        if data is None:
            continue
        for zipf in zipfiles:
            write_pdf(zipf, arcname, data)
        count += 1
    return count


def build_single(testakte_dir: Path, dist: Path) -> tuple[Path, int]:
    out = dist / f"testakte-{testakte_dir.name}-einzelpdfs.zip"
    tmp = out.with_name(f".{out.name}.tmp")
    with zipfile.ZipFile(tmp, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=1) as zipf:
        count = add_testakte(zipf, testakte_dir)
    if count == 0:
        tmp.unlink(missing_ok=True)
        out.unlink(missing_ok=True)
    else:
        tmp.replace(out)
    return out, count


def _is_testakte_name(arg: str) -> bool:
    return "/" not in arg and "\\" not in arg and (TESTAKTEN / arg).is_dir()


def main() -> None:
    argv = sys.argv[1:]
    # Erstes Argument, das KEIN Testakten-Name ist, gilt als Ziel-Verzeichnis.
    dist = REPO_ROOT / "dist"
    targets: list[str] = []
    for arg in argv:
        if _is_testakte_name(arg):
            targets.append(arg)
        elif dist == REPO_ROOT / "dist":
            dist = Path(arg)
        else:
            targets.append(arg)
    dist.mkdir(parents=True, exist_ok=True)

    dirs = sorted(d for d in TESTAKTEN.iterdir() if d.is_dir())
    if targets:
        dirs = [d for d in dirs if d.name in targets]
    if not dirs:
        print("Keine Testakten gefunden.")
        return

    built: list[Path] = []
    pending: list[tuple[Path, Path]] = []
    total_pdfs = 0
    skipped: list[str] = []
    all_out = dist / "alle-testakten-einzelpdfs.zip"
    all_tmp = all_out.with_name(f".{all_out.name}.tmp")
    try:
        with zipfile.ZipFile(
            all_tmp, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=1
        ) as combined:
            for d in dirs:
                out = dist / f"testakte-{d.name}-einzelpdfs.zip"
                tmp = out.with_name(f".{out.name}.tmp")
                try:
                    with zipfile.ZipFile(
                        tmp, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=1
                    ) as individual:
                        count = add_testakte_many([individual, combined], d)
                    if count == 0:
                        tmp.unlink(missing_ok=True)
                        out.unlink(missing_ok=True)
                        skipped.append(d.name)
                        continue
                    pending.append((tmp, out))
                except Exception:
                    tmp.unlink(missing_ok=True)
                    raise
                built.append(d)
                total_pdfs += count
                print(f"Baue {out.name}: {count} PDFs")
        for tmp, out in pending:
            tmp.replace(out)
        all_tmp.replace(all_out)
    except Exception:
        all_tmp.unlink(missing_ok=True)
        for tmp, _ in pending:
            tmp.unlink(missing_ok=True)
        raise

    if skipped:
        print(f"Hinweis: {len(skipped)} Ordner ohne renderbare Unterlagen uebersprungen: {skipped[:10]}")

    print(f"Baue {all_out.name}: {total_pdfs} PDFs aus {len(built)} Testakten")
    print(f"Fertig: {len(built)} Einzel-PDF-ZIPs, {total_pdfs} PDFs")


if __name__ == "__main__":
    main()
