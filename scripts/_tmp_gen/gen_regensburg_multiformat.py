#!/usr/bin/env python3
"""Multi-Format-Ergaenzungen fuer insolvenzanfechtung-gesellschafterdarlehen-cash-pool-regensburg."""
import sys
sys.path.insert(0, "/home/user/workspace/legal-work/target/scripts/_tmp_gen")
from aktenbau import make_eml, make_xlsx, make_jpg, make_csv, TESTAKTEN

D = TESTAKTEN / "insolvenzanfechtung-gesellschafterdarlehen-cash-pool-regensburg"

make_eml(
    D / "eml" / "2026-12-20_ladung_sv_ruckdeschel.eml",
    "geschaeftsstelle@lg-regensburg.justiz.bayern.de",
    "immel@immel-recht.de",
    "Bestellung Sachverstaendiger Ruckdeschel - Az. 2 O 987/26",
    "Sun, 20 Dec 2026 09:00:00 +0100",
    "Sehr geehrter Herr Dr. Immel,\n\n"
    "das Gericht hat Diplom-Kaufmann Anton Ruckdeschel zum Sachverstaendigen bestellt. "
    "Der Gutachtenauftrag wird in Kuerze uebersandt.\n\n"
    "Mit freundlichen Gruessen\nGeschaeftsstelle, Landgericht Regensburg",
)

make_eml(
    D / "eml" / "2027-06-23_urteilszustellung_stadlbauer.eml",
    "poststelle@lg-regensburg.justiz.bayern.de",
    "kanzlei@stadlbauer-insolvenz.de",
    "Zustellung Urteil 2 O 987/26",
    "Wed, 23 Jun 2027 08:30:00 +0200",
    "Sehr geehrter Herr Dr. Stadlbauer,\n\n"
    "anbei die Zustellung des Urteils vom 22.06.2027 in Sachen Stadlbauer ./. AVR Automotive "
    "Beteiligungs GmbH, Az. 2 O 987/26.\n\n"
    "Mit freundlichen Gruessen\nPoststelle, Landgericht Regensburg",
)

make_eml(
    D / "eml" / "2027-09-15_avr_uebergabe_maschinenpark.eml",
    "wenng@avr-automotive.de",
    "kanzlei@stadlbauer-insolvenz.de",
    "Uebergabe des Maschinenparks",
    "Wed, 15 Sep 2027 11:15:00 +0200",
    "Sehr geehrter Herr Dr. Stadlbauer,\n\n"
    "wir bestaetigen die heutige Uebergabe des Maschinenparks gemaess Anlagenverzeichnis vom "
    "16.06.2025 an die Masse sowie die Ueberweisung von 654.320,00 EUR (Urteilssumme nebst Zinsen) "
    "auf das Massekonto.\n\n"
    "Mit freundlichen Gruessen\nDr. Carola Wenng",
)

make_xlsx(
    D / "xlsx" / "streitwertberechnung_kostenfestsetzung.xlsx",
    "Streitwert",
    ["Position", "Betrag EUR"],
    [
        ["Zahlungsantrag (Saldenabbau)", 640000.00],
        ["Herausgabeantrag Maschinenpark (Buchwert)", 1180000.00],
        ["Gesamtstreitwert", 1820000.00],
        ["Verfahrensgebuehr 1,3", 12480.00],
        ["Terminsgebuehr 1,2", 11520.00],
        ["Auslagen und Sachverstaendigenkosten", 680.00],
        ["Gesamtkosten", 24680.00],
    ],
    title="Kostenberechnung 2 O 987/26",
)

make_csv(
    D / "csv" / "zahlungseingang_masse.csv",
    ["Datum", "Betrag_EUR", "Vorgang"],
    [
        ["2027-09-12", "654320,00", "Urteilssumme nebst Zinsen"],
        ["2027-09-15", "0,00", "Herausgabe Maschinenpark (Sachwert)"],
    ],
)

make_jpg(
    D / "jpg" / "maschinenpark_donaupart_werkshalle.jpg",
    "Werkshalle Donaupart Praezisionstechnik GmbH",
    [
        "Osttangente 44, 93055 Regensburg",
        "Aufnahme vom 16.06.2025 (Bestandsaufnahme vor Sicherungsuebereignung)",
        "Zehn CNC-Bearbeitungszentren, Gesamtbuchwert 1.180.000 EUR",
        "Zustand: betriebsbereit, laufende Produktion zum Aufnahmezeitpunkt",
    ],
)

print("Regensburg Multi-Format erzeugt.")
