#!/usr/bin/env python3
"""Multi-Format-Ordner fuer lumen-studios-insolvenz-strafverfahren."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from aktenbau import make_docx, make_eml, make_md_email, make_csv, make_xlsx, make_jpg, TESTAKTEN

SLUG = "lumen-studios-insolvenz-strafverfahren"
D = TESTAKTEN / SLUG

mails = [
    ("01_weber_an_richter_dringlichkeit", "f.weber@lumen-studios.de", "s.richter@lumen-studios.de",
     "Wir muessen jetzt handeln", "Mon, 18 Mar 2024 20:14:00 +0100",
     "Sebastian,\n\nich habe heute nochmal mit Klingmann telefoniert. Er sagt, wir sind schon laenger "
     "zahlungsunfaehig. Ich mache mir grosse Sorgen wegen persoenlicher Haftung. Bitte lass uns morgen "
     "in Ruhe reden.\n\nFlorian"),
    ("02_richter_antwort_zuversicht", "s.richter@lumen-studios.de", "f.weber@lumen-studios.de",
     "AW: Wir muessen jetzt handeln", "Tue, 19 Mar 2024 08:03:00 +0100",
     "Florian,\n\nich bin da entspannter als du. Wir haben zwei grosse Angebote in der Pipeline, die im "
     "Sommer kommen sollen. Lass uns nicht ueberstuerzt einen Insolvenzantrag stellen, das schadet uns bei "
     "den Kunden.\n\nSebastian"),
    ("03_weber_an_klingmann_zugriff", "f.weber@lumen-studios.de", "r.klingmann@klingmann-fuchs.de",
     "Zugriff auf Kontobewegungen", "Wed, 27 Mar 2024 09:44:00 +0100",
     "Sehr geehrter Herr Klingmann,\n\nkoennen Sie mir helfen, Einsicht in die aktuellen Kontobewegungen "
     "zu bekommen? Ich habe keinen eigenen Online-Banking-Zugang, nur Herr Richter.\n\nMit freundlichen "
     "Gruessen\nFlorian Weber"),
    ("04_vermieter_kuendigungsandrohung", "hausverwaltung@goethestrasse18.de", "s.richter@lumen-studios.de",
     "Mahnung Miete April 2024 und Kuendigungsandrohung", "Fri, 12 Apr 2024 10:00:00 +0200",
     "Sehr geehrter Herr Richter,\n\ndie Miete fuer April 2024 in Hoehe von EUR 3.200,00 ist nicht "
     "eingegangen. Bei erneutem Zahlungsverzug sehen wir uns zur fristlosen Kuendigung des Mietverhaeltnisses "
     "gezwungen.\n\nMit freundlichen Gruessen\nHausverwaltung Goethestrasse 18"),
    ("05_weber_ankuendigung_eigenantrag", "f.weber@lumen-studios.de", "s.richter@lumen-studios.de",
     "Ich stelle den Insolvenzantrag", "Tue, 21 May 2024 19:30:00 +0200",
     "Sebastian,\n\nich habe lange gewartet, aber du reagierst nicht mehr auf meine Nachrichten. Ich werde "
     "morgen einen Eigenantrag beim Amtsgericht stellen, um weiteren Schaden und persoenliche Haftung zu "
     "vermeiden. Es tut mir leid, dass es so weit kommen musste.\n\nFlorian"),
]
for fname, frm, to, subj, date, body in mails:
    make_md_email(D / "emails" / f"{fname}.md", frm, to, subj, date, body)
    make_eml(D / "eml" / f"{fname}.eml", frm, to, subj, date, body)

# csv/
make_csv(
    D / "csv" / "glaeubigerliste_insolvenztabelle_auszug.csv",
    ["Glaeubiger", "Forderung (EUR)", "Rechtsgrund"],
    [
        ["Finanzamt Frankfurt am Main III", "24.680,00", "USt/LSt-Rueckstaende"],
        ["Deutsche Rentenversicherung Hessen", "16.520,00", "SV-Beitraege"],
        ["Videoequipment Rentals Rhein-Main GmbH", "8.940,00", "Mietausstand"],
        ["Hausverwaltung Goethestrasse 18", "9.600,00", "Mietrueckstand 3 Monate"],
        ["Diverse Freelancer/Kreative", "12.400,00", "offene Honorare"],
    ],
)
make_csv(
    D / "csv" / "umsatzentwicklung_2022_2024.csv",
    ["Jahr/Quartal", "Umsatz (EUR)"],
    [
        ["2022 gesamt", "410.000,00"],
        ["2023 Q1", "95.000,00"],
        ["2023 Q2", "88.000,00"],
        ["2023 Q3", "61.000,00"],
        ["2023 Q4", "48.200,00"],
        ["2024 Q1", "31.500,00"],
    ],
)

# xlsx/
make_xlsx(
    D / "xlsx" / "deckungsluecke_monatsverlauf.xlsx",
    "Deckungsluecke",
    ["Monat", "Liquide Mittel (EUR)", "Faellige Verbindlichkeiten (EUR)"],
    [
        ["2023-12", "22.100,00", "168.900,00"],
        ["2024-01", "14.600,00", "175.200,00"],
        ["2024-02", "9.800,00", "182.400,00"],
        ["2024-03", "7.100,00", "189.700,00"],
        ["2024-04", "5.900,00", "194.300,00"],
        ["2024-05", "5.482,33", "196.100,00"],
    ],
    title="Deckungsluecken-Verlauf LUMEN Studios GmbH",
)

# jpg/
make_jpg(
    D / "jpg" / "buero_goethestrasse_aussenaufnahme.jpg",
    "Foto: Buero LUMEN Studios GmbH, Goethestrasse 18",
    [
        "Aufnahme im Rahmen der Ortsbesichtigung durch IV",
        "Datum: 24.05.2024",
        "Zustand: geraeumt, Geraete teilweise sichergestellt",
    ],
)

# pdfs/ real reportlab PDF
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

pdf_path = D / "pdfs" / "urteil_ausfertigung_original.pdf"
pdf_path.parent.mkdir(parents=True, exist_ok=True)
c = canvas.Canvas(str(pdf_path), pagesize=A4)
width, height = A4
c.setFont("Helvetica-Bold", 14)
c.drawString(2*cm, height-2*cm, "Amtsgericht Frankfurt am Main - Az. 933 Cs 78/25")
c.setFont("Helvetica", 10)
lines = [
    "Urteilsausfertigung (Scan Original), verkuendet am 14.05.2025",
    "",
    "Sebastian Richter wird wegen Verletzung der Buchfuehrungspflicht",
    "gemaess Sec. 283b Abs. 1 Nr. 1, Abs. 3 iVm Sec. 283 Abs. 6 StGB",
    "zu einer Geldstrafe von 150 Tagessaetzen zu je EUR 65,00 verurteilt.",
    "",
    "Frankfurt am Main, den 14.05.2025",
]
y = height - 3*cm
for line in lines:
    c.drawString(2*cm, y, line)
    y -= 0.7*cm
c.showPage()
c.save()

print("Multiformat Lumen Studios erzeugt.")
