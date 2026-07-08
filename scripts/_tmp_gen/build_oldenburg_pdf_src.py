import sys
sys.path.insert(0, "/home/user/workspace/legal-work/target/scripts/_tmp_gen")
from docx_helper import new_document, add_title, add_h2, add_p, add_letterhead, add_table, add_formathinweis, save

BASE = "/home/user/workspace/legal-work/target/testakten/sozialrecht-elektrorollstuhl-koerner-oldenburg"

SANITAETSHAUS = [
    "RehaTechnik Albrecht GmbH",
    "Sanitaetshaus und Rehatechnik",
    "Nadorster Straße 145, 26123 Oldenburg",
    "Telefon 0441 88 77 20, Telefax 0441 88 77 29",
]

doc = new_document()
add_title(doc, "Technisches Datenblatt Elektrorollstuhl Kompaktmodell")
add_letterhead(doc, SANITAETSHAUS)
add_p(doc, "Anlage zum Kostenvoranschlag vom 20.05.2026", align="right")
add_h2(doc, "Technische Daten")
add_table(doc, ["Merkmal", "Wert"], [
    ["Modell", "Kompakt-Elektrorollstuhl Innen- und Nahbereich"],
    ["Gesamtbreite", "58 Zentimeter"],
    ["Wendekreis", "95 Zentimeter"],
    ["Hoechstgeschwindigkeit", "6 Kilometer pro Stunde, stufenlos regulierbar"],
    ["Reichweite", "bis 25 Kilometer je Akkuladung"],
    ["Zuladung", "bis 130 Kilogramm"],
    ["Sitzsystem", "hoehenverstellbar, mit Rueckenverstellung"],
    ["Steuerung", "Joystick rechts, alternativ Kinnsteuerung nachruestbar"],
    ["Zerlegbarkeit", "Sitzeinheit und Antriebseinheit trennbar fuer Transport"],
])
add_h2(doc, "Einsatzbereich laut Hersteller")
add_p(doc, "Das Modell ist fuer den Innenbereich und fuer befestigte Wege im Nahbereich der Wohnung ausgelegt. Es ist nicht fuer laengere Ueberlandfahrten oder unbefestigtes Gelaende vorgesehen. Der geringe Wendekreis ermoeglicht die Nutzung in Fluren und Tueroeffnungen ab 80 Zentimeter Breite.")
add_formathinweis(doc)
save(doc, "/tmp/oldenburg_datenblatt.docx")
