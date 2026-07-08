#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Erzeugt/ueberarbeitet Aktenstuecke fuer die Erlangen-Akte
(statusfeststellung-gmbh-geschaeftsfuehrer-minderheit-erlangen).
Kein Teil des Produktiv-Repos - Bauskript fuer diese Session.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from docx_helper import (
    new_document, add_title, add_h2, add_h3, add_p, add_letterhead,
    add_table, add_formathinweis, save,
)

ROOT = Path("/home/user/workspace/legal-work/target/testakten/statusfeststellung-gmbh-geschaeftsfuehrer-minderheit-erlangen")

KANZLEI = [
    "Kanzlei Rehbogen und Kollegen, Fachanwaelte fuer Sozialrecht und Gesellschaftsrecht",
    "Rathausplatz 4, 91054 Erlangen",
    "Telefon 09131 88 40 21 - Telefax 09131 88 40 29",
    "USt-IdNr. DE 274 615 903 - RA-Kennnummer 41 883 2",
    "Bearbeiter: Rechtsanwalt und Rentenberater Dr. Fabian Rehbogen",
]

# ---------------------------------------------------------------------------
# 10 Handelsregisterauszug HRB
# ---------------------------------------------------------------------------

def doc_10_handelsregister():
    doc = new_document()
    add_title(doc, "Handelsregisterauszug")
    add_p(doc, "Amtsgericht Fuerth, Abteilung B, HRB 18442", bold=True)
    add_p(doc, "Abrufdatum: 03.02.2026, Abruf durch Kanzlei Rehbogen und Kollegen ueber das gemeinsame Registerportal der Laender.")
    add_h2(doc, "1 Firma und Sitz")
    add_p(doc, "1.1 Firma: Neuralis MedTech GmbH.")
    add_p(doc, "1.2 Sitz: Erlangen. Geschaeftsanschrift: Henkestrasse 91, 91054 Erlangen.")
    add_p(doc, "1.3 Gegenstand: Entwicklung, klinische Erprobung, Zulassung und Vertrieb von Medizinprodukten der Neurotechnologie sowie zugehoerige Softwareentwicklung.")
    add_h2(doc, "2 Stammkapital")
    add_p(doc, "2.1 Stammkapital: 100000,00 EUR.")
    add_h2(doc, "3 Geschaeftsfuehrung, lfd. Eintragungen")
    add_table(doc, ["Lfd. Nr.", "Datum", "Eintragung"], [
        [1, "14.11.2019", "Ersteintragung. Geschaeftsfuehrer: Dr. Henrik Vogt, einzelvertretungsberechtigt, befreit von den Beschraenkungen des Paragraf 181 BGB."],
        [2, "22.05.2021", "Kapitalerhoehung auf 100000,00 EUR nach Eintritt der FrankenHealth Ventures GmbH und der Frau Dr. Miriam Seidl."],
        [3, "06.03.2023", "Neufassung des Gesellschaftsvertrags aufgrund Beschlusses vom 24.02.2023, Urkunde des Notars Dr. Alfons Reinboth, Urkundenrolle Nr. 214/2023."],
        [4, "19.09.2025", "Neufassung Paragraf 6 und Paragraf 9 des Gesellschaftsvertrags (Sperrminoritaet, Vinkulierung) aufgrund Beschlusses vom 02.09.2025, Urkunde des Notars Dr. Alfons Reinboth, Urkundenrolle Nr. 501/2025."],
    ])
    add_h2(doc, "4 Gesellschafter laut zuletzt eingereichter Liste")
    add_table(doc, ["Gesellschafter", "Geschaeftsanteil Nr.", "Nennbetrag EUR", "Anteil Prozent"], [
        ["FrankenHealth Ventures GmbH, Muenchen", 1, "51000,00", "51"],
        ["Dr. Henrik Vogt, Erlangen", 2, "32000,00", "32"],
        ["Dr. Miriam Seidl, Nuernberg", 3, "17000,00", "17"],
    ])
    add_h2(doc, "5 Vertretungsbefugnis, aktueller Stand")
    add_p(doc, "Dr. Henrik Vogt ist einzelvertretungsberechtigter Geschaeftsfuehrer, befreit von den Beschraenkungen des Paragraf 181 BGB. Ein Prokurist ist nicht bestellt.")
    add_formathinweis(doc)
    save(doc, ROOT / "10_handelsregisterauszug_hrb.docx")


def doc_11_gesellschafterliste():
    doc = new_document()
    add_title(doc, "Gesellschafterliste, aktuelle und historische Fassung")
    add_h2(doc, "1 Aktuelle Gesellschafterliste, eingereicht am 19.09.2025")
    add_table(doc, ["Lfd. Nr.", "Gesellschafter", "Geburtsdatum/Sitz", "Nennbetrag EUR", "Anteil Prozent"], [
        [1, "FrankenHealth Ventures GmbH", "Muenchen, HRB 234981", "51000,00", "51"],
        [2, "Dr. Henrik Vogt", "geboren 11.04.1979, Erlangen", "32000,00", "32"],
        [3, "Dr. Miriam Seidl", "geboren 02.09.1981, Nuernberg", "17000,00", "17"],
    ])
    add_h2(doc, "2 Historische Gesellschafterliste, Stand Gruendung 14.11.2019")
    add_table(doc, ["Lfd. Nr.", "Gesellschafter", "Nennbetrag EUR", "Anteil Prozent"], [
        [1, "Dr. Henrik Vogt", "25000,00", "100"],
    ])
    add_p(doc, "Anmerkung zur Entwicklung: Dr. Vogt gruendete die Gesellschaft 2019 als Alleingesellschafter. Mit der Kapitalerhoehung vom 22.05.2021 traten die FrankenHealth Ventures GmbH und Frau Dr. Seidl gegen Bareinlage ein. Dr. Vogts Anteil sank rechnerisch von 100 Prozent auf 32 Prozent, ohne dass sich an der taeglichen Geschaeftsfuehrung zunaechst etwas aenderte.")
    add_h2(doc, "3 Veraenderungen seit Gruendung")
    add_table(doc, ["Datum", "Vorgang"], [
        ["14.11.2019", "Gruendung, Alleingesellschafter Dr. Vogt, Stammkapital 25000,00 EUR"],
        ["22.05.2021", "Kapitalerhoehung auf 100000,00 EUR, Eintritt FrankenHealth Ventures GmbH (51 Prozent) und Dr. Seidl (17 Prozent)"],
        ["06.03.2023", "Neufassung Gesellschaftsvertrag, Einfuehrung Beirat"],
        ["19.09.2025", "Nachtrag Sperrminoritaet und Vinkulierung nach Gesellschafterstreit"],
    ])
    add_formathinweis(doc)
    save(doc, ROOT / "11_gesellschafterliste_aktuell_und_historisch.docx")


def doc_12_notarurkunde_2023():
    doc = new_document()
    add_title(doc, "Notarielle Urkunde, Gesellschafterbeschluss vom 24.02.2023")
    add_p(doc, "Urkundenrolle Nr. 214/2023 des Notars Dr. Alfons Reinboth, Erlangen")
    add_p(doc, "Verhandelt in Erlangen am 24.02.2023. Vor mir, dem unterzeichnenden Notar, erschienen die Gesellschafter der Neuralis MedTech GmbH, vertreten wie im Beurkundungsprotokoll ausgewiesen, und erklaerten einstimmig folgenden Beschluss:")
    add_h2(doc, "1 Gegenstand des Beschlusses")
    add_p(doc, "1.1 Der Gesellschaftsvertrag der Neuralis MedTech GmbH vom 22.05.2021 wird in der als Anlage beigefuegten Fassung vollstaendig neu gefasst.")
    add_p(doc, "1.2 Wesentliche Aenderungen gegenueber der Vorfassung sind die Einfuehrung eines dreikoepfigen Beirats mit Zustimmungsvorbehalten nach Paragraf 7 der Neufassung, die Anpassung der Mehrheitserfordernisse in Paragraf 6 und die Neufassung der Regeln zur Geschaeftsfuehrung in Paragraf 4.")
    add_h2(doc, "2 Abstimmungsergebnis")
    add_p(doc, "Die FrankenHealth Ventures GmbH stimmte mit 51 Stimmen dafuer. Dr. Henrik Vogt stimmte mit 32 Stimmen dafuer. Dr. Miriam Seidl stimmte mit 17 Stimmen dafuer. Der Beschluss wurde einstimmig gefasst.")
    add_h2(doc, "3 Hintergrund laut Erklaerung der Beteiligten")
    add_p(doc, "Die Beteiligten erklaerten zu Protokoll, dass nach dem Einstieg der FrankenHealth Ventures GmbH im Jahr 2021 eine formalisierte Beiratsstruktur eingerichtet werden solle, um die operative Steuerung von Dr. Vogt und die finanzielle Aufsicht des Fonds klar zu trennen. Dr. Vogt erklaerte, er lege Wert darauf, weiterhin einzelvertretungsberechtigter Geschaeftsfuehrer mit Befreiung von Paragraf 181 BGB zu bleiben.")
    add_h2(doc, "4 Registrierung")
    add_p(doc, "Der Notar wurde beauftragt, die Neufassung zur Eintragung beim Handelsregister des Amtsgerichts Fuerth einzureichen. Die Eintragung erfolgte am 06.03.2023 unter HRB 18442.")
    add_p(doc, "Vorstehende Niederschrift wurde den Erschienenen vom Notar vorgelesen, von ihnen genehmigt und eigenhaendig unterschrieben.")
    add_p(doc, "Erlangen, den 24.02.2023 - Dr. Alfons Reinboth, Notar")
    add_formathinweis(doc)
    save(doc, ROOT / "12_notarurkunde_satzungsneufassung_2023.docx")


def doc_13_notarurkunde_2025():
    doc = new_document()
    add_title(doc, "Notarielle Urkunde, Gesellschafterbeschluss vom 02.09.2025")
    add_p(doc, "Urkundenrolle Nr. 501/2025 des Notars Dr. Alfons Reinboth, Erlangen")
    add_p(doc, "Verhandelt in Erlangen am 02.09.2025. Vor mir erschienen die Gesellschafter der Neuralis MedTech GmbH und erklaerten folgenden Beschluss:")
    add_h2(doc, "1 Vorgeschichte")
    add_p(doc, "Im Fruehjahr 2025 kam es zwischen der FrankenHealth Ventures GmbH und Dr. Henrik Vogt zum Streit ueber die Verschiebung der zweiten klinischen Studie und ueber eine beabsichtigte Lizenzierung der Patentfamilie NLM-4 an einen US-Partner. Dr. Vogt lehnte die Lizenzierung ab und drohte im Gesellschafterkreis mit Ruecktritt als Geschaeftsfuehrer, falls seine Sperrposition nicht satzungsfest werde. Die Beteiligten einigten sich in der Folge auf die nachstehende Satzungsaenderung als Kompromiss.")
    add_h2(doc, "2 Beschlossene Aenderungen")
    add_p(doc, "2.1 Paragraf 6.2 des Gesellschaftsvertrags wird um folgende Nummer 6.2.9 ergaenzt: Der Lizenzierung, Uebertragung oder ausschliesslichen Nutzungsueberlassung von Patenten der Patentfamilie NLM-4 an Dritte ausserhalb der Europaeischen Union beduerfen einer Mehrheit von mindestens neunzig Prozent der abgegebenen Stimmen.")
    add_p(doc, "2.2 Paragraf 6 des Gesellschaftsvertrags wird um folgenden Absatz 6.5 ergaenzt: Solange Dr. Henrik Vogt Geschaeftsfuehrer und Gesellschafter mit einem Anteil von mindestens fuenfundzwanzig Prozent ist, bedarf jede Aenderung seines Ressorts Entwicklung, regulatorische Zulassung und klinische Kooperationen sowie jede Weisung, die eine laufende klinische Studie unmittelbar unterbricht, seiner Zustimmung. Diese Zustimmung gilt als Sperrminoritaet im operativen Bereich und laesst die Weisungsbefugnis der Gesellschafterversammlung im Uebrigen unberuehrt.")
    add_p(doc, "2.3 Paragraf 9.1 des Gesellschaftsvertrags wird dahin geaendert, dass die Abtretung von Geschaeftsanteilen an gesellschaftsfremde Dritte zusaetzlich der Zustimmung des jeweils betroffenen Mitgesellschafters bedarf, dessen Anteil mindestens siebzehn Prozent betraegt (Vinkulierung zugunsten Dr. Seidl und Dr. Vogt).")
    add_h2(doc, "3 Abstimmungsergebnis")
    add_p(doc, "Die FrankenHealth Ventures GmbH stimmte mit 51 Stimmen dafuer. Dr. Henrik Vogt stimmte mit 32 Stimmen dafuer. Dr. Miriam Seidl stimmte mit 17 Stimmen dafuer. Der Beschluss wurde einstimmig gefasst und ist noch nicht im Handelsregister bekanntgemacht, jedoch bereits eingetragen.")
    add_h2(doc, "4 Erklaerung der FrankenHealth Ventures GmbH zu Protokoll")
    add_p(doc, "Der Vertreter der FrankenHealth Ventures GmbH erklaerte, die Zustimmung erfolge, um Dr. Vogt als Schluesselperson zu halten, nicht um ihm allgemeine Weisungsfreiheit einzuraeumen. Die Aenderung solle auf das Ressort Entwicklung und laufende Studien begrenzt bleiben.")
    add_p(doc, "Erlangen, den 02.09.2025 - Dr. Alfons Reinboth, Notar")
    add_formathinweis(doc)
    save(doc, ROOT / "13_notarurkunde_satzungsaenderung_sperrminoritaet_2025.docx")


def doc_14_gesellschafterbeschluss_abberufung():
    doc = new_document()
    add_title(doc, "Gesellschafterbeschluss, Antrag auf Abberufung")
    add_p(doc, "Ausserordentliche Gesellschafterversammlung der Neuralis MedTech GmbH vom 12.05.2026, Protokoll (Auszug)")
    add_h2(doc, "1 Anwesende")
    add_p(doc, "Fuer die FrankenHealth Ventures GmbH: Herr Torben Aldenhoven, Partner. Dr. Henrik Vogt, persoenlich. Dr. Miriam Seidl, persoenlich.")
    add_h2(doc, "2 Tagesordnungspunkt: Antrag auf Abberufung des Geschaeftsfuehrers Dr. Vogt")
    add_p(doc, "Herr Aldenhoven beantragt namens der FrankenHealth Ventures GmbH die Abberufung von Dr. Vogt als Geschaeftsfuehrer aus wichtigem Grund. Zur Begruendung fuehrt er an, Dr. Vogt habe die vom Beirat beschlossene Verschiebung von zwei Entwicklerstellen im Mai 2026 eigenmaechtig unterlaufen, indem er einen befristeten Werkvertrag mit einem externen Entwickler abschloss, ohne die Zustimmung des Beirats einzuholen.")
    add_p(doc, "Dr. Vogt erwidert, der Werkvertrag falle mit einem Volumen von 42000,00 EUR unter die in Ziffer 5.1 des Geschaeftsfuehrervertrags genannte eigenstaendige Entscheidungsbefugnis bis 50000,00 EUR und sei keine Neueinstellung im Sinne von Ziffer 7.3.2 des Gesellschaftsvertrags.")
    add_h2(doc, "3 Abstimmung")
    add_p(doc, "Ueber die Abberufung aus wichtigem Grund wird abgestimmt. Dr. Vogt ist gemaess Paragraf 6.3 Satz 2 des Gesellschaftsvertrags von der Stimmabgabe zu diesem Punkt ausgeschlossen.")
    add_table(doc, ["Gesellschafter", "Stimmen", "Votum"], [
        ["FrankenHealth Ventures GmbH", 51, "dafuer"],
        ["Dr. Miriam Seidl", 17, "dagegen"],
        ["Dr. Henrik Vogt", 32, "kein Stimmrecht bei diesem Punkt"],
    ])
    add_p(doc, "Ergebnis: 51 Stimmen dafuer, 17 Stimmen dagegen bei 32 Stimmen ohne Stimmrecht. Die nach Paragraf 6.3 erforderliche einfache Mehrheit der abgegebenen Stimmen (ohne den betroffenen Gesellschafter) ist erreicht. Dr. Seidl erklaert, sie halte den wichtigen Grund fuer nicht hinreichend belegt und kuendigt an, den Beschluss gesellschaftsrechtlich pruefen zu lassen.")
    add_h2(doc, "4 Weiteres Vorgehen")
    add_p(doc, "Der Beschluss wird Dr. Vogt am 13.05.2026 zugestellt. Die Frist zur Anfechtung nach Paragraf 6.4 des Gesellschaftsvertrags laeuft einen Monat ab Zugang der Niederschrift. Getrennt zu beurteilen bleibt die Kuendigung des Anstellungsvertrags nach Ziffer 7.3 des Geschaeftsfuehrervertrags.")
    add_formathinweis(doc)
    save(doc, ROOT / "14_gesellschafterbeschluss_abberufungsantrag.docx")

if __name__ == "__main__":
    doc_10_handelsregister()
    doc_11_gesellschafterliste()
    doc_12_notarurkunde_2023()
    doc_13_notarurkunde_2025()
    doc_14_gesellschafterbeschluss_abberufung()
