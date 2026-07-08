#!/usr/bin/env python3
"""Multi-Format-Ergaenzungen fuer insolvenzanfechtung-inkongruente-deckung-warenlager-an-erfuellungs-statt-kassel."""
import sys
sys.path.insert(0, "/home/user/workspace/legal-work/target/scripts/_tmp_gen")
from aktenbau import make_eml, make_xlsx, make_jpg, make_csv, TESTAKTEN

D = TESTAKTEN / "insolvenzanfechtung-inkongruente-deckung-warenlager-an-erfuellungs-statt-kassel"

make_eml(
    D / "eml" / "2026-12-08_ladung_zeuge_kurrle.eml",
    "geschaeftsstelle@lg-kassel.justiz.hessen.de",
    "appelt@appelt-recht.de",
    "Bestellung Sachverstaendiger und Ladung Zeuge - Az. 4 O 318/26",
    "Tue, 08 Dec 2026 10:00:00 +0100",
    "Sehr geehrter Herr Dr. Appelt,\n\n"
    "das Gericht hat Diplom-Kaufmann Bernd Osterhage zum Sachverstaendigen bestellt und laedt "
    "zugleich den Zeugen Sascha Kurrle zum Beweistermin.\n\n"
    "Mit freundlichen Gruessen\nGeschaeftsstelle, Landgericht Kassel",
)

make_eml(
    D / "eml" / "2027-06-22_urteilszustellung_salzwedel.eml",
    "poststelle@lg-kassel.justiz.hessen.de",
    "kanzlei@salzwedel-insolvenz.de",
    "Zustellung Urteil 4 O 318/26",
    "Tue, 22 Jun 2027 08:45:00 +0200",
    "Sehr geehrte Frau Dr. Salzwedel,\n\n"
    "anbei die Zustellung des Urteils vom 21.06.2027 in Sachen Salzwedel ./. Daemmtec Werra GmbH, "
    "Az. 4 O 318/26.\n\n"
    "Mit freundlichen Gruessen\nPoststelle, Landgericht Kassel",
)

make_eml(
    D / "eml" / "2027-08-10_zahlungsbestaetigung_daemmtec.eml",
    "ostheim@daemmtec-werra.de",
    "kanzlei@salzwedel-insolvenz.de",
    "Zahlungsbestaetigung Urteilssumme",
    "Tue, 10 Aug 2027 14:20:00 +0200",
    "Sehr geehrte Frau Dr. Salzwedel,\n\n"
    "wir bestaetigen die heutige Ueberweisung von 142.370,00 EUR nebst Zinsen auf das Massekonto "
    "sowie die gleichzeitige Anmeldung unserer urspruenglichen Lieferantenforderung von "
    "118.000,00 EUR zur Insolvenztabelle gemaess Paragraf 144 InsO.\n\n"
    "Mit freundlichen Gruessen\nDieter Ostheim",
)

make_xlsx(
    D / "xlsx" / "berechnung_rueckgewaehranspruch.xlsx",
    "Berechnung",
    ["Position", "Betrag EUR"],
    [
        ["Warenlager Daemmplatten (663 Paletten)", 96000.00],
        ["Abtretung Hochbau Menzel", 14650.00],
        ["Abtretung Zimmerei Brandau", 9720.00],
        ["Gesamtsumme Rueckgewaehranspruch", 142370.00],
        ["Wiederauflebende Lieferantenforderung (Paragraf 144 InsO)", 118000.00],
    ],
    title="Fuldablick Baustoffhandel GmbH - Rueckgewaehrberechnung",
)

make_csv(
    D / "csv" / "verfahrenschronologie.csv",
    ["Datum", "Ereignis"],
    [
        ["2025-12-18", "Uebereignungs- und Tilgungsvereinbarung"],
        ["2026-02-09", "Eigenantrag"],
        ["2026-05-01", "Eroeffnungsbeschluss"],
        ["2026-09-07", "Klageschrift"],
        ["2027-06-21", "Urteil LG Kassel"],
        ["2027-07-26", "Rechtskraft"],
        ["2027-08-10", "Zahlungseingang"],
    ],
)

make_jpg(
    D / "jpg" / "lagerhalle_fuldablick_leipziger_strasse.jpg",
    "Lagerhalle Fuldablick Baustoffhandel GmbH",
    [
        "Leipziger Strasse 312, 34123 Kassel",
        "Aufnahme vom 19.12.2025 (Uebergabeprotokoll Daemmplatten-Lager)",
        "Regallager, nach Abholung weitgehend leergeraeumt",
        "Zustand: 663 von 665 Paletten abgeholt, zwei Paletten beschaedigt zurueckgelassen",
    ],
)

print("Kassel Multi-Format erzeugt.")
