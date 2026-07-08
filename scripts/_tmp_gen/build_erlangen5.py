#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ersetzt die alte Matrix durch reinen Rohbeleg (ausgefuellter C0032-Bogen ohne
Risikobewertung) und ergaenzt weitere Rohbelege statt Antwort-Matrizen."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from docx_helper import (
    new_document, add_title, add_h2, add_h3, add_p, add_letterhead,
    add_table, add_formathinweis, save,
)

ROOT = Path("/home/user/workspace/legal-work/target/testakten/statusfeststellung-gmbh-geschaeftsfuehrer-minderheit-erlangen")


def doc_05_c0032_ausgefuellt():
    doc = new_document()
    add_title(doc, "Feststellungsbogen C0032, ausgefuellte Fassung")
    add_p(doc, "Deutsche Rentenversicherung Bund - Feststellung des sozialversicherungsrechtlichen Status eines Gesellschafter-Geschaeftsfuehrers")
    add_p(doc, "Ausgefuellt von: Caroline Benkert, CFO Neuralis MedTech GmbH - Datum: 25.08.2023")
    add_h2(doc, "1 Angaben zur Beteiligung")
    add_p(doc, "1.1 Hoehe der Kapitalbeteiligung des Geschaeftsfuehrers am Stammkapital: 32 Prozent.")
    add_p(doc, "1.2 Bestehen gesellschaftsvertragliche Sonderrechte (Vetorecht, Sperrminoritaet)? Zum Zeitpunkt der Antragstellung: Nein. Eine Sperrminoritaet fuer das Ressort Entwicklung wurde erst am 19.09.2025 nachtraeglich eingefuehrt, siehe Nachtragsurkunde.")
    add_p(doc, "1.3 Kann der Geschaeftsfuehrer Beschluesse der Gesellschafterversammlung mit einfacher Mehrheit verhindern? Nein.")
    add_p(doc, "1.4 Kann der Geschaeftsfuehrer Beschluesse mit qualifizierter Mehrheit (75 Prozent) verhindern? Ja, da 25 Prozent zur Verhinderung genuegen und er 32 Prozent haelt.")
    add_h2(doc, "2 Angaben zur Weisungsgebundenheit")
    add_p(doc, "2.1 Unterliegt der Geschaeftsfuehrer einer Geschaeftsordnung mit Zustimmungsvorbehalten? Ja, siehe Gesellschaftsvertrag Paragraf 7.3 (Beirat).")
    add_p(doc, "2.2 Wurden dem Geschaeftsfuehrer seit Vertragsbeginn Weisungen erteilt? Angabe der Gesellschaft: Der Beirat hat am 06.05.2026 die Weisung erteilt, zwei Entwicklerstellen erst nach Finanzierungszusage zu besetzen. Am 14.02.2025 wurde die zweite klinische Studie um drei Monate verschoben.")
    add_p(doc, "2.3 Feste Arbeitszeit vereinbart? Nein, laut Ziffer 2.1 des Anstellungsvertrags.")
    add_p(doc, "2.4 Urlaubsanspruch vertraglich geregelt? Ja, 30 Arbeitstage, Abstimmung mit dem Beiratsvorsitzenden erforderlich (Stand bei Antragstellung 2023, seit Nachtrag 2025 fuer das Ressort Entwicklung nicht mehr erforderlich).")
    add_p(doc, "2.5 Entgeltfortzahlung im Krankheitsfall vertraglich geregelt? Ja, sechs Wochen.")
    add_h2(doc, "3 Angaben zum Unternehmerrisiko")
    add_p(doc, "3.1 Feste oder variable Verguetung? Feste Verguetung 12000 EUR monatlich, variable Verguetung bis 40000 EUR jaehrlich nach Meilensteinen.")
    add_p(doc, "3.2 Wurde die variable Verguetung in der Vergangenheit tatsaechlich in voller Hoehe, teilweise oder gar nicht gezahlt? Angabe der Gesellschaft: 2023 stand aus, 2024 wurden 30000 EUR von moeglichen 40000 EUR gezahlt, 2025 wurde die variable Verguetung auf Beschluss der Gesellschafterversammlung vom 18.07.2024 vollstaendig gestrichen.")
    add_p(doc, "3.3 Hat der Geschaeftsfuehrer Sicherheiten fuer die Gesellschaft uebernommen? Ja, persoenliche Buergschaft gegenueber der Hausbank in Hoehe von 400000 EUR, uebernommen am 03.06.2021 im Zusammenhang mit einem Investitionskredit fuer das Labor.")
    add_p(doc, "3.4 Hat der Geschaeftsfuehrer der Gesellschaft Darlehen gewaehrt? Ja, 60000 EUR im Jahr 2024 zu drei Prozent Zinsen.")
    add_h2(doc, "4 Sonstige Angaben")
    add_p(doc, "4.1 Ist der Geschaeftsfuehrer Mitgruender? Ja, Gruendung 2019 als Alleingesellschafter, Reduzierung auf 32 Prozent im Zuge der Finanzierungsrunde 2021.")
    add_p(doc, "4.2 Verfuegt der Geschaeftsfuehrer ueber technisches Fachwissen, ohne das der Betrieb nicht fortgefuehrt werden koennte? Angabe der Gesellschaft: Herr Dr. Vogt ist alleiniger Erfinder beziehungsweise Miterfinder der Patentfamilie NLM-4.")
    add_p(doc, "Erklaerung: Die Angaben wurden nach bestem Wissen gemacht. Rueckfragen der Clearingstelle sind moeglich.")
    add_formathinweis(doc)
    save(doc, ROOT / "05_c0032_feststellungsbogen_ausgefuellt.docx")


def doc_31_gehaltsabrechnung_auszug():
    doc = new_document()
    add_title(doc, "Gehaltsabrechnungen Dr. Vogt, Auszuege")
    add_p(doc, "Lohnbuero Klett und Partner, Erlangen - Erstellt fuer Unterlagenvorlage im Statusfeststellungsverfahren am 14.01.2026")
    add_h2(doc, "1 Abrechnung Maerz 2023")
    add_p(doc, "Bruttoverguetung 12000,00 EUR. Lohnsteuerklasse III. Abzuege Lohnsteuer und Solidaritaetszuschlag. Keine Abzuege fuer Sozialversicherung (Behandlung als nicht versicherungspflichtiger Gesellschafter-Geschaeftsfuehrer). Auszahlungsbetrag 8140,22 EUR.")
    add_h2(doc, "2 Abrechnung Dezember 2024")
    add_p(doc, "Bruttoverguetung 12000,00 EUR zuzueglich anteiliger variabler Verguetung 2500,00 EUR. Keine Abzuege fuer Sozialversicherung. Auszahlungsbetrag 9870,14 EUR.")
    add_h2(doc, "3 Abrechnung Juni 2026")
    add_p(doc, "Bruttoverguetung 12000,00 EUR. Keine Abzuege fuer Sozialversicherung, Verfahren noch nicht bestandskraeftig abgeschlossen. Vermerk des Lohnbueros: Bei rueckwirkender Feststellung der Versicherungspflicht sind saemtliche Abrechnungen seit Maerz 2023 zu korrigieren.")
    add_h2(doc, "4 Hinweis des Lohnbueros")
    add_p(doc, "Die Korrektur betrifft nach vorlaeufiger Schaetzung 40 Monate. Eine detaillierte Neuberechnung ist erst nach Abschluss des Verfahrens sinnvoll, da Beitragsbemessungsgrenzen jahresbezogen zu beruecksichtigen sind.")
    add_formathinweis(doc)
    save(doc, ROOT / "32_gehaltsabrechnungen_auszuege.docx")


if __name__ == "__main__":
    doc_05_c0032_ausgefuellt()
    doc_31_gehaltsabrechnung_auszug()
