#!/usr/bin/env python3
"""Ausbau insolvenzanfechtung-kontokorrent-verrechnungen-geduldete-ueberziehung-dortmund auf >=25 Aktenstuecke."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from aktenbau import make_docx, TESTAKTEN

SLUG = "insolvenzanfechtung-kontokorrent-verrechnungen-geduldete-ueberziehung-dortmund"
D = TESTAKTEN / SLUG

KOPF_IV = "Rechtsanwalt Dr. Konstantin Wehmeyer – Insolvenzverwalter\nHansastrasse 90, 44137 Dortmund"
KOPF_BANK_ANW = "Terhardt & Cloppenburg Rechtsanwaelte\nPrinzipalmarkt 21, 48143 Muenster"
KOPF_GERICHT = "Landgericht Dortmund – 8. Zivilkammer\nGerichtsplatz 1, 44135 Dortmund"

docs = [
("14_duplik_verwalter_saldodifferenz.docx", KOPF_IV,
 "Duplik des Insolvenzverwalters",
 [
  "An das Landgericht Dortmund – Az. 8 O 112/26",
  "Die Klaegerseite haelt an der Saldodifferenzbetrachtung Hoechststand zu Endsaldo fest: Am 05.02.2026 betrug die Kontokorrentschuld EUR 309.900,00, am Ende des Anfechtungszeitraums (15.04.2026) noch EUR 226.300,00. Die Rueckfuehrung von EUR 83.600,00 ist in einen inkongruenten Teil (Rueckfuehrung der geduldeten Ueberziehung von EUR 309.900,00 auf die Kreditlinie von EUR 250.000,00, mithin EUR 59.900,00) und einen kongruenten Teil (innerhalb der Linie, EUR 23.700,00) aufzuteilen.",
  "Fuer den inkongruenten Teil kommt es nach Paragraf 131 Absatz 1 Nr. 1 und Nr. 2 InsO nicht auf die Kenntnis der Bank an, da die geduldete Ueberziehung woechentlich widerruflich war und keinen Anspruch auf Rueckfuehrung 'in der Art' begruendete.",
  "Der Bargeschaeftseinwand der Bank greift nicht durch, da die Verrechnung von Kundenzahlungseingaengen mit dem debitorischen Konto keine Gegenleistung im Sinne des Paragraf 142 InsO darstellt, sondern eine reine Kreditrueckfuehrung.",
  "Dr. Konstantin Wehmeyer\nRechtsanwalt, Insolvenzverwalter"]),

("15_triplik_bank_globalzession.docx", KOPF_BANK_ANW,
 "Triplik der Beklagten",
 [
  "An das Landgericht Dortmund – Az. 8 O 112/26",
  "Die Beklagte haelt an ihrer Rechtsauffassung fest. Die eingehenden Kundenzahlungen waren aufgrund der wirksamen Globalzession vom 30.06.2021 bereits vorab an die Beklagte abgetreten. Eine Glaeubigerbenachteiligung durch die Verrechnung liegt daher nicht vor, da die Zahlungseingaenge wirtschaftlich nie zur Masse gehoert haetten.",
  "Hilfsweise wird bestritten, dass die Beklagte im relevanten Zeitraum positive Kenntnis von der Zahlungsunfaehigkeit der Schuldnerin hatte. Die Kuendigung des Kontokorrents am 08.04.2026 erfolgte aus allgemeiner Risikovorsorge, nicht aufgrund konkreter Kenntnis einer Zahlungseinstellung.",
  "Dr. Matthias Terhardt\nRechtsanwalt"]),

("16_beweisbeschluss_lg_dortmund.docx", KOPF_GERICHT,
 "Beweisbeschluss",
 [
  "Az. 8 O 112/26",
  "In dem Rechtsstreit Dr. Wehmeyer ./. Volksbank Emscher-Hellweg eG wird beschlossen:",
  "1. Es wird Beweis erhoben durch Vernehmung der Zeugin Dr. Beate Sanders (Marktfolge Kredit der Beklagten) zu der Behauptung, die Kuendigung des Kontokorrents vom 08.04.2026 sei aus allgemeiner Risikovorsorge und nicht aufgrund konkreter Kenntnis der Zahlungsunfaehigkeit erfolgt.",
  "2. Es wird Beweis erhoben durch Einholung eines schriftlichen Sachverstaendigengutachtens zur Wirksamkeit und zum Umfang der Globalzession vom 30.06.2021 sowie zur Frage, ob und in welchem Umfang durch die Verrechnung eine Glaeubigerbenachteiligung eingetreten ist.",
  "3. Zur Sachverstaendigen wird bestellt: Prof. Dr. Insa Lohmeyer, Lehrstuhl fuer Bank- und Insolvenzrecht, Universitaet Bochum.",
  "Dortmund, 30.09.2026\nVorsitzende Richterin am Landgericht Dr. Miriam Kastrup"]),

("17_zeugenvernehmungsprotokoll_sanders.docx", KOPF_GERICHT,
 "Protokoll der Zeugenvernehmung",
 [
  "Termin vom 20.10.2026, Az. 8 O 112/26",
  "Zeugin: Dr. Beate Sanders, Marktfolge Kredit, Volksbank Emscher-Hellweg eG",
  "Die Zeugin gibt an: 'Wir haben die Kuendigung ausgesprochen, weil die Ueberziehung dauerhaft ueber der Linie lag und mehrere Lastschriften zurueckgegeben werden mussten. Ob das Unternehmen schon insolvenzreif war, konnte ich zu diesem Zeitpunkt nicht sicher beurteilen, aber die Signale waren eindeutig negativ.'",
  "Auf Nachfrage des Klaegervertreters: 'Der Gespraechsvermerk vom 28.01.2026 spiegelt meine damalige Einschaetzung wider, dass eine Fortfuehrung ohne zusaetzliche Sicherheiten nicht mehr vertretbar war.'",
  "Protokollfuehrer: Justizangestellter T. Brammertz"]),

("18_sachverstaendigengutachten_lohmeyer_globalzession.docx", "Prof. Dr. Insa Lohmeyer\nLehrstuhl fuer Bank- und Insolvenzrecht, Universitaet Bochum",
 "Schriftliches Sachverstaendigengutachten",
 [
  "Gutachten zur Wirksamkeit der Globalzession und zur Glaeubigerbenachteiligung, erstattet im Auftrag des Landgerichts Dortmund, Az. 8 O 112/26",
  "1. Die Globalzession vom 30.06.2021 ist wirksam vereinbart, unterliegt jedoch dem Anfechtungsregime der Paragrafen 129 ff. InsO wie jede andere Rechtshandlung auch (BGH-Rechtsprechung zur revolvierenden Globalzession, live zu verifizieren).",
  "2. Die Verrechnung von Kundenzahlungseingaengen mit dem debitorischen Konto stellt trotz vorab erfolgter Abtretung eine anfechtbare Rechtshandlung dar, wenn und soweit die Abtretung selbst im Dreimonatszeitraum vor Antragstellung inkongruent oder zumindest kongruent unter Kenntnis der Zahlungsunfaehigkeit erfolgte.",
  "3. Vorliegend wurde die Globalzession bereits 2021 vereinbart, mithin ausserhalb der Anfechtungsfristen. Fuer die Frage der Glaeubigerbenachteiligung kommt es daher darauf an, ob die einzelnen Einzugsermaechtigungen im Anfechtungszeitraum wirtschaftlich der Masse zugestanden haetten.",
  "4. Ergebnis: Eine Glaeubigerbenachteiligung liegt in Hoehe der Saldorueckfuehrung von EUR 83.600,00 vor, da diese Betraege ohne die Verrechnung der Masse zur Verfuegung gestanden haetten.",
  "Bochum, 15.12.2026\nProf. Dr. Insa Lohmeyer"]),

("19_stellungnahme_bank_zum_gutachten.docx", KOPF_BANK_ANW,
 "Stellungnahme zum Sachverstaendigengutachten",
 [
  "An das Landgericht Dortmund – Az. 8 O 112/26",
  "Die Beklagte nimmt zum Gutachten von Prof. Dr. Lohmeyer vom 15.12.2026 Stellung und weist darauf hin, dass die Gutachterin die Frage der subjektiven Kenntnis der Beklagten im Zeitpunkt der jeweiligen Verrechnungen nicht abschliessend beantwortet hat.",
  "Angesichts der Aussage der Zeugin Dr. Sanders und der objektiven Feststellungen des Gutachtens regt die Beklagte eine vergleichsweise Erledigung an, um das verbleibende Prozessrisiko beiderseits zu begrenzen.",
  "Dr. Matthias Terhardt\nRechtsanwalt"]),

("20_vergleichsvorschlag_verwalter.docx", KOPF_IV,
 "Vergleichsvorschlag",
 [
  "An das Landgericht Dortmund – Az. 8 O 112/26, nachrichtlich an die Beklagtenvertretung",
  "Der Insolvenzverwalter unterbreitet folgenden Vergleichsvorschlag:",
  "1. Die Beklagte zahlt an die Insolvenzmasse EUR 52.000,00 binnen vier Wochen nach Rechtskraft des Feststellungsbeschlusses.",
  "2. Der Insolvenzverwalter verzichtet auf die Geltendmachung des Restbetrags von EUR 31.600,00 sowie auf Zinsen.",
  "3. Die Kosten des Rechtsstreits werden im Verhaeltnis 60 zu 40 zu Lasten der Beklagten verteilt.",
  "Dr. Konstantin Wehmeyer\nRechtsanwalt, Insolvenzverwalter"]),

("21_vergleichsannahme_bank.docx", KOPF_BANK_ANW,
 "Annahme des Vergleichsvorschlags",
 [
  "An das Landgericht Dortmund – Az. 8 O 112/26",
  "Die Beklagte nimmt den Vergleichsvorschlag vom 22.12.2026 in vollem Umfang an und bittet um gerichtliche Feststellung gemaess Paragraf 278 Absatz 6 ZPO.",
  "Dr. Matthias Terhardt\nRechtsanwalt"]),

("22_feststellungsbeschluss_vergleich.docx", KOPF_GERICHT,
 "Beschluss ueber das Zustandekommen und den Inhalt des Vergleichs",
 [
  "Az. 8 O 112/26",
  "Das Gericht stellt gemaess Paragraf 278 Absatz 6 ZPO fest, dass zwischen den Parteien folgender Vergleich zustande gekommen ist:",
  "1. Die Beklagte zahlt an den Klaeger EUR 52.000,00 binnen vier Wochen nach Rechtskraft dieses Beschlusses.",
  "2. Im Uebrigen verzichtet der Klaeger auf weitergehende Anspruche aus dem streitgegenstaendlichen Sachverhalt.",
  "3. Die Kosten des Rechtsstreits tragen die Beklagte zu 60 Prozent und der Klaeger zu 40 Prozent.",
  "Streitwert: EUR 83.600,00",
  "Dortmund, 10.01.2027\nVorsitzende Richterin am Landgericht Dr. Miriam Kastrup"]),

("23_zahlungseingang_massekonto_bestaetigung.docx", KOPF_IV,
 "Aktenvermerk: Zahlungseingang aus Vergleich",
 [
  "Az. 251 IN 74/26, Rechtsstreit 8 O 112/26",
  "Am 04.02.2027 ist der Vergleichsbetrag in Hoehe von EUR 52.000,00 auf dem Massekonto der Ruhrland Getraenkegrosshandel GmbH i.I. eingegangen.",
  "Der Vorgang ist damit erledigt und wird im Schlussbericht als realisierter Anfechtungsanspruch ausgewiesen.",
  "Dr. Konstantin Wehmeyer\nRechtsanwalt, Insolvenzverwalter"]),

("24_verteilungsverzeichnis_auszug.docx", KOPF_IV,
 "Verteilungsverzeichnis (Auszug)",
 [
  "Az. 251 IN 74/26",
  "Auszug aus dem Verteilungsverzeichnis der Ruhrland Getraenkegrosshandel GmbH i.I., Stand 01.03.2027.",
  "Realisierte Anfechtungsanspruche: EUR 52.000,00 (Volksbank Emscher-Hellweg eG, Vergleich vom 10.01.2027).",
  "Die Verteilungsquote fuer die Insolvenzglaeubiger erhoeht sich durch diesen Anfechtungserloes um rechnerisch 1,4 Prozentpunkte.",
  "Dr. Konstantin Wehmeyer\nRechtsanwalt, Insolvenzverwalter"]),

("25_kostenfestsetzungsbeschluss.docx", KOPF_GERICHT,
 "Kostenfestsetzungsbeschluss",
 [
  "Az. 8 O 112/26",
  "Auf Antrag der Parteien werden die zu erstattenden aussergerichtlichen Kosten wie folgt festgesetzt: Klaeger EUR 3.120,40, Beklagte EUR 4.680,60, jeweils entsprechend der Kostenquote 40 zu 60.",
  "Dortmund, 24.02.2027\nRechtspflegerin am Landgericht Dortmund"]),
]

for fname, kopf, titel, absaetze in docs:
    make_docx(D / fname, kopf, titel, absaetze)

print(f"Erzeugt: {len(docs)} Aktenstuecke fuer {SLUG}")
