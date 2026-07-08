#!/usr/bin/env python3
"""Multi-Format-Ordner-Ergaenzung fuer insolvenz-asset-deal-chaincortex-ai-berlin."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from aktenbau import make_docx, make_eml, make_md_email, make_csv, make_xlsx, make_jpg, TESTAKTEN

SLUG = "insolvenz-asset-deal-chaincortex-ai-berlin"
D = TESTAKTEN / SLUG

mails = [
    ("06_treuhandkonto_zahlungsbestaetigung", "notariat@saegeberg-berlin.de", "m.reuter@vorberg-steinhausen.de",
     "Kaufpreiszahlung Voracis Ventures - Treuhandkonto", "Mon, 06 Jul 2026 09:12:00 +0200",
     "Sehr geehrter Herr Reuter,\n\nhiermit bestaetige ich den Eingang der ersten Kaufpreisrate in Hoehe von "
     "EUR 240.000,00 auf dem Notaranderkonto. Die Freigabe erfolgt vereinbarungsgemaess nach Vorliegen der "
     "Zustimmung des Glaeubigerausschusses.\n\nMit freundlichen Gruessen\nDr. Roderich Saegeberg\nNotariat Saegeberg"),
    ("07_widerspruch_arbeitnehmerin_uebermittlung", "m.reuter@vorberg-steinhausen.de", "kanzlei@arbeitsrecht-mitte-berlin.de",
     "Widerspruch Frau Kettlitz gegen Betriebsuebergang", "Wed, 08 Jul 2026 11:40:00 +0200",
     "Sehr geehrte Kolleginnen und Kollegen,\n\nanbei erhalten Sie den Widerspruch unserer Mandantin, Frau Nadine "
     "Kettlitz, gegen den Uebergang ihres Arbeitsverhaeltnisses auf die Voracis Ventures GmbH nach Sec. 613a Abs. 6 BGB. "
     "Wir bitten um Bestaetigung des Fortbestehens des Arbeitsverhaeltnisses mit der Insolvenzschuldnerin.\n\n"
     "Mit freundlichen Gruessen\nRA Mathis Reuter"),
    ("08_it-gutachter_ruecksprache_gpl", "dr.hemauer@it-forensik-muenchen.de", "m.reuter@vorberg-steinhausen.de",
     "Rueckfrage Lizenzkonflikt Compliance-Engine", "Fri, 10 Jul 2026 14:05:00 +0200",
     "Sehr geehrter Herr Reuter,\n\nbei der Code-Analyse der Compliance-Engine ist eine eingebundene Bibliothek "
     "unter GPLv3 aufgefallen, die mit der proprietaeren Lizenzierung des Produkts kollidiert. Ich werde dies in "
     "meinem Gutachten naeher darstellen und Handlungsoptionen skizzieren.\n\nMit freundlichen Gruessen\n"
     "Dr. Elias Hemauer\nIT-Forensik Muenchen"),
    ("09_kaeuferin_reklamation_softwarefehler", "c.hennings@voracis-ventures.de", "m.reuter@vorberg-steinhausen.de",
     "Mangelanzeige Compliance-Engine - dringend", "Mon, 13 Jul 2026 08:55:00 +0200",
     "Sehr geehrter Herr Dr. Vorberg, sehr geehrter Herr Reuter,\n\nunsere Entwicklungsabteilung hat festgestellt, "
     "dass die uebernommene Compliance-Engine eine ungeklaerte Lizenzabhaengigkeit enthaelt, die im Data Room nicht "
     "offengelegt wurde. Wir behalten uns Gewaehrleistungsansprueche nach Ziffer 9 des APA ausdruecklich vor.\n\n"
     "Mit freundlichen Gruessen\nDr. Carlotta Hennings\nGeschaeftsfuehrerin Voracis Ventures GmbH"),
    ("10_iv_antwort_gewaehrleistung_verhandlung", "m.reuter@vorberg-steinhausen.de", "c.hennings@voracis-ventures.de",
     "AW: Mangelanzeige Compliance-Engine - dringend", "Wed, 15 Jul 2026 16:20:00 +0200",
     "Sehr geehrte Frau Dr. Hennings,\n\nwir nehmen Ihre Mangelanzeige zur Kenntnis. Der Insolvenzverwalter haftet "
     "aus der Masse gemaess Ziffer 9.4 APA nur beschraenkt. Wir schlagen eine einvernehmliche Loesung durch "
     "Reduzierung des zurueckbehaltenen Retention-Betrags vor und bitten um ein Gespraech in der kommenden Woche.\n\n"
     "Mit freundlichen Gruessen\nRA Mathis Reuter"),
]
for fname, frm, to, subj, date, body in mails:
    make_md_email(D / "emails" / f"{fname}.md", frm, to, subj, date, body)
    make_eml(D / "eml" / f"{fname}.eml", frm, to, subj, date, body)

# csv/
make_csv(
    D / "csv" / "kaufpreisraten_zahlungsplan.csv",
    ["Rate", "Faelligkeit", "Betrag (EUR)", "Status"],
    [
        ["1. Rate (Signing)", "06.07.2026", "240.000,00", "eingegangen"],
        ["2. Rate (Closing)", "01.08.2026", "120.000,00", "offen"],
        ["Retention (12 Monate)", "01.07.2027", "40.000,00", "einbehalten Notaranderkonto"],
    ],
)

# xlsx/
make_xlsx(
    D / "xlsx" / "massekostenkalkulation_nach_closing.xlsx",
    "Massekosten",
    ["Position", "Betrag (EUR)"],
    [
        ["Kaufpreis gesamt", "400.000,00"],
        ["Verfahrenskosten IV-Verguetung", "38.500,00"],
        ["Sachverstaendigenkosten (IT-Gutachten)", "6.200,00"],
        ["Notarkosten Treuhandabwicklung", "3.100,00"],
        ["Massekostenbeitrag Sec. 171 InsO Absonderungsgut", "0,00"],
        ["Verteilbare Masse (vorlaeufig)", "352.200,00"],
    ],
    title="Massekostenkalkulation ChainCortex nach Closing",
)

# jpg/
make_jpg(
    D / "jpg" / "closing_unterzeichnung_notariat.jpg",
    "Foto: Unterzeichnung APA im Notariat Saegeberg",
    [
        "Datum: 01.07.2026",
        "Anwesend: RA Dr. Vorberg, Dr. Hennings, Notar Dr. Saegeberg",
        "Ort: Notariat Saegeberg, Berlin",
    ],
)

# pdfs/ real reportlab PDF
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

pdf_path = D / "pdfs" / "schlussbericht_insolvenzverwalter_auszug.pdf"
pdf_path.parent.mkdir(parents=True, exist_ok=True)
c = canvas.Canvas(str(pdf_path), pagesize=A4)
width, height = A4
c.setFont("Helvetica-Bold", 14)
c.drawString(2*cm, height-2*cm, "AG Charlottenburg - Az. 36 IN 1342/26")
c.setFont("Helvetica", 10)
lines = [
    "Schlussbericht des Insolvenzverwalters (Auszug, Scan)",
    "",
    "ChainCortex AI GmbH i.I. - RA Dr. Konrad Vorberg",
    "",
    "Der Asset Deal mit der Voracis Ventures GmbH wurde am 01.07.2026",
    "vollzogen. Die Kaufpreiszahlung erfolgte planmaessig in zwei Raten,",
    "ein Retention-Betrag von EUR 40.000,00 wurde wegen der Gewaehr-",
    "leistungsdiskussion um die Compliance-Engine einvernehmlich reduziert",
    "einbehalten.",
    "",
    "Berlin, den 20.07.2026",
]
y = height - 3*cm
for line in lines:
    c.drawString(2*cm, y, line)
    y -= 0.7*cm
c.showPage()
c.save()

print("Multiformat ChainCortex erzeugt.")
