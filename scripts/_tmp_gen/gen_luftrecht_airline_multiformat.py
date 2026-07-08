#!/usr/bin/env python3
"""Multi-Format-Ordner fuer luftrecht-airline-insolvenz-flugzeugpfand-flughafen."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from aktenbau import make_docx, make_eml, make_md_email, make_csv, make_xlsx, make_jpg, TESTAKTEN

SLUG = "luftrecht-airline-insolvenz-flugzeugpfand-flughafen"
D = TESTAKTEN / SLUG

mails = [
    ("01_grounding_mitteilung_lba", "aufsicht@lba.bund.de", "ops@westair-regional.de",
     "Grounding D-AWRB - Bremssystemfehler", "Wed, 08 Oct 2025 07:15:00 +0200",
     "Sehr geehrte Damen und Herren,\n\naufgrund eines wiederholt aufgetretenen Bremssystemfehlers wird das "
     "Luftfahrzeug D-AWRB mit sofortiger Wirkung fuer den Flugbetrieb gesperrt (Grounding), bis der Mangel "
     "nachweislich behoben ist.\n\nMit freundlichen Gruessen\nLuftfahrt-Bundesamt, Referat Lufttuechtigkeit"),
    ("02_interne_reaktion_geschaeftsleitung", "gf@westair-regional.de", "ops@westair-regional.de",
     "AW: Grounding D-AWRB - weiteres Vorgehen", "Wed, 08 Oct 2025 11:40:00 +0200",
     "Liebe Kolleginnen und Kollegen,\n\nangesichts der angespannten Liquiditaetslage koennen wir die Reparatur "
     "(geschaetzt EUR 65.000,00) derzeit nicht kurzfristig finanzieren. Bitte prueft Zwischenfinanzierung "
     "ueber die Hausbank.\n\nViele Gruesse\nGeschaeftsfuehrung"),
    ("03_mahnung_flughafen_1", "forderungen@flughafen-dortmund.de", "buchhaltung@westair-regional.de",
     "1. Mahnung Landeentgelte September 2025", "Mon, 13 Oct 2025 09:00:00 +0200",
     "Sehr geehrte Damen und Herren,\n\ndie Rechnung ueber Landeentgelte September 2025 in Hoehe von "
     "EUR 6.552,00 ist ueberfaellig. Wir bitten um Ausgleich binnen 10 Tagen.\n\nMit freundlichen Gruessen\n"
     "Flughafen Dortmund GmbH, Forderungsmanagement"),
    ("04_ruecksprache_kaltenborn_wessels", "h.kaltenborn@kaltenborn-rae.de", "a.wessels@flughafen-dortmund.de",
     "Ruecksprache Pfandrecht D-AWRB und Insolvenzeroeffnung", "Mon, 24 Nov 2025 15:20:00 +0100",
     "Sehr geehrte Frau Dr. Wessels,\n\nwie telefonisch besprochen bitte ich um Uebersendung einer aktuellen "
     "Forderungsaufstellung sowie um Mitteilung, ob eine einvernehmliche Loesung mit der Leasinggeberin "
     "moeglich erscheint.\n\nMit freundlichen Gruessen\nDr. Henning Kaltenborn"),
    ("05_vergleichsangebot_afs", "legal@airbusfs.ie", "h.kaltenborn@kaltenborn-rae.de",
     "Vergleichsangebot Herausgabe D-AWRB", "Fri, 09 Jan 2026 10:00:00 +0100",
     "Dear Dr. Kaltenborn,\n\nwe are prepared to settle the outstanding airport charges directly with "
     "Dortmund Airport in order to obtain release of MSN 6217. Please confirm the current outstanding amount.\n\n"
     "Best regards\nAirbus Financial Services Legal Team"),
]
for fname, frm, to, subj, date, body in mails:
    make_md_email(D / "emails" / f"{fname}.md", frm, to, subj, date, body)
    # eml/ folder already exists with earlier files; add ours there too
    make_eml(D / "eml" / f"{fname}.eml", frm, to, subj, date, body)

# csv/
make_csv(
    D / "csv" / "standgebuehren_verlauf.csv",
    ["Datum", "Standtag_Nr", "Gebuehr_EUR", "Kumuliert_EUR"],
    [
        ["2025-10-08", "1", "0,00", "0,00"],
        ["2025-10-10", "3", "183,00", "183,00"],
        ["2025-11-01", "25", "183,00", "4.209,00"],
        ["2025-12-01", "55", "183,00", "10.065,00"],
        ["2026-01-01", "86", "183,00", "15.738,00"],
        ["2026-01-15", "100", "183,00", "18.300,00"],
    ],
)
make_csv(
    D / "csv" / "flottenuebersicht_westair.csv",
    ["Kennzeichen", "Muster", "MSN", "Status"],
    [
        ["D-AWRA", "Airbus A320-214", "6104", "im Flugbetrieb (Leasing andere Gesellschaft)"],
        ["D-AWRB", "Airbus A320-214", "6217", "Grounding seit 08.10.2025, Streitobjekt"],
        ["D-AWRC", "Airbus A319-112", "3355", "im Flugbetrieb"],
    ],
)

# xlsx/
make_xlsx(
    D / "xlsx" / "forderungsuebersicht_flughafen.xlsx",
    "Forderungen",
    ["Position", "Betrag (EUR)", "Status"],
    [
        ["Landeentgelte Aug/Sep 2025", "14.414,40", "streitig, Anfechtungspruefung offen"],
        ["Standgebuehren Okt 2025-Jan 2026", "21.228,00", "im Vergleich beruecksichtigt"],
        ["Mahngebuehren", "120,00", "im Vergleich beruecksichtigt"],
        ["Vergleichsbetrag (LG Frankfurt 15.01.2026)", "29.008,00", "gezahlt"],
    ],
    title="Forderungsuebersicht Flughafen Dortmund ./. WestAir/AFS",
)

# jpg/
make_jpg(
    D / "jpg" / "d-awrb_vorfeld_c_stellplatz_14.jpg",
    "Foto: D-AWRB, Vorfeld C, Stellplatz 14",
    [
        "Aufnahmedatum: 12.11.2025",
        "Grounding seit 08.10.2025",
        "Bremssystemfehler dokumentiert",
        "Fotodokumentation im Auftrag Insolvenzverwalter",
    ],
)

# pdfs/ real reportlab PDF
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

pdf_path = D / "pdfs" / "vergleichsbeschluss_lg_frankfurt_original.pdf"
pdf_path.parent.mkdir(parents=True, exist_ok=True)
c = canvas.Canvas(str(pdf_path), pagesize=A4)
width, height = A4
c.setFont("Helvetica-Bold", 14)
c.drawString(2*cm, height-2*cm, "Landgericht Frankfurt am Main - Az. 3-08 O 66/26")
c.setFont("Helvetica", 10)
lines = [
    "Vergleichsbeschluss vom 15.01.2026 (Scan Original)",
    "",
    "Airbus Financial Services (Dublin) DAC ./. Flughafen Dortmund GmbH",
    "",
    "Die Beklagte gibt das Luftfahrzeug D-AWRB Zug um Zug gegen Zahlung von",
    "EUR 29.008,00 frei. Kosten des Rechtsstreits gegeneinander aufgehoben.",
    "",
    "Frankfurt am Main, den 15.01.2026",
]
y = height - 3*cm
for line in lines:
    c.drawString(2*cm, y, line)
    y -= 0.7*cm
c.showPage()
c.save()

print("Multiformat Luftrecht/Airline erzeugt.")
