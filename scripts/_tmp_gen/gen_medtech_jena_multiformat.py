#!/usr/bin/env python3
"""Multi-Format-Ordner fuer MedTech Jena"""
import sys
sys.path.insert(0, "scripts/_tmp_gen")
from pathlib import Path
from aktenbau import make_eml, make_md_email, make_csv, make_xlsx, make_jpg

BASE = Path("testakten/insolvenzrecht-eigenverwaltung-schutzschirm-medtech-jena")

emails = [
    dict(frm="marco.huettenrauch@biometrik-jena.de", to="f.sandhof@lindenhof-partner.de",
         subject="Liquiditaetsstatus KW29 - dringend", date="Mon, 20 Jul 2026 08:14:00 +0200",
         body="Sehr geehrter Herr Dr. Sandhof,\n\nanbei der aktualisierte 13-Wochen-Status. Die Deckungsluecke hat sich in KW29 auf 1,34 Mio EUR vergroessert, da Sensotec Optik nun ebenfalls auf Vorkasse besteht.\n\nWir muessen den Massekreditantrag beschleunigen.\n\nMit freundlichen Gruessen\nMarco Huettenrauch"),
    dict(frm="j.wehnert@sachwalter-erfurt.de", to="marco.huettenrauch@biometrik-jena.de",
         subject="Anzeigepflicht Zahlung PlastForm Suhl", date="Wed, 22 Jul 2026 11:02:00 +0200",
         body="Sehr geehrter Herr Huettenrauch,\n\ndie angezeigte Zahlung an PlastForm Suhl GmbH ueber 22.400 EUR wird freigegeben. Bitte reichen Sie kuenftig Zahlungsanzeigen mindestens zwei Werktage vor Faelligkeit ein.\n\nMit freundlichen Gruessen\nDr. Jonas Wehnert, vorlaeufiger Sachwalter"),
    dict(frm="p.willmsen@igmetall.de", to="f.sandhof@lindenhof-partner.de",
         subject="Terminvorschlag zweite Verhandlungsrunde Interessenausgleich", date="Fri, 24 Jul 2026 09:45:00 +0200",
         body="Sehr geehrter Herr Dr. Sandhof,\n\nwir schlagen den 05.08.2026, 10:00 Uhr, fuer die zweite Verhandlungsrunde vor. Bitte teilen Sie uns vorab die aktualisierte Sozialauswahl-Liste mit.\n\nMit gewerkschaftlichen Gruessen\nPetra Willmsen"),
    dict(frm="carsten.ohlendorf@medventures.de", to="e.frantzen@biometrik-jena.de",
         subject="Ruecksprache DIP-Financing Term Sheet", date="Mon, 27 Jul 2026 15:30:00 +0200",
         body="Liebe Frau Dr. Frantzen,\n\nunser Investment Committee tagt am 03.08.2026. Bitte stellen Sie bis dahin die finale Quotenberechnung sowie den Status der Sensortech-Verhandlungen bereit.\n\nBeste Gruesse\nCarsten Ohlendorf"),
    dict(frm="r.imhof@sensortech-holding.ch", to="f.sandhof@lindenhof-partner.de",
         subject="Due-Diligence-Fragenliste", date="Thu, 30 Jul 2026 10:12:00 +0200",
         body="Sehr geehrter Herr Dr. Sandhof,\n\nanbei unsere erste Fragenliste zur Due Diligence: Patentstatus, Kundenvertraege Top 5, Personalkostenstruktur nach Sozialplan. Wir bitten um Antworten bis 12.08.2026.\n\nMit freundlichen Gruessen\nDr. Rebecca Imhof"),
    dict(frm="u.kalinski@biometrik-jena.de", to="m.kellerbach@biometrik-jena.de",
         subject="Rueckmeldungen aus der Belegschaft nach Betriebsversammlung", date="Fri, 10 Jul 2026 17:20:00 +0200",
         body="Hallo Herr Dr. Kellerbach,\n\nviele Kolleginnen und Kollegen fragen nach dem Stand der Lohnzahlungen fuer Juli und nach der betrieblichen Altersvorsorge. Koennen wir dazu kurzfristig informieren?\n\nViele Gruesse\nUwe Kalinski"),
]

for i, e in enumerate(emails, start=1):
    make_eml(BASE/"eml"/f"{i:02d}_{e['subject'][:30].lower().replace(' ','_').replace('-','_')}.eml",
             e["frm"], e["to"], e["subject"], e["date"], e["body"], msgid_domain="biometrik-jena.de")
    make_md_email(BASE/"emails"/f"{i:02d}_{e['subject'][:30].lower().replace(' ','_').replace('-','_')}.md",
             e["frm"], e["to"], e["subject"], e["date"], e["body"])

# csv/ Ordner
make_csv(BASE/"csv"/"kontobewegungen_geschaeftskonto_juni_juli_2026.csv",
    ["Datum","Buchungstext","Betrag_EUR","Saldo_EUR"],
    [["2026-06-15","Gutschrift Kunde MedTech Nord","184300.00","540000.00"],
     ["2026-06-18","Lastschrift PlastForm Suhl","-22400.00","517600.00"],
     ["2026-06-22","Gehaltszahlung Juni","-280000.00","237600.00"],
     ["2026-06-30","Gutschrift Kunde Klinikverbund Sued","96500.00","334100.00"],
     ["2026-07-05","Ueberweisung Sensotec Optik Vorkasse","-45000.00","289100.00"],
     ["2026-07-15","Gutschrift Kunde MedTech Nord","102400.00","391500.00"],
     ["2026-07-22","Gehaltszahlung Juli (teilweise)","-260000.00","131500.00"]])

make_csv(BASE/"csv"/"fristenliste_schutzschirmverfahren.csv",
    ["Frist","Datum","Verantwortlich","Status"],
    [["Vorlage Insolvenzplan (3 Monate)","2026-10-06","CRO Dr. Kellerbach","laeuft"],
     ["Berichtstermin","2026-08-25","Sachwalter Dr. Wehnert","erledigt"],
     ["Abstimmungstermin Insolvenzplan","2026-10-15","Amtsgericht Jena","geplant"],
     ["Exklusivitaet Sensortech LOI","2026-09-28","RA Dr. Sandhof","laeuft"]])

# xlsx bereits vorhanden (streitige_forderungen_status.xlsx) -> weiteres xlsx ergaenzen
make_xlsx(BASE/"xlsx"/"liquiditaetsplanung_13_wochen_update.xlsx", "13-Wochen-Plan",
    ["KW","Anfangsbestand","Einzahlungen","Auszahlungen","Endbestand"],
    [[27,540000,820000,780000,580000],
     [28,580000,650000,700000,530000],
     [29,530000,590000,760000,360000],
     [30,360000,610000,790000,180000],
     [31,180000,640000,700000,120000],
     [32,120000,600000,690000,30000],
     [33,30000,900000,720000,210000]],
    title="BioMetrik Jena GmbH - 13-Wochen-Liquiditaetsplan (Update Massekredit)")

# pdfs/ - Hinweis: echte Renderungen erfolgen zentral ueber build-testakten-einzelpdf-zips; hier nur Platzhalter-Kopie eines Originaldokuments als PDF-Quelle nicht noetig, Ordner mit Verweisdatei
(BASE/"pdfs").mkdir(exist_ok=True)
(BASE/"pdfs"/".keep").write_text("Renderungen werden zentral ueber die Build-Skripte erzeugt.\n")

# jpg/
make_jpg(BASE/"jpg"/"vermerk_scan_krisensitzung.jpg", "BioMetrik Jena GmbH - Scan",
    ["Krisensitzungsvermerk vom 29.06.2026", "Teilnehmer: Dr. Frantzen, Huettenrauch,",
     "RA Dr. Sandhof (Lindenhof und Partner)", "Handschriftlicher Vermerk: 'Schutzschirm pruefen'",
     "Abgelegt: Akte 555 IN 132/26, Anlage 1"])

print("MedTech Jena: Multi-Format-Ordner befuellt")
