import sys
sys.path.insert(0, "/home/user/workspace/legal-work/target/scripts/_tmp_gen")
from docx_helper import new_document, add_title, add_h2, add_h3, add_p, add_letterhead, add_table, add_formathinweis, save

BASE = "/home/user/workspace/legal-work/target/testakten/unfallversicherung-arbeitsunfall-lagerleiter-sturz-trier/"
BG = ["Berufsgenossenschaft Handel und Warenlogistik", "Bezirksverwaltung Trier", "Loebstrasse 22, 54292 Trier", "Aktenzeichen: BGHW-2026-350118-MOELLER"]

# 31 - Berufsgenossenschaftliche Reha-Empfehlung
doc = new_document()
add_title(doc, "Berufsgenossenschaftliche Reha-Empfehlung")
add_letterhead(doc, BG)
add_p(doc, "Erstellt vom Reha-Management der Berufsgenossenschaft am 30.06.2026, unter dem ausdruecklichen Vorbehalt der Anerkennung als Arbeitsunfall.")
add_h2(doc, "1. Ausgangslage")
add_p(doc, "Nach dem Bericht der BG Klinik Ludwigshafen vom 22.06.2026 besteht ein relevantes Kraftdefizit der rechten Schulter, das eine Rueckkehr auf den bisherigen, koerperlich anspruchsvollen Arbeitsplatz als Lagerleiter derzeit erschwert.")
add_h2(doc, "2. Empfohlene Massnahmen")
add_p(doc, "Empfohlen werden eine stufenweise Wiedereingliederung nach dem Hamburger Modell ueber acht Wochen, begleitende ambulante Physiotherapie zweimal woechentlich sowie eine ergonomische Arbeitsplatzberatung durch den technischen Aufsichtsdienst der Berufsgenossenschaft.")
add_h2(doc, "3. Zeitplan")
add_table(doc, ["Phase", "Zeitraum", "Belastung"], [
    ["Wiedereingliederung Stufe 1", "August 2026", "vier Stunden taeglich, keine Hebetaetigkeit"],
    ["Wiedereingliederung Stufe 2", "September 2026", "sechs Stunden taeglich, Heben bis 5 Kilogramm"],
    ["Wiedereingliederung Stufe 3", "Oktober 2026", "volle Arbeitszeit, Heben bis 10 Kilogramm unter Beobachtung"],
])
add_h2(doc, "4. Vorbehalt")
add_p(doc, "Die Empfehlung wird ausdruecklich nur fuer den Fall ausgesprochen, dass die Anerkennung als Arbeitsunfall im Widerspruchs- oder Klageverfahren erfolgt. Bis dahin ruht die Umsetzung.")
add_formathinweis(doc)
save(doc, BASE + "31_bg_reha_empfehlung.docx")

print("Teil 7 fertig")
