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
    "Kanzlei Ahlers und Brinkmann, Fachanwälte für Sozialrecht, Oldenburg",
    "Bearbeiter: Rechtsanwalt Joost Ahlers",
    "Staulinie 8, 26122 Oldenburg",
    "Telefon 0441 77 03 30, Telefax 0441 77 03 39",
    "USt-IdNr. DE 812 447 903",
]

# 24: Zweitgutachten-Antrag (korrigierte Kanzlei)
doc = new_document()
add_title(doc, "Antrag auf Einholung eines Zweitgutachtens")
add_letterhead(doc, KANZLEI)
add_p(doc, "An die Weser-Ems Gesundheitskasse, Leistungsabteilung Hilfsmittel, Schreiben vom 22.06.2026.")
add_h2(doc, "1. Antrag")
add_p(doc, "Namens des Herrn Heinz Körner wird beantragt, vor abschließender Entscheidung über den Widerspruch ein unabhängiges Zweitgutachten einzuholen, das auf einer persönlichen Untersuchung und einer praktischen Erprobung des beantragten Elektrorollstuhls im Wohnumfeld beruht.")
add_h2(doc, "2. Begründung")
add_p(doc, "Die bisherige Stellungnahme des Medizinischen Dienstes beruht ausschließlich auf Aktenlage, ohne eigene körperliche Untersuchung, Gehprobe oder Erprobung der in Betracht kommenden Hilfsmittel. Demgegenüber stützt sich das private Gutachten von RehaTechnik Albrecht auf eine mehrstündige praktische Erprobung im tatsächlichen Wohnumfeld. Angesichts dieser Diskrepanz erscheint eine erneute, unabhängige Begutachtung sachgerecht.")
add_p(doc, "Es wird angeregt, mit der Begutachtung eine Fachärztin oder einen Facharzt für Physikalische und Rehabilitative Medizin zu beauftragen, die oder der weder für die Krankenkasse noch für den Kläger bereits tätig geworden ist.")
add_formathinweis(doc)
save(doc, f"{BASE}/24_zweitgutachten_antrag.docx")

# 26: Klageschrift komplett
doc = new_document()
add_title(doc, "Klageschrift")
add_letterhead(doc, KANZLEI)
add_p(doc, "An das Sozialgericht Oldenburg, Klingenbergstraße 4, 26133 Oldenburg", align="right")
add_p(doc, "Oldenburg, den 03.07.2026", align="right")
doc.add_paragraph()
add_p(doc, "In dem Rechtsstreit")
add_p(doc, "des Herrn Heinz Körner, Peterstraße 18, 26122 Oldenburg, Kläger,")
add_p(doc, "Prozessbevollmächtigte: Kanzlei Ahlers und Brinkmann, Staulinie 8, 26122 Oldenburg,")
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
add_p(doc, "Zeugenvernehmung der Tochter des Klägers, Frau Dr. Maren Körner, zum Alltag und zu Sturzereignissen,")
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

# 30: BSG-Rechtsprechungsanalyse
doc = new_document()
add_title(doc, "Rechtsprechungsübersicht Hilfsmittelversorgung Elektrorollstuhl")
add_p(doc, "Interne Arbeitsunterlage der Kanzlei Ahlers und Brinkmann, Stand 20.09.2026")
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

print("fertig 24/26/27/30 korrigiert")
