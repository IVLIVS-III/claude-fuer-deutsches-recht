#!/usr/bin/env python3
"""Multi-Format-Ergaenzungen fuer insolvenzanfechtung-schenkung-familie-oldenburg."""
import sys
sys.path.insert(0, "/home/user/workspace/legal-work/target/scripts/_tmp_gen")
from aktenbau import make_eml, make_xlsx, make_jpg, make_csv, TESTAKTEN

D = TESTAKTEN / "insolvenzanfechtung-schenkung-familie-oldenburg"

make_eml(
    D / "eml" / "2026-12-05_ladung_zeuge_wienken.eml",
    "geschaeftsstelle@lg-oldenburg.justiz.niedersachsen.de",
    "bruns@bruns-kollegen.de",
    "Ladung des Zeugen Wienken - Az. 5 O 612/26",
    "Sat, 05 Dec 2026 09:30:00 +0100",
    "Sehr geehrter Herr Dr. Bruns,\n\n"
    "hiermit wird der Zeuge Hartmut Wienken zum Termin am 16.02.2027, 09:30 Uhr, Saal 245, "
    "geladen.\n\n"
    "Mit freundlichen Gruessen\nGeschaeftsstelle, Landgericht Oldenburg",
)

make_eml(
    D / "eml" / "2027-05-12_urteilszustellung_feddersen.eml",
    "poststelle@lg-oldenburg.justiz.niedersachsen.de",
    "kanzlei@feddersen-osterloh.de",
    "Zustellung Urteil 5 O 612/26",
    "Wed, 12 May 2027 08:15:00 +0200",
    "Sehr geehrter Herr Dr. Feddersen,\n\n"
    "anbei die Zustellung des Urteils vom 11.05.2027 in Sachen Feddersen ./. Hollmann u.a., "
    "Az. 5 O 612/26.\n\n"
    "Mit freundlichen Gruessen\nPoststelle, Landgericht Oldenburg",
)

make_eml(
    D / "eml" / "2027-08-31_zahlungsbestaetigung_bruns.eml",
    "bruns@bruns-kollegen.de",
    "kanzlei@feddersen-osterloh.de",
    "Zahlungsbestaetigung - alle drei Beklagten",
    "Tue, 31 Aug 2027 16:00:00 +0200",
    "Sehr geehrter Herr Dr. Feddersen,\n\n"
    "wir bestaetigen, dass alle drei Mandanten die titulierten Betraege nebst Zinsen und Kosten "
    "heute vollstaendig auf das Massekonto ueberwiesen haben. Damit ist der Rechtsstreit "
    "5 O 612/26 erledigt.\n\n"
    "Mit freundlichen Gruessen\nDr. Heiner Bruns",
)

make_xlsx(
    D / "xlsx" / "kostenverteilung_urteil.xlsx",
    "Kostenverteilung",
    ["Beklagte", "Hauptforderung_EUR", "Kosten_EUR", "Gesamt_EUR"],
    [
        ["Karin Hollmann", 27900.00, 3240.00, 31140.00],
        ["Lena Hollmann", 30000.00, 4180.00, 34180.00],
        ["Uwe Tietjen", 19800.00, 3560.00, 23360.00],
        ["Summe", 77700.00, 10980.00, 88680.00],
    ],
    title="Hollmann Bau- und Sanierungs GmbH - Kostenverteilung 5 O 612/26",
)

make_csv(
    D / "csv" / "zahlungseingaenge_masse.csv",
    ["Datum", "Zahler", "Betrag_EUR"],
    [
        ["2027-08-31", "Karin Hollmann", "31140,00"],
        ["2027-08-31", "Lena Hollmann", "34180,00"],
        ["2027-08-31", "Uwe Tietjen", "23360,00"],
    ],
)

make_jpg(
    D / "jpg" / "firmensitz_ammerlaender_heerstrasse.jpg",
    "Firmensitz Hollmann Bau- und Sanierungs GmbH",
    [
        "Ammerlaender Heerstrasse 214, 26129 Oldenburg",
        "Aufnahme vom 28.05.2026 (Bestandsaufnahme durch Insolvenzverwalter)",
        "Buero- und Lagergebaeude mit angrenzender Werkstatt",
        "Zustand: Geschaeftsbetrieb eingestellt, Gebaeude vermietet",
    ],
)

print("Oldenburg Multi-Format erzeugt.")
