#!/usr/bin/env python3
"""Erzeugt Aktenstuecke 17-25 fuer insolvenzanfechtung-kontokorrent-rueckfuehrung-kreditlinie-mainz."""
import sys
sys.path.insert(0, "/home/user/workspace/legal-work/target/scripts/_tmp_gen")
from aktenbau import make_docx, TESTAKTEN

D = TESTAKTEN / "insolvenzanfechtung-kontokorrent-rueckfuehrung-kreditlinie-mainz"
KOPF = "Rechtsanwaeltin Dr. Ilka Bernstorf | Insolvenzverwalterin | Mainz"
KOPF_GEGEN = "Dr. Cammann & Weyrich Rechtsanwaelte | Wiesbaden"

# 17 - Klageschrift
make_docx(
    D / "17_klageschrift_lg_mainz_2026-08-04.docx",
    KOPF,
    "Klageschrift — LG Mainz",
    [
        "Landgericht Mainz",
        "Klaegerin: Dr. Ilka Bernstorf als Insolvenzverwalterin ueber das Vermoegen der "
        "Domblick Weinkellerei-Betriebs-GmbH",
        "Beklagte: Sparkasse Weinbergland Mainz, Anstalt des oeffentlichen Rechts",
        "## Antrag",
        "Die Beklagte wird verurteilt, an die Klaegerin 360.000,00 EUR nebst Zinsen in Hoehe von "
        "5 Prozentpunkten ueber dem Basiszinssatz seit dem 01.05.2026 zu zahlen.",
        "## Sachverhalt",
        "Nach fruchtlosem Ablauf der mit Schreiben vom 26.06.2026 gesetzten Frist zum 17.07.2026 "
        "wird die mit Anfechtungsschreiben vom 12.05.2026 geltend gemachte Rueckgewaehr nach "
        "Paragrafen 130, 131, 143 InsO nunmehr klageweise verfolgt. Die Beklagte hat im "
        "Dreimonatszeitraum vor dem Eigenantrag die Kontokorrentlinie in drei Schritten von "
        "480.000,00 EUR auf 120.000,00 EUR herabgesetzt und Zahlungseingaenge in Hoehe von "
        "476.100,00 EUR zur Saldenreduzierung vereinnahmt, waehrend nur 116.100,00 EUR an "
        "Verfuegungen zugelassen wurden. Der Verrechnungssaldo von 360.000,00 EUR ist zurueckzugewaehren.",
        "## Rechtliche Wuerdigung",
        "Die Rueckfuehrung stellt eine inkongruente Deckung gemaess Paragraf 131 Abs. 1 InsO dar, "
        "da die endgueltige Vereinnahmung erst auf den im Dreimonatszeitraum abgeschlossenen "
        "Anpassungsvereinbarungen beruht. Die Beklagte hatte aufgrund der eigenen Kontodaten "
        "(17 Ruecklastschriften seit April 2025, zwei Scheckrueckgaben, zwei Kontopfaendungen, "
        "ausgereizte Linie, Intensivbetreuungsvermerk vom 24.11.2025) Kenntnis von der "
        "Zahlungsunfaehigkeit im Sinne des Paragraf 130 Abs. 2 InsO.",
    ],
    "Dr. Ilka Bernstorf, Rechtsanwaeltin",
)

# 18 - Klageerwiderung
make_docx(
    D / "18_klageerwiderung_sparkasse_2026-09-15.docx",
    KOPF_GEGEN,
    "Klageerwiderung",
    [
        "Landgericht Mainz, Az. 8 O 214/26",
        "in Sachen Dr. Bernstorf ./. Sparkasse Weinbergland Mainz",
        "## Antrag",
        "Die Klage wird abgewiesen.",
        "## Begruendung",
        "Die Anpassungsvereinbarungen beruhen auf einvernehmlicher Vertragsaenderung im Rahmen "
        "der laufenden Geschaeftsbeziehung; die AGB-Verrechnungsbefugnis nach Paragraf 355 HGB "
        "begruendet Kongruenz. Die Linienherabsetzung sei durch saisonale Umsatzschwankungen "
        "im Weinhandel veranlasst gewesen, wie sie in den Vorjahren regelmaessig aufgetreten sei. "
        "Eine Kenntnis von der Zahlungsunfaehigkeit wird bestritten; die Ruecklastschriften seien "
        "vereinzelte technische Vorgaenge gewesen. Hilfsweise wird der Bargeschaeftseinwand nach "
        "Paragraf 142 InsO erhoben, da die Beklagte die Betriebsfortfuehrung durch Belassung der "
        "Restlinie von 120.000,00 EUR ermoeglicht habe.",
    ],
    "Dr. Bettina Cammann, Rechtsanwaeltin",
)

# 19 - Replik
make_docx(
    D / "19_replik_verwalterin_2026-10-06.docx",
    KOPF,
    "Replik zur Klageerwiderung",
    [
        "Landgericht Mainz, Az. 8 O 214/26",
        "## Erwiderung auf die Klageerwiderung",
        "Der Saisonalitaetseinwand ist unbegruendet: Ein Vorjahresvergleich der Bankspiegel zeigt, "
        "dass die Linienausnutzung im relevanten Zeitraum erstmals dauerhaft ueber 95 Prozent lag, "
        "waehrend in den Vorjahren saisonale Spitzen jeweils binnen vier bis sechs Wochen "
        "zurueckgefuehrt wurden. Die Verrechnung von Altkredit gegen neue Zahlungseingaenge stellt "
        "keinen Leistungsaustausch dar, da die Beklagte keine neue gleichwertige Gegenleistung "
        "in das Schuldnervermoegen erbracht hat; der Bargeschaeftseinwand nach Paragraf 142 InsO "
        "greift daher nicht.",
    ],
    "Dr. Ilka Bernstorf, Rechtsanwaeltin",
)

# 20 - Duplik
make_docx(
    D / "20_duplik_sparkasse_2026-10-27.docx",
    KOPF_GEGEN,
    "Duplik",
    [
        "Landgericht Mainz, Az. 8 O 214/26",
        "## Erwiderung auf die Replik",
        "Die Beklagte haelt an ihrer Rechtsauffassung fest und verweist ergaenzend darauf, dass "
        "die Restlinie von 120.000,00 EUR revolvierend genutzt wurde und damit ein Sanierungsbeitrag "
        "vorliege. Vorsorglich wird beantragt, ueber die Kenntnis der Beklagten von der "
        "Zahlungsunfaehigkeit Beweis durch Vernehmung der Zeugin Sandra Vietinghoff zu erheben.",
    ],
    "Dr. Bettina Cammann, Rechtsanwaeltin",
)

# 21 - Beweisbeschluss
make_docx(
    D / "21_beweisbeschluss_lg_mainz_2026-11-10.docx",
    "Landgericht Mainz",
    "Beweisbeschluss",
    [
        "Az. 8 O 214/26",
        "## Beschluss",
        "Es wird Beweis erhoben ueber die Frage, ob und wann die Sparkasse Weinbergland Mainz "
        "Kenntnis von der Zahlungsunfaehigkeit der Domblick Weinkellerei-Betriebs-GmbH erlangt hat, "
        "durch Vernehmung der Zeugin Sandra Vietinghoff sowie durch Einholung eines "
        "Sachverstaendigengutachtens zur Frage des Eintritts der Zahlungsunfaehigkeit.",
        "Zum Sachverstaendigen wird bestellt: Diplom-Kaufmann Reinhold Wachtel, Mainz.",
    ],
    "Die Vorsitzende Richterin am Landgericht",
)

# 22 - Sachverstaendigengutachten
make_docx(
    D / "22_sachverstaendigengutachten_wachtel_2027-01-20.docx",
    "Diplom-Kaufmann Reinhold Wachtel | Oeffentlich bestellter und vereidigter Sachverstaendiger",
    "Sachverstaendigengutachten zur Zahlungsunfaehigkeit",
    [
        "Landgericht Mainz, Az. 8 O 214/26",
        "Gutachten vom 20.01.2027",
        "## Auftrag",
        "Feststellung des Zeitpunkts des Eintritts der Zahlungsunfaehigkeit der Domblick "
        "Weinkellerei-Betriebs-GmbH.",
        "## Feststellungen",
        "Die Auswertung der BWA-Reihe 2025, des Bankspiegels und der Ruecklastschriftenliste ergibt "
        "eine Liquiditaetsluecke, die bereits im April 2025 bei 14,7 Prozent lag und bis Dezember 2025 "
        "auf 46,5 Prozent anstieg. Damit lag die Liquiditaetsluecke durchgehend ueber der "
        "10-Prozent-Schwelle der ueblichen Zahlungsstockung. Zahlungsunfaehigkeit im Sinne des "
        "Paragraf 17 InsO ist demnach bereits im April 2025 eingetreten, nicht erst Mitte Januar 2026 "
        "wie im Eigenantrag angegeben.",
        "## Ergebnis",
        "Der Eigenantrag datiert die Zahlungsunfaehigkeit rund elf Monate zu spaet.",
    ],
    "Diplom-Kaufmann Reinhold Wachtel",
)

# 23 - Zeugenvernehmungsprotokoll
make_docx(
    D / "23_zeugenvernehmungsprotokoll_vietinghoff_2027-02-09.docx",
    "Landgericht Mainz",
    "Protokoll der Zeugenvernehmung — Sandra Vietinghoff",
    [
        "Az. 8 O 214/26, Termin vom 09.02.2027",
        "## Aussage der Zeugin",
        "Die Zeugin Sandra Vietinghoff, Marktfolge Kredit der Sparkasse Weinbergland Mainz, sagt aus, "
        "dass sie das Engagement der Domblick Weinkellerei-Betriebs-GmbH seit November 2025 in der "
        "Intensivbetreuung fuehrte. Sie bestaetigt, den Vermerk vom 24.11.2025 mit der darin "
        "beschriebenen 'Exit-Strategie' verfasst zu haben. Auf Nachfrage der Klaegervertreterin "
        "raeumt sie ein, dass ihr die wiederholten Ruecklastschriften seit April 2025 sowie die "
        "beiden Kontopfaendungen bekannt gewesen seien und sie diese als deutliches Warnsignal "
        "gewertet habe.",
    ],
    "Die Protokollfuehrerin",
)

# 24 - Urteil
make_docx(
    D / "24_urteil_lg_mainz_2027-05-18.docx",
    "Landgericht Mainz",
    "Urteil",
    [
        "Az. 8 O 214/26",
        "verkuendet am 18.05.2027",
        "## Tenor",
        "1. Die Beklagte wird verurteilt, an die Klaegerin 360.000,00 EUR nebst Zinsen in Hoehe von "
        "5 Prozentpunkten ueber dem Basiszinssatz seit dem 01.05.2026 zu zahlen.",
        "2. Die Beklagte traegt die Kosten des Rechtsstreits.",
        "3. Das Urteil ist vorlaeufig vollstreckbar gegen Sicherheitsleistung in Hoehe von "
        "120 Prozent des jeweils zu vollstreckenden Betrags.",
        "## Entscheidungsgruende",
        "Die Kammer ist nach dem Ergebnis der Beweisaufnahme davon ueberzeugt, dass die Beklagte "
        "aufgrund der eigenen Kontodaten und der Aussage der Zeugin Vietinghoff Kenntnis von der "
        "Zahlungsunfaehigkeit der Schuldnerin hatte. Das Sachverstaendigengutachten bestaetigt den "
        "Eintritt der Zahlungsunfaehigkeit bereits im April 2025. Die dreistufige Linienherabsetzung "
        "mit anschliessender Vereinnahmung der Zahlungseingaenge stellt eine inkongruente Deckung "
        "gemaess Paragraf 131 Abs. 1 InsO dar. Der Bargeschaeftseinwand greift nicht, da die Beklagte "
        "keine neue gleichwertige Gegenleistung erbracht hat.",
    ],
    "Die Vorsitzende Richterin am Landgericht",
)

# 25 - Schlussvermerk
make_docx(
    D / "25_schlussvermerk_verwalterin_2027-07-02.docx",
    KOPF,
    "Schlussvermerk zur Handakte",
    [
        "Insolvenzverfahren Domblick Weinkellerei-Betriebs-GmbH, Az. 273 IN 45/26",
        "Vermerk vom 02.07.2027",
        "## Zusammenfassung",
        "Das Urteil des Landgerichts Mainz vom 18.05.2027 (Az. 8 O 214/26) ist seit dem 20.06.2027 "
        "rechtskraeftig, nachdem die Beklagte auf Rechtsmittel verzichtet hat. Die titulierte Summe "
        "von 360.000,00 EUR nebst Zinsen wurde am 28.06.2027 vollstaendig zur Masse gezahlt. Der "
        "Anfechtungskomplex Sparkasse Weinbergland Mainz ist damit abgeschlossen.",
        "## Bewertung",
        "Der Fall zeigt exemplarisch, wie eine formal einvernehmliche Linienherabsetzung materiell "
        "eine inkongruente Deckung darstellen kann, wenn die Bank auf eigene Kontodaten gestuetzte "
        "Kenntnis von der Zahlungsunfaehigkeit hatte.",
    ],
    "Dr. Ilka Bernstorf, Insolvenzverwalterin",
)

print("Mainz 17-25 erzeugt.")
