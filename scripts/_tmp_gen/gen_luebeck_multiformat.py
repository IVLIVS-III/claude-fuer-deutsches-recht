#!/usr/bin/env python3
"""Multi-Format-Ergaenzung fuer Luebeck Krankenkasse-Anfechtungsakte."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from aktenbau import make_eml, make_xlsx, TESTAKTEN

SLUG = "insolvenzanfechtung-kongruente-deckung-krankenkasse-nach-antrag-luebeck"
D = TESTAKTEN / SLUG

mails = [
    ("2026-11-25_vergleichsvorschlag_bkk", "a.wehrmann@bkk-ostseekueste.de", "h.petersen@iv-petersen-luebeck.de",
     "Vergleichsvorschlag 4 O 91/26", "Wed, 25 Nov 2026 11:20:00 +0100",
     "Sehr geehrter Herr Dr. Petersen,\n\nanbei unser Vergleichsvorschlag in vorbezeichneter Sache.\n\n"
     "Mit freundlichen Gruessen\nDr. Annegret Wehrmann"),
    ("2027-01-15_zahlungsbestaetigung_luebeck", "h.petersen@iv-petersen-luebeck.de", "a.wehrmann@bkk-ostseekueste.de",
     "Zahlungseingang Vergleichsbetrag bestaetigt", "Fri, 15 Jan 2027 10:00:00 +0100",
     "Sehr geehrte Frau Dr. Wehrmann,\n\nwir bestaetigen den Eingang von EUR 22.000,00 auf dem Massekonto. Die "
     "Angelegenheit ist damit erledigt.\n\nMit freundlichen Gruessen\nDr. Hauke Petersen"),
]
for fname, frm, to, subj, date, body in mails:
    make_eml(D / "eml" / f"{fname}.eml", frm, to, subj, date, body)

make_xlsx(
    D / "xlsx" / "beitragszahlungen_anfechtungszeitraum.xlsx",
    "Beitragszahlungen",
    ["Zahlungsdatum", "Betrag (EUR)", "Beitragsmonat"],
    [
        ["10.12.2025", "11.240,00", "November 2025"],
        ["14.01.2026", "11.980,00", "Dezember 2025"],
        ["06.02.2026", "11.560,00", "Januar 2026"],
    ],
    title="Beitragszahlungen an BKK Ostseekueste im Anfechtungszeitraum",
)

print("Multiformat Luebeck erzeugt.")
