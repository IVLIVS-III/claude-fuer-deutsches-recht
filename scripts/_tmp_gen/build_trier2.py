import sys
sys.path.insert(0, "/home/user/workspace/legal-work/target/scripts/_tmp_gen")
from docx_helper import new_document, add_title, add_h2, add_h3, add_p, add_letterhead, add_table, add_formathinweis, save

BASE = "/home/user/workspace/legal-work/target/testakten/unfallversicherung-arbeitsunfall-lagerleiter-sturz-trier/"

KLINIK = [
    "Bruederkrankenhaus Trier",
    "Abteilung Unfallchirurgie und Orthopaedie",
    "Nordallee 1, 54292 Trier",
]

# 12 - Erste-Hilfe-Bericht Sicherheitsbeauftragter
doc = new_document()
add_title(doc, "Erste-Hilfe-Bericht der Sicherheitsbeauftragten")
add_letterhead(doc, ["MoselLogistik GmbH", "Arbeitssicherheit", "Hafenstrasse 28, 54293 Trier"])
add_h2(doc, "1. Angaben zur Ersthelferin")
add_p(doc, "Sicherheitsbeauftragte und Ersthelferin: Petra Winkelmann, Fachkraft fuer Arbeitssicherheit im Nebenamt, seit 2015 im Betrieb. Sie wurde um 6:43 Uhr per Funk alarmiert und traf um 6:45 Uhr an Rampe 4 ein.")
add_h2(doc, "2. Vorgefundene Situation")
add_p(doc, "Herr Moeller sass an der Rampenkante auf dem Hallenboden, hielt sich die rechte Schulter und wirkte laut Bericht blass und leicht desorientiert. Eine kleine Schuerfwunde am rechten Ellenbogen blutete leicht. Am Hinterkopf war eine geroetete Stelle ohne offene Wunde sichtbar.")
add_h2(doc, "3. Erste-Hilfe-Massnahmen")
add_p(doc, "Stabile Seitenlage wurde nicht angewendet, da der Mandant ansprechbar war. Die Schuerfwunde wurde mit einem Verbandpaeckchen aus dem Verbandskasten Halle C versorgt. Der rechte Arm wurde behelfsmaessig mit einem Dreiecktuch ruhiggestellt. Um 6:47 Uhr erfolgte die Alarmierung des Rettungsdienstes ueber die Notrufnummer 112.")
add_h2(doc, "4. Aussage des Verletzten gegenueber der Ersthelferin")
add_p(doc, "Frau Winkelmann notierte woertlich: 'Die Bruecke ist auf einmal durchgerutscht, ich konnte mich nicht mehr halten.' Diese Angabe wurde noch am selben Tag in das betriebliche Meldeblatt uebernommen.")
add_h2(doc, "5. Uebergabe an den Rettungsdienst")
add_p(doc, "Der Rettungsdienst traf um 6:58 Uhr ein und uebernahm die weitere Versorgung. Frau Winkelmann uebergab die Kurzangaben zum Unfallhergang muendlich an den Rettungsassistenten.")
add_formathinweis(doc)
save(doc, BASE + "12_erste_hilfe_bericht_sicherheitsbeauftragte.docx")

# 13 - Rettungsdienst-Protokoll
doc = new_document()
add_title(doc, "Rettungsdienstprotokoll, Auszug")
add_letterhead(doc, ["Rettungsdienst Trier-Saarburg", "Einsatzprotokoll Nr. RD-2026-04-03-0142"])
add_h2(doc, "1. Einsatzdaten")
add_table(doc, ["Feld", "Angabe"], [
    ["Alarmierung", "03.04.2026, 6:47 Uhr"],
    ["Eintreffen am Einsatzort", "03.04.2026, 6:58 Uhr"],
    ["Einsatzort", "MoselLogistik GmbH, Hafenstrasse 28, Rampe 4"],
    ["Uebergabe Krankenhaus", "03.04.2026, 7:34 Uhr, Bruederkrankenhaus Trier"],
])
add_h2(doc, "2. Erstbefund des Rettungsdienstes")
add_p(doc, "Patient ansprechbar, orientiert zu Person, Ort und Zeit. Glasgow Coma Scale 15. Angabe starker Schmerzen in der rechten Schulter mit deutlich eingeschraenkter Beweglichkeit. Kleine Schuerfwunde rechter Ellenbogen, geroetete druckschmerzhafte Stelle am Hinterkopf ohne neurologische Ausfaelle.")
add_h2(doc, "3. Vitalparameter")
add_table(doc, ["Zeit", "Puls", "Blutdruck", "SpO2"], [
    ["7:00 Uhr", "92", "138/86", "97 Prozent"],
    ["7:15 Uhr", "88", "134/82", "98 Prozent"],
    ["7:30 Uhr", "86", "132/80", "98 Prozent"],
])
add_h2(doc, "4. Massnahmen")
add_p(doc, "Anlage eines venoesen Zugangs, Schmerzmedikation nach Ruecksprache mit dem Notarzt, Ruhigstellung des rechten Arms mit Armschlinge, Immobilisation der Halswirbelsaeule mit Stiffneck aus Vorsicht wegen Kopfanprall, liegender Transport in die Notaufnahme.")
add_h2(doc, "5. Fremdanamnese laut Protokoll")
add_p(doc, "Betriebliche Ersthelferin gibt an, der Patient sei beim Loesen einer klemmenden Laderampe gestuerzt. Patient selbst bestaetigt gegenueber dem Rettungsdienst: 'Die Ueberladebruecke hat nachgegeben, ich bin nach vorne gefallen.'")
add_formathinweis(doc)
save(doc, BASE + "13_rettungsdienst_protokoll.docx")

# 14 - Krankenhaus-Aufnahmebericht und Verlaufsbericht
doc = new_document()
add_title(doc, "Krankenhaus-Aufnahmebericht und Verlaufsbericht")
add_letterhead(doc, KLINIK)
add_h2(doc, "1. Aufnahme")
add_p(doc, "Aufnahme in die Notaufnahme am 03.04.2026 um 7:34 Uhr durch den Rettungsdienst. Aufnehmender Arzt: Dr. Reiner Kauth, Durchgangsarzt. Diagnosen bei Aufnahme: Verdacht auf Rotatorenmanschettenruptur rechts, Schaedelprellung, Schuerfwunden rechter Ellenbogen.")
add_h2(doc, "2. Untersuchungsbefund")
add_p(doc, "Rechte Schulter druckschmerzhaft, aktive Abduktion nicht ueber 30 Grad moeglich, passive Beweglichkeit endgradig eingeschraenkt und schmerzhaft. Kein neurologisches Defizit im Bereich des Plexus brachialis. Kopf: reizlose Kopfschwarte, keine Kalottenstufe tastbar, Pupillen isokor und lichtreagibel.")
add_h2(doc, "3. Bildgebung am Aufnahmetag")
add_p(doc, "Roentgen Schulter rechts in zwei Ebenen: keine knoecherne Fraktur, keine Luxation, altersentsprechende AC-Gelenksveraenderungen. Craniales CT bei Verdacht auf Schaedel-Hirn-Trauma ersten Grades: keine intrakranielle Blutung, keine Kalottenfraktur.")
add_h2(doc, "4. Verlauf stationaer")
add_p(doc, "Stationaere Aufnahme zur Ueberwachung bei Kopfanprall vom 03.04.2026 bis 04.04.2026. Neurologische Kontrollen unauffaellig. Entlassung am 04.04.2026 mit ambulanter Weiterbehandlung, Terminvereinbarung MRT Schulter und Wiedervorstellung in der Unfallchirurgie.")
add_h2(doc, "5. Ambulanter Verlauf bis Operation")
add_p(doc, "Wiedervorstellung am 10.04.2026 nach MRT-Befund vom 09.04.2026. Bei bestaetigter Teilruptur der Supraspinatussehne mit zunehmenden Beschwerden und ausbleibender Besserung unter konservativer Behandlung wird die Indikation zur arthroskopischen Rekonstruktion gestellt. Aufklaerungsgespraech am 16.04.2026, Operationstermin 21.04.2026.")
add_formathinweis(doc)
save(doc, BASE + "14_krankenhaus_aufnahmebericht_verlauf.docx")

# 15 - OP-Bericht
doc = new_document()
add_title(doc, "Operationsbericht, Auszug")
add_letterhead(doc, KLINIK)
add_h2(doc, "1. Eingriffsdaten")
add_table(doc, ["Feld", "Angabe"], [
    ["Operationsdatum", "21.04.2026"],
    ["Operateur", "Dr. Felix Brandenburger, Oberarzt Unfallchirurgie"],
    ["Anaesthesie", "Interskalenaere Plexusblockade und Allgemeinanaesthesie"],
    ["Diagnose", "Teilruptur der Supraspinatussehne rechts, subacromiales Impingement"],
    ["Eingriff", "Arthroskopische Rotatorenmanschettennaht, subacromiale Dekompression"],
])
add_h2(doc, "2. Operativer Befund")
add_p(doc, "Intraoperativ zeigt sich eine partielle, gelenkseitige Ruptur der Supraspinatussehne mit frischem, blutig imbibiertem Randsaum, vereinbar mit einem akuten traumatischen Ereignis auf vorbestehender degenerativer Sehnenstruktur. Zusaetzlich maessige Bursitis subacromialis.")
add_h2(doc, "3. Operationsverlauf")
add_p(doc, "Arthroskopischer Zugang ueber Standardportale, Debridement der Rupturzone, transossaere Refixation mit zwei Fadenankern, subacromiale Dekompression mittels Acromioplastik. Intraoperativ kein Hinweis auf ausschliesslich degenerative Genese ohne akuten Anteil.")
add_h2(doc, "4. Postoperative Anordnung")
add_p(doc, "Ruhigstellung im Abduktionskissen fuer sechs Wochen, fruehfunktionelle Physiotherapie ab dem dritten postoperativen Tag nach festem Schema, Wiedervorstellung nach zwei Wochen zur Wundkontrolle.")
add_h2(doc, "5. Anmerkung zur Zusammenhangsfrage")
add_p(doc, "Der Operateur haelt in der Epikrise fest, dass der intraoperative Befund eine frische traumatische Komponente auf degenerativer Vorschaedigung zeige und die Ruptur ohne das Sturzereignis nach seiner Einschaetzung nicht in diesem Ausmass und Zeitpunkt aufgetreten waere.")
add_formathinweis(doc)
save(doc, BASE + "15_op_bericht_schulter.docx")

print("Teil 2 fertig")
