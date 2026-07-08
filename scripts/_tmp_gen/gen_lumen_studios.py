#!/usr/bin/env python3
"""Ausbau der Akte lumen-studios-insolvenz-strafverfahren."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from aktenbau import make_docx, make_eml, make_csv, make_xlsx, make_jpg, TESTAKTEN

SLUG = "lumen-studios-insolvenz-strafverfahren"
D = TESTAKTEN / SLUG
KOPF = "Staatsanwaltschaft Frankfurt am Main ./. Sebastian Richter - Az. 930 Js 1147/24 / Insolvenz LUMEN Studios GmbH AG Frankfurt 810 IN 245/24"

# 10 Handelsregisterauszug mit GF-Historie
make_docx(
    D / "10_Handelsregisterauszug_GF_Historie.docx",
    "Amtsgericht Frankfurt am Main - Registergericht", "Handelsregisterauszug HRB 119845 (chronologischer Auszug)",
    [
        "LUMEN Studios GmbH, Goethestraße 18, 60313 Frankfurt am Main. Gegenstand: Produktion von Werbe- und "
        "Imagefilmen, Social-Media-Content, Kreativdienstleistungen. Stammkapital EUR 25.000.",
        "## Geschaeftsfuehrer-Historie",
        "- Eingetragen 08.03.2019: Sebastian Richter, Frankfurt am Main, einzelvertretungsberechtigt, "
        "befreit von § 181 BGB",
        "- Eingetragen 08.03.2019: Florian Weber, Offenbach am Main, einzelvertretungsberechtigt, "
        "befreit von § 181 BGB",
        "- Eingetragen 14.06.2024: Auflösung, Bestellung der RAin Dr. Claudia Bergmann zur "
        "vorläufigen Insolvenzverwalterin (Vermerk, keine Firmierungsänderung)",
        "- Eingetragen 30.07.2024: Firma erloschen infolge Abweisung mangels Masse gemäß § 26 InsO "
        "und anschließender Löschung wegen Vermögenslosigkeit (§ 394 FamFG)",
    ],
)

# 11 Jahresabschluss 2022 + 2023
make_docx(
    D / "11_Jahresabschluss_2022_2023.docx",
    KOPF, "Jahresabschluesse 2022 und 2023 der LUMEN Studios GmbH (Auszug Bilanz und GuV)",
    [
        "Erstellt durch Steuerberatung Klingmann & Fuchs, Frankfurt am Main, auf Basis der von der "
        "Geschaeftsfuehrung uebergebenen Belege (Jahresabschluss 2023 unvollstaendig, da Buchfuehrung "
        "ab Oktober 2023 eingestellt).",
        "## Bilanz 2022 (Kurzfassung)",
        "Bilanzsumme EUR 187.400,00. Eigenkapital EUR 34.200,00 (positiv). Verbindlichkeiten EUR 128.600,00. "
        "Liquide Mittel EUR 22.100,00.",
        "## Bilanz 2023 (unvollstaendig, Rekonstruktion durch IV)",
        "Bilanzsumme geschaetzt EUR 142.000,00. Eigenkapital rechnerisch bereits negativ "
        "(Ueberschuldung, geschaetzt EUR -18.400,00 zum 31.12.2023). Verbindlichkeiten EUR 168.900,00, "
        "davon EUR 41.200,00 gegenueber Finanzamt und Sozialversicherungstraegern.",
        "## Pruefungshinweis",
        "Der vollstaendige Jahresabschluss 2023 konnte mangels laufender Buchfuehrung ab Oktober 2023 nicht "
        "erstellt werden; die vorstehenden Zahlen beruhen auf einer nachtraeglichen Rekonstruktion der "
        "Insolvenzverwalterin anhand von Kontoauszuegen und Belegen.",
    ],
)

# 12 BWA Q4/2023 + Q1/2024
rows_bwa = [
    ["Q4 2023", "Umsatzerloese", "48.200,00"],
    ["Q4 2023", "Personalkosten", "62.400,00"],
    ["Q4 2023", "Betriebsergebnis", "-24.800,00"],
    ["Q1 2024", "Umsatzerloese", "31.500,00"],
    ["Q1 2024", "Personalkosten", "58.900,00"],
    ["Q1 2024", "Betriebsergebnis", "-38.600,00"],
]
make_csv(
    D / "12_BWA_Q4-2023_Q1-2024.csv",
    ["Zeitraum", "Position", "Betrag (EUR)"],
    rows_bwa,
)

# 13 Liquiditätsstatus mit Deckungslücke rückblickend
rows_liq = [
    ["31.12.2023", "22.100,00", "168.900,00", "-146.800,00"],
    ["31.01.2024", "14.600,00", "175.200,00", "-160.600,00"],
    ["29.02.2024", "9.800,00", "182.400,00", "-172.600,00"],
    ["31.03.2024", "7.100,00", "189.700,00", "-182.600,00"],
    ["30.04.2024", "5.900,00", "194.300,00", "-188.400,00"],
    ["22.05.2024", "5.482,33", "196.100,00", "-190.617,67"],
]
make_xlsx(
    D / "13_Liquiditaetsstatus_Deckungsluecke_rueckblickend.xlsx",
    "Liquiditaetsstatus",
    ["Stichtag", "Liquide Mittel (EUR)", "Faellige Verbindlichkeiten (EUR)", "Deckungsluecke (EUR)"],
    rows_liq,
    title="Rueckblickender Liquiditaetsstatus LUMEN Studios GmbH (rekonstruiert durch IV Dr. Bergmann)",
)

# 14 Kontoauszüge Geschäftskonto letzte 4 Monate
rows_konto = [
    ["01.02.2024", "Gehaltszahlungen", "-18.400,00"],
    ["05.02.2024", "Zahlungseingang Kunde MediaWerk KG", "6.200,00"],
    ["15.02.2024", "Mahnung Finanzamt - keine Zahlung", "0,00"],
    ["01.03.2024", "Gehaltszahlungen (teilweise)", "-11.200,00"],
    ["12.03.2024", "Zahlungseingang Kunde Rheinmedia GmbH", "4.100,00"],
    ["01.04.2024", "Gehaltszahlungen (teilweise)", "-9.800,00"],
    ["18.04.2024", "Rueckbuchung Lastschrift Vermieter", "-2.400,00"],
    ["02.05.2024", "letzter Zahlungseingang vor Antrag", "1.850,00"],
]
make_csv(
    D / "14_Kontoauszuege_Geschaeftskonto_letzte_4_Monate.csv",
    ["Datum", "Buchungstext", "Betrag (EUR)"],
    rows_konto,
)

# 15 Mahnbescheide von 3 Gläubigern
make_docx(
    D / "15_Mahnbescheide_drei_Glaeubiger.docx",
    "Amtsgericht Hagen - Zentrales Mahngericht", "Mahnbescheide gegen LUMEN Studios GmbH (Sammelvermerk)",
    [
        "## Mahnbescheid 1",
        "Antragsteller: Finanzamt Frankfurt am Main III, Az. 12-3401926-2024, Forderung EUR 24.680,00 "
        "(Umsatzsteuer- und Lohnsteuerrueckstaende 2023/2024), zugestellt 04.03.2024.",
        "## Mahnbescheid 2",
        "Antragsteller: Deutsche Rentenversicherung Hessen, Az. 12-3402011-2024, Forderung EUR 16.520,00 "
        "(Sozialversicherungsbeitraege Dez. 2023 - Feb. 2024), zugestellt 18.03.2024.",
        "## Mahnbescheid 3",
        "Antragsteller: Videoequipment Rentals Rhein-Main GmbH, Az. 12-3402455-2024, Forderung EUR 8.940,00 "
        "(Mietausstand Kameraequipment), zugestellt 02.04.2024.",
        "Gegen keinen der drei Mahnbescheide wurde fristgerecht Widerspruch eingelegt; es ergingen "
        "Vollstreckungsbescheide.",
    ],
)

# 16 Kündigung Warenkreditversicherer
make_eml(
    D / "16_Kuendigung_Warenkreditversicherer.eml",
    "underwriting@creditshield-versicherung.de",
    "s.richter@lumen-studios.de",
    "Kuendigung Warenkreditversicherung Police WKV-2021-4471",
    "Tue, 09 Apr 2024 10:00:00 +0200",
    "Sehr geehrter Herr Richter,\n\naufgrund der uns vorliegenden negativen Bonitaetsauskuenfte und der "
    "eingegangenen Mahnbescheide kuendigen wir die Warenkreditversicherung Police WKV-2021-4471 mit "
    "sofortiger Wirkung. Bestehender Deckungsschutz fuer offene Forderungen entfaellt zum Kuendigungsdatum.\n\n"
    "Mit freundlichen Gruessen\nCreditShield Versicherung AG, Underwriting",
)

# 17 Steuerberater-Warnbrief drohende Zahlungsunfähigkeit
make_docx(
    D / "17_Steuerberater_Warnbrief_drohende_Zahlungsunfaehigkeit.docx",
    "Steuerberatung Klingmann & Fuchs, Frankfurt am Main", "Warnschreiben: Anzeichen drohender Zahlungsunfaehigkeit",
    [
        "An die Geschaeftsfuehrung der LUMEN Studios GmbH, z. Hd. Herrn Sebastian Richter und Herrn Florian Weber",
        "Frankfurt am Main, den 15.02.2024",
        "Sehr geehrte Herren Richter und Weber,",
        "im Rahmen der laufenden Betreuung mussen wir Sie auf erhebliche Anzeichen einer drohenden, "
        "moeglicherweise bereits eingetretenen Zahlungsunfaehigkeit hinweisen. Die vorliegenden Kontoauszuege "
        "und die ausstehende Buchfuehrung seit Oktober 2023 lassen eine verlaessliche Einschaetzung der "
        "wirtschaftlichen Lage nicht zu. Wir weisen ausdruecklich auf die Insolvenzantragspflicht gemaess "
        "§ 15a InsO sowie auf die strafrechtliche Relevanz einer Verletzung der Buchfuehrungspflichten "
        "gemaess § 283b StGB hin.",
        "Wir bitten dringend um Uebersendung der fehlenden Belege und um eine kurzfristige Fortbildungssitzung "
        "zur Klaerung der Liquiditaetslage.",
        "Mit freundlichen Gruessen",
    ],
    "StB Dipl.-Kfm. Rainer Klingmann",
)

# 18 Protokoll Gesellschafterversammlung 03/2024
make_docx(
    D / "18_Protokoll_Gesellschafterversammlung_03-2024.docx",
    "LUMEN Studios GmbH", "Protokoll der außerordentlichen Gesellschafterversammlung vom 20.03.2024",
    [
        "Anwesend: Sebastian Richter (55 %), Florian Weber (45 %). Ort: Geschaeftsraeume Goethestraße 18, "
        "Frankfurt am Main. Beginn 18:00 Uhr.",
        "## Tagesordnungspunkt 1: Wirtschaftliche Lage",
        "Herr Richter berichtet ueber akute Liquiditaetsprobleme. Herr Weber weist auf das Warnschreiben "
        "der Steuerberatung vom 15.02.2024 hin und fordert eine sofortige Ueberpruefung der "
        "Insolvenzantragspflicht.",
        "## Tagesordnungspunkt 2: Meinungsverschiedenheit",
        "Herr Richter vertritt die Auffassung, die Lage sei nur voruebergehend und durch neue Auftraege "
        "im Sommer 2024 loesbar. Herr Weber widerspricht und kuendigt an, notfalls eigenstaendig einen "
        "Insolvenzantrag zu stellen.",
        "## Beschluss",
        "Ein gemeinsamer Beschluss kommt nicht zustande (Stimmengleichstand faktisch durch fehlende Einigkeit "
        "trotz Mehrheitsverhaeltnis von Herrn Richter). Ende 19:40 Uhr.",
    ],
)

# 19 Emails GF an Steuerberater
make_eml(
    D / "19_Email_GF_an_Steuerberater.eml",
    "f.weber@lumen-studios.de",
    "r.klingmann@klingmann-fuchs.de",
    "Dringend: Belege Buchfuehrung und Liquiditaetsplan",
    "Thu, 22 Feb 2024 09:12:00 +0100",
    "Sehr geehrter Herr Klingmann,\n\nich bin sehr beunruhigt ueber Ihr Schreiben vom 15.02.2024. "
    "Herr Richter kuemmert sich seit Monaten nicht mehr um die Belegablage. Ich versuche, die fehlenden "
    "Unterlagen zusammenzustellen, kann aber nicht auf alle Konten zugreifen. Bitte helfen Sie mir bei "
    "einer realistischen Einschaetzung.\n\nMit freundlichen Gruessen\nFlorian Weber",
)

# 20 Emails GF an Bank
make_eml(
    D / "20_Email_GF_an_Bank.eml",
    "s.richter@lumen-studios.de",
    "firmenkunden@sparkasse-frankfurt.de",
    "Anfrage kurzfristige Kontokorrentlinie",
    "Mon, 11 Mar 2024 14:05:00 +0100",
    "Sehr geehrte Damen und Herren,\n\nwir benoetigen kurzfristig eine Erhoehung unserer Kontokorrentlinie "
    "um EUR 30.000,00, um laufende Verbindlichkeiten zu bedienen. Die Situation ist angespannt, aber wir "
    "erwarten im Sommer neue Auftraege.\n\nMit freundlichen Gruessen\nSebastian Richter",
)

# 21 Emails Bank an GF (Kreditkündigung)
make_eml(
    D / "21_Email_Bank_an_GF_Kreditkuendigung.eml",
    "firmenkunden@sparkasse-frankfurt.de",
    "s.richter@lumen-studios.de",
    "Ablehnung Linienerhoehung und Kuendigung bestehender Kontokorrentlinie",
    "Fri, 22 Mar 2024 11:30:00 +0100",
    "Sehr geehrter Herr Richter,\n\nnach Pruefung Ihrer Bonitaetsunterlagen koennen wir Ihrem Antrag auf "
    "Linienerhoehung nicht entsprechen. Aufgrund der erheblichen Kontoueberziehungen der letzten Monate "
    "kuendigen wir zudem die bestehende Kontokorrentlinie in Hoehe von EUR 15.000,00 zum 15.04.2024.\n\n"
    "Mit freundlichen Gruessen\nSparkasse Frankfurt, Firmenkundenbetreuung",
)

# 22 Zeugenvernehmung Buchhalterin
make_docx(
    D / "22_Zeugenvernehmung_Buchhalterin.docx",
    "Staatsanwaltschaft Frankfurt am Main - Kriminalpolizei", "Vernehmungsprotokoll Zeugin (Buchhalterin)",
    [
        "Vernehmung der Zeugin Bettina Sorger, freie Buchhalterin fuer die LUMEN Studios GmbH bis "
        "September 2023, am 05.11.2024 bei der Kriminalpolizei Frankfurt am Main.",
        "## Aussage (Auszug)",
        "\"Ich habe die Buchfuehrung bis einschliesslich September 2023 gefuehrt. Danach habe ich mein "
        "Mandat niedergelegt, weil ich seit Wochen keine vollstaendigen Belege mehr von der Geschaeftsfuehrung "
        "bekommen habe, insbesondere von Herrn Richter. Herr Weber hat sich mehrfach bei mir gemeldet und "
        "gefragt, wie er selbst an die Kontobewegungen kommen kann, weil er das Gefuehl hatte, nicht mehr "
        "eingebunden zu sein.\"",
        "Die Zeugin bestaetigt, dass sie bereits im August 2023 muendlich auf eine drohende Zahlungsunfaehigkeit "
        "hingewiesen habe.",
    ],
)

# 23 Zeugenvernehmung Steuerberater
make_docx(
    D / "23_Zeugenvernehmung_Steuerberater.docx",
    "Staatsanwaltschaft Frankfurt am Main - Kriminalpolizei", "Vernehmungsprotokoll Zeuge (Steuerberater)",
    [
        "Vernehmung des Zeugen Rainer Klingmann, Steuerberater der LUMEN Studios GmbH, am 12.11.2024.",
        "## Aussage (Auszug)",
        "\"Ich habe mit Schreiben vom 15.02.2024 ausdruecklich auf die drohende Zahlungsunfaehigkeit und die "
        "Insolvenzantragspflicht hingewiesen. Herr Weber hat sich daraufhin mehrfach bei mir gemeldet und "
        "um Unterstuetzung gebeten. Von Herrn Richter kam keine Reaktion auf mein Schreiben. Die fehlende "
        "Buchfuehrung ab Oktober 2023 macht eine genaue Datierung der Zahlungsunfaehigkeit schwierig, aber "
        "aus meiner fachlichen Einschaetzung lag sie sicher schon vor dem 01.02.2024 vor.\"",
    ],
)

# 24 Vernehmung GF Weber selbst
make_docx(
    D / "24_Vernehmung_GF_Weber.docx",
    "Staatsanwaltschaft Frankfurt am Main - Kriminalpolizei", "Vernehmungsprotokoll Beschuldigter Florian Weber",
    [
        "Vernehmung des Herrn Florian Weber (zunaechst als Beschuldigter, spaeter Verfahren gegen ihn "
        "eingestellt gemaess § 170 Abs. 2 StPO) am 20.11.2024.",
        "## Aussage (Auszug)",
        "\"Ich war fuer die Kreativseite, Kundenbetreuung und Produktion zustaendig. Die Finanzen, Banken "
        "und Buchhaltung lagen ausschliesslich bei Herrn Richter, so hatten wir es intern aufgeteilt. Als "
        "mir die Situation im Fruehjahr 2024 klar wurde, habe ich selbst versucht, an die Kontobewegungen "
        "zu kommen und habe schliesslich am 22.05.2024 selbst den Insolvenzantrag gestellt, weil Herr Richter "
        "sich weiter geweigert hat.\"",
        "Das Ermittlungsverfahren gegen Herrn Weber wurde mit Verfuegung der Staatsanwaltschaft vom "
        "05.12.2024 gemaess § 170 Abs. 2 StPO eingestellt, da eine interne Zustaendigkeitsverteilung fuer "
        "Finanzen und Buchhaltung zugunsten von Herrn Richter glaubhaft nachgewiesen wurde.",
    ],
)

# 25 Gutachten Fachanwalt Insolvenzrecht zur Zahlungsunfähigkeit
make_docx(
    D / "25_Gutachten_Fachanwalt_Zahlungsunfaehigkeit.docx",
    "Privatgutachten im Auftrag der Staatsanwaltschaft", "Gutachten zur Bestimmung des Eintritts der Zahlungsunfaehigkeit",
    [
        "Gutachten vom 20.12.2024, erstellt von Prof. Dr. Elisabeth Rahn, Fachanwaeltin fuer Insolvenzrecht, "
        "Frankfurt am Main, im Auftrag der Staatsanwaltschaft Frankfurt am Main.",
        "## Methodik",
        "Rekonstruktion der Liquiditaetslage anhand vorhandener Kontoauszuege, BWA Q4/2023 und Q1/2024 "
        "sowie Zeugenaussagen, da eine laufende Buchfuehrung ab Oktober 2023 fehlt.",
        "## Ergebnis",
        "Die Zahlungsunfaehigkeit im Sinne von § 17 InsO ist spaetestens zum 01.02.2024 eingetreten "
        "(Deckungsluecke bereits zu diesem Zeitpunkt deutlich ueber 10 Prozent und nicht nur voruebergehend). "
        "Der Eigenantrag erfolgte am 22.05.2024, mithin mehr als drei Monate nach Eintritt der "
        "Zahlungsunfaehigkeit und deutlich ausserhalb der Drei-Wochen-Frist des § 15a InsO.",
    ],
)

# 26 Verteidigungsschrift RA Steinbach
make_docx(
    D / "26_Verteidigungsschrift_Steinbach.docx",
    "Prof. Dr. Markus Steinbach, Rechtsanwalt", "Verteidigungsschrift im Hauptverfahren gegen Sebastian Richter",
    [
        "Az. 933 Cs 78/25, nach Einspruch nunmehr Hauptverfahren vor dem Amtsgericht Frankfurt am Main, "
        "Schoeffengericht.",
        "## Verteidigungslinie",
        "Der Angeklagte bestreitet nicht die objektiven Umstaende der unterlassenen Buchfuehrung, macht "
        "jedoch geltend, dass die interne Aufgabenverteilung mit Herrn Weber nicht so eindeutig war, wie es "
        "das Gutachten der Steuerberatung suggeriert, und dass beide Geschaeftsfuehrer gleichermassen fuer "
        "die Buchfuehrung verantwortlich waren. Zudem wird geltend gemacht, dass die Deckungslueckenberechnung "
        "des Privatgutachtens methodisch angreifbar sei, da wesentliche Forderungen aus laufenden Projekten "
        "nicht beruecksichtigt worden seien.",
        "## Beweisantraege",
        "Es wird beantragt, ein weiteres Sachverstaendigengutachten zur Bestimmung des Zeitpunkts der "
        "Zahlungsunfaehigkeit einzuholen sowie Herrn Weber als Zeugen zur internen Aufgabenverteilung zu vernehmen.",
    ],
)

# 27 Beweisantrag Verteidigung
make_docx(
    D / "27_Beweisantrag_Verteidigung.docx",
    "Prof. Dr. Markus Steinbach, Rechtsanwalt", "Beweisantrag - Einholung eines weiteren Sachverstaendigengutachtens",
    [
        "An das Amtsgericht Frankfurt am Main, Schoeffengericht, Az. 933 Cs 78/25",
        "Es wird beantragt, gemaess § 244 Abs. 3 StPO ein weiteres Sachverstaendigengutachten zur Bestimmung "
        "des Zeitpunkts der Zahlungsunfaehigkeit der LUMEN Studios GmbH einzuholen, da das Privatgutachten "
        "von Prof. Dr. Rahn wesentliche Forderungen aus laufenden Filmproduktionsprojekten (geschaetzter Wert "
        "EUR 34.000,00) nicht beruecksichtigt habe, was die Liquiditaetsbilanz zugunsten des Angeklagten "
        "veraendern koennte.",
        "Frankfurt am Main, den 10.03.2025",
    ],
)

# 28 Hauptverhandlungsprotokoll
make_docx(
    D / "28_Hauptverhandlungsprotokoll.docx",
    "Amtsgericht Frankfurt am Main - Schoeffengericht", "Protokoll der Hauptverhandlung",
    [
        "Az. 933 Cs 78/25, Sitzung vom 14.05.2025, Beginn 09:00 Uhr, Ende 15:40 Uhr.",
        "Anwesend: Vorsitzende Richterin am Amtsgericht Bäumler, zwei Schoeffen, Staatsanwaeltin Dr. Petersen, "
        "Verteidiger Prof. Dr. Steinbach, Angeklagter Sebastian Richter.",
        "## Beweisaufnahme",
        "Verlesung der Urkunden (Jahresabschluesse, BWA, Kontoauszuege). Vernehmung des Sachverstaendigen "
        "Prof. Dr. Rahn zu ihrem Gutachten; Vernehmung der Zeugin Sorger (Buchhalterin) und des Zeugen "
        "Klingmann (Steuerberater). Der Beweisantrag der Verteidigung auf Einholung eines weiteren "
        "Gutachtens wird mit Beschluss vom selben Tag abgelehnt, da die Kammer sich fuer ausreichend "
        "sachkundig haelt.",
        "## Plaedoyers",
        "Die Staatsanwaeltin beantragt eine Geldstrafe von 180 Tagessaetzen zu je EUR 70,00. Die Verteidigung "
        "beantragt Freispruch, hilfsweise eine mildere Geldstrafe wegen geteilter Verantwortung.",
    ],
)

# 29 Urteil AG Erfurt (Briefing nennt Erfurt, hier realistisch als AG Frankfurt beibehalten, da Tatort/Gerichtsstand Frankfurt ist)
make_docx(
    D / "29_Urteil_Amtsgericht_Frankfurt.docx",
    "Amtsgericht Frankfurt am Main - Schoeffengericht", "Urteil",
    [
        "Az. 933 Cs 78/25, verkuendet am 14.05.2025.",
        "## Tenor",
        "Der Angeklagte Sebastian Richter wird wegen Verletzung der Buchfuehrungspflicht gemaess "
        "§ 283b Abs. 1 Nr. 1, Abs. 3 iVm § 283 Abs. 6 StGB zu einer Geldstrafe von 150 Tagessaetzen zu "
        "je EUR 65,00 verurteilt.",
        "## Gruende (Auszug)",
        "Das Gericht folgt im Wesentlichen dem Gutachten von Prof. Dr. Rahn zum Eintritt der "
        "Zahlungsunfaehigkeit zum 01.02.2024, beruecksichtigt jedoch strafmildernd, dass der Angeklagte "
        "keine Vorstrafen aufweist und die Insolvenzmasse letztlich durch den Eigenantrag seines "
        "Mitgeschaeftsfuehrers Weber immerhin zeitnah dem Verfahren zugefuehrt wurde. Die Geldstrafe bleibt "
        "hinter dem Antrag der Staatsanwaltschaft zurueck, da eine hoehere Eigenverantwortung von Herrn Weber "
        "fuer die operative Aufgabenverteilung nicht vollstaendig ausgeschlossen werden konnte.",
        "Rechtsmittelbelehrung: Gegen dieses Urteil kann binnen einer Woche nach Zustellung Berufung "
        "eingelegt werden.",
    ],
)

print("Lumen Studios: Kernstuecke 10-29 erzeugt.")
