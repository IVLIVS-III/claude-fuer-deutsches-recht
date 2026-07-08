#!/usr/bin/env python3
"""Ausbau: insolvenzrecht-eigenverwaltung-schutzschirm-medtech-jena"""
import sys
sys.path.insert(0, "scripts/_tmp_gen")
from pathlib import Path
from aktenbau import make_docx, make_eml, make_md_email, make_csv, make_xlsx, make_jpg

BASE = Path("testakten/insolvenzrecht-eigenverwaltung-schutzschirm-medtech-jena")
KOPF = "BioMetrik Jena GmbH i.E.V. | Lindenhof und Partner mbB | Az. AG Jena 555 IN 132/26"

# 08 Handelsregisterauszug
make_docx(BASE/"08_handelsregisterauszug_prokuristen.docx", KOPF,
    "Handelsregisterauszug (Abdruck) - BioMetrik Jena GmbH",
    ["Amtsgericht Jena, Handelsregister B, HRB 512 887",
     "Firma: BioMetrik Jena GmbH, Sitz: Jena, Geschaeftsanschrift: Loebstedter Strasse 67, 07749 Jena",
     "Gegenstand: Entwicklung, Herstellung und Vertrieb medizintechnischer Sensorik und Diagnosegeraete.",
     "Stammkapital: 250.000,00 EUR",
     "## Geschaeftsfuehrung",
     "- Dr. Elisa Frantzen, geb. 1979, einzelvertretungsberechtigt, befreit von § 181 BGB, bestellt seit 03.2016",
     "- Marco Huettenrauch, geb. 1984, einzelvertretungsberechtigt, bestellt seit 01.2022 (CFO-Funktion)",
     "## Prokura",
     "- Sandra Wei, geb. 1988, Prokura seit 07.2021, gemeinsam mit einem Geschaeftsfuehrer oder einem weiteren Prokuristen",
     "- Tobias Rehm, geb. 1981, Prokura seit 02.2024, gemeinsam mit einem Geschaeftsfuehrer",
     "## Gesellschafter",
     "- Frantzen Beteiligungs GmbH: 61 %",
     "- MedVentures Rhein-Main Fonds II GmbH & Co. KG: 39 %",
     "Eingetragene Veraenderungen: Bestellung Prokura Rehm am 14.02.2024 (HRB-Aenderung Nr. 14).",
     "Abdruck erstellt am 30.06.2026 zur Vorlage beim Amtsgericht Jena, Insolvenzabteilung."],
    "Amtsgericht Jena - Registergericht")

# 09 Bilanz 2024/2025
make_docx(BASE/"09_bilanz_2024_2025_stille_reserven_vermerk.docx", KOPF,
    "Bilanz 2024 und 2025 mit Vermerk zu stillen Reserven",
    ["Kurzbilanz zum 31.12.2024 und 31.12.2025 (Werte in TEUR), erstellt durch Steuerberatung Kolbe & Nauendorf.",
     "## Aktiva",
     "- Sachanlagen: 2024: 4.180 / 2025: 3.960",
     "- Patente und Zulassungen (immateriell): 2024: 1.240 / 2025: 1.510",
     "- Vorraete: 2024: 2.310 / 2025: 2.870",
     "- Forderungen aus Lieferungen und Leistungen: 2024: 1.980 / 2025: 2.640 (davon streitig 2025: 640)",
     "- Kasse/Bank: 2024: 890 / 2025: 210",
     "## Passiva",
     "- Eigenkapital: 2024: 1.760 / 2025: -340",
     "- Gesellschafterdarlehen (Rangruecktritt vorgesehen): 2024: 800 / 2025: 1.100",
     "- Bankverbindlichkeiten: 2024: 3.200 / 2025: 3.950",
     "- Verbindlichkeiten aus Lieferungen und Leistungen: 2024: 2.140 / 2025: 3.480",
     "- Rueckstellungen (Gewaehrleistung, Personal): 2024: 700 / 2025: 1.020",
     "## Vermerk stille Reserven",
     "Der bilanzielle Restbuchwert der Produktionshalle Loebstedter Strasse betraegt 1,42 Mio EUR; nach Einschaetzung des beauftragten Gutachters Dipl.-Ing. Falko Reinsch liegt der Verkehrswert bei rund 2,35 Mio EUR. Zusaetzlich sind zwei Patentfamilien (Sensorkalibrierung, EP 3 912 xxx) nicht bilanziert, deren Marktwert vom Patentanwalt auf 400.000 bis 650.000 EUR geschaetzt wird.",
     "Diese stillen Reserven sind bei der Fortfuehrungsprognose und der Vergleichsrechnung zum Insolvenzplan zu beruecksichtigen."],
    "Kolbe & Nauendorf Steuerberatungsgesellschaft mbH, Jena, 18.06.2026")

# 10 BWA Q1+Q2 2026
make_csv(BASE/"10_bwa_q1_q2_2026.csv",
    ["Monat", "Umsatzerloese", "Materialaufwand", "Personalaufwand", "Sonstige_Kosten", "EBITDA", "Liquide_Mittel_Monatsende"],
    [["2026-01","640000","310000","280000","95000","-45000","540000"],
     ["2026-02","580000","300000","280000","98000","-98000","410000"],
     ["2026-03","510000","295000","282000","101000","-168000","260000"],
     ["2026-04","470000","270000","284000","104000","-188000","150000"],
     ["2026-05","430000","260000","286000","108000","-224000","70000"],
     ["2026-06","399000","250000","288000","112000","-251000","-40000"]])

# 11 Lieferantenuebersicht CSV
make_csv(BASE/"11_lieferantenuebersicht_zahlungsverhalten.csv",
    ["Lieferant", "Kategorie", "Offene_Forderung_EUR", "Zahlungsziel_Tage", "Zahlungsverhalten_letzte_6_Monate", "Kreditversicherung"],
    [["Sensotec Optik GmbH","Sensorik","184300.00","30","2x Skonto verpasst, 1x Mahnung","COFACE gekuendigt zum 15.06.2026"],
     ["PlastForm Suhl GmbH","Gehaeuseteile","76900.00","21","puenktlich","COFACE aktiv, Limit reduziert auf 40000"],
     ["MedKabel Systeme AG","Kabelkonfektion","54200.00","30","1x verspaetet 12 Tage","Euler Hermes aktiv"],
     ["Reinraum Service Ost","Dienstleistung","19800.00","14","puenktlich","keine Versicherung"],
     ["Zolltech Logistik GmbH","Logistik","41250.00","30","2x verspaetet, aktuell nur Vorkasse","COFACE gekuendigt zum 01.07.2026"]])

# 12 Kuendigungsschreiben Warenkreditversicherer
make_docx(BASE/"12_kuendigung_warenkreditversicherer_cofinsure.docx", KOPF,
    "COFINSURE Kreditversicherung AG - Kuendigung der Deckungszusage",
    ["Sehr geehrte Damen und Herren,",
     "wir nehmen Bezug auf die Warenkreditversicherung Police Nr. WKV-88213-DE fuer Lieferungen an die BioMetrik Jena GmbH.",
     "Nach Auswertung der aktuellen Bonitaetsinformationen (Ruecklastschriften Mai 2026, verlaengerte Zahlungsziele, negative Presseberichterstattung zu Liquiditaetsengpaessen) kuendigen wir die Deckungszusage fuer alle Lieferungen an die BioMetrik Jena GmbH mit Wirkung zum 15.06.2026.",
     "Bereits bestehende, gedeckte Forderungen aus Lieferungen bis einschliesslich 14.06.2026 bleiben im Rahmen der Policenbedingungen versichert.",
     "Fuer Rueckfragen steht Ihnen unser Underwriting-Team zur Verfuegung.",
     "Mit freundlichen Gruessen"],
    "COFINSURE Kreditversicherung AG, Underwriting Team Mitte, Mainz")

# 13 Sanierungsgutachten IDW S6 Kurzfassung
make_docx(BASE/"13_sanierungsgutachten_idw_s6_kurzfassung.docx", KOPF,
    "Sanierungsgutachten nach IDW S6 - Kurzfassung",
    ["Auftraggeberin: BioMetrik Jena GmbH. Gutachter: WP/StB Dr. Hendrik Rossmann, Rossmann Sanierungsberatung Leipzig.",
     "## Rahmenkapitel",
     "Die BioMetrik Jena GmbH befindet sich nach Einschaetzung des Gutachters in der Unternehmenskrise im Stadium der Erfolgs- und Liquiditaetskrise (IDW S6 Tz. 27). Ausloeser sind die FDA-Zulassungsverzoegerung eines Kernprodukts, die Kuendigung der Warenkreditversicherung sowie eine streitige Kundenforderung von 640.000 EUR.",
     "## Zahlen",
     "Umsatzerloese 2025: 6,42 Mio EUR (Vorjahr 7,88 Mio EUR). EBITDA 2025: -1,05 Mio EUR. Eigenkapitalquote 2025: -6,1 %. Liquiditaetsluecke laut 13-Wochen-Status in KW 30: 1,18 Mio EUR bei Ausfall der streitigen Forderung.",
     "## Massnahmenkatalog",
     "- Rangruecktritt Gesellschafterdarlehen 1,1 Mio EUR",
     "- Personalanpassung um 45 Stellen (Sozialplanvolumen ca. 1,4 Mio EUR)",
     "- Working-Capital-Programm Lager- und Forderungsmanagement",
     "- Verhandlung Massekredit mit Hausbank ueber 900.000 EUR",
     "- Pruefung Schutzschirmverfahren § 270d InsO zur Fortfuehrung unter Eigenverwaltung",
     "Der Gutachter attestiert eine positive Fortfuehrungsprognose unter der Bedingung, dass die genannten Massnahmen fristgerecht umgesetzt werden."],
    "Rossmann Sanierungsberatung, Leipzig, 22.06.2026")

# 14 CRO-Bestellungsurkunde
make_docx(BASE/"14_cro_bestellungsurkunde_gesellschafterbeschluss.docx", KOPF,
    "Gesellschafterbeschluss - Bestellung Chief Restructuring Officer",
    ["Beschluss der Gesellschafterversammlung der BioMetrik Jena GmbH vom 24.06.2026 (schriftliches Umlaufverfahren).",
     "Die Gesellschafter beschliessen einstimmig:",
     "1. Herr Dr. Matthias Kellerbach, Restrukturierungsberater, wird mit Wirkung zum 01.07.2026 zum Chief Restructuring Officer (CRO) bestellt.",
     "2. Der CRO erhaelt Einzelprokura sowie Zustimmungsvorbehalte fuer Zahlungen ueber 25.000 EUR, Vertragsabschluesse ueber 50.000 EUR und alle insolvenzrechtlich relevanten Entscheidungen.",
     "3. Die Bestellung erfolgt bis zum Abschluss des Schutzschirmverfahrens, laengstens bis 31.12.2026.",
     "4. Die Verguetung betraegt 24.000 EUR monatlich zzgl. Erfolgskomponente gemaess separatem Dienstvertrag."],
    "Fuer die Frantzen Beteiligungs GmbH: Dr. Elisa Frantzen | Fuer MedVentures Rhein-Main Fonds II: Carsten Ohlendorf")

# 15 Schutzschirmantrag Reinschrift
make_docx(BASE/"15_schutzschirmantrag_reinschrift_270d_inso.docx", KOPF,
    "Antrag auf Eigenverwaltung im Schutzschirmverfahren gemaess Paragraf 270d InsO",
    ["An das Amtsgericht Jena, Insolvenzabteilung",
     "In dem Insolvenzeroeffnungsverfahren der BioMetrik Jena GmbH, vertreten durch die Geschaeftsfuehrerin Dr. Elisa Frantzen, beantragen wir:",
     "1. Die Eroeffnung des Insolvenzverfahrens ueber das Vermoegen der BioMetrik Jena GmbH wegen drohender Zahlungsunfaehigkeit (§ 18 InsO) und Ueberschuldung (§ 19 InsO).",
     "2. Die Anordnung der vorlaeufigen Eigenverwaltung gemaess § 270a InsO.",
     "3. Die Bestimmung einer Frist zur Vorlage eines Insolvenzplans von nicht mehr als drei Monaten gemaess § 270d Abs. 1 InsO.",
     "4. Die vorlaeufige Bestellung eines Sachwalters.",
     "Der Antrag stuetzt sich auf die beigefuegte Bescheinigung einer in Insolvenzsachen erfahrenen Person nach § 270d Abs. 1 Satz 1 InsO, wonach die angestrebte Sanierung nicht offensichtlich aussichtslos ist.",
     "Anlagen: Bescheinigung § 270d InsO, 13-Wochen-Liquiditaetsplan, Sanierungsgutachten IDW S6, Jahresabschluesse 2024/2025, Handelsregisterauszug."],
    "Lindenhof und Partner mbB, RA Dr. Fabian Sandhof, Jena, 03.07.2026")

# 16 Bescheinigung 270d
make_docx(BASE/"16_bescheinigung_270d_steuerberater.docx", KOPF,
    "Bescheinigung gemaess Paragraf 270d Absatz 1 InsO",
    ["Ausstellerin: Kolbe & Nauendorf Steuerberatungsgesellschaft mbH, Jena.",
     "Wir bescheinigen als in Insolvenzsachen erfahrene Berufstraeger, dass die BioMetrik Jena GmbH zum Stichtag 30.06.2026 drohend zahlungsunfaehig, jedoch nicht zahlungsunfaehig im Sinne des § 17 InsO ist.",
     "Grundlage der Beurteilung sind der 13-Wochen-Liquiditaetsstatus, die BWA Januar bis Juni 2026, die Jahresabschluesse 2024 und 2025 sowie Gespraeche mit der Geschaeftsfuehrung.",
     "Die angestrebte Sanierung im Rahmen eines Schutzschirmverfahrens ist nach unserer fachlichen Einschaetzung nicht offensichtlich aussichtslos, insbesondere angesichts der vorhandenen stillen Reserven, laufender Verhandlungen mit der Hausbank ueber einen Massekredit und eines Kaufinteresses eines strategischen Investors."],
    "Kolbe & Nauendorf Steuerberatungsgesellschaft mbH, StB Frank Nauendorf, Jena, 02.07.2026")

# 17 Beschluss AG Jena vorlaeufige Eigenverwaltung
make_docx(BASE/"17_beschluss_ag_jena_vorlaeufige_eigenverwaltung.docx", KOPF,
    "Beschluss des Amtsgerichts Jena",
    ["Amtsgericht Jena, Insolvenzabteilung, Az. 555 IN 132/26",
     "In dem Insolvenzeroeffnungsverfahren ueber das Vermoegen der BioMetrik Jena GmbH ergeht folgender Beschluss:",
     "1. Es wird angeordnet, dass die Schuldnerin unter Aufsicht eines vorlaeufigen Sachwalters die Verwaltungs- und Verfuegungsbefugnis ueber ihr Vermoegen behaelt (vorlaeufige Eigenverwaltung, § 270a InsO).",
     "2. Zum vorlaeufigen Sachwalter wird Herr Rechtsanwalt Dr. Jonas Wehnert, Erfurt, bestellt.",
     "3. Der Schuldnerin wird aufgegeben, Masseverbindlichkeiten nur mit Zustimmung des vorlaeufigen Sachwalters einzugehen, soweit sie den gewoehnlichen Geschaeftsbetrieb ueberschreiten.",
     "4. Die Frist zur Vorlage eines Insolvenzplans wird auf drei Monate ab heute bestimmt (§ 270d Abs. 1 Satz 2 InsO)."],
    "Amtsgericht Jena, Insolvenzabteilung, 06.07.2026")

# 18 Bestellung vorlaeufiger Sachwalter Anzeigepflichten
make_docx(BASE/"18_bestellung_sachwalter_anzeigepflichten.docx", KOPF,
    "Anzeigepflichten des vorlaeufigen Sachwalters",
    ["Herr RA Dr. Jonas Wehnert wurde mit Beschluss vom 06.07.2026 zum vorlaeufigen Sachwalter der BioMetrik Jena GmbH bestellt.",
     "Der Sachwalter weist die Geschaeftsfuehrung auf folgende Anzeigepflichten hin:",
     "1. Jede Zahlung ueber 10.000 EUR ist vorab anzuzeigen und vom Sachwalter freizugeben.",
     "2. Personalmassnahmen mit Kostenwirkung ueber 20.000 EUR beduerfen der vorherigen Zustimmung.",
     "3. Der 13-Wochen-Liquiditaetsstatus ist woechentlich zu aktualisieren und dem Sachwalter zu uebermitteln.",
     "4. Wesentliche Vertragsaenderungen mit Kunden oder Lieferanten sind unverzueglich mitzuteilen.",
     "Verstoesse gegen diese Pflichten koennen zur Aufhebung der Eigenverwaltung fuehren (§ 270e InsO)."],
    "RA Dr. Jonas Wehnert, vorlaeufiger Sachwalter, Erfurt, 08.07.2026")

# 19 Betriebsversammlungsprotokoll
make_docx(BASE/"19_betriebsversammlungsprotokoll.docx", KOPF,
    "Protokoll der außerordentlichen Betriebsversammlung",
    ["Ort: Kantine BioMetrik Jena, Datum: 09.07.2026, 15:00 Uhr. Teilnehmer: 118 von 128 Beschaeftigten, Betriebsratsvorsitzender Herr Uwe Kalinski, Geschaeftsfuehrerin Dr. Elisa Frantzen, CRO Dr. Matthias Kellerbach.",
     "Dr. Frantzen informierte ueber die Anordnung der vorlaeufigen Eigenverwaltung und das Schutzschirmverfahren. Sie erlaeuterte, dass ein Personalabbau von bis zu 45 Stellen im Rahmen des Sanierungskonzepts unvermeidbar sei.",
     "Der Betriebsratsvorsitzende Kalinski forderte umgehende Verhandlungen ueber Interessenausgleich und Sozialplan sowie eine Beteiligung der IG Metall.",
     "Mehrere Wortmeldungen aus der Belegschaft betrafen die Sicherung ausstehender Lohnzahlungen und die Fortfuehrung der betrieblichen Altersvorsorge.",
     "Es wurde vereinbart, dass die erste Verhandlungsrunde mit der IG Metall am 16.07.2026 stattfindet."],
    "Protokollfuehrung: Personalabteilung BioMetrik Jena GmbH")

# 20 IG-Metall Interessenausgleich Verhandlungsprotokoll
make_docx(BASE/"20_igmetall_interessenausgleich_verhandlungsprotokoll.docx", KOPF,
    "Verhandlungsprotokoll Interessenausgleich - erste Runde",
    ["Datum: 16.07.2026, Ort: Lindenhof und Partner mbB, Jena. Teilnehmer: RA Dr. Fabian Sandhof (Schuldnerin), CRO Dr. Matthias Kellerbach, IG Metall Verhandlungsfuehrerin Petra Willmsen, Betriebsratsvorsitzender Uwe Kalinski.",
     "Die Schuldnerin stellte den Personalabbauplan vor: Wegfall von 45 der 128 Stellen, schwerpunktmaessig in der Verwaltung und einer nicht profitablen Produktlinie.",
     "IG Metall forderte eine Sozialauswahl nach transparenten Kriterien, Abfindungsfaktor mindestens 0,7 Monatsgehaelter je Beschaeftigungsjahr sowie eine Transfergesellschaft fuer betroffene Beschaeftigte.",
     "Die Schuldnerin verwies auf die begrenzte Masse und bot einen Abfindungsfaktor von 0,4 sowie eine Transfergesellschaft fuer maximal sechs Monate an.",
     "Die Verhandlungen wurden ohne Einigung vertagt; naechster Termin: 24.07.2026."],
    "Protokollfuehrung: RA Dr. Fabian Sandhof")

# 21 Massekreditvertrag Bank
make_docx(BASE/"21_massekreditvertrag_bank_sicherheiten.docx", KOPF,
    "Massekreditvertrag mit der Thueringer Landesbank",
    ["Vertragsparteien: BioMetrik Jena GmbH (in Eigenverwaltung), vertreten durch Dr. Elisa Frantzen und CRO Dr. Matthias Kellerbach, und Thueringer Landesbank AöR, Erfurt.",
     "## Kreditrahmen",
     "Die Bank raeumt der Schuldnerin einen Massekredit in Hoehe von bis zu 900.000 EUR zur Sicherung der Betriebsfortfuehrung waehrend des Schutzschirmverfahrens ein.",
     "## Sicherheiten",
     "- Globalzession der Forderungen aus Lieferungen und Leistungen",
     "- Sicherungsuebereignung des Maschinenparks (Buchwert 1,2 Mio EUR)",
     "- Verpfaendung der Patentfamilie Sensorkalibrierung",
     "## Konditionen",
     "Zinssatz: 3-Monats-Euribor zzgl. 4,25 Prozentpunkten. Bereitstellungsprovision: 0,25 % p.a. auf nicht abgerufene Betraege. Laufzeit: bis zum rechtskraeftigen Abschluss des Insolvenzplanverfahrens, laengstens 30.06.2027.",
     "Der Massekredit ist gemaess § 264 InsO als Masseverbindlichkeit zu bedienen."],
    "Thueringer Landesbank AöR, Bereich Sanierungsfinanzierung, Erfurt, 18.07.2026")

# 22 DIP financing term sheet
make_docx(BASE/"22_dip_financing_term_sheet.docx", KOPF,
    "Debtor-in-Possession-Financing Term Sheet (Entwurf)",
    ["Interessent: MedVentures Rhein-Main Fonds II GmbH & Co. KG (Bestandsgesellschafter).",
     "## Eckpunkte",
     "- Finanzierungsvolumen: bis zu 500.000 EUR als nachrangiges Ueberbrueckungsdarlehen",
     "- Zinssatz: 8 % p.a., endfaellig",
     "- Rangfolge: nachrangig gegenueber Massekredit der Thueringer Landesbank, vorrangig gegenueber Alt-Gesellschafterdarlehen",
     "- Bedingung: Zustimmung des vorlaeufigen Sachwalters sowie Aufnahme einer Besserungsklausel im Insolvenzplan",
     "- Laufzeit: bis Planvollzug, laengstens 24 Monate",
     "Dieses Term Sheet ist unverbindlich und steht unter dem Vorbehalt der Gremienzustimmung bei MedVentures."],
    "MedVentures Rhein-Main Fonds II GmbH & Co. KG, Carsten Ohlendorf, Frankfurt am Main, 20.07.2026 (Entwurf)")

# 23 Erste Glaeubigerversammlung Protokoll
make_docx(BASE/"23_erste_glaeubigerversammlung_protokoll.docx", KOPF,
    "Protokoll der ersten Gläubigerversammlung (Berichtstermin)",
    ["Amtsgericht Jena, Az. 555 IN 132/26, Termin am 25.08.2026, 09:30 Uhr.",
     "Anwesend: Insolvenzrichterin Frau Kortmann, vorlaeufiger Sachwalter Dr. Jonas Wehnert, Geschaeftsfuehrerin Dr. Elisa Frantzen, CRO Dr. Matthias Kellerbach sowie Vertreter von 14 Glaeubigern.",
     "Der Sachwalter berichtete ueber den Stand der Eigenverwaltung, die Fortfuehrung des Geschaeftsbetriebs und den Massekredit. Die Geschaeftsfuehrung stellte den Sanierungsfahrplan und den geplanten Insolvenzplan vor.",
     "Auf Antrag mehrerer Glaeubiger wurde ein vorlaeufiger Glaeubigerausschuss mit fuenf Mitgliedern eingesetzt (Hausbank, zwei Warenkreditgeber, Arbeitnehmervertretung, Finanzamt).",
     "Die naechste Glaeubigerversammlung zur Abstimmung ueber den Insolvenzplan wurde fuer den 15.10.2026 terminiert."],
    "Protokollfuehrung: Geschaeftsstelle Amtsgericht Jena")

# 24 Insolvenzplan-Skizze mit Quotenberechnung
make_docx(BASE/"24_insolvenzplan_skizze_quotenberechnung.docx", KOPF,
    "Insolvenzplan - Skizze mit Quotenberechnung (Arbeitsstand)",
    ["## Gestaltender Teil (Skizze)",
     "Die ungesicherten Insolvenzglaeubiger erhalten eine Quote, die aus dem Fortfuehrungsertrag und einem Besserungsschein finanziert wird.",
     "## Quotenberechnung (vorlaeufig)",
     "Masseerloes aus Fortfuehrung und Verwertung stiller Reserven (Grundstueck, Patente): geschaetzt 2,1 Mio EUR. Massekosten und Masseverbindlichkeiten (Sachwalter, Massekredit, Sozialplan): geschaetzt 1,55 Mio EUR. Verbleibender Betrag fuer ungesicherte Glaeubiger: rund 0,55 Mio EUR bei einer Forderungssumme von 4,9 Mio EUR, entsprechend einer vorlaeufigen Quote von etwa 11 %.",
     "## Offene Punkte",
     "Die endgueltige Quote haengt vom Ausgang der streitigen Kundenforderung (640.000 EUR) sowie vom Verkaufserloes der Patentfamilie ab. Beide Punkte sind zum Zeitpunkt dieser Skizze nicht abschliessend geklaert."],
    "CRO Dr. Matthias Kellerbach, Arbeitsstand 05.08.2026")

# 25 Sozialplan-Entwurf
make_docx(BASE/"25_sozialplan_entwurf_45_gekuendigte.docx", KOPF,
    "Sozialplan-Entwurf fuer den Personalabbau von 45 Stellen",
    ["Zwischen der BioMetrik Jena GmbH (in Eigenverwaltung) und dem Betriebsrat, vertreten durch Herrn Uwe Kalinski, wird folgender Sozialplan vereinbart (Entwurf, Stand 30.07.2026):",
     "1. Abfindung: 0,5 Bruttomonatsgehaelter je vollem Beschaeftigungsjahr, gedeckelt auf 25.000 EUR pro Person.",
     "2. Transfergesellschaft fuer alle betroffenen Beschaeftigten mit einer Laufzeit von neun Monaten, finanziert anteilig aus Massemitteln und Foerderung der Bundesagentur fuer Arbeit.",
     "3. Sozialauswahl nach den Kriterien Betriebszugehoerigkeit, Lebensalter, Unterhaltspflichten und Schwerbehinderung gemaess § 1 Abs. 3 KSchG.",
     "4. Das Gesamtvolumen des Sozialplans wird auf 1,38 Mio EUR geschaetzt und ist als Masseverbindlichkeit zu bedienen, begrenzt durch § 123 InsO (Sozialplan-Deckelung)."],
    "Entwurf zur Verhandlung, Stand 30.07.2026")

# 26 Steuerliche Fortfuehrungsprognose
make_docx(BASE/"26_steuerliche_fortfuehrungsprognose_verlustvortraege.docx", KOPF,
    "Steuerliche Fortführungsprognose zur Werthaltigkeit der Verlustvorträge",
    ["Erstellt durch Kolbe & Nauendorf Steuerberatungsgesellschaft mbH zur Beurteilung der Anwendung des § 3a EStG (Sanierungsertrag) sowie zur Werthaltigkeit koerperschaftsteuerlicher Verlustvortraege.",
     "Zum 31.12.2025 bestehen koerperschaftsteuerliche Verlustvortraege in Hoehe von 2,86 Mio EUR sowie gewerbesteuerliche Verlustvortraege von 2,74 Mio EUR.",
     "Im Rahmen des geplanten Insolvenzplans mit Forderungsverzicht der ungesicherten Glaeubiger in Hoehe von rund 4,35 Mio EUR entsteht ein Sanierungsertrag im Sinne des § 3a EStG. Dieser ist grundsaetzlich steuerfrei, mindert jedoch vorrangig die vorhandenen Verlustvortraege.",
     "Nach der beigefuegten Beispielrechnung verbleibt nach Verrechnung ein Restverlustvortrag von rund 0 EUR koerperschaftsteuerlich und rund 0 EUR gewerbesteuerlich; ein zu versteuernder Sanierungsertrag entsteht nach dieser vorlaeufigen Berechnung nicht."],
    "Kolbe & Nauendorf Steuerberatungsgesellschaft mbH, StB Frank Nauendorf, Jena, 12.08.2026")

# 27 Kaufinteressent NDA + LOI
make_docx(BASE/"27_kaufinteressent_nda_loi.docx", KOPF,
    "Vertraulichkeitsvereinbarung und Absichtserklaerung (LOI) mit Kaufinteressent",
    ["Zwischen der BioMetrik Jena GmbH (in Eigenverwaltung) und der Sensortech Holding AG, Zuerich, als Kaufinteressentin.",
     "## Vertraulichkeitsvereinbarung (NDA)",
     "Die Parteien vereinbaren gegenseitige Vertraulichkeit hinsichtlich aller im Rahmen der Due Diligence ausgetauschten Informationen fuer die Dauer von drei Jahren.",
     "## Letter of Intent (Eckpunkte)",
     "- Gegenstand: Erwerb des operativen Geschaeftsbetriebs im Rahmen eines Asset Deals (uebertragende Sanierung) oder alternativ Beteiligung im Rahmen des Insolvenzplans",
     "- Indikativer Kaufpreis: 2,4 bis 2,9 Mio EUR, vorbehaltlich Due Diligence",
     "- Exklusivitaet: 45 Tage ab Unterzeichnung",
     "- Bedingung: Zustimmung des Glaeubigerausschusses und des Sachwalters",
     "Diese Absichtserklaerung ist rechtlich nicht bindend mit Ausnahme der Vertraulichkeits- und Exklusivitaetsregelung."],
    "Sensortech Holding AG, Dr. Rebecca Imhof, Zuerich, 14.08.2026")

# 28 Anzeige drohender Zahlungsunfaehigkeit (interne Notiz)
make_docx(BASE/"28_anzeige_drohende_zahlungsunfaehigkeit_18_inso_notiz.docx", KOPF,
    "Interne Notiz - Anzeige drohender Zahlungsunfaehigkeit gemaess Paragraf 18 InsO",
    ["Verfasser: RA Dr. Fabian Sandhof, Lindenhof und Partner mbB. Datum: 28.06.2026.",
     "Die Geschaeftsfuehrung der BioMetrik Jena GmbH hat die Kanzlei gebeten, die Voraussetzungen fuer eine Anzeige drohender Zahlungsunfaehigkeit nach § 18 InsO zu pruefen, um Zugang zu den Instrumenten der Eigenverwaltung und des Schutzschirmverfahrens zu erhalten.",
     "Nach dem vorliegenden 13-Wochen-Liquiditaetsstatus ist davon auszugehen, dass die Gesellschaft ohne Gegenmassnahmen ab Kalenderwoche 30 ihre faelligen Zahlungspflichten voraussichtlich nicht mehr vollstaendig erfuellen kann.",
     "Empfehlung: Zeitnahe Stellung des Antrags auf Eigenverwaltung im Schutzschirmverfahren, verbunden mit der Bescheinigung nach § 270d InsO, um den Handlungsspielraum der Geschaeftsfuehrung zu sichern und eine geordnete Sanierung zu ermoeglichen.",
     "Diese Notiz dient ausschliesslich der internen Vorbereitung und ist nicht zur Weitergabe an Dritte bestimmt."],
    "Lindenhof und Partner mbB, interne Akte")

print("MedTech Jena: DOCX-Kernstuecke erzeugt")
