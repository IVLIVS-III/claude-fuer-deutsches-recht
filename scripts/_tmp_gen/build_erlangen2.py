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


def doc_15_c0031_antrag():
    doc = new_document()
    add_title(doc, "Antrag auf Statusfeststellung, Formular C0031")
    add_p(doc, "Deutsche Rentenversicherung Bund, Clearingstelle, 10704 Berlin", bold=True)
    add_p(doc, "Eingegangen: 04.09.2023 - Aktenzeichen: SV-2023-771402-VOGT")
    add_h2(doc, "1 Angaben zum Auftraggeber")
    add_table(doc, ["Feld", "Angabe"], [
        ["Firma", "Neuralis MedTech GmbH"],
        ["Anschrift", "Henkestrasse 91, 91054 Erlangen"],
        ["Betriebsnummer", "38714402"],
    ])
    add_h2(doc, "2 Angaben zur Person, ueber deren Status entschieden werden soll")
    add_table(doc, ["Feld", "Angabe"], [
        ["Name", "Dr. Henrik Vogt"],
        ["Geburtsdatum", "11.04.1979"],
        ["Funktion", "Geschaeftsfuehrer"],
        ["Beteiligung am Stammkapital", "32 Prozent"],
        ["Beginn der Taetigkeit als Geschaeftsfuehrer", "14.11.2019, seit 01.03.2023 auf Grundlage des neu gefassten Anstellungsvertrags"],
    ])
    add_h2(doc, "3 Fragen zur Rechtsmacht")
    add_p(doc, "3.1 Verfuegt die Person ueber mindestens 50 Prozent der Stimmrechte? Antwort: Nein, 32 Prozent.")
    add_p(doc, "3.2 Verfuegt die Person ueber eine im Gesellschaftsvertrag verankerte Sperrminoritaet, mit der sie ihr nicht genehme Weisungen verhindern kann? Antwort: Eingeschraenkt, siehe Anlage Gesellschaftsvertrag Paragraf 6.5 (Sperrminoritaet im Ressort Entwicklung, eingefuehrt 2025), nicht umfassend.")
    add_h2(doc, "4 Fragen zur Weisungsgebundenheit")
    add_p(doc, "4.1 Unterliegt die Person einem Zeit-, Orts- und Fachweisungsrecht? Antwort: Kein festes Zeit- und Ortsweisungsrecht laut Anstellungsvertrag Ziffer 2, jedoch Zustimmungsvorbehalte des Beirats nach Gesellschaftsvertrag Paragraf 7.3 und Anstellungsvertrag Ziffer 5.2.")
    add_p(doc, "4.2 Erhaelt die Person Urlaub und Entgeltfortzahlung im Krankheitsfall wie ein Arbeitnehmer? Antwort: Ja, 30 Tage Urlaub und sechs Wochen Entgeltfortzahlung laut Anstellungsvertrag Ziffer 4.")
    add_h2(doc, "5 Fragen zum Unternehmerrisiko")
    add_p(doc, "5.1 Traegt die Person ein Unternehmerrisiko, insbesondere durch Kapitaleinsatz oder Buergschaften? Antwort: Ja, persoenliche Buergschaft ueber 400000,00 EUR gegenueber der Hausbank der Gesellschaft, siehe Anlage Buergschaftsurkunde.")
    add_p(doc, "5.2 Ist die Verguetung erfolgsabhaengig oder gewinnbezogen? Antwort: Feste Verguetung von 12000,00 EUR monatlich, zusaetzlich variable Verguetung bis 40000,00 EUR jaehrlich nach Meilensteinen.")
    add_h2(doc, "6 Erklaerung der Antragstellerin")
    add_p(doc, "Die Neuralis MedTech GmbH erklaert, dass die vorstehenden Angaben nach bestem Wissen vollstaendig und richtig sind. Anlagen: Gesellschaftsvertrag, Geschaeftsfuehrervertrag, Handelsregisterauszug, Buergschaftsurkunde (in Kopie).")
    add_p(doc, "Erlangen, den 01.09.2023 - Fuer die Neuralis MedTech GmbH: Caroline Benkert, CFO")
    add_formathinweis(doc)
    save(doc, ROOT / "15_c0031_statusfeststellungsantrag.docx")


def doc_16_drv_anhoerung():
    doc = new_document()
    add_letterhead(doc, [
        "Deutsche Rentenversicherung Bund",
        "Clearingstelle Sozialversicherungsstatus",
        "Ruhrstrasse 2, 10709 Berlin",
    ])
    add_title(doc, "Anhoerung nach Paragraf 24 SGB X im Statusfeststellungsverfahren")
    add_p(doc, "Aktenzeichen: SV-2023-771402-VOGT - Berlin, den 18.11.2025")
    add_p(doc, "Sehr geehrte Damen und Herren,")
    add_h2(doc, "1 Zwischenergebnis der Pruefung")
    add_p(doc, "nach Auswertung des Gesellschaftsvertrags, des Geschaeftsfuehrervertrags, der Beiratsprotokolle und des Feststellungsbogens C0031/C0032 beabsichtigen wir festzustellen, dass Herr Dr. Henrik Vogt seine Taetigkeit als Geschaeftsfuehrer der Neuralis MedTech GmbH seit dem 01.03.2023 im Rahmen eines abhaengigen, dem Grunde nach sozialversicherungspflichtigen Beschaeftigungsverhaeltnisses ausuebt.")
    add_h2(doc, "2 Tragende Gesichtspunkte")
    add_p(doc, "2.1 Herr Dr. Vogt haelt mit 32 Prozent lediglich einen Minderheitsanteil am Stammkapital der Gesellschaft und kann Beschluesse der Gesellschafterversammlung, die mit einfacher Mehrheit gefasst werden, nicht verhindern.")
    add_p(doc, "2.2 Der Anstellungsvertrag sieht eine feste monatliche Verguetung, einen Urlaubsanspruch von 30 Arbeitstagen und eine Entgeltfortzahlung im Krankheitsfall von sechs Wochen vor. Diese Regelungen entsprechen typischen arbeitsvertraglichen Schutzmechanismen.")
    add_p(doc, "2.3 Der Gesellschaftsvertrag sieht in Paragraf 7 einen Beirat mit eigenen Zustimmungsvorbehalten vor, denen die Geschaeftsfuehrung unterworfen ist, unter anderem bei Investitionen ab 50000,00 EUR und Personalentscheidungen ab Leitungsebene.")
    add_p(doc, "2.4 Die im Jahr 2025 nachtraeglich eingefuehrte Sperrminoritaet in Paragraf 6.5 des Gesellschaftsvertrags beschraenkt sich auf das Ressort Entwicklung und laufende klinische Studien. Sie vermittelt keine umfassende Sperrminoritaet ueber alle wesentlichen Gesellschafterbeschluesse.")
    add_h2(doc, "3 Gesichtspunkte, die fuer Selbstaendigkeit sprechen koennten")
    add_p(doc, "3.1 Herr Dr. Vogt hat eine persoenliche Buergschaft ueber 400000,00 EUR zugunsten der Hausbank der Gesellschaft uebernommen und traegt damit ein Kapitalrisiko, das ueber eine reine Arbeitnehmerstellung hinausgeht.")
    add_p(doc, "3.2 Herr Dr. Vogt ist Mitgruender und alleiniger Inhaber des technischen Kernwissens zur Patentfamilie NLM-4.")
    add_h2(doc, "4 Anhoerung")
    add_p(doc, "Wir geben Ihnen Gelegenheit, sich zu den vorgenannten Tatsachen und zu der beabsichtigten Feststellung innerhalb eines Monats nach Zugang dieses Schreibens zu aeussern. Ergaenzende Unterlagen zur tatsaechlichen Handhabung von Weisungen, Urlaub und Berichtspflichten werden erbeten.")
    add_p(doc, "Mit freundlichen Gruessen, i.A. Pruefstelle Statusfeststellung")
    add_h2(doc, "5 Fragenkatalog zur Stellungnahme")
    add_table(doc, ["Nr.", "Frage"], [
        [1, "Wurde Herrn Dr. Vogt seit 2023 mindestens einmal eine Weisung erteilt, der er gegen seinen erklaerten Willen gefolgt ist?"],
        [2, "Wie oft und in welcher Form hat der Beirat seit 2023 von seinen Zustimmungsvorbehalten Gebrauch gemacht?"],
        [3, "Wurde die variable Verguetung in den Jahren 2023 bis 2025 tatsaechlich vollstaendig, teilweise oder gar nicht ausgezahlt?"],
        [4, "In welchem Umfang hat Herr Dr. Vogt seinen vertraglichen Urlaubsanspruch tatsaechlich genommen?"],
        [5, "Besteht neben der Buergschaft ein Gesellschafterdarlehen oder eine Nachrangabrede von Herrn Dr. Vogt gegenueber der Gesellschaft?"],
        [6, "Wie wurde die Sperrminoritaet nach Paragraf 6.5 des Gesellschaftsvertrags seit ihrer Einfuehrung im September 2025 in der Praxis gehandhabt?"],
    ])
    add_formathinweis(doc)
    save(doc, ROOT / "16_drv_anhoerung_fragenkatalog.docx")


def doc_17_drv_bescheid():
    doc = new_document()
    add_letterhead(doc, [
        "Deutsche Rentenversicherung Bund",
        "Clearingstelle Sozialversicherungsstatus",
        "Ruhrstrasse 2, 10709 Berlin",
    ])
    add_title(doc, "Bescheid im Statusfeststellungsverfahren")
    add_p(doc, "Aktenzeichen: SV-2023-771402-VOGT - Berlin, den 09.02.2026")
    add_p(doc, "Betroffene: Neuralis MedTech GmbH und Herr Dr. Henrik Vogt")
    add_h2(doc, "1 Entscheidung")
    add_p(doc, "Es wird festgestellt, dass Herr Dr. Henrik Vogt seine Taetigkeit als Geschaeftsfuehrer der Neuralis MedTech GmbH seit dem 01.03.2023 im Rahmen eines abhaengigen Beschaeftigungsverhaeltnisses ausuebt. Es besteht Versicherungspflicht in der gesetzlichen Rentenversicherung und nach dem Recht der Arbeitsfoerderung. Fuer die Kranken- und Pflegeversicherung wird auf die freiwillige beziehungsweise private Absicherung von Herrn Dr. Vogt verwiesen, die von dieser Feststellung unberuehrt bleibt.")
    add_h2(doc, "2 Begruendung")
    add_p(doc, "2.1 Herr Dr. Vogt haelt mit 32 Prozent des Stammkapitals keine beherrschende Mehrheitsbeteiligung. Beschluesse mit einfacher Mehrheit kann er nicht verhindern.")
    add_p(doc, "2.2 Die im September 2025 eingefuehrte Sperrminoritaet nach Paragraf 6.5 des Gesellschaftsvertrags ist auf das Ressort Entwicklung und laufende klinische Studien beschraenkt und vermittelt keine umfassende Sperrminoritaet im Sinne der Rechtsprechung des Bundessozialgerichts.")
    add_p(doc, "2.3 Der Anstellungsvertrag enthaelt mit fester Monatsverguetung, Urlaubsanspruch und Entgeltfortzahlung im Krankheitsfall typische Arbeitnehmerschutzrechte.")
    add_p(doc, "2.4 Der Beirat hat nach den vorgelegten Protokollen wiederholt in operative Entscheidungen eingegriffen, etwa durch die Weisung zur Verschiebung von Neueinstellungen am 06.05.2026 und durch die Verschiebung der klinischen Studie am 14.02.2025.")
    add_p(doc, "2.5 Die persoenliche Buergschaft und das technische Fachwissen von Herrn Dr. Vogt begruenden ein wirtschaftliches Eigeninteresse, ersetzen jedoch nach staendiger Rechtsprechung des Bundessozialgerichts keine gesellschaftsrechtliche Rechtsmacht (vergleiche BSG, Urteil vom 14.03.2018, B 12 KR 13/17 R).")
    add_h2(doc, "3 Beitragsrechtliche Folgen")
    add_p(doc, "Die Neuralis MedTech GmbH wird als Arbeitgeberin zur Nachentrichtung der Gesamtsozialversicherungsbeitraege fuer den Zeitraum vom 01.03.2023 bis laufend herangezogen. Die Berechnung erfolgt gesondert durch den zustaendigen Rentenversicherungstraeger im Rahmen der Betriebspruefung nach Paragraf 28p SGB IV.")
    add_h2(doc, "4 Rechtsbehelfsbelehrung")
    add_p(doc, "Gegen diesen Bescheid kann innerhalb eines Monats nach Bekanntgabe Widerspruch bei der Deutschen Rentenversicherung Bund, Clearingstelle Sozialversicherungsstatus, Ruhrstrasse 2, 10709 Berlin, eingelegt werden.")
    add_p(doc, "Mit freundlichen Gruessen, i.A. Pruefstelle Statusfeststellung")
    add_formathinweis(doc)
    save(doc, ROOT / "17_drv_bescheid_statusfeststellung.docx")


def doc_18_widerspruch_mandant():
    doc = new_document()
    add_p(doc, "Dr. Henrik Vogt")
    add_p(doc, "Schuhstrasse 12, 91052 Erlangen")
    add_p(doc, "Erlangen, den 20.02.2026")
    add_p(doc, "An die Deutsche Rentenversicherung Bund, Clearingstelle Sozialversicherungsstatus, Ruhrstrasse 2, 10709 Berlin")
    add_h2(doc, "Widerspruch gegen den Bescheid vom 09.02.2026")
    add_p(doc, "Sehr geehrte Damen und Herren, ich widerspreche Ihrem Bescheid vom 09.02.2026, Aktenzeichen SV-2023-771402-VOGT. Ich bin nicht angestellt in dem Sinne, den Sie meinen. Ich habe die Firma gegruendet und bin bis heute derjenige, der die Technik versteht. Ohne mich gibt es das Produkt nicht. Ausserdem hafte ich mit 400000 Euro persoenlich fuer den Bankkredit, das macht doch kein normaler Arbeitnehmer.")
    add_p(doc, "Ich arbeite wann ich will und so viel wie noetig ist, oft nachts und am Wochenende. Von Urlaub im eigentlichen Sinn kann keine Rede sein, ich habe seit drei Jahren keine zwei Wochen am Stueck freigenommen. Der Beirat redet zwar mit, aber am Ende mache ich das, was fachlich richtig ist, das lasse ich mir nicht vorschreiben.")
    add_p(doc, "Ich bitte um Aufhebung des Bescheids. Falls das nicht geht, bitte ich um ein Gespraech, weil die Nachzahlung die Firma in ernste Schwierigkeiten bringen wuerde.")
    add_p(doc, "Mit freundlichen Gruessen, Henrik Vogt")
    add_p(doc, "Anmerkung Kanzlei: Dieser Widerspruch wurde vom Mandanten am 20.02.2026 ohne vorherige Ruecksprache eigenhaendig eingelegt und der Kanzlei erst am 25.02.2026 zur Kenntnis gebracht. Er enthaelt keine Auseinandersetzung mit der Sperrminoritaet nach Paragraf 6.5 des Gesellschaftsvertrags und stuetzt sich im Kern auf faktische Unentbehrlichkeit und Haftungsrisiko, was nach der Rechtsprechung des Bundessozialgerichts allein nicht ausreicht.")
    add_formathinweis(doc)
    save(doc, ROOT / "18_widerspruch_mandant_eigenhaendig.docx")


def doc_19_widerspruch_nachbesserung():
    doc = new_document()
    add_p(doc, "Kanzlei Rehbogen und Kollegen, Fachanwaelte fuer Sozialrecht und Gesellschaftsrecht")
    add_p(doc, "Rathausplatz 4, 91054 Erlangen - Telefon 09131 88 40 21 - Telefax 09131 88 40 29")
    add_p(doc, "Erlangen, den 10.03.2026")
    add_p(doc, "An die Deutsche Rentenversicherung Bund, Clearingstelle Sozialversicherungsstatus, Ruhrstrasse 2, 10709 Berlin")
    add_h2(doc, "Ergaenzung und Nachbesserung des Widerspruchs vom 20.02.2026, Aktenzeichen SV-2023-771402-VOGT")
    add_p(doc, "Sehr geehrte Damen und Herren, namens und in Vollmacht der Neuralis MedTech GmbH und des Herrn Dr. Henrik Vogt nehmen wir zu dem Bescheid vom 09.02.2026 wie folgt ergaenzend Stellung und vertiefen den bereits form- und fristgerecht eingelegten Widerspruch vom 20.02.2026.")
    add_h2(doc, "1 Rechtsmacht aus dem Gesellschaftsvertrag")
    add_p(doc, "Wir verweisen auf Paragraf 6.5 und Paragraf 7.3 des Gesellschaftsvertrags in der seit dem 19.09.2025 geltenden Fassung. Danach bedarf jede Weisung, die eine laufende klinische Studie unmittelbar unterbricht, sowie jede Aenderung des Ressorts von Herrn Dr. Vogt seiner Zustimmung. Diese Zustimmungsrechte gehen ueber ein blosses Anhoerungsrecht hinaus.")
    add_h2(doc, "2 Tatsaechliche Handhabung")
    add_p(doc, "Wir legen die Beiratsprotokolle vom 20.11.2025 vor, wonach Herr Dr. Vogt die Erteilung einer Patentlizenz an einen US-Partner erfolgreich verweigert hat, weil hierfuer eine Mehrheit von 75 Prozent beziehungsweise nach der Neufassung 90 Prozent erforderlich ist, die ohne seine Zustimmung nicht erreichbar ist.")
    add_h2(doc, "3 Unternehmerrisiko")
    add_p(doc, "Wir verweisen erneut auf die persoenliche Buergschaft ueber 400000,00 EUR und auf die Tatsache, dass Herr Dr. Vogt als Mitgruender im Jahr 2019 Alleingesellschafter war und seinen Anteil im Zuge der Finanzierungsrunde 2021 freiwillig reduziert hat, ohne operative Kontrolle vollstaendig abzugeben.")
    add_h2(doc, "4 Antrag")
    add_p(doc, "Wir beantragen, den Bescheid vom 09.02.2026 aufzuheben und festzustellen, dass Herr Dr. Vogt seine Taetigkeit als Geschaeftsfuehrer nicht im Rahmen eines abhaengigen Beschaeftigungsverhaeltnisses ausuebt. Hilfsweise wird angeregt, ein Gespraechstermin zur Erlaeuterung der Sperrminoritaet und ihrer gelebten Praxis anzuberaumen.")
    add_p(doc, "Mit freundlichen Gruessen, Dr. Fabian Rehbogen, Rechtsanwalt und Rentenberater")
    add_formathinweis(doc)
    save(doc, ROOT / "19_widerspruch_nachbesserung_kanzlei.docx")


def doc_20_widerspruchsbescheid():
    doc = new_document()
    add_letterhead(doc, [
        "Deutsche Rentenversicherung Bund",
        "Clearingstelle Sozialversicherungsstatus, Widerspruchsstelle",
        "Ruhrstrasse 2, 10709 Berlin",
    ])
    add_title(doc, "Widerspruchsbescheid")
    add_p(doc, "Aktenzeichen: SV-2023-771402-VOGT-W - Berlin, den 04.05.2026")
    add_h2(doc, "1 Entscheidung")
    add_p(doc, "Der Widerspruch der Neuralis MedTech GmbH und des Herrn Dr. Henrik Vogt vom 20.02.2026 in der Fassung der Ergaenzung vom 10.03.2026 gegen den Bescheid vom 09.02.2026 wird zurueckgewiesen.")
    add_h2(doc, "2 Gruende")
    add_p(doc, "2.1 Die mit Nachtrag vom 19.09.2025 eingefuehrte Sperrminoritaet nach Paragraf 6.5 des Gesellschaftsvertrags ist gegenstaendlich auf das Ressort Entwicklung und auf laufende klinische Studien beschraenkt. Sie erstreckt sich nicht auf Beschluesse der Gesellschafterversammlung zur Abberufung, zur Verguetung oder zu sonstigen fuer den Status massgeblichen Fragen.")
    add_p(doc, "2.2 Nach staendiger Rechtsprechung des Bundessozialgerichts kommt es fuer die sozialversicherungsrechtliche Beurteilung eines Gesellschafter-Geschaeftsfuehrers massgeblich auf dessen Rechtsmacht innerhalb der Gesellschaft an, wie sie sich aus dem Gesellschaftsvertrag ergibt, nicht auf seine faktische Position oder seine Unentbehrlichkeit fuer das operative Geschaeft (Bundessozialgericht, Urteil vom 19.09.2019, B 12 R 25/18 R; Bundessozialgericht, Urteil vom 14.03.2018, B 12 KR 13/17 R; Bundessozialgericht, Urteil vom 12.05.2020, B 12 R 5/16 R).")
    add_p(doc, "2.3 Eine punktuelle Sperrminoritaet fuer einzelne Sachbereiche genuegt nach der Rechtsprechung nicht, um eine umfassende Rechtsmacht zur Verhinderung ihm nicht genehmer Weisungen in allen fuer das Anstellungsverhaeltnis zentralen Fragen zu begruenden (vergleiche Bundessozialgericht, Urteil vom 12.05.2020, B 12 R 5/16 R, sowie Bundessozialgericht, Urteil vom 08.07.2020, B 12 R 6/19 R, zur Notwendigkeit einer im Gesellschaftsvertrag verankerten Rechtsmacht statt blosser Ruecksichtnahme unter Familienangehoerigen oder Mitgruendern).")
    add_p(doc, "2.4 Die persoenliche Buergschaft ueber 400000,00 EUR und die technische Schluesselstellung von Herrn Dr. Vogt begruenden ein wirtschaftliches Eigeninteresse, ersetzen jedoch keine gesellschaftsrechtliche Rechtsmacht und sind allenfalls im Rahmen einer Gesamtwuerdigung von untergeordneter Bedeutung.")
    add_p(doc, "2.5 Die vertraglich vereinbarte feste Verguetung, der Urlaubsanspruch von 30 Arbeitstagen und die sechswoechige Entgeltfortzahlung im Krankheitsfall sind gewichtige Indizien fuer ein Beschaeftigungsverhaeltnis.")
    add_h2(doc, "3 Rechtsbehelfsbelehrung")
    add_p(doc, "Gegen diesen Widerspruchsbescheid kann innerhalb eines Monats nach Zustellung Klage beim Sozialgericht Erlangen, Ohmplatz 4, 91054 Erlangen, erhoben werden.")
    add_p(doc, "Mit freundlichen Gruessen, i.A. Widerspruchsstelle Statusfeststellung")
    add_formathinweis(doc)
    save(doc, ROOT / "20_widerspruchsbescheid_drv.docx")


if __name__ == "__main__":
    doc_15_c0031_antrag()
    doc_16_drv_anhoerung()
    doc_17_drv_bescheid()
    doc_18_widerspruch_mandant()
    doc_19_widerspruch_nachbesserung()
    doc_20_widerspruchsbescheid()
