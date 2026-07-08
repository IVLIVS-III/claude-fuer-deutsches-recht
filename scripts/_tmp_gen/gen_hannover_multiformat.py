#!/usr/bin/env python3
"""Multi-Format-Ergaenzung fuer Hannover 15b-InsO-Haftungsakte."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from aktenbau import make_eml, make_xlsx, TESTAKTEN

SLUG = "geschaeftsfuehrerhaftung-15b-inso-zahlungen-nach-insolvenzreife-hannover"
D = TESTAKTEN / SLUG

mails = [
    ("2026-12-16_teilanerkenntnis_ankuendigung", "c.lohgerber@lohgerber-voss.de", "h.wittkopp@iv-wittkopp-hannover.de",
     "Teilanerkenntnis und Vergleichsangebot 21 O 156/26", "Wed, 16 Dec 2026 16:00:00 +0100",
     "Sehr geehrte Frau Dr. Wittkopp,\n\nwir kuendigen ein Teilanerkenntnis sowie ein Vergleichsangebot fuer den "
     "verbleibenden Streitgegenstand an. Details folgen im naechsten Schriftsatz.\n\n"
     "Mit freundlichen Gruessen\nDr. Cornelius Lohgerber"),
    ("2027-02-10_zahlungseingang_bestaetigung_hannover", "h.wittkopp@iv-wittkopp-hannover.de", "c.lohgerber@lohgerber-voss.de",
     "Zahlungseingang aus Urteil und Vergleich bestaetigt", "Wed, 10 Feb 2027 09:30:00 +0100",
     "Sehr geehrter Herr Dr. Lohgerber,\n\nwir bestaetigen den vollstaendigen Zahlungseingang von EUR 57.000,00 "
     "(Teilanerkenntnis und Vergleich) auf dem Massekonto.\n\nMit freundlichen Gruessen\nDr. Henrike Wittkopp"),
]
for fname, frm, to, subj, date, body in mails:
    make_eml(D / "eml" / f"{fname}.eml", frm, to, subj, date, body)

make_xlsx(
    D / "xlsx" / "aufteilung_zahlungen_privilegiert_nicht_privilegiert.xlsx",
    "Zahlungsaufteilung",
    ["Kategorie", "Betrag (EUR)", "Einordnung"],
    [
        ["Zug-um-Zug-Wareneinkauf", "74.300,00", "privilegiert, Sec. 15b Abs. 4 S. 2 InsO"],
        ["Energie/Versicherung", "35.600,00", "privilegiert, Schadensabwendung"],
        ["AN-Anteile Sozialversicherung", "48.400,00", "privilegiert, Sec. 266a StGB"],
        ["Summe anerkannt", "158.300,00", "-"],
        ["Nettoloehne", "387.200,00", "nicht privilegiert"],
        ["AG-Anteile Sozialversicherung", "48.400,00", "nicht privilegiert"],
        ["Mieten", "448.000,00", "nicht privilegiert"],
        ["Leasing", "12.000,00", "nicht privilegiert"],
        ["Umsatzsteuer", "95.200,00", "nicht privilegiert, Sec. 15b Abs. 8 greift nicht"],
        ["Lohnsteuer", "41.300,00", "nicht privilegiert, Sec. 15b Abs. 8 greift nicht"],
        ["Beraterhonorar Ohlendorf Beteiligungs-UG", "48.000,00", "nicht privilegiert, zusaetzlich Sec. 15b Abs. 5 InsO"],
        ["Erstattungsbetrag gesamt", "1.080.100,00", "Klageforderung"],
    ],
    title="Aufteilung Zahlungen nach Insolvenzreife (Anspruchsschreiben/Replik IV)",
)

print("Multiformat Hannover erzeugt.")
