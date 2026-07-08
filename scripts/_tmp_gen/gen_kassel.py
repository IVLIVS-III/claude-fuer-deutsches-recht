#!/usr/bin/env python3
"""Erzeugt Aktenstuecke 18-25 fuer insolvenzanfechtung-inkongruente-deckung-warenlager-an-erfuellungs-statt-kassel."""
import sys
sys.path.insert(0, "/home/user/workspace/legal-work/target/scripts/_tmp_gen")
from aktenbau import make_docx, TESTAKTEN

D = TESTAKTEN / "insolvenzanfechtung-inkongruente-deckung-warenlager-an-erfuellungs-statt-kassel"
KOPF = "Rechtsanwaeltin Dr. Friederike Salzwedel | Insolvenzverwalterin | Kassel"
KOPF_GEGEN = "Rechtsanwalt Dr. Jochen Appelt | Goettingen"

# 18 - Klageschrift
make_docx(
    D / "18_klageschrift_lg_kassel_2026-09-07.docx",
    KOPF,
    "Klageschrift — LG Kassel",
    [
        "Landgericht Kassel",
        "Klaegerin: Dr. Friederike Salzwedel als Insolvenzverwalterin ueber das Vermoegen der "
        "Fuldablick Baustoffhandel GmbH",
        "Beklagte: Daemmtec Werra GmbH, Eschwege",
        "## Antrag",
        "Die Beklagte wird verurteilt, an die Klaegerin 142.370,00 EUR nebst Zinsen seit dem "
        "01.05.2026 zu zahlen sowie Auskunft ueber den Verbleib der uebernommenen 663 Paletten "
        "Daemmplatten zu erteilen.",
        "## Sachverhalt",
        "Die Beklagte erhielt am 18.12.2025 zur Tilgung offener Rechnungen von 118.000,00 EUR das "
        "gesamte Restlager Daemmplatten (663 Paletten, Buchwert 96.000,00 EUR) an Erfuellungs statt "
        "sowie zwei Kundenforderungen ueber zusammen 24.370,00 EUR abgetreten. Der Vorgang faellt in "
        "den zweiten Monat vor dem Eigenantrag vom 09.02.2026 (Zeitraum 09.12.2025 bis 08.01.2026).",
        "## Rechtliche Wuerdigung",
        "Die Leistung an Erfuellungs statt ist eine inkongruente Deckung im Sinne des Paragraf 131 "
        "Abs. 1 InsO. Die objektive Zahlungsunfaehigkeit am Stichtag 18.12.2025 ergibt sich aus dem "
        "Liquiditaetsstatus (Unterdeckung 92,6 Prozent zum 15.12.2025); auf Kenntnis kommt es nach "
        "Nr. 2 nicht an. Hilfsweise wird auf Nr. 3 und die Kenntnis der Beklagten von der "
        "Glaeubigerbenachteiligung abgestellt.",
    ],
    "Dr. Friederike Salzwedel, Rechtsanwaeltin",
)

# 19 - Klageerwiderung
make_docx(
    D / "19_klageerwiderung_appelt_2026-10-19.docx",
    KOPF_GEGEN,
    "Klageerwiderung",
    [
        "Landgericht Kassel, Az. 4 O 318/26",
        "in Sachen Dr. Salzwedel ./. Daemmtec Werra GmbH",
        "## Antrag",
        "Die Klage wird abgewiesen.",
        "## Begruendung",
        "Die Uebernahme des Warenlagers sei ueblicher Ausdruck einer Warenruecknahme im "
        "Baustoffhandel und keine inkongruente Deckung. Die objektive Zahlungsunfaehigkeit am "
        "18.12.2025 werde bestritten; die Schuldnerin habe sich noch in einer beherrschbaren "
        "Uebergangsphase befunden. Eine Kenntnis der Beklagten von einer Glaeubigerbenachteiligung "
        "habe nicht bestanden; die interne E-Mail vom 09.12.2025 sei ueberzogen formuliert gewesen "
        "und spiegele nicht die tatsaechliche Einschaetzung wider. Hilfsweise wird der "
        "Bargeschaefts-Einwand nach Paragraf 142 InsO erhoben, da eine Wiederbelieferungszusage "
        "erteilt worden sei.",
    ],
    "Dr. Jochen Appelt, Rechtsanwalt",
)

# 20 - Replik
make_docx(
    D / "20_replik_verwalterin_2026-11-09.docx",
    KOPF,
    "Replik zur Klageerwiderung",
    [
        "Landgericht Kassel, Az. 4 O 318/26",
        "## Erwiderung",
        "Die ausdrueckliche Ersetzungsabrede in der Uebereignungs- und Tilgungsvereinbarung vom "
        "18.12.2025 spricht gegen eine blosse Warenruecknahme und fuer eine Leistung an "
        "Erfuellungs statt. Der Bargeschaefts-Einwand greift nicht, da die Wiederbelieferungszusage "
        "nur gegen Vorkasse erfolgte und die getilgten Rechnungen aus August bis November 2025 "
        "stammen, mithin keine unmittelbare Gegenleistung vorliegt.",
    ],
    "Dr. Friederike Salzwedel, Rechtsanwaeltin",
)

# 21 - Duplik
make_docx(
    D / "21_duplik_appelt_2026-11-30.docx",
    KOPF_GEGEN,
    "Duplik",
    [
        "Landgericht Kassel, Az. 4 O 318/26",
        "## Erwiderung auf die Replik",
        "Die Beklagte haelt an ihrer Rechtsauffassung fest und beantragt vorsorglich, ueber die "
        "Umstaende der Vertragsverhandlungen und die tatsaechliche wirtschaftliche Lage der "
        "Schuldnerin am 18.12.2025 Beweis durch Sachverstaendigengutachten und Zeugenvernehmung zu erheben.",
    ],
    "Dr. Jochen Appelt, Rechtsanwalt",
)

# 22 - Beweisbeschluss
make_docx(
    D / "22_beweisbeschluss_lg_kassel_2026-12-14.docx",
    "Landgericht Kassel",
    "Beweisbeschluss",
    [
        "Az. 4 O 318/26",
        "## Beschluss",
        "Es wird Beweis erhoben ueber die Frage der Zahlungsunfaehigkeit der Fuldablick "
        "Baustoffhandel GmbH am 18.12.2025 durch Einholung eines Sachverstaendigengutachtens sowie "
        "ueber die Kenntnis der Beklagten von der Glaeubigerbenachteiligung durch Vernehmung des "
        "Zeugen Sascha Kurrle.",
        "Zum Sachverstaendigen wird bestellt: Diplom-Kaufmann Bernd Osterhage, Kassel.",
    ],
    "Der Vorsitzende Richter am Landgericht",
)

# 23 - Sachverstaendigengutachten
make_docx(
    D / "23_sachverstaendigengutachten_osterhage_2027-03-08.docx",
    "Diplom-Kaufmann Bernd Osterhage | Oeffentlich bestellter und vereidigter Sachverstaendiger",
    "Sachverstaendigengutachten zur Zahlungsunfaehigkeit",
    [
        "Landgericht Kassel, Az. 4 O 318/26",
        "Gutachten vom 08.03.2027",
        "## Feststellungen",
        "Der Liquiditaetsstatus zeigt zum 15.12.2025 eine Unterdeckung von 92,6 Prozent der "
        "faelligen Verbindlichkeiten. Bereits seit dem 01.02.2025 besteht eine durchgehende Luecke "
        "von deutlich ueber 10 Prozent ueber mehr als drei Wochen. Die Voraussetzungen der "
        "Zahlungsunfaehigkeit im Sinne des Paragraf 17 InsO waren am 18.12.2025 objektiv erfuellt. "
        "Die im Sanierungskurzgutachten vom 10.12.2024 als Bedingung genannte Gesellschafterzuschuss-"
        "Zahlung von 350.000,00 EUR ist zu keinem Zeitpunkt erfolgt.",
    ],
    "Diplom-Kaufmann Bernd Osterhage",
)

# 24 - Urteil
make_docx(
    D / "24_urteil_lg_kassel_2027-06-21.docx",
    "Landgericht Kassel",
    "Urteil",
    [
        "Az. 4 O 318/26",
        "verkuendet am 21.06.2027",
        "## Tenor",
        "1. Die Beklagte wird verurteilt, an die Klaegerin 142.370,00 EUR nebst Zinsen in Hoehe von "
        "5 Prozentpunkten ueber dem Basiszinssatz seit dem 01.05.2026 zu zahlen.",
        "2. Die Beklagte traegt die Kosten des Rechtsstreits.",
        "## Entscheidungsgruende",
        "Die Uebereignung des Warenlagers an Erfuellungs statt sowie die Forderungsabtretungen "
        "stellen eine inkongruente Deckung gemaess Paragraf 131 Abs. 1 InsO dar. Nach dem Ergebnis "
        "der Beweisaufnahme steht die objektive Zahlungsunfaehigkeit der Schuldnerin am 18.12.2025 "
        "fest, sodass es auf eine Kenntnis der Beklagten nach Nr. 2 nicht ankommt. Der "
        "Bargeschaefts-Einwand nach Paragraf 142 InsO greift nicht, da die Tilgung Altverbindlichkeiten "
        "aus August bis November 2025 betraf und die Wiederbelieferungszusage nur gegen Vorkasse "
        "erfolgte.",
    ],
    "Der Vorsitzende Richter am Landgericht",
)

# 25 - Schlussvermerk
make_docx(
    D / "25_schlussvermerk_verwalterin_2027-08-16.docx",
    KOPF,
    "Schlussvermerk zur Handakte",
    [
        "Insolvenzverfahren Fuldablick Baustoffhandel GmbH, Az. 660 IN 71/26",
        "Vermerk vom 16.08.2027",
        "## Zusammenfassung",
        "Das Urteil des Landgerichts Kassel vom 21.06.2027 (Az. 4 O 318/26) ist seit dem 26.07.2027 "
        "rechtskraeftig. Die Beklagte hat die titulierte Summe von 142.370,00 EUR nebst Zinsen am "
        "10.08.2027 vollstaendig zur Masse gezahlt. Nach Paragraf 144 Abs. 1 InsO lebt die "
        "urspruengliche Lieferantenforderung der Beklagten in Hoehe von 118.000,00 EUR wieder auf "
        "und wurde zur Insolvenztabelle angemeldet.",
        "## Bewertung",
        "Der Fall bestaetigt, dass eine Leistung an Erfuellungs statt eine inkongruente Deckung "
        "darstellt und dass die objektive Zahlungsunfaehigkeit nach Paragraf 131 Abs. 1 Nr. 2 InsO "
        "unabhaengig von einer Kenntnis des Anfechtungsgegners zur Anfechtbarkeit fuehrt.",
    ],
    "Dr. Friederike Salzwedel, Insolvenzverwalterin",
)

print("Kassel 18-25 erzeugt.")
