import sys
sys.path.insert(0, "/home/user/workspace/legal-work/target/scripts/_tmp_gen")
from docx_helper import new_document, add_title, add_h2, add_h3, add_p, add_letterhead, add_table, add_formathinweis, save

BASE = "/home/user/workspace/legal-work/target/testakten/unfallversicherung-arbeitsunfall-lagerleiter-sturz-trier/"
GUTACHTER = ["Praxis fuer Unfallchirurgische Begutachtung", "Prof. Dr. Matthias Sorgenfrei, Facharzt fuer Orthopaedie und Unfallchirurgie", "Kaiserstrasse 2, 55116 Mainz"]

# 28 - Sachverstaendigengutachten orthopaedisch-unfallchirurgisch
doc = new_document()
add_title(doc, "Unfallchirurgisch-orthopaedisches Zusammenhangsgutachten")
add_letterhead(doc, GUTACHTER)
add_p(doc, "Gutachten im Auftrag des Sozialgerichts Trier, Az. S 4 U 88/26, erstattet am 14.01.2027 nach ambulanter Untersuchung des Klaegers am 08.01.2027.")
add_h2(doc, "1. Fragestellung des Gerichts")
add_p(doc, "Steht die am 09.04.2026 diagnostizierte Teilruptur der Supraspinatussehne rechts im Sinne der wesentlichen Bedingung in ursaechlichem Zusammenhang mit dem Ereignis vom 03.04.2026, oder ist sie ausschliesslich oder ueberwiegend auf die vorbestehende degenerative Schaedigung zurueckzufuehren.")
add_h2(doc, "2. Untersuchungsbefund")
add_p(doc, "Aktive Abduktion rechts 150 Grad, Kraftgrad 4 von 5 im Seitenvergleich, endgradiger Schmerz bei Aussenrotation. Vernarbte arthroskopische Portale reizlos. Im Vergleich zur linken Schulter deutliches, aber nicht vollstaendiges funktionelles Defizit.")
add_h2(doc, "3. Auswertung der Aktenlage")
add_p(doc, "Der Sachverstaendige wertet den geschilderten Unfallhergang, die uebereinstimmenden Erstangaben gegenueber Ersthelferin, Rettungsdienst und Durchgangsarzt, den intraoperativen Befund eines frischen Rupturrandes sowie das im MRT nachgewiesene Knochenmarkoedem als konsistentes Gesamtbild fuer eine akute traumatische Komponente.")
add_h2(doc, "4. Gutachterliche Einschaetzung")
add_p(doc, "Der Sachverstaendige gelangt zu dem Ergebnis, dass das Ereignis vom 03.04.2026 mit hinreichender Wahrscheinlichkeit eine wesentliche Teilursache der aufgetretenen Funktionsstoerung darstellt. Die vorbestehende degenerative Veraenderung des AC-Gelenks habe die Schulter fuer eine Verletzung anfaelliger gemacht, trete aber als Ursache des konkreten Funktionsverlusts gegenueber dem Unfallereignis nicht in den Vordergrund.")
add_h2(doc, "5. Einschaetzung der Minderung der Erwerbsfaehigkeit")
add_p(doc, "Unter Zugrundelegung der gaengigen unfallmedizinischen Bewertungstabellen fuer Schaeden der oberen Extremitaet schaetzt der Sachverstaendige die unfallbedingte Minderung der Erwerbsfaehigkeit auf der Grundlage des aktuellen Funktionsbefundes auf 20 vom Hundert ein, mit der Einschraenkung, dass eine Nachuntersuchung nach weiteren zwoelf Monaten zur Beurteilung der Dauerhaftigkeit angezeigt ist.")
add_formathinweis(doc)
save(doc, BASE + "28_sachverstaendigengutachten_unfallchirurgisch.docx")

# 29 - Vorschadenshistorie ausfuehrlich
doc = new_document()
add_title(doc, "Vorschadenshistorie, ausfuehrliche Zusammenstellung")
add_letterhead(doc, ["Kanzlei Lindenhof und Partner mbB", "Domfreihof 6, 54290 Trier"])
add_h2(doc, "1. Hausarztunterlagen 2016 bis 2018")
add_p(doc, "Hausarzt Dr. Wilfried Sommerlath dokumentiert am 14.09.2016 eine Vorstellung wegen Schulterschmerzen rechts nach einem Handballspiel, verordnet wird eine kurzzeitige Schonung ohne Bildgebung. Weitere Vorstellungen am 22.05.2017 und 03.03.2018 mit aehnlichem Beschwerdebild, jeweils folgenlos ausgeheilt, keine Arbeitsunfaehigkeit laenger als drei Tage.")
add_h2(doc, "2. Sportliche Aktivitaet")
add_p(doc, "Herr Moeller spielte bis 2018 in der Kreisliga Handball, seither nach eigenen Angaben nur noch gelegentlich Freizeitsport ohne Wettkampfbetrieb. Der Handballverein SG Trier-Ehrang bestaetigt auf Anfrage der Kanzlei, dass Herr Moeller seit der Saison 2018/2019 nicht mehr aktiv gemeldet ist.")
add_h2(doc, "3. Betriebsaerztliche Vorsorgeuntersuchung 2024")
add_p(doc, "Die turnusmaessige Vorsorgeuntersuchung durch die Betriebsaerztin Dr. Swetlana Iwanowa am 11.03.2024 attestiert uneingeschraenkte Tauglichkeit fuer die Taetigkeit als Lagerleiter einschliesslich Hebe- und Tragetaetigkeiten bis 15 Kilogramm, keine Einschraenkung der Schulterfunktion dokumentiert.")
add_h2(doc, "4. Fehlzeitenauswertung")
add_p(doc, "Nach der Personalakte gab es zwischen 2019 und dem Unfalltag keine einzige krankheitsbedingte Fehlzeit wegen Schulterbeschwerden. Die letzte schulterbezogene Arbeitsunfaehigkeit lag mehr als sieben Jahre zurueck.")
add_h2(doc, "5. Bedeutung fuer die Kausalitaetsfrage")
add_p(doc, "Die Zusammenstellung soll den Vorschaden weder verschweigen noch ueberzeichnen, sondern die Beschwerdefreiheit im Alltag und Beruf in den Jahren vor dem Unfall dokumentieren, um dem Sachverstaendigen und dem Gericht eine belastbare Tatsachengrundlage fuer die Abgrenzung von Vorschaden und Unfallfolge zu liefern.")
add_formathinweis(doc)
save(doc, BASE + "29_vorschadenshistorie_ausfuehrlich.docx")

print("Teil 6a fertig")
