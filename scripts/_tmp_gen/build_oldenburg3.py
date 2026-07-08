import sys
sys.path.insert(0, "/home/user/workspace/legal-work/target/scripts/_tmp_gen")
from docx_helper import new_document, add_title, add_h2, add_h3, add_p, add_letterhead, add_table, add_formathinweis, save

BASE = "/home/user/workspace/legal-work/target/testakten/sozialrecht-elektrorollstuhl-koerner-oldenburg"

KASSE = [
    "Weser-Ems Gesundheitskasse",
    "Krankenversicherung und Pflegeversicherung",
    "Leistungsabteilung Hilfsmittel",
    "Huntestraße 42, 26135 Oldenburg",
    "Telefon 0441 55 219-0, Telefax 0441 55 219-90",
]

KANZLEI = [
    "Kanzlei Brammertz und Kollegen",
    "Fachanwälte für Sozialrecht",
    "Damm 21, 26135 Oldenburg",
    "Telefon 0441 92 41 00, Telefax 0441 92 41 09",
    "USt-IdNr. DE 815 632 447",
]

# 25: Widerspruchsbescheid komplett ausformuliert (ersetzt/ergaenzt 11, hier als vollstaendige neue Fassung mit Sachverhalt)
doc = new_document()
add_title(doc, "Widerspruchsbescheid")
add_letterhead(doc, KASSE)
add_p(doc, "Aktenzeichen: WEK-HM-2026-4471", align="right")
add_p(doc, "Oldenburg, den 24.06.2026", align="right")
doc.add_paragraph()
add_p(doc, "In der Verwaltungssache")
add_p(doc, "Herr Heinz Körner, geboren am 03.02.1948, wohnhaft Peterstraße 18, 26122 Oldenburg,")
add_p(doc, "gegen den Bescheid vom 10.06.2026 über die Ablehnung der Versorgung mit einem Elektrorollstuhl,")
doc.add_paragraph()
add_h2(doc, "Tenor")
add_p(doc, "Der Widerspruch vom 20.06.2026 gegen den Bescheid vom 10.06.2026 wird zurückgewiesen.")
add_h2(doc, "Sachverhalt")
add_p(doc, "Der Widerspruchsführer beantragte am 12.05.2026 die Versorgung mit einem Elektrorollstuhl mit Nahbereichs- und Innenraumtauglichkeit. Grundlage war die ärztliche Verordnung von Dr. Stahlmann vom 07.05.2026 sowie der Facharztbericht von Dr. Radtke vom 17.05.2026. Der Medizinische Dienst nahm am 05.06.2026 Stellung und hielt eine Versorgung mit Unterarmgehstütze, vorhandenem Rollator und Standard-Faltrollstuhl für ausreichend. Mit Bescheid vom 10.06.2026 lehnte die Krankenkasse den Antrag ab. Hiergegen legte der Widerspruchsführer am 20.06.2026 form- und fristgerecht Widerspruch ein.")
add_h2(doc, "Gründe")
add_p(doc, "Der Widerspruch ist zulässig, aber unbegründet.")
add_p(doc, "Nach Paragraf 33 Absatz 1 SGB V haben Versicherte Anspruch auf Versorgung mit Hilfsmitteln, die im Einzelfall erforderlich sind, um den Erfolg der Krankenbehandlung zu sichern, einer drohenden Behinderung vorzubeugen oder eine Behinderung auszugleichen. Der Anspruch besteht nicht, wenn das Hilfsmittel als allgemeiner Gebrauchsgegenstand des täglichen Lebens anzusehen ist oder wenn es nach Paragraf 34 SGB V ausgeschlossen ist.")
add_p(doc, "Die Krankenkasse ist an die Empfehlung des Medizinischen Dienstes vom 05.06.2026 gebunden, soweit diese schlüssig und nachvollziehbar ist. Danach verfügt der Widerspruchsführer über eine Restgehfähigkeit, die mit den vorhandenen Hilfsmitteln Rollator und Unterarmgehstütze im häuslichen Umfeld ausreichend ausgeglichen werden kann. Der beantragte Elektrorollstuhl geht über den Basisausgleich hinaus, den die gesetzliche Krankenversicherung schuldet.")
add_p(doc, "Das im Widerspruchsverfahren vorgelegte private Reha-Gutachten vom 18.06.2026 wurde geprüft. Es führt nach Auffassung der Kasse nicht zu einer anderen Bewertung, da es auf einer einmaligen Untersuchung im Wohnumfeld beruht und keine neuen medizinischen Befunde gegenüber der Aktenlage des Medizinischen Dienstes enthält.")
add_p(doc, "Der Widerspruch war daher zurückzuweisen.")
add_h2(doc, "Rechtsbehelfsbelehrung")
add_p(doc, "Gegen diesen Widerspruchsbescheid kann innerhalb eines Monats nach Zustellung Klage beim Sozialgericht Oldenburg, Klingenbergstraße 4, 26133 Oldenburg, erhoben werden.")
add_formathinweis(doc)
save(doc, f"{BASE}/25_widerspruchsbescheid_komplett_ausformuliert.docx")

# 26: Klageschrift komplett (nicht nur Entwurf) - eingereichte Fassung mit Antrag, Begruendung, Beweisantritten
doc = new_document()
add_title(doc, "Klageschrift")
add_letterhead(doc, KANZLEI)
add_p(doc, "An das Sozialgericht Oldenburg, Klingenbergstraße 4, 26133 Oldenburg", align="right")
add_p(doc, "Oldenburg, den 03.07.2026", align="right")
doc.add_paragraph()
add_p(doc, "In dem Rechtsstreit")
add_p(doc, "des Herrn Heinz Körner, Peterstraße 18, 26122 Oldenburg, Kläger,")
add_p(doc, "Prozessbevollmächtigte: Kanzlei Brammertz und Kollegen, Damm 21, 26135 Oldenburg,")
add_p(doc, "gegen")
add_p(doc, "die Weser-Ems Gesundheitskasse, Huntestraße 42, 26135 Oldenburg, Beklagte,")
doc.add_paragraph()
add_p(doc, "wird namens und im Auftrag des Klägers Klage erhoben und beantragt:")
add_h2(doc, "Anträge")
add_p(doc, "1. Der Bescheid der Beklagten vom 10.06.2026 in Gestalt des Widerspruchsbescheids vom 24.06.2026 wird aufgehoben.")
add_p(doc, "2. Die Beklagte wird verurteilt, den Kläger mit einem geeigneten Elektrorollstuhl mit Innenraum- und Nahbereichstauglichkeit entsprechend der Verordnung vom 07.05.2026 zu versorgen.")
add_p(doc, "3. Die Beklagte trägt die notwendigen außergerichtlichen Kosten des Klägers.")
add_h2(doc, "Begründung")
add_h3(doc, "I. Sachverhalt")
add_p(doc, "Der 78-jährige Kläger leidet an einer Spinalkanalstenose, einer diabetischen Polyneuropathie sowie den Folgen einer Hüft-Totalendoprothese links. Er lebt allein im ersten Obergeschoss eines Altbaus in Oldenburg. Wegen Sturzgefahr, Sensibilitätsstörungen und rascher Erschöpfung ist ihm eine selbständige Fortbewegung im Nahbereich mit den bislang zur Verfügung gestellten Hilfsmitteln nicht möglich.")
add_p(doc, "Die Beklagte lehnte die Versorgung mit Bescheid vom 10.06.2026 ab und wies den Widerspruch mit Widerspruchsbescheid vom 24.06.2026 zurück.")
add_h3(doc, "II. Rechtliche Würdigung")
add_p(doc, "Der Kläger hat einen Anspruch aus Paragraf 33 Absatz 1 SGB V. Der Elektrorollstuhl ist zum Ausgleich der Behinderung im Bereich der Mobilität erforderlich. Nach der Rechtsprechung des Bundessozialgerichts, unter anderem B 3 KR 3/19 R, ist bei der Prüfung des Basisausgleichs nicht allein auf die Fähigkeit zu wenigen Schritten im Wohnbereich abzustellen, sondern auf die Erschließung eines Bewegungsraums, der die Nutzung öffentlicher Wege, Ärzte und Geschäfte im Nahbereich der Wohnung ermöglicht.")
add_p(doc, "Die von der Beklagten angeführten Alternativen sind nicht gleich geeignet. Ein Rollator setzt ausreichende Standsicherheit und Ausdauer voraus, die beim Kläger wegen der Polyneuropathie nicht durchgehend gegeben sind. Ein manueller Rollstuhl kann vom Kläger wegen der Schulterbeschwerden nicht dauerhaft selbständig angetrieben werden. Beide Alternativen stellen daher keinen vollwertigen Ersatz für den beantragten Elektrorollstuhl dar.")
add_p(doc, "Das Wirtschaftlichkeitsgebot nach Paragraf 12 SGB V steht dem Anspruch nicht entgegen, da eine nicht geeignete, günstigere Versorgung keine wirtschaftliche Alternative im Sinne dieser Vorschrift darstellt.")
add_h3(doc, "III. Beweisantritte")
add_p(doc, "Zum Beweis der Tatsache, dass der Kläger im Nahbereich nicht ausreichend sicher mobil ist, wird angeboten:")
add_p(doc, "Einholung eines Sachverständigengutachtens zur Gehfähigkeit und Fahrsicherheit,")
add_p(doc, "Zeugenvernehmung der Tochter des Klägers, Frau Bettina Körner-Aswege, zum Alltag und zu Sturzereignissen,")
add_p(doc, "Beiziehung der Behandlungsunterlagen von Dr. Stahlmann und Dr. Radtke.")
add_formathinweis(doc)
save(doc, f"{BASE}/26_klageschrift_komplett.docx")

# 27: Klageerwiderung Kasse komplett
doc = new_document()
add_title(doc, "Klageerwiderung")
add_letterhead(doc, KASSE)
add_p(doc, "An das Sozialgericht Oldenburg", align="right")
add_p(doc, "Oldenburg, den 22.07.2026", align="right")
doc.add_paragraph()
add_p(doc, "In dem Rechtsstreit Körner gegen Weser-Ems Gesundheitskasse, Aktenzeichen S 12 KR 188/26,")
add_p(doc, "wird beantragt:")
add_p(doc, "Die Klage wird abgewiesen.")
add_h2(doc, "Begründung")
add_p(doc, "Die Klage ist unbegründet. Der Kläger hat keinen Anspruch auf Versorgung mit dem beantragten Elektrorollstuhl.")
add_p(doc, "Der Medizinische Dienst hat in seiner Stellungnahme vom 05.06.2026 nachvollziehbar dargelegt, dass der Kläger über eine hinreichende Restgehfähigkeit verfügt, um sich mit Unterarmgehstütze und Rollator im häuslichen Umfeld und auf kurzen ebenen Wegen zu bewegen. Für längere Strecken steht dem Kläger ein Standard-Faltrollstuhl zur Verfügung, der mit Unterstützung der Tochter genutzt werden kann.")
add_p(doc, "Die gesetzliche Krankenversicherung schuldet nach ständiger Rechtsprechung nur den Basisausgleich der Behinderung, nicht die Herstellung größtmöglicher Mobilität. Die Beklagte verweist hierzu auf die Entscheidung des Bundessozialgerichts B 3 KR 4/16 R, wonach der Ausgleich sich am Basisbedürfnis orientiert und nicht an einer vollständigen Gleichstellung mit der Mobilität eines Nichtbehinderten.")
add_p(doc, "Die Wohnsituation des Klägers, insbesondere die fehlende Barrierefreiheit des Altbaus und die Lage im ersten Obergeschoss, begründet für sich genommen keinen Anspruch gegen die Krankenversicherung. Bauliche Hindernisse und die fehlende ständige Verfügbarkeit einer Begleitperson fallen nicht in den Zuständigkeitsbereich der gesetzlichen Krankenversicherung.")
add_p(doc, "Die von Klägerseite angeführte Entscheidung B 3 KR 3/19 R ist nach Auffassung der Beklagten nicht auf den vorliegenden Fall übertragbar, da dort eine vollständige Rollstuhlpflichtigkeit ohne jede Restgehfähigkeit vorlag. Im vorliegenden Fall besteht demgegenüber eine relevante Restgehfähigkeit, die vom Kläger nicht hinreichend widerlegt wurde.")
add_p(doc, "Die Beklagte regt an, ein Gutachten zur tatsächlichen Gehfähigkeit und zur Eignung der vorhandenen Hilfsmittel einzuholen, bevor über die Notwendigkeit der begehrten elektrischen Versorgung entschieden wird.")
add_formathinweis(doc)
save(doc, f"{BASE}/27_klageerwiderung_kasse_komplett.docx")

print("fertig 25-27")
