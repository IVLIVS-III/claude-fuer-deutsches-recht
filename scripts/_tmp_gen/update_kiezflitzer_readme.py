# -*- coding: utf-8 -*-
import io

path = "/home/user/workspace/legal-work/target/testakten/insolvenzanfechtung-kiezflitzer-gesellschafterdarlehen-berlin/README.md"
with io.open(path, encoding="utf-8") as f:
    content = f.read()

old_block = """## Aktenstücke

Nummerierte Einzeldateien in realistischen Formaten (Markdown, CSV, EML, Chat-Export). Chronologie und Widersprüche sind Teil der Akte."""

new_block = """## Aktenstruktur

```
insolvenzanfechtung-kiezflitzer-gesellschafterdarlehen-berlin/
├── 01_mandatsvermerk_anfechtungsklage.docx          — Handakte der Verwalterin: Verfahren, Gegenstand, offene Punkte
├── 02_handelsregisterauszug.docx                    — HRB 224871 B (AG Charlottenburg) mit Insolvenzvermerk
├── 03_gesellschafterdarlehensvertrag_2023.docx      — Darlehensvertrag Brosekamp, 150.000 EUR
├── 04_beratervertrag_interim_finance.docx           — Beratervertrag „Interim Finance Advisory"
├── 05_rechnung_2025_002_beraterhonorar.docx         — Rechnung ueber 20.230 EUR fuer Juli/August 2025
├── 06_stundennachweise_juli_august_2025.csv         — Stundennachweise zur Beraterrechnung
├── 07_kontoauszuege_auszuege_2024_2025.csv          — Kontobewegungen 2024/2025
├── 08_protokoll_gesellschafterversammlung_2025-10-28.docx — Protokoll: Diskussion Liquiditaetslage und LOI
├── 09_mahnungen_und_opos_uebersicht.docx            — Offene-Posten-Uebersicht der Schuldnerin
├── 10_loi_kollibri_2025-09-30.docx                  — Unverbindlicher Investoren-LOI Kollibri Ventures GmbH
├── 11_eigenantrag_insolvenz_2025-11-14.docx         — Eigenantrag der Schuldnerin
├── 12_beschluss_vorlaeufige_verwaltung_2025-11-17.docx — Beschluss ueber die vorlaeufige Verwaltung
├── 13_gutachten_eroeffnungsverfahren_2026-02-20.docx — Gutachten: Ueberschuldung 30.06.2025, Zahlungsunfaehigkeit 01.09.2025
├── 14_eroeffnungsbeschluss_2026-03-01.docx          — Eroeffnungsbeschluss AG Charlottenburg, 36c IN 2291/25
├── 15_liquiditaetsstatus_stichtage.csv              — Liquiditaetsstatus je Stichtag
├── 16_ueberschuldungsstatus_2025-06-30.docx         — Ueberschuldungsstatus zum 30.06.2025
├── 17_rueckforderungsschreiben_verwalterin_2026-05-12.docx — Anfechtung aller drei Zahlungen
├── 18_antwort_ra_okatan_2026-06-03.docx             — Erwiderung: Bestreiten der Kenntnis, Verweis auf LOI
├── 19_klageschrift_lg_berlin_2026-09-01.docx        — Klageschrift auf Rueckgewaehr von 165.230 EUR
├── 20_klageerwiderung_okatan_2026-10-13.docx        — Klageerwiderung: Fristbeginn, Bargeschaefts-Einwand, LOI
├── 21_replik_trux_2026-11-03.docx                   — Replik: Fristbeginn Eroeffnungsantrag, Kenntnisvermutung § 138 Abs. 2 InsO
├── 22_duplik_okatan_2026-11-24.docx                 — Duplik: Bestreiten der Kenntnis aus dem Wochenreport
├── 23_beweisbeschluss_lg_berlin_2026-12-10.docx      — Beweisbeschluss: Zeugenvernehmung Wittkamp, ergaenzendes Sachverstaendigengutachten
├── 24_urteil_lg_berlin_2027-06-15.docx              — Urteil: Rueckgewaehr Darlehen und Vorschuss, Beraterhonorar bleibt privilegiert
├── 25_schlussvermerk_trux_2027-08-30.docx           — Schlussvermerk: Zahlungseingang, Verfahrensabschluss
├── csv/
│   └── verfahrenschronologie.csv                    — Chronologie aller Verfahrensschritte vom Darlehen bis zum Schlussvermerk
├── xlsx/
│   └── berechnung_rueckgewaehranspruch.xlsx         — Berechnung des Rueckgewaehranspruchs je Zahlung
├── jpg/
│   └── buero_kiezflitzer_weserstrasse.jpg           — Bueroraeume der Schuldnerin, Weserstrasse, Berlin-Neukoelln
├── pdfs/
│   ├── 24_urteil_lg_berlin_2027-06-15.pdf           — Urteil als PDF-Rendering
│   └── 25_schlussvermerk_trux_2027-08-30.pdf        — Schlussvermerk als PDF-Rendering
├── eml/
│   ├── 2025-08-22_cash-report_kw34.eml              — Wochenreport mit Liquiditaetskennzahlen
│   ├── 2025-10-20_brosekamp_vorschuss.eml           — Anforderung des Vorschusses durch Brosekamp
│   ├── 2025-10-23_wittkamp_antwort_kollibri.eml     — Antwort zum Stand der Kollibri-Verhandlungen
│   ├── 2025-11-07_kollibri_absage.eml               — Absage der Kollibri Ventures GmbH
│   ├── 2026-07-06_sachstand_nachforderung.eml       — Sachstandsanfrage der Verwalterin vor Klageerhebung
│   ├── 2026-11-20_ladung_zeuge_wittkamp.eml         — Ladung des Zeugen Wittkamp zum Beweistermin
│   ├── 2027-06-18_urteilszustellung_trux.eml        — Zustellungsmitteilung des Urteils an die Verwalterin
│   └── 2027-08-30_zahlungsbestaetigung_brosekamp.eml — Zahlungsbestaetigung Brosekamps nach Rechtskraft
├── whatsapp/
│   └── gruenderchat_auszug.txt                      — Gruender-Chat mit Hinweisen zur Liquiditaetslage
├── gesamt-pdf/
│   └── insolvenzanfechtung-kiezflitzer-gesellschafterdarlehen-berlin_gesamt.pdf — Gesamt-PDF aller Aktenstuecke
├── README.md
└── rubric.yaml
```

Nummerierte Einzeldateien in realistischen Formaten (DOCX, CSV, EML, XLSX, JPG, PDF, Chat-Export). Chronologie und Widersprüche sind Teil der Akte."""

assert old_block in content, "old_block not found"
content = content.replace(old_block, new_block)

with io.open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("README updated OK")
