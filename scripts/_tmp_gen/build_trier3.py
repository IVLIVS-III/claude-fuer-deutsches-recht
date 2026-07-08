import sys
sys.path.insert(0, "/home/user/workspace/legal-work/target/scripts/_tmp_gen")
from docx_helper import new_document, add_title, add_h2, add_h3, add_p, add_letterhead, add_table, add_formathinweis, save

BASE = "/home/user/workspace/legal-work/target/testakten/unfallversicherung-arbeitsunfall-lagerleiter-sturz-trier/"

RADIOLOGIE = ["Radiologische Praxis am Domfreihof", "Dr. Simone Hage, Fachaerztin fuer Radiologie", "Domfreihof 9, 54290 Trier"]
BGKLINIK = ["BG Klinik Ludwigshafen", "Abteilung Unfallchirurgische Rehabilitation", "Ludwig-Guttmann-Strasse 13, 67071 Ludwigshafen am Rhein"]

# 16 - Roentgenbefunde mehrere
doc = new_document()
add_title(doc, "Roentgenbefunde im Verlauf, mit radiologischer Bewertung")
add_letterhead(doc, RADIOLOGIE)
add_h2(doc, "1. Roentgen Schulter rechts, 03.04.2026")
add_p(doc, "Zwei Ebenen, angefertigt im Bruederkrankenhaus Trier am Aufnahmetag. Kein Frakturnachweis, keine Luxation. Acromioclaviculargelenk mit geringer Arthrose, Humeruskopf regelrecht positioniert. Beurteilung: keine knoecherne Verletzung, Weichteilbefund radiologisch nicht sicher beurteilbar.")
add_h2(doc, "2. Kontrollroentgen, 12.05.2026")
add_p(doc, "Drei Wochen postoperativ. Fadenanker regelrecht lagegetreu, keine sekundaere Dislokation, Acromioplastik-Areal reizlos. Beurteilung: postoperativer Verlauf ohne Auffaelligkeiten.")
add_h2(doc, "3. Vergleich mit Voraufnahmen")
add_p(doc, "Aeltere Roentgenaufnahmen der Schulter liegen nicht vor, da 2016 bis 2018 keine Bildgebung erfolgte. Dr. Hage weist ausdruecklich darauf hin, dass ein bildgebender Vorbefund zum direkten Vergleich fehlt und die Bewertung des Vorschadens daher auf der MRT-Morphologie und der Anamnese beruhen muss.")
add_h2(doc, "4. Zusammenfassende radiologische Einschaetzung")
add_p(doc, "Nach Aktenlage und Bildbefund haelt Dr. Hage eine ausschliesslich degenerative Erklaerung fuer nicht zwingend, da das im MRT nachgewiesene Knochenmarkoedem am Tuberculum majus typischerweise Ausdruck einer akuten knoechernen Belastungsreaktion und kein Zeichen einer chronisch-degenerativen Veraenderung ist.")
add_formathinweis(doc)
save(doc, BASE + "16_roentgenbefunde_verlauf.docx")

# 17 - Reha-Verlaufsbericht BG-Klinik
doc = new_document()
add_title(doc, "Reha-Verlaufsbericht BG-Klinik")
add_letterhead(doc, BGKLINIK)
add_h2(doc, "1. Aufnahme zur Anschlussheilbehandlung")
add_p(doc, "Aufnahme am 02.06.2026 zur dreiwoechigen stationaeren Anschlussheilbehandlung nach arthroskopischer Rotatorenmanschettennaht. Behandelnder Oberarzt: Dr. Katja Vollmer.")
add_h2(doc, "2. Therapieverlauf")
add_p(doc, "Physiotherapeutische Bewegungsschule, Ergotherapie zur Kraeftigung des Schultergueftels, Ergometertraining, arbeitsplatzbezogenes Belastungstraining mit Simulation von Hebe- und Zugbewegungen wie im Lagerbetrieb. Zwischenbefund nach zwei Wochen: aktive Abduktion bis 90 Grad, weiterhin endgradiges Kraftdefizit.")
add_h2(doc, "3. Sozialmedizinische Epikrise")
add_p(doc, "Die Klinik stuft das Ereignis vom 03.04.2026 aus behandlungsseitiger Sicht als wesentliche Ursache der aktuellen Funktionsstoerung ein, weist aber auf die vorbestehende degenerative Komponente als mitwirkenden Faktor hin. Fuer die sozialmedizinische Leistungsbeurteilung sei die Abgrenzung zwischen Unfallfolge und Vorschaden gutachterlich zu klaeren.")
add_h2(doc, "4. Entlassungsempfehlung")
add_p(doc, "Entlassung am 22.06.2026 mit ambulanter Fortfuehrung der Physiotherapie zweimal woechentlich, stufenweiser Wiedereingliederung nicht vor August 2026, keine Hebebelastung ueber 5 Kilogramm mit dem rechten Arm bis auf Weiteres.")
add_formathinweis(doc)
save(doc, BASE + "17_reha_verlaufsbericht_bg_klinik.docx")

# 18 - Berufshilfe-Antrag
doc = new_document()
add_title(doc, "Antrag auf Leistungen zur Berufshilfe")
add_letterhead(doc, ["Kanzlei Lindenhof und Partner mbB", "Domfreihof 6, 54290 Trier"])
add_h2(doc, "1. Antragsteller und Adressat")
add_p(doc, "Antragsteller: Karsten Moeller, vertreten durch die unterzeichnende Kanzlei. Adressat: Berufsgenossenschaft Handel und Warenlogistik, Bezirksverwaltung Trier, Aktenzeichen BGHW-2026-350118-MOELLER.")
add_h2(doc, "2. Antrag")
add_p(doc, "Es werden Leistungen zur Berufshilfe nach Paragraf 35 SGB VII beantragt, hilfsweise Leistungen zur medizinisch-beruflich orientierten Rehabilitation, fuer den Fall, dass eine Rueckkehr auf den bisherigen Arbeitsplatz als Lagerleiter mit koerperlich schwerer Taetigkeit dauerhaft nicht moeglich ist.")
add_h2(doc, "3. Begruendung")
add_p(doc, "Nach dem Reha-Verlaufsbericht der BG Klinik Ludwigshafen vom 22.06.2026 besteht weiterhin ein relevantes Kraftdefizit der rechten Schulter. Der Arbeitsplatz als Lagerleiter erfordert regelmaessiges Heben und Ueberkopfarbeiten, die nach aerztlicher Einschaetzung derzeit nicht zumutbar sind. Es wird angeregt, eine innerbetriebliche Umsetzung in eine disponierende, ueberwiegend sitzende Taetigkeit zu pruefen, hilfsweise eine externe Qualifizierungsmassnahme.")
add_h2(doc, "4. Vorlaeufiger Vorbehalt")
add_p(doc, "Der Antrag wird ausdruecklich unter dem Vorbehalt gestellt, dass die BG das Ereignis vom 03.04.2026 als Arbeitsunfall anerkennt. Sollte die Anerkennung verweigert bleiben, wird der Antrag als Eventualantrag fuer das Widerspruchsverfahren aufrechterhalten.")
add_formathinweis(doc)
save(doc, BASE + "18_berufshilfe_antrag.docx")

# 19 - Detaillierter D-Arzt-Bericht mit Nachbehandlung
doc = new_document()
add_title(doc, "Detaillierter Durchgangsarztbericht mit Nachbehandlungsverlauf")
add_letterhead(doc, ["Bruederkrankenhaus Trier", "Durchgangsarztpraxis Dr. Reiner Kauth", "Nordallee 1, 54292 Trier"])
add_h2(doc, "1. Erstvorstellung")
add_p(doc, "Erstvorstellung am 03.04.2026 um 8:15 Uhr nach Verlegung aus der Notaufnahme. Diagnosen: Schulterprellung rechts mit Verdacht auf Rotatorenmanschettenruptur, Schaedelprellung ohne Bewusstlosigkeit, Schuerfwunden rechter Ellenbogen. Arbeitsunfaehigkeit ab 03.04.2026.")
add_h2(doc, "2. Verlaufskontrollen")
add_table(doc, ["Datum", "Befund", "Massnahme"], [
    ["10.04.2026", "MRT bestaetigt Teilruptur Supraspinatussehne", "Operationsindikation gestellt"],
    ["16.04.2026", "Aufklaerung, praeoperative Diagnostik", "OP-Termin 21.04.2026 vereinbart"],
    ["05.05.2026", "Zwei Wochen postoperativ, reizlose Wundverhaeltnisse", "Physiotherapie fortgesetzt"],
    ["02.06.2026", "Beginn stationaere Anschlussheilbehandlung", "Ueberweisung BG Klinik Ludwigshafen"],
    ["30.06.2026", "Nach Reha, Kraftdefizit rueckläufig, Abduktion 110 Grad", "Stufenweise Wiedereingliederung geplant"],
])
add_h2(doc, "3. Zusammenhangsbeurteilung des Durchgangsarztes")
add_p(doc, "Dr. Kauth haelt in seinem Zwischenbericht vom 30.06.2026 fest, dass der geschilderte Unfallmechanismus, der intraoperative Befund eines frischen Rupturrandes sowie der zeitliche Zusammenhang zwischen Ereignis und Erstschmerz fuer eine wesentliche Teilursache des Unfalls sprechen. Der Vorschaden werde dadurch nicht bestritten, trete aber nach seiner fachaerztlichen Einschaetzung in der Gesamtwuerdigung in den Hintergrund.")
add_h2(doc, "4. Arbeitsfaehigkeitsprognose")
add_p(doc, "Bei planmaessigem Verlauf wird eine Wiederaufnahme leichter Buerotaetigkeiten ab August 2026 fuer moeglich gehalten, eine vollstaendige Rueckkehr zur urspruenglichen koerperlich schweren Lagerleitertaetigkeit ist nach jetzigem Stand ungewiss und haengt vom Ergebnis der Anschlussuntersuchung im September 2026 ab.")
add_formathinweis(doc)
save(doc, BASE + "19_d_arzt_bericht_detailliert_nachbehandlung.docx")

print("Teil 3 fertig")
