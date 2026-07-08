import sys
sys.path.insert(0, "/home/user/workspace/legal-work/target/scripts/_tmp_gen")
from docx_helper import new_document, add_title, add_h2, add_h3, add_p, add_letterhead, add_table, add_formathinweis, save

BASE = "/home/user/workspace/legal-work/target/testakten/unfallversicherung-arbeitsunfall-lagerleiter-sturz-trier/"

KANZLEI = [
    "Kanzlei Lindenhof und Partner mbB",
    "Fachanwaelte fuer Sozialrecht",
    "Domfreihof 6, 54290 Trier",
    "Telefon 0651 145 7720, Telefax 0651 145 7721",
    "USt-IdNr. DE 267 991 430",
    "Bearbeiterin: Dr. Nadine Ohlerich, Rechtsanwaeltin, Fachanwaeltin fuer Sozialrecht",
]

BG = [
    "Berufsgenossenschaft Handel und Warenlogistik",
    "Bezirksverwaltung Trier",
    "Loebstrasse 22, 54292 Trier",
    "Aktenzeichen: BGHW-2026-350118-MOELLER",
    "Sachbearbeiterin: Yvonne Kastner",
]

# 10 - Ausfuehrliche Unfallschilderung des Mandanten
doc = new_document()
add_title(doc, "Ausfuehrliche Unfallschilderung des Mandanten")
add_letterhead(doc, KANZLEI)
add_h2(doc, "1. Vorbemerkung")
add_p(doc, "Die nachfolgende Schilderung wurde am 14.04.2026 im Rahmen eines rund neunzigminuetigen Mandantengespraechs in der Kanzlei aufgenommen und dem Mandanten Karsten Moeller anschliessend zur Durchsicht und Unterschrift vorgelegt. Sie ersetzt keine eidesstattliche Versicherung, dient aber als Grundlage fuer die Widerspruchsbegruendung.")
add_h2(doc, "2. Tagesablauf vor dem Ereignis")
add_p(doc, "Herr Moeller begann die Fruehschicht am 03.04.2026 um 6:00 Uhr mit der Uebergabe von Schichtleiter Dennis Auer. Auer berichtete, dass Rampe 4 bereits in der Nachtschicht Probleme beim Ausfahren der Ueberladebruecke gemacht habe und ein LKW der Spedition Havelmann seit 5:50 Uhr an Rampe 4 auf Entladung warte. Herr Moeller entschied sich, selbst nach Rampe 4 zu sehen, weil der zustaendige Rampenwart erst ab 7:00 Uhr eingeteilt war.")
add_h2(doc, "3. Ablauf an der Rampe")
add_p(doc, "Gegen 6:38 Uhr erreichte Herr Moeller Rampe 4. Die Ueberladebruecke stand schraeg und liess sich mit dem Hebel nicht vollstaendig ausfahren. Er stellte sich seitlich auf die Rampenkante, um mit beiden Haenden am Hebel Zug auszuueben. Nach eigener Erinnerung loeste sich der Widerstand ploetzlich, die Bruecke schnellte nach unten durch, und er verlor den Halt. Er stuerzte nach rechts vornueber auf den etwa 90 Zentimeter tiefer liegenden Hallenboden vor der Rampe.")
add_h3(doc, "3.1 Koerperhaltung beim Aufprall")
add_p(doc, "Der Mandant beschreibt, dass er versucht habe, sich mit dem rechten Arm abzufangen, dabei aber mit der rechten Schulter zuerst aufgeschlagen sei; der Kopf habe die Betonkante der Rampenlippe im Nachgang gestreift. Er sei kurz benommen gewesen, habe aber nicht das Bewusstsein verloren.")
add_h3(doc, "3.2 Erste Reaktion")
add_p(doc, "Er habe sofort laut nach Hilfe gerufen und dabei sinngemaess gesagt: 'Die Bruecke hat nachgegeben, die war schon wieder schwergaengig.' Diese Aussage deckt sich mit der spaeteren Zeugenangabe von Bastian Kopp.")
add_h2(doc, "4. Angaben zur Vorgeschichte der Schulter")
add_p(doc, "Herr Moeller bestaetigt, in den Jahren 2016 bis 2018 gelegentlich nach Handballspielen Schulterbeschwerden rechts gehabt zu haben, die jeweils nach wenigen Tagen ohne Arztbesuch abgeklungen seien. Seit 2019 habe er keinen Leistungssport mehr betrieben und keinerlei Einschraenkung im Arbeitsalltag gehabt, was durch die betriebsaerztliche Untersuchung 2024 bestaetigt worden sei.")
add_h2(doc, "5. Angaben zur Arbeitsanweisung")
add_p(doc, "Nach interner Arbeitsanweisung Nr. 14 zur Ladungssicherung ist eine klemmende Ueberladebruecke durch den Rampenwart und nicht durch den Lagerleiter zu warten. Herr Moeller raeumt ein, im Zeitdruck gegen diese Anweisung verstossen zu haben, weist aber darauf hin, dass Vorgesetzte wiederholt toleriert haetten, dass Schichtverantwortliche bei Personalengpaessen selbst eingriffen.")
add_formathinweis(doc)
save(doc, BASE + "10_unfallschilderung_mandant_ausfuehrlich.docx")

# 11 - Unfallanzeige BG Formular komplett
doc = new_document()
add_title(doc, "Unfallanzeige des Unternehmers, Formular BGHW, ausgefuellt")
add_h2(doc, "1. Angaben zum Unternehmen")
add_table(doc, ["Feld", "Angabe"], [
    ["Unternehmen", "MoselLogistik GmbH"],
    ["Anschrift", "Hafenstrasse 28, 54293 Trier"],
    ["Mitgliedsnummer BGHW", "350118"],
    ["Betriebsstaette", "Logistikzentrum Trier-Ehrang, Halle C"],
    ["Zustaendige Berufsgenossenschaft", "Berufsgenossenschaft Handel und Warenlogistik, Bezirksverwaltung Trier"],
])
add_h2(doc, "2. Angaben zur versicherten Person")
add_table(doc, ["Feld", "Angabe"], [
    ["Name", "Karsten Moeller"],
    ["Geburtsdatum", "19.08.1971"],
    ["Beschaeftigt seit", "01.03.2011"],
    ["Taetigkeit", "Lagerleiter, Schichtverantwortlicher Wareneingang"],
    ["Versicherungsnummer", "65 190871 M 003"],
])
add_h2(doc, "3. Angaben zum Unfallhergang")
add_table(doc, ["Feld", "Angabe"], [
    ["Unfalltag", "03.04.2026"],
    ["Unfallzeit", "gegen 6:42 Uhr"],
    ["Unfallort", "Rampe 4, Logistikzentrum Trier-Ehrang"],
    ["Letzter Arbeitstag vor Meldung", "03.04.2026"],
    ["Datum der Anzeige", "08.04.2026"],
    ["Meldeweg", "elektronisch ueber DGUV-Formularservice"],
])
add_h2(doc, "4. Unfallhergang laut Unternehmer")
add_p(doc, "Der Versicherte habe beim Loesen einer klemmenden Ueberladebruecke an Rampe 4 das Gleichgewicht verloren und sei zu Boden gestuerzt. Zeugen des unmittelbaren Sturzes seien nicht vorhanden. Erste Hilfe sei durch die Sicherheitsbeauftragte vor Ort geleistet worden, anschliessend Transport durch den Rettungsdienst.")
add_h2(doc, "5. Angaben zu Verletzungen")
add_p(doc, "Nach vorlaeufiger Einschaetzung: Schulterverletzung rechts, Schuerfwunden, Verdacht auf Kopfprellung. Erstbehandelnder Arzt: Dr. Reiner Kauth, Bruederkrankenhaus Trier, Durchgangsarzt.")
add_h2(doc, "6. Anmerkung der Kanzlei")
add_p(doc, "Das Formular enthaelt in Feld 14 (Zusatzangaben) keinen Hinweis auf die Wartungshistorie der Rampe, obwohl diese dem Arbeitgeber nach dem Wartungsbuch bekannt war. Diese Luecke ist fuer die Beweiswuerdigung im Widerspruch bedeutsam.")
add_formathinweis(doc)
save(doc, BASE + "11_unfallanzeige_bg_formular_komplett.docx")

print("Teil 1 fertig")
