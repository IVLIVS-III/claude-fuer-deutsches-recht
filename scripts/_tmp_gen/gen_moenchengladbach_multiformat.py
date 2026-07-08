#!/usr/bin/env python3
"""Multi-Format-Ergaenzung Moenchengladbach: eml, xlsx, jpg."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from aktenbau import make_eml, make_xlsx, make_jpg, TESTAKTEN

SLUG = "insolvenzanfechtung-glaeubigerbenachteiligung-grundstuecksverkauf-moenchengladbach"
D = TESTAKTEN / SLUG

mails = [
    ("2026-09-08_terminsladung_gutachterin", "poststelle@lg-moenchengladbach.nrw.de", "kanzlei@hellwege-recht.de",
     "Terminsladung 5 O 214/26 mit Sachverstaendiger", "Tue, 08 Sep 2026 09:00:00 +0200",
     "Sehr geehrte Damen und Herren,\n\nes ergeht Ladung zum Termin am 10.11.2026, 10:00 Uhr, mit muendlicher "
     "Gutachtenerlaeuterung durch Dipl.-Ing. Dallmer.\n\nMit freundlichen Gruessen\nGeschaeftsstelle 3. Zivilkammer"),
    ("2026-11-24_vergleichsannahme_rheinpark", "l.brandstaetter@brandstaetter-recht.de", "c.hellwege@hellwege-recht.de",
     "Vergleichsannahme 5 O 214/26", "Tue, 24 Nov 2026 15:40:00 +0100",
     "Sehr geehrter Herr Dr. Hellwege,\n\nunsere Mandantin nimmt den Vergleichsvorschlag ueber EUR 155.000,00 in "
     "zwei Raten an.\n\nMit freundlichen Gruessen\nDr. Leo Brandstaetter"),
    ("2027-02-02_zahlungseingang_zweite_rate", "c.hellwege@hellwege-recht.de", "l.brandstaetter@brandstaetter-recht.de",
     "Zahlungseingang beide Raten bestaetigt", "Tue, 02 Feb 2027 11:15:00 +0100",
     "Sehr geehrter Herr Dr. Brandstaetter,\n\nwir bestaetigen den vollstaendigen Eingang beider Raten (insgesamt "
     "EUR 155.000,00) auf dem Massekonto.\n\nMit freundlichen Gruessen\nDr. Carsten Hellwege"),
]
for fname, frm, to, subj, date, body in mails:
    make_eml(D / "eml" / f"{fname}.eml", frm, to, subj, date, body)

make_xlsx(
    D / "xlsx" / "massekostenkalkulation_und_erloesverteilung.xlsx",
    "Kalkulation",
    ["Position", "Betrag (EUR)", "Bemerkung"],
    [
        ["Vergleichsbetrag Rheinpark", "155.000,00", "zwei Raten, vollstaendig eingegangen"],
        ["Titulierte Forderung Stefan Vondering", "60.000,00", "Versaeumnisurteil AG Moenchengladbach"],
        ["Davon per Kontopfaendung realisiert", "22.400,00", "Sparkasse Moenchengladbach"],
        ["Restforderung tituliert offen", "37.600,00", "weitere Vollstreckung vorgemerkt"],
        ["Gerichtskosten beide Verfahren", "6.940,00", "aus der Masse verauslagt"],
        ["Sachverstaendigenkosten", "3.850,00", "muendliche Gutachtenerlaeuterung"],
        ["Nettoerloes fuer die Masse (Stand Abschluss)", "166.610,00", "155.000 + 22.400 - 6.940 - 3.850"],
    ],
    title="Massekostenkalkulation Anfechtungskomplexe Rheinpark/Vondering",
)

make_jpg(
    D / "jpg" / "grundstueck_krefelder_strasse_luftbild_vermerk.jpg",
    "Anlage: Betriebsgrundstueck Krefelder Str. 214",
    [
        "Flurstueck 1188/4, Gemarkung Rheydt",
        "Grundbuch von Moenchengladbach-Rheydt Blatt 4471",
        "Grundstuecksflaeche: 8.420 qm, Hallenflaeche: 3.100 qm",
        "Verkauft an Rheinpark Gewerbeimmobilien GmbH & Co. KG am 12.11.2025",
        "Foto-Vermerk der Sachverstaendigen vom 24.10.2025",
    ],
)

print("Multiformat Moenchengladbach erzeugt.")
