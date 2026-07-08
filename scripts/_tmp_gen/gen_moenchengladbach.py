#!/usr/bin/env python3
"""Ausbau Moenchengladbach Grundstuecksverkauf/Provision auf 25 Aktenstuecke."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from aktenbau import make_docx, make_csv

SLUG = "insolvenzanfechtung-glaeubigerbenachteiligung-grundstuecksverkauf-moenchengladbach"
D = Path("/home/user/workspace/legal-work/target/testakten") / SLUG

VERWALTER_KOPF = "Rechtsanwalt Dr. Carsten Hellwege - Insolvenzverwalter\nBismarckstrasse 65, 41061 Moenchengladbach"
GEGNER_KOPF = "Rechtsanwalt Dr. Leo Brandstaetter\nKoenigsallee 78, 40212 Duesseldorf"
GERICHT_KOPF = "Landgericht Moenchengladbach - 3. Zivilkammer\nHohenzollernstrasse 157, 41061 Moenchengladbach"

# 16 Klageschrift gegen Rheinpark (Rueckuebertragung/Wertersatz)
make_docx(
    D / "16_klageschrift_rheinpark_lg_moenchengladbach.docx",
    VERWALTER_KOPF,
    "Klageschrift",
    [
        "Landgericht Moenchengladbach",
        "3. Zivilkammer",
        "Hohenzollernstrasse 157, 41061 Moenchengladbach",
        "",
        "In dem Rechtsstreit",
        "",
        "Rechtsanwalt Dr. Carsten Hellwege, als Insolvenzverwalter ueber das Vermoegen der Vondering Metallform GmbH",
        "- Klaeger -",
        "",
        "gegen",
        "",
        "Rheinpark Gewerbeimmobilien GmbH & Co. KG, vertreten durch die Komplementaerin, diese vertreten durch den Geschaeftsfuehrer Bjoern Casparius, Koenigsallee 108, 40212 Duesseldorf",
        "- Beklagte -",
        "",
        "wird namens und im Auftrag des Klaegers Klage erhoben mit dem Antrag, die Beklagte zu verurteilen, an den Klaeger Wertersatz in Hoehe von EUR 197.400,00 nebst Zinsen seit dem 16.07.2026 zu zahlen, hilfsweise das im Grundbuch von Moenchengladbach-Rheydt Blatt 4471 eingetragene Grundstueck Zug um Zug gegen Rueckzahlung des Kaufpreises von EUR 1.850.000,00 an den Klaeger rueckaufzulassen.",
        "## Begruendung",
        "Der Kaufvertrag vom 12.11.2025 unterliegt der Anfechtung nach Paragraf 133 Abs. 1, hilfsweise Paragraf 132 InsO. Der im Verkehrswertgutachten vom 24.10.2025 vorgenommene Marktanpassungsabschlag von 10 Prozent beruht ausweislich Ziffer 4.2 des Gutachtens allein auf dem Zeitdruck der Schuldnerin und nicht auf der Marktlage; der tatsaechliche Verkehrswert ohne Zeitdruck betraegt EUR 2.050.000,00. Der Klaeger beziffert die unmittelbare Benachteiligung mit der Differenz zwischen diesem Wert und dem erzielten Kaufpreis, abzueglich der wertausschoepfenden Belastung.",
        "Die Beklagte kannte nach dem im Gutachten dokumentierten Hinweis auf die Ruckfuehrung faelliger Bankverbindlichkeiten den drohenden Benachteiligungsvorsatz der Schuldnerin oder haette ihn bei der gebotenen Sorgfalt einer gewerblichen Bestandshalterin erkennen muessen.",
    ],
    "Dr. Carsten Hellwege\nRechtsanwalt, Insolvenzverwalter",
)

# 17 Klageerwiderung Rheinpark
make_docx(
    D / "17_klageerwiderung_rheinpark_2026-08-18.docx",
    GEGNER_KOPF,
    "Klageerwiderung",
    [
        "An das Landgericht Moenchengladbach - Az. 5 O 214/26",
        "",
        "Namens und im Auftrag der Beklagten wird beantragt, die Klage abzuweisen.",
        "## Begruendung",
        "Die Beklagte hat zum vollen gutachterlich festgestellten Verkehrswert erworben. Der Marktanpassungsabschlag ist gutachterlich ueblich und nicht zu beanstanden; ein Sachverstaendiger duerfe Verwertungsdruck einpreisen, ohne dass dies die Marktueblichkeit des Ergebnisses in Frage stelle. Die Beklagte hatte keinerlei Kenntnis von einer wirtschaftlichen Krise der Schuldnerin; der Hinweis im Gutachten auf die Rueckfuehrung von Bankverbindlichkeiten sei ihr vor Abschluss nicht bekannt gewesen, da sie das Gutachten erst nach Vertragsschluss vollstaendig erhalten habe.",
        "Die wertausschoepfende Belastung schliesse jede Glaeubigerbenachteiligung von vornherein aus; auf den Marktanpassungsabschlag komme es daher nicht an.",
    ],
    "Dr. Leo Brandstaetter\nRechtsanwalt",
)

# 18 Replik Verwalter
make_docx(
    D / "18_replik_verwalter_rheinpark_2026-09-05.docx",
    VERWALTER_KOPF,
    "Replik",
    [
        "An das Landgericht Moenchengladbach - Az. 5 O 214/26",
        "",
        "Die Klageerwiderung ueberzeugt nicht.",
        "1. Der Marktanpassungsabschlag ist ausweislich der Gutachtenformulierung ausdruecklich individuell, nicht marktbezogen begruendet; ein pauschaler Verweis auf gutachterliche Ueblichkeit ersetzt keine Auseinandersetzung mit dem konkreten Gutachtentext.",
        "2. Der Vortrag, das Gutachten sei erst nach Vertragsschluss vollstaendig uebermittelt worden, steht im Widerspruch zur E-Mail der Beklagten vom 29.09.2025, in der bereits auf eine 'interne Bewertung mit Bankinformationen' Bezug genommen wird.",
        "3. Die wertausschoepfende Belastung schliesst allenfalls die mittelbare, nicht aber die unmittelbare Benachteiligung durch den unter Wert liegenden Kaufpreis aus.",
        "Es wird um Terminsbestimmung und Ladung des Sachverstaendigen zur muendlichen Erlaeuterung gebeten.",
    ],
    "Dr. Carsten Hellwege\nRechtsanwalt, Insolvenzverwalter",
)

# 19 Beweisbeschluss
make_docx(
    D / "19_beweisbeschluss_lg_moenchengladbach_2026-09-22.docx",
    GERICHT_KOPF,
    "Beweisbeschluss",
    [
        "Az. 5 O 214/26",
        "",
        "In dem Rechtsstreit Dr. Hellwege ./. Rheinpark Gewerbeimmobilien GmbH & Co. KG wird beschlossen:",
        "1. Es wird Beweis erhoben durch Einholung eines ergaenzenden muendlichen Gutachtens der Sachverstaendigen Dipl.-Ing. Henrike Dallmer zu der Frage, ob und in welcher Hoehe der im schriftlichen Gutachten vom 24.10.2025 vorgenommene Marktanpassungsabschlag marktueblich oder individuell verwertungsdruckbedingt war.",
        "2. Es wird Beweis erhoben durch Vernehmung des Zeugen Bjoern Casparius zu der Frage, wann die Beklagte erstmals Kenntnis vom Inhalt des Verkehrswertgutachtens erlangt hat.",
        "Moenchengladbach, 22.09.2026",
    ],
    "Vorsitzende Richterin am Landgericht Dr. Sabine Kortmann",
)

# 20 Ergaenzendes Gutachten muendlich - Protokoll
make_docx(
    D / "20_protokoll_muendliche_gutachtenerlaeuterung_2026-11-10.docx",
    GERICHT_KOPF,
    "Protokoll der muendlichen Verhandlung mit Gutachtenerlaeuterung",
    [
        "Termin vom 10.11.2026, Az. 5 O 214/26",
        "",
        "Die Sachverstaendige Dipl.-Ing. Henrike Dallmer erlaeutert: 'Der von mir vorgenommene Abschlag von 10 Prozent war ausschliesslich durch die von der Auftraggeberin mitgeteilte Notwendigkeit einer zuegigen Verwertung veranlasst. Ein Erwerber ohne Zeitdruck haette den Ertragswert von 2.050.000 Euro voraussichtlich ohne Abschlag gezahlt.'",
        "Der Zeuge Bjoern Casparius gibt an: 'Wir haben das vollstaendige Gutachten einschliesslich der Bankinformationen bereits am 20. Oktober 2025 erhalten, also vor Beurkundung.'",
        "Protokollfuehrer: Justizangestellter T. Reimann",
    ],
    "Vorsitzende Richterin am Landgericht Dr. Sabine Kortmann",
)

# 21 Vergleichsverhandlungsprotokoll
make_docx(
    D / "21_vergleichsverhandlungsprotokoll_2026-11-10.docx",
    GERICHT_KOPF,
    "Vergleichsverhandlungsprotokoll",
    [
        "Im Anschluss an die Beweisaufnahme vom 10.11.2026 erklaeren die Parteien Vergleichsbereitschaft.",
        "Die Beklagte bietet eine Zahlung von EUR 140.000,00 zur Abgeltung des unmittelbaren Benachteiligungskomplexes an; der Klaeger fordert EUR 170.000,00 unter Hinweis auf das Beweisergebnis.",
        "Beiden Seiten wird eine Erklaerungsfrist bis zum 24.11.2026 eingeraeumt.",
    ],
    "Protokollfuehrerin: Justizangestellte C. Wollersheim",
)

# 22 Vergleichsvereinbarung
make_docx(
    D / "22_vergleichsvereinbarung_rheinpark_2026-11-24.docx",
    VERWALTER_KOPF,
    "Vergleichsvereinbarung",
    [
        "Zwischen Rechtsanwalt Dr. Carsten Hellwege als Insolvenzverwalter und der Rheinpark Gewerbeimmobilien GmbH & Co. KG wird folgender Vergleich geschlossen:",
        "1. Die Beklagte zahlt an die Masse EUR 155.000,00 in zwei Raten (EUR 80.000,00 bis 15.12.2026, EUR 75.000,00 bis 31.01.2027).",
        "2. Mit vollstaendiger Zahlung sind saemtliche wechselseitigen Anspruche aus dem Grundstuecksverkauf vom 12.11.2025 erledigt.",
        "3. Die Kosten des Rechtsstreits werden gegeneinander aufgehoben.",
    ],
    "Dr. Carsten Hellwege\nRechtsanwalt, Insolvenzverwalter",
)

# 23 Zahlungsklage gegen Stefan Vondering
make_docx(
    D / "23_klageschrift_stefan_vondering_ag_moenchengladbach.docx",
    VERWALTER_KOPF,
    "Klageschrift",
    [
        "Amtsgericht Moenchengladbach",
        "Hohenzollernstrasse 157, 41061 Moenchengladbach",
        "",
        "In dem Rechtsstreit",
        "Rechtsanwalt Dr. Carsten Hellwege, als Insolvenzverwalter ueber das Vermoegen der Vondering Metallform GmbH",
        "- Klaeger -",
        "gegen",
        "Herrn Stefan Vondering, Inhaber der Vondering Immobilien e.K., Aachener Strasse 220, 41063 Moenchengladbach",
        "- Beklagter -",
        "",
        "wird Klage erhoben mit dem Antrag, den Beklagten zu verurteilen, an den Klaeger EUR 60.000,00 nebst Zinsen seit dem 29.06.2026 zu zahlen.",
        "## Begruendung",
        "Die als 'Vermittlungsprovision' bezeichnete Zahlung erfolgte unentgeltlich im Sinne des Paragraf 134 InsO, da der Beklagte keine werthaltige Vermittlungsleistung erbracht hat; der Notarvertrag weist ausdruecklich aus, dass Maklerkosten nicht angefallen sind. Die Provisionsvereinbarung vom 05.11.2025 datiert eine Woche vor der Beurkundung und wurde erst nach dem eigenen Erstkontakt der Erwerberin am 29.09.2025 erstellt.",
    ],
    "Dr. Carsten Hellwege\nRechtsanwalt, Insolvenzverwalter",
)

# 24 Versaeumnisurteil / Anerkenntnis
make_docx(
    D / "24_versaeumnisurteil_ag_moenchengladbach_2026-10-08.docx",
    "Amtsgericht Moenchengladbach\nHohenzollernstrasse 157, 41061 Moenchengladbach",
    "Versaeumnisurteil",
    [
        "Az. 12 C 388/26",
        "",
        "Der Beklagte Stefan Vondering ist trotz ordnungsgemaesser Ladung im Termin vom 08.10.2026 nicht erschienen und hat sich zur Klage nicht schriftsaetzlich geaeussert.",
        "Es ergeht folgendes Versaeumnisurteil: Der Beklagte wird verurteilt, an den Klaeger EUR 60.000,00 nebst Zinsen in Hoehe von 5 Prozentpunkten ueber dem Basiszinssatz seit dem 29.06.2026 zu zahlen. Der Beklagte traegt die Kosten des Rechtsstreits.",
        "Moenchengladbach, 08.10.2026",
    ],
    "Richterin am Amtsgericht Dr. Franziska Lohmann",
)

# 25 Kostenfestsetzung + Vollstreckung Abschluss
make_docx(
    D / "25_kostenfestsetzungsbeschluss_und_vollstreckungsvermerk.docx",
    VERWALTER_KOPF,
    "Kostenfestsetzungsbeschluss und Abschlussvermerk",
    [
        "Das Amtsgericht Moenchengladbach setzt die von Stefan Vondering an den Klaeger zu erstattenden Kosten auf EUR 4.238,60 fest (Az. 12 C 388/26).",
        "## Abschlussvermerk des Verwalters",
        "Der Vergleichsbetrag aus dem Verfahren gegen die Rheinpark Gewerbeimmobilien GmbH & Co. KG (EUR 155.000,00) ist vollstaendig auf dem Massekonto eingegangen. Gegen Stefan Vondering wurde nach fruchtlosem Fristablauf die Zwangsvollstreckung aus dem Versaeumnisurteil eingeleitet; eine Kontopfaendung bei der Sparkasse Moenchengladbach erbrachte EUR 22.400,00, die Restforderung von EUR 37.600,00 zuzueglich Kosten bleibt tituliert offen.",
        "Beide Anfechtungskomplexe sind damit wirtschaftlich abgeschlossen; die Akte wird zur Schlussrechnungslegung vorgemerkt.",
    ],
    "Dr. Carsten Hellwege\nRechtsanwalt, Insolvenzverwalter",
)

# Fristenliste CSV im csv/ Ordner
make_csv(
    D / "csv" / "kontobewegungen_stefan_vondering_2025.csv",
    ["Datum", "Betrag (EUR)", "Verwendungszweck"],
    [
        ["12.11.2025", "60.000,00", "Vermittlungsprovision Grundstuecksverkauf Krefelder Strasse 214"],
        ["14.11.2025", "-18.500,00", "Ueberweisung an Ehefrau L. Vondering, Verwendungszweck Darlehen"],
        ["20.11.2025", "-9.900,00", "Kfz-Kauf Autohaus Niederrhein"],
        ["02.12.2025", "-6.200,00", "Bareinzahlung eigenes Geschaeftskonto Vondering Immobilien e.K."],
    ],
)
make_csv(
    D / "csv" / "fristenliste_verjaehrung_paragraf_146_inso.csv",
    ["Anspruch", "Kenntnis Verwalter ab", "Verjaehrung (3 Jahre)", "Status"],
    [
        ["Anfechtung Grundstuecksverkauf Rheinpark", "01.06.2026", "31.12.2029", "gewahrt, Klage erhoben 16.07.2026"],
        ["Anfechtung Provisionszahlung Stefan Vondering", "01.06.2026", "31.12.2029", "gewahrt, Klage erhoben 29.06.2026"],
    ],
)

print("Moenchengladbach Kernstuecke 16-25 sowie csv/ erzeugt.")
