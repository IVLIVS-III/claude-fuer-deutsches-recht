#!/usr/bin/env python3
"""Ausbau: insolvenzverwaltung-nordlicht-handels-kiel"""
import sys
sys.path.insert(0, "scripts/_tmp_gen")
from pathlib import Path
from aktenbau import make_docx, make_eml, make_md_email, make_csv, make_xlsx, make_jpg

BASE = Path("testakten/insolvenzverwaltung-nordlicht-handels-kiel")
KOPF = "Nordlicht Handels GmbH i.I. | Brinkmann Hartmann und Kollegen | Az. AG Kiel 10 IN 127/13"

make_docx(BASE/"06_insolvenzantrag_schuldnerin_mit_anlagen.docx", KOPF,
    "Eigenantrag der Schuldnerin mit Anlagen",
    ["An das Amtsgericht Kiel, Insolvenzabteilung.",
     "Die Nordlicht Handels GmbH, vertreten durch die Geschaeftsfuehrer Stefan Berger und Katrin Berger, beantragt die Eroeffnung des Insolvenzverfahrens ueber ihr Vermoegen wegen Zahlungsunfaehigkeit und Ueberschuldung.",
     "Anlagen: Vermoegensuebersicht zum 31.12.2012, Glaeubiger- und Schuldnerverzeichnis, Personalliste (34 Beschaeftigte), Bankverbindungen (Kieler Volksbank eG), Gesellschafterliste.",
     "Die Zahlungsunfaehigkeit ist eingetreten, nachdem die Kieler Volksbank eG am 20.12.2012 die Kontokorrentlinie fristlos gekuendigt hat. Die Ueberschuldung ergibt sich aus der beigefuegten Ueberschuldungsbilanz (Aktiva 890.000 EUR, Passiva 1.240.000 EUR)."],
    "Nordlicht Handels GmbH, Stefan Berger und Katrin Berger, Kiel, 14.01.2013")

make_docx(BASE/"07_glaeubigerantrag_krankenkasse.docx", KOPF,
    "Gläubigerantrag der DAK-Gesundheit",
    ["An das Amtsgericht Kiel.",
     "Die DAK-Gesundheit beantragt die Eroeffnung des Insolvenzverfahrens ueber das Vermoegen der Nordlicht Handels GmbH wegen rueckstaendiger Sozialversicherungsbeitraege fuer den Zeitraum Juli bis Dezember 2012 in Hoehe von 18.740,00 EUR.",
     "Die Forderung ist durch vollstreckbaren Beitragsbescheid tituliert. Mehrere Vollstreckungsversuche blieben erfolglos.",
     "Az. 10 IN 168/13."],
    "DAK-Gesundheit, Regionaldirektion Nord, Kiel, 22.01.2013")

make_docx(BASE/"08_vorlaeufiger_iv_bericht_sicherungsmassnahmen.docx", KOPF,
    "Erster Bericht des vorläufigen Insolvenzverwalters - Sicherungsmaßnahmen",
    ["Nach meiner Bestellung zum vorlaeufigen Insolvenzverwalter mit Beschluss vom 16.01.2013 habe ich folgende Sicherungsmassnahmen getroffen:",
     "1. Sicherung der Geschaeftsraeume Holstenstrasse, Rendsburger Landstrasse und Wellseedamm.",
     "2. Inventur des Warenbestands (geschaetzter Wert: 340.000 EUR).",
     "3. Einrichtung eines Anderkontos fuer laufende Einnahmen.",
     "4. Fortfuehrung des Geschaeftsbetriebs bis zur Eroeffnungsentscheidung zur Vermeidung eines Wertverlusts bei den Textilbestaenden (Saisonware).",
     "Empfehlung: Eroeffnung des Regelinsolvenzverfahrens mit Fortfuehrung bis zum Abverkauf der Saisonware."],
    "Dr. Jens-Peter Hartmann, vorlaeufiger Insolvenzverwalter, Kiel, 25.01.2013")

make_docx(BASE/"09_sicherungsanordnung_21_inso.docx", KOPF,
    "Sicherungsanordnung gemaess Paragraf 21 InsO",
    ["Amtsgericht Kiel, Az. 10 IN 127/13.",
     "Das Gericht ordnet folgende Sicherungsmassnahmen an:",
     "1. Bestellung von Herrn RA Dr. Jens-Peter Hartmann zum vorlaeufigen Insolvenzverwalter.",
     "2. Allgemeines Verfuegungsverbot fuer die Schuldnerin (§ 21 Abs. 2 Nr. 2 InsO).",
     "3. Vorlaeufiges Verwertungs- und Einziehungsverbot fuer Sicherungsrechte der Kieler Volksbank eG.",
     "Der vorlaeufige Verwalter wird ermaechtigt, den Geschaeftsbetrieb bis zur Entscheidung ueber den Eroeffnungsantrag fortzufuehren."],
    "Amtsgericht Kiel, Insolvenzabteilung, 16.01.2013")

make_docx(BASE/"10_betriebseinstellungs_anordnung.docx", KOPF,
    "Anordnung zur Betriebseinstellung",
    ["Nach Abschluss der Raeumungsverkaeufe zum 31.08.2013 ordnet der Insolvenzverwalter die Einstellung des operativen Geschaeftsbetriebs an.",
     "Die Geschaeftsraeume Holstenstrasse, Rendsburger Landstrasse und das Hafen-Geschaeft werden zum 31.08.2013 geschlossen. Der Online-Shop wird bis 30.09.2013 abgewickelt.",
     "Alle 34 Beschaeftigten wurden zum 30.06.2013 gekuendigt; Kuendigungsschutzklagen sind nicht anhaengig.",
     "Das Zentrallager Wellseedamm wird bis zur vollstaendigen Verwertung der Restbestaende bis 31.12.2013 weitergefuehrt."],
    "Dr. Jens-Peter Hartmann, Insolvenzverwalter, Kiel, 25.08.2013")

make_docx(BASE/"11_gutachten_iv_zur_verfahrenseroeffnung.docx", KOPF,
    "Gutachten des vorläufigen Insolvenzverwalters zur Verfahrenseröffnung",
    ["Das Gutachten kommt zu dem Ergebnis, dass Eroeffnungsgruende (Zahlungsunfaehigkeit gemaess § 17 InsO und Ueberschuldung gemaess § 19 InsO) vorliegen.",
     "Die Insolvenzmasse wird auf rund 340.000 EUR Warenbestand zzgl. Forderungen aus Lieferungen und Leistungen (ca. 85.000 EUR) sowie Kassenbestand geschaetzt.",
     "Massekostendeckung ist gegeben. Die Eroeffnung des Regelinsolvenzverfahrens wird empfohlen.",
     "Besondere Pruefpunkte: Kontokorrentrueckfuehrungen an die Kieler Volksbank eG in den letzten drei Monaten vor Antragstellung sowie Zahlungen an die Geschaeftsfuehrung."],
    "Dr. Jens-Peter Hartmann, Kiel, 20.05.2013")

make_docx(BASE/"12_anfechtungsklageschrift_bank_kontokorrent.docx", KOPF,
    "Anfechtungsklage gegen die Kieler Volksbank eG",
    ["An das Landgericht Kiel.",
     "Klaeger: Dr. Jens-Peter Hartmann als Insolvenzverwalter ueber das Vermoegen der Nordlicht Handels GmbH. Beklagte: Kieler Volksbank eG.",
     "Antrag: Die Beklagte wird verurteilt, an den Klaeger 87.400,00 EUR nebst Zinsen zu zahlen.",
     "Begruendung: Im Zeitraum vom 20.09.2012 bis 20.12.2012 wurden auf dem Kontokorrentkonto Nr. 4471-9982 Gutschriften in Hoehe von insgesamt 87.400,00 EUR mit dem debitorischen Saldo verrechnet, nachdem die Beklagte am 15.09.2012 von der drohenden Zahlungsunfaehigkeit der Schuldnerin durch ein internes Kreditueberwachungsschreiben Kenntnis erlangt hatte. Die Rechtshandlungen seien nach § 130 Abs. 1 Nr. 1 InsO anfechtbar.",
     "Az. Landgericht Kiel: 3 O 218/13."],
    "Dr. Jens-Peter Hartmann, Insolvenzverwalter, Kiel, 10.09.2013")

make_docx(BASE/"13_klageerwiderung_volksbank.docx", KOPF,
    "Klageerwiderung der Kieler Volksbank eG",
    ["Landgericht Kiel, Az. 3 O 218/13.",
     "Namens und in Vollmacht der Beklagten wird beantragt, die Klage abzuweisen.",
     "Die Beklagte bestreitet, zum Zeitpunkt der streitgegenstaendlichen Gutschriften Kenntnis von einer Zahlungsunfaehigkeit der Klaegerin gehabt zu haben. Das interne Kreditueberwachungsschreiben vom 15.09.2012 habe lediglich eine routinemaessige Bonitaetspruefung dokumentiert, keine Feststellung der Zahlungsunfaehigkeit.",
     "Ferner wird die Auffassung vertreten, dass es sich bei den Gutbuchungen im laufenden Kontokorrent um kongruente Deckungen im Rahmen des vereinbarten Kreditrahmens gehandelt habe."],
    "RA Dr. Wolfgang Petersen, Kanzlei Petersen und Kollegen, Kiel, 05.11.2013")

make_docx(BASE/"14_beweisbeschluss_lg_kiel.docx", KOPF,
    "Beweisbeschluss des Landgerichts Kiel",
    ["Landgericht Kiel, Az. 3 O 218/13.",
     "Das Gericht ordnet die Vernehmung folgender Zeugen an: Herr Matthias Suhrkamp (Firmenkundenberater, Kieler Volksbank eG) zu der Frage, ob und wann die Beklagte Kenntnis von der Zahlungsunfaehigkeit der Schuldnerin erlangt hat.",
     "Ferner wird die Vorlage der internen Kreditakte der Beklagten fuer den Zeitraum 01.06.2012 bis 20.12.2012 angeordnet.",
     "Termin zur Beweisaufnahme: 14.01.2014, 10:00 Uhr."],
    "Landgericht Kiel, 3. Zivilkammer, 02.12.2013")

make_docx(BASE/"15_zeugenaussagen_bankberater.docx", KOPF,
    "Protokoll der Zeugenvernehmung - Matthias Suhrkamp",
    ["Landgericht Kiel, Termin 14.01.2014.",
     "Der Zeuge Matthias Suhrkamp, Firmenkundenberater der Kieler Volksbank eG, sagt aus: Im September 2012 sei ihm aufgefallen, dass das Konto der Nordlicht Handels GmbH wiederholt die vereinbarte Kreditlinie ueberschritten habe. Er habe daraufhin ein internes Ueberwachungsschreiben verfasst, in dem er auf 'deutliche Liquiditaetsanspannung' hingewiesen habe.",
     "Auf Frage des Klaegervertreters bestaetigt der Zeuge, dass er in einem Telefonat vom 18.09.2012 mit Herrn Stefan Berger ueber 'ernste Zahlungsschwierigkeiten' gesprochen habe.",
     "Der Zeuge verneint, das Wort 'zahlungsunfaehig' verwendet zu haben, raeumt aber ein, dass ihm die angespannte Lage bekannt gewesen sei."],
    "Protokollfuehrung: Landgericht Kiel, 3. Zivilkammer")

make_docx(BASE/"16_vergleichsverhandlungsprotokoll_volksbank.docx", KOPF,
    "Vergleichsverhandlung mit der Kieler Volksbank eG",
    ["Nach der Zeugenvernehmung vom 14.01.2014 fuehrten die Parteien Vergleichsgespraeche.",
     "Die Beklagte bietet eine Zahlung von 55.000,00 EUR zur vollstaendigen Erledigung der Anfechtungsklage an, ohne Anerkennung einer Rechtspflicht.",
     "Der Klaeger haelt angesichts der Zeugenaussage eine Erfolgsaussicht von rund 70 % fuer die Klageforderung in voller Hoehe (87.400 EUR), beruecksichtigt jedoch das Prozesskostenrisiko und die Verfahrensdauer.",
     "Einigung auf 62.000,00 EUR, zahlbar bis 15.05.2014."],
    "Protokollfuehrung: RA Dr. Jens-Peter Hartmann, 28.04.2014")

make_docx(BASE/"17_haftungsklage_gf_berger_15b_inso_43_gmbhg.docx", KOPF,
    "Haftungsklage gegen Geschäftsführer Stefan Berger",
    ["An das Landgericht Kiel.",
     "Klaeger: Dr. Jens-Peter Hartmann als Insolvenzverwalter. Beklagter: Stefan Berger, ehemaliger Geschaeftsfuehrer der Nordlicht Handels GmbH.",
     "Antrag: Der Beklagte wird verurteilt, an den Klaeger 64.800,00 EUR zu zahlen.",
     "Begruendung: Der Beklagte hat im Zeitraum vom 15.12.2012 (Eintritt der Zahlungsunfaehigkeit) bis zur Antragstellung am 14.01.2013 Zahlungen an einzelne Lieferanten in Hoehe von insgesamt 64.800,00 EUR geleistet, obwohl die Gesellschaft bereits zahlungsunfaehig war. Diese Zahlungen seien nach dem zum Zeitpunkt der Handlung geltenden § 64 Satz 1 GmbHG a.F. (heute vergleichbar § 15b InsO) zu erstatten.",
     "Az. Landgericht Kiel: 3 O 340/13."],
    "Dr. Jens-Peter Hartmann, Insolvenzverwalter, Kiel, 18.09.2014")

make_docx(BASE/"18_anwaltsschreiben_gf_verteidiger.docx", KOPF,
    "Schreiben des Verteidigers von Stefan Berger",
    ["Sehr geehrter Herr Dr. Hartmann,",
     "namens und in Vollmacht meines Mandanten Stefan Berger nehme ich Stellung zur Haftungsklage.",
     "Mein Mandant bestreitet, zum 15.12.2012 Kenntnis von der Zahlungsunfaehigkeit gehabt zu haben. Die geleisteten Zahlungen seien zur Aufrechterhaltung des Geschaeftsbetriebs erforderlich gewesen und stuenden im Einklang mit der Sorgfalt eines ordentlichen Geschaeftsmanns.",
     "Wir regen an, vor Klageerhebung eine aussergerichtliche Regelung mit Ratenzahlung zu pruefen."],
    "RA Torben Klages, Kanzlei Klages und Partner, Kiel, 30.09.2014")

make_docx(BASE/"19_bilanzanalyse_wp_zahlungsunfaehigkeit.docx", KOPF,
    "Bilanzanalyse der Wirtschaftsprüfung zur Zahlungsunfähigkeit",
    ["Gutachterin: WP Cordula Reimann, Reimann Wirtschaftspruefung Kiel.",
     "Auftrag: Feststellung des Zeitpunkts der Zahlungsunfaehigkeit der Nordlicht Handels GmbH.",
     "Auf Grundlage der Kontoauszuege und der betriebswirtschaftlichen Auswertungen fuer Oktober bis Dezember 2012 stellt die Gutachterin fest, dass die Liquiditaetsluecke ab dem 15.12.2012 mehr als 10 % der faelligen Verbindlichkeiten betrug und auch innerhalb von drei Wochen nicht mehr geschlossen werden konnte.",
     "Die Gesellschaft war damit ab dem 15.12.2012 zahlungsunfaehig im Sinne des § 17 InsO."],
    "Reimann Wirtschaftspruefung, Kiel, 12.06.2014")

make_csv(BASE/"20_liquiditaetsstatus_rueckblickend_6_monate.csv",
    ["Monat","Faellige_Verbindlichkeiten_EUR","Liquide_Mittel_EUR","Deckungsgrad_Prozent"],
    [["2012-07","210000","195000","92.9"],
     ["2012-08","218000","188000","86.2"],
     ["2012-09","225000","172000","76.4"],
     ["2012-10","232000","158000","68.1"],
     ["2012-11","240000","140000","58.3"],
     ["2012-12","248000","118000","47.6"]])

make_docx(BASE/"21_verzichtserklaerung_sozialversicherungstraeger.docx", KOPF,
    "Verzichtserklärung der Sozialversicherungsträger",
    ["Die DAK-Gesundheit und die IKK Nord erklaeren im Rahmen der Vergleichsverhandlungen zur Anfechtung von SV-Beitragszahlungen, auf einen Teilbetrag ihrer Anfechtungsansprueche zu verzichten.",
     "DAK-Gesundheit verzichtet auf 4.200,00 EUR bei Zahlung von 8.400,00 EUR binnen vier Wochen.",
     "IKK Nord verzichtet auf 2.100,00 EUR bei Zahlung von 5.600,00 EUR binnen vier Wochen.",
     "Beide Traeger bestaetigen, dass mit Zahlung der genannten Betraege alle Anfechtungsansprueche des Insolvenzverwalters gegen sie erledigt sind."],
    "DAK-Gesundheit / IKK Nord, Regionaldirektionen, 10.02.2014")

make_docx(BASE/"22_massekostenkalkulation.docx", KOPF,
    "Massekostenkalkulation",
    ["Verguetung Insolvenzverwalter (§ 63 InsO, Regelverguetung nach InsVV): 38.400,00 EUR.",
     "Gerichtskosten: 4.200,00 EUR. Kosten der Wirtschaftspruefung (Bilanzanalyse): 6.800,00 EUR. Sonstige Massekosten (Lagerraeumung, Inventur, Rechtsanwaltskosten Anfechtungsverfahren): 22.400,00 EUR.",
     "Summe Massekosten: 71.800,00 EUR, zu entnehmen vorrangig aus der Insolvenzmasse gemaess § 53 InsO."],
    "Dr. Jens-Peter Hartmann, Kiel, Stand 2019")

make_docx(BASE/"23_verguetungsantrag_verwalter_63_inso.docx", KOPF,
    "Vergütungsantrag des Insolvenzverwalters gemaess Paragraf 63 InsO",
    ["An das Amtsgericht Kiel.",
     "Der Insolvenzverwalter beantragt die Festsetzung seiner Verguetung fuer die Taetigkeit von der Eroeffnung am 01.06.2013 bis zum Antragszeitpunkt.",
     "Berechnungsgrundlage: Regelverguetung nach § 2 InsVV auf Basis der Teilungsmasse von 510.200,00 EUR, zzgl. Zuschlaegen fuer die Fuehrung der Anfechtungsprozesse (15 %) und die lange Verfahrensdauer (10 %).",
     "Beantragte Verguetung: 42.600,00 EUR zzgl. Auslagen und Umsatzsteuer."],
    "Dr. Jens-Peter Hartmann, Kiel, 20.11.2023")

make_docx(BASE/"24_schlussbericht.docx", KOPF,
    "Schlussbericht des Insolvenzverwalters",
    ["Nach elfjaehriger Verfahrensdauer legt der Insolvenzverwalter folgenden Schlussbericht vor.",
     "Die Betriebsfortfuehrung bis 31.08.2013 ermoeglichte einen geordneten Abverkauf der Saisonware. Die Anfechtungsprozesse gegen die Kieler Volksbank eG (Vergleich 62.000 EUR) und die Haftungsklage gegen Stefan Berger (Vergleich mit Ratenzahlung) haben die Masse wesentlich erhoeht.",
     "Endgueltiger Massebestand: 120.462,00 EUR. Die festgestellten Forderungen belaufen sich auf rund 510.200,00 EUR, sodass sich eine Quote von rund 13,5 % ergibt.",
     "Der Bericht wird dem Amtsgericht Kiel zur Vorbereitung des Schlusstermins vorgelegt."],
    "Dr. Jens-Peter Hartmann, Kiel, 15.03.2024")

make_docx(BASE/"25_schlussverzeichnis.docx", KOPF,
    "Schlussverzeichnis der Insolvenzgläubiger",
    ["Das Schlussverzeichnis weist alle festgestellten Forderungen mit Quotenberechnung aus.",
     "Kieler Volksbank eG: Forderung 248.500,00 EUR, Quote 13,5 %, Auszahlung 33.547,50 EUR.",
     "Fashion Forward KG: Forderung 42.380,00 EUR, Quote 13,5 %, Auszahlung 5.721,30 EUR.",
     "DAK-Gesundheit: Forderung 14.540,00 EUR (nach Vergleich), Quote 13,5 %, Auszahlung 1.962,90 EUR.",
     "IKK Nord: Forderung 10.350,00 EUR (nach Vergleich), Quote 13,5 %, Auszahlung 1.397,25 EUR.",
     "Diverse Warenlieferanten: Forderungen zwischen 1.200,00 EUR und 34.200,00 EUR, jeweils Quote 13,5 %."],
    "Dr. Jens-Peter Hartmann, Kiel, 20.03.2024")

make_docx(BASE/"26_aufhebungsbeschluss.docx", KOPF,
    "Aufhebungsbeschluss des Amtsgerichts Kiel",
    ["Amtsgericht Kiel, Az. 10 IN 127/13.",
     "Nach Vollzug der Schlussverteilung wird das Insolvenzverfahren ueber das Vermoegen der Nordlicht Handels GmbH gemaess § 200 InsO aufgehoben.",
     "Die Aufhebung erfolgt mit Wirkung zum 30.04.2024. Der Insolvenzverwalter ist von seinem Amt entbunden.",
     "Eine Nachtragsverteilung wegen einer Steuererstattung des Finanzamts Kiel in Hoehe von 3.180,00 EUR wurde bereits im Schlussbericht beruecksichtigt."],
    "Amtsgericht Kiel, Insolvenzabteilung, 25.04.2024")

print("Nordlicht Kiel: Kernstuecke erzeugt")
