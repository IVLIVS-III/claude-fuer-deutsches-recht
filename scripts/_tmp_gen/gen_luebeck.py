#!/usr/bin/env python3
"""Ausbau insolvenzanfechtung-kongruente-deckung-krankenkasse-nach-antrag-luebeck auf >=25 Aktenstuecke."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from aktenbau import make_docx, TESTAKTEN

SLUG = "insolvenzanfechtung-kongruente-deckung-krankenkasse-nach-antrag-luebeck"
D = TESTAKTEN / SLUG

KOPF_IV = "Rechtsanwalt Dr. Hauke Petersen – Insolvenzverwalter\nBreite Strasse 6, 23552 Luebeck"
KOPF_KASSE = "BKK Ostseekueste – Rechtsabteilung\nWestring 305, 24118 Kiel"
KOPF_GERICHT = "Landgericht Luebeck – 4. Zivilkammer\nAm Burgfeld 7, 23568 Luebeck"

docs = [
("15_replik_verwalter.docx", KOPF_IV,
 "Replik des Insolvenzverwalters",
 [
  "An die BKK Ostseekueste, Rechtsabteilung, z. Hd. Frau Dr. Wehrmann",
  "Die Erwiderung vom 24.06.2026 vermag nicht zu ueberzeugen. Die Vollstreckungsankuendigung vom 28.01.2026 (Aktenstueck 05) belegt eine positive Kenntnis der Zahlungsunfaehigkeit im Sinne des Paragraf 130 Absatz 2 InsO, da eine oeffentliche Kasse regelmaessig davon ausgehen muss, dass ein Unternehmen, dem die Zwangsvollstreckung angedroht wird und das daraufhin zahlt, zahlungsunfaehig ist.",
  "Der Telefonvermerk des Aussendienstmitarbeiters Kroeger vom 17.02.2026 (Aktenstueck 08) sowie dessen eidesstattliche Versicherung vom 03.06.2026 (Aktenstueck 09) bestaetigen, dass ihm gegenueber offen von Liquiditaetsproblemen gesprochen wurde.",
  "Der Insolvenzverwalter fordert daher unter Fristsetzung bis zum 15.08.2026 zur Rueckzahlung der angefochtenen Betraege in Hoehe von EUR 34.780,00 auf.",
  "Dr. Hauke Petersen\nRechtsanwalt, Insolvenzverwalter"]),

("16_duplik_bkk.docx", KOPF_KASSE,
 "Duplik der BKK Ostseekueste",
 [
  "An Herrn Rechtsanwalt Dr. Hauke Petersen",
  "Die BKK Ostseekueste haelt an ihrer Rechtsauffassung fest. Die Vollstreckungsankuendigung vom 28.01.2026 war ein routinemaessiger Verwaltungsakt, wie er bei jedem Beitragsrueckstand versendet wird, und begruendet fuer sich genommen keine Kenntnis von einer Zahlungsunfaehigkeit im insolvenzrechtlichen Sinne.",
  "Die vom ehemaligen Aussendienstmitarbeiter Kroeger abgegebene eidesstattliche Versicherung wird in ihrer rechtlichen Bedeutung bestritten, da Herr Kroeger zum Zeitpunkt des Telefonats keine Entscheidungsbefugnis in der Kasse hatte und seine Einschaetzung nicht der Kasse zuzurechnen ist.",
  "Eine Rueckzahlung wird daher weiterhin abgelehnt.",
  "Dr. Annegret Wehrmann\nJustiziarin"]),

("17_klageschrift_verwalter_lg_luebeck.docx", KOPF_IV,
 "Klageschrift",
 [
  "Landgericht Luebeck\n4. Zivilkammer\nAm Burgfeld 7, 23568 Luebeck",
  "In dem Rechtsstreit\n\nRechtsanwalt Dr. Hauke Petersen, als Insolvenzverwalter ueber das Vermoegen der Trave Clean Gebaeudeservice GmbH\n– Klaeger –\n\ngegen\n\nBKK Ostseekueste, Koerperschaft des oeffentlichen Rechts, vertreten durch den Vorstand\n– Beklagte –",
  "wird namens und im Auftrag des Klaegers Klage erhoben mit dem Antrag, die Beklagte zu verurteilen, an die Insolvenzmasse EUR 34.780,00 nebst Zinsen zu zahlen.",
  "Begruendung: Die Beklagte erhielt im Dreimonatszeitraum vor dem Fremdantrag vom 09.02.2026 mehrere Zahlungen auf faellige Beitragsforderungen. Die Kenntnis der Zahlungsunfaehigkeit ergibt sich aus der Vollstreckungsankuendigung, dem Telefonvermerk und der eidesstattlichen Versicherung des Zeugen Kroeger.",
  "Dr. Hauke Petersen\nRechtsanwalt, Insolvenzverwalter"]),

("18_klageerwiderung_bkk_lg_luebeck.docx", KOPF_KASSE,
 "Klageerwiderung",
 [
  "An das Landgericht Luebeck – Az. 4 O 91/26",
  "Namens der Beklagten wird beantragt, die Klage abzuweisen. Ergaenzend zum vorprozessualen Vortrag wird bestritten, dass die Vollstreckungsankuendigung eine ueber das uebliche Mass hinausgehende Kenntnis begruendet. Die Beklagte verweist auf die staendige Verwaltungspraxis, wonach Vollstreckungsankuendigungen bereits ab dem ersten Zahlungsverzug automatisiert versendet werden.",
  "Dr. Annegret Wehrmann\nJustiziarin"]),

("19_beweisbeschluss_lg_luebeck.docx", KOPF_GERICHT,
 "Beweisbeschluss",
 [
  "Az. 4 O 91/26",
  "In dem Rechtsstreit Dr. Petersen ./. BKK Ostseekueste wird beschlossen:",
  "1. Es wird Beweis erhoben durch Vernehmung des Zeugen Malte Kroeger zu der Behauptung, im Telefonat vom 17.02.2026 sei ihm gegenueber offen von Liquiditaetsproblemen gesprochen worden.",
  "2. Es wird Beweis erhoben durch Vernehmung der Zeugin Sabine Wohlert (Teamleiterin Beitragseinzug) zu der Behauptung, Vollstreckungsankuendigungen wuerden automatisiert und ohne Einzelfallpruefung versendet.",
  "Luebeck, 20.09.2026\nVorsitzende Richterin am Landgericht Dr. Sonja Timm"]),

("20_zeugenvernehmungsprotokoll_kroeger_wohlert.docx", KOPF_GERICHT,
 "Protokoll der Zeugenvernehmung",
 [
  "Termin vom 12.10.2026, Az. 4 O 91/26",
  "Zeuge Malte Kroeger: 'Der Geschaeftsfuehrer Albayrak hat mir am Telefon gesagt, dass er gerade grosse Probleme hat, alle Rechnungen zu bezahlen, und um Ratenzahlung gebeten. Ich habe das in meinem Vermerk festgehalten und an die Teamleiterin weitergegeben.'",
  "Zeugin Sabine Wohlert: 'Ich habe den Vermerk von Herrn Kroeger erhalten und zur Kenntnis genommen. Die Vollstreckungsankuendigung wurde regulaer nach Ablauf der Zahlungsfrist versendet, aber der Inhalt des Vermerks war uns natuerlich bekannt.'",
  "Protokollfuehrer: Justizangestellter H. Bostelmann"]),

("21_stellungnahme_verwalter_nach_beweisaufnahme.docx", KOPF_IV,
 "Stellungnahme nach Beweisaufnahme",
 [
  "An das Landgericht Luebeck – Az. 4 O 91/26",
  "Die Beweisaufnahme hat bestaetigt, dass der Teamleiterin Wohlert der Inhalt des Telefonvermerks bekannt war, bevor die streitgegenstaendlichen Zahlungen erfolgten. Dies begruendet eine Kenntniszurechnung im Sinne des Paragraf 130 Absatz 1 Satz 1 Nr. 1 InsO.",
  "Der Klaeger haelt an seinem Klageantrag in vollem Umfang fest.",
  "Dr. Hauke Petersen\nRechtsanwalt, Insolvenzverwalter"]),

("22_vergleichsvorschlag_bkk.docx", KOPF_KASSE,
 "Vergleichsvorschlag",
 [
  "An Herrn Rechtsanwalt Dr. Hauke Petersen",
  "Angesichts der Aussage der Zeugin Wohlert schlaegt die Beklagte vor: Zahlung von EUR 22.000,00 an die Insolvenzmasse gegen vollstaendige Erledigung des Rechtsstreits, Kostenteilung im Verhaeltnis 50 zu 50.",
  "Dr. Annegret Wehrmann\nJustiziarin"]),

("23_vergleichsannahme_verwalter.docx", KOPF_IV,
 "Annahme des Vergleichsvorschlags",
 [
  "An die BKK Ostseekueste, z. Hd. Frau Dr. Wehrmann",
  "Der Insolvenzverwalter nimmt den Vergleichsvorschlag vom 25.11.2026 an und bittet um gerichtliche Feststellung gemaess Paragraf 278 Absatz 6 ZPO.",
  "Dr. Hauke Petersen\nRechtsanwalt, Insolvenzverwalter"]),

("24_feststellungsbeschluss_vergleich_luebeck.docx", KOPF_GERICHT,
 "Beschluss ueber das Zustandekommen und den Inhalt des Vergleichs",
 [
  "Az. 4 O 91/26",
  "Das Gericht stellt gemaess Paragraf 278 Absatz 6 ZPO fest, dass zwischen den Parteien folgender Vergleich zustande gekommen ist:",
  "1. Die Beklagte zahlt an die Insolvenzmasse EUR 22.000,00 binnen vier Wochen nach Rechtskraft.",
  "2. Im Uebrigen sind alle wechselseitigen Ansprueche aus dem streitgegenstaendlichen Sachverhalt erledigt.",
  "3. Die Kosten des Rechtsstreits werden gegeneinander aufgehoben.",
  "Luebeck, 10.12.2026\nVorsitzende Richterin am Landgericht Dr. Sonja Timm"]),

("25_schlussvermerk_verwalter_luebeck.docx", KOPF_IV,
 "Aktenvermerk: Abschluss des Anfechtungsverfahrens",
 [
  "Az. 53c IN 21/26, Rechtsstreit 4 O 91/26",
  "Der Vergleichsbetrag von EUR 22.000,00 ist am 15.01.2027 auf dem Massekonto der Trave Clean Gebaeudeservice GmbH i.I. eingegangen. Der Anfechtungsanspruch gegen die BKK Ostseekueste ist damit vollstaendig erledigt.",
  "Dr. Hauke Petersen\nRechtsanwalt, Insolvenzverwalter"]),
]

for fname, kopf, titel, absaetze in docs:
    make_docx(D / fname, kopf, titel, absaetze)

print(f"Erzeugt: {len(docs)} Aktenstuecke fuer {SLUG}")
