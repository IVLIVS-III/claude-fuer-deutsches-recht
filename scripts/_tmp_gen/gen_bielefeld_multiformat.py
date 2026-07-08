#!/usr/bin/env python3
"""Multi-Format-Ergaenzung fuer insolvenzanfechtung-kongruente-deckung-lieferant-mahnlauf-bielefeld."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from aktenbau import make_eml, make_xlsx, make_jpg, TESTAKTEN

SLUG = "insolvenzanfechtung-kongruente-deckung-lieferant-mahnlauf-bielefeld"
D = TESTAKTEN / SLUG

mails = [
    ("2026-07-14_uebersendung_klageerwiderung", "y.broscheit@broscheit-weyland.de", "f.sanftleben@ivkanzlei-sanftleben.de",
     "Uebersendung Klageerwiderung 12 O 47/26", "Tue, 14 Jul 2026 17:20:00 +0200",
     "Sehr geehrte Frau Dr. Sanftleben,\n\nanbei erhalten Sie die Klageerwiderung in vorbezeichneter Sache. Wir "
     "bitten um Kenntnisnahme.\n\nMit freundlichen Gruessen\nDr. Yannick Broscheit"),
    ("2026-12-05_vergleich_bestaetigung", "f.sanftleben@ivkanzlei-sanftleben.de", "y.broscheit@broscheit-weyland.de",
     "Vergleich 12 O 47/26 - Feststellungsbeschluss liegt vor", "Fri, 05 Dec 2026 10:05:00 +0100",
     "Sehr geehrter Herr Dr. Broscheit,\n\nder Feststellungsbeschluss des Landgerichts Bielefeld liegt vor. Wir "
     "bitten um fristgerechte Zahlung der ersten Rate bis zum 30.12.2026 auf das Massekonto.\n\n"
     "Mit freundlichen Gruessen\nDr. Friederike Sanftleben"),
]
for fname, frm, to, subj, date, body in mails:
    make_eml(D / "eml" / f"{fname}.eml", frm, to, subj, date, body)

make_xlsx(
    D / "xlsx" / "liquiditaetsluecke_berechnung_sv_wruck.xlsx",
    "Liquiditaetsluecke",
    ["Stichtag", "Liquide Mittel (EUR)", "Faellige Verbindlichkeiten (EUR)", "Deckungsquote (%)"],
    [
        ["31.08.2025", "42.100,00", "398.000,00", "10,6"],
        ["30.09.2025", "31.400,00", "412.500,00", "7,6"],
        ["31.10.2025", "22.900,00", "437.100,00", "5,2"],
        ["30.11.2025", "18.200,00", "461.800,00", "3,9"],
        ["31.12.2025", "14.700,00", "479.300,00", "3,1"],
    ],
    title="Liquiditaetsluecke Teutoburger Moebelwerk (SV-Gutachten Wruck)",
)

make_jpg(
    D / "jpg" / "produktionshalle_moebelwerk_baender_still.jpg",
    "Foto: Produktionshalle Teutoburger Moebelwerk GmbH",
    [
        "Aufnahme im Rahmen eines Kundenbesuchs des Vertriebsleiters",
        "Datum: 05.12.2025",
        "Zustand: reduzierter Schichtbetrieb, teilweise stillstehende Baender",
    ],
)

print("Multiformat Bielefeld erzeugt.")
