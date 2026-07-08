import sys, os
sys.path.insert(0, "/home/user/workspace/legal-work/target/scripts/_tmp_gen")
from docx_helper import new_document, add_title, add_h2, add_h3, add_p, add_letterhead, add_table, add_formathinweis, save

BASE = "/home/user/workspace/legal-work/target/testakten/sozialrecht-elektrorollstuhl-koerner-oldenburg"

GERICHT = [
    "Sozialgericht Oldenburg",
    "Kammer für Krankenversicherungssachen",
    "Klingenbergstraße 4, 26133 Oldenburg",
]

# Datei 15 ersetzen: statt fertiger Urteilsentwuerfe mit Entscheidungsweichen nur die
# gerichtliche Zwischenverfuegung mit offenen Fragen, ohne Ergebnis vorwegzunehmen.
old15 = f"{BASE}/15_urteilsentwurf_zwei_varianten.docx"
if os.path.exists(old15):
    os.remove(old15)

doc = new_document()
add_title(doc, "Terminsverfügung und Hinweise zur mündlichen Verhandlung")
add_letterhead(doc, GERICHT)
add_p(doc, "Aktenzeichen: S 12 KR 188/26", align="right")
add_p(doc, "Oldenburg, den 25.09.2026", align="right")
doc.add_paragraph()
add_p(doc, "In dem Rechtsstreit Körner gegen Weser-Ems Gesundheitskasse wird Termin zur mündlichen Verhandlung bestimmt auf:")
add_p(doc, "Donnerstag, den 22.10.2026, 10.30 Uhr, Sitzungssaal 3.")
add_h2(doc, "Hinweise der Kammer")
add_p(doc, "Das eingeholte Sachverständigengutachten vom 16.09.2026 liegt den Beteiligten vor. Die Kammer weist darauf hin, dass sich die Entscheidung maßgeblich auf die dort getroffenen Feststellungen zur Gehstrecke mit Rollator, zur Belastbarkeit beim manuellen Rollstuhlantrieb und zum Ergebnis des Fahrversuchs mit dem Elektrorollstuhl stützen wird.")
add_p(doc, "Die Beteiligten erhalten Gelegenheit, bis zum Termin ergänzend vorzutragen, insbesondere zu der Frage, ob und in welchem Umfang die im Gutachten beschriebene Erschöpfung bei Nutzung des manuellen Rollstuhls eine dauerhafte, alltagstaugliche Versorgung ausschließt.")
add_p(doc, "Ein Vergleichsvorschlag wurde bislang von keiner Seite unterbreitet. Die Kammer regt an, vor dem Termin zu prüfen, ob eine gütliche Einigung, etwa durch eine testweise Versorgung mit Rückgaberecht, in Betracht kommt.")
add_h2(doc, "Ladung der Beteiligten")
add_p(doc, "Geladen werden der Kläger persönlich sowie ein Vertreter der Beklagten mit Entscheidungsbefugnis. Der Sachverständigen wird anheimgestellt, an der Verhandlung teilzunehmen, falls Rückfragen zum Gutachten zu erwarten sind.")
add_formathinweis(doc)
save(doc, f"{BASE}/15_terminsverfuegung_und_hinweise.docx")

# Datei 16 ersetzen: Fristenblatt und Anlagenverzeichnis bleiben (reine Verwaltungsangaben),
# aber die Klaeger-vs-Kasse-Argumentmatrix (Antwortmatrix) entfernen. Stattdessen ein
# neutrales Anlagenverzeichnis mit Fristen, ohne Wertung.
old16 = f"{BASE}/16_fristsachen_anlagen_und_pruefmatrix.docx"
if os.path.exists(old16):
    os.remove(old16)

doc = new_document()
add_title(doc, "Fristenblatt und Anlagenverzeichnis")
add_h2(doc, "Fristenblatt")
add_table(doc, ["Frist", "Berechnung", "Ergebnis"], [
    ["Widerspruch gegen Ausgangsbescheid", "Bescheid 10.06.2026, Widerspruch 20.06.2026", "fristgerecht"],
    ["Klage gegen Widerspruchsbescheid", "Zugang 26.06.2026, Monatsfrist", "Ende Montag, 27.07.2026"],
    ["Kanzlei-Wiedervorlage", "sofort nach Mandatierung", "03.07.2026"],
    ["MD-Akte anfordern", "Akteneinsicht Verwaltungsvorgang", "sofort"],
    ["Facharzt-Ergaenzung", "kurze Stellungnahme zu Hilfsmittelalternativen", "bis 10.07.2026"],
    ["Beweisbeschluss Rueckfragen", "Frist laut gerichtlichem Hinweis", "zwei Wochen ab Zustellung"],
    ["Terminsvorbereitung", "vor mündlicher Verhandlung", "bis 15.10.2026"],
])
add_h2(doc, "Anlagenverzeichnis Klägerseite")
add_table(doc, ["Anlage", "Dokument"], [
    ["K 1", "Bescheid Weser-Ems Gesundheitskasse vom 10.06.2026"],
    ["K 2", "Widerspruch Heinz Körner vom 20.06.2026"],
    ["K 3", "Widerspruchsbescheid vom 24.06.2026"],
    ["K 4", "Überweisung und Hilfsmittelverordnung Dr. Stahlmann"],
    ["K 5", "Facharztbericht Dr. Radtke vom 17.05.2026"],
    ["K 6", "Eigenschilderung Alltag und Wege"],
    ["K 7", "Wohnumfeldbericht RehaTechnik Albrecht"],
    ["K 8", "Kostenvoranschlag RehaTechnik Albrecht vom 20.05.2026"],
    ["K 9", "MD-Stellungnahme vom 05.06.2026"],
    ["K 10", "Privates Reha-Gutachten vom 18.06.2026"],
    ["K 11", "E-Mail Tochter vom 27.06.2026"],
    ["K 12", "Gerichtliches Sachverständigengutachten vom 16.09.2026"],
])
add_h2(doc, "Offene Arbeitspunkte")
add_p(doc, "Vor dem Verhandlungstermin sind noch die ergänzende Stellungnahme des Facharztes zur Belastbarkeit beim manuellen Rollstuhlantrieb einzuholen und die Reisekosten des Sachverständigen abzurechnen. Die Kanzlei prüft zudem, ob eine testweise Versorgung mit Rückgaberecht als Vergleichsgrundlage angeboten werden kann.")
add_formathinweis(doc)
save(doc, f"{BASE}/16_fristenblatt_und_anlagenverzeichnis.docx")

print("fertig 15/16 ersetzt")
