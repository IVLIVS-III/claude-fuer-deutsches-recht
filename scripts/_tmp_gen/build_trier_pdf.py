import sys
sys.path.insert(0, "/home/user/workspace/legal-work/target/scripts/_tmp_gen")
from docx_helper import new_document, add_title, add_h2, add_p, add_letterhead, save
import subprocess

BASE = "/home/user/workspace/legal-work/target/testakten/unfallversicherung-arbeitsunfall-lagerleiter-sturz-trier/"
TMP_DOCX = "/tmp/arbeitsanweisung14.docx"

doc = new_document()
add_title(doc, "Interne Arbeitsanweisung Nr. 14, Ladungssicherung und Rampenwartung")
add_letterhead(doc, ["MoselLogistik GmbH", "Qualitaets- und Sicherheitsmanagement", "Hafenstrasse 28, 54293 Trier"])
add_h2(doc, "1. Geltungsbereich")
add_p(doc, "Diese Anweisung regelt die Zustaendigkeiten fuer die Wartung und Fehlerbehebung an Ueberladebruecken und Rampenanlagen im Logistikzentrum Trier-Ehrang.")
add_h2(doc, "2. Zustaendigkeit")
add_p(doc, "Technische Stoerungen an Ueberladebruecken sind ausschliesslich durch den eingeteilten Rampenwart zu beheben. Schichtverantwortliche und Lagerleiter duerfen technische Anlagen nicht selbst warten oder reparieren, sondern haben Stoerungen unverzueglich an den Rampenwart oder die technische Leitstelle zu melden.")
add_h2(doc, "3. Meldewege")
add_p(doc, "Meldungen erfolgen ueber Funk an die Disposition oder telefonisch an die technische Leitstelle. Bei akuter Betriebsbehinderung ist zusaetzlich die Schichtleitung zu informieren.")
add_h2(doc, "4. Stand und Freigabe")
add_p(doc, "Fassung vom 12.01.2024, freigegeben durch die Geschaeftsfuehrung, gueltig bis zur naechsten Revision.")
save(doc, TMP_DOCX)

subprocess.run(["libreoffice", "--headless", "--convert-to", "pdf", "--outdir", BASE + "pdfs", TMP_DOCX], check=True)
print("PDF erzeugt")
