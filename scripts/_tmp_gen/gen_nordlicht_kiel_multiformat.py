#!/usr/bin/env python3
import sys
sys.path.insert(0, "scripts/_tmp_gen")
from pathlib import Path
from aktenbau import make_eml, make_md_email, make_csv, make_xlsx, make_jpg
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm

BASE = Path("testakten/insolvenzverwaltung-nordlicht-handels-kiel")

emails = [
    dict(frm="j.hartmann@brinkmann-hartmann.de", to="m.suhrkamp@kieler-volksbank.de",
         subject="Anfrage interne Kreditakte 2012", date="Mon, 04 Nov 2013 10:00:00 +0100",
         body="Sehr geehrter Herr Suhrkamp,\n\nim Rahmen des Anfechtungsverfahrens 3 O 218/13 bitte ich um Uebersendung der internen Kreditakte fuer den Zeitraum Juni bis Dezember 2012.\n\nMit freundlichen Gruessen\nDr. Jens-Peter Hartmann"),
    dict(frm="t.klages@klages-partner.de", to="j.hartmann@brinkmann-hartmann.de",
         subject="Vergleichsgespraech Berger", date="Tue, 14 Oct 2014 15:20:00 +0200",
         body="Sehr geehrter Herr Dr. Hartmann,\n\nmein Mandant Stefan Berger ist bereit, ueber eine Ratenzahlung zur Erledigung der Haftungsklage zu sprechen. Koennen wir kurzfristig telefonieren?\n\nMit freundlichen Gruessen\nRA Torben Klages"),
    dict(frm="j.hartmann@brinkmann-hartmann.de", to="poststelle@amtsgericht-kiel.schleswig-holstein.de",
         subject="Zwischenbericht Nr. 8 zur Weiterleitung", date="Fri, 20 Nov 2020 09:15:00 +0100",
         body="Sehr geehrte Damen und Herren,\n\nanbei der 8. Zwischenbericht zum Verfahren 10 IN 127/13. Der Massebestand betraegt zum Stichtag 108.400 EUR.\n\nMit freundlichen Gruessen\nDr. Jens-Peter Hartmann"),
    dict(frm="c.reimann@reimann-wp.de", to="j.hartmann@brinkmann-hartmann.de",
         subject="Uebersendung Bilanzanalyse", date="Thu, 12 Jun 2014 11:40:00 +0200",
         body="Sehr geehrter Herr Dr. Hartmann,\n\nanbei die abgeschlossene Bilanzanalyse zur Feststellung des Zeitpunkts der Zahlungsunfaehigkeit. Ergebnis: Zahlungsunfaehigkeit ab 15.12.2012.\n\nMit freundlichen Gruessen\nWP Cordula Reimann"),
    dict(frm="j.hartmann@brinkmann-hartmann.de", to="finanzamt-kiel@fa.landsh.de",
         subject="Nachfrage Steuererstattung 2023", date="Wed, 15 Nov 2023 08:50:00 +0100",
         body="Sehr geehrte Damen und Herren,\n\nfuer die Nordlicht Handels GmbH i.I. bitte ich um Mitteilung, ob eine Steuererstattung fuer die Jahre 2013/2014 noch aussteht, da diese im Rahmen der Nachtragsverteilung zu beruecksichtigen waere.\n\nMit freundlichen Gruessen\nDr. Jens-Peter Hartmann"),
]
for i, e in enumerate(emails, start=1):
    fname = f"{i:02d}_{e['subject'][:28].lower().replace(' ','_')}"
    make_eml(BASE/"eml"/f"{fname}.eml", e["frm"], e["to"], e["subject"], e["date"], e["body"], msgid_domain="brinkmann-hartmann.de")
    make_md_email(BASE/"emails"/f"{fname}.md", e["frm"], e["to"], e["subject"], e["date"], e["body"])

make_csv(BASE/"csv"/"forderungstabelle_auszug.csv",
    ["Glaeubiger","Forderung_EUR","Status","Quote_Prozent","Auszahlung_EUR"],
    [["Kieler Volksbank eG","248500.00","festgestellt","13.5","33547.50"],
     ["Fashion Forward KG","42380.00","festgestellt","13.5","5721.30"],
     ["DAK-Gesundheit","14540.00","festgestellt (nach Vergleich)","13.5","1962.90"],
     ["IKK Nord","10350.00","festgestellt (nach Vergleich)","13.5","1397.25"]])

make_csv(BASE/"csv"/"treuhandkonto_bewegungen_2013.csv",
    ["Datum","Buchungstext","Betrag_EUR","Saldo_EUR"],
    [["2013-06-01","Eroeffnung Anderkonto","12400.00","12400.00"],
     ["2013-07-15","Erloes Raeumungsverkauf","28400.00","40800.00"],
     ["2013-08-31","Erloes Restverwertung Lager","18900.00","59700.00"],
     ["2013-09-30","Massekosten Miete/Nebenkosten","-9200.00","50500.00"]])

make_xlsx(BASE/"xlsx"/"masseentwicklung_2013_2024.xlsx", "Masseentwicklung",
    ["Datum","Massebestand_EUR"],
    [["2013-06-01","12400"],["2013-12-31","38700"],["2014-12-31","72500"],
     ["2015-12-31","84200"],["2016-12-31","91800"],["2017-12-31","95400"],
     ["2018-12-31","100200"],["2019-12-31","106800"],["2020-11-15","108400"],
     ["2024-04-25","120462"]],
    title="Nordlicht Handels GmbH - Masseentwicklung 2013-2024")

styles = getSampleStyleSheet()
doc = SimpleDocTemplate(str(BASE/"pdfs"/"vergleichsvereinbarung_volksbank_original.pdf"), pagesize=A4,
    topMargin=2.5*cm, bottomMargin=2*cm, leftMargin=2.5*cm, rightMargin=2.5*cm)
story = [Paragraph("Vergleichsvereinbarung", styles["Heading2"]),
         Paragraph("Nordlicht Handels GmbH i.I. ./. Kieler Volksbank eG, LG Kiel 3 O 218/13", styles["Normal"]), Spacer(1,20),
         Paragraph("Die Parteien einigen sich auf eine Zahlung von 62.000,00 EUR durch die Kieler Volksbank eG zur vollstaendigen Erledigung der Anfechtungsklage, zahlbar bis 15.05.2014, ohne Anerkennung einer Rechtspflicht.", styles["Normal"])]
doc.build(story)

make_jpg(BASE/"jpg"/"inventur_lager_wellseedamm_2013.jpg", "Nordlicht Handels GmbH - Inventur",
    ["Zentrallager Wellseedamm, Kiel", "Inventur vom 20.06.2013",
     "Geschaetzter Warenbestand: 340.000 EUR", "Durchgefuehrt durch: Insolvenzverwalter-Team"])

print("Nordlicht Kiel: Multi-Format-Ordner befuellt")
