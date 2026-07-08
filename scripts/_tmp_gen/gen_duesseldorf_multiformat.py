#!/usr/bin/env python3
"""Multi-Format-Ergaenzungen fuer starug-aufhebung-holding-duesseldorf-ix-zb-18-25."""
import sys
sys.path.insert(0, "/home/user/workspace/legal-work/target/scripts/_tmp_gen")
from aktenbau import make_eml, make_xlsx, make_jpg, make_csv, TESTAKTEN

D = TESTAKTEN / "starug-aufhebung-holding-duesseldorf-ix-zb-18-25"

# EML 1 - Verwalter informiert Geschaeftsfuehrung ueber Eroeffnung
make_eml(
    D / "eml" / "2026-08-04_verwalter_information_eroeffnung.eml",
    "kanzlei@ovelgoenne-rae.de",
    "wefing@silberweiher-beteiligung.de",
    "Insolvenzverfahren eroeffnet - naechste Schritte",
    "Mon, 04 Aug 2026 08:45:00 +0200",
    "Sehr geehrter Herr Dr. Wefing,\n\n"
    "das Amtsgericht Duesseldorf hat gestern das Insolvenzverfahren ueber das Vermoegen der "
    "Silberweiher Beteiligungs GmbH eroeffnet (Az. 512 IN 88/26). Ich bitte Sie, mir bis zum "
    "11.08.2026 saemtliche Geschaeftsunterlagen, Kontoauszuege und die Buchhaltung der letzten "
    "drei Jahre zu uebergeben.\n\n"
    "Mit freundlichen Gruessen\nDr. Markus Ovelgoenne",
)

# EML 2 - Rheinboden meldet Forderung an
make_eml(
    D / "eml" / "2026-08-25_rheinboden_forderungsanmeldung_begleitschreiben.eml",
    "recovery@rheinboden-kreditbank.de",
    "kanzlei@ovelgoenne-rae.de",
    "Forderungsanmeldung Silberweiher Beteiligungs GmbH",
    "Tue, 25 Aug 2026 14:12:00 +0200",
    "Sehr geehrter Herr Dr. Ovelgoenne,\n\n"
    "anbei uebersenden wir unsere Forderungsanmeldung zur Insolvenztabelle nebst Anlagen "
    "(Buergschaftsurkunde, Faelligstellungsschreiben, Kostenfestsetzungsbeschluss BGH). "
    "Fuer Rueckfragen stehen wir gerne zur Verfuegung.\n\n"
    "Mit freundlichen Gruessen\nRecovery Management, Rheinboden Kreditbank AG",
)

# EML 3 - Quirrenbach an Wefing zum Abschluss
make_eml(
    D / "eml" / "2027-05-12_quirrenbach_abschlussmitteilung.eml",
    "a.quirrenbach@quirrenbach-partner.de",
    "wefing@silberweiher-beteiligung.de",
    "Abschluss des Mandats - Silberweiher Beteiligungs GmbH",
    "Wed, 12 May 2027 16:20:00 +0200",
    "Sehr geehrter Herr Dr. Wefing,\n\n"
    "mit der Aufhebung des Insolvenzverfahrens am 30.04.2027 ist das Verfahren rechtskraeftig "
    "abgeschlossen. Ich uebersende Ihnen anbei den Schlussvermerk zu unserer Handakte sowie eine "
    "Kopie des Aufhebungsbeschlusses. Vielen Dank fuer die vertrauensvolle Zusammenarbeit ueber "
    "die vergangenen zweieinhalb Jahre.\n\n"
    "Mit freundlichen Gruessen\nDr. Alexander Quirrenbach",
)

# XLSX - Massekostenrechnung
make_xlsx(
    D / "xlsx" / "masseverzeichnis_schlussrechnung.xlsx",
    "Masseverzeichnis",
    ["Position", "Betrag EUR", "Bemerkung"],
    [
        ["Kassenbestand bei Eroeffnung", 4180.00, "Stand 03.08.2026"],
        ["Kostenvorschuss Geschaeftsfuehrung", 6000.00, "Einzahlung 10.08.2026"],
        ["Verwertungserloes Bueroausstattung", 890.00, "Versteigerung 15.11.2026"],
        ["Gesamtmasse", 11070.00, "Summe"],
        ["Gerichtskosten", 1200.00, ""],
        ["Verwaltervergütung", 8280.00, "Festsetzung durch Insolvenzgericht"],
        ["Verfahrenskosten gesamt", 9480.00, "Summe"],
        ["Verteilungsmasse", 1590.32, "Quote 0,236 Prozent"],
    ],
    title="Silberweiher Beteiligungs GmbH - Schlussrechnung 512 IN 88/26",
)

# CSV - Forderungstabelle
make_csv(
    D / "csv" / "forderungstabelle_512_in_88_26.csv",
    ["Glaeubiger", "Forderung_EUR", "Rang", "Status"],
    [
        ["Rheinboden Kreditbank AG", "666606,47", "einfache Insolvenzforderung", "festgestellt"],
        ["Fedder & Sohst", "1897,00", "einfache Insolvenzforderung", "festgestellt"],
        ["Finanzamt Duesseldorf-Nord", "3240,00", "einfache Insolvenzforderung", "festgestellt"],
        ["Sonstige Kleinglaeubiger", "2114,90", "einfache Insolvenzforderung", "festgestellt"],
    ],
)

# CSV - Verfahrenschronologie
make_csv(
    D / "csv" / "verfahrenschronologie.csv",
    ["Datum", "Ereignis", "Aktenzeichen"],
    [
        ["2024-11-08", "Restrukturierungsanzeige Paragraf 31 StaRUG", "603 RES 6/24"],
        ["2024-12-02", "Faelligstellung Rheinboden", ""],
        ["2024-12-06", "Anzeige Zahlungsunfaehigkeit Paragraf 32 Abs. 3 StaRUG", ""],
        ["2025-01-15", "Aufhebungsbeschluss AG Duesseldorf", "603 RES 6/24"],
        ["2025-03-25", "Zurueckweisung LG, Zulassung Rechtsbeschwerde", "314c T 4/25"],
        ["2026-04-23", "BGH-Beschluss Zurueckweisung Rechtsbeschwerde", "IX ZB 18/25"],
        ["2026-05-28", "Eigenantrag Insolvenzverfahren", ""],
        ["2026-08-03", "Eroeffnungsbeschluss", "512 IN 88/26"],
        ["2027-04-30", "Aufhebungsbeschluss Insolvenzverfahren", "512 IN 88/26"],
    ],
)

# JPG
make_jpg(
    D / "jpg" / "grafenberger_allee_214_geschaeftssitz.jpg",
    "Geschaeftssitz Silberweiher Beteiligungs GmbH",
    [
        "Grafenberger Allee 214, 40237 Duesseldorf",
        "Aufnahme vom 12.08.2026 (Bestandsaufnahme durch Insolvenzverwalter)",
        "Buerogebaeude, 3. Obergeschoss, angemietete Flaeche 85 qm",
        "Zustand: geraeumt, Mietvertrag zum 30.09.2026 gekuendigt",
    ],
)

print("Duesseldorf Multi-Format erzeugt.")
