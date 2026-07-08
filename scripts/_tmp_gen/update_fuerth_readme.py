# -*- coding: utf-8 -*-
import io

path = "/home/user/workspace/legal-work/target/testakten/insolvenzanfechtung-inkongruente-deckung-zwangsvollstreckung-fuerth/README.md"
with io.open(path, encoding="utf-8") as f:
    content = f.read()

old_block = """├── 17_handaktenvermerk_verwalter_2026-07-02.docx    — Erste Bewertung der Erwiderung und weiteres Vorgehen
├── eml/
│   ├── 2025-11-10_ratenzahlungsbitte_frankenletter.eml — Ratenzahlungsbitte der Schuldnerin mit offener Krisenschilderung
│   ├── 2025-11-14_karow_ablehnung_raten.eml            — Ablehnung der Raten unter Hinweis auf die Warenkreditversicherung
│   └── 2026-03-03_pflugbeil_intern_freigabe_gv_zahlung.eml — Interne Freigabe der 20.000-EUR-Zahlung („sonst stehen die am 11.03. wieder auf dem Hof")
├── README.md
└── rubric.yaml
```"""

new_block = """├── 17_handaktenvermerk_verwalter_2026-07-02.docx    — Erste Bewertung der Erwiderung und weiteres Vorgehen
├── 18_klageschrift_lg_nuernberg-fuerth_2026-09-14.docx — Klageschrift auf Rueckgewaehr von 41.750 EUR
├── 19_klageerwiderung_ottmann_2026-10-26.docx       — Klageerwiderung: Bestreiten der Inkongruenz und der Kenntnis
├── 20_replik_wehrfritz_2026-11-16.docx              — Replik: Kenntnis-Falle bei § 131 Abs. 1 Nr. 1 InsO, Insolvenzreife seit Februar 2025
├── 21_duplik_ottmann_2026-12-07.docx                — Duplik: Zurechnung der internen E-Mail und Bewertung des Kreditvermerks bestritten
├── 22_beweisbeschluss_lg_nuernberg-fuerth_2026-12-21.docx — Beweisbeschluss: Zeugenvernehmung Karow, Sachverstaendigengutachten zur Zahlungsunfaehigkeit
├── 23_sachverstaendigengutachten_fessenmayer_2027-04-30.docx — Gutachten Fessenmayer: Zahlungsunfaehigkeit bereits ab 01.02.2025 belegt
├── 24_urteil_lg_nuernberg-fuerth_2027-07-09.docx    — Urteil: Verurteilung zur Rueckgewaehr in voller Hoehe
├── 25_schlussvermerk_wehrfritz_2027-09-20.docx      — Schlussvermerk: Zahlungseingang, Verfahrensabschluss
├── csv/
│   └── verfahrenschronologie.csv                    — Chronologie aller Verfahrensschritte vom Eigenantrag bis zum Schlussvermerk
├── eml/
│   ├── 2025-11-10_ratenzahlungsbitte_frankenletter.eml — Ratenzahlungsbitte der Schuldnerin mit offener Krisenschilderung
│   ├── 2025-11-14_karow_ablehnung_raten.eml            — Ablehnung der Raten unter Hinweis auf die Warenkreditversicherung
│   ├── 2026-03-03_pflugbeil_intern_freigabe_gv_zahlung.eml — Interne Freigabe der 20.000-EUR-Zahlung („sonst stehen die am 11.03. wieder auf dem Hof")
│   ├── 2026-11-05_ladung_zeuge_karow.eml            — Ladung des Zeugen Karow zum Beweistermin
│   ├── 2027-07-12_urteilszustellung_wehrfritz.eml   — Zustellungsmitteilung des Urteils an den Verwalter
│   └── 2027-09-15_zahlungsbestaetigung_karow.eml    — Zahlungsbestaetigung der Karow Verpackungswerk GmbH nach Rechtskraft
├── xlsx/
│   └── berechnung_rueckgewaehranspruch.xlsx         — Berechnung des Rueckgewaehranspruchs: Hauptforderung, Zinsen, Gesamtbetrag
├── jpg/
│   └── warenrampe_frankenletter_fuerth.jpg          — Warenrampe der Schuldnerin, Ort der Barzahlung vom 18.02.2026
├── pdfs/
│   ├── 24_urteil_lg_nuernberg-fuerth_2027-07-09.pdf — Urteil als PDF-Rendering
│   └── 25_schlussvermerk_wehrfritz_2027-09-20.pdf   — Schlussvermerk als PDF-Rendering
├── gesamt-pdf/
│   └── insolvenzanfechtung-inkongruente-deckung-zwangsvollstreckung-fuerth_gesamt.pdf — Gesamt-PDF aller Aktenstuecke
├── README.md
└── rubric.yaml
```"""

assert old_block in content, "old_block not found"
content = content.replace(old_block, new_block)

with io.open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("README updated OK")
