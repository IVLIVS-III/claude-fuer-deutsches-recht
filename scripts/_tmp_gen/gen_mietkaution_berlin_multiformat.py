#!/usr/bin/env python3
import sys
sys.path.insert(0, "scripts/_tmp_gen")
from pathlib import Path
from aktenbau import make_eml, make_md_email, make_csv, make_xlsx, make_jpg

BASE = Path("testakten/insolvenzrecht-forderungspruefung-mietkaution-berlin")

emails = [
    dict(frm="y.barsch@wvb-grundbesitz.de", to="s.threin@insolvenz-threin.de",
         subject="Terminvorschlag Ruecknahme Mietflaeche", date="Mon, 01 Jun 2026 09:10:00 +0200",
         body="Sehr geehrte Frau Dr. Threin,\n\nwir schlagen den 11.06.2026, 10:00 Uhr, fuer die Ruecknahme der Mietflaeche Kantstrasse 88-90 vor. Bitte bringen Sie alle Schluessel und Transponder mit.\n\nMit freundlichen Gruessen\nYvonne Barsch"),
    dict(frm="s.threin@insolvenz-threin.de", to="d.rausch@sv-rausch-berlin.de",
         subject="Beauftragung Wertminderungsgutachten", date="Thu, 18 Jun 2026 14:05:00 +0200",
         body="Sehr geehrter Herr Rausch,\n\nhiermit beauftrage ich Sie mit der Erstellung eines Gutachtens zur Wertminderung der Mietflaeche Kantstrasse 88-90 nach Rueckgabe. Das Rueckgabeprotokoll vom 11.06.2026 liegt bei.\n\nMit freundlichen Gruessen\nDr. Sabine Threin"),
    dict(frm="v.ehmke@kanzlei-ehmke.de", to="s.threin@insolvenz-threin.de",
         subject="Nachfrage Stand Kautionsauskehr", date="Thu, 16 Jul 2026 11:30:00 +0200",
         body="Sehr geehrte Frau Dr. Threin,\n\nnamens der WVB Grundbesitz Charlottenburg GmbH & Co. KG frage ich nach dem Stand der Pruefung unseres Antrags auf Kautionsauskehr vom 10.07.2026. Wir bitten um Ruecksprache bis 25.07.2026.\n\nMit freundlichen Gruessen\nDr. Volker Ehmke"),
    dict(frm="info@coworkzone-ev.de", to="s.threin@insolvenz-threin.de",
         subject="Rueckforderung Deposit Coworkzone e.V.", date="Fri, 12 Jun 2026 16:40:00 +0200",
         body="Sehr geehrte Frau Dr. Threin,\n\nwir hatten bei der Flexhof Berlin GmbH ein Deposit von 3.200 EUR hinterlegt und moechten dieses zur Insolvenztabelle anmelden. Anbei unser Untermietvertrag als Nachweis.\n\nMit freundlichen Gruessen\nCoworkzone e.V."),
    dict(frm="s.threin@insolvenz-threin.de", to="poststelle@amtsgericht-charlottenburg.berlin.de",
         subject="Mitteilung Pruefungsergebnis vor Termin", date="Tue, 21 Jul 2026 09:00:00 +0200",
         body="Sehr geehrte Damen und Herren,\n\nanbei die vorlaeufige Tabelle mit Pruefungsergebnissen zum Termin am 28.08.2026. Zwei Forderungen bleiben bestritten (IT-Systemhaus Bergmann, Unterkunde Freelance Base UG).\n\nMit freundlichen Gruessen\nDr. Sabine Threin"),
]
for i, e in enumerate(emails, start=1):
    fname = f"{i:02d}_{e['subject'][:28].lower().replace(' ','_')}"
    make_eml(BASE/"eml"/f"{fname}.eml", e["frm"], e["to"], e["subject"], e["date"], e["body"], msgid_domain="insolvenz-threin.de")
    make_md_email(BASE/"emails"/f"{fname}.md", e["frm"], e["to"], e["subject"], e["date"], e["body"])

make_csv(BASE/"csv"/"kontobewegungen_flexhof_maerz_juni_2026.csv",
    ["Datum","Buchungstext","Betrag_EUR","Saldo_EUR"],
    [["2026-03-31","Miete WVB Grundbesitz","-21600.00","18400.00"],
     ["2026-04-15","Einzahlung Unterkunden","32400.00","50800.00"],
     ["2026-04-30","Miete WVB Grundbesitz","-21600.00","29200.00"],
     ["2026-05-15","Einzahlung Unterkunden","28900.00","58100.00"],
     ["2026-05-31","Kontokorrentverrechnung Berliner Sparkasse","-8900.00","49200.00"],
     ["2026-06-02","Insolvenzantragstellung","0.00","49200.00"]])

make_csv(BASE/"csv"/"unterkunden_deposit_uebersicht.csv",
    ["Unterkunde","Deposit_EUR","Vertragsbeginn","Vertragsende","Status"],
    [["Coworkzone e.V.","3200.00","2023-02-01","2026-06-02","angemeldet"],
     ["Studio Nordlicht GbR","4800.00","2022-11-01","2026-06-02","angemeldet"],
     ["Freelance Base UG","2600.00","2024-05-01","2026-06-02","bestritten"]])

make_xlsx(BASE/"xlsx"/"forderungspruefung_kalkulation.xlsx", "Pruefung",
    ["Glaeubiger","Betrag_EUR","Status","Bemerkung"],
    [["WVB Grundbesitz Charlottenburg","63540.00","teilweise bestritten","14200 EUR Instandsetzung strittig"],
     ["Berliner Sparkasse","142000.00","festgestellt","Kontokorrentkredit"],
     ["Unterkunde Coworkzone e.V.","3200.00","festgestellt","Deposit"],
     ["Unterkunde Freelance Base UG","2600.00","bestritten","kein Untermietvertrag vorgelegt"]],
    title="Flexhof Berlin GmbH - Forderungspruefung Kalkulation")

(BASE/"pdfs").mkdir(exist_ok=True)
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
styles = getSampleStyleSheet()
doc = SimpleDocTemplate(str(BASE/"pdfs"/"kostenvoranschlag_elektrotechnik_bruns_original.pdf"), pagesize=A4,
    topMargin=2.5*cm, bottomMargin=2*cm, leftMargin=2.5*cm, rightMargin=2.5*cm)
story = [Paragraph("Elektrotechnik Bruns GmbH", styles["Heading2"]),
         Paragraph("Berlin-Wedding", styles["Normal"]), Spacer(1,20),
         Paragraph("Angebot Nr. EB-2026-4471 vom 20.06.2026", styles["Heading3"]),
         Paragraph("Austausch von 6 defekten Deckenleuchten LED-Panel 60x60, inkl. Montage und Entsorgung Altleuchten. Nettosumme: 1.368,00 EUR zzgl. 19% USt. Gesamtsumme: 1.627,92 EUR.", styles["Normal"])]
doc.build(story)

make_jpg(BASE/"jpg"/"rueckgabeprotokoll_foto1_bodenbelag_eg.jpg", "Flexhof Berlin - Rueckgabe 11.06.2026",
    ["Foto 1: Bodenbelag Empfangsbereich EG", "Zustand: starke Abnutzung, punktuelle Flecken",
     "Aufgenommen von: Dipl.-Ing. D. Rausch", "Vergleich siehe Musterprotokoll Nachbarobjekt"])

print("Mietkaution Berlin: Multi-Format-Ordner befuellt")
