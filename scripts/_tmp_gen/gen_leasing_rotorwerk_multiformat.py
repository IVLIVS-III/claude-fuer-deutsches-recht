#!/usr/bin/env python3
"""Multi-Format-Ordner fuer leasingrecht-maschinenfleet-restwert-insolvenz (Rotorwerk)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from aktenbau import make_docx, make_eml, make_md_email, make_csv, make_xlsx, make_jpg, TESTAKTEN

SLUG = "leasingrecht-maschinenfleet-restwert-insolvenz"
D = TESTAKTEN / SLUG

# emails/ + eml/
mails = [
    ("01_zustimmung_auslandseinsatz_anfrage", "t.wibbeling@rotorwerk-praezision.de", "s.krohn@nordlease-bielefeld.de",
     "Anfrage Zustimmung Auslandseinsatz Objekte 11/12", "Wed, 30 Jul 2025 11:20:00 +0200",
     "Sehr geehrte Frau Krohn,\n\nwir moechten zwei Maschinen kurzfristig fuer ein Projekt unserer tschechischen "
     "Tochtergesellschaft nach Pilsen verbringen. Bitte bestaetigen Sie kurzfristig Ihr Einverstaendnis.\n\n"
     "Viele Gruesse\nThorsten Wibbeling"),
    ("02_antwort_nordlease_ausland_ausstehend", "s.krohn@nordlease-bielefeld.de", "t.wibbeling@rotorwerk-praezision.de",
     "AW: Anfrage Zustimmung Auslandseinsatz Objekte 11/12", "Fri, 01 Aug 2025 09:05:00 +0200",
     "Sehr geehrter Herr Wibbeling,\n\nein Auslandseinsatz beduerfte einer schriftlichen Nachtragsvereinbarung "
     "und ggf. einer Anpassung der Versicherung. Bitte reichen Sie zunaechst den genauen Standort und die "
     "Projektdauer ein, bevor wir zustimmen koennen.\n\nMit freundlichen Gruessen\nSabine Krohn"),
    ("03_ruecksprache_versicherung_ausland", "versicherung@allrisk-industrie.de", "s.krohn@nordlease-bielefeld.de",
     "Ruecksprache Auslandsdeckung Maschinenbruch/Transport", "Mon, 04 Aug 2025 14:30:00 +0200",
     "Sehr geehrte Frau Krohn,\n\neine Deckung fuer den Einsatz ausserhalb der Bundesrepublik Deutschland ist "
     "in der bestehenden Police nicht automatisch eingeschlossen und muesste gesondert beantragt werden.\n\n"
     "Mit freundlichen Gruessen\nAllRisk Industrieversicherung"),
    ("04_mahnung_novemberrate", "buchhaltung@nordlease-bielefeld.de", "buchhaltung@rotorwerk-praezision.de",
     "1. Mahnung Leasingrate November 2025", "Tue, 09 Dec 2025 08:00:00 +0100",
     "Sehr geehrte Damen und Herren,\n\ndie Leasingrate fuer November 2025 in Hoehe von EUR 46.680,00 ist bislang "
     "nicht bei uns eingegangen. Wir bitten um Ausgleich binnen 7 Tagen.\n\nMit freundlichen Gruessen\nBuchhaltung NordLease"),
    ("05_antwort_liquiditaetsengpass", "t.wibbeling@rotorwerk-praezision.de", "buchhaltung@nordlease-bielefeld.de",
     "AW: 1. Mahnung Leasingrate November 2025", "Thu, 11 Dec 2025 16:45:00 +0100",
     "Sehr geehrte Damen und Herren,\n\naufgrund eines vorruebergehenden Liquiditaetsengpasses bitten wir um "
     "eine Ratenzahlung ueber die naechsten drei Monate. Wir stehen im Austausch mit unserer Hausbank.\n\n"
     "Mit freundlichen Gruessen\nThorsten Wibbeling"),
]
for fname, frm, to, subj, date, body in mails:
    make_md_email(D / "emails" / f"{fname}.md", frm, to, subj, date, body)
    make_eml(D / "eml" / f"{fname}.eml", frm, to, subj, date, body)

# csv/
make_csv(
    D / "csv" / "leasingraten_zahlungsverlauf_2022_2026.csv",
    ["Monat", "Sollrate_EUR", "Zahlungseingang", "Bemerkung"],
    [
        ["2022-03", "46680,00", "puenktlich", "Vertragsbeginn"],
        ["2023-06", "46680,00", "puenktlich", ""],
        ["2024-09", "46680,00", "puenktlich", ""],
        ["2025-06", "46680,00", "puenktlich", ""],
        ["2025-09", "46680,00", "5 Tage verspaetet", "erste Auffaelligkeit"],
        ["2025-10", "46680,00", "puenktlich", ""],
        ["2025-11", "46680,00", "nicht gezahlt", "Mahnung 09.12.2025"],
        ["2025-12", "46680,00", "nicht gezahlt", "Kuendigungsandrohung"],
    ],
)
make_csv(
    D / "csv" / "objektliste_kurzuebersicht.csv",
    ["Objekt", "Seriennummer", "Standort", "Zustand"],
    [
        ["1", "HVF6-22091", "Halle A Bielefeld", "betriebsbereit"],
        ["2", "HVF6-22092", "Halle A Bielefeld", "betriebsbereit"],
        ["3", "HVF6-22093", "Halle A Bielefeld", "Softwarefehler"],
        ["4", "HVF6-22094", "Halle A Bielefeld", "Spindelschaden"],
        ["5", "HVF6-22095", "Halle B Bielefeld", "betriebsbereit"],
        ["6", "HVF6-22096", "Halle B Bielefeld", "betriebsbereit"],
        ["7", "HVF6-22097", "Halle B Bielefeld", "betriebsbereit"],
        ["8", "HVF6-22098", "Halle B Bielefeld", "Softwarefehler"],
        ["9", "HVF6-22099", "Zweigwerk Herford", "betriebsbereit"],
        ["10", "HVF6-22100", "Zweigwerk Herford", "betriebsbereit"],
        ["11", "HVF6-22101", "Pilsen/Tschechien (streitig)", "unbekannt"],
        ["12", "HVF6-22102", "Pilsen/Tschechien (streitig)", "unbekannt"],
    ],
)

# xlsx/
make_xlsx(
    D / "xlsx" / "restwert_szenarien.xlsx",
    "Szenarien",
    ["Szenario", "Erloes gesamt (EUR)", "Nachforderung NordLease (EUR)"],
    [
        ["Best Case (DEKRA-Werte voll realisiert)", "259.700,00", "160.300,00"],
        ["Realisiert (Verkauf Wester)", "258.000,00", "162.000,00"],
        ["Worst Case (Zwangsverwertung Zerschlagung)", "180.000,00", "240.000,00"],
    ],
    title="Restwert-Szenarien Objekte 1-10",
)

# jpg/
make_jpg(
    D / "jpg" / "rueckholung_halle_a_foto.jpg",
    "Foto: Rueckholung Halle A, 26.01.2026",
    [
        "Objekte 1, 2, 5, 6, 7 vor Abtransport",
        "Spedition Trescher Schwertransporte",
        "Zustand: aeusserlich unauffaellig",
        "Fotodokumentation: 14 Einzelbilder je Objekt",
    ],
)

# pdfs/ - real rendered PDF via reportlab
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

pdf_path = D / "pdfs" / "leasingvertrag_unterschriebenes_original.pdf"
pdf_path.parent.mkdir(parents=True, exist_ok=True)
c = canvas.Canvas(str(pdf_path), pagesize=A4)
width, height = A4
c.setFont("Helvetica-Bold", 14)
c.drawString(2*cm, height-2*cm, "Maschinen-Leasingvertrag Nr. NL-2022-0847 (unterschriebenes Original, Scan)")
c.setFont("Helvetica", 10)
lines = [
    "NordLease Maschinen-Leasing GmbH / Rotorwerk Praezisionstechnik GmbH",
    "",
    "Vertragsgegenstand: 12 CNC-Bearbeitungszentren Haas VF-6SS",
    "Grundmietzeit: 60 Monate ab 01.03.2022",
    "Monatliche Gesamtrate: EUR 46.680,00 zzgl. USt.",
    "Kalkulierter Restwert gesamt: EUR 504.000,00",
    "",
    "Unterschrieben am 24.02.2022 in Bielefeld.",
    "",
    "gez. Sabine Krohn (NordLease)          gez. Thorsten Wibbeling (Rotorwerk)",
]
y = height - 3*cm
for line in lines:
    c.drawString(2*cm, y, line)
    y -= 0.7*cm
c.showPage()
c.save()

print("Multiformat Leasing/Rotorwerk erzeugt.")
