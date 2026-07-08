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


def doc_21_klageschrift():
    doc = new_document()
    add_p(doc, "Kanzlei Rehbogen und Kollegen, Fachanwaelte fuer Sozialrecht und Gesellschaftsrecht")
    add_p(doc, "Rathausplatz 4, 91054 Erlangen - Telefon 09131 88 40 21 - Telefax 09131 88 40 29")
    add_p(doc, "Unser Zeichen: 26-VOGT-0917 - Erlangen, den 28.05.2026")
    add_p(doc, "An das Sozialgericht Erlangen, Ohmplatz 4, 91054 Erlangen")
    add_title(doc, "Klage")
    add_p(doc, "der Neuralis MedTech GmbH, vertreten durch den Geschaeftsfuehrer Dr. Henrik Vogt, Henkestrasse 91, 91054 Erlangen, und des Herrn Dr. Henrik Vogt, Schuhstrasse 12, 91052 Erlangen - Klaeger -")
    add_p(doc, "Prozessbevollmaechtigte: Kanzlei Rehbogen und Kollegen, Rathausplatz 4, 91054 Erlangen")
    add_p(doc, "gegen die Deutsche Rentenversicherung Bund, Ruhrstrasse 2, 10709 Berlin - Beklagte -")
    add_p(doc, "wegen Feststellung des sozialversicherungsrechtlichen Status")
    add_h2(doc, "1 Antraege")
    add_p(doc, "1.1 Der Bescheid der Beklagten vom 09.02.2026 in Gestalt des Widerspruchsbescheids vom 04.05.2026 wird aufgehoben.")
    add_p(doc, "1.2 Es wird festgestellt, dass Herr Dr. Henrik Vogt in seiner Taetigkeit als Geschaeftsfuehrer der Neuralis MedTech GmbH seit dem 01.03.2023 nicht der Versicherungspflicht in der gesetzlichen Rentenversicherung und nach dem Recht der Arbeitsfoerderung unterliegt.")
    add_h2(doc, "2 Sachverhalt")
    add_p(doc, "Der Klaeger zu 2 ist Mitgruender der Klaegerin zu 1 und hielt bei Gruendung im Jahr 2019 saemtliche Geschaeftsanteile. Nach dem Einstieg der FrankenHealth Ventures GmbH im Jahr 2021 haelt er noch 32 Prozent des Stammkapitals. Er ist alleinvertretungsberechtigter Geschaeftsfuehrer mit Befreiung von Paragraf 181 BGB. Mit Nachtrag vom 19.09.2025 wurde ihm eine Sperrminoritaet fuer sein Ressort Entwicklung und fuer laufende klinische Studien eingeraeumt.")
    add_h2(doc, "3 Rechtliche Wuerdigung")
    add_p(doc, "3.1 Zwar verfuegt der Klaeger zu 2 formal nur ueber eine Minderheitsbeteiligung. Nach der Rechtsprechung des Bundessozialgerichts kommt es jedoch nicht allein auf die Kapitalmehrheit an, sondern darauf, ob der Geschaeftsfuehrer aufgrund gesellschaftsvertraglich eingeraeumter Vetorechte Weisungen der Gesellschafterversammlung verhindern kann, die seinen Aufgabenbereich betreffen (Bundessozialgericht, Urteil vom 12.05.2020, B 12 R 5/16 R).")
    add_p(doc, "3.2 Die mit Nachtrag vom 19.09.2025 eingefuehrte Sperrminoritaet in Paragraf 6.5 des Gesellschaftsvertrags erstreckt sich zwar nur auf das Ressort Entwicklung. Dieses Ressort ist jedoch nach der internen Aufgabenverteilung der einzige operative Kernbereich des Klaegers zu 2 und wirtschaftlich der Kern der unternehmerischen Taetigkeit der Klaegerin zu 1.")
    add_p(doc, "3.3 Der Klaeger zu 2 traegt mit der persoenlichen Buergschaft ueber 400000,00 EUR ein Unternehmerrisiko, das deutlich ueber das eines Fremdgeschaeftsfuehrers hinausgeht.")
    add_p(doc, "3.4 Die im Anstellungsvertrag vorgesehene feste Verguetung und der Urlaubsanspruch sind bei Gesellschafter-Geschaeftsfuehrern kein zwingendes Indiz fuer Beschaeftigung, wenn die uebrigen Umstaende, insbesondere die tatsaechliche Steuerungsmacht im operativen Kernbereich, fuer Selbstaendigkeit sprechen.")
    add_h2(doc, "4 Beweisantritt")
    add_p(doc, "Zeugenvernehmung des Beiratsvorsitzenden Prof. Dr. Cornelius Baumhauer und der Gesellschafterin Dr. Miriam Seidl zur tatsaechlichen Handhabung der Sperrminoritaet seit September 2025. Beiziehung der Beiratsprotokolle vom 14.02.2025, 20.11.2025 und 06.05.2026.")
    add_p(doc, "Dr. Fabian Rehbogen, Rechtsanwalt und Rentenberater")
    add_formathinweis(doc)
    save(doc, ROOT / "21_klageschrift_sozialgericht_erlangen.docx")


def doc_22_klageerwiderung():
    doc = new_document()
    add_letterhead(doc, [
        "Deutsche Rentenversicherung Bund",
        "Prozessvertretung, Dezernat Statusfeststellung",
        "Ruhrstrasse 2, 10709 Berlin",
    ])
    add_p(doc, "Aktenzeichen: SV-2023-771402-VOGT - Berlin, den 30.06.2026")
    add_p(doc, "An das Sozialgericht Erlangen, Az. S 5 R 214/26")
    add_title(doc, "Klageerwiderung")
    add_p(doc, "In dem Rechtsstreit Neuralis MedTech GmbH und Dr. Henrik Vogt gegen Deutsche Rentenversicherung Bund")
    add_h2(doc, "1 Antrag")
    add_p(doc, "Die Klage wird abgewiesen.")
    add_h2(doc, "2 Begruendung")
    add_p(doc, "2.1 Die von den Klaegern angefuehrte Sperrminoritaet nach Paragraf 6.5 des Gesellschaftsvertrags ist gegenstaendlich eng begrenzt. Sie betrifft ausschliesslich Weisungen, die eine laufende klinische Studie unmittelbar unterbrechen, sowie Aenderungen des Ressorts des Klaegers zu 2. Sie erstreckt sich nicht auf Beschluesse zur Abberufung, zur Verguetung, zur Feststellung des Jahresabschlusses oder zu sonstigen fuer die Statusbeurteilung zentralen Fragen.")
    add_p(doc, "2.2 Nach der Rechtsprechung des Bundessozialgerichts genuegt eine derart punktuelle Sperrminoritaet nicht, um eine umfassende Rechtsmacht zu begruenden, die es dem Gesellschafter-Geschaeftsfuehrer erlaubt, ihm nicht genehme Weisungen in allen fuer das Anstellungsverhaeltnis wesentlichen Fragen zu verhindern (Bundessozialgericht, Urteil vom 08.07.2020, B 12 R 6/19 R).")
    add_p(doc, "2.3 Die Beiratsprotokolle belegen im Uebrigen, dass der Beirat wiederholt in die operative Fuehrung eingegriffen hat, etwa durch die Weisung zur Verschiebung von Neueinstellungen vom 06.05.2026 und durch die Verweigerung des Budgets fuer die zweite klinische Studie am 14.02.2025, wo der Klaeger zu 2 lediglich ein Alternativbudget vorlegen, die Verschiebung aber letztlich hinnehmen musste.")
    add_p(doc, "2.4 Die persoenliche Buergschaft begruendet ein zivilrechtliches Haftungsrisiko gegenueber der Bank, nicht jedoch eine gesellschaftsrechtliche Rechtsmacht gegenueber der Klaegerin zu 1 und ihren Organen. Nach der Rechtsprechung des Bundessozialgerichts ist ein Unternehmerrisiko nur dann von Bedeutung, wenn ihm eine entsprechende Rechtsmacht gegenuebersteht (Bundessozialgericht, Urteil vom 14.03.2018, B 12 KR 13/17 R).")
    add_p(doc, "2.5 Die vertraglichen Regelungen zu Verguetung, Urlaub und Entgeltfortzahlung entsprechen typischen Arbeitnehmerschutzrechten und sind im Rahmen der Gesamtwuerdigung zu beruecksichtigen.")
    add_h2(doc, "3 Hinweis zur gebotenen Gesamtwuerdigung")
    add_p(doc, "Die Beklagte regt an, im Rahmen der muendlichen Verhandlung insbesondere die tatsaechliche Handhabung der Sperrminoritaet seit September 2025 sowie den Umgang mit der variablen Verguetung in den Jahren 2023 bis 2025 aufzuklaeren.")
    add_p(doc, "i.A. Prozessvertretung Statusfeststellung")
    add_formathinweis(doc)
    save(doc, ROOT / "22_klageerwiderung_drv.docx")


def doc_23_vergleichsvorschlag():
    doc = new_document()
    add_p(doc, "Kanzlei Rehbogen und Kollegen, Fachanwaelte fuer Sozialrecht und Gesellschaftsrecht")
    add_p(doc, "Rathausplatz 4, 91054 Erlangen - Erlangen, den 15.09.2026")
    add_p(doc, "An das Sozialgericht Erlangen, Az. S 5 R 214/26, sowie an die Deutsche Rentenversicherung Bund")
    add_title(doc, "Vergleichsvorschlag")
    add_p(doc, "Im Anschluss an den Eroerterungstermin vom 08.09.2026 unterbreiten die Klaeger folgenden Vergleichsvorschlag, um das Verfahren einer einvernehmlichen Erledigung zuzufuehren.")
    add_h2(doc, "1 Vorschlag zur zeitlichen Aufteilung")
    add_p(doc, "1.1 Fuer den Zeitraum vom 01.03.2023 bis zum 18.09.2025 (vor Einfuehrung der Sperrminoritaet) erkennen die Klaeger die Sozialversicherungspflicht des Herrn Dr. Vogt als Geschaeftsfuehrer an.")
    add_p(doc, "1.2 Fuer den Zeitraum ab dem 19.09.2025 (nach Einfuehrung der Sperrminoritaet in Paragraf 6.5 des Gesellschaftsvertrags) stellt die Beklagte die Selbstaendigkeit des Herrn Dr. Vogt fest.")
    add_h2(doc, "2 Beitragsfolgen des Vorschlags")
    add_p(doc, "2.1 Fuer den anerkannten Zeitraum wird eine Beitragsnachforderung nach Massgabe der als Anlage beigefuegten Berechnung akzeptiert, begrenzt auf die Verjaehrungsfrist nach Paragraf 25 SGB IV.")
    add_p(doc, "2.2 Saeumniszuschlaege werden nur fuer den Zeitraum ab Zugang der Anhoerung vom 18.11.2025 erhoben, da die Klaeger vorher gutglaeubig von Selbstaendigkeit ausgingen und keine grobe Fahrlaessigkeit vorliegt.")
    add_h2(doc, "3 Gegenleistung der Klaeger")
    add_p(doc, "Die Klaeger verzichten im Gegenzug auf die Fortfuehrung der Klage fuer den Zeitraum bis zum 18.09.2025 und erklaeren sich zur zuegigen Zahlung binnen sechs Monaten bereit.")
    add_p(doc, "Wir bitten um Mitteilung, ob die Beklagte diesem Vorschlag naehertreten kann, und regen einen weiteren Erörterungstermin an.")
    add_p(doc, "Dr. Fabian Rehbogen, Rechtsanwalt und Rentenberater")
    add_formathinweis(doc)
    save(doc, ROOT / "23_vergleichsvorschlag_beitragserstattung.docx")


def doc_24_vergleichsprotokoll():
    doc = new_document()
    add_title(doc, "Protokoll des Erörterungstermins und Vergleichsniederschrift")
    add_p(doc, "Sozialgericht Erlangen, Az. S 5 R 214/26 - Termin vom 20.10.2026")
    add_h2(doc, "1 Anwesende")
    add_p(doc, "Fuer die Klaeger: Dr. Fabian Rehbogen, Rechtsanwalt. Dr. Henrik Vogt, persoenlich. Fuer die Beklagte: Regierungsdirektorin Frau Bettina Holzapfel.")
    add_h2(doc, "2 Erörterung")
    add_p(doc, "Das Gericht weist darauf hin, dass die Sperrminoritaet nach Paragraf 6.5 des Gesellschaftsvertrags nach vorlaeufiger Einschaetzung der Kammer zu eng gefasst sei, um fuer die Zeit ab September 2025 eine durchgreifende Rechtsmachtaenderung zu belegen. Die Kammer regt gleichwohl eine vergleichsweise Erledigung an, weil die tatsaechliche Handhabung im Einzelfall streitig bleibt und eine Beweisaufnahme mit erheblichem Aufwand verbunden waere.")
    add_h2(doc, "3 Vergleich")
    add_p(doc, "Die Beteiligten schliessen folgenden Vergleich: Fuer den Zeitraum vom 01.03.2023 bis zum 31.12.2025 besteht Sozialversicherungspflicht des Herrn Dr. Vogt als Geschaeftsfuehrer der Neuralis MedTech GmbH. Fuer den Zeitraum ab dem 01.01.2026 stellt die Beklagte fest, dass Herr Dr. Vogt nicht der Versicherungspflicht unterliegt, nachdem die Klaegerin zu 1 mit weiterem Nachtrag vom 15.10.2026 die Sperrminoritaet auf saemtliche Beschluesse zur Feststellung des Jahresbudgets und zur Verguetungsstruktur des Klaegers zu 2 erstreckt hat.")
    add_p(doc, "Die Beitragsnachforderung fuer den anerkannten Zeitraum wird auf Grundlage der Anlage zur Beitragsberechnung festgesetzt. Saeumniszuschlaege werden ab dem 18.11.2025 (Zugang der Anhoerung) erhoben. Die Kosten des Verfahrens werden gegeneinander aufgehoben.")
    add_p(doc, "Vorgelesen und genehmigt. Protokollfuehrerin: Justizangestellte Frau Karin Deml.")
    add_formathinweis(doc)
    save(doc, ROOT / "24_vergleichsprotokoll.docx")


def doc_25_betriebspruefungsbericht():
    doc = new_document()
    add_letterhead(doc, [
        "Deutsche Rentenversicherung Bund",
        "Betriebspruefungsdienst, Pruefbereich Mittelfranken",
        "Wittelsbacherring 11, 95444 Bayreuth",
    ])
    add_title(doc, "Betriebspruefungsbericht nach Paragraf 28p SGB IV")
    add_p(doc, "Geprueftes Unternehmen: Neuralis MedTech GmbH, Henkestrasse 91, 91054 Erlangen - Pruefzeitraum: 01.01.2022 bis 31.12.2025 - Pruefungstermin vor Ort: 03.02.2026 bis 05.02.2026")
    add_h2(doc, "1 Pruefungsschwerpunkt")
    add_p(doc, "Sozialversicherungsrechtlicher Status des Geschaeftsfuehrers Dr. Henrik Vogt sowie ordnungsgemaesse Beitragsabfuehrung fuer die uebrigen zwoelf Beschaeftigten.")
    add_h2(doc, "2 Feststellungen zu Dr. Vogt")
    add_p(doc, "2.1 Die Gesellschaft hat fuer Herrn Dr. Vogt seit dem 01.03.2023 keine Beitraege zur Renten- und Arbeitslosenversicherung abgefuehrt und ihn als selbstaendigen Gesellschafter-Geschaeftsfuehrer behandelt.")
    add_p(doc, "2.2 Das parallel laufende Statusfeststellungsverfahren der Clearingstelle (Aktenzeichen SV-2023-771402-VOGT) ist noch nicht bestandskraeftig abgeschlossen. Der Pruefdienst schliesst sich der vorlaeufigen Einschaetzung der Clearingstelle an und geht von einer Nachforderung dem Grunde nach aus, stellt die Hoehe jedoch bis zur bestandskraeftigen Entscheidung zurueck.")
    add_h2(doc, "3 Uebrige Feststellungen")
    add_p(doc, "3.1 Bei den zwoelf uebrigen Beschaeftigten wurden keine Beanstandungen festgestellt.")
    add_p(doc, "3.2 Die Meldungen zur Sozialversicherung fuer das Jahr 2024 wurden mit einer Verspaetung von durchschnittlich elf Tagen abgegeben; hierfuer wird ein gesondertes Verwarnungsgeld gepruft, jedoch nicht Gegenstand dieses Berichts.")
    add_h2(doc, "4 Vorlaeufiges Ergebnis")
    add_p(doc, "Der Pruefdienst wird nach Abschluss des Statusfeststellungsverfahrens einen gesonderten Beitragsbescheid fuer Herrn Dr. Vogt erlassen. Bis dahin ruht die Festsetzung insoweit.")
    add_p(doc, "Bayreuth, den 12.02.2026 - i.A. Betriebspruefungsdienst")
    add_formathinweis(doc)
    save(doc, ROOT / "25_betriebspruefungsbericht.docx")


def doc_26_steuerberater_stellungnahme():
    doc = new_document()
    add_letterhead(doc, [
        "Steuerkanzlei Wengert und Partner",
        "Nuernberger Strasse 62, 91052 Erlangen",
        "Telefon 09131 40 22 10",
    ])
    add_title(doc, "Stellungnahme zu bAV-Auswirkungen und Zusagen")
    add_p(doc, "Mandantin: Neuralis MedTech GmbH - Erlangen, den 03.04.2026")
    add_h2(doc, "1 Anlass")
    add_p(doc, "Im Rahmen des laufenden Statusfeststellungsverfahrens bittet die Geschaeftsfuehrung um Einschaetzung, welche steuerlichen und betriebsrentenrechtlichen Folgen eine rueckwirkende Feststellung der Sozialversicherungspflicht von Herrn Dr. Vogt haette.")
    add_h2(doc, "2 Betriebliche Altersversorgung")
    add_p(doc, "Herr Dr. Vogt hat im Jahr 2021 eine Pensionszusage der Gesellschaft in Hoehe von 800 EUR monatlicher Anwartschaft ab Vollendung des 67. Lebensjahres erhalten. Diese Zusage wurde als Vorstands- beziehungsweise Gesellschafter-Geschaeftsfuehrer-Zusage bilanziert. Bei rueckwirkender Feststellung der Beschaeftigung ist zu pruefen, ob die Zusage als beherrschender Gesellschafter-Geschaeftsfuehrer im Sinne der koerperschaftsteuerlichen Rechtsprechung zu verdeckten Gewinnausschuettungen fuehrt. Da Herr Dr. Vogt mit 32 Prozent nicht beherrschend im koerperschaftsteuerlichen Sinne ist, ist dieses Risiko nachrangig.")
    add_h2(doc, "3 Lohnsteuerliche Behandlung")
    add_p(doc, "Die bisherige Verguetung wurde als Geschaeftsfuehrervergueting ohne Lohnsteuerabzug im engeren Sinne, jedoch mit Lohnsteuerabzug analog Paragraf 19 EStG behandelt, da die Vergueting bereits als Arbeitslohn deklariert wurde. Eine sozialversicherungsrechtliche Nachforderung aendert an der bisherigen lohnsteuerlichen Behandlung nichts Wesentliches.")
    add_h2(doc, "4 Gesellschafterdarlehen")
    add_p(doc, "Herr Dr. Vogt hat der Gesellschaft im Jahr 2024 ein Gesellschafterdarlehen ueber 60000,00 EUR zu einem Zinssatz von drei Prozent gewaehrt. Bei rueckwirkender Feststellung der Beschaeftigung bleibt dieses Darlehen zivilrechtlich unberuehrt; es kann jedoch im Statusfeststellungsverfahren als zusaetzliches Indiz fuer Unternehmerrisiko angefuehrt werden.")
    add_h2(doc, "5 Empfehlung")
    add_p(doc, "Aus steuerlicher Sicht bestehen gegen eine rueckwirkende Feststellung keine durchgreifenden Bedenken. Eine Ruecklage fuer die moegliche Beitragsnachforderung in Hoehe der Berechnung der Kanzlei Rehbogen wird empfohlen.")
    add_p(doc, "Dipl.-Kfm. Sören Wengert, Steuerberater")
    add_formathinweis(doc)
    save(doc, ROOT / "26_steuerberater_stellungnahme_bav.docx")


if __name__ == "__main__":
    doc_21_klageschrift()
    doc_22_klageerwiderung()
    doc_23_vergleichsvorschlag()
    doc_24_vergleichsprotokoll()
    doc_25_betriebspruefungsbericht()
    doc_26_steuerberater_stellungnahme()
