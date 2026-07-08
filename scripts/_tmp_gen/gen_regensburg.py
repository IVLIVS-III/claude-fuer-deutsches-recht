#!/usr/bin/env python3
"""Erzeugt Aktenstuecke 17-25 fuer insolvenzanfechtung-gesellschafterdarlehen-cash-pool-regensburg."""
import sys
sys.path.insert(0, "/home/user/workspace/legal-work/target/scripts/_tmp_gen")
from aktenbau import make_docx, TESTAKTEN

D = TESTAKTEN / "insolvenzanfechtung-gesellschafterdarlehen-cash-pool-regensburg"
KOPF = "Rechtsanwalt Dr. Ludwig Stadlbauer | Insolvenzverwalter | Regensburg"
KOPF_GEGEN = "Dr. Peter Immel | Rechtsanwalt | Muenchen"

# 17 - Klageschrift
make_docx(
    D / "17_klageschrift_lg_regensburg_2026-09-02.docx",
    KOPF,
    "Klageschrift — LG Regensburg",
    [
        "Landgericht Regensburg",
        "Klaeger: Dr. Ludwig Stadlbauer als Insolvenzverwalter ueber das Vermoegen der "
        "Donaupart Praezisionstechnik GmbH",
        "Beklagte: AVR Automotive Beteiligungs GmbH, Regensburg",
        "## Antrag",
        "Die Beklagte wird verurteilt, an den Klaeger 640.000,00 EUR nebst Zinsen seit dem "
        "12.05.2026 zu zahlen sowie den ihr sicherungsuebereigneten Maschinenpark laut Anlagenverzeichnis "
        "vom 16.06.2025 an den Klaeger herauszugeben, hilfsweise 1.180.000,00 EUR nebst Zinsen zu zahlen.",
        "## Sachverhalt",
        "Die Beklagte haelt 92 Prozent der Geschaeftsanteile an der Schuldnerin und fungierte als "
        "Poolfuehrerin eines Zero-Balancing-Cash-Pools. Im Jahr vor dem Eigenantrag vom 16.02.2026 "
        "wurde der Sollsaldo der Schuldnerin von 1.480.000,00 EUR auf 840.000,00 EUR zurueckgefuehrt "
        "(saldiert 640.000,00 EUR). Acht Monate vor Antragstellung wurde zudem ein seit 2019 "
        "unbesichertes Gesellschafterdarlehen ueber 750.000,00 EUR durch Sicherungsuebereignung des "
        "gesamten Maschinenparks (Buchwert 1.180.000,00 EUR) nachtraeglich gesichert.",
        "## Rechtliche Wuerdigung",
        "Die Rueckfuehrung ist nach Paragraf 135 Abs. 1 Nr. 2 InsO anfechtbar, da sie innerhalb des "
        "letzten Jahres vor dem Insolvenzantrag erfolgte; auf Kenntnis kommt es nicht an. Die "
        "Sicherungsuebereignung ist nach Paragraf 135 Abs. 1 Nr. 1 InsO anfechtbar, da sie innerhalb "
        "der Zehnjahresfrist fuer ein Gesellschafterdarlehen bestellt wurde, das im Zeitpunkt der "
        "Darlehensgewaehrung 2019 unbesichert war.",
    ],
    "Dr. Ludwig Stadlbauer, Rechtsanwalt",
)

# 18 - Klageerwiderung
make_docx(
    D / "18_klageerwiderung_avr_2026-10-14.docx",
    KOPF_GEGEN,
    "Klageerwiderung",
    [
        "Landgericht Regensburg, Az. 2 O 987/26",
        "in Sachen Dr. Stadlbauer ./. AVR Automotive Beteiligungs GmbH",
        "## Antrag",
        "Die Klage wird abgewiesen.",
        "## Begruendung",
        "Die Cash-Pool-Salden seien keine Gesellschafterdarlehen, sondern Ausfluss einer reinen "
        "Verrechnungsbeziehung im Konzern-Liquiditaetsmanagement. Selbst bei Anwendung des Paragraf 135 "
        "InsO sei allenfalls die Nettobetrachtung massgeblich, da die Beklagte im selben Zeitraum "
        "2.900.000,00 EUR neu zugefuehrt habe. Die Sicherungsuebereignung sei lediglich Vollzug der "
        "bereits 2019 vereinbarten Nachbesicherungsklausel und daher kein neuer Sicherungsvorgang "
        "im Sinne des Paragraf 135 Abs. 1 Nr. 1 InsO.",
    ],
    "Dr. Peter Immel, Rechtsanwalt",
)

# 19 - Replik
make_docx(
    D / "19_replik_verwalter_2026-11-05.docx",
    KOPF,
    "Replik zur Klageerwiderung",
    [
        "Landgericht Regensburg, Az. 2 O 987/26",
        "## Erwiderung",
        "Die Nachbesicherungsklausel aus 2019 begruendete allenfalls einen schuldrechtlichen Anspruch "
        "auf Sicherheit, keine dingliche Sicherung; die tatsaechliche Bestellung der Sicherheit am "
        "18.06.2025 ist der massgebliche Anfechtungszeitpunkt. Die Nettobetrachtung wird bestritten: "
        "Nach herrschender Rechtsprechung ist bei revolvierenden Kontokorrentverhaeltnissen im Rahmen "
        "des Paragraf 135 Abs. 1 Nr. 2 InsO auf den tatsaechlichen Saldenabbau im Jahreszeitraum "
        "abzustellen, hilfsweise wird der Anspruch auf den Saldenabbau von 640.000,00 EUR gestuetzt.",
    ],
    "Dr. Ludwig Stadlbauer, Rechtsanwalt",
)

# 20 - Duplik
make_docx(
    D / "20_duplik_avr_2026-11-26.docx",
    KOPF_GEGEN,
    "Duplik",
    [
        "Landgericht Regensburg, Az. 2 O 987/26",
        "## Erwiderung auf die Replik",
        "Die Beklagte haelt an ihrer Rechtsauffassung fest und beantragt vorsorglich, ueber die "
        "Umstaende der Sicherheitenbestellung sowie ueber die betriebswirtschaftliche Notwendigkeit "
        "der Nachbesicherung Beweis durch Einholung eines Sachverstaendigengutachtens zu erheben.",
    ],
    "Dr. Peter Immel, Rechtsanwalt",
)

# 21 - Beweisbeschluss
make_docx(
    D / "21_beweisbeschluss_lg_regensburg_2026-12-15.docx",
    "Landgericht Regensburg",
    "Beweisbeschluss",
    [
        "Az. 2 O 987/26",
        "## Beschluss",
        "Es wird Beweis erhoben ueber die Frage des Zeitpunkts des Eintritts der wirtschaftlichen Krise "
        "der Donaupart Praezisionstechnik GmbH sowie ueber die Bewertung des sicherungsuebereigneten "
        "Maschinenparks durch Einholung eines Sachverstaendigengutachtens.",
        "Zum Sachverstaendigen wird bestellt: Diplom-Kaufmann Anton Ruckdeschel, Regensburg.",
    ],
    "Der Vorsitzende Richter am Landgericht",
)

# 22 - Sachverstaendigengutachten
make_docx(
    D / "22_sachverstaendigengutachten_ruckdeschel_2027-03-10.docx",
    "Diplom-Kaufmann Anton Ruckdeschel | Oeffentlich bestellter und vereidigter Sachverstaendiger",
    "Sachverstaendigengutachten",
    [
        "Landgericht Regensburg, Az. 2 O 987/26",
        "Gutachten vom 10.03.2027",
        "## Feststellungen zur Krise",
        "Das Konzern-Reporting und das Treasury-Memo vom 31.03.2025 belegen ein negatives Eigenkapital "
        "der Donaupart Praezisionstechnik GmbH bereits ab Maerz 2025 sowie eine Deckungsluecke von "
        "durchgehend ueber 15 Prozent der faelligen externen Verbindlichkeiten. Die im Eigenantrag "
        "angegebene Zahlungsunfaehigkeit erst ab Mitte Dezember 2025 ist mit den Konzernunterlagen "
        "nicht vereinbar; die Krise trat bereits im ersten Quartal 2025 ein.",
        "## Bewertung des Maschinenparks",
        "Der Buchwert des sicherungsuebereigneten Maschinenparks von 1.180.000,00 EUR entspricht "
        "im Wesentlichen dem Verkehrswert; eine Übersicherung im Verhaeltnis zur gesicherten "
        "Forderung von 750.000,00 EUR liegt vor.",
    ],
    "Diplom-Kaufmann Anton Ruckdeschel",
)

# 23 - Urteil
make_docx(
    D / "23_urteil_lg_regensburg_2027-06-22.docx",
    "Landgericht Regensburg",
    "Urteil",
    [
        "Az. 2 O 987/26",
        "verkuendet am 22.06.2027",
        "## Tenor",
        "1. Die Beklagte wird verurteilt, an den Klaeger 640.000,00 EUR nebst Zinsen in Hoehe von "
        "5 Prozentpunkten ueber dem Basiszinssatz seit dem 12.05.2026 zu zahlen.",
        "2. Die Beklagte wird verurteilt, den ihr sicherungsuebereigneten Maschinenpark laut "
        "Anlagenverzeichnis vom 16.06.2025 an den Klaeger herauszugeben.",
        "3. Die Beklagte traegt die Kosten des Rechtsstreits.",
        "## Entscheidungsgruende",
        "Die Cash-Pool-Salden sind Gesellschafterdarlehen im Sinne des Paragraf 39 Abs. 1 Nr. 5 InsO; "
        "die Rueckfuehrung von 640.000,00 EUR im letzten Jahr vor Antragstellung ist nach Paragraf 135 "
        "Abs. 1 Nr. 2 InsO anfechtbar, ohne dass es auf Kenntnis ankommt. Die Sicherungsuebereignung "
        "vom 18.06.2025 ist nach Paragraf 135 Abs. 1 Nr. 1 InsO anfechtbar, da die tatsaechliche "
        "Bestellung der Sicherheit und nicht die schuldrechtliche Nachbesicherungsklausel von 2019 "
        "massgeblich ist. Die Rueckzahlung an den Mitgesellschafter Kastl bleibt demgegenueber "
        "unangefochten, da dieser als nicht geschaeftsfuehrender Gesellschafter mit 8 Prozent unter "
        "das Kleinbeteiligtenprivileg des Paragraf 39 Abs. 5 InsO faellt.",
    ],
    "Der Vorsitzende Richter am Landgericht",
)

# 24 - Kostenfestsetzungsbeschluss
make_docx(
    D / "24_kostenfestsetzungsbeschluss_2027-08-05.docx",
    "Landgericht Regensburg",
    "Kostenfestsetzungsbeschluss",
    [
        "Az. 2 O 987/26",
        "Beschluss vom 05.08.2027",
        "## Tenor",
        "Die von der Beklagten an den Klaeger zu erstattenden Kosten des Rechtsstreits werden auf "
        "24.680,00 EUR nebst Zinsen festgesetzt.",
        "## Berechnung",
        "1,3 Verfahrensgebuehr und 1,2 Terminsgebuehr aus einem Streitwert von 1.820.000,00 EUR "
        "(640.000,00 EUR Zahlungsantrag zuzueglich 1.180.000,00 EUR Herausgabeantrag) zuzueglich "
        "Sachverstaendigenkosten und Auslagen.",
    ],
    "Der Rechtspfleger",
)

# 25 - Schlussvermerk
make_docx(
    D / "25_schlussvermerk_verwalter_2027-09-20.docx",
    KOPF,
    "Schlussvermerk zur Handakte",
    [
        "Insolvenzverfahren Donaupart Praezisionstechnik GmbH, Az. 3 IN 152/26",
        "Vermerk vom 20.09.2027",
        "## Zusammenfassung",
        "Das Urteil des Landgerichts Regensburg vom 22.06.2027 (Az. 2 O 987/26) ist seit dem "
        "27.07.2027 rechtskraeftig. Die Beklagte hat die titulierte Summe von 640.000,00 EUR nebst "
        "Zinsen am 12.09.2027 vollstaendig gezahlt und den Maschinenpark am 15.09.2027 an die Masse "
        "herausgegeben. Die Rueckzahlung an den Mitgesellschafter Kastl blieb wie vom Verwalter "
        "zutreffend erkannt aufgrund des Kleinbeteiligtenprivilegs unangefochten.",
        "## Bewertung",
        "Der Fall bestaetigt, dass Cash-Pool-Salden im Konzern als Gesellschafterdarlehen zu "
        "qualifizieren sind und dass die tatsaechliche Bestellung einer Sicherheit fuer die "
        "Zehnjahresfrist des Paragraf 135 Abs. 1 Nr. 1 InsO massgeblich ist, unabhaengig von einer "
        "aelteren schuldrechtlichen Nachbesicherungsklausel.",
    ],
    "Dr. Ludwig Stadlbauer, Insolvenzverwalter",
)

print("Regensburg 17-25 erzeugt.")
