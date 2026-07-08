#!/usr/bin/env python3
"""Ausbau Stuttgart Konzernsicherheit-Anfechtung auf 25 Aktenstuecke."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from aktenbau import make_docx, make_csv

SLUG = "insolvenzanfechtung-unentgeltlich-konzernsicherheit-upstream-stuttgart"
D = Path("/home/user/workspace/legal-work/target/testakten") / SLUG

VERWALTERIN_KOPF = "Rechtsanwaeltin Dr. Sibylle Mangold - Mangold Restrukturierung\nBueroanschrift: Koenigstrasse 26, 70173 Stuttgart"
BANK_KOPF = "Berkhoff Lauterbach & Partner mbB\nMainzer Landstrasse 46, 60325 Frankfurt am Main"
GERICHT_KOPF = "Landgericht Stuttgart - 34. Zivilkammer fuer Handelssachen\nUrbanstrasse 20, 70182 Stuttgart"

make_docx(
    D / "16_klageschrift_bank_lg_stuttgart.docx",
    VERWALTERIN_KOPF,
    "Klageschrift",
    [
        "Landgericht Stuttgart",
        "34. Zivilkammer fuer Handelssachen",
        "Urbanstrasse 20, 70182 Stuttgart",
        "",
        "In dem Rechtsstreit",
        "Rechtsanwaeltin Dr. Sibylle Mangold, als Insolvenzverwalterin ueber das Vermoegen der Feinwerk Praezisionswerkzeuge GmbH",
        "- Klaegerin -",
        "gegen",
        "Sueddeutsche Kreditbank AG, vertreten durch den Vorstand, Bolzstrasse 3, 70173 Stuttgart",
        "- Beklagte -",
        "",
        "wird Klage erhoben mit dem Antrag, festzustellen, dass die Grundschuldbestellung vom 15.05.2023 ueber EUR 1.200.000,00 und die Buergschaftserklaerung vom selben Tag ueber EUR 800.000,00 gegenueber der Masse unwirksam sind, hilfsweise die Beklagte zu verurteilen, an die Klaegerin EUR 1.200.000,00 zu zahlen.",
        "## Begruendung",
        "Die Sicherheitenbestellung erfolgte unentgeltlich im Sinne des Paragraf 134 Abs. 1 InsO, da die Schuldnerin keine eigene, ausgleichsfaehige Gegenleistung erhalten hat. Der Rueckgriffsanspruch gegen die Muttergesellschaft war im Bestellungszeitpunkt nach dem Sanierungsgutachten vom 28.04.2023 bereits wertlos oder jedenfalls nicht werthaltig; das bankinterne Rating-Memo vom 05.05.2023 bestaetigt dies ausdruecklich mit dem Vermerk 'nicht belastbar'.",
    ],
    "Dr. Sibylle Mangold\nRechtsanwaeltin, Insolvenzverwalterin",
)

make_docx(
    D / "17_klageerwiderung_bank_2026-09-01.docx",
    BANK_KOPF,
    "Klageerwiderung",
    [
        "An das Landgericht Stuttgart - Az. 34 O 88/26 KfH",
        "",
        "Namens und im Auftrag der Beklagten wird beantragt, die Klage abzuweisen.",
        "## Begruendung",
        "Die Sicherheiten wurden im Rahmen eines Gesamtpakets bestellt, das der Schuldnerin mittelbare Vorteile durch Fortbestand der Unternehmensgruppe, Cash-Pooling und Konzernauftraege verschafft hat. Diese mittelbaren Vorteile schliessen die Unentgeltlichkeit aus. Das Sanierungsgutachten sei nur ein Zwischenstand gewesen; die Muttergesellschaft habe im Bestellungszeitpunkt noch als sanierungsfaehig gegolten.",
        "Die Beklagte habe zudem keine Kenntnis von einer etwaigen Wertlosigkeit des Rueckgriffsanspruchs gehabt; das interne Rating-Memo sei nicht Gegenstand der Kreditentscheidung im engeren Sinne gewesen.",
    ],
    "Berkhoff Lauterbach & Partner mbB",
)

make_docx(
    D / "18_replik_verwalterin_2026-09-22.docx",
    VERWALTERIN_KOPF,
    "Replik",
    [
        "An das Landgericht Stuttgart - Az. 34 O 88/26 KfH",
        "",
        "1. Bei der Unentgeltlichkeitsanfechtung nach Paragraf 134 InsO kommt es nicht auf Kenntnis der Beklagten an; die Anfechtung ist verschuldensunabhaengig ausgestaltet.",
        "2. Mittelbare Konzernvorteile (Fortbestand der Gruppe, Auftragslage) sind nach staendiger Rechtsprechung keine ausgleichsfaehige Gegenleistung der Tochter selbst, sondern reflektieren nur das eigene Konzerninteresse der Mutter.",
        "3. Das Rating-Memo datiert eine Woche vor der Bestellung und war ausweislich des Vermerks Grundlage der Konditionengestaltung; es ist daher kein bloss nachrangiges internes Papier.",
        "Es wird Fristsetzung zur Gegenerwiderung binnen drei Wochen beantragt.",
    ],
    "Dr. Sibylle Mangold\nRechtsanwaeltin, Insolvenzverwalterin",
)

make_docx(
    D / "19_duplik_bank_2026-10-13.docx",
    BANK_KOPF,
    "Duplik",
    [
        "An das Landgericht Stuttgart - Az. 34 O 88/26 KfH",
        "",
        "Die Beklagte haelt an ihrer Rechtsauffassung fest und bietet nunmehr Zeugenbeweis durch den ehemaligen CFO der Holding, Herrn Ludger Sattelmaier, zur Frage der im Bestellungszeitpunkt bestehenden Sanierungsaussichten der Mutter an.",
        "Ergaenzend wird ein Sachverstaendigengutachten zur Werthaltigkeit des Rueckgriffsanspruchs zum Stichtag 15.05.2023 beantragt.",
    ],
    "Berkhoff Lauterbach & Partner mbB",
)

make_docx(
    D / "20_beweisbeschluss_lg_stuttgart_2026-10-27.docx",
    GERICHT_KOPF,
    "Beweisbeschluss",
    [
        "Az. 34 O 88/26 KfH",
        "",
        "In dem Rechtsstreit Dr. Mangold ./. Sueddeutsche Kreditbank AG wird beschlossen:",
        "1. Es wird Beweis erhoben durch Vernehmung des Zeugen Ludger Sattelmaier zu den Sanierungsaussichten der Karrenberg Industrieholding GmbH zum Stichtag 15.05.2023.",
        "2. Es wird Beweis erhoben durch Einholung eines schriftlichen Sachverstaendigengutachtens zur Werthaltigkeit des Rueckgriffsanspruchs der Schuldnerin gegen die Holding zum selben Stichtag.",
        "3. Zum Sachverstaendigen wird bestellt: Prof. Dr. Elmar Wachsmuth, oeffentlich bestellter Sachverstaendiger fuer Unternehmensbewertung, Stuttgart.",
        "Stuttgart, 27.10.2026",
    ],
    "Vorsitzender Richter am Landgericht Dr. Holger Ammersbach",
)

make_docx(
    D / "21_sachverstaendigengutachten_wachsmuth_regressquote.docx",
    "Prof. Dr. Elmar Wachsmuth\nOeffentlich bestellter Sachverstaendiger, Stuttgart",
    "Schriftliches Sachverstaendigengutachten",
    [
        "Gutachten zur Werthaltigkeit des Rueckgriffsanspruchs der Feinwerk Praezisionswerkzeuge GmbH gegen die Karrenberg Industrieholding GmbH zum Stichtag 15.05.2023, erstattet im Auftrag des Landgerichts Stuttgart, Az. 34 O 88/26 KfH.",
        "1. Grundlage: Sanierungsgutachten Treumann & Cie. vom 28.04.2023, Finanzkennzahlenreihe 2019 bis Q1 2023 (Aktenstueck 15), Rating-Memo der Bank vom 05.05.2023.",
        "2. Befund: Die Eigenkapitalquote der Holding war zum Stichtag bereits negativ, die Zinsdeckung lag deutlich unter 1,0; eine im Sanierungsgutachten fuer moeglich gehaltene Fortfuehrung war an nicht gesicherte Zusatzfinanzierungen geknuepft.",
        "3. Ergebnis: Der Rueckgriffsanspruch der Schuldnerin war zum Stichtag mit einer Regressquote von schaetzungsweise 4 bis 7 Prozent des Nominalbetrags zu bewerten und damit wirtschaftlich nahezu wertlos.",
        "Stuttgart, 15.01.2027",
    ],
    "Prof. Dr. Elmar Wachsmuth",
)

make_docx(
    D / "22_zeugenvernehmungsprotokoll_sattelmaier.docx",
    GERICHT_KOPF,
    "Protokoll der Zeugenvernehmung",
    [
        "Termin vom 15.01.2027, Az. 34 O 88/26 KfH",
        "Zeuge: Ludger Sattelmaier, vormals CFO der Karrenberg Industrieholding GmbH",
        "",
        "Der Zeuge gibt an: 'Zum Zeitpunkt der Sicherheitenbestellung im Mai 2023 wussten wir intern bereits, dass die Sanierung nur mit zusaetzlichem, zu diesem Zeitpunkt nicht zugesagtem Kapital gelingen konnte. Ich habe das der Bank in dieser Deutlichkeit nicht mitgeteilt.'",
        "Protokollfuehrerin: Justizangestellte M. Herzberger",
    ],
    "Vorsitzender Richter am Landgericht Dr. Holger Ammersbach",
)

make_docx(
    D / "23_vergleichsverhandlungsprotokoll_2026-02-02.docx",
    GERICHT_KOPF,
    "Vergleichsverhandlungsprotokoll",
    [
        "Im Anschluss an die Beweisaufnahme vom 15.01.2027 erklaeren beide Parteien Vergleichsbereitschaft.",
        "Die Beklagte bietet eine Zahlung von EUR 480.000,00 zur Abgeltung saemtlicher wechselseitiger Anspruche aus der Sicherheitenbestellung an; die Klaegerin fordert unter Hinweis auf das Gutachtenergebnis EUR 620.000,00.",
        "Beiden Seiten wird eine Erklaerungsfrist bis zum 16.02.2027 eingeraeumt.",
    ],
    "Protokollfuehrer: Justizangestellter F. Brenneisen",
)

make_docx(
    D / "24_vergleichsvereinbarung_bank_2027-02-16.docx",
    VERWALTERIN_KOPF,
    "Vergleichsvereinbarung",
    [
        "Zwischen Rechtsanwaeltin Dr. Sibylle Mangold als Insolvenzverwalterin und der Sueddeutschen Kreditbank AG wird folgender Vergleich geschlossen:",
        "1. Die Beklagte zahlt an die Masse EUR 545.000,00 in drei Raten (je EUR 181.666,67 zum 15.03., 15.04. und 15.05.2027).",
        "2. Die Grundschuld und die Buergschaftserklaerung gelten mit vollstaendiger Zahlung als gegenueber der Masse abgefunden; ein weitergehender Rueckgewaehranspruch besteht nicht.",
        "3. Die Kosten des Rechtsstreits werden im Verhaeltnis 45 (Klaegerin) zu 55 (Beklagte) verteilt.",
    ],
    "Dr. Sibylle Mangold\nRechtsanwaeltin, Insolvenzverwalterin",
)

make_docx(
    D / "25_schlussvermerk_verwalterin_abschluss.docx",
    VERWALTERIN_KOPF,
    "Schlussvermerk",
    [
        "Der Vergleichsbetrag von EUR 545.000,00 ist in drei Raten vollstaendig auf dem Massekonto eingegangen (letzter Eingang 14.05.2027).",
        "Der Rechtsstreit gegen die Sueddeutsche Kreditbank AG ist damit wirtschaftlich abgeschlossen. Ansprueche gegen die Konsortin, Bankhaus Loewental KGaA, wurden gepruft und wegen untergeordneter Beteiligung (15 Prozent Konsortialanteil) sowie fehlender eigener Sicherheitenbestellung nicht weiterverfolgt.",
        "Die Akte wird zur Schlussrechnungslegung vorgemerkt.",
    ],
    "Dr. Sibylle Mangold\nRechtsanwaeltin, Insolvenzverwalterin",
)

make_csv(
    D / "csv" / "fristenliste_verjaehrung_paragraf_146_inso.csv",
    ["Anspruch", "Kenntnis Verwalterin ab", "Verjaehrung (3 Jahre)", "Status"],
    [
        ["Anfechtung Grundschuldbestellung", "26.05.2026", "31.12.2029", "gewahrt, Klage erhoben 20.07.2026"],
        ["Anfechtung Buergschaftserklaerung", "26.05.2026", "31.12.2029", "gewahrt, im selben Verfahren geltend gemacht"],
    ],
)
make_csv(
    D / "csv" / "ratenzahlungen_vergleich_bank.csv",
    ["Faelligkeit", "Betrag (EUR)", "Status"],
    [
        ["15.03.2027", "181.666,67", "eingegangen 14.03.2027"],
        ["15.04.2027", "181.666,67", "eingegangen 13.04.2027"],
        ["15.05.2027", "181.666,66", "eingegangen 14.05.2027"],
    ],
)

print("Stuttgart Kernstuecke 16-25 sowie csv/ erzeugt.")
