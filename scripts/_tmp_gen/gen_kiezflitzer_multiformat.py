#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Erzeugt Multi-Format-Dateien fuer die Kiezflitzer-Akte."""
import sys
sys.path.insert(0, "/home/user/workspace/legal-work/target/scripts/_tmp_gen")
from aktenbau import make_eml, make_csv, make_xlsx, make_jpg, TESTAKTEN

BASE = TESTAKTEN / "insolvenzanfechtung-kiezflitzer-gesellschafterdarlehen-berlin"

# EML
make_eml(
    BASE / "eml" / "2026-11-20_ladung_zeuge_wittkamp.eml",
    frm="Geschaeftsstelle Kammer fuer Handelssachen <handelssachen94.geschaeftsstelle@lg-berlin.de>",
    to="Dr. Selim Okatan <okatan@kanzlei-okatan-berlin.de>",
    subject="94 O 47/26 - Ladung des Zeugen Jonas Wittkamp",
    date="Fri, 20 Nov 2026 10:05:00 +0100",
    body=(
        "Sehr geehrter Herr Rechtsanwalt Dr. Okatan,\n\n"
        "in obiger Sache wird Termin zur Vernehmung des Zeugen Jonas Wittkamp\n"
        "auf den 04.03.2027, 09:30 Uhr, Sitzungssaal 118, bestimmt.\n\n"
        "Mit freundlichen Gruessen\n"
        "Geschaeftsstelle Kammer fuer Handelssachen"
    ),
    msgid_domain="lg-berlin.de",
)

make_eml(
    BASE / "eml" / "2027-06-18_urteilszustellung_trux.eml",
    frm="Geschaeftsstelle Kammer fuer Handelssachen <handelssachen94.geschaeftsstelle@lg-berlin.de>",
    to="Dr. Gesa Trux <trux@insolvenz-berlin.de>",
    subject="94 O 47/26 - Zustellung des Urteils vom 15.06.2027",
    date="Fri, 18 Jun 2027 13:20:00 +0200",
    body=(
        "Sehr geehrte Frau Dr. Trux,\n\n"
        "anbei erhalten Sie das Urteil der Kammer vom 15.06.2027 zur weiteren Verwendung.\n\n"
        "Mit freundlichen Gruessen\n"
        "Geschaeftsstelle Kammer fuer Handelssachen"
    ),
    msgid_domain="lg-berlin.de",
)

make_eml(
    BASE / "eml" / "2027-08-30_zahlungsbestaetigung_brosekamp.eml",
    frm="Dr. Valentin Brosekamp <brosekamp@interim-finance-advisory.de>",
    to="Dr. Gesa Trux <trux@insolvenz-berlin.de>",
    subject="Az. 94 O 47/26 - Zahlung erfolgt",
    date="Mon, 30 Aug 2027 16:10:00 +0200",
    body=(
        "Sehr geehrte Frau Dr. Trux,\n\n"
        "ich bestaetige die heutige Ueberweisung von 178.170,15 EUR (Hauptforderung nebst Zinsen)\n"
        "auf das von Ihnen benannte Massekonto gemaess Urteil des LG Berlin vom 15.06.2027.\n\n"
        "Mit freundlichen Gruessen\n"
        "Dr. Valentin Brosekamp"
    ),
    msgid_domain="interim-finance-advisory.de",
)

# CSV: Verfahrenschronologie
make_csv(
    BASE / "csv" / "verfahrenschronologie.csv",
    ["Datum", "Ereignis"],
    [
        ["2024-12-15", "Rueckzahlung Gesellschafterdarlehen 150.000 EUR"],
        ["2025-09-30", "LOI Kollibri Ventures GmbH unterzeichnet"],
        ["2025-09-15", "Zahlung Beraterhonorar 20.230 EUR"],
        ["2025-10-20", "Zahlung Vorschuss 15.000 EUR"],
        ["2025-11-07", "Absage Kollibri Ventures GmbH"],
        ["2025-11-14", "Eigenantrag der Schuldnerin"],
        ["2025-11-17", "Beschluss vorlaeufige Verwaltung"],
        ["2026-02-20", "Gutachten Eroeffnungsverfahren"],
        ["2026-03-01", "Eroeffnungsbeschluss"],
        ["2026-05-12", "Rueckforderungsschreiben der Verwalterin"],
        ["2026-06-03", "Antwort Ra. Okatan"],
        ["2026-09-01", "Klageschrift eingereicht"],
        ["2026-10-13", "Klageerwiderung"],
        ["2026-11-03", "Replik"],
        ["2026-11-24", "Duplik"],
        ["2026-12-10", "Beweisbeschluss"],
        ["2027-03-04", "Zeugenvernehmung Wittkamp"],
        ["2027-06-15", "Urteil LG Berlin"],
        ["2027-07-20", "Rechtskraft"],
        ["2027-08-30", "Zahlungseingang 178.170,15 EUR"],
    ],
)

# XLSX: Berechnung Rückgewähranspruch
make_xlsx(
    BASE / "xlsx" / "berechnung_rueckgewaehranspruch.xlsx",
    "Rueckgewaehr",
    ["Position", "Betrag EUR", "Bemerkung"],
    [
        ["Darlehensrueckzahlung Dezember 2024", 150000.00, "§ 135 Abs. 1 Nr. 2 InsO"],
        ["Vorschuss Oktober 2025", 15000.00, "§§ 130, 133 InsO, § 138 Abs. 2 InsO"],
        ["Beraterhonorar September 2025", 20230.00, "§ 142 InsO - Bargeschaeft, nicht anfechtbar"],
        ["Klagesumme (ohne Beraterhonorar)", 165230.00, ""],
        ["Zinsen 5 %-Punkte ueber Basiszins seit 02.09.2026", 12940.15, "bis 30.08.2027"],
        ["Gesamtbetrag Zahlungseingang", 178170.15, "vollstaendig beglichen am 30.08.2027"],
    ],
    title="Berechnung des Rueckgewaehranspruchs - Dr. Valentin Brosekamp",
)

# JPG
make_jpg(
    BASE / "jpg" / "buero_kiezflitzer_weserstrasse.jpg",
    "Kiezflitzer Mobility GmbH - Bueroraeume",
    [
        "Weserstrasse 168, 12045 Berlin-Neukoelln",
        "E-Lastenrad-Abo-Startup",
        "Aufnahme im Rahmen der Bestandsaufnahme",
        "durch die Insolvenzverwalterin Dr. Gesa Trux",
    ],
)

print("Kiezflitzer Multiformat erzeugt")
