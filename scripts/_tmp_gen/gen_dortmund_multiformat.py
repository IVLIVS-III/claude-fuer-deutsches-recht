#!/usr/bin/env python3
"""Multi-Format-Ergaenzung fuer Dortmund Kontokorrent-Anfechtungsakte."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from aktenbau import make_eml, make_xlsx, TESTAKTEN

SLUG = "insolvenzanfechtung-kontokorrent-verrechnungen-geduldete-ueberziehung-dortmund"
D = TESTAKTEN / SLUG

mails = [
    ("2026-12-22_vergleichsvorschlag_uebersendung", "k.wehmeyer@iv-wehmeyer-dortmund.de", "m.terhardt@terhardt-cloppenburg.de",
     "Vergleichsvorschlag 8 O 112/26", "Tue, 22 Dec 2026 15:40:00 +0100",
     "Sehr geehrter Herr Dr. Terhardt,\n\nanbei erhalten Sie unseren Vergleichsvorschlag in vorbezeichneter Sache. "
     "Wir bitten um kurzfristige Rueckmeldung.\n\nMit freundlichen Gruessen\nDr. Konstantin Wehmeyer"),
    ("2027-02-04_zahlungseingang_bestaetigung", "k.wehmeyer@iv-wehmeyer-dortmund.de", "m.terhardt@terhardt-cloppenburg.de",
     "Zahlungseingang Vergleichsbetrag bestaetigt", "Thu, 04 Feb 2027 09:15:00 +0100",
     "Sehr geehrter Herr Dr. Terhardt,\n\nwir bestaetigen den Eingang des Vergleichsbetrags in Hoehe von "
     "EUR 52.000,00 auf dem Massekonto. Damit ist die Angelegenheit erledigt.\n\n"
     "Mit freundlichen Gruessen\nDr. Konstantin Wehmeyer"),
]
for fname, frm, to, subj, date, body in mails:
    make_eml(D / "eml" / f"{fname}.eml", frm, to, subj, date, body)

make_xlsx(
    D / "xlsx" / "aufteilung_kongruent_inkongruent_berechnung.xlsx",
    "Saldoaufteilung",
    ["Position", "Betrag (EUR)", "Einordnung"],
    [
        ["Hoechststand 05.02.2026", "309.900,00", "Ausgangswert"],
        ["Kreditlinie vertraglich", "250.000,00", "Grenze kongruent/inkongruent"],
        ["Rueckfuehrung geduldete Ueberziehung", "59.900,00", "inkongruent, Sec. 131 InsO"],
        ["Rueckfuehrung innerhalb Linie", "23.700,00", "kongruent, Sec. 130 InsO"],
        ["Tiefststand 08.04.2026", "221.480,00", "Zwischenwert"],
        ["Endsaldo 15.04.2026", "226.300,00", "Anfechtungszeitraumende"],
    ],
    title="Aufteilung Saldorueckfuehrung Volksbank Emscher-Hellweg",
)

print("Multiformat Dortmund erzeugt.")
