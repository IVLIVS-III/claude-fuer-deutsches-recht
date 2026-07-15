#!/usr/bin/env python3
"""Erzeugt Whiteboardbild und Versorgungsauskünfte der Akte."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, black
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_LEFT

PIL_BLACK = (15, 17, 21)

BASE = Path(__file__).resolve().parent.parent
JPG = BASE / "jpg"
PDFS = BASE / "pdfs"
JPG.mkdir(exist_ok=True)
PDFS.mkdir(exist_ok=True)

# JPG: Whiteboard "Vermögensübersicht"
def build_whiteboard():
    W, H = 1800, 1200
    img = Image.new("RGB", (W, H), color=(247, 246, 242))
    draw = ImageDraw.Draw(img)

    try:
        font_t = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 42)
        font_h = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
        font_r = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 26)
        font_s = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf", 20)
    except Exception:
        font_t = ImageFont.load_default()
        font_h = font_t
        font_r = font_t
        font_s = font_t

    teal = (1, 105, 111)
    muted = (122, 121, 116)
    body = PIL_BLACK

    # Header
    draw.text((60, 50), "Vermögen Frau L. Schäfer (Erbschaft 2019, Stand 31.12.2021)", fill=teal, font=font_t)
    draw.line([(60, 130), (W - 60, 130)], fill=teal, width=4)

    # Linke Spalte: Aktiva
    draw.text((60, 160), "AKTIVA", fill=teal, font=font_h)

    rows = [
        ("Mehrfamilienhaus Bamberg, Promenadestr. 14 (12 WE)", "2.795.000 EUR"),
        ("Gewerbeimmobilie Forchheim, Bayreuther Str. 88", "1.510.000 EUR"),
        ("Eigentumswohnung München, Hohenzollernstraße 47", "945.000 EUR"),
        ("Wertpapierdepot DZ Privatbank, Nr. 4119 002 71", "1.200.000 EUR"),
        ("Festgeldkonten Sparkasse Bamberg", "450.000 EUR"),
    ]
    y = 220
    for left, right in rows:
        draw.text((90, y), "- " + left, fill=body, font=font_r)
        draw.text((1380, y), right, fill=teal, font=font_r)
        y += 56

    draw.line([(60, y + 20), (W - 60, y + 20)], fill=muted, width=2)
    y += 40
    draw.text((90, y), "Summe Reinvermögen", fill=teal, font=font_h)
    draw.text((1380, y), "6.900.000 EUR", fill=teal, font=font_h)

    # Block Cashflow
    y += 110
    draw.text((60, y), "Laufende Einkommensströme (brutto, p. M.)", fill=teal, font=font_h)
    y += 60
    cf = [
        ("Mieten gesamt (3 Objekte)", "ca. 23.300 EUR"),
        ("Dividenden Depot (umgerechnet p.M.)", "ca. 4.000 EUR"),
        ("Festgelderträge (umgerechnet p. M.)", "ca. 1.000 EUR"),
    ]
    for left, right in cf:
        draw.text((90, y), "- " + left, fill=body, font=font_r)
        draw.text((1380, y), right, fill=teal, font=font_r)
        y += 50

    # Fußnote
    draw.line([(60, H - 110), (W - 60, H - 110)], fill=muted, width=1)
    draw.text((60, H - 95), "Aufnahme Erstgespräch 22.05.2021, fortgeschrieben nach Gutachten Weisbacher 18.10.2022.", fill=muted, font=font_s)
    draw.text((60, H - 65), "Hinweis Bewirtschaftungskosten ca. 35-40% des Mietaufkommens; Netto-Cashflow ca. 14.700 EUR p.M.", fill=muted, font=font_s)
    draw.text((60, H - 35), "Söll Rödelsteiner und Partner mbB, Az. 0918-2021/VA.", fill=muted, font=font_s)

    img.save(JPG / "whiteboard_vermoegen_winterstein_erbe.jpg", quality=92)


# Versorgungsauskunft des Landesamts für Finanzen
def pdf_baylff():
    doc = SimpleDocTemplate(str(PDFS / "Auskunft_BayLfF_Beamtenversorgung_22_09_2021.pdf"),
                            pagesize=A4, leftMargin=2.5*cm, rightMargin=2.5*cm,
                            topMargin=2.5*cm, bottomMargin=2.5*cm)
    styles = getSampleStyleSheet()
    teal = HexColor("#01696F")
    h1 = ParagraphStyle("H1", parent=styles["Heading1"], textColor=teal, fontSize=16, spaceAfter=12)
    h2 = ParagraphStyle("H2", parent=styles["Heading2"], textColor=black, fontSize=12, spaceAfter=8)
    body = ParagraphStyle("B", parent=styles["BodyText"], fontSize=10, leading=14, alignment=TA_LEFT)

    flow = []
    flow.append(Paragraph("Bayerisches Landesamt für Finanzen", h1))
    flow.append(Paragraph("Dienststelle Würzburg – Versorgungsausgleichsstelle", body))
    flow.append(Paragraph("Klosterstraße 8, 97070 Würzburg", body))
    flow.append(Spacer(1, 0.6*cm))
    flow.append(Paragraph("An Söll Rödelsteiner und Partner mbB", body))
    flow.append(Paragraph("Karolinenstraße 27, 90402 Nürnberg", body))
    flow.append(Spacer(1, 0.4*cm))
    flow.append(Paragraph("Würzburg, 22.09.2021", body))
    flow.append(Spacer(1, 0.6*cm))
    flow.append(Paragraph("Versorgungsausgleichsauskunft – Az. AG Nürnberg-Fürth 110 F 2418/21", h2))
    flow.append(Spacer(1, 0.2*cm))
    flow.append(Paragraph("Beamten-Nr.: BY-7029-118-1961", body))
    flow.append(Paragraph("Versicherte: Frau Leonie Schäfer geb. Winterstein, geb. 11.06.1961", body))
    flow.append(Paragraph("Status: Beamtin auf Lebenszeit, Besoldungsgruppe A 12, Stufe 11, Teilzeit 18/28 (Schweinau-Schule)", body))
    flow.append(Spacer(1, 0.3*cm))
    flow.append(Paragraph("Ehezeit nach Paragraf 3 Absatz 1 VersAusglG: 01.09.1987 bis 30.04.2021", body))
    flow.append(Spacer(1, 0.3*cm))
    flow.append(Paragraph("In der Ehezeit erworbene monatliche Versorgung (Endstand zu Ehezeitende): <b>1.850,00 EUR</b>", body))
    flow.append(Paragraph("Korrespondierender Kapitalwert: 185.000,00 EUR", body))
    flow.append(Paragraph("Vorgeschlagener Ausgleichswert: 925,00 EUR / 92.500,00 EUR Kapital", body))
    flow.append(Paragraph("Vorgeschlagene Ausgleichsform: interne Teilung gemäß Paragraf 16 VersAusglG", body))
    flow.append(Spacer(1, 0.4*cm))
    flow.append(Paragraph("Hinweis: Die Anwartschaft umfasst die zukünftige Beamtenversorgung. Die Auskunft berücksichtigt den ehezeitlichen Anteil an den Dienstbezügen sowie den Anrechnungsfaktor 0,75 für die Teilzeitbeschäftigung.", body))
    flow.append(Spacer(1, 0.6*cm))
    flow.append(Paragraph("Mit freundlichen Grüßen", body))
    flow.append(Spacer(1, 0.4*cm))
    flow.append(Paragraph("Hubertus Eschenheimer", body))
    flow.append(Paragraph("Sachgebietsleiter Versorgungsausgleich", body))

    doc.build(flow)


# Versorgungsauskunft der Bayerischen Ärzteversorgung
def pdf_bvz():
    doc = SimpleDocTemplate(str(PDFS / "Auskunft_BVZ_Bayer_Aerzteversorgung_17_08_2021.pdf"),
                            pagesize=A4, leftMargin=2.5*cm, rightMargin=2.5*cm,
                            topMargin=2.5*cm, bottomMargin=2.5*cm)
    styles = getSampleStyleSheet()
    teal = HexColor("#01696F")
    h1 = ParagraphStyle("H1", parent=styles["Heading1"], textColor=teal, fontSize=16, spaceAfter=12)
    h2 = ParagraphStyle("H2", parent=styles["Heading2"], textColor=black, fontSize=12, spaceAfter=8)
    body = ParagraphStyle("B", parent=styles["BodyText"], fontSize=10, leading=14, alignment=TA_LEFT)

    flow = []
    flow.append(Paragraph("Bayerische Versorgungskammer", h1))
    flow.append(Paragraph("Bayerische Ärzteversorgung – Abteilung Zahnärzteversorgung", body))
    flow.append(Paragraph("Denninger Straße 37, 81925 München", body))
    flow.append(Spacer(1, 0.6*cm))
    flow.append(Paragraph("Söll Rödelsteiner und Partner mbB", body))
    flow.append(Paragraph("Karolinenstraße 27, 90402 Nürnberg", body))
    flow.append(Spacer(1, 0.4*cm))
    flow.append(Paragraph("München, 17.08.2021", body))
    flow.append(Spacer(1, 0.4*cm))
    flow.append(Paragraph("Versorgungsauskunft V/3 – Az. AG Nürnberg-Fürth 110 F 2418/21", h2))
    flow.append(Paragraph("Mitglieds-Nr. 14-072 184/1958", body))
    flow.append(Spacer(1, 0.2*cm))
    flow.append(Paragraph("Versicherter: Dr. Maximilian Schäfer, geb. 03.02.1958", body))
    flow.append(Paragraph("Status: Pflichtmitglied seit 01.06.1985, durchgängig", body))
    flow.append(Paragraph("Ehezeit nach Paragraf 3 Absatz 1 VersAusglG: 01.09.1987 bis 30.04.2021", body))
    flow.append(Spacer(1, 0.4*cm))
    flow.append(Paragraph("<b>In der Ehezeit erworbene monatliche Anwartschaft: 4.127,42 EUR</b>", body))
    flow.append(Paragraph("Korrespondierender Kapitalwert: 412.853,20 EUR", body))
    flow.append(Spacer(1, 0.2*cm))
    flow.append(Paragraph("Vorgeschlagener Ausgleichswert: 2.063,71 EUR monatlich / 206.426,60 EUR Kapital", body))
    flow.append(Paragraph("Teilungskosten: 500,00 EUR (bereits in der Quote berücksichtigt)", body))
    flow.append(Paragraph("Vorgeschlagene Ausgleichsform: interne Teilung gemäß Paragraf 10 VersAusglG", body))
    flow.append(Paragraph("Neues Versorgungskonto auf den Namen der ausgleichsberechtigten Person bei der Bayerischen Ärzteversorgung.", body))
    flow.append(Spacer(1, 0.4*cm))
    flow.append(Paragraph("Die Auskunft wurde nach dem Barwertverfahren BVZ unter Berücksichtigung der Rechnungsgrundlagen 2021 erstellt.", body))
    flow.append(Spacer(1, 0.5*cm))
    flow.append(Paragraph("Mit freundlichen Grüßen", body))
    flow.append(Spacer(1, 0.4*cm))
    flow.append(Paragraph("Magdalene Röschelhof – Sachgebietsleiterin Versorgungsausgleich", body))

    doc.build(flow)


# Erbschein PDF
def pdf_erbschein():
    doc = SimpleDocTemplate(str(PDFS / "Erbschein_AG_Bamberg_02_09_2019.pdf"),
                            pagesize=A4, leftMargin=2.5*cm, rightMargin=2.5*cm,
                            topMargin=2.5*cm, bottomMargin=2.5*cm)
    styles = getSampleStyleSheet()
    teal = HexColor("#01696F")
    h1 = ParagraphStyle("H1", parent=styles["Heading1"], textColor=teal, fontSize=16, spaceAfter=12, alignment=1)
    body = ParagraphStyle("B", parent=styles["BodyText"], fontSize=11, leading=15, alignment=TA_LEFT)

    flow = []
    flow.append(Paragraph("Amtsgericht Bamberg - Nachlassgericht", h1))
    flow.append(Spacer(1, 0.4*cm))
    flow.append(Paragraph("VI 1138/19", body))
    flow.append(Spacer(1, 0.6*cm))
    flow.append(Paragraph("<b>ERBSCHEIN</b>", ParagraphStyle("center", parent=h1, fontSize=20, alignment=1)))
    flow.append(Spacer(1, 0.6*cm))
    flow.append(Paragraph("Am 14. März 2019 ist", body))
    flow.append(Spacer(1, 0.2*cm))
    flow.append(Paragraph("<b>Theodor Maximilian Winterstein</b>,", body))
    flow.append(Paragraph("geboren am 22. April 1937 in Bamberg,", body))
    flow.append(Paragraph("zuletzt wohnhaft Schönleinsplatz 8, 96047 Bamberg,", body))
    flow.append(Paragraph("verwitwet, ohne leibliche Kinder,", body))
    flow.append(Spacer(1, 0.2*cm))
    flow.append(Paragraph("verstorben.", body))
    flow.append(Spacer(1, 0.4*cm))
    flow.append(Paragraph("Aufgrund testamentarischer Verfügung vom 14. Juli 2014 (Notarin Dr. Erika Streichlen, Bamberg, UR-Nr. 781/2014), eröffnet durch Beschluss des Amtsgerichts Bamberg vom 26. April 2019, ist alleinige Erbin:", body))
    flow.append(Spacer(1, 0.4*cm))
    flow.append(Paragraph("<b>Leonie Schäfer geb. Winterstein</b>,", body))
    flow.append(Paragraph("geboren am 11. Juni 1961 in Nürnberg,", body))
    flow.append(Paragraph("wohnhaft Schweinauer Hauptstraße 144, 90441 Nürnberg.", body))
    flow.append(Spacer(1, 0.4*cm))
    flow.append(Paragraph("Diese ist Nichte des Erblassers.", body))
    flow.append(Spacer(1, 0.5*cm))
    flow.append(Paragraph("Bamberg, den 02. September 2019", body))
    flow.append(Spacer(1, 0.6*cm))
    flow.append(Paragraph("Das Nachlassgericht", body))
    flow.append(Spacer(1, 0.4*cm))
    flow.append(Paragraph("Anneliese Forstmaier, Rechtspflegerin", body))

    doc.build(flow)


if __name__ == "__main__":
    build_whiteboard()
    pdf_baylff()
    pdf_bvz()
    pdf_erbschein()
    print("OK")
