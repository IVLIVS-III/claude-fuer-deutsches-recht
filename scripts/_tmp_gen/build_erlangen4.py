#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from docx_helper import (
    new_document, add_title, add_h2, add_h3, add_p, add_letterhead,
    add_table, add_formathinweis, save,
)

ROOT = Path("/home/user/workspace/legal-work/target/testakten/statusfeststellung-gmbh-geschaeftsfuehrer-minderheit-erlangen")


def doc_27_nachtrag_gf_vertrag():
    doc = new_document()
    add_title(doc, "Nachtrag zum Geschaeftsfuehrer-Anstellungsvertrag")
    add_p(doc, "zwischen der Neuralis MedTech GmbH und Herrn Dr. Henrik Vogt - Nachtrag Nr. 1 vom 25.09.2025")
    add_h2(doc, "1 Anlass")
    add_p(doc, "Im Zusammenhang mit der Satzungsaenderung vom 02.09.2025 (Sperrminoritaet Ressort Entwicklung) passen die Parteien den Anstellungsvertrag vom 27.02.2023 in den nachfolgenden Punkten an.")
    add_h2(doc, "2 Aenderung von Ziffer 2 (Arbeitszeit und Arbeitsort)")
    add_p(doc, "2.1 Ziffer 2.1 wird wie folgt neu gefasst: Der Geschaeftsfuehrer bestimmt Zeit, Dauer und Ort seiner Taetigkeit im Ressort Entwicklung eigenverantwortlich. Eine Kernarbeitszeit oder Anwesenheitspflicht besteht fuer dieses Ressort nicht. Fuer die uebrigen Aufgaben aus Ziffer 1.2 (regulatorische Zulassung, klinische Kooperationen) verbleibt es bei der Ausrichtung an den Erfordernissen der Gesellschaft und den Vorgaben des Beirats.")
    add_h2(doc, "3 Aenderung von Ziffer 4 (Urlaub und Verhinderung)")
    add_p(doc, "3.1 Ziffer 4.1 wird ergaenzt: Fuer das Ressort Entwicklung ist eine Abstimmung der Urlaubslage mit dem Beiratsvorsitzenden nicht erforderlich; der Geschaeftsfuehrer zeigt Abwesenheiten von mehr als fuenf Tagen lediglich zur Information an.")
    add_h2(doc, "4 Klarstellung zur Auslegung")
    add_p(doc, "4.1 Die Parteien stellen klar, dass diese Aenderungen ausschliesslich das Ressort Entwicklung betreffen und die uebrigen Regelungen des Anstellungsvertrags, insbesondere zu Verguetung, Zustimmungsvorbehalten nach Ziffer 5 und Kuendigung nach Ziffer 7, unveraendert fortgelten.")
    add_p(doc, "4.2 Der Beiratsvorsitzende weist bei Unterzeichnung darauf hin, dass diese Anpassung dem Statusfeststellungsverfahren Rechnung tragen, jedoch keine rueckwirkende Wirkung entfalten solle.")
    add_p(doc, "Erlangen, den 25.09.2025 - Fuer die Gesellschaft: Prof. Dr. Cornelius Baumhauer, Beiratsvorsitzender - Der Geschaeftsfuehrer: Dr. Henrik Vogt")
    add_formathinweis(doc)
    save(doc, ROOT / "27_nachtrag_geschaeftsfuehrervertrag_2025.docx")


def doc_28_protokoll_strittige_versammlung():
    doc = new_document()
    add_title(doc, "Protokoll der Gesellschafterversammlung vom 02.09.2025")
    add_p(doc, "Neuralis MedTech GmbH - außerordentliche Versammlung, Beginn 14:00 Uhr, Ende 17:40 Uhr, Notariat Dr. Reinboth")
    add_h2(doc, "1 Anwesende")
    add_p(doc, "Torben Aldenhoven fuer FrankenHealth Ventures GmbH (51 Stimmen), Dr. Henrik Vogt (32 Stimmen), Dr. Miriam Seidl (17 Stimmen). Notar Dr. Alfons Reinboth beurkundend zugegen.")
    add_h2(doc, "2 Verlauf der Diskussion")
    add_p(doc, "Herr Aldenhoven eroeffnet mit dem Hinweis, der Fonds sei nur bereit, Dr. Vogt eine Sperrminoritaet einzuraeumen, wenn diese strikt auf das Ressort Entwicklung begrenzt bleibe. Dr. Vogt fordert zunaechst eine Sperrminoritaet fuer alle strategischen Entscheidungen einschliesslich Finanzierungsrunden. Nach laengerer Diskussion und einer Sitzungsunterbrechung von 45 Minuten einigt man sich auf die enger gefasste Fassung.")
    add_p(doc, "Dr. Seidl aeussert Bedenken, dass eine zu enge Fassung im laufenden DRV-Verfahren wenig hilfreich sei, stimmt aber letztlich mit den anderen fuer die vorgeschlagene Fassung, um den Konflikt beizulegen.")
    add_h2(doc, "3 Abstimmung ueber die Satzungsaenderung")
    add_table(doc, ["Gesellschafter", "Stimmen", "Votum"], [
        ["FrankenHealth Ventures GmbH", 51, "dafuer"],
        ["Dr. Henrik Vogt", 32, "dafuer"],
        ["Dr. Miriam Seidl", 17, "dafuer"],
    ])
    add_p(doc, "Ergebnis: Einstimmig angenommen (100 von 100 Stimmen).")
    add_h2(doc, "4 Sonstiges")
    add_p(doc, "Dr. Vogt bittet um Protokollierung, dass er die Fassung nur als ersten Schritt akzeptiere und im naechsten Jahr eine Ausweitung verlangen werde. Der Vorsitzende nimmt dies zur Kenntnis, ohne eine Zusage zu machen.")
    add_formathinweis(doc)
    save(doc, ROOT / "28_protokoll_gesellschafterversammlung_2025-09-02.docx")


def doc_29_protokoll_versammlung_2024():
    doc = new_document()
    add_title(doc, "Protokoll der ordentlichen Gesellschafterversammlung vom 18.07.2024")
    add_p(doc, "Neuralis MedTech GmbH - ordentliche Versammlung, Beginn 10:00 Uhr, Ende 12:15 Uhr, Geschaeftsraeume Henkestrasse 91")
    add_h2(doc, "1 Anwesende")
    add_p(doc, "Torben Aldenhoven fuer FrankenHealth Ventures GmbH (51 Stimmen), Dr. Henrik Vogt (32 Stimmen), Dr. Miriam Seidl (17 Stimmen), Prof. Dr. Cornelius Baumhauer als Gast (Beiratsvorsitzender, kein Stimmrecht).")
    add_h2(doc, "2 Tagesordnung")
    add_p(doc, "2.1 Feststellung des Jahresabschlusses 2023.")
    add_p(doc, "2.2 Beschlussfassung ueber die variable Verguetung des Geschaeftsfuehrers fuer 2023.")
    add_p(doc, "2.3 Bericht zum Stand der klinischen Studie und zur Zulassung.")
    add_h2(doc, "3 Beschluesse")
    add_p(doc, "Zu 2.1: Der Jahresabschluss 2023 wird einstimmig festgestellt.")
    add_p(doc, "Zu 2.2: Der Beirat hatte empfohlen, die variable Verguetung wegen verfehlter Meilensteine (CE-Zulassung verzoegert) auf 0 EUR festzusetzen. Nach Diskussion beschliesst die Versammlung mit 68 von 100 Stimmen (FrankenHealth Ventures GmbH dafuer, Dr. Vogt dagegen, Dr. Seidl dafuer), die variable Verguetung fuer 2023 ersatzlos zu streichen. Dr. Vogt haelt dies fuer nicht sachgerecht, da die Verzoegerung auf einer Anforderung der Benannten Stelle beruhe, auf die er keinen Einfluss habe.")
    add_p(doc, "Zu 2.3: Kenntnisnahme ohne Beschluss.")
    add_formathinweis(doc)
    save(doc, ROOT / "29_protokoll_gesellschafterversammlung_2024-07-18.docx")


def doc_30_zeugen_belege():
    doc = new_document()
    add_title(doc, "Zeugenliste und Belegverzeichnis")
    add_h2(doc, "1 Mögliche Zeugen")
    add_table(doc, ["Name", "Rolle", "Beweisthema"], [
        ["Prof. Dr. Cornelius Baumhauer", "Beiratsvorsitzender", "Handhabung der Zustimmungsvorbehalte und der Sperrminoritaet seit 2025"],
        ["Dr. Miriam Seidl", "Mitgesellschafterin, 17 Prozent", "Abstimmungsverhalten, Wahrnehmung der faktischen Machtverhaeltnisse"],
        ["Caroline Benkert", "CFO Neuralis MedTech GmbH", "Umgang mit Weisungen, Zahlungsfluesse, Buergschaft"],
        ["Torben Aldenhoven", "Partner FrankenHealth Ventures GmbH", "Motive fuer die Satzungsaenderung 2025, Beteiligung an Abberufungsantrag"],
    ])
    add_h2(doc, "2 Belegverzeichnis")
    add_table(doc, ["Lfd. Nr.", "Beleg", "Fundstelle"], [
        [1, "Gesellschaftsvertrag Neufassung 2023 und Nachtrag 2025", "Aktenstuecke 02, 12, 13"],
        [2, "Geschaeftsfuehrervertrag und Nachtrag", "Aktenstuecke 03, 27"],
        [3, "Beiratsprotokolle 2025 und 2026", "Aktenstueck 04"],
        [4, "Gesellschafterprotokolle 2024 und 2025", "Aktenstuecke 28, 29"],
        [5, "Buergschaftsbezug", "Aktenstueck 01, Ziffer 3.2"],
        [6, "Beitragsberechnung", "Aktenstueck 31"],
    ])
    add_h2(doc, "3 Offene Lücken")
    add_p(doc, "Die Buergschaftsurkunde selbst liegt der Kanzlei nicht im Original vor, nur der Verweis aus der Mandatsnotiz. Eine Anforderung bei der Hausbank ist offen. Die genaue Zahl der tatsaechlich genommenen Urlaubstage seit 2023 ist nicht dokumentiert und muss ueber die Reisekostenabrechnung rekonstruiert werden.")
    add_formathinweis(doc)
    save(doc, ROOT / "30_zeugen_und_belegverzeichnis.docx")


if __name__ == "__main__":
    doc_27_nachtrag_gf_vertrag()
    doc_28_protokoll_strittige_versammlung()
    doc_29_protokoll_versammlung_2024()
    doc_30_zeugen_belege()
