#!/usr/bin/env python3
"""Multi-Format-Ergaenzung Stuttgart: eml, xlsx, jpg."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from aktenbau import make_eml, make_xlsx, make_jpg, TESTAKTEN

SLUG = "insolvenzanfechtung-unentgeltlich-konzernsicherheit-upstream-stuttgart"
D = TESTAKTEN / SLUG

mails = [
    ("2026-10-30_terminsladung_beweisaufnahme", "poststelle@lg-stuttgart.de", "kanzlei@mangold-restrukturierung.de",
     "Terminsladung 34 O 88/26 KfH Beweisaufnahme", "Fri, 30 Oct 2026 10:00:00 +0100",
     "Sehr geehrte Damen und Herren,\n\nes ergeht Ladung zum Beweistermin am 15.01.2027, 09:30 Uhr.\n\n"
     "Mit freundlichen Gruessen\nGeschaeftsstelle 34. Zivilkammer fuer Handelssachen"),
    ("2027-02-16_vergleichsannahme_bank", "recht@berkhoff-lauterbach.de", "s.mangold@mangold-restrukturierung.de",
     "Vergleichsannahme 34 O 88/26 KfH", "Tue, 16 Feb 2027 14:20:00 +0100",
     "Sehr geehrte Frau Dr. Mangold,\n\nunsere Mandantin nimmt den Vergleichsvorschlag ueber EUR 545.000,00 in drei "
     "Raten an.\n\nMit freundlichen Gruessen\nBerkhoff Lauterbach & Partner mbB"),
    ("2027-05-14_zahlungseingang_letzte_rate", "s.mangold@mangold-restrukturierung.de", "recht@berkhoff-lauterbach.de",
     "Zahlungseingang letzte Rate bestaetigt", "Fri, 14 May 2027 11:00:00 +0200",
     "Sehr geehrte Damen und Herren,\n\nwir bestaetigen den vollstaendigen Eingang aller drei Raten (insgesamt "
     "EUR 545.000,00) auf dem Massekonto.\n\nMit freundlichen Gruessen\nDr. Sibylle Mangold"),
]
for fname, frm, to, subj, date, body in mails:
    make_eml(D / "eml" / f"{fname}.eml", frm, to, subj, date, body)

make_xlsx(
    D / "xlsx" / "massekostenkalkulation_vergleich_bank.xlsx",
    "Kalkulation",
    ["Position", "Betrag (EUR)", "Bemerkung"],
    [
        ["Vergleichsbetrag Sueddeutsche Kreditbank AG", "545.000,00", "drei Raten, vollstaendig eingegangen"],
        ["Gerichtskosten", "8.960,00", "aus der Masse verauslagt, 45 Prozent Kostenanteil Klaegerin"],
        ["Sachverstaendigenkosten Prof. Wachsmuth", "12.400,00", "schriftliches und muendliches Gutachten"],
        ["Zeugenentschaedigung Sattelmaier", "640,00", "Fahrtkosten und Zeitversaeumnis"],
        ["Nettoerloes fuer die Masse", "523.000,00", "545.000 - 8.960 - 12.400 - 640"],
    ],
    title="Massekostenkalkulation Anfechtung Konzernsicherheit",
)

make_jpg(
    D / "jpg" / "betriebsgrundstueck_feuerbach_grundschuld_vermerk.jpg",
    "Anlage: Betriebsgrundstueck Siemensstrasse 47",
    [
        "Flurstueck 662/9, Gemarkung Stuttgart-Feuerbach",
        "Grundbuch von Stuttgart-Feuerbach Blatt 2290",
        "Erstrangige Grundschuld EUR 1.200.000,00 vom 15.05.2023",
        "Zugunsten Sueddeutsche Kreditbank AG (Konsortialfuehrerin)",
        "Foto-Vermerk der Sachverstaendigen im Rahmen der Verwertungspruefung",
    ],
)

print("Multiformat Stuttgart erzeugt.")
