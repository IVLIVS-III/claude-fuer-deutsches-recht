#!/usr/bin/env python3
"""Ausbau: insolvenzrecht-forderungspruefung-mietkaution-berlin"""
import sys
sys.path.insert(0, "scripts/_tmp_gen")
from pathlib import Path
from aktenbau import make_docx, make_eml, make_md_email, make_csv, make_xlsx, make_jpg

BASE = Path("testakten/insolvenzrecht-forderungspruefung-mietkaution-berlin")
KOPF = "Flexhof Berlin GmbH i.I. | Insolvenzverwalterin Dr. Sabine Threin | Az. AG Charlottenburg 36g IN 892/26"

make_docx(BASE/"08_mietvertrag_vollversion.docx", KOPF,
    "Gewerbemietvertrag - Vollversion",
    ["Zwischen der WVB Grundbesitz Charlottenburg GmbH & Co. KG (Vermieterin) und der Flexhof Berlin GmbH (Mieterin) wird folgender Mietvertrag geschlossen (Auszug Vollversion, urspruenglich unterzeichnet am 14.03.2022):",
     "## Mietobjekt",
     "Gewerbeflaechen im Erdgeschoss und 1. OG, Kantstrasse 88-90, 10627 Berlin, Nutzflaeche 890 qm, nebst 14 Tiefgaragenstellplaetzen.",
     "## Mietzeit und Miete",
     "Mietbeginn: 01.05.2022, Festlaufzeit 7 Jahre bis 30.04.2029 mit zweimaliger Verlaengerungsoption von je 3 Jahren. Nettokaltmiete: 18.400 EUR monatlich, Betriebskostenvorauszahlung: 3.200 EUR monatlich.",
     "## Kaution",
     "Die Mieterin hat eine Kaution in Hoehe von drei Nettokaltmieten (55.200 EUR) zu leisten, zu hinterlegen auf einem insolvenzfesten, offen ausgewiesenen Kautionskonto gemaess § 551 Abs. 3 BGB analog fuer Gewerberaum in Verbindung mit der vertraglichen Kautionsabrede in § 12.",
     "## Untervermietung",
     "Eine Untervermietung an Dritte (Coworking-Nutzer) ist mit Zustimmung der Vermieterin gestattet; die Zustimmung gilt als generell erteilt fuer Vertragslaufzeiten der Unterkunden von maximal 24 Monaten.",
     "## Kuendigung",
     "Ordentliche Kuendigung waehrend der Festlaufzeit ist ausgeschlossen. Bei Insolvenz der Mieterin gilt § 109 InsO."],
    "WVB Grundbesitz Charlottenburg GmbH & Co. KG, unterzeichnet 14.03.2022")

make_docx(BASE/"09_nachtraege_mietvertrag_untervermietung_umbau.docx", KOPF,
    "Nachtraege zum Mietvertrag",
    ["## Nachtrag 1 - Untervermietungserlaubnis erweitert (15.09.2023)",
     "Die Vermieterin erweitert die generelle Untervermietungserlaubnis auf Vertragslaufzeiten der Unterkunden von bis zu 36 Monaten, gegen eine einmalige Zustimmungsgebuehr von 2.500 EUR.",
     "## Nachtrag 2 - Umbau 1. Obergeschoss (10.01.2024)",
     "Die Mieterin wird ermaechtigt, im 1. Obergeschoss Trennwaende fuer 12 zusaetzliche Buero-Boxen zu errichten. Rueckbauverpflichtung bei Vertragsende: ja, auf Kosten der Mieterin. Die Vermieterin gewaehrt einen Baukostenzuschuss von 18.000 EUR, verrechnet mit drei Monatsmieten.",
     "## Nachtrag 3 - Erhoehung Kaution (22.11.2024)",
     "Aufgrund der erweiterten Nutzflaeche durch den Umbau wird die Kaution um 9.200 EUR auf insgesamt 64.400 EUR erhoeht, zahlbar bis 31.12.2024."],
    "WVB Grundbesitz Charlottenburg GmbH & Co. KG")

make_docx(BASE/"10_kautionsverpfaendungsvertrag_bankinstitut.docx", KOPF,
    "Verpfaendungsvertrag Kautionskonto",
    ["Zwischen der Flexhof Berlin GmbH und der Berliner Sparkasse wird folgender Verpfaendungsvertrag zugunsten der WVB Grundbesitz Charlottenburg GmbH & Co. KG geschlossen:",
     "Die Flexhof Berlin GmbH unterhaelt bei der Berliner Sparkasse ein Kautionssparkonto Nr. 1044-887321 mit einem Guthaben von zuletzt 64.400 EUR.",
     "Das Guthaben wird zur Sicherung aller Anspruche der Vermieterin aus dem Mietverhaeltnis Kantstrasse 88-90 verpfaendet. Die Bank bestaetigt, dass ueber das Konto nur mit Zustimmung beider Parteien verfuegt werden darf.",
     "Hinweis der Bank vom 30.06.2026: Aufgrund eines internen Buchungsfehlers wurde das Kautionsguthaben zeitweise nicht getrennt von den sonstigen Geschaeftskonten der Flexhof Berlin GmbH gefuehrt; eine Bereinigung erfolgte am 15.01.2025."],
    "Berliner Sparkasse, Gewerbekundenbetreuung, 20.12.2022")

make_docx(BASE/"11_rueckgabeprotokoll_ausfuehrlich_fotoanhaenge.docx", KOPF,
    "Rückgabeprotokoll Mietflaeche - ausfuehrlich",
    ["Rueckgabetermin: 11.06.2026, 10:00 Uhr. Teilnehmer: Hausverwalterin Frau Yvonne Barsch (WVB Grundbesitz), Insolvenzverwalterin Dr. Sabine Threin, technischer Sachverstaendiger Herr Dietmar Rausch.",
     "## Zustand Erdgeschoss",
     "Bodenbelag (Teppichfliesen) in Bereich Empfang: starke Abnutzung, punktuelle Flecken (Foto 1-3). Trennwandsystem: 4 von 18 Modulen mit Kratzern (Foto 4).",
     "## Zustand 1. Obergeschoss (Umbau-Bereich)",
     "12 Buero-Boxen aus Nachtrag 2 nicht zurueckgebaut (vertraglich vereinbarte Rueckbaupflicht, Foto 5-8). Deckenleuchten: 6 Stueck defekt oder fehlend (Foto 9).",
     "## Tiefgarage",
     "13 von 14 Stellplaetzen ordnungsgemaess, 1 Stellplatz mit Oelfleck (Foto 10).",
     "## Schluesseluebergabe",
     "42 Schluessel und 8 Transponder zurueckgegeben, 3 Transponder als verloren gemeldet.",
     "Fotoanhaenge (Foto 1 bis Foto 10) liegen als Anlage jpg/ bei."],
    "Protokollfuehrung: Hausverwaltung WVB Grundbesitz Charlottenburg GmbH & Co. KG")

make_docx(BASE/"12_reparaturkosten_angebot_handwerker.docx", KOPF,
    "Kostenvoranschlag Reparaturarbeiten - Elektrotechnik Bruns GmbH",
    ["Angebot Nr. EB-2026-4471 vom 20.06.2026 fuer die WVB Grundbesitz Charlottenburg GmbH & Co. KG.",
     "Leistungsumfang: Austausch von 6 defekten Deckenleuchten LED-Panel 60x60, inkl. Montage und Entsorgung Altleuchten, 1. Obergeschoss Kantstrasse 88-90.",
     "Materialkosten: 840,00 EUR. Arbeitszeit: 6 Stunden a 68,00 EUR = 408,00 EUR. Anfahrt und Entsorgung: 120,00 EUR.",
     "Nettosumme: 1.368,00 EUR zzgl. 19 % USt 259,92 EUR. Gesamtsumme: 1.627,92 EUR.",
     "Angebot gueltig bis 20.07.2026."],
    "Elektrotechnik Bruns GmbH, Berlin-Wedding")

make_docx(BASE/"13_kostenvoranschlag_malerbetrieb_bodenverleger.docx", KOPF,
    "Kostenvoranschlage Malerarbeiten und Bodenbelag",
    ["## Angebot Malerbetrieb Kowalski (23.06.2026)",
     "Ausbesserung und Neuanstrich Wandflaechen Erdgeschoss nach Entfernung Trennwandsystem: 620 qm, 8,50 EUR/qm netto = 5.270,00 EUR netto.",
     "## Angebot Bodenwerk Nordberg (24.06.2026)",
     "Austausch Teppichfliesen Empfangsbereich, 140 qm, inkl. Unterbodenvorbereitung: 42,00 EUR/qm netto = 5.880,00 EUR netto. Rueckbau 12 Buero-Boxen 1. OG (Trockenbauwaende, Elektroinstallation zurueckbauen): Pauschalangebot 8.400,00 EUR netto.",
     "Gesamtsumme beider Angebote netto: 19.550,00 EUR, brutto 23.264,50 EUR."],
    "Malerbetrieb Kowalski / Bodenwerk Nordberg GmbH, Berlin")

make_docx(BASE/"14_sachverstaendigengutachten_wertminderung.docx", KOPF,
    "Sachverständigengutachten zur Wertminderung der Mietsache",
    ["Gutachter: Dipl.-Ing. Dietmar Rausch, oeffentlich bestellter und vereidigter Sachverstaendiger fuer Schaeden an Gebaeuden, Berlin.",
     "Auftrag: Feststellung des ueber die normale Abnutzung hinausgehenden Instandsetzungsbedarfs der Mietflaeche Kantstrasse 88-90 nach Beendigung des Mietverhaeltnisses mit der Flexhof Berlin GmbH.",
     "## Feststellungen",
     "Der nicht zurueckgebaute Umbau des 1. Obergeschosses (12 Buero-Boxen) stellt eine ueber die vertragsgemaesse Nutzung hinausgehende bauliche Veraenderung dar, deren Rueckbau vertraglich geschuldet ist (Nachtrag 2). Rueckbaukosten laut vorliegenden Angeboten: 8.400 EUR netto.",
     "Die Abnutzung von Bodenbelag und Trennwandsystem im Erdgeschoss bewegt sich teils im Rahmen ueblicher Abnutzung bei sieben Jahren Mietdauer, teils darueber hinaus (punktuelle Flecken, 4 beschaedigte Trennwandmodule).",
     "## Ergebnis",
     "Der Sachverstaendige schaetzt den ueber die normale Abnutzung hinausgehenden Instandsetzungsbedarf auf insgesamt 14.200 EUR netto (Rueckbau, Trennwandreparatur, Deckenleuchten, Oelfleck-Beseitigung Tiefgarage)."],
    "Dipl.-Ing. Dietmar Rausch, Berlin, 05.07.2026")

make_docx(BASE/"15_betriebskostenabrechnung_2024_nachzahlung.docx", KOPF,
    "Betriebskostenabrechnung 2024",
    ["Abrechnungszeitraum: 01.01.2024 bis 31.12.2024.",
     "Vorauszahlungen geleistet: 38.400,00 EUR (12 x 3.200,00 EUR).",
     "Tatsaechliche Betriebskosten: Heizung/Warmwasser 11.240,00 EUR, Wasser/Abwasser 6.180,00 EUR, Versicherung 4.920,00 EUR, Hausmeister/Reinigung 14.760,00 EUR, Grundsteuer 5.340,00 EUR, Sonstiges 2.100,00 EUR. Summe: 44.540,00 EUR.",
     "Nachzahlung zulasten der Flexhof Berlin GmbH: 6.140,00 EUR, faellig zum 30.09.2025. Die Nachzahlung wurde bis zur Insolvenzeroeffnung nicht beglichen und ist Gegenstand der Forderungsanmeldung."],
    "WVB Grundbesitz Charlottenburg GmbH & Co. KG, Abrechnungsstelle, 15.08.2025")

make_docx(BASE/"16_kautionsauskehr_antrag_bankverrechnung.docx", KOPF,
    "Antrag auf Kautionsauskehr mit Bankverrechnung",
    ["Die WVB Grundbesitz Charlottenburg GmbH & Co. KG beantragt bei der Berliner Sparkasse die Auskehr des verpfaendeten Kautionsguthabens (Konto 1044-887321, Stand 64.400 EUR) zur teilweisen Befriedigung ihrer Forderungen aus Nutzungsentschaedigung, Betriebskostennachzahlung und Instandsetzung.",
     "Berechnung: Betriebskostennachzahlung 6.140,00 EUR, Instandsetzungsbedarf laut Gutachten 14.200,00 EUR, offene Nutzungsentschaedigung Mai/Juni 2026 (2 x 21.600,00 EUR) 43.200,00 EUR. Gesamtforderung: 63.540,00 EUR.",
     "Beantragte Verrechnung mit Kautionsguthaben 64.400,00 EUR, verbleibender Ueberschuss zugunsten der Masse: 860,00 EUR.",
     "Die Insolvenzverwalterin wird um Zustimmung zur Verrechnung binnen zwei Wochen gebeten."],
    "WVB Grundbesitz Charlottenburg GmbH & Co. KG, RA Dr. Volker Ehmke, 10.07.2026")

make_docx(BASE/"17_anfechtungspruefung_iv_130_zeitraum.docx", KOPF,
    "Aktenvermerk - Anfechtungspruefung Kautionserhoehung",
    ["Verfasserin: Dr. Sabine Threin, Insolvenzverwalterin.",
     "Zu pruefen ist, ob die Erhoehung der Kaution um 9.200 EUR gemaess Nachtrag 3 vom 22.11.2024 der Anfechtung nach §§ 129 ff. InsO unterliegt.",
     "Die Zahlung erfolgte am 28.12.2024. Der Insolvenzantrag wurde am 02.06.2026 gestellt. Der Zeitraum von mehr als 18 Monaten zwischen Zahlung und Antragstellung liegt ausserhalb der 3-Monats-Frist des § 130 InsO.",
     "Zu pruefen bleibt eine Anfechtung nach § 133 Abs. 1 InsO (Vorsatzanfechtung, 10-Jahres-Frist), wofuer bislang keine tragfaehigen Anhaltspunkte fuer einen Benachteiligungsvorsatz der Schuldnerin vorliegen. Der Vermerk ist als reine Pruefungsnotiz zu verstehen; eine abschliessende Bewertung steht noch aus."],
    "Interner Aktenvermerk, 12.07.2026")

make_docx(BASE/"18_pruefungsschreiben_iv_vermieter_widerspruch_178.docx", KOPF,
    "Prüfungsschreiben der Insolvenzverwalterin an die Vermieterin",
    ["Sehr geehrte Damen und Herren,",
     "im Rahmen der Forderungspruefung zur angemeldeten Forderung Nr. 14 (WVB Grundbesitz Charlottenburg GmbH & Co. KG, 63.540,00 EUR) widerspreche ich der Forderung gemaess § 178 InsO in Hoehe eines Teilbetrags von 14.200,00 EUR (Instandsetzungsbedarf laut Sachverstaendigengutachten), da die zugrunde liegende Rueckbauverpflichtung aus Nachtrag 2 nach meiner vorlaeufigen Einschaetzung nicht in voller Hoehe zu Lasten der Masse geht.",
     "Die uebrigen Teilbetraege (Betriebskostennachzahlung 6.140,00 EUR und Nutzungsentschaedigung 43.200,00 EUR) werden zur Tabelle festgestellt.",
     "Ich bitte um Mitteilung, ob der Widerspruch akzeptiert oder gerichtlich geklaert werden soll."],
    "Dr. Sabine Threin, Insolvenzverwalterin, Berlin, 15.07.2026")

make_docx(BASE/"19_widerspruchsklage_entwurf_179_inso.docx", KOPF,
    "Entwurf Feststellungsklage gemaess Paragraf 179 InsO",
    ["An das Amtsgericht Charlottenburg (Entwurf, noch nicht eingereicht).",
     "Klaegerin: WVB Grundbesitz Charlottenburg GmbH & Co. KG. Beklagte: Dr. Sabine Threin als Insolvenzverwalterin ueber das Vermoegen der Flexhof Berlin GmbH.",
     "Antrag: Es wird festgestellt, dass der Klaegerin eine Forderung in Hoehe von 14.200,00 EUR als Insolvenzforderung im Rang des § 38 InsO zusteht.",
     "Begruendung (Entwurf): Die Rueckbauverpflichtung aus Nachtrag 2 zum Mietvertrag vom 10.01.2024 sei eine vertragliche Nebenpflicht, deren Nichterfuellung einen Schadensersatzanspruch nach § 280 Abs. 1 BGB begruende. Der Anspruch sei in voller Hoehe des Sachverstaendigengutachtens berechtigt.",
     "Dieser Entwurf ist noch nicht final abgestimmt und dient der Vorbereitung des Prüfungstermins."],
    "RA Dr. Volker Ehmke, Entwurf vom 22.07.2026")

make_csv(BASE/"20_tabellenauszug_vollstaendig.csv",
    ["Lfd_Nr","Glaeubiger","Angemeldeter_Betrag_EUR","Grund","Status_Pruefungstermin"],
    [["1","Finanzamt Berlin Charlottenburg","18420.50","Umsatzsteuer 2025","festgestellt"],
     ["2","Berliner Sparkasse","142000.00","Kontokorrentkredit","festgestellt"],
     ["3","Deutsche Rentenversicherung Bund","9840.30","Sozialversicherungsbeitraege","festgestellt"],
     ["4","Reinigungsservice Nord GmbH","4120.00","Dienstleistungsrechnungen","festgestellt"],
     ["5","IT-Systemhaus Bergmann","6780.00","Wartungsvertrag","bestritten"],
     ["6","Unterkunde Coworkzone e.V.","3200.00","Deposit-Rueckforderung","festgestellt"],
     ["7","Unterkunde Studio Nordlicht GbR","4800.00","Deposit-Rueckforderung","festgestellt"],
     ["8","Unterkunde Freelance Base UG","2600.00","Deposit-Rueckforderung","bestritten"],
     ["9","Getraenke Schmidt KG","1140.00","Lieferantenrechnung","festgestellt"],
     ["10","Facility Management Rausch","3980.00","Wartungsvertrag","festgestellt"],
     ["11","Personal - 6 ehemalige Beschaeftigte","28400.00","Lohnrueckstaende","festgestellt"],
     ["12","Versicherung Nordstern AG","2140.00","Betriebshaftpflicht Restpraemie","festgestellt"],
     ["13","Buerobedarf Klaas GmbH","890.00","Lieferantenrechnung","festgestellt"],
     ["14","WVB Grundbesitz Charlottenburg GmbH & Co. KG","63540.00","Kaution/Nutzungsentschaedigung/Instandsetzung","teilweise bestritten (14200 EUR)"]])

make_docx(BASE/"21_berechnung_insolvenzquote_massekalkulation.docx", KOPF,
    "Massekalkulation und vorläufige Quotenberechnung",
    ["## Masseaktiva",
     "Verwertung Bueroausstattung und IT: 18.400,00 EUR. Ueberschuss Kautionsverrechnung: 860,00 EUR. Forderungseinzug offene Kundenrechnungen: 24.600,00 EUR. Bankguthaben zum Eroeffnungsstichtag: 4.120,00 EUR. Summe Masseaktiva: 47.980,00 EUR.",
     "## Massekosten und Masseverbindlichkeiten",
     "Verguetung Insolvenzverwalterin (vorlaeufig geschaetzt): 14.200,00 EUR. Gerichtskosten: 1.800,00 EUR. Sonstige Masseverbindlichkeiten: 2.400,00 EUR. Summe: 18.400,00 EUR.",
     "## Verteilungsmasse",
     "Verbleibend fuer Insolvenzglaeubiger: 29.580,00 EUR bei festgestellten Forderungen von insgesamt 231.130,80 EUR (ohne bestrittene Betraege), entsprechend einer vorlaeufigen Quote von rund 12,8 %."],
    "Dr. Sabine Threin, Insolvenzverwalterin, Zwischenstand 20.07.2026")

make_docx(BASE/"22_aktenvermerk_aufrechnung_94ff_inso.docx", KOPF,
    "Aktenvermerk - Pruefung Aufrechnung gemaess Paragraf 94 ff. InsO",
    ["Verfasserin: Dr. Sabine Threin.",
     "Zu pruefen ist, ob die Berliner Sparkasse berechtigt war, am 31.05.2026 eine Kontokorrentverrechnung in Hoehe von 8.900,00 EUR zulasten des Geschaeftskontos der Flexhof Berlin GmbH vorzunehmen, nachdem der Insolvenzantrag am 02.06.2026 gestellt wurde.",
     "Die Verrechnung erfolgte vor Antragstellung, sodass § 96 Abs. 1 Nr. 1 InsO (Aufrechnungsverbot nach Verfahrenseroeffnung) nicht unmittelbar einschlaegig erscheint. Zu pruefen bleibt, ob die Bank zum Zeitpunkt der Verrechnung bereits Kenntnis von einem Insolvenzantrag oder der Zahlungsunfaehigkeit hatte, was eine Anfechtung der Rechtshandlung nach §§ 129 ff. InsO in Verbindung mit § 96 Abs. 1 Nr. 3 InsO ermoeglichen wuerde.",
     "Dieser Vermerk fasst nur den Pruefungsstand zusammen; eine Entscheidung ueber das weitere Vorgehen steht noch aus."],
    "Interner Aktenvermerk, 14.07.2026")

make_docx(BASE/"23_schriftverkehr_verwalter_vermieterin.docx", KOPF,
    "Schriftwechsel Insolvenzverwalterin - Vermieterin (Zusammenstellung)",
    ["## Schreiben vom 05.06.2026 (Verwalterin an Vermieterin)",
     "Mitteilung ueber die Eroeffnung des Insolvenzverfahrens und Aufforderung zur Forderungsanmeldung binnen der gesetzlichen Frist.",
     "## Schreiben vom 20.06.2026 (Vermieterin an Verwalterin)",
     "Ankuendigung der Forderungsanmeldung sowie Bitte um zeitnahe Terminvereinbarung zur Ruecknahme der Mietflaeche.",
     "## Schreiben vom 02.07.2026 (Verwalterin an Vermieterin)",
     "Bestaetigung des Rueckgabetermins am 11.06.2026 (bereits erfolgt) und Ankuendigung, dass die Instandsetzungsforderung noch geprueft werde.",
     "## Schreiben vom 16.07.2026 (Vermieterin an Verwalterin)",
     "Nachfrage zum Stand der Pruefung und Hinweis auf drohende Verzugszinsen."],
    "Zusammenstellung Kanzleiakte, Stand 20.07.2026")

make_docx(BASE/"24_musterrueckgabeprotokoll_vergleichsobjekt.docx", KOPF,
    "Musterrückgabeprotokoll Nachbarobjekt (Vergleichsobjekt)",
    ["Zum Vergleich der ueblichen Abnutzung wird das Rueckgabeprotokoll eines vergleichbaren Nachbarobjekts (Kantstrasse 92, ebenfalls Coworking-Nutzung, Rueckgabe 14.02.2026, anderer Mieter) beigefuegt.",
     "Zustand bei Rueckgabe nach 6 Jahren Mietdauer: Bodenbelag mit ueblichem Abrieb, keine Fehlstellen. Trennwandsystem: keine Beschaedigungen. Keine baulichen Veraenderungen, keine offenen Rueckbaupflichten.",
     "Dieses Vergleichsobjekt dient der Einordnung, welcher Instandsetzungsbedarf ueber die normale Abnutzung hinausgeht und welcher nicht."],
    "Hausverwaltung WVB Grundbesitz Charlottenburg GmbH & Co. KG, 14.02.2026")

print("Mietkaution Berlin: Kernstuecke erzeugt")
