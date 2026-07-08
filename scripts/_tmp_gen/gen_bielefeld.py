#!/usr/bin/env python3
"""Ausbau insolvenzanfechtung-kongruente-deckung-lieferant-mahnlauf-bielefeld auf >=25 Aktenstuecke."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from aktenbau import make_docx, TESTAKTEN

SLUG = "insolvenzanfechtung-kongruente-deckung-lieferant-mahnlauf-bielefeld"
D = TESTAKTEN / SLUG

KOPF_IV = "Rechtsanwaeltin Dr. Friederike Sanftleben – Insolvenzverwalterin\nBueltmannshof 12, 33602 Bielefeld"
KOPF_BROSCHEIT = "Broscheit & Weyland Rechtsanwaelte PartG mbB\nFriedrichstrasse 8, 42551 Velbert"
KOPF_GERICHT = "Landgericht Bielefeld – Kammer fuer Handelssachen\nGerichtstrasse 6, 33602 Bielefeld"

docs = [
("14_klageschrift_verwalterin_lg_bielefeld.docx", KOPF_IV,
 "Klageschrift",
 [
  "Landgericht Bielefeld\nKammer fuer Handelssachen\nGerichtstrasse 6, 33602 Bielefeld",
  "In dem Rechtsstreit\n\nRechtsanwaeltin Dr. Friederike Sanftleben, als Insolvenzverwalterin ueber das Vermoegen der Teutoburger Moebelwerk GmbH, Eckendorfer Strasse 145, 33609 Bielefeld\n– Klaegerin –\n\ngegen\n\nHebeFix Beschlagtechnik GmbH, vertreten durch die Geschaeftsfuehrerin Petra Stollberg, Poststrasse 12, 42551 Velbert\n– Beklagte –",
  "wird namens und im Auftrag der Klaegerin Klage erhoben mit dem Antrag,\n\ndie Beklagte zu verurteilen, an die Klaegerin EUR 87.400,00 nebst Zinsen in Hoehe von 5 Prozentpunkten ueber dem Basiszinssatz seit Rechtshaengigkeit zu zahlen.",
  "Begruendung:\n\nDie Beklagte erhielt von der spaeteren Schuldnerin am 01.12.2025, 19.12.2025 und 09.01.2026 Zahlungen ueber insgesamt EUR 87.400,00 auf faellige Forderungen aus der laufenden Belieferung mit Beschlagtechnik. Die Zahlungen sind kongrunet im Sinne des Paragraf 130 Absatz 1 InsO.",
  "Die Beklagte kannte die Zahlungsunfaehigkeit der Schuldnerin im Zeitpunkt der Zahlungen. Dies ergibt sich aus dem dreistufigen Mahnlauf (02.10., 03.11., 24.11.2025), zwei Lastschriftrueckgaben mangels Deckung vom 08.10. und 22.10.2025, der E-Mail des Geschaeftsfuehrers der Schuldnerin vom 26.11.2025 ('wir koennen derzeit nur zahlen, wenn Sie liefern, sonst stehen die Baender still'), der Ratenzahlungsbitte vom 02.12.2025 sowie dem internen Vermerk des Vertriebsleiters der Beklagten vom 05.12.2025 ('Bonitaet rot, nur noch gegen Vorkasse?').",
  "Die Zahlungsunfaehigkeit der Schuldnerin bestand bereits ab dem 12.10.2025, wie sich aus der BWA-Reihe 2025 und der OPOS-Liste zum 30.11.2025 ergibt.",
  "Ein Anlagenverzeichnis ist beigefuegt (Anlagen K1 bis K9, entsprechend Aktenstuecke 04 bis 12).",
  "Dr. Friederike Sanftleben\nRechtsanwaeltin, Insolvenzverwalterin"]),

("15_klageerwiderung_ra_broscheit.docx", KOPF_BROSCHEIT,
 "Klageerwiderung",
 [
  "An das Landgericht Bielefeld – Kammer fuer Handelssachen",
  "In dem Rechtsstreit Dr. Sanftleben ./. HebeFix Beschlagtechnik GmbH, Az. 12 O 47/26",
  "beantragen wir namens und im Auftrag der Beklagten,\n\ndie Klage abzuweisen.",
  "Begruendung:\n\nDie Beklagte bestreitet, im Zeitpunkt der drei streitgegenstaendlichen Zahlungen positive Kenntnis von der Zahlungsunfaehigkeit der Schuldnerin gehabt zu haben. Die von der Klaegerin angefuehrten Indizien lassen jeweils auch eine andere Deutung zu und sind teilweise durch Aktenstuecke widerlegt, die die Klaegerin nicht vorgelegt hat.",
  "Insbesondere die Ratenzahlungsbitte vom 02.12.2025 bezog sich nach dem eigenen Vortrag der Schuldnerin auf eine kurzfristige Verzoegerung wegen eines Grossauftrags (Anlage B1, Aktenstueck 09), nicht auf eine dauerhafte Zahlungsunfaehigkeit. Zudem zahlte die Schuldnerin zwei Zwischenrechnungen vor Faelligkeit, was gegen eine erkennbare Zahlungseinstellung spricht.",
  "Der interne Vermerk des Vertriebsleiters vom 05.12.2025 war eine unverbindliche Frage, die von der Geschaeftsfuehrung der Beklagten mit Verweis auf den Pressebericht ueber den Arkadia-Grossauftrag vom 21.11.2025 ausdruecklich verworfen wurde (Aktenstueck 08, Nachtrag).",
  "Die von der Klaegerin vorgelegte BWA-Reihe datiert die Zahlungsunfaehigkeit abweichend vom Anfechtungsschreiben selbst; die Klaegerin traegt widerspruechlich vor.",
  "Dr. Yannick Broscheit\nRechtsanwalt"]),

("16_duplik_verwalterin.docx", KOPF_IV,
 "Duplik der Klaegerin",
 [
  "An das Landgericht Bielefeld – Az. 12 O 47/26",
  "In Erwiderung auf die Klageerwiderung vom 14.07.2026 wird ausgefuehrt:",
  "Die Behauptung, die Ratenzahlungsbitte habe sich nur auf eine kurzfristige Verzoegerung bezogen, steht im Widerspruch zum Wortlaut des Schreibens vom 02.12.2025, in dem die Schuldnerin selbst von einem 'seit dem Spaetsommer andauernden Liquiditaetsengpass' spricht (Aktenstueck 07). Dies ist keine kurzfristige Verzoegerung, sondern die Beschreibung einer strukturellen Krise.",
  "Die zwei vor Faelligkeit bezahlten Zwischenrechnungen aendern nichts an der Gesamtwuerdigung: Zahlungsunfaehigkeit schliesst einzelne fristgerechte Zahlungen nicht aus (BGH-Rechtsprechung zur Gesamtschau, live zu verifizieren).",
  "Die Klaegerin haelt an ihrem Vortrag zur Kenntnis der Beklagten in vollem Umfang fest und beantragt ergaenzend die Vernehmung des Vertriebsleiters Ralf Kaczmarek als Zeugen zum internen Vermerk vom 05.12.2025.",
  "Dr. Friederike Sanftleben\nRechtsanwaeltin"]),

("17_triplik_ra_broscheit.docx", KOPF_BROSCHEIT,
 "Triplik der Beklagten",
 [
  "An das Landgericht Bielefeld – Az. 12 O 47/26",
  "Die Beklagte haelt an ihrem Vortrag fest. Ergaenzend wird auf die im Aktenstueck 09 dokumentierte Berichterstattung ueber den Arkadia-Hotelauftrag verwiesen, welche der Geschaeftsleitung der Beklagten am 21.11.2025, also noch vor der letzten Zahlung, bekannt war und aus Sicht der Beklagten die wirtschaftliche Erholung der Schuldnerin plausibel erscheinen liess.",
  "Der von der Klaegerin benannte Zeuge Kaczmarek wird bestaetigen, dass sein Vermerk vom 05.12.2025 eine unverbindliche Nachfrage ohne tatsaechliche Grundlage war und von der Geschaeftsfuehrung nicht aufgegriffen wurde.",
  "Die Beklagte beantragt hilfsweise die Einholung eines Sachverstaendigengutachtens zur Frage des Eintritts der Zahlungsunfaehigkeit anhand der BWA-Reihe und der OPOS-Liste.",
  "Dr. Yannick Broscheit\nRechtsanwalt"]),

("18_beweisbeschluss_lg_bielefeld.docx", KOPF_GERICHT,
 "Beweisbeschluss",
 [
  "Az. 12 O 47/26",
  "In dem Rechtsstreit Dr. Sanftleben ./. HebeFix Beschlagtechnik GmbH wird beschlossen:",
  "1. Es wird Beweis erhoben durch Vernehmung des Zeugen Ralf Kaczmarek (Vertriebsleiter der Beklagten) zu der Behauptung, der interne Vermerk vom 05.12.2025 sei eine unverbindliche Nachfrage ohne tatsaechliche Grundlage gewesen.",
  "2. Es wird Beweis erhoben durch Einholung eines schriftlichen Sachverstaendigengutachtens zu der Frage, ob und ab welchem Zeitpunkt die Teutoburger Moebelwerk GmbH im Zeitraum Oktober 2025 bis Januar 2026 zahlungsunfaehig im Sinne des Paragraf 17 InsO war.",
  "3. Zum Sachverstaendigen wird bestellt: Diplom-Kaufmann Herbert Wruck, oeffentlich bestellter und vereidigter Sachverstaendiger fuer Unternehmensbewertung und Insolvenzen, Bielefeld.",
  "Bielefeld, 28.07.2026\nVorsitzender Richter am Landgericht Dr. Anselm Pietrzak"]),

("19_zeugenvernehmungsprotokoll_kaczmarek.docx", KOPF_GERICHT,
 "Protokoll der Zeugenvernehmung",
 [
  "Termin zur Beweisaufnahme vom 15.09.2026, Az. 12 O 47/26",
  "Zeuge: Ralf Kaczmarek, Vertriebsleiter der HebeFix Beschlagtechnik GmbH",
  "Der Zeuge gibt an: 'Ich habe den Vermerk am 05.12.2025 nach einem Kundentermin geschrieben, weil ich unsicher war. Frau Stollberg hat mir am selben Tag noch gesagt, dass wir wegen des Arkadia-Auftrags weiterliefern sollen. Ich hatte keine konkreten Anhaltspunkte fuer eine Insolvenz, nur ein ungutes Gefuehl wegen der Mahnungen.'",
  "Auf Nachfrage der Klaegervertreterin: 'Ja, mir war der Mahnlauf bekannt, das ist bei Kunden mit Zahlungsverzoegerungen aber nicht ungewoehnlich.'",
  "Auf Nachfrage des Beklagtenvertreters: 'Der Pressebericht ueber den Grossauftrag war fuer uns intern schon ein wichtiges Signal, dass es wieder aufwaerts geht.'",
  "Protokollfuehrerin: Justizangestellte S. Rohleder"]),

("20_sachverstaendigengutachten_wruck_zahlungsunfaehigkeit.docx", "Dipl.-Kfm. Herbert Wruck\nOeffentlich bestellter Sachverstaendiger, Bielefeld",
 "Schriftliches Sachverstaendigengutachten",
 [
  "Gutachten zur Frage des Eintritts der Zahlungsunfaehigkeit der Teutoburger Moebelwerk GmbH, erstattet im Auftrag des Landgerichts Bielefeld, Az. 12 O 47/26",
  "1. Grundlage: BWA-Reihe Januar bis Dezember 2025 (Aktenstueck 10), OPOS-Liste zum 30.11.2025 (Aktenstueck 11), Kontoauszuege der HebeFix Beschlagtechnik GmbH (Aktenstueck 12).",
  "2. Methodik: Ermittlung der Liquiditaetsluecke nach der IDW-S-11-Methodik anhand der monatlichen Deckungsquoten aus der BWA-Reihe.",
  "3. Befund: Die Liquiditaetsluecke uebersteigt bereits zum Stichtag 30.09.2025 die Zehn-Prozent-Schwelle des Paragraf 17 InsO und bleibt in den Folgemonaten oberhalb dieser Schwelle. Eine Beseitigung der Luecke innerhalb von drei Wochen war ab diesem Zeitpunkt nicht mehr zu erwarten.",
  "4. Ergebnis: Zahlungsunfaehigkeit trat nach den vorgelegten Unterlagen bereits zum 30.09.2025 ein, mithin vor dem im Anfechtungsschreiben genannten 12.10.2025 und erst recht vor den drei streitgegenstaendlichen Zahlungen.",
  "Bielefeld, 10.11.2026\nDipl.-Kfm. Herbert Wruck"]),

("21_stellungnahme_beklagte_zum_gutachten.docx", KOPF_BROSCHEIT,
 "Stellungnahme zum Sachverstaendigengutachten",
 [
  "An das Landgericht Bielefeld – Az. 12 O 47/26",
  "Die Beklagte nimmt zum Gutachten des Sachverstaendigen Wruck vom 10.11.2026 wie folgt Stellung:",
  "Das Gutachten bestaetigt den objektiven Eintritt der Zahlungsunfaehigkeit zum 30.09.2025. Fuer die Kenntnis der Beklagten im Sinne des Paragraf 130 Absatz 2 InsO ist damit jedoch nichts gewonnen, da die Beklagte keinen Einblick in die BWA-Reihe oder die OPOS-Liste der Schuldnerin hatte und auch nicht haben musste.",
  "Die Beklagte regt an, angesichts des nunmehr feststehenden objektiven Befundes und der verbleibenden Unsicherheit zur subjektiven Kenntnis eine vergleichsweise Erledigung zu pruefen.",
  "Dr. Yannick Broscheit\nRechtsanwalt"]),

("22_vergleichsvorschlag_massekostenverzicht.docx", KOPF_IV,
 "Vergleichsvorschlag",
 [
  "An das Landgericht Bielefeld – Az. 12 O 47/26, nachrichtlich an die Beklagtenvertretung",
  "Die Klaegerin unterbreitet folgenden Vergleichsvorschlag:",
  "1. Die Beklagte zahlt an die Insolvenzmasse EUR 55.000,00 in zwei Raten (30.12.2026 und 28.02.2027).",
  "2. Die Klaegerin verzichtet auf die Geltendmachung des Restbetrags von EUR 32.400,00 sowie auf Zinsen.",
  "3. Die Kosten des Rechtsstreits werden gegeneinander aufgehoben.",
  "4. Mit vollstaendiger Zahlung sind saemtliche Anspruche aus dem streitgegenstaendlichen Sachverhalt erledigt.",
  "Begruendung: Angesichts der nach dem Sachverstaendigengutachten verbleibenden Unsicherheit zur subjektiven Kenntnis der Beklagten und der damit verbundenen Prozessrisiken erscheint eine vergleichsweise Erledigung im Interesse der Masse sachgerecht.",
  "Dr. Friederike Sanftleben\nRechtsanwaeltin"]),

("23_vergleichsannahme_beklagte.docx", KOPF_BROSCHEIT,
 "Annahme des Vergleichsvorschlags",
 [
  "An das Landgericht Bielefeld – Az. 12 O 47/26",
  "Die Beklagte nimmt den Vergleichsvorschlag der Klaegerin vom 20.11.2026 in vollem Umfang an.",
  "Wir bitten um gerichtliche Feststellung des Vergleichs gemaess Paragraf 278 Absatz 6 ZPO im schriftlichen Verfahren.",
  "Dr. Yannick Broscheit\nRechtsanwalt"]),

("24_gerichtlicher_feststellungsbeschluss_vergleich.docx", KOPF_GERICHT,
 "Beschluss ueber das Zustandekommen und den Inhalt des Vergleichs",
 [
  "Az. 12 O 47/26",
  "Das Gericht stellt gemaess Paragraf 278 Absatz 6 ZPO fest, dass zwischen den Parteien folgender Vergleich zustande gekommen ist:",
  "1. Die Beklagte zahlt an die Klaegerin EUR 55.000,00 in zwei Raten (30.12.2026 und 28.02.2027).",
  "2. Im Uebrigen verzichtet die Klaegerin auf weitergehende Anspruche aus dem streitgegenstaendlichen Sachverhalt.",
  "3. Die Kosten des Rechtsstreits werden gegeneinander aufgehoben.",
  "Streitwert: EUR 87.400,00",
  "Bielefeld, 05.12.2026\nVorsitzender Richter am Landgericht Dr. Anselm Pietrzak"]),

("25_kostenfestsetzungsantrag_beklagte.docx", KOPF_BROSCHEIT,
 "Kostenfestsetzungsantrag",
 [
  "An das Landgericht Bielefeld – Az. 12 O 47/26",
  "Namens der Beklagten wird beantragt, die von der Klaegerin gemaess Vergleich vom 05.12.2026 zu erstattenden aussergerichtlichen Kosten der Beklagten in Hoehe von EUR 6.847,50 festzusetzen.",
  "Kostenaufstellung: 1,3 Verfahrensgebuehr, 1,2 Terminsgebuehr, Auslagenpauschale, Umsatzsteuer, jeweils nach einem hälftig geteilten Streitwert entsprechend der Kostenaufhebung.",
  "Dr. Yannick Broscheit\nRechtsanwalt"]),
]

for fname, kopf, titel, absaetze in docs:
    make_docx(D / fname, kopf, titel, absaetze)

print(f"Erzeugt: {len(docs)} Aktenstuecke fuer {SLUG}")
