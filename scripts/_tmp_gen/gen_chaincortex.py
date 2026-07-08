#!/usr/bin/env python3
"""Ausbau der Akte insolvenz-asset-deal-chaincortex-ai-berlin."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from aktenbau import make_docx, make_eml, make_csv, make_xlsx, TESTAKTEN

SLUG = "insolvenz-asset-deal-chaincortex-ai-berlin"
D = TESTAKTEN / SLUG
KOPF = "Vorberg + Steinhausen Rechtsanwaelte mbB - Insolvenzverwaltung ChainCortex AI GmbH, AG Charlottenburg 36 IN 1342/26"

# 12 Kaufpreiszahlung Nachweis / Treuhandkonto
rows_kp = [
    ["01.07.2026", "Eingang Kaufpreis 1. Rate", "280.000,00"],
    ["15.07.2026", "Eingang Kaufpreis 2. Rate (Retention Release Teil 1)", "80.000,00"],
    ["01.10.2026", "Eingang Kaufpreis 3. Rate (Retention Release Teil 2, nach Gewaehrleistungsfrist)", "40.000,00"],
]
make_csv(
    D / "12_kaufpreiszahlungen_treuhandkonto.csv",
    ["Datum", "Position", "Betrag (EUR)"],
    rows_kp,
)

# 13 Massekostenkalkulation nach Closing
rows_mk = [
    ["Kaufpreis gesamt (netto)", "400.000,00"],
    ["abzgl. Massekostenbeitrag Feststellung 4%", "-16.000,00"],
    ["abzgl. Kosten DD und Transaktionsberatung", "-38.500,00"],
    ["abzgl. Notarkosten (anteilig Masse)", "-4.200,00"],
    ["Nettoerloes zur Verteilung an Glaeubiger", "341.300,00"],
]
make_xlsx(
    D / "13_massekostenkalkulation_nach_closing.xlsx",
    "Massekosten",
    ["Position", "Betrag (EUR)"],
    rows_mk,
    title="Massekostenkalkulation nach Vollzug des Asset Deals",
)

# 14 Übernahmebestätigung Arbeitnehmer § 613a BGB (Sammelschreiben)
make_docx(
    D / "14_uebernahmebestaetigung_arbeitnehmer_613a.docx",
    KOPF, "Bestaetigungsschreiben an uebergehende Arbeitnehmer gemaess § 613a BGB",
    [
        "Sammelschreiben vom 02.07.2026 an die zehn von Voracis Ventures GmbH uebernommenen Arbeitnehmer "
        "der ChainCortex AI GmbH (i.L.), mit Bestaetigung des Betriebsuebergangs zum 01.07.2026 sowie "
        "Belehrung ueber das Widerspruchsrecht gemaess § 613a Abs. 6 BGB.",
        "Zwei Arbeitnehmer (Frontend-Entwicklerin und eine Compliance-Analystin) haben mit Schreiben vom "
        "08.07.2026 bzw. 10.07.2026 dem Betriebsuebergang widersprochen und verbleiben in der Insolvenzmasse; "
        "fuer diese wird betriebsbedingte Kuendigung durch den Insolvenzverwalter geprueft.",
    ],
)

# 15 Widerspruch Arbeitnehmerin
make_eml(
    D / "15_widerspruch_arbeitnehmerin_betriebsuebergang.eml",
    "j.thalberg@chaincortex-ai.de",
    "m.reuter@vorberg-steinhausen.de",
    "Widerspruch gegen Betriebsuebergang gemaess § 613a Abs. 6 BGB",
    "Wed, 08 Jul 2026 16:20:00 +0200",
    "Sehr geehrter Herr Reuter,\n\nhiermit widerspreche ich fristgerecht dem Uebergang meines "
    "Arbeitsverhaeltnisses auf die Voracis Ventures GmbH gemaess § 613a Abs. 6 BGB. Ich habe bereits "
    "eine neue Stelle in Aussicht und moechte nicht bei der Erwerberin verbleiben.\n\n"
    "Mit freundlichen Gruessen\nJette Thalberg",
)

# 16 Betriebsbedingte Kündigung verbleibender AN
make_docx(
    D / "16_kuendigung_verbleibender_arbeitnehmer_betriebsbedingt.docx",
    KOPF, "Betriebsbedingte Kuendigung fuer widersprechende Arbeitnehmer",
    [
        "Da die ChainCortex AI GmbH (i.L.) nach dem Asset Deal ueber keinen operativen Geschaeftsbetrieb "
        "mehr verfuegt, spricht der Insolvenzverwalter gegenueber den beiden widersprechenden Arbeitnehmern "
        "(Frau Thalberg und Frau Okonkwo) fristgerecht betriebsbedingte Kuendigungen zum naechstmoeglichen "
        "Termin unter Berücksichtigung der insolvenzrechtlichen Kuendigungsfrist gemaess § 113 InsO aus.",
        "Kuendigungsschreiben vom 15.07.2026, Kuendigungsfrist 3 Monate zum Monatsende (§ 113 Satz 2 InsO).",
    ],
)

# 17 DPMA-Markenübertragung Bestätigung
make_docx(
    D / "17_dpma_markenuebertragung_bestaetigung.docx",
    "Deutsches Patent- und Markenamt (DPMA)", "Bestaetigung der Umschreibung der Marken 'ChainCortex' und 'BlockSight'",
    [
        "Bestaetigung vom 22.07.2026 ueber die Umschreibung der Markenrechte DE Nr. 30 2019 123456 "
        "('ChainCortex') und DE Nr. 30 2020 987654 ('BlockSight') von der ChainCortex AI GmbH (i.L.) auf "
        "die Voracis Ventures GmbH gemaess Umschreibungsantrag vom 05.07.2026.",
    ],
)

# 18 Datenschutz-Übernahmevereinbarung Kundendaten
make_docx(
    D / "18_datenuebernahmevereinbarung_dsgvo.docx",
    KOPF, "Vereinbarung zur datenschutzkonformen Uebernahme der Kundendaten (Anlage zum APA)",
    [
        "Vereinbarung vom 28.06.2026 zwischen dem Insolvenzverwalter und der Voracis Ventures GmbH ueber "
        "die Uebertragung der Kundendatenbestaende (B2B ca. 340 Kunden, B2C ca. 1.850 Nutzerkonten).",
        "## Regelungsinhalt",
        "Uebernahme erfolgt auf Grundlage berechtigten Interesses gemaess Art. 6 Abs. 1 lit. f DSGVO im "
        "Rahmen der Unternehmensveraeusserung; betroffene Personen werden binnen 30 Tagen nach Closing per "
        "E-Mail und Website-Hinweis ueber den Wechsel des Verantwortlichen informiert und auf ihr "
        "Widerspruchsrecht hingewiesen.",
        "Die B2C-Nutzerkonten mit Opt-out innerhalb der Frist (17 Konten) werden vor Uebertragung geloescht "
        "bzw. anonymisiert.",
    ],
)

# 19 Gewährleistungsanspruch Käufer (Post-Closing-Streit)
make_eml(
    D / "19_gewaehrleistungsanspruch_kaeuferin_mangel_software.eml",
    "t.strehlemann@strehlemann-karawane.de",
    "k.vorberg@vorberg-steinhausen.de",
    "Gewaehrleistungsanspruch - Mangel Software-Repository BlockSight-Core",
    "Mon, 24 Aug 2026 11:15:00 +0200",
    "Sehr geehrter Herr Dr. Vorberg,\n\nunsere Mandantin hat nach Closing festgestellt, dass das "
    "Software-Repository 'BlockSight-Core' entgegen den vertraglichen Zusicherungen ungeloeste "
    "Lizenzkonflikte mit einer Open-Source-Komponente (GPL-Kollision) aufweist. Wir behalten uns "
    "Gewaehrleistungsansprueche in Hoehe von bis zu EUR 45.000,00 vor und bitten um Stellungnahme "
    "binnen zwei Wochen.\n\nMit freundlichen Gruessen\nRA Tobitz Strehlemann",
)

# 20 Stellungnahme IV zum Gewährleistungsanspruch
make_docx(
    D / "20_stellungnahme_iv_gewaehrleistung.docx",
    KOPF, "Stellungnahme des Insolvenzverwalters zum Gewaehrleistungsanspruch",
    [
        "Stellungnahme vom 05.09.2026 von RA Dr. Konrad Vorberg zum Schreiben der Kaeuferin vom 24.08.2026.",
        "Der Insolvenzverwalter weist darauf hin, dass im Asset-Purchase-Agreement eine Gewaehrleistung "
        "fuer Rechtsmaengel an der Software ausdruecklich nur bis zur Hoehe des zurueckbehaltenen "
        "Kaufpreisanteils (Retention, EUR 40.000,00) uebernommen wurde (§ 9 APA). Eine darueberhinausgehende "
        "Haftung der insolventen Masse kommt nicht in Betracht. Es wird vorgeschlagen, den Retention-Betrag "
        "zur Abgeltung des Anspruchs einzubehalten, sofern der Mangel durch ein neutrales Gutachten bestaetigt wird.",
    ],
)

# 21 IT-Gutachten Lizenzkonflikt
make_docx(
    D / "21_it-gutachten_lizenzkonflikt_gpl.docx",
    "Sachverstaendigenbuero Dr. Feldkamp, IT-Recht und Softwareforensik", "Kurzgutachten zum behaupteten GPL-Lizenzkonflikt",
    [
        "Gutachten vom 20.09.2026, erstellt von Dr.-Ing. Malte Feldkamp auf gemeinsamen Auftrag beider Parteien.",
        "## Ergebnis",
        "Der geruegte Lizenzkonflikt betrifft eine einzelne, nicht produktionskritische Hilfsbibliothek, "
        "die mit vertretbarem Aufwand (geschaetzt 2 Personentage) durch eine lizenzkonforme Alternative "
        "ersetzt werden kann. Der wirtschaftliche Schaden wird auf EUR 6.500,00 geschaetzt, deutlich unter "
        "dem urspruenglich geltend gemachten Betrag von EUR 45.000,00.",
    ],
)

# 22 Einigung Retention-Freigabe
make_docx(
    D / "22_einigung_retention_freigabe_reduziert.docx",
    KOPF, "Einigung ueber die Freigabe des Retention-Betrags (reduziert)",
    [
        "Einigung vom 01.10.2026 zwischen Insolvenzverwalter und Voracis Ventures GmbH: Von dem einbehaltenen "
        "Retention-Betrag in Hoehe von EUR 40.000,00 werden EUR 6.500,00 zur Abgeltung des Gewaehrleistungs- "
        "anspruchs an die Kaeuferin ausgekehrt; die restlichen EUR 33.500,00 werden zeitgleich an die "
        "Insolvenzmasse freigegeben (siehe Kaufpreiszahlungen Nr. 12).",
    ],
)

# 23 Schlussverzeichnis / Verteilungsverzeichnis
rows_vert = [
    ["Berliner Mittelstandsbank AG (Absonderung)", "185.400,00"],
    ["Finanzamt Berlin-Mitte", "42.800,00"],
    ["Deutsche Rentenversicherung Bund", "18.900,00"],
    ["Ungesicherte Insolvenzglaeubiger (Quote ca. 22 %)", "94.200,00"],
]
make_csv(
    D / "23_verteilungsverzeichnis_auszug.csv",
    ["Glaeubiger/Gruppe", "Betrag (EUR)"],
    rows_vert,
)

# 24 Schlussbericht Insolvenzverwalter
make_docx(
    D / "24_schlussbericht_insolvenzverwalter.docx",
    KOPF, "Schlussbericht des Insolvenzverwalters",
    [
        "Schlussbericht vom 15.10.2026 zur Vorlage beim AG Charlottenburg.",
        "Der Insolvenzverwalter berichtet ueber den erfolgreichen Vollzug des Asset Deals mit der "
        "Voracis Ventures GmbH, die Erledigung der Post-Closing-Anzeigen, die Beilegung des "
        "Gewaehrleistungsstreits sowie die abschliessende Verteilung des Massevermoegens an die "
        "Glaeubiger. Die Quote fuer ungesicherte Insolvenzglaeubiger betraegt rechnerisch rund 22 Prozent.",
    ],
)

# 25 Aufhebungsbeschluss
make_docx(
    D / "25_aufhebungsbeschluss_ag_charlottenburg.docx",
    "Amtsgericht Charlottenburg - Insolvenzgericht", "Beschluss ueber die Aufhebung des Insolvenzverfahrens",
    [
        "Az. 36 IN 1342/26",
        "Nach Vollzug der Schlussverteilung wird das Insolvenzverfahren ueber das Vermoegen der "
        "ChainCortex AI GmbH gemaess § 200 InsO aufgehoben.",
        "Berlin, den 05.11.2026",
    ],
)

print("ChainCortex: Kernstuecke 12-25 erzeugt.")
