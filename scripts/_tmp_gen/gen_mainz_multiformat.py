#!/usr/bin/env python3
"""Multi-Format-Ergaenzungen fuer insolvenzanfechtung-kontokorrent-rueckfuehrung-kreditlinie-mainz."""
import sys
sys.path.insert(0, "/home/user/workspace/legal-work/target/scripts/_tmp_gen")
from aktenbau import make_eml, make_xlsx, make_jpg, make_csv, TESTAKTEN

D = TESTAKTEN / "insolvenzanfechtung-kontokorrent-rueckfuehrung-kreditlinie-mainz"

make_eml(
    D / "eml" / "2026-11-15_ladung_zeugin_vietinghoff.eml",
    "geschaeftsstelle@lg-mainz.justiz.rlp.de",
    "cammann@cammann-weyrich.de",
    "Ladung der Zeugin Sandra Vietinghoff - Termin 09.02.2027",
    "Fri, 15 Nov 2026 10:05:00 +0100",
    "Sehr geehrte Frau Dr. Cammann,\n\n"
    "hiermit wird die Zeugin Sandra Vietinghoff zum Termin am 09.02.2027, 10:00 Uhr, Saal 118, "
    "geladen. Bitte sorgen Sie fuer die Ladung.\n\n"
    "Mit freundlichen Gruessen\nGeschaeftsstelle, Landgericht Mainz",
)

make_eml(
    D / "eml" / "2027-05-19_urteilszustellung_bernstorf.eml",
    "poststelle@lg-mainz.justiz.rlp.de",
    "kanzlei@bernstorf-insolvenz.de",
    "Zustellung Urteil 8 O 214/26",
    "Wed, 19 May 2027 09:00:00 +0200",
    "Sehr geehrte Frau Dr. Bernstorf,\n\n"
    "anbei die Zustellung des Urteils vom 18.05.2027 in Sachen Bernstorf ./. Sparkasse "
    "Weinbergland Mainz, Az. 8 O 214/26.\n\n"
    "Mit freundlichen Gruessen\nPoststelle, Landgericht Mainz",
)

make_eml(
    D / "eml" / "2027-06-28_zahlungsbestaetigung_sparkasse.eml",
    "tremmel@sparkasse-weinbergland.de",
    "kanzlei@bernstorf-insolvenz.de",
    "Zahlungsbestaetigung Urteilssumme",
    "Mon, 28 Jun 2027 15:40:00 +0200",
    "Sehr geehrte Frau Dr. Bernstorf,\n\n"
    "wir bestaetigen die heutige Ueberweisung von 372.450,00 EUR (Urteilssumme nebst Zinsen) "
    "auf das Massekonto. Damit ist der Rechtsstreit 8 O 214/26 aus unserer Sicht erledigt.\n\n"
    "Mit freundlichen Gruessen\nJoerg Tremmel",
)

make_xlsx(
    D / "xlsx" / "urteilssumme_zinsberechnung.xlsx",
    "Zinsberechnung",
    ["Position", "Betrag EUR", "Zeitraum"],
    [
        ["Hauptforderung", 360000.00, "Verrechnungssaldo"],
        ["Zinssatz p.a.", 8.12, "Basiszinssatz + 5 Prozentpunkte (Stand 2027)"],
        ["Zinslauf Beginn", 0, "01.05.2026"],
        ["Zinslauf Ende", 0, "28.06.2027"],
        ["Zinsen (kumuliert)", 12450.00, "rund 424 Tage"],
        ["Gesamtsumme", 372450.00, "Zahlung 28.06.2027"],
    ],
    title="Domblick Weinkellerei - Zinsberechnung Urteilssumme",
)

make_csv(
    D / "csv" / "fristenliste_berufung_verjaehrung.csv",
    ["Datum", "Ereignis"],
    [
        ["2027-05-18", "Urteil verkuendet"],
        ["2027-06-01", "Berufungsfrist eingegangen (Verzicht)"],
        ["2027-06-20", "Rechtskraft eingetreten"],
        ["2027-06-28", "Zahlungseingang Urteilssumme"],
    ],
)

make_jpg(
    D / "jpg" / "weinkellerei_lagerhalle_laubenheim.jpg",
    "Lagerhalle Domblick Weinkellerei-Betriebs-GmbH",
    [
        "Laubenheimer Hoehe 12, 55131 Mainz",
        "Aufnahme vom 06.05.2026 (Bestandsaufnahme durch Insolvenzverwalterin)",
        "Weinlager mit rund 40.000 Flaschen Restbestand",
        "Zustand: versiegelt, Inventarisierung abgeschlossen",
    ],
)

print("Mainz Multi-Format erzeugt.")
