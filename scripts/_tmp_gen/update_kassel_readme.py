# -*- coding: utf-8 -*-
import io

path = "/home/user/workspace/legal-work/target/testakten/insolvenzanfechtung-inkongruente-deckung-warenlager-an-erfuellungs-statt-kassel/README.md"
with io.open(path, encoding="utf-8") as f:
    content = f.read()

old_block = """├── 17_replik_verwalterin_2026-06-29.docx            — Replik: Liquiditätsstatus, Inkongruenz, Kenntnisindizien, Bezifferung
├── eml/
│   ├── 2025-11-27_daemmtec_lieferstopp.eml          — Lieferstopp und Gesprächsangebot mit Bitte um Lagerliste
│   ├── 2025-12-09_hillebrand_intern_ware_sichern.eml — Interne Weisung des Lieferanten-GF („bevor die Bude kippt, nehmen wir Ware")
│   └── 2025-12-16_wenzel_uebereignung_entwurf.eml   — Entwurfsabstimmung mit offenem Hinweis auf das Brandau-Risiko
├── whatsapp/
│   └── chatverlauf_kurrle_wenzel.txt                — Chat der Vertriebsleute (Lieferstopp, Besichtigung, „unauffällige" Abholung)
├── README.md
└── rubric.yaml
```"""

new_block = """├── 17_replik_verwalterin_2026-06-29.docx            — Replik: Liquiditätsstatus, Inkongruenz, Kenntnisindizien, Bezifferung
├── 18_klageschrift_lg_kassel_2026-09-07.docx        — Klageschrift der Verwalterin: Rückgewähr des Lagerwerts und der Forderungen
├── 19_klageerwiderung_appelt_2026-10-19.docx        — Klageerwiderung: Bestreiten der Insolvenzreife und der Kenntnis, Bargeschäftseinwand
├── 20_replik_verwalterin_2026-11-09.docx            — Replik zum Klageverfahren: Vertiefung Liquiditätslage und Kenntnisindizien
├── 21_duplik_appelt_2026-11-30.docx                 — Duplik: Angriff auf Sanierungsgutachten und Bewertungsansatz
├── 22_beweisbeschluss_lg_kassel_2026-12-14.docx      — Beweisbeschluss: Zeugenvernehmung Kurrle, Sachverständigengutachten zur Zahlungsunfähigkeit
├── 23_sachverstaendigengutachten_osterhage_2027-03-08.docx — Gutachten Osterhage: Zahlungsunfähigkeit bereits ab 01.02.2025 belegt
├── 24_urteil_lg_kassel_2027-06-21.docx              — Urteil: Verurteilung zur Rückgewähr dem Grunde und ganz überwiegend der Höhe nach
├── 25_schlussvermerk_verwalterin_2027-08-16.docx     — Schlussvermerk: Zahlungseingang, Verfahrensabschluss, Massequote
├── csv/
│   └── verfahrenschronologie.csv                    — Chronologie aller Verfahrensschritte vom Eigenantrag bis zum Schlussvermerk
├── eml/
│   ├── 2025-11-27_daemmtec_lieferstopp.eml          — Lieferstopp und Gesprächsangebot mit Bitte um Lagerliste
│   ├── 2025-12-09_hillebrand_intern_ware_sichern.eml — Interne Weisung des Lieferanten-GF („bevor die Bude kippt, nehmen wir Ware")
│   ├── 2025-12-16_wenzel_uebereignung_entwurf.eml   — Entwurfsabstimmung mit offenem Hinweis auf das Brandau-Risiko
│   ├── 2026-07-06_sachstand_nachforderung.eml       — Sachstandsanfrage der Verwalterin vor Klageerhebung
│   ├── 2026-12-08_ladung_zeuge_kurrle.eml           — Ladung des Zeugen Kurrle zum Beweistermin
│   ├── 2027-06-22_urteilszustellung_salzwedel.eml   — Zustellungsmitteilung des Urteils an die Verwalterin
│   └── 2027-08-10_zahlungsbestaetigung_daemmtec.eml — Zahlungsbestätigung der Dämmtec Werra GmbH nach Rechtskraft
├── xlsx/
│   └── berechnung_rueckgewaehranspruch.xlsx         — Berechnung des Rückgewähranspruchs: Lagerwert, Forderungen, Zinsen
├── jpg/
│   └── lagerhalle_fuldablick_leipziger_strasse.jpg  — Lagerhalle der Schuldnerin, Leipziger Straße, Kassel
├── pdfs/
│   ├── 24_urteil_lg_kassel_2027-06-21.pdf           — Urteil als PDF-Rendering
│   └── 25_schlussvermerk_verwalterin_2027-08-16.pdf — Schlussvermerk als PDF-Rendering
├── whatsapp/
│   └── chatverlauf_kurrle_wenzel.txt                — Chat der Vertriebsleute (Lieferstopp, Besichtigung, „unauffällige" Abholung)
├── gesamt-pdf/
│   └── insolvenzanfechtung-inkongruente-deckung-warenlager-an-erfuellungs-statt-kassel_gesamt.pdf — Gesamt-PDF aller Aktenstücke
├── README.md
└── rubric.yaml
```"""

assert old_block in content, "old_block not found"
content = content.replace(old_block, new_block)

with io.open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("README updated OK")
