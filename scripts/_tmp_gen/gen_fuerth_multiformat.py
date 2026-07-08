#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Erzeugt Multi-Format-Dateien fuer die Fuerth-Akte."""
import sys
sys.path.insert(0, "/home/user/workspace/legal-work/target/scripts/_tmp_gen")
from aktenbau import make_eml, make_csv, make_xlsx, make_jpg, TESTAKTEN

BASE = TESTAKTEN / "insolvenzanfechtung-inkongruente-deckung-zwangsvollstreckung-fuerth"

# EML
make_eml(
    BASE / "eml" / "2026-11-05_ladung_zeuge_karow.eml",
    frm="Geschaeftsstelle 4. Zivilkammer <zivilkammer4.geschaeftsstelle@lg-nuernberg-fuerth.bayern.de>",
    to="Dr. Sabine Ottmann <ottmann@kanzlei-ottmann-nbg.de>",
    subject="4 O 812/26 - Ladung des Zeugen Herbert Karow",
    date="Thu, 05 Nov 2026 09:14:00 +0100",
    body=(
        "Sehr geehrte Frau Rechtsanwaeltin Dr. Ottmann,\n\n"
        "in obiger Sache wird Termin zur Vernehmung des Zeugen Herbert Karow\n"
        "auf den 18.02.2027, 10:00 Uhr, Sitzungssaal 214, bestimmt.\n\n"
        "Wir bitten um Sicherstellung des persoenlichen Erscheinens des Zeugen.\n\n"
        "Mit freundlichen Gruessen\n"
        "Geschaeftsstelle 4. Zivilkammer"
    ),
    msgid_domain="lg-nuernberg-fuerth.bayern.de",
)

make_eml(
    BASE / "eml" / "2027-07-12_urteilszustellung_wehrfritz.eml",
    frm="Geschaeftsstelle 4. Zivilkammer <zivilkammer4.geschaeftsstelle@lg-nuernberg-fuerth.bayern.de>",
    to="Dr. Cornelius Wehrfritz <wehrfritz@insolvenz-nuernberg.de>",
    subject="4 O 812/26 - Zustellung des Urteils vom 09.07.2027",
    date="Mon, 12 Jul 2027 11:02:00 +0200",
    body=(
        "Sehr geehrter Herr Dr. Wehrfritz,\n\n"
        "anbei erhalten Sie das Urteil der Kammer vom 09.07.2027 zur weiteren Verwendung.\n"
        "Die Rechtsmittelfrist laeuft mit Zustellung an beide Parteien.\n\n"
        "Mit freundlichen Gruessen\n"
        "Geschaeftsstelle 4. Zivilkammer"
    ),
    msgid_domain="lg-nuernberg-fuerth.bayern.de",
)

make_eml(
    BASE / "eml" / "2027-09-15_zahlungsbestaetigung_karow.eml",
    frm="Buchhaltung Karow Verpackungswerk GmbH <buchhaltung@karow-verpackung.de>",
    to="Dr. Cornelius Wehrfritz <wehrfritz@insolvenz-nuernberg.de>",
    subject="Az. 4 O 812/26 - Zahlung erfolgt",
    date="Wed, 15 Sep 2027 14:47:00 +0200",
    body=(
        "Sehr geehrter Herr Dr. Wehrfritz,\n\n"
        "wir bestaetigen die heutige Ueberweisung von 44.930,45 EUR (Hauptforderung nebst Zinsen)\n"
        "auf das von Ihnen benannte Massekonto gemaess Urteil des LG Nuernberg-Fuerth vom 09.07.2027.\n\n"
        "Mit freundlichen Gruessen\n"
        "Buchhaltung Karow Verpackungswerk GmbH"
    ),
    msgid_domain="karow-verpackung.de",
)

# CSV: Verfahrenschronologie
make_csv(
    BASE / "csv" / "verfahrenschronologie.csv",
    ["Datum", "Ereignis"],
    [
        ["2026-02-18", "Barzahlung 9.750 EUR an der Warenrampe"],
        ["2026-02-25", "Kassenpfaendung 12.000 EUR"],
        ["2026-03-04", "Ueberweisung 20.000 EUR zur Abwendung der Vollstreckung"],
        ["2026-03-12", "Eigenantrag der Schuldnerin"],
        ["2026-06-01", "Eroeffnungsbeschluss AG Fuerth"],
        ["2026-06-22", "Anfechtungsschreiben des Verwalters"],
        ["2026-07-01", "Erwiderung Ra. Ottmann"],
        ["2026-09-14", "Klageschrift eingereicht"],
        ["2026-10-26", "Klageerwiderung"],
        ["2026-11-16", "Replik"],
        ["2026-12-07", "Duplik"],
        ["2026-12-21", "Beweisbeschluss"],
        ["2027-02-18", "Zeugenvernehmung Karow"],
        ["2027-04-30", "Sachverstaendigengutachten Fessenmayer"],
        ["2027-07-09", "Urteil LG Nuernberg-Fuerth"],
        ["2027-08-12", "Rechtskraft"],
        ["2027-09-15", "Zahlungseingang 44.930,45 EUR"],
        ["2027-09-20", "Schlussvermerk"],
    ],
)

# XLSX: Berechnung Rückgewähranspruch
make_xlsx(
    BASE / "xlsx" / "berechnung_rueckgewaehranspruch.xlsx",
    "Rueckgewaehr",
    ["Position", "Betrag EUR", "Bemerkung"],
    [
        ["Barzahlung Warenrampe 18.02.2026", 9750.00, "§ 131 Abs. 1 Nr. 1 InsO"],
        ["Kassenpfaendung 25.02.2026", 12000.00, "§ 131 Abs. 1 Nr. 1 InsO, § 88 InsO"],
        ["Ueberweisung 04.03.2026", 20000.00, "Druckzahlung, § 131 Abs. 1 Nr. 1 InsO"],
        ["Summe Hauptforderung", 41750.00, ""],
        ["Zinsen 5 %-Punkte ueber Basiszins seit 15.09.2026", 3180.45, "bis 15.09.2027"],
        ["Gesamtbetrag Zahlungseingang", 44930.45, "vollstaendig beglichen am 15.09.2027"],
    ],
    title="Berechnung des Rueckgewaehranspruchs - Karow Verpackungswerk GmbH",
)

# JPG
make_jpg(
    BASE / "jpg" / "warenrampe_frankenletter_fuerth.jpg",
    "Warenrampe Frankenletter Druck- und Medien GmbH",
    [
        "Waldstrasse 41, 90763 Fuerth",
        "Ort der Barzahlung vom 18.02.2026",
        "Aufnahme im Rahmen der Vollstreckungsmassnahme",
        "durch Obergerichtsvollzieher Martin Heckel",
    ],
)

print("Fuerth Multiformat erzeugt")
