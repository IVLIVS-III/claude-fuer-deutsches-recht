import sys
sys.path.insert(0, "/home/user/workspace/legal-work/target/scripts/_tmp_gen")
from docx_helper import new_document, add_title, add_h2, add_h3, add_p, add_letterhead, add_table, add_formathinweis, save

BASE = "/home/user/workspace/legal-work/target/testakten/unfallversicherung-arbeitsunfall-lagerleiter-sturz-trier/"
KANZLEI = ["Kanzlei Lindenhof und Partner mbB", "Fachanwaelte fuer Sozialrecht", "Domfreihof 6, 54290 Trier", "Bearbeiterin: Dr. Nadine Ohlerich"]
BG = ["Berufsgenossenschaft Handel und Warenlogistik", "Bezirksverwaltung Trier", "Loebstrasse 22, 54292 Trier", "Aktenzeichen: BGHW-2026-350118-MOELLER"]
SG = ["Sozialgericht Trier", "Kutzbachstrasse 3a, 54290 Trier"]

# 24 - Widerspruch komplett ausgebaut Vollversion
doc = new_document()
add_title(doc, "Widerspruch gegen den Ablehnungsbescheid, Vollversion")
add_letterhead(doc, KANZLEI)
add_p(doc, "An die Berufsgenossenschaft Handel und Warenlogistik, Bezirksverwaltung Trier, Aktenzeichen BGHW-2026-350118-MOELLER, per beA am 20.07.2026 uebermittelt.")
add_h2(doc, "1. Antrag")
add_p(doc, "Namens und im Auftrag des Herrn Karsten Moeller wird gegen den Bescheid vom 18.06.2026, zugegangen am 22.06.2026, form- und fristgerecht Widerspruch eingelegt. Beantragt wird, den Bescheid aufzuheben und das Ereignis vom 03.04.2026 als Arbeitsunfall im Sinne von Paragraf 8 SGB VII anzuerkennen sowie die gesetzlich geschuldeten Leistungen, insbesondere Heilbehandlung und Verletztengeld, zu gewaehren.")
add_h2(doc, "2. Sachverhalt aus Sicht des Widerspruchsfuehrers")
add_p(doc, "Herr Moeller uebte bei dem Ereignis eine versicherte Taetigkeit aus, indem er eine betrieblich benoetigte, klemmende Ueberladebruecke an Rampe 4 zu sichern versuchte, um den Wareneingang eines wartenden Lastzugs zu ermoeglichen. Der Sturz erfolgte zeitlich begrenzt und wirkte von aussen auf den Koerper ein.")
add_h2(doc, "3. Beweiswuerdigung")
add_h3(doc, "3.1 Zeugenangaben")
add_p(doc, "Die Zeugen Bastian Kopp und Sandra Lehnert bestaetigen unabhaengig voneinander, dass Herr Moeller sich unmittelbar nach dem Sturz zum technischen Versagen der Rampe geaeussert hat und dass die Rampe im relevanten Zeitraum wiederholt schwergaengig war.")
add_h3(doc, "3.2 Wartungsbuch und technischer Zustand")
add_p(doc, "Nach dem Wartungsbuch wurde die Bruecke im Maerz 2026 mindestens dreimal als schwergaengig vermerkt, ein Reparaturtermin war fuer den 8. April 2026 bereits vereinbart. Diese Dokumentation stuetzt die Darstellung eines technischen Defekts als Ausloeser des Sturzes.")
add_h3(doc, "3.3 Kameraausfall")
add_p(doc, "Der zeitlich mit dem Unfallereignis zusammenfallende Ausfall der Kamera an Rampe 4 spricht nicht gegen, sondern ist neutral zu werten; er darf nicht zu Lasten des Versicherten gewuerdigt werden, da der Ausfall unstreitig technische, nicht in der Sphaere des Mandanten liegende Ursachen hatte.")
add_h3(doc, "3.4 Medizinische Befunde")
add_p(doc, "Der intraoperative Befund vom 21.04.2026 dokumentiert einen frischen, blutig imbibierten Rupturrand, der nach der Einschaetzung des Operateurs eine akute traumatische Komponente auf vorbestehender degenerativer Struktur belegt. Das im MRT nachgewiesene Knochenmarkoedem am Tuberculum majus ist ein typisches Zeichen einer frischen knoechernen Belastungsreaktion.")
add_h2(doc, "4. Rechtliche Bewertung")
add_p(doc, "Nach der Rechtsprechung des Bundessozialgerichts, unter anderem B 2 U 4/18 R, genuegt fuer den Nachweis des Unfallereignisses der Vollbeweis anhand einer Gesamtwuerdigung aller Umstaende; eine unmittelbare Beobachtung ist nicht zwingend erforderlich, wenn sich aus Indizien ein schluessiges Gesamtbild ergibt. Auch bei vorbestehendem Gesundheitsschaden genuegt es, wenn das Unfallereignis eine wesentliche Teilursache im Sinne der im Sozialrecht geltenden Kausalitaetslehre der wesentlichen Bedingung darstellt.")
add_h2(doc, "5. Beweisantraege")
add_p(doc, "Es wird beantragt, das vollstaendige Wartungsbuch Rampe 4 fuer die Monate Februar bis April 2026 beizuziehen, die Zeugen Kopp, Lehnert und Nauheim erneut unter Vorhalt der ergaenzenden Unterlagen zu befragen sowie ein unfallchirurgisches Zusammenhangsgutachten einzuholen.")
add_formathinweis(doc)
save(doc, BASE + "24_widerspruch_vollversion.docx")

# 25 - Widerspruchsbescheid BG
doc = new_document()
add_title(doc, "Widerspruchsbescheid der Berufsgenossenschaft")
add_letterhead(doc, BG)
add_p(doc, "Datum: 25.09.2026")
add_h2(doc, "1. Entscheidung")
add_p(doc, "Der Widerspruch des Herrn Karsten Moeller gegen den Bescheid vom 18.06.2026 wird zurueckgewiesen.")
add_h2(doc, "2. Begruendung")
add_p(doc, "Die Widerspruchsstelle haelt nach erneuter Pruefung an ihrer Auffassung fest, dass der Vollbeweis eines von aussen einwirkenden Ereignisses nicht erbracht sei. Die vorgelegten Zeugenaussagen beschraenkten sich auf Wahrnehmungen vor und nach dem eigentlichen Sturz, nicht auf den Sturz selbst. Das Wartungsbuch belege zwar technische Maengel, lasse aber offen, ob diese ursaechlich fuer den konkreten Sturz waren oder ob der Versicherte aus anderen Gruenden das Gleichgewicht verlor.")
add_h2(doc, "3. Auseinandersetzung mit dem medizinischen Vorbringen")
add_p(doc, "Der intraoperative Befund werde zur Kenntnis genommen, aendere aber nichts an der Einschaetzung, dass angesichts der erheblichen degenerativen Vorschaedigung eine ueberwiegende Wahrscheinlichkeit fuer eine schicksalhafte, nicht unfallbedingte Ursache der Ruptur bestehe.")
add_h2(doc, "4. Rechtsbehelfsbelehrung")
add_p(doc, "Gegen diesen Widerspruchsbescheid kann innerhalb eines Monats nach Zugang Klage beim Sozialgericht Trier erhoben werden.")
add_formathinweis(doc)
save(doc, BASE + "25_widerspruchsbescheid_bg.docx")

# 26 - Klageschrift Sozialgericht Trier
doc = new_document()
add_title(doc, "Klageschrift zum Sozialgericht Trier")
add_letterhead(doc, KANZLEI)
add_p(doc, "An das Sozialgericht Trier, Kutzbachstrasse 3a, 54290 Trier, per beA am 20.10.2026 eingereicht.")
add_h2(doc, "1. Parteien")
add_p(doc, "Klaeger: Karsten Moeller, Hafenstrasse nahe Trier-Ehrang wohnhaft, vertreten durch die Kanzlei Lindenhof und Partner mbB. Beklagte: Berufsgenossenschaft Handel und Warenlogistik, Bezirksverwaltung Trier.")
add_h2(doc, "2. Klageantrag")
add_p(doc, "Es wird beantragt, den Bescheid vom 18.06.2026 in der Gestalt des Widerspruchsbescheids vom 25.09.2026 aufzuheben und festzustellen, dass das Ereignis vom 03.04.2026 ein Arbeitsunfall im Sinne von Paragraf 8 SGB VII ist, sowie die Beklagte zu verurteilen, die gesetzlichen Leistungen der Unfallversicherung zu gewaehren.")
add_h2(doc, "3. Klagebegruendung")
add_p(doc, "Zur Begruendung wird auf den ausfuehrlichen Widerspruch vom 20.07.2026 und die dort dargestellte Beweislage verwiesen. Ergaenzend wird darauf hingewiesen, dass die Beklagte den Beweiswert der uebereinstimmenden Zeugenangaben unzureichend gewuerdigt und dem Kameraausfall zu Unrecht eine dem Klaeger nachteilige Bedeutung beigemessen hat.")
add_h2(doc, "4. Beweisantritt")
add_p(doc, "Es wird die Einholung eines unfallchirurgischen Zusammenhangsgutachtens beantragt, ferner die zeugenschaftliche Vernehmung von Bastian Kopp, Sandra Lehnert und Herbert Nauheim sowie die Beiziehung des vollstaendigen Wartungsbuchs Rampe 4.")
add_formathinweis(doc)
save(doc, BASE + "26_klageschrift_sozialgericht_trier.docx")

# 27 - Klageerwiderung BG
doc = new_document()
add_title(doc, "Klageerwiderung der Berufsgenossenschaft")
add_letterhead(doc, BG)
add_p(doc, "An das Sozialgericht Trier, Az. S 4 U 88/26, Erwiderung vom 25.11.2026.")
add_h2(doc, "1. Antrag")
add_p(doc, "Die Beklagte beantragt, die Klage abzuweisen.")
add_h2(doc, "2. Erwiderung in der Sache")
add_p(doc, "Die Beklagte haelt an ihrer im Widerspruchsbescheid dargelegten Auffassung fest. Ergaenzend wird vorgetragen, dass Herr Moeller nach der internen Arbeitsanweisung Nr. 14 nicht zur eigenhaendigen Wartung der Ueberladebruecke befugt gewesen sei; ein Verstoss gegen innerbetriebliche Anweisungen koenne den Zusammenhang mit der versicherten Taetigkeit infrage stellen.")
add_h2(doc, "3. Stellungnahme zu den Beweisantraegen")
add_p(doc, "Gegen die Einholung eines Sachverstaendigengutachtens bestehen keine grundsaetzlichen Einwaende; die Beklagte behaelt sich vor, nach Vorlage des Gutachtens ergaenzend Stellung zu nehmen. Die erneute Vernehmung der bereits im Verwaltungsverfahren gehoerten Zeugen wird fuer nicht erforderlich gehalten.")
add_h2(doc, "4. Hinweis zur Arbeitsanweisung")
add_p(doc, "Die Beklagte legt als Anlage die interne Arbeitsanweisung Nr. 14 zur Ladungssicherung vor, wonach die Wartung technischer Rampenanlagen ausschliesslich dem Rampenwart obliegt.")
add_formathinweis(doc)
save(doc, BASE + "27_klageerwiderung_bg.docx")

print("Teil 5 fertig")
