import sys
sys.path.insert(0, "/home/user/workspace/legal-work/target/scripts/_tmp_gen")
from docx_helper import new_document, add_title, add_h2, add_h3, add_p, add_letterhead, add_table, add_formathinweis, save

BASE = "/home/user/workspace/legal-work/target/testakten/sozialrecht-elektrorollstuhl-koerner-oldenburg/"

HAUSARZT = ["Hausarztpraxis Dr. Ferdinand Stahlmann", "Donnerschweer Strasse 44, 26123 Oldenburg"]
NEURO = ["Neurologische Praxis am Pferdemarkt", "Dr. Elisabeth Radtke, Fachaerztin fuer Neurologie", "Pferdemarkt 12, 26121 Oldenburg"]
ERGO = ["Ergotherapie Nordwest", "Praxis fuer Ergotherapie, Melanie Bruns", "Nadorster Strasse 60, 26123 Oldenburg"]
PHYSIO = ["Physiotherapie Am Stadtwall", "Praxis Timo Elsholz", "Stau 15, 26122 Oldenburg"]

# 17 - Aerztliche Verordnung komplett ausformuliert
doc = new_document()
add_title(doc, "Aerztliche Verordnung, vollstaendig ausformuliert")
add_letterhead(doc, HAUSARZT)
add_p(doc, "Verordnung vom 16.05.2026 fuer Herrn Heinz Koerner, geboren 03.02.1948, wohnhaft Donnerschweer Strasse 112, 26123 Oldenburg.")
add_h2(doc, "1. Diagnosen nach ICD-10")
add_table(doc, ["ICD-10", "Diagnose"], [
    ["M48.06", "Spinalkanalstenose, Lumbalbereich"],
    ["G63.2", "Diabetische Polyneuropathie"],
    ["Z96.641", "Zustand nach Hueft-Totalendoprothese links"],
    ["R26.81", "Gangunsicherheit"],
    ["E11.90", "Diabetes mellitus Typ 2 ohne Komplikationen, entgleist mit Folgeschaeden anderenorts kodiert"],
])
add_h2(doc, "2. Verordnete Hilfsmittelversorgung")
add_p(doc, "Verordnet wird ein Elektrorollstuhl, kompakte Innenraum- und Nahbereichsausfuehrung, mit Kippschutz, gedrosselter Geschwindigkeit und Fahrtraining. Hilfsmittelnummer nach Produktgruppe 18 des Hilfsmittelverzeichnisses.")
add_h2(doc, "3. Begruendung des Mobilitaetsverlusts")
add_p(doc, "Herr Koerner kann im Innenbereich nur wenige Schritte mit Unterarmgehstuetze zuruecklegen, danach droht Sturzgefahr durch die diabetische Polyneuropathie mit vermindertem Gefuehl in beiden Fuessen. Der Rollator bietet auf ebener Strecke im Hausflur begrenzte Sicherheit, ist aber auf dem unebenen Gehweg vor dem Haus und beim Ueberqueren der Bordsteinkante nicht ausreichend sicher nutzbar. Ein manueller Rollstuhl kann von Herrn Koerner wegen eingeschraenkter Schulterkraft nach der Hueftoperation nicht selbststaendig angetrieben werden.")
add_h2(doc, "4. Behandlungsziel")
add_p(doc, "Ziel der Versorgung ist die Wiederherstellung einer selbststaendigen Mobilitaet im Nahbereich der Wohnung, insbesondere fuer Arztbesuche, Apothekenwege und den Weg zum Briefkasten, ohne durchgehende Angewiesenheit auf eine Begleitperson.")
add_h2(doc, "5. Dringlichkeit")
add_p(doc, "Angesichts wiederholter Stuerze in den letzten zwoelf Monaten und der zunehmenden sozialen Isolation wird eine zeitnahe Bearbeitung des Antrags dringend angeraten.")
add_formathinweis(doc)
save(doc, BASE + "17_aerztliche_verordnung_vollstaendig.docx")

# 18 - Detaillierter Facharztbericht Neurologie
doc = new_document()
add_title(doc, "Detaillierter Facharztbericht Neurologie")
add_letterhead(doc, NEURO)
add_h2(doc, "1. Untersuchungsdaten")
add_p(doc, "Untersuchung am 17.05.2026 durch Dr. Elisabeth Radtke, Fachaerztin fuer Neurologie, im Rahmen der Abklaerung der Gangstoerung und Sturzneigung.")
add_h2(doc, "2. Neurologischer Befund")
add_p(doc, "Deutlich reduzierte Vibrationsempfindung beidseits distal betont, abgeschwaechte Achillessehnenreflexe beidseits, positiver Romberg-Test mit Fallneigung nach hinten. Gangbild kleinschrittig, breitbasig, mit deutlich verlaengerter Standphase.")
add_h2(doc, "3. Elektrophysiologische Zusatzdiagnostik")
add_p(doc, "Nervenleitgeschwindigkeitsmessung bestaetigt eine sensomotorische Polyneuropathie beider Beine, vereinbar mit der bekannten diabetischen Genese. Die Befunde erklaeren die verminderte Standfestigkeit und die erhoehte Sturzgefahr insbesondere auf unebenem Untergrund.")
add_h2(doc, "4. Funktionelle Einschaetzung")
add_p(doc, "Die Gehstrecke ohne Hilfsmittel liegt unter 10 Metern, mit Unterarmgehstuetze bei kontrollierten Bedingungen bei etwa 15 Metern, jedoch mit deutlich erhoehtem Sturzrisiko bei Richtungswechseln oder Bodenunebenheiten. Aus neurologischer Sicht ist die vorhandene Restgehfaehigkeit fuer eine sichere Alltagsmobilitaet im Aussenbereich nicht ausreichend.")
add_h2(doc, "5. Fachaerztliche Empfehlung")
add_p(doc, "Aus neurologischer Sicht wird eine Versorgung mit einem sturzsicheren, selbststaendig zu bedienenden Mobilitaetshilfsmittel fuer den Nahbereich empfohlen. Ein Elektrorollstuhl mit Kippschutz und gedrosselter Geschwindigkeit erscheint geeignet, sofern ein Fahrtraining die kognitive und motorische Eignung bestaetigt.")
add_formathinweis(doc)
save(doc, BASE + "18_facharztbericht_neurologie_detailliert.docx")

# 19 - Ergotherapeutischer Bericht
doc = new_document()
add_title(doc, "Ergotherapeutischer Bericht")
add_letterhead(doc, ERGO)
add_h2(doc, "1. Behandlungsauftrag")
add_p(doc, "Ergotherapeutische Befunderhebung im Auftrag des Hausarztes zur Beurteilung der Alltagskompetenz und Handlungsfaehigkeit von Herrn Heinz Koerner, Behandlung vom 20.05.2026 bis 03.06.2026, insgesamt vier Termine.")
add_h2(doc, "2. Befunderhebung Alltagsaktivitaeten")
add_p(doc, "Transfer Bett zu Rollstuhl gelingt mit Anleitung und Haltegriff, benoetigt jedoch mehr Zeit als altersueblich. Greiffunktion beider Haende eingeschraenkt durch verminderte Sensibilitaet, feinmotorische Aufgaben wie das Bedienen eines Schluessels gelingen verlangsamt.")
add_h2(doc, "3. Beobachtung im hauslichen Umfeld")
add_p(doc, "Beim Hausbesuch am 27.05.2026 zeigte sich, dass Herr Koerner die Wohnungstuer nur mit Muehe selbststaendig oeffnen kann, wenn er sich gleichzeitig am Rollator festhalten muss. Die Kuechenarbeitsflaeche ist im Stehen nur kurzzeitig nutzbar.")
add_h2(doc, "4. Einschaetzung zur Hilfsmittelnutzung")
add_p(doc, "Ein Elektrorollstuhl wuerde die Haende fuer Greif- und Bedienaufgaben freihalten, waehrend Gehstock und Rollator beide Haende zur Stabilisierung binden. Dies ist fuer die Verrichtung alltaeglicher Handlungen wie Tueroeffnen, Briefkasten leeren oder Einkaufstasche tragen von Bedeutung.")
add_h2(doc, "5. Empfehlung")
add_p(doc, "Aus ergotherapeutischer Sicht wird die Versorgung mit einem Elektrorollstuhl befuerwortet, verbunden mit einem strukturierten Bedienungstraining ueber vier bis sechs Einheiten.")
add_formathinweis(doc)
save(doc, BASE + "19_ergotherapeutischer_bericht.docx")

# 20 - Physiotherapeutischer Bericht
doc = new_document()
add_title(doc, "Physiotherapeutischer Bericht")
add_letterhead(doc, PHYSIO)
add_h2(doc, "1. Behandlungsverlauf")
add_p(doc, "Physiotherapeutische Behandlung seit Januar 2026, zweimal woechentlich, Schwerpunkt Gangschulung, Gleichgewichtstraining und Kraeftigung der Beinmuskulatur nach Hueft-TEP links.")
add_h2(doc, "2. Aktueller Trainingsstand")
add_p(doc, "Trotz regelmaessiger Uebungsbehandlung konnte die Gehstrecke in den letzten sechs Monaten nicht wesentlich gesteigert werden. Die Standsicherheit bleibt durch die diabetische Polyneuropathie limitiert, das Sturzrisiko wird durch Uebungen nur bedingt reduziert.")
add_h2(doc, "3. Sturzereignisse im Behandlungszeitraum")
add_p(doc, "Nach Angaben des Patienten kam es im Behandlungszeitraum zu drei Stuerzen, davon zwei im Wohnungsflur und einer auf dem Gehweg vor dem Haus, jeweils ohne schwere Verletzungsfolgen, jedoch mit zunehmender Sturzangst.")
add_h2(doc, "4. Physiotherapeutische Einschaetzung")
add_p(doc, "Eine weitere Verbesserung der Gehfaehigkeit ueber das aktuelle Niveau hinaus ist nach fachlicher Einschaetzung nur eingeschraenkt zu erwarten, da die zugrunde liegende Polyneuropathie nicht reversibel ist. Die Fortfuehrung der Physiotherapie dient dem Erhalt der Restmobilitaet, ersetzt aber keine geeignete Hilfsmittelversorgung fuer den Nahbereich ausserhalb der Wohnung.")
add_formathinweis(doc)
save(doc, BASE + "20_physiotherapeutischer_bericht.docx")

print("Oldenburg Teil 1 fertig")
