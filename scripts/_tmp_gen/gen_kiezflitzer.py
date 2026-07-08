#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Erzeugt Aktenstuecke 19-25 fuer die Kiezflitzer-Akte (Klageverfahren)."""
import sys
sys.path.insert(0, "/home/user/workspace/legal-work/target/scripts/_tmp_gen")
from aktenbau import make_docx, TESTAKTEN

BASE = TESTAKTEN / "insolvenzanfechtung-kiezflitzer-gesellschafterdarlehen-berlin"

KOPF_VERWALTERIN = "Dr. Gesa Trux, Rechtsanwaeltin und Insolvenzverwalterin | Kurfuerstendamm 178, 10707 Berlin"
KOPF_GEGNER = "Rechtsanwalt Dr. Selim Okatan | Torstrasse 55, 10119 Berlin"
KOPF_GERICHT = "Landgericht Berlin, Kammer fuer Handelssachen"

# 19 Klageschrift
make_docx(
    BASE / "19_klageschrift_lg_berlin_2026-09-01.docx",
    KOPF_VERWALTERIN,
    "Klageschrift",
    [
        "An das Landgericht Berlin, Kammer fuer Handelssachen",
        "",
        "In dem Rechtsstreit",
        "Dr. Gesa Trux als Insolvenzverwalterin ueber das Vermoegen der Kiezflitzer Mobility GmbH, Weserstrasse 168, 12045 Berlin",
        "- Klaegerin -",
        "gegen",
        "Dr. Valentin Brosekamp, Berlin",
        "- Beklagter -",
        "",
        "wegen Insolvenzanfechtung (Streitwert: 185.230,00 EUR)",
        "",
        "erhebe ich namens und in Vollmacht der Klaegerin Klage und werde beantragen:",
        "1. Der Beklagte wird verurteilt, an die Klaegerin 165.230,00 EUR nebst Zinsen in Hoehe von fuenf Prozentpunkten ueber dem Basiszinssatz seit Rechtshaengigkeit zu zahlen.",
        "2. Der Beklagte traegt die Kosten des Rechtsstreits.",
        "## Sachverhalt",
        "Der Beklagte war zu 20 % an der Schuldnerin beteiligt und zugleich im Rahmen eines Beratervertrags 'Interim Finance Advisory' fuer sie taetig. Im Dezember 2024 erhielt er die Rueckzahlung eines Gesellschafterdarlehens ueber 150.000,00 EUR. Im September 2025 wurde seine Beraterrechnung ueber 20.230,00 EUR fuer im Juli und August 2025 nachweislich geleistete Arbeit beglichen. Im Oktober 2025 erhielt er zudem einen vertraglich nicht vorgesehenen Vorschuss von 15.000,00 EUR.",
        "Der Eigenantrag der Schuldnerin datiert vom 14.11.2025. Das im Eroeffnungsverfahren eingeholte Gutachten stellt eine Ueberschuldung bereits zum 30.06.2025 und Zahlungsunfaehigkeit zum 01.09.2025 fest.",
        "## Rechtliche Wuerdigung",
        "Die Darlehensrueckzahlung von 150.000,00 EUR unterliegt der Anfechtung nach § 135 Abs. 1 Nr. 2 InsO, da sie innerhalb eines Jahres vor dem Eroeffnungsantrag erfolgte. Auf eine Kenntnis des Beklagten kommt es hierfuer nicht an. Das Kleinbeteiligtenprivileg des § 39 Abs. 5 InsO greift bei einer Beteiligung von 20 % nicht.",
        "Der Vorschuss von 15.000,00 EUR ist mangels vertraglicher Grundlage und mangels Gleichwertigkeit von Leistung und Gegenleistung nicht nach § 142 InsO privilegiert und unterliegt der Anfechtung nach §§ 130, 133 InsO, da der Beklagte als nahestehende Person im Sinne des § 138 Abs. 2 InsO Kenntnis von der Krise hatte oder haben musste.",
        "Die Zahlung des Beraterhonorars von 20.230,00 EUR betrifft demgegenueber eine tatsaechlich erbrachte, gleichwertige Gegenleistung und ist als Bargeschaeft nach § 142 InsO grundsaetzlich privilegiert; sie wird hilfsweise nach § 133 InsO angegriffen, soweit dem Beklagten eine Glaeubigerbenachteiligungsabsicht der Schuldnerin bekannt war.",
        "Es wird Klageerhebung beantragt.",
    ],
    unterschrift="Dr. Gesa Trux, Rechtsanwaeltin und Insolvenzverwalterin",
)

# 20 Klageerwiderung
make_docx(
    BASE / "20_klageerwiderung_okatan_2026-10-13.docx",
    KOPF_GEGNER,
    "Klageerwiderung",
    [
        "In dem Rechtsstreit Dr. Gesa Trux ./. Dr. Valentin Brosekamp",
        "94 O 47/26 - Landgericht Berlin",
        "",
        "beantrage ich fuer den Beklagten, die Klage abzuweisen.",
        "## Begruendung",
        "Zur Darlehensrueckzahlung wird nicht bestritten, dass diese innerhalb der Jahresfrist des § 135 Abs. 1 Nr. 2 InsO erfolgte. Der Beklagte macht jedoch geltend, die Klaegerin habe die Frist ab dem falschen Bezugspunkt berechnet; massgeblich sei nicht der Eroeffnungsantrag vom 14.11.2025, sondern die Eroeffnung des Verfahrens am 01.03.2026.",
        "Zum Vorschuss von 15.000,00 EUR wird vorgetragen, dieser sei eine ueblicherweise gewaehrte Abschlagszahlung auf zukuenftige, bereits absehbare Beratungsleistungen gewesen und daher letztlich ebenfalls als Bargeschaeft zu behandeln.",
        "Eine Kenntnis von einer Zahlungsunfaehigkeit oder Ueberschuldung der Schuldnerin wird bestritten. Der Beklagte verweist auf den bis kurz vor dem Eigenantrag verhandelten Investoren-LOI der Kollibri Ventures GmbH vom 30.09.2025, der aus seiner Sicht eine positive Fortfuehrungsprognose begruendet habe.",
        "Zur Beraterrechnung ueber 20.230,00 EUR wird auf die als Anlage vorgelegten Stundennachweise fuer Juli und August 2025 verwiesen, die eine tatsaechlich erbrachte, gleichwertige Leistung belegten; die Zahlung sei ein privilegiertes Bargeschaeft nach § 142 InsO.",
        "Aus diesen Gruenden wird beantragt, die Klage vollumfaenglich abzuweisen.",
    ],
    unterschrift="Dr. Selim Okatan, Rechtsanwalt",
)

# 21 Replik
make_docx(
    BASE / "21_replik_trux_2026-11-03.docx",
    KOPF_VERWALTERIN,
    "Replik",
    [
        "In dem Rechtsstreit Dr. Gesa Trux ./. Dr. Valentin Brosekamp",
        "94 O 47/26 - Landgericht Berlin",
        "",
        "erwidere ich auf die Klageerwiderung vom 13.10.2026 wie folgt:",
        "## Zum Fristbeginn nach § 135 Abs. 1 Nr. 2 InsO",
        "Massgeblicher Bezugspunkt fuer die Jahresfrist ist nach staendiger Rechtsprechung des Bundesgerichtshofs der Eroeffnungsantrag, hier der Eigenantrag vom 14.11.2025, nicht die spaetere Verfahrenseroeffnung am 01.03.2026. Die Darlehensrueckzahlung vom Dezember 2024 liegt damit innerhalb der Jahresfrist. Auf eine Kenntnis des Beklagten kommt es fuer diesen Tatbestand nicht an.",
        "## Zum Vorschuss",
        "Der Beratervertrag sieht keine Abschlagszahlungen vor. Der Vorschuss vom Oktober 2025 stand keiner gleichwertigen, bereits erbrachten Gegenleistung gegenueber und ist damit kein Bargeschaeft im Sinne des § 142 InsO. Als naheliegende Person im Sinne des § 138 Abs. 2 InsO trifft den Beklagten die Vermutung der Kenntnis von der Zahlungsunfaehigkeit; diese Vermutung hat er nicht widerlegt.",
        "## Zum Investoren-LOI",
        "Der LOI der Kollibri Ventures GmbH war zum Zeitpunkt seiner Unterzeichnung am 30.09.2025 rechtlich unverbindlich und stand bereits im Oktober 2025 erkennbar auf der Kippe; die als Anlage K9 vorgelegte Absage-E-Mail der Kollibri Ventures GmbH datiert vom 07.11.2025. Der Beklagte hatte als aktiver Berater der Schuldnerin und Empfaenger des Wochenreports vom 22.08.2025 Einblick in die tatsaechliche Liquiditaetslage, die im Gruender-Chat und in den Gesellschafterprotokollen ausfuehrlich dokumentiert ist.",
        "## Zum Beraterhonorar",
        "Die Stundennachweise fuer Juli und August 2025 werden nicht bestritten. Insoweit wird an der Klage nur hilfsweise, gestuetzt auf § 133 InsO, festgehalten.",
    ],
    unterschrift="Dr. Gesa Trux, Rechtsanwaeltin und Insolvenzverwalterin",
)

# 22 Duplik
make_docx(
    BASE / "22_duplik_okatan_2026-11-24.docx",
    KOPF_GEGNER,
    "Duplik",
    [
        "In dem Rechtsstreit Dr. Gesa Trux ./. Dr. Valentin Brosekamp",
        "94 O 47/26 - Landgericht Berlin",
        "",
        "nehme ich zur Replik vom 03.11.2026 wie folgt Stellung:",
        "Der Beklagte raeumt ein, dass nach der zitierten Rechtsprechung des Bundesgerichtshofs grundsaetzlich auf den Eroeffnungsantrag abzustellen ist, halt jedoch daran fest, dass er zum Zeitpunkt der Darlehensrueckzahlung im Dezember 2024 keinerlei Anhaltspunkte fuer eine bevorstehende Krise gehabt habe.",
        "Zum Wochenreport vom 22.08.2025 wird vorgetragen, dieser habe lediglich allgemeine Kennzahlen enthalten und keine konkrete Aussage zu Zahlungsunfaehigkeit oder Ueberschuldung getroffen. Der Beklagte habe sich bis zur Absage der Kollibri Ventures GmbH am 07.11.2025 auf eine positive Fortfuehrungsprognose verlassen duerfen.",
        "An der rechtlichen Einordnung des Vorschusses als letztlich unschaedliche Abschlagszahlung sowie an der Klageabweisung im Uebrigen wird festgehalten.",
    ],
    unterschrift="Dr. Selim Okatan, Rechtsanwalt",
)

# 23 Beweisbeschluss
make_docx(
    BASE / "23_beweisbeschluss_lg_berlin_2026-12-10.docx",
    KOPF_GERICHT,
    "Beweisbeschluss",
    [
        "94 O 47/26",
        "",
        "In dem Rechtsstreit Dr. Gesa Trux ./. Dr. Valentin Brosekamp",
        "",
        "beschliesst das Gericht:",
        "1. Es wird Beweis erhoben durch Vernehmung des Zeugen Jonas Wittkamp, Geschaeftsfuehrer der Schuldnerin, zu der Behauptung, dem Beklagten sei die Liquiditaetslage der Schuldnerin bereits im August 2025 durch den Wochenreport sowie durch Aeusserungen im Gruender-Chat bekannt gewesen.",
        "2. Es wird ferner Beweis erhoben durch Einholung eines ergaenzenden schriftlichen Sachverstaendigengutachtens zu der Behauptung, dass die im Gutachten des Eroeffnungsverfahrens festgestellten Stichtage der Ueberschuldung (30.06.2025) und der Zahlungsunfaehigkeit (01.09.2025) zutreffend ermittelt wurden.",
        "3. Zur Sachverstaendigen wird bestellt: Dipl.-Kffr. Nadja Ohlerich, Berlin.",
        "4. Termin zur Zeugenvernehmung wird bestimmt auf den 04.03.2027, 09:30 Uhr.",
    ],
)

# 24 Urteil
make_docx(
    BASE / "24_urteil_lg_berlin_2027-06-15.docx",
    KOPF_GERICHT,
    "Urteil",
    [
        "94 O 47/26",
        "",
        "IM NAMEN DES VOLKES",
        "",
        "In dem Rechtsstreit Dr. Gesa Trux als Insolvenzverwalterin ./. Dr. Valentin Brosekamp",
        "",
        "hat das Landgericht Berlin, Kammer fuer Handelssachen, fuer Recht erkannt:",
        "1. Der Beklagte wird verurteilt, an die Klaegerin 165.230,00 EUR nebst Zinsen in Hoehe von fuenf Prozentpunkten ueber dem Basiszinssatz seit dem 02.09.2026 zu zahlen.",
        "2. Im Uebrigen wird die Klage abgewiesen.",
        "3. Die Kosten des Rechtsstreits tragen die Klaegerin zu 11 % und der Beklagte zu 89 %.",
        "4. Das Urteil ist vorlaeufig vollstreckbar.",
        "## Tatbestand",
        "Die Klaegerin macht als Insolvenzverwalterin Rueckgewaehranspruche wegen dreier Zahlungen an den Beklagten geltend: Darlehensrueckzahlung 150.000,00 EUR, Vorschuss 15.000,00 EUR und Beraterhonorar 20.230,00 EUR.",
        "## Entscheidungsgruende",
        "Die Klage ist ueberwiegend begruendet. Die Darlehensrueckzahlung von 150.000,00 EUR unterliegt der Anfechtung nach § 135 Abs. 1 Nr. 2 InsO. Massgeblicher Bezugspunkt der Jahresfrist ist der Eroeffnungsantrag vom 14.11.2025; die Rueckzahlung im Dezember 2024 liegt innerhalb dieser Frist. Auf eine Kenntnis des Beklagten kommt es fuer diesen Tatbestand nicht an; das Kleinbeteiligtenprivileg des § 39 Abs. 5 InsO greift bei einer Beteiligung von 20 % nicht.",
        "Der Vorschuss von 15.000,00 EUR ist ebenfalls anfechtbar. Die Vernehmung des Zeugen Wittkamp hat zur Ueberzeugung der Kammer ergeben, dass der Beklagte durch den Wochenreport vom 22.08.2025 sowie durch die im Gruender-Chat dokumentierten Aeusserungen jedenfalls im Oktober 2025 Kenntnis von der drohenden Zahlungsunfaehigkeit hatte. Als dem Geschaeftsleiter nahestehende Person im Sinne des § 138 Abs. 2 InsO streitet fuer diese Kenntnis zudem die gesetzliche Vermutung, die der Beklagte nicht widerlegt hat. Der Vorschuss steht keiner gleichwertigen Gegenleistung gegenueber und ist mangels vertraglicher Grundlage nicht nach § 142 InsO privilegiert.",
        "Die Zahlung des Beraterhonorars von 20.230,00 EUR ist demgegenueber nicht zu erstatten. Die eingereichten Stundennachweise belegen eine tatsaechlich erbrachte und gleichwertige Beratungsleistung fuer Juli und August 2025; die Zahlung ist als Bargeschaeft nach § 142 InsO privilegiert. Eine Kenntnis von einer Glaeubigerbenachteiligungsabsicht im Sinne des § 133 InsO konnte nicht zur Ueberzeugung der Kammer festgestellt werden; der bis zum 07.11.2025 verhandelte Investoren-LOI der Kollibri Ventures GmbH begruendete jedenfalls bis zu diesem Zeitpunkt eine nicht von vornherein unplausible Sanierungshoffnung.",
        "Das ergaenzende Sachverstaendigengutachten der Sachverstaendigen Ohlerich hat die im Eroeffnungsverfahren festgestellten Stichtage der Ueberschuldung (30.06.2025) und der Zahlungsunfaehigkeit (01.09.2025) bestaetigt.",
        "Der Rueckgewaehranspruch fuer die anfechtbaren Zahlungen folgt aus § 143 Abs. 1 InsO nebst Zinsen seit Rechtshaengigkeit.",
        "Die Kostenentscheidung beruht auf § 92 Abs. 1 ZPO, die Entscheidung zur vorlaeufigen Vollstreckbarkeit auf § 709 ZPO.",
    ],
)

# 25 Schlussvermerk
make_docx(
    BASE / "25_schlussvermerk_trux_2027-08-30.docx",
    KOPF_VERWALTERIN,
    "Schlussvermerk zum Anfechtungsprozess Dr. Valentin Brosekamp",
    [
        "Az. 94 O 47/26 (LG Berlin); 36c IN 2291/25 (AG Charlottenburg)",
        "## Verfahrensstand",
        "Das Urteil vom 15.06.2027 ist seit dem 20.07.2027 rechtskraeftig, nachdem beide Parteien auf Rechtsmittel verzichtet haben. Der Beklagte hat den titulierten Betrag von 165.230,00 EUR nebst Zinsen in Hoehe von 12.940,15 EUR, insgesamt 178.170,15 EUR, am 30.08.2027 vollstaendig auf das Massekonto ueberwiesen.",
        "## Zusammenfassung",
        "Die Anfechtung der Darlehensrueckzahlung nach § 135 Abs. 1 Nr. 2 InsO wurde in voller Hoehe bestaetigt; auf eine Kenntnis kam es hierfuer nicht an. Der Vorschuss wurde ebenfalls zur Rueckgewaehr verurteilt, gestuetzt auf die Vermutung des § 138 Abs. 2 InsO und die Zeugenaussage Wittkamp. Das Beraterhonorar fuer tatsaechlich erbrachte Leistungen blieb dagegen als privilegiertes Bargeschaeft nach § 142 InsO unangetastet.",
        "Die vereinnahmten 178.170,15 EUR werden der Masse zugefuehrt. Der Vorgang gilt als abgeschlossen.",
    ],
    unterschrift="Dr. Gesa Trux, Rechtsanwaeltin und Insolvenzverwalterin",
)

print("Kiezflitzer 19-25 erzeugt")
