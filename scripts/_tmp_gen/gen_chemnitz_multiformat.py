#!/usr/bin/env python3
"""Multi-Format-Ergaenzung fuer Chemnitz Bargeschaeft-Vorkasse-Akte."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from aktenbau import make_eml, make_xlsx, TESTAKTEN

SLUG = "insolvenzanfechtung-bargeschaeft-vorkasse-rohstofflieferant-chemnitz"
D = TESTAKTEN / SLUG

mails = [
    ("2026-12-10_vergleichsannahme_granova", "l.huesgen@ra-huesgen-dresden.de", "f.stollberg@iv-stollberg-chemnitz.de",
     "Annahme Vergleichsvorschlag 5 O 233/26", "Thu, 10 Dec 2026 14:30:00 +0100",
     "Sehr geehrte Frau Dr. Stollberg,\n\nnamens unserer Mandantin nehmen wir den Vergleichsvorschlag vom "
     "05.12.2026 an.\n\nMit freundlichen Gruessen\nDr. Lennart Huesgen"),
    ("2027-01-20_zahlungsbestaetigung", "f.stollberg@iv-stollberg-chemnitz.de", "l.huesgen@ra-huesgen-dresden.de",
     "Zahlungseingang Vergleichsbetrag bestaetigt", "Wed, 20 Jan 2027 09:40:00 +0100",
     "Sehr geehrter Herr Dr. Huesgen,\n\nwir bestaetigen den Eingang von EUR 45.000,00 auf dem Massekonto. Die "
     "Angelegenheit ist damit erledigt.\n\nMit freundlichen Gruessen\nDr. Friederike Stollberg"),
]
for fname, frm, to, subj, date, body in mails:
    make_eml(D / "eml" / f"{fname}.eml", frm, to, subj, date, body)

make_xlsx(
    D / "xlsx" / "zeitliche_zuordnung_zahlungen_lieferungen.xlsx",
    "Zeitzuordnung",
    ["Rechnung", "Zahlungsdatum", "Lieferdatum", "Abstand (Tage)", "Bargeschaeft"],
    [
        ["RE-2026-0098", "12.01.2026", "08.01.2026", "4", "ja"],
        ["RE-2026-0121", "02.02.2026", "29.01.2026", "4", "ja"],
        ["RE-2026-0142", "18.02.2026", "15.01.2026", "34", "nein"],
        ["RE-2026-0165", "10.03.2026", "05.03.2026", "5", "ja"],
        ["RE-2026-0187", "22.03.2026", "09.02.2026", "41", "nein"],
        ["RE-2026-0210", "08.04.2026", "15.02.2026", "52", "nein"],
    ],
    title="Zeitliche Zuordnung Zahlungen zu Lieferungen (SV-Gutachten Ottersbach)",
)

print("Multiformat Chemnitz erzeugt.")
