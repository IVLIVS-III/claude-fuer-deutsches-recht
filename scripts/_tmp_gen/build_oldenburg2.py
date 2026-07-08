import sys
sys.path.insert(0, "/home/user/workspace/legal-work/target/scripts/_tmp_gen")
from docx_helper import new_document, add_title, add_h2, add_h3, add_p, add_letterhead, add_table, add_formathinweis, save

BASE = "/home/user/workspace/legal-work/target/testakten/sozialrecht-elektrorollstuhl-koerner-oldenburg/"
SANITAETSHAUS = ["RehaTechnik Albrecht GmbH", "Fachhandel fuer Rehabilitationstechnik", "Cloppenburger Strasse 302, 26133 Oldenburg"]
KASSE = ["Weser-Ems Gesundheitskasse", "Leistungsabteilung Hilfsmittel", "Huntestrasse 14, 26135 Oldenburg"]
KANZLEI = ["Kanzlei am Pferdemarkt", "Rechtsanwaeltin Beate Sonnenschein, Fachanwaeltin fuer Sozialrecht", "Pferdemarkt 5, 26121 Oldenburg"]

# 21 - Wohnungs-Rundgang-Protokoll mit Skizze
doc = new_document()
add_title(doc, "Wohnungs-Rundgang-Protokoll mit Skizzenbeschreibung")
add_letterhead(doc, SANITAETSHAUS)
add_h2(doc, "1. Termin und Anwesende")
add_p(doc, "Hausbesuch am 19.05.2026 durch den Rehatechniker Jonas Wiechmann. Anwesend waren Herr Koerner und seine Tochter Frau Dagmar Lindqvist.")
add_h2(doc, "2. Raumbeschreibung mit Massangaben")
add_table(doc, ["Bereich", "Masse und Beschaffenheit", "Bewertung fuer Elektrorollstuhl"], [
    ["Hauseingang", "Zwei Stufen a 16 cm, kein Handlauf", "Rampe oder Treppenlift erforderlich, gesondert zu pruefen"],
    ["Treppenhaus zur Wohnung im ersten Obergeschoss", "Breite 110 cm, kein Aufzug", "Elektrorollstuhl bleibt im Erdgeschoss, Transferloesung noetig"],
    ["Wohnungsflur", "Breite 95 cm, ein Wandvorsprung", "ausreichend fuer kompakten Elektrorollstuhl"],
    ["Wohnzimmer", "18 Quadratmeter, ein Teppich mit erhoehter Kante", "Teppichkante zu entfernen oder abzuflachen"],
    ["Kueche", "schmal, Arbeitsflaeche 60 cm Durchgangsbreite", "eingeschraenkt befahrbar, Rangieren erschwert"],
    ["Badezimmer", "Tuerbreite 70 cm, keine Schwellenfreiheit", "nicht mit Elektrorollstuhl befahrbar, Rollator im Bad erforderlich"],
])
add_h2(doc, "3. Skizzenbeschreibung")
add_p(doc, "Die beigefuegte Handskizze (siehe jpg/wohnungsskizze_koerner.jpg) zeigt den Grundriss der Wohnung mit eingezeichneten Wegstrecken vom Hauseingang ueber das Treppenhaus zur Wohnungstuer sowie die Innenwege zwischen Wohnzimmer, Kueche, Schlafzimmer und Bad. Die kritischen Engstellen bei Kueche und Bad sind rot markiert, die fuer den Elektrorollstuhl geeigneten Bereiche gruen.")
add_h2(doc, "4. Aussenbereich")
add_p(doc, "Der Gehweg vor dem Haus ist asphaltiert, weist jedoch nach 40 Metern eine abgesenkte, aber leicht schraege Bordsteinkante zur Querungshilfe auf. Die naechste Apotheke liegt in etwa 180 Metern Entfernung, der Hausarzt in etwa 600 Metern.")
add_h2(doc, "5. Fazit des Rehatechnikers")
add_p(doc, "Fuer den Innenbereich der Wohnung sowie den unmittelbaren Nahbereich nach Ueberwindung der Eingangsstufen ist ein kompakter Elektrorollstuhl technisch geeignet. Die beiden Eingangsstufen erfordern zusaetzlich eine mobile Rampe oder einen baulichen Umbau, der gesondert bei der Pflegekasse zu beantragen waere.")
add_formathinweis(doc)
save(doc, BASE + "21_wohnungsrundgang_protokoll_mit_skizze.docx")

# 22 - Kostenvoranschlag komplett mit Alternativen
doc = new_document()
add_title(doc, "Kostenvoranschlag mit Alternativen, vollstaendige Fassung")
add_letterhead(doc, SANITAETSHAUS)
add_p(doc, "Kostenvoranschlag Nr. RTA-2026-3381 vom 20.05.2026")
add_h2(doc, "1. Hauptangebot: Kompakter Elektrorollstuhl")
add_table(doc, ["Position", "Bezeichnung", "Einzelpreis EUR"], [
    ["1", "Elektrorollstuhl Innenraum- und Nahbereichsklasse B", "8990.00"],
    ["2", "Kippschutz hinten", "310.00"],
    ["3", "Zusatzakku fuer erweiterte Reichweite", "540.00"],
    ["4", "Fahrtraining, sechs Einheiten", "480.00"],
    ["5", "Anpassung Sitzsystem", "670.00"],
])
add_p(doc, "Gesamtsumme Hauptangebot: 10990.00 EUR")
add_h2(doc, "2. Alternative 1: Aufsatz-Antrieb fuer vorhandenen Faltrollstuhl")
add_p(doc, "Ein elektrischer Zusatzantrieb, der auf den bereits vorhandenen manuellen Faltrollstuhl aufgesetzt wird, kaeme auf etwa 4200.00 EUR. Diese Loesung wuerde die Anschaffung eines komplett neuen Rollstuhls vermeiden, ist jedoch technisch nur eingeschraenkt fuer die schmalen Innenraeume der Wohnung geeignet, da sich die Gesamtbreite des Systems um zusaetzliche 12 Zentimeter vergroessert.")
add_h2(doc, "3. Alternative 2: Standard-Elektrorollstuhl ohne Sonderausstattung")
add_p(doc, "Ein einfacheres Modell ohne Zusatzakku und ohne individuelle Sitzanpassung wuerde etwa 6100.00 EUR kosten, wuerde nach fachlicher Einschaetzung des Sanitaetshauses jedoch die notwendige Reichweite fuer den taeglichen Weg zur Apotheke und zum Hausarzt nicht zuverlaessig gewaehrleisten.")
add_h2(doc, "4. Vergleich mit dem von der Kasse favorisierten Standard-Faltrollstuhl")
add_p(doc, "Ein Standard-Faltrollstuhl aus dem Vertragssortiment der Krankenkasse liegt bei etwa 740.00 EUR, setzt aber durchgehend eine schiebende Begleitperson voraus und stellt keine selbststaendige Mobilitaet her.")
add_h2(doc, "5. Empfehlung des Sanitaetshauses")
add_p(doc, "Aus fachlicher Sicht wird das Hauptangebot empfohlen, da es die einzige Option ist, die sowohl den raeumlichen Anforderungen der Wohnung als auch der erforderlichen Reichweite fuer den Nahbereich gerecht wird.")
add_formathinweis(doc)
save(doc, BASE + "22_kostenvoranschlag_mit_alternativen_vollstaendig.docx")

# 23 - Vergleichsangebot Kasse Standardmodell
doc = new_document()
add_title(doc, "Vergleichsangebot der Krankenkasse, Standardmodell")
add_letterhead(doc, KASSE)
add_p(doc, "Schreiben vom 09.06.2026 an das Sanitaetshaus RehaTechnik Albrecht GmbH, zur Kenntnis an den Versicherten.")
add_h2(doc, "1. Angebot der Kasse")
add_p(doc, "Die Weser-Ems Gesundheitskasse bietet im Rahmen ihres Vertragssortiments einen Standard-Faltrollstuhl zum Vertragspreis von 740.00 EUR sowie ergaenzend eine Unterarmgehstuetze zum Preis von 38.00 EUR an. Beide Hilfsmittel seien im Hilfsmittelverzeichnis unter Produktgruppe 18 und 22 gelistet und aus Sicht der Kasse ausreichend.")
add_h2(doc, "2. Begruendung der Kasse")
add_p(doc, "Nach der Stellungnahme des Medizinischen Dienstes vom 05.06.2026 bestehe eine Restgehfaehigkeit, die in Verbindung mit einem Rollator und einem Faltrollstuhl fuer Begleitwege ausreiche. Die Kasse verweist auf das Wirtschaftlichkeitsgebot nach Paragraf 12 SGB V.")
add_h2(doc, "3. Reaktion der Kanzlei")
add_p(doc, "Mit Schreiben vom 16.06.2026 weist die Kanzlei darauf hin, dass der Faltrollstuhl nach dem privaten Reha-Gutachten vom Versicherten nicht selbststaendig angetrieben werden kann und daher keine gleich geeignete Alternative darstellt. Das Vergleichsangebot wird ausdruecklich nicht angenommen.")
add_formathinweis(doc)
save(doc, BASE + "23_vergleichsangebot_kasse_standardmodell.docx")

# 24 - Zweitgutachten-Antrag
doc = new_document()
add_title(doc, "Antrag auf Einholung eines Zweitgutachtens")
add_letterhead(doc, KANZLEI)
add_p(doc, "An die Weser-Ems Gesundheitskasse, Leistungsabteilung Hilfsmittel, Schreiben vom 22.06.2026.")
add_h2(doc, "1. Antrag")
add_p(doc, "Namens des Herrn Heinz Koerner wird beantragt, vor abschliessender Entscheidung ueber den Widerspruch ein unabhaengiges Zweitgutachten einzuholen, das auf einer persoenlichen Untersuchung und einer praktischen Erprobung des beantragten Elektrorollstuhls im Wohnumfeld beruht.")
add_h2(doc, "2. Begruendung")
add_p(doc, "Die bisherige Stellungnahme des Medizinischen Dienstes beruht ausschliesslich auf Aktenlage, ohne eigene koerperliche Untersuchung, Gehprobe oder Erprobung der in Betracht kommenden Hilfsmittel. Demgegenueber stuetzt sich das private Gutachten von Reha-Kompetenz Nordwest auf eine mehrstuendige praktische Erprobung im tatsaechlichen Wohnumfeld. Angesichts dieser Diskrepanz erscheint eine erneute, unabhaengige Begutachtung sachgerecht.")
add_h2(doc, "3. Vorschlag zur Gutachterauswahl")
add_p(doc, "Es wird angeregt, einen von der Kasse und der Klaegerseite gemeinsam benannten Gutachter mit Erfahrung in der Hilfsmittelversorgung bei Polyneuropathie zu beauftragen, hilfsweise wird die gerichtliche Begutachtung im spaeteren Klageverfahren angeregt.")
add_h2(doc, "4. Reaktion der Kasse")
add_p(doc, "Die Kasse lehnt mit Schreiben vom 24.06.2026 die Einholung eines Zweitgutachtens im Verwaltungsverfahren ab und verweist auf die abschliessende Bearbeitung im Widerspruchsbescheid vom selben Tag.")
add_formathinweis(doc)
save(doc, BASE + "24_zweitgutachten_antrag.docx")

print("Oldenburg Teil 2 fertig")
