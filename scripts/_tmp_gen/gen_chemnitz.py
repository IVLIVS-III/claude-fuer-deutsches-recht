#!/usr/bin/env python3
"""Ausbau insolvenzanfechtung-bargeschaeft-vorkasse-rohstofflieferant-chemnitz auf >=25 Aktenstuecke."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from aktenbau import make_docx, TESTAKTEN

SLUG = "insolvenzanfechtung-bargeschaeft-vorkasse-rohstofflieferant-chemnitz"
D = TESTAKTEN / SLUG

KOPF_IV = "Rechtsanwaeltin Dr. Friederike Stollberg – Insolvenzverwalterin\nAnnaberger Strasse 73, 09120 Chemnitz"
KOPF_GEGNER = "Rechtsanwalt Dr. Lennart Huesgen\nWaisenhausstrasse 4, 01067 Dresden"
KOPF_GERICHT = "Landgericht Chemnitz – 3. Zivilkammer\nFuerstenstrasse 21, 09112 Chemnitz"

docs = [
("15_klageschrift_verwalterin_lg_chemnitz.docx", KOPF_IV,
 "Klageschrift",
 [
  "Landgericht Chemnitz\n3. Zivilkammer\nFuerstenstrasse 21, 09112 Chemnitz",
  "In dem Rechtsstreit\n\nRechtsanwaeltin Dr. Friederike Stollberg, als Insolvenzverwalterin ueber das Vermoegen der Vellnitz Kunststofftechnik GmbH\n– Klaegerin –\n\ngegen\n\nGranova Polymer Handels GmbH, vertreten durch den Geschaeftsfuehrer Dr. Peter Hallmert\n– Beklagte –",
  "wird namens und im Auftrag der Klaegerin Klage erhoben mit dem Antrag, die Beklagte zu verurteilen, an die Klaegerin die im Zeitraum 01.01.2026 bis 15.04.2026 geleisteten Vorkassezahlungen zurueckzuzahlen, soweit sie den Umfang eines nach Paragraf 142 InsO privilegierten Bargeschaefts uebersteigen.",
  "Begruendung: Die Beklagte stellte die Schuldnerin am 05.11.2025 einseitig von Zahlungsziel auf Vorkasse um, nachdem der Warenkreditversicherer Nordkredit die Kreditlimits am 28.10.2025 gestrichen hatte. Die Vorkassezahlungen im Anfechtungszeitraum ueberschreiten teilweise den engen zeitlichen Zusammenhang zwischen Zahlung und Gegenleistung, der fuer die Bargeschaeftsprivilegierung erforderlich ist (mehr als 30 Tage Abstand bei drei Lieferungen).",
  "Die Beklagte kannte die Zahlungsunfaehigkeit der Schuldnerin aufgrund des Kurzgutachtens zur Insolvenzreife vom 18.07.2025 (das der Beklagten im Rahmen der Kreditverhandlungen vorgelegt wurde) sowie des internen Kreditentscheidungsvermerks vom 03.11.2025.",
  "Dr. Friederike Stollberg\nRechtsanwaeltin, Insolvenzverwalterin"]),

("16_klageerwiderung_granova.docx", KOPF_GEGNER,
 "Klageerwiderung",
 [
  "An das Landgericht Chemnitz – Az. 5 O 233/26",
  "Namens und im Auftrag der Beklagten wird beantragt, die Klage abzuweisen.",
  "Die Umstellung auf Vorkasse war eine ueblicherweise praktizierte Reaktion auf die Streichung des Warenkreditversicherungslimits und begruendet fuer sich keine Kenntnis von einer Zahlungsunfaehigkeit. Das Kurzgutachten vom 18.07.2025 wurde der Beklagten nicht vorgelegt, sondern lediglich in stark verkuerzter, anonymisierter Form im Rahmen allgemeiner Sanierungsgespraeche referenziert.",
  "Saemtliche streitgegenstaendlichen Zahlungen stehen in unmittelbarem zeitlichem Zusammenhang mit der jeweiligen Warenlieferung und sind daher nach Paragraf 142 InsO privilegierte Bargeschaefte.",
  "Dr. Lennart Huesgen\nRechtsanwalt"]),

("17_duplik_verwalterin.docx", KOPF_IV,
 "Duplik der Klaegerin",
 [
  "An das Landgericht Chemnitz – Az. 5 O 233/26",
  "Die Klaegerin haelt an ihrem Vortrag fest. Der interne Vermerk der Beklagten vom 03.11.2025 (Aktenstueck 14) belegt, dass der Restrukturierungsberater Dr. Feldkamp der Beklagten am 30.10.2025 Kernzahlen aus dem Kurzgutachten mitgeteilt hat, um eine weitere Belieferung zu erwirken. Dies begruendet eine positive Kenntnis von einer drohenden Zahlungsunfaehigkeit im Sinne des Paragraf 130 Absatz 2 InsO.",
  "Ferner ergibt der Rechnungs-Zahlungs-Abgleich (Aktenstueck 06), dass drei Zahlungen jeweils mehr als 30 Tage vor der zugehoerigen Lieferung erfolgten und damit ausserhalb des von der Rechtsprechung anerkannten engen zeitlichen Zusammenhangs liegen (BGH-Rechtsprechung zum Bargeschaeft, live zu verifizieren).",
  "Dr. Friederike Stollberg\nRechtsanwaeltin"]),

("18_triplik_granova.docx", KOPF_GEGNER,
 "Triplik der Beklagten",
 [
  "An das Landgericht Chemnitz – Az. 5 O 233/26",
  "Die Beklagte bestreitet, dass der Restrukturierungsberater Dr. Feldkamp konkrete Zahlen aus dem Kurzgutachten mitgeteilt habe. Der Vermerk vom 03.11.2025 beziehe sich lediglich auf allgemeine Aussagen zur Marktentwicklung im Kunststoffsektor.",
  "Hilfsweise wird die Einholung eines Sachverstaendigengutachtens zur Frage beantragt, ob die drei streitigen Zahlungen tatsaechlich ausserhalb des fuer Bargeschaefte unschaedlichen Zeitraums lagen, da die Lieferungen in Teilchargen erfolgten und die Zuordnung streitig ist.",
  "Dr. Lennart Huesgen\nRechtsanwalt"]),

("19_beweisbeschluss_lg_chemnitz.docx", KOPF_GERICHT,
 "Beweisbeschluss",
 [
  "Az. 5 O 233/26",
  "In dem Rechtsstreit Dr. Stollberg ./. Granova Polymer Handels GmbH wird beschlossen:",
  "1. Es wird Beweis erhoben durch Vernehmung des Zeugen Dr. Roman Feldkamp zu der Behauptung, er habe der Beklagten am 30.10.2025 Kernzahlen aus dem Kurzgutachten zur Insolvenzreife mitgeteilt.",
  "2. Es wird Beweis erhoben durch Einholung eines schriftlichen Sachverstaendigengutachtens zur zeitlichen Zuordnung der drei streitigen Zahlungen zu den jeweiligen Teillieferungen.",
  "3. Zum Sachverstaendigen wird bestellt: Diplom-Kaufmann Sven Ottersbach, oeffentlich bestellter Sachverstaendiger fuer betriebswirtschaftliche Bewertung, Leipzig.",
  "Chemnitz, 15.09.2026\nVorsitzender Richter am Landgericht Dr. Tobias Reichenbach"]),

("20_zeugenvernehmungsprotokoll_feldkamp.docx", KOPF_GERICHT,
 "Protokoll der Zeugenvernehmung",
 [
  "Termin vom 08.10.2026, Az. 5 O 233/26",
  "Zeuge: Dr. Roman Feldkamp, Restrukturierungsberater",
  "Der Zeuge gibt an: 'Ich habe Herrn Sarrasin am 30.10.2025 telefonisch mitgeteilt, dass die Liquiditaetsluecke der Vellnitz Kunststofftechnik erheblich sei und ich empfehle, nur noch gegen Vorkasse zu liefern. Konkrete Zahlen aus dem Kurzgutachten habe ich nicht genannt, aber der Tenor war eindeutig alarmierend.'",
  "Auf Nachfrage der Klaegervertretung: 'Ja, ich habe deutlich gemacht, dass eine Insolvenz in absehbarer Zeit drohen koennte.'",
  "Protokollfuehrerin: Justizangestellte C. Wendlandt"]),

("21_sachverstaendigengutachten_ottersbach_zuordnung.docx", "Dipl.-Kfm. Sven Ottersbach\nOeffentlich bestellter Sachverstaendiger, Leipzig",
 "Schriftliches Sachverstaendigengutachten",
 [
  "Gutachten zur zeitlichen Zuordnung der Vorkassezahlungen zu den Teillieferungen, erstattet im Auftrag des Landgerichts Chemnitz, Az. 5 O 233/26",
  "1. Grundlage: Rechnungs-Zahlungs-Matching Januar bis April 2026 (Aktenstueck 06), Lieferscheine und Chargenprotokolle der Beklagten.",
  "2. Befund: Von 14 Zahlungen im Anfechtungszeitraum stehen elf in einem Abstand von weniger als 30 Tagen zur zugehoerigen Teillieferung. Drei Zahlungen (Rechnungen RE-2026-0142, RE-2026-0187 und RE-2026-0210) weisen einen Abstand von 34, 41 und 52 Tagen auf.",
  "3. Ergebnis: Fuer die elf zeitnahen Zahlungen ist von einem engen zeitlichen Zusammenhang im Sinne des Paragraf 142 InsO auszugehen. Fuer die drei abweichenden Zahlungen mit Gesamtvolumen von EUR 61.200,00 liegt kein privilegiertes Bargeschaeft vor.",
  "Leipzig, 20.11.2026\nDipl.-Kfm. Sven Ottersbach"]),

("22_stellungnahme_granova_zum_gutachten.docx", KOPF_GEGNER,
 "Stellungnahme zum Sachverstaendigengutachten",
 [
  "An das Landgericht Chemnitz – Az. 5 O 233/26",
  "Die Beklagte akzeptiert den Befund des Sachverstaendigen zu den drei abweichenden Zahlungen, haelt aber die Kenntnisfrage weiterhin fuer streitig. Angesichts des reduzierten Streitgegenstands (nunmehr EUR 61.200,00 statt urspruenglich EUR 184.500,00) regt die Beklagte eine vergleichsweise Erledigung an.",
  "Dr. Lennart Huesgen\nRechtsanwalt"]),

("23_vergleichsvorschlag_und_annahme.docx", KOPF_IV,
 "Vergleichsvorschlag und Annahme",
 [
  "An das Landgericht Chemnitz – Az. 5 O 233/26",
  "Die Klaegerin schlaegt vor: Zahlung von EUR 45.000,00 durch die Beklagte gegen vollstaendige Erledigung aller wechselseitigen Ansprueche und hälftige Kostenteilung. Die Beklagte hat mit Schreiben vom 10.12.2026 zugestimmt.",
  "Wir bitten um gerichtliche Feststellung gemaess Paragraf 278 Absatz 6 ZPO.",
  "Dr. Friederike Stollberg\nRechtsanwaeltin"]),

("24_feststellungsbeschluss_vergleich_chemnitz.docx", KOPF_GERICHT,
 "Beschluss ueber das Zustandekommen und den Inhalt des Vergleichs",
 [
  "Az. 5 O 233/26",
  "Das Gericht stellt gemaess Paragraf 278 Absatz 6 ZPO fest, dass zwischen den Parteien ein Vergleich mit folgendem Inhalt zustande gekommen ist:",
  "1. Die Beklagte zahlt an die Klaegerin EUR 45.000,00 binnen vier Wochen nach Rechtskraft.",
  "2. Im Uebrigen sind alle wechselseitigen Ansprueche aus dem streitgegenstaendlichen Sachverhalt erledigt.",
  "3. Die Kosten des Rechtsstreits werden gegeneinander aufgehoben.",
  "Chemnitz, 22.12.2026\nVorsitzender Richter am Landgericht Dr. Tobias Reichenbach"]),

("25_schlussvermerk_verwalterin.docx", KOPF_IV,
 "Aktenvermerk: Abschluss des Anfechtungsverfahrens",
 [
  "Az. 15 IN 388/26, Rechtsstreit 5 O 233/26",
  "Der Vergleichsbetrag von EUR 45.000,00 ist am 20.01.2027 auf dem Massekonto der Vellnitz Kunststofftechnik GmbH i.I. eingegangen. Der Anfechtungsanspruch gegen die Granova Polymer Handels GmbH ist damit vollstaendig erledigt und wird im Schlussbericht ausgewiesen.",
  "Dr. Friederike Stollberg\nRechtsanwaeltin, Insolvenzverwalterin"]),
]

for fname, kopf, titel, absaetze in docs:
    make_docx(D / fname, kopf, titel, absaetze)

print(f"Erzeugt: {len(docs)} Aktenstuecke fuer {SLUG}")
