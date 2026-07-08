#!/usr/bin/env python3
"""Ausbau geschaeftsfuehrerhaftung-15b-inso-zahlungen-nach-insolvenzreife-hannover auf >=25 Aktenstuecke.
Zahlen konsistent mit Anspruchsschreiben (Aktenstueck 11) und Replik (Aktenstueck 13):
Gesamtzahlungen 1.238.400 EUR, anerkannt 158.300 EUR, Erstattungsbetrag 1.080.100 EUR,
davon Beraterhonorar Ohlendorf Beteiligungs-UG 48.000 EUR (Sec. 15b Abs. 5 InsO)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from aktenbau import make_docx, TESTAKTEN

SLUG = "geschaeftsfuehrerhaftung-15b-inso-zahlungen-nach-insolvenzreife-hannover"
D = TESTAKTEN / SLUG

KOPF_IV = "Rechtsanwaeltin Dr. Henrike Wittkopp – Insolvenzverwalterin\nGeorgstrasse 24, 30159 Hannover"
KOPF_VERT = "Lohgerber Voss Rechtsanwaelte PartG mbB\nSchiffgraben 41, 30175 Hannover"
KOPF_DO = "Hannoversche Kaution und Industrie Versicherung AG\nSchiffgraben 20, 30159 Hannover"
KOPF_GERICHT = "Landgericht Hannover – 21. Zivilkammer\nVolgersweg 65, 30175 Hannover"

docs = [
("15_duplik_verteidiger.docx", KOPF_VERT,
 "Duplik des Verteidigers",
 [
  "An Frau Rechtsanwaeltin Dr. Henrike Wittkopp",
  "Die Replik vom 03.07.2026 aendert nichts an der Rechtsauffassung der Verteidigung. Herr Ohlendorf hat sich um eine Fortfuehrung im Interesse der Arbeitsplaetze und Glaeubiger bemueht; von einer masseverzehrenden Verlustfortfuehrung koenne keine Rede sein, da der Betrieb ohne die Zahlungen sofort haette eingestellt werden muessen.",
  "Zum Beraterhonorar wird nunmehr vorgetragen, dass die Ohlendorf Beteiligungs-UG tatsaechlich Marketingleistungen (Social-Media-Kampagnen, Flyer-Konzepte) erbracht habe; entsprechende Unterlagen wuerden nachgereicht.",
  "Eine aussergerichtliche Einigung wird angesichts der Deckungspruefung des D&O-Versicherers derzeit nicht fuer sachgerecht gehalten.",
  "Dr. Cornelius Lohgerber\nRechtsanwalt"]),

("16_klageschrift_verwalterin_lg_hannover.docx", KOPF_IV,
 "Klageschrift",
 [
  "Landgericht Hannover\n21. Zivilkammer\nVolgersweg 65, 30175 Hannover",
  "In dem Rechtsstreit\n\nRechtsanwaeltin Dr. Henrike Wittkopp, als Insolvenzverwalterin ueber das Vermoegen der Nordlicht Systemgastronomie GmbH\n– Klaegerin –\n\ngegen\n\nHerrn Sven Ohlendorf, Ahornweg 3, 30916 Isernhagen\n– Beklagter –",
  "wird namens und im Auftrag der Klaegerin Klage erhoben mit dem Antrag, den Beklagten zu verurteilen, an die Klaegerin EUR 1.080.100,00 nebst Zinsen seit dem 02.07.2026 zu zahlen.",
  "Begruendung: Der Beklagte hat als Geschaeftsfuehrer der Schuldnerin zwischen dem 22.09.2025 und dem 20.01.2026 Zahlungen in Hoehe von insgesamt EUR 1.238.400,00 nach Eintritt der Zahlungsunfaehigkeit (spaetestens 22.09.2025) geleistet, die entgegen Paragraf 15b Absatz 1 InsO nicht mit der Sorgfalt eines ordentlichen Geschaeftsmanns vereinbar waren. Nach Abzug der anerkannten privilegierten Positionen von EUR 158.300,00 verbleibt ein Erstattungsanspruch von EUR 1.080.100,00 aus Paragraf 15b Absatz 4 Satz 1 InsO, davon EUR 48.000,00 zusaetzlich gestuetzt auf Paragraf 15b Absatz 5 InsO (Zahlungen an die Alleingesellschafterin Ohlendorf Beteiligungs-UG).",
  "Der Klaegerin ist es unbenommen, dem Beklagten den Streit gegenueber dem D&O-Versicherer zu verkuenden.",
  "Dr. Henrike Wittkopp\nRechtsanwaeltin, Insolvenzverwalterin"]),

("17_klageerwiderung_verteidiger_lg_hannover.docx", KOPF_VERT,
 "Klageerwiderung",
 [
  "An das Landgericht Hannover – Az. 21 O 156/26",
  "Namens des Beklagten wird beantragt, die Klage abzuweisen. Der Beklagte bestreitet den von der Klaegerin angenommenen Zeitpunkt des Eintritts der Zahlungsunfaehigkeit (22.09.2025) und behauptet, eine Sanierung sei bis zur endgueltigen Absage der Bank am 05.01.2026 (Aktenstueck 14) ernsthaft aussichtsreich gewesen.",
  "Zu den Zahlungen an die Ohlendorf Beteiligungs-UG (EUR 48.000,00) wird nunmehr vorgetragen, dass tatsaechlich Marketingleistungen erbracht wurden; entsprechende Nachweise werden angekuendigt, aber nicht vorgelegt.",
  "Dr. Cornelius Lohgerber\nRechtsanwalt"]),

("18_streitverkuendung_do_versicherer.docx", KOPF_VERT,
 "Streitverkuendung",
 [
  "An die Hannoversche Kaution und Industrie Versicherung AG, Police FL-DO-2023-448291",
  "Namens des Beklagten Sven Ohlendorf wird der Hannoverschen Kaution und Industrie Versicherung AG in dem Rechtsstreit Dr. Wittkopp ./. Ohlendorf, Az. 21 O 156/26, der Streit verkuendet, da der Beklagte im Falle des Unterliegens Deckungsanspruch aus der D&O-Versicherung geltend machen wird.",
  "Dr. Cornelius Lohgerber\nRechtsanwalt"]),

("19_beitrittserklaerung_do_versicherer.docx", KOPF_DO,
 "Beitrittserklaerung des Streitverkuendeten",
 [
  "An das Landgericht Hannover – Az. 21 O 156/26",
  "Die Hannoversche Kaution und Industrie Versicherung AG tritt dem Rechtsstreit auf Seiten des Beklagten Sven Ohlendorf bei, ohne damit eine Deckungszusage abzugeben. Der Deckungsanspruch wird gesondert im Deckungsverhaeltnis geprueft, insbesondere im Hinblick auf den Ausschluss wissentlicher Pflichtverletzungen gemaess Ziffer 5.3 der Versicherungsbedingungen, der fuer die Zahlungen an die Alleingesellschafterin von besonderer Bedeutung sein duerfte.",
  "Rechtsabteilung, i. A. Dr. Konrad Ellermann"]),

("20_beweisbeschluss_lg_hannover.docx", KOPF_GERICHT,
 "Beweisbeschluss",
 [
  "Az. 21 O 156/26",
  "In dem Rechtsstreit Dr. Wittkopp ./. Ohlendorf wird beschlossen:",
  "1. Es wird Beweis erhoben durch Vernehmung der Zeugin Marlies Petersilie (Buchhaltung) zur Frage, ob und welche Leistungsnachweise fuer das Beraterhonorar an die Ohlendorf Beteiligungs-UG existieren.",
  "2. Es wird Beweis erhoben durch Einholung eines ergaenzenden schriftlichen Sachverstaendigengutachtens zur Bestaetigung des Zeitpunkts des Eintritts der Zahlungsunfaehigkeit (22.09.2025) anhand der Buchhaltungsunterlagen.",
  "3. Zur Sachverstaendigen wird bestellt: Dr. Judith Ossenberg-Engels, oeffentlich bestellte Sachverstaendige fuer Unternehmensbewertung und Insolvenzen, Hannover.",
  "Hannover, 25.09.2026\nVorsitzender Richter am Landgericht Dr. Falko Brammer"]),

("21_sachverstaendigengutachten_ossenberg_zahlungsunfaehigkeit.docx", "Dr. Judith Ossenberg-Engels\nOeffentlich bestellte Sachverstaendige, Hannover",
 "Schriftliches Sachverstaendigengutachten",
 [
  "Gutachten zum Zeitpunkt des Eintritts der Zahlungsunfaehigkeit der Nordlicht Systemgastronomie GmbH, erstattet im Auftrag des Landgerichts Hannover, Az. 21 O 156/26",
  "1. Grundlage: BWA-Monatsreihe 2025 (Aktenstueck 06), Liquiditaetsstatus zu Stichtagen 2025/2026 (Aktenstueck 05), Zahlungsauswertung nach Insolvenzreife (Aktenstueck 07).",
  "2. Befund: Die Unterdeckung der fälligen Verbindlichkeiten betrug bereits zum 31.05.2025 mehr als 15 Prozent und zum 31.08.2025 rund 34 Prozent. Die von der Klaegerin angenommene Zahlungsunfaehigkeit zum 22.09.2025 (drei Wochen nach dem Stichtag 31.08.2025) wird bestaetigt.",
  "3. Ergebnis: Die Ermittlung der Klaegerin zum Zeitpunkt des Eintritts der Zahlungsunfaehigkeit ist zutreffend und nachvollziehbar hergeleitet.",
  "Hannover, 05.12.2026\nDr. Judith Ossenberg-Engels"]),

("22_zeugenvernehmungsprotokoll_petersilie.docx", KOPF_GERICHT,
 "Protokoll der Zeugenvernehmung",
 [
  "Termin vom 15.12.2026, Az. 21 O 156/26",
  "Zeugin: Marlies Petersilie, Buchhaltung der Schuldnerin",
  "Die Zeugin gibt an: 'Ich habe nie Leistungsnachweise oder Rechnungen mit Leistungsbeschreibung fuer die Zahlungen an die Ohlendorf Beteiligungs-UG erhalten, nur die monatliche Pauschale von 12.000 Euro. Auf meine Nachfrage sagte Herr Ohlendorf, das sei Marketingberatung, aber ich habe nie ein Konzept oder eine Rechnung gesehen.'",
  "Protokollfuehrerin: Justizangestellte B. Wilkening"]),

("23_teilanerkenntnis_verteidiger.docx", KOPF_VERT,
 "Teilanerkenntnis",
 [
  "An das Landgericht Hannover – Az. 21 O 156/26",
  "Angesichts der Aussage der Zeugin Petersilie und des Sachverstaendigengutachtens erkennt der Beklagte den Klageanspruch in Hoehe von EUR 48.000,00 (Zahlungen an die Ohlendorf Beteiligungs-UG, Paragraf 15b Absatz 5 InsO) an.",
  "Im Uebrigen wird angesichts des bestaetigten Zeitpunkts der Zahlungsunfaehigkeit eine vergleichsweise Regelung fuer den Restbetrag von EUR 1.032.100,00 angeregt, um das beiderseitige Prozessrisiko und die Frage der D&O-Deckung zu begrenzen.",
  "Dr. Cornelius Lohgerber\nRechtsanwalt"]),

("24_teilanerkenntnisurteil_und_vergleich.docx", KOPF_GERICHT,
 "Teilanerkenntnisurteil und Vergleich",
 [
  "Az. 21 O 156/26",
  "Das Gericht erlaesst folgendes Teilanerkenntnisurteil: Der Beklagte wird verurteilt, an die Klaegerin EUR 48.000,00 nebst Zinsen zu zahlen.",
  "Im Uebrigen wird gemaess Paragraf 278 Absatz 6 ZPO festgestellt, dass zwischen den Parteien folgender Vergleich zustande gekommen ist: Der Beklagte zahlt zusaetzlich EUR 420.000,00 auf den Restanspruch von EUR 1.032.100,00 in monatlichen Raten von EUR 3.500,00 ab Rechtskraft; im Uebrigen verzichtet die Klaegerin auf den Restbetrag.",
  "Die Kosten werden im Verhaeltnis 40 (Klaegerin) zu 60 (Beklagter) verteilt.",
  "Hannover, 20.01.2027\nVorsitzender Richter am Landgericht Dr. Falko Brammer"]),

("25_deckungsanfrage_do_versicherer_abschluss.docx", KOPF_DO,
 "Deckungsentscheidung",
 [
  "An Herrn Rechtsanwalt Dr. Cornelius Lohgerber",
  "Nach Pruefung des Teilanerkenntnisurteils und Vergleichs vom 20.01.2027 gewaehrt die Hannoversche Kaution und Industrie Versicherung AG anteilige Deckung fuer den vergleichsweise geregelten Betrag von EUR 420.000,00, soweit er auf allgemeine Fortfuehrungszahlungen entfaellt.",
  "Fuer den anerkannten Betrag von EUR 48.000,00 (Zahlungen an die Ohlendorf Beteiligungs-UG) wird Deckung unter Verweis auf den Ausschluss wissentlicher Pflichtverletzungen gemaess Ziffer 5.3 der Versicherungsbedingungen abgelehnt, da es sich um eine bewusste Zahlung ohne nachgewiesene Gegenleistung an die Alleingesellschafterin handelte.",
  "Rechtsabteilung, i. A. Dr. Konrad Ellermann"]),
]

for fname, kopf, titel, absaetze in docs:
    make_docx(D / fname, kopf, titel, absaetze)

print(f"Erzeugt: {len(docs)} Aktenstuecke fuer {SLUG}")
