#!/usr/bin/env python3
"""Multi-Format-Ergaenzung Augsburg: eml, xlsx, jpg."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from aktenbau import make_eml, make_xlsx, make_jpg, TESTAKTEN

SLUG = "insolvenzanfechtung-vorsatzanfechtung-finanzamt-ratenzahlung-augsburg"
D = TESTAKTEN / SLUG

mails = [
    ("2026-11-02_terminsladung_beweisaufnahme", "poststelle@lg-augsburg.bayern.de", "kanzlei@brettschneider-recht.de",
     "Terminsladung 5 O 611/26 Beweisaufnahme", "Mon, 02 Nov 2026 09:15:00 +0100",
     "Sehr geehrte Damen und Herren,\n\nes ergeht Ladung zum Beweistermin am 20.01.2027, 09:00 Uhr.\n\n"
     "Mit freundlichen Gruessen\nGeschaeftsstelle 5. Zivilkammer"),
    ("2027-03-10_urteilszustellung", "poststelle@lg-augsburg.bayern.de", "kanzlei@brettschneider-recht.de",
     "Urteilszustellung 5 O 611/26", "Wed, 10 Mar 2027 15:00:00 +0100",
     "Sehr geehrte Damen und Herren,\n\nanbei die Zustellung des Urteils vom heutigen Tag.\n\n"
     "Mit freundlichen Gruessen\nGeschaeftsstelle 5. Zivilkammer"),
    ("2027-04-28_zahlungseingang_urteilssumme", "kanzlei@brettschneider-recht.de", "poststelle.aug-stadt@finanzamt.bayern.de",
     "Zahlungseingang Urteilssumme und Kosten bestaetigt", "Wed, 28 Apr 2027 10:30:00 +0200",
     "Sehr geehrte Damen und Herren,\n\nwir bestaetigen den vollstaendigen Eingang von EUR 356.940,20 auf dem "
     "Massekonto.\n\nMit freundlichen Gruessen\nDr. Simon Brettschneider"),
]
for fname, frm, to, subj, date, body in mails:
    make_eml(D / "eml" / f"{fname}.eml", frm, to, subj, date, body)

make_xlsx(
    D / "xlsx" / "massekostenkalkulation_urteil_finanzamt.xlsx",
    "Kalkulation",
    ["Position", "Betrag (EUR)", "Bemerkung"],
    [
        ["Urteilssumme (26 Raten + Sicherungsabtretung)", "338.000,00", "rechtskraeftig seit 12.04.2027"],
        ["Kostenerstattung Beklagter", "18.940,20", "Kostenfestsetzungsbeschluss vom 14.04.2027"],
        ["Sachverstaendigenkosten Osswald", "9.800,00", "aus der Masse verauslagt, anteilig erstattet"],
        ["Gerichtskosten", "6.480,00", "13 Prozent Kostenanteil Klaeger"],
        ["Nettoerloes fuer die Masse", "340.660,20", "356.940,20 - 6.480,00 - 9.800,00"],
    ],
    title="Massekostenkalkulation Anfechtung Finanzamt Augsburg-Stadt",
)

make_jpg(
    D / "jpg" / "fuhrpark_lechtal_spedition_uebersicht.jpg",
    "Anlage: Fuhrpark Lechtal Spedition und Logistik GmbH",
    [
        "28 Zugmaschinen, Standort Augsburg-Lechhausen",
        "Sicherungsabtretung Frachtforderungen vom 09.09.2024",
        "Betroffene Kunden: 14 Speditionsauftraggeber im Raum Bayern-Schwaben",
        "Foto-Vermerk im Rahmen der Anfechtungspruefung",
    ],
)

print("Multiformat Augsburg erzeugt.")
