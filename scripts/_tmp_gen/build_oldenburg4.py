import sys
sys.path.insert(0, "/home/user/workspace/legal-work/target/scripts/_tmp_gen")
from docx_helper import new_document, add_title, add_h2, add_h3, add_p, add_letterhead, add_table, add_formathinweis, save

BASE = "/home/user/workspace/legal-work/target/testakten/sozialrecht-elektrorollstuhl-koerner-oldenburg"

GERICHT = [
    "Sozialgericht Oldenburg",
    "Kammer für Krankenversicherungssachen",
    "Klingenbergstraße 4, 26133 Oldenburg",
]

# 28: Beweisbeschluss SG
doc = new_document()
add_title(doc, "Beweisbeschluss")
add_letterhead(doc, GERICHT)
add_p(doc, "Aktenzeichen: S 12 KR 188/26", align="right")
add_p(doc, "Oldenburg, den 05.08.2026", align="right")
doc.add_paragraph()
add_p(doc, "In dem Rechtsstreit Körner gegen Weser-Ems Gesundheitskasse beschließt die Kammer:")
add_h2(doc, "Beschluss")
add_p(doc, "1. Es wird gemäß Paragraf 106 SGG Beweis erhoben durch Einholung eines schriftlichen Sachverständigengutachtens.")
add_p(doc, "2. Zum Sachverständigen wird bestimmt: Prof. Dr. med. Anneliese Wickenrath, Fachärztin für Orthopädie und Unfallchirurgie, Physikalische und Rehabilitative Medizin, Bremen.")
add_h2(doc, "Beweisfragen")
add_p(doc, "1. Welche Wegstrecke kann der Kläger nach dem gegenwärtigen Gesundheitszustand mit einem Rollator sicher und ohne relevantes Sturzrisiko zurücklegen?")
add_p(doc, "2. Ist der Kläger in der Lage, einen manuellen Aktivrollstuhl über einen Nahbereich von mindestens 500 Metern selbständig anzutreiben, insbesondere unter Berücksichtigung der Schulterbeschwerden?")
add_p(doc, "3. Besteht bei Nutzung eines Standard-Faltrollstuhls ohne Begleitperson eine ausreichende Sicherheit gegen Sturz und Unterzuckerungsfolgen?")
add_p(doc, "4. Ist der Kläger unter Berücksichtigung von Sehvermögen, Reaktionsvermögen und Sensibilitätsstörungen in der Lage, einen Elektrorollstuhl mit gedrosselter Geschwindigkeit sicher zu führen?")
add_p(doc, "5. Welche Auswirkungen hat die jeweilige Versorgung auf die Teilhabe am gesellschaftlichen Leben im Sinne des Basisausgleichs?")
add_h2(doc, "Hinweis an die Beteiligten")
add_p(doc, "Den Beteiligten wird Gelegenheit gegeben, innerhalb von zwei Wochen ergänzende Fragen an den Sachverständigen zu stellen. Der Sachverständigen wird die vollständige Verwaltungsakte einschließlich der Stellungnahme des Medizinischen Dienstes und des privaten Reha-Gutachtens übersandt.")
add_formathinweis(doc)
save(doc, f"{BASE}/28_beweisbeschluss_sozialgericht.docx")

# 29: Gerichtliches Sachverstaendigengutachten
doc = new_document()
add_title(doc, "Gerichtliches Sachverständigengutachten")
add_p(doc, "Prof. Dr. med. Anneliese Wickenrath")
add_p(doc, "Fachärztin für Orthopädie und Unfallchirurgie, Physikalische und Rehabilitative Medizin")
add_p(doc, "Domsheide 9, 28195 Bremen")
doc.add_paragraph()
add_p(doc, "Auftraggeber: Sozialgericht Oldenburg, Aktenzeichen S 12 KR 188/26", align="right")
add_p(doc, "Untersuchungstermin: 02.09.2026, Bremen", align="right")
add_p(doc, "Gutachten vom 16.09.2026", align="right")
add_h2(doc, "1. Auftrag")
add_p(doc, "Mit Beweisbeschluss vom 05.08.2026 wurde die Unterzeichnende beauftragt, zur Gehfähigkeit, zur Nutzbarkeit eines manuellen Rollstuhls sowie zur Fahrsicherheit mit einem Elektrorollstuhl bei Herrn Heinz Körner Stellung zu nehmen.")
add_h2(doc, "2. Untersuchungsbefund")
add_p(doc, "Der Kläger erschien in Begleitung seiner Tochter zur Untersuchung. Klinisch zeigt sich eine deutliche Gangunsicherheit mit verkürzter Schrittlänge und breitbasigem Gangbild. Bei der Gehprobe im Klinikflur legte der Kläger mit Rollator eine Strecke von etwa 40 Metern zurück, danach musste er sich wegen Erschöpfung und einsetzendem Schwindel setzen. Eine Sensibilitätsprüfung der Füße ergab eine deutlich herabgesetzte Berührungsempfindung beidseits, vereinbar mit der bekannten diabetischen Polyneuropathie.")
add_p(doc, "Die Schulterbeweglichkeit rechts ist endgradig eingeschränkt, links besteht Zustand nach der Hüft-TEP ohne relevante Einschränkung der oberen Extremität. Beim Antriebsversuch mit einem testweise bereitgestellten manuellen Aktivrollstuhl konnte der Kläger eine Strecke von 30 Metern auf ebenem Boden zurücklegen, danach zeigte sich eine deutliche muskuläre Erschöpfung der Schultern.")
add_p(doc, "Der Fahrversuch mit einem auf niedrige Geschwindigkeit programmierten Elektrorollstuhl verlief unauffällig. Der Kläger zeigte ein sicheres Bedienverhalten, angemessene Reaktionszeiten und keine Anzeichen von Fehlbedienung in mehreren Kurvenfahrten und beim Anhalten vor Hindernissen.")
add_h2(doc, "3. Beantwortung der Beweisfragen")
add_table(doc, ["Beweisfrage", "Untersuchungsergebnis"], [
    ["Wegstrecke mit Rollator", "etwa 40 Meter, danach Erschöpfung und Schwindel"],
    ["Manueller Rollstuhl Nahbereich", "nach etwa 30 Metern deutliche Erschöpfung der Schultermuskulatur"],
    ["Sicherheit Standard-Faltrollstuhl ohne Begleitung", "nicht ausreichend wegen Sturz- und Unterzuckerungsrisiko bei fehlender Aufsicht"],
    ["Fahrsicherheit Elektrorollstuhl gedrosselt", "im Fahrversuch unauffällig, sicheres Bedienverhalten"],
    ["Teilhabe-Auswirkung", "Elektrorollstuhl würde selbständige Wege im Nahbereich ermöglichen, die derzeit nicht zurückgelegt werden können"],
])
add_h2(doc, "4. Zusammenfassende Beurteilung")
add_p(doc, "Die vorhandenen Hilfsmittel Rollator und Standard-Faltrollstuhl ermöglichen dem Kläger nach den erhobenen Befunden keine sichere und ausdauernde Fortbewegung im Nahbereich der Wohnung. Die im Fahrversuch festgestellte sichere Bedienung eines gedrosselten Elektrorollstuhls spricht aus gutachterlicher Sicht für die grundsätzliche Eignung dieses Hilfsmittels.")
add_formathinweis(doc)
save(doc, f"{BASE}/29_gerichtliches_sachverstaendigengutachten.docx")

# 30: BSG-Rechtsprechungsanalyse
doc = new_document()
add_title(doc, "Rechtsprechungsübersicht Hilfsmittelversorgung Elektrorollstuhl")
add_p(doc, "Interne Arbeitsunterlage der Kanzlei Brammertz und Kollegen, Stand 20.09.2026")
add_h2(doc, "1. Bundessozialgericht, Urteil vom 18.05.2021, B 3 KR 3/19 R")
add_p(doc, "Das Bundessozialgericht hat entschieden, dass sich der Basisausgleich einer Gehbehinderung nicht auf das bloße Erreichen der eigenen Wohnungstür beschränkt. Erfasst wird auch die Erschließung eines gewissen körperlichen Freiraums im Nahbereich der Wohnung, der die Wahrnehmung elementarer Bedürfnisse des täglichen Lebens ermöglicht, etwa der Weg zu Ärzten, Apotheken oder Geschäften in fußläufiger Entfernung. Eine Versorgung, die nur die Fortbewegung innerhalb der eigenen vier Wände sicherstellt, deckt den Anspruch nicht vollständig.")
add_h2(doc, "2. Bundessozialgericht, Urteil vom 07.10.2010, B 3 KR 5/10 R")
add_p(doc, "Nach dieser Entscheidung ist bei der Auswahl zwischen mehreren geeigneten Hilfsmitteln das Wirtschaftlichkeitsgebot zu beachten. Ein Hilfsmittel ist jedoch nur dann eine wirtschaftliche Alternative, wenn es den Versorgungszweck tatsächlich gleichwertig erfüllt. Kann der Versicherte ein günstigeres Hilfsmittel aus gesundheitlichen Gründen nicht in vergleichbarer Weise nutzen, scheidet der Verweis auf dieses Hilfsmittel aus.")
add_h2(doc, "3. Bundessozialgericht, Urteil vom 21.03.2013, B 3 KR 4/12 R")
add_p(doc, "Die Entscheidung befasst sich mit der Abgrenzung zwischen Behinderungsausgleich und allgemeinem Gebrauchsgegenstand. Ein Elektrorollstuhl ist danach regelmäßig kein allgemeiner Gebrauchsgegenstand, weil er speziell auf die Bedürfnisse von Menschen mit erheblich eingeschränkter Gehfähigkeit zugeschnitten ist und im Handel nicht als Gegenstand des allgemeinen täglichen Bedarfs erhältlich ist.")
add_h2(doc, "4. Bundessozialgericht, Urteil vom 29.01.2019, B 3 KR 4/16 R")
add_p(doc, "Diese Entscheidung betont, dass die gesetzliche Krankenversicherung nicht zur Herstellung größtmöglicher Mobilität verpflichtet ist, sondern nur zum Ausgleich der Behinderung im Sinne eines Basisausgleichs. Der Umfang der geschuldeten Versorgung richtet sich nach dem, was zur Befriedigung der Grundbedürfnisse notwendig ist, nicht nach einer vollständigen Gleichstellung mit nicht behinderten Menschen.")
add_h2(doc, "5. Einordnung für das vorliegende Verfahren")
add_p(doc, "Die genannten Entscheidungen zeigen, dass die Abgrenzung im vorliegenden Fall maßgeblich von zwei Tatsachenfragen abhängt: erstens vom Umfang der tatsächlich verbliebenen Gehfähigkeit und deren Belastbarkeit über eine gewisse Strecke, und zweitens von der Frage, ob der Kläger einen manuellen Rollstuhl aus gesundheitlichen Gründen nicht in vergleichbarer Weise wie einen Elektrorollstuhl nutzen kann. Beide Fragen sind tatrichterlich auf Grundlage der Beweisaufnahme zu klären und werden durch keine der zitierten Entscheidungen vorweggenommen.")
add_formathinweis(doc)
save(doc, f"{BASE}/30_bsg_rechtsprechungsanalyse.docx")

print("fertig 28-30")
