# Vollprüfung: fachanwalt-insolvenz-sanierungsrecht

## Zusammensetzung

Dieser Vollprüfung enthaelt top-8 von 505 Skills (gekuerzt fuer Chat-Fenster) des Plugins `fachanwalt-insolvenz-sanierungsrecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Wenn es um Anwalts-Dashboard Fachanwalt Insolvenz- und Sanierungsrecht in Fachanwalt Insolvenz- und Sanierungsrecht geht…
2. **fachanwalt-insolvenz-sanierungsrecht-orientierung** — Wenn es um Fachanwalt für Insolvenz- und Sanierungsrecht — Orientierung in Fachanwalt Insolvenz- und Sanierungsrecht geh…
3. **orientierung-mandat-fachanwaltschaft** — Wenn es um Orientierung Mandat Fachanwaltschaft in Fachanwalt Insolvenz- und Sanierungsrecht geht: prüft Frist, Form, Zu…
4. **erstgespraech-mandatsannahme** — Wenn es um Erstgespraech Mandatsannahme in Fachanwalt Insolvenz- und Sanierungsrecht geht: prüft Frist, Form, Zuständigk…
5. **erstpruefung-und-mandatsziel** — Wenn es um Erstpruefung Und Mandatsziel in Fachanwalt Insolvenz- und Sanierungsrecht geht: klärt Rolle, Ziel, Frist, Unt…
6. **zahlungsunfaehigkeit-paragraf-17-inso-bgh-ix-zb-25-17** — Wenn es um Zahlungsunfähigkeit nach Paragraf 17 InsO fachanwaltlich prüfen in Fachanwalt Insolvenz- und Sanierungsrecht …
7. **schutzschirmverfahren** — Wenn es um Schutzschirmverfahren Paragraf 270d InsO Eigenverwaltung in Insolvenz in Fachanwalt Insolvenz- und Sanierungs…
8. **insolvenz-glaeubigerverhandlung-sanierung** — Wenn es um Sanierungs-Verhandlung mit Gläubigern vor und in der Insolvenz nach StaRUG und InsO in Fachanwalt Insolvenz- …

---

## Skill: `einstieg-routing`

_Wenn es um Anwalts-Dashboard Fachanwalt Insolvenz- und Sanierungsrecht in Fachanwalt Insolvenz- und Sanierungsrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Anwalts-Dashboard Fachanwalt Insolvenz- und Sanierungsrecht

> Antragspflicht, Eigenverwaltung, Anfechtung, Restrukturierung — die 3-Wochen-Frist § 15a InsO ist der Taktgeber.
>
> Sie sehen unten die Sofort-Triage. Keine Rückfragen, bis die Tabelle steht. Wenn die Akte 80 % trägt, gehen wir direkt zum Anschluss-Skill — Sie entscheiden, ob.

## Sofort-Triage

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
| --- | --- | --- |
| Rolle | Wen vertrete ich? (Mandant · Gegenseite · Mehrere) | Mandantenmail, Vertretungsbestellung |
| Verfahrensstand | Vorprozessual · außergerichtlich · Klage · Rechtsmittel · Vollstreckung | Vorhandene Schriftsätze, Eingangsstempel |
| Eilfrist | **§ 15a I InsO: 3 Wochen** Insolvenzantragspflicht bei Zahlungsunfähigkeit / 6 Wochen bei Überschuldung (nach SanInsKG befristet). § 270b InsO: Schutzschirmverfahren — Antrag im Vorfeld der Insolvenz. § 174 InsO: Anmeldefrist Gläubiger nach öffentlicher Bekanntmachung. | Frist aus Zugangs-/Kenntnisdatum berechnen |
| Hauptanspruch | Antragspflicht §§ 15a, 17 ff. InsO · Anfechtung §§ 129 ff. InsO · GF-Haftung § 64 GmbHG a. F. / § 15b InsO n. F. · Gläubigeranfechtung AnfG außerhalb Insolvenz · Schutzschirm § 270b InsO · Eigenverwaltung § 270 InsO · StaRUG (Stabilisierungs- und Restrukturierungsrahmen). | Sachverhaltsabgleich mit Tatbestandsmerkmalen |
| Zuständigkeit | Insolvenzgericht (AG am Sitz, § 3 InsO). Restrukturierungsgericht nach StaRUG = LG (§§ 30 ff. StaRUG). Anfechtungsklage gegen Gläubiger: LG/AG nach Streitwert. | Gesetz, Vertrag, Gerichtsstandsklausel |

## Risiko-Ampel

- **Frist:** 🔴 § 15a InsO: 3 Wochen ab Zahlungsunfähigkeit. Frist tickt taggenau — Kalender. 🟠 § 270b InsO: Vorbereitung vor Antrag in 4-8 Wochen.
- **Beweislage:** 🔴 Zahlungsunfähigkeit § 17 II InsO: 3-Wochen-Liquiditätsstatus. Buchhaltungs- und Bankkontodaten sichern. 🟠 Überschuldung § 19 II InsO: Fortbestehensprognose dokumentieren.
- **Wirtschaftlich:** 🔴 Geschäftsführerhaftung § 15b InsO (Zahlungen nach Insolvenzreife) — sofort einstellen. 🟠 Anfechtungsangriff in 4 Jahren (§ 133 InsO 10 Jahre Vorsatzanfechtung).

## Anschluss-Skills (Router)

| Wenn der Fall trägt … | dann Skill | Erwartung |
| --- | --- | --- |
| Fortbestehensprognose anwerfen | `insanw-fortbestehensprognose-workflow` | Liquiditätsplan 12 Monate, IDW S 11, Beweisdokument |
| Eigenverwaltung / Schutzschirm § 270b | `insanw-eigenverwaltung-schutzschirm-spezial` | Antragsfähigkeit, Bescheinigung, Sachwalter |
| **Antragspflicht § 15a InsO** | `inso-p015a-antragspflicht-bei-juristischen-personen-und-rechtsfa` | 3-Wochen-Frist, GF-Haftung, Strafrecht § 15a IV InsO |
| Anfechtungsmandat (Gläubiger / Verwalter) | `insanw-anfechtungsmandat-leitfaden` | Tatbestände §§ 129 ff. InsO, Verteidigungsstrategie |
| Konzerninsolvenz / Gruppenkoordination | `insanw-konzerninsolvenz-koordination-spezial` | Gruppen-Gerichtsstand § 3a InsO, Koordinationsverfahren |

## Norm-Radar (live verifizieren)

- **§ 15a InsO** — Insolvenzantragspflicht — 3 Wochen / 6 Wochen
- **§ 17 InsO** — Zahlungsunfähigkeit
- **§ 19 InsO** — Überschuldung
- **§ 270 InsO** — Eigenverwaltung; § 270b Schutzschirm
- **§ 133 InsO** — Vorsatzanfechtung; 10-Jahres-Zeitraum
- **§ 15b InsO** — Zahlungsverbot nach Insolvenzreife

## Genau eine Rückfrage (nur wenn nötig)

> Stehen wir **vor** der Antragstellung (Beratung GF / Sanierung) oder **nach** Verfahrenseröffnung (Verwalter, Gläubiger, Anfechtung)?

Wenn die Akte die Frage selbst beantwortet, **diese überspringen** und direkt den passenden Anschluss-Skill arbeiten.

## Leitentscheidungs-Anker (Such-Wegweiser, keine fertigen Zitate)

- **Verwerterpflichten; höchstmögliche Erlöserzielung** — BGH IX. Zivilsenat (Linie IX ZR 169/04 v. 13.04.2006, fortgeführt) — *live verifizieren auf* `bundesgerichtshof.de`
- **Vorsatzanfechtung § 133 InsO; Bargeschäfts-Ausnahme** — BGH IX. Zivilsenat (Linienwandel ab 2021) — *live verifizieren auf* `bundesgerichtshof.de`
- **Insolvenzantragspflicht § 15a InsO; § 15b InsO Zahlungsverbot** — BGH II./IX. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Geschäftsveräußerung im Ganzen § 1 Ia UStG** — EuGH C-497/01 (Zita Modes); EuGH C-444/10 (Schriever); BFH — *live verifizieren auf* `curia.europa.eu + bfh.bund.de`

> Diese Anker sind Sucheinstieg. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle prüfen und Datum, Aktenzeichen, Randnummer abklären. Kuratierte Anker-Sammlung in `references/leitentscheidungen-anker.md`.

## Hinweis

Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Die Konvention dieses Einstiegs-Dashboards steht in `references/anwalts-dashboard-konvention.md`.

---

## Skill: `fachanwalt-insolvenz-sanierungsrecht-orientierung`

_Wenn es um Fachanwalt für Insolvenz- und Sanierungsrecht — Orientierung in Fachanwalt Insolvenz- und Sanierungsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Fachanwalt für Insolvenz- und Sanierungsrecht — Orientierung

## FAO-Voraussetzungen (§ 14 FAO)

- Lehrgang 120 Stunden + drei Klausuren.
- 60 Fälle in den letzten drei Jahren, davon mindestens 40 Fälle aus dem Insolvenzrecht und mindestens 20 rechtsförmliche Verfahren oder Aufgaben als Insolvenzverwalter, Sachwalter oder Sanierungsgeschäftsführer.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| Insolvenzordnung | InsO — §§ 1 ff. allgemein; §§ 14 ff. Antrag; §§ 17–19 Eröffnungsgründe; §§ 21 ff. einstweilige Sicherungen; §§ 80 ff. Insolvenzverwaltung; §§ 129–147 Anfechtung; §§ 217 ff. Insolvenzplan; §§ 270–285 Eigenverwaltung; §§ 286 ff. Restschuldbefreiung |
| Sanierung außerhalb InsO | StaRUG — Unternehmensstabilisierungs- und -restrukturierungsgesetz |
| Antragspflicht | § 15a InsO (Geschäftsführer/Vorstand juristischer Personen) |
| Strafrecht | §§ 283 ff. StGB (Bankrott, Gläubigerbegünstigung) |
| Europäisch | EuInsVO (VO 2015/848) |
| Arbeit | §§ 113, 125 ff. InsO; § 613a BGB |
| Insolvenzgeld | §§ 165 ff. SGB III |
| Insolvenzanfechtung Gerichte | spezialisierte Senate beim AG / LG / OLG |

## Typische Mandate

- Antragspflicht-Beratung Geschäftsführung (§ 15a InsO) und Haftungsschutz.
- Stellung Eigenantrag (§ 13 InsO) und Gläubigerantrag (§ 14 InsO).
- Eigenverwaltung und Schutzschirmverfahren (§§ 270, 270d InsO).
- Restrukturierungsplan nach StaRUG.
- Forderungsanmeldung (§ 174 InsO), Bestreiten (§ 178 InsO), Tabellenklage (§ 180 InsO).
- Insolvenzanfechtung als Anwalt der Insolvenzverwaltung oder Anfechtungsgegner.
- Verbraucherinsolvenz und Restschuldbefreiung (§§ 304 ff., 286 ff. InsO).
- Fortbestehens- und Liquiditätsprognose.

## Eröffnungsgründe (kurz)

- **Zahlungsunfähigkeit:** § 17 InsO; in der Regel angenommen bei Zahlungseinstellung; nach BGH-Schwelle ca. 10 % Liquiditätslücke länger als 3 Wochen. Konkrete Aktenzeichen über dejure.org / openjur.de live verifizieren.
- **Drohende Zahlungsunfähigkeit:** § 18 InsO; nur Schuldner kann darauf stützen. Prognosezeitraum 24 Monate.
- **Überschuldung:** § 19 InsO — modifizierter zweistufiger Überschuldungsbegriff mit positiver Fortbestehensprognose. Prognosezeitraum **seit 01.01.2024 wieder regulär 12 Monate** (SanInsKG-Verkürzung auf 4 Monate endete am 31.12.2023; eine zusätzliche temporäre Anpassung ist nicht in Kraft).

## Fristen (Auswahl)

- **Antragspflicht** § 15a Abs. 1 S. 1 InsO — bei Zahlungsunfähigkeit ohne schuldhaftes Zögern, spätestens drei Wochen; bei Überschuldung sechs Wochen.
- **Insolvenzanfechtung** §§ 129 ff. InsO — Anfechtungsfristen drei bis zehn Jahre rückwärts ab Antragstellung.
- **Forderungsanmeldung** §§ 28, 174 InsO — bis zum Schlusstermin; verspätete Anmeldung möglich, ggf. Kostenfolge.
- **Berufung gegen Eröffnungsbeschluss** § 34 InsO — sofortige Beschwerde § 6 InsO, ggf. zwei Wochen.

## Hauptgerichte

- Insolvenzgericht beim Amtsgericht (§ 2 InsO; örtliche Zuständigkeit § 3 InsO).
- Beschwerdegericht: Landgericht.
- BGH IX. Zivilsenat — Insolvenz, Insolvenzanfechtung.
- EuGH bei EuInsVO-Fragen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Berufsverband

- Arbeitsgemeinschaft Insolvenzrecht und Sanierung im DAV.
- VID — Verband Insolvenzverwalter und Sachwalter Deutschlands.

## Schnittstellen

- **`insolvenzrecht`** für operative Mandatsführung.
- **`steuerrecht-anwalt-und-berater`** für Steuerforderungen in der Insolvenz und § 75 AO.
- **`fachanwalt-arbeitsrecht`** bei §§ 113, 125 ff. InsO und Insolvenzgeld.
- **`fachanwalt-handels-gesellschaftsrecht`** bei Geschäftsführerhaftung § 15b InsO (§ 64 GmbHG aufgehoben durch SanInsFoG zum 01.01.2021).

## Triage — Erste Einordnung des Mandats

Bevor losgelegt wird, klaere:

1. **Welche Partei?** Schuldner (Eigenantrag), Glaeubigervertreter (Fremdantrag), Insolvenzverwalter, Sachwalter oder Anfechtungsgegner?
2. **Eröffnungsgrund vorhanden?** Zahlungsunfaehigkeit (§ 17), drohende Zahlungsunfaehigkeit (§ 18) oder Ueberschuldung (§ 19 InsO)?
3. **Fristen?** Antragspflicht § 15a Abs. 1 InsO: 3 Wochen bei Zahlungsunfaehigkeit, 6 Wochen bei Ueberschuldung — Haftungsrisiko § 15b InsO!
4. **Sanierungs-Pfad?** StaRUG (vor Insolvenz), Schutzschirm § 270d InsO, Eigenverwaltung §§ 270 ff. InsO, Insolvenzplan §§ 217 ff. InsO oder Regelverfahren?
5. **Handlungsbedarf?** Sofortsicherung § 21 InsO, Insolvenzgeld § 165 SGB III, Betriebsfortfuehrung?

## Aktuelle Leitentscheidungen des BGH IX. Zivilsenats (Stand Mai 2026)

- **BGH IX ZR 122/23 vom 05.12.2024** — Konkretisierung der *Unlauterkeit* iSd § 142 Abs. 1 Hs. 2 InsO bei der Vorsatzanfechtung im Bargeschäft.
  <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=05.12.2024&Aktenzeichen=IX+ZR+122/23>
- **BGH IX ZR 129/22 vom 18.04.2024** — Neuausrichtung der Vorsatzanfechtung; konkrete Erwartung dauerhafter Liquiditätsunterdeckung erforderlich.
  <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=18.04.2024&Aktenzeichen=IX+ZR+129/22>
- **BGH IX ZR 239/22 vom 18.04.2024** — Anfechtung gesellschafterähnlicher Stellung (§ 135 InsO).
  <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=18.04.2024&Aktenzeichen=IX+ZR+239/22>
- **BGH IX ZR 114/23 vom 19.12.2024** — Forderungsanmeldung bei Abtretung; Individualisierung.
  <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=19.12.2024&Aktenzeichen=IX+ZR+114/23>
- **BGH IX ZR 127/24 vom 13.11.2025** (Wirecard) — Aktionärs-Schadensersatzforderungen sind in der Insolvenz der AG keine einfachen Insolvenzforderungen iSd § 38 InsO; Nachrang.
- **BGH II ZR 206/22 vom 23.07.2024** — Fortwirkende Haftung des ausgeschiedenen Geschäftsführers für Neugläubigerschäden (§ 823 II BGB iVm § 15a InsO).
  <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=23.07.2024&Aktenzeichen=II+ZR+206/22>
- **BGH IV ZR 66/25 vom 19.11.2025** — D&O-Versicherung; Wissentlichkeitsausschluss erfordert positive Kenntnis pro konkreter Pflichtverletzung; § 15a / § 15b InsO nicht koppelbar.
- **BGH 5 StR 287/24 vom 27.02.2025** — Faktischer Geschäftsführer / Firmenbestattung.
  <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=27.02.2025&Aktenzeichen=5+StR+287/24>
- **BVerfG 1 BvR 418/25 vom 28.02.2025** (VARTA AG) — Verfassungsbeschwerde gegen Bestätigung des StaRUG-Restrukturierungsplans unzulässig.
  <https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2025/02/rk20250228_1bvr041825.html>

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Workflow — Ersteinschätzung in 5 Schritten

1. **Sachverhalt aufnehmen:** Mandantenrolle (Schuldner, Gläubiger, Verwalter, Anfechtungsgegner), Eröffnungsgrund prüfen, Fristen sichern. Bei Aktenzeichen-Bezug: konkrete BGH/BVerfG-Entscheidung über dejure.org/openjur.de mit Datum verifizieren.
2. **Pfad waehlen:** Entscheidungsbaum: [ZU vorhanden?] → Ja: Eigenantrag + Eigenverwaltung/Schutzschirm moeglich → Nein: StaRUG wenn drohende ZU.
3. **Antragspflicht pruefen:** Geschaeftsfuehrung/Vorstand beraten, Haftungsrisiko § 15b InsO dokumentieren, ggf. Antrag unmittelbar vorbereiten.
4. **Sofortmassnahmen:** Insolvenzgeld § 165 SGB III sichern (3-Monats-Vorlaufprinzip); Sicherungsantrag § 21 InsO stellen falls Vermoegen gefaehrdet; Betriebsfortfuehrung finanzieren.
5. **Sanierungskonzept:** IDW S 6 / IDW S 11 beauftragen; Glaeubigerstruktur kartieren; Plan-Optionen StaRUG vs. InsO-Plan durchrechnen.

## Output-Template Erstgutachten-Memo (Insolvenzrechtliche Ersteinschaetzung)

**Adressat:** Mandant (Geschaeftsfuehrung) — Tonfall: verstaendlich-erklaerend mit klaren Handlungsempfehlungen

```
Insolvenzrechtliche Ersteinschaetzung
Mandant: [NAME MANDANT]
Datum: [DATUM]
Erstellende Kanzlei: [KANZLEI]

I. SACHVERHALT (Kurzdarstellung)
[2-3 Saetze: Gesellschaft, Branche, Krisenlage]

II. ERÖFFNUNGSGRUNDE (§§ 17-19 InsO)
Zahlungsunfaehigkeit § 17 InsO: [JA/NEIN] — Begruendung: [...]
Ueberschuldung § 19 InsO: [JA/NEIN] — Begruendung: [...]
Drohende ZU § 18 InsO: [JA/NEIN]

III. ANTRAGSPFLICHT
Frist: [DATUM] (3 Wochen ab ZU / 6 Wochen ab Ueberschuldung)
Haftungsrisiko GF: § 15b InsO — Zahlungen nach Insolvenzreife rueckforderbar

IV. EMPFOHLENER PFAD
[ ] Eigenantrag Regelverfahren   [ ] Schutzschirm § 270d InsO
[ ] StaRUG-Plan                  [ ] Eigenverwaltung §§ 270 ff.

V. SOFORT-MASSNAHMEN (bis [DATUM])
1. [...]
2. [...]

VI. KOSTEN / HONORARRAHMEN
[...]
```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

---

## Skill: `orientierung-mandat-fachanwaltschaft`

_Wenn es um Orientierung Mandat Fachanwaltschaft in Fachanwalt Insolvenz- und Sanierungsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Orientierung im Insolvenz- und Sanierungsrecht für Mandate und Fachanwaltschaft nach § 14 FAO


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: InsO §§ 1, 13-22, 35, 39, 47, 55-56, 60, 80, 87, 129, 133, 174, 175, 270 ff., 286-300, StaRUG §§ 1, 29, 31; StaRUG §§ 1, 29, 31, 39, 49-55, 84, 102, IDW S 6, IDW S 11, InsO § 270; AO §§ 38, 42, 90, 93, 153, 162, 164, 169-171, 173, 233a, 370-378, UStG, EStG, KStG, GewStG, GrEStG, ErbStG, FGO; § 14. InsO Eroeffnung Antragspflicht; § 15a Gläubigerantrag; § 14 InsO. StaRUG Restrukturierungsplan. Insolvenzanfechtung — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Orientierung im Insolvenz- und Sanierungsrecht für Mandate und Fachanwaltschaft nach § 14 FAO. Anwendungsfall Kanzlei will Insolvenzmandat beurteilen oder Anwalt bereitet sich auf FAO-Fachanwaltsprüfung vor. Normen §§ 17-19 InsO Eroeffnungsgründe § 15a InsO Antragspflicht §§ 270 ff. InsO Eigenverwaltung § 270d InsO Schutzschirm StaRUG EuInsVO. Prüfraster Eroeffnungsgründe Antragspflicht Plan-Verfahren Anfechtung Fachanwalt-Voraussetzungen verifizierbare Quellen. Output Rechtsgebietsuebersicht mit Normenkarte verifizierbare Quellen und Routing zu Mandatsskills. Abgrenzung zu erstgespraech-mandatsannahme und fachanwalt-insolvenz-sanierungsrecht-restrukturierungsplan.

### Fachanwalt für Insolvenz- und Sanierungsrecht — Orientierung

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Fachanwalt für Insolvenz- und Sanierungsrecht — Orientierung` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## FAO-Voraussetzungen (§ 14 FAO)

- Lehrgang 120 Stunden + drei Klausuren.
- 60 Fälle in den letzten drei Jahren, davon mindestens 40 Fälle aus dem Insolvenzrecht und mindestens 20 rechtsförmliche Verfahren oder Aufgaben als Insolvenzverwalter, Sachwalter oder Sanierungsgeschäftsführer.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| Insolvenzordnung | InsO — §§ 1 ff. allgemein; §§ 14 ff. Antrag; §§ 17–19 Eröffnungsgründe; §§ 21 ff. einstweilige Sicherungen; §§ 80 ff. Insolvenzverwaltung; §§ 129–147 Anfechtung; §§ 217 ff. Insolvenzplan; §§ 270–285 Eigenverwaltung; §§ 286 ff. Restschuldbefreiung |
| Sanierung außerhalb InsO | StaRUG — Unternehmensstabilisierungs- und -restrukturierungsgesetz |
| Antragspflicht | § 15a InsO (Geschäftsführer/Vorstand juristischer Personen) |
| Strafrecht | §§ 283 ff. StGB (Bankrott, Gläubigerbegünstigung) |
| Europäisch | EuInsVO (VO 2015/848) |
| Arbeit | §§ 113, 125 ff. InsO; § 613a BGB |
| Insolvenzgeld | §§ 165 ff. SGB III |
| Insolvenzanfechtung Gerichte | spezialisierte Senate beim AG / LG / OLG |

## Typische Mandate

- Antragspflicht-Beratung Geschäftsführung (§ 15a InsO) und Haftungsschutz.
- Stellung Eigenantrag (§ 13 InsO) und Gläubigerantrag (§ 14 InsO).
- Eigenverwaltung und Schutzschirmverfahren (§§ 270, 270d InsO).
- Restrukturierungsplan nach StaRUG.
- Forderungsanmeldung (§ 174 InsO), Bestreiten (§ 178 InsO), Tabellenklage (§ 180 InsO).
- Insolvenzanfechtung als Anwalt der Insolvenzverwaltung oder Anfechtungsgegner.
- Verbraucherinsolvenz und Restschuldbefreiung (§§ 304 ff., 286 ff. InsO).
- Fortbestehens- und Liquiditätsprognose.

## Eröffnungsgründe (kurz)

- **Zahlungsunfähigkeit:** § 17 InsO; in der Regel angenommen bei Zahlungseinstellung; nach BGH-Schwelle ca. 10 % Liquiditätslücke länger als 3 Wochen. Konkrete Aktenzeichen über dejure.org / openjur.de live verifizieren.
- **Drohende Zahlungsunfähigkeit:** § 18 InsO; nur Schuldner kann darauf stützen. Prognosezeitraum 24 Monate.
- **Überschuldung:** § 19 InsO — modifizierter zweistufiger Überschuldungsbegriff mit positiver Fortbestehensprognose. Prognosezeitraum **seit 01.01.2024 wieder regulär 12 Monate** (SanInsKG-Verkürzung auf 4 Monate endete am 31.12.2023; eine zusätzliche temporäre Anpassung ist nicht in Kraft).

## Fristen (Auswahl)

- **Antragspflicht** § 15a Abs. 1 S. 1 InsO — bei Zahlungsunfähigkeit ohne schuldhaftes Zögern, spätestens drei Wochen; bei Überschuldung sechs Wochen.
- **Insolvenzanfechtung** §§ 129 ff. InsO — Anfechtungsfristen drei bis zehn Jahre rückwärts ab Antragstellung.
- **Forderungsanmeldung** §§ 28, 174 InsO — bis zum Schlusstermin; verspätete Anmeldung möglich, ggf. Kostenfolge.
- **Berufung gegen Eröffnungsbeschluss** § 34 InsO — sofortige Beschwerde § 6 InsO, ggf. zwei Wochen.

## Hauptgerichte

- Insolvenzgericht beim Amtsgericht (§ 2 InsO; örtliche Zuständigkeit § 3 InsO).
- Beschwerdegericht: Landgericht.
- BGH IX. Zivilsenat — Insolvenz, Insolvenzanfechtung.
- EuGH bei EuInsVO-Fragen.

## Berufsverband

- Arbeitsgemeinschaft Insolvenzrecht und Sanierung im DAV.
- VID — Verband Insolvenzverwalter und Sachwalter Deutschlands.

## Schnittstellen

- **`insolvenzrecht`** für operative Mandatsführung.
- **`steuerrecht-anwalt-und-berater`** für Steuerforderungen in der Insolvenz und § 75 AO.
- **`fachanwalt-arbeitsrecht`** bei §§ 113, 125 ff. InsO und Insolvenzgeld.
- **`fachanwalt-handels-gesellschaftsrecht`** bei Geschäftsführerhaftung § 15b InsO (§ 64 GmbHG aufgehoben durch SanInsFoG zum 01.01.2021).

## Triage — Erste Einordnung des Mandats

Bevor losgelegt wird, klaere:

1. **Welche Partei?** Schuldner (Eigenantrag), Gläubigervertreter (Fremdantrag), Insolvenzverwalter, Sachwalter oder Anfechtungsgegner?
2. **Eröffnungsgrund vorhanden?** Zahlungsunfaehigkeit (§ 17), drohende Zahlungsunfaehigkeit (§ 18) oder Ueberschuldung (§ 19 InsO)?
3. **Fristen?** Antragspflicht § 15a Abs. 1 InsO: 3 Wochen bei Zahlungsunfaehigkeit, 6 Wochen bei Ueberschuldung — Haftungsrisiko § 15b InsO!
4. **Sanierungs-Pfad?** StaRUG (vor Insolvenz), Schutzschirm § 270d InsO, Eigenverwaltung §§ 270 ff. InsO, Insolvenzplan §§ 217 ff. InsO oder Regelverfahren?
5. **Handlungsbedarf?** Sofortsicherung § 21 InsO, Insolvenzgeld § 165 SGB III, Betriebsfortfuehrung?

## Aktuelle Leitentscheidungen des BGH IX. Zivilsenats (Stand Mai 2026)

- **BGH IX ZR 122/23 vom 05.12.2024** — Konkretisierung der *Unlauterkeit* iSd § 142 Abs. 1 Hs. 2 InsO bei der Vorsatzanfechtung im Bargeschäft.
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=05.12.2024&Aktenzeichen=IX+ZR+122/23>
- **BGH IX ZR 129/22 vom 18.04.2024** — Neuausrichtung der Vorsatzanfechtung; konkrete Erwartung dauerhafter Liquiditätsunterdeckung erforderlich.
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=18.04.2024&Aktenzeichen=IX+ZR+129/22>
- **BGH IX ZR 239/22 vom 18.04.2024** — Anfechtung gesellschafterähnlicher Stellung (§ 135 InsO).
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=18.04.2024&Aktenzeichen=IX+ZR+239/22>
- **BGH IX ZR 114/23 vom 19.12.2024** — Forderungsanmeldung bei Abtretung; Individualisierung.
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=19.12.2024&Aktenzeichen=IX+ZR+114/23>
- **BGH IX ZR 127/24 vom 13.11.2025** (Wirecard) — Aktionärs-Schadensersatzforderungen sind in der Insolvenz der AG keine einfachen Insolvenzforderungen iSd § 38 InsO; Nachrang.
- **BGH II ZR 206/22 vom 23.07.2024** — Fortwirkende Haftung des ausgeschiedenen Geschäftsführers für Neugläubigerschäden (§ 823 II BGB iVm § 15a InsO).
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=23.07.2024&Aktenzeichen=II+ZR+206/22>
- **BGH IV ZR 66/25 vom 19.11.2025** — D&O-Versicherung; Wissentlichkeitsausschluss erfordert positive Kenntnis pro konkreter Pflichtverletzung; § 15a / § 15b InsO nicht koppelbar.
- **BGH 5 StR 287/24 vom 27.02.2025** — Faktischer Geschäftsführer / Firmenbestattung.
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=27.02.2025&Aktenzeichen=5+StR+287/24>
- **BVerfG 1 BvR 418/25 vom 28.02.2025** (VARTA AG) — Verfassungsbeschwerde gegen Bestätigung des StaRUG-Restrukturierungsplans unzulässig.
 <https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2025/02/rk20250228_1bvr041825.html>

## — Ersteinschätzung in 5 Schritten

1. **Sachverhalt aufnehmen:** Mandantenrolle (Schuldner, Gläubiger, Verwalter, Anfechtungsgegner), Eröffnungsgrund prüfen, Fristen sichern. Bei Aktenzeichen-Bezug: konkrete BGH/BVerfG-Entscheidung über dejure.org/openjur.de mit Datum verifizieren.
2. **Pfad waehlen:** Entscheidungsbaum: [ZU vorhanden?] → Ja: Eigenantrag + Eigenverwaltung/Schutzschirm möglich → Nein: StaRUG wenn drohende ZU.
3. **Antragspflicht prüfen:** Geschäftsführung/Vorstand beraten, Haftungsrisiko § 15b InsO dokumentieren, ggf. Antrag unmittelbar vorbereiten.
4. **Sofortmassnahmen:** Insolvenzgeld § 165 SGB III sichern (3-Monats-Vorlaufprinzip); Sicherungsantrag § 21 InsO stellen falls Vermögen gefaehrdet; Betriebsfortfuehrung finanzieren.
5. **Sanierungskonzept:** IDW S 6 / IDW S 11 beauftragen; Gläubigerstruktur kartieren; Plan-Optionen StaRUG vs. InsO-Plan durchrechnen.

## Output-Template Erstgutachten-Memo (Insolvenzrechtliche Ersteinschaetzung)

**Adressat:** Mandant (Geschäftsführung) — Tonfall: verstaendlich-erklaerend mit klaren Handlungsempfehlungen

```
Insolvenzrechtliche Ersteinschaetzung
Mandant: [NAME MANDANT]
Datum: [DATUM]
Erstellende Kanzlei: [KANZLEI]

I. SACHVERHALT (Kurzdarstellung)
[2-3 Saetze: Gesellschaft, Branche, Krisenlage]

II. ERÖFFNUNGSGRUNDE (§§ 17-19 InsO)
Zahlungsunfaehigkeit § 17 InsO: [JA/NEIN] — Begruendung: [...]
Ueberschuldung § 19 InsO: [JA/NEIN] — Begruendung: [...]
Drohende ZU § 18 InsO: [JA/NEIN]

III. ANTRAGSPFLICHT
Frist: [DATUM] (3 Wochen ab ZU / 6 Wochen ab Ueberschuldung)
Haftungsrisiko GF: § 15b InsO — Zahlungen nach Insolvenzreife rueckforderbar

IV. EMPFOHLENER PFAD
[ ] Eigenantrag Regelverfahren [ ] Schutzschirm § 270d InsO
[ ] StaRUG-Plan [ ] Eigenverwaltung §§ 270 ff.

V. SOFORT-MASSNAHMEN (bis [DATUM])
1. [...]
2. [...]

VI. KOSTEN / HONORARRAHMEN
[...]
```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

---

## Skill: `erstgespraech-mandatsannahme`

_Wenn es um Erstgespraech Mandatsannahme in Fachanwalt Insolvenz- und Sanierungsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Strukturierter Erstgespraechsleitfaden für Insolvenz- und Restrukturierungsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen.


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: InsO §§ 1, 13-22, 35, 39, 47, 55-56, 60, 80, 87, 129, 133, 174, 175, 270 ff., 286-300, StaRUG §§ 1, 29, 31; StaRUG §§ 1, 29, 31, 39, 49-55, 84, 102, IDW S 6, IDW S 11, InsO § 270; AO §§ 38, 42, 90, 93, 153, 162, 164, 169-171, 173, 233a, 370-378, UStG, EStG, KStG, GewStG, GrEStG, ErbStG, FGO; § 14. InsO Eroeffnung Antragspflicht; § 15a Gläubigerantrag; § 14 InsO. StaRUG Restrukturierungsplan. Insolvenzanfechtung — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Strukturierter Erstgespraechsleitfaden für Insolvenz- und Restrukturierungsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen.

### Erstgespraech und Mandatsannahme im Insolvenz- und Restrukturierungsrecht

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Erstgespraech und Mandatsannahme im Insolvenz- und Restrukturierungsrecht` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Wann dieser Arbeitsgang greift

- Neue Anfrage aus dem Bereich Insolvenz- und Restrukturierungsrecht (Telefon, Mail, Empfehlung, Walk-in).
- Mandantin oder Mandant beschreibt Sachverhalt unstrukturiert; viele Anlagen ohne System.
- Vor jeder weiteren fachlichen Bearbeitung: erst Annahme klären, Konflikt- und GwG-Prüfung, Vollmacht, Streitwert/Vereinbarung, Fristen.

## Phasen des Erstgespraechs

### 1. Aufnahme der Konstellation (10-15 Min.)

Standard-Fragenraster für Insolvenz- und Restrukturierungsrecht:

- Beteiligte (Vor-/Nachname, Geburtsdatum, Anschrift, Rolle: Klägerin/Beklagter, Antragsteller, Beschuldigter)
- Konflikt-Kern in einem Satz ("Was ist Ihr Ziel?")
- Konkrete fachliche Stossrichtung: Eigenverwaltung, Insolvenzantrag, StaRUG, Anfechtung, Sanierungsplanung
- Bisherige Korrespondenz (Bescheide, Schreiben der Gegenseite, anwaltliche Vertretung der Gegenseite?)
- **Fristenscreening sofort:** anstehende Klage-/Widerspruchs-/Einspruchsfristen aus den vorgelegten Schreiben (z.B. Insolvenzantrag, Anfechtungsklage, StaRUG-Restrukturierungsantrag). Frist-Alarm an die Vorbereitung weitergeben.

### 2. Konflikt-Prüfung und GwG-Check (5 Min.)

- Konflikt-Check über Mandantsystem: Gegnerin, Streitgegenstand, frueherer Mandant?
- GwG-Identifizierung: amtlicher Lichtbildausweis (Ausweisscan), bei juristischer Person Handelsregister-/Transparenzregister-Auszug, ggf. wirtschaftlich Berechtigte/n.
- Risikobewertung (niedrig/mittel/hoch) abhaengig von Mandatscharakter, Bargeld, Auslandsbezug.
- Doku im Mandatsbogen (Pflicht nach §§ 10 ff. GwG i.V.m. § 2 Abs. 1 Nr. 10 GwG für RA-Mandate).

### 3. Vollmacht und Schweigepflichtentbindung

- Allgemeine Prozess-/Aussenvollmacht (BORA, ZPO, FamFG, je nach Fachgebiet).
- Spezielle Vollmachten: ggf. Akteneinsicht Strafakte, KV-Abrechnungsdaten, Sozialdaten (Schweigepflichtentbindung gegenueber Krankenkasse, Arzt, Behörde).
- Bei Eheleuten/GbR/GmbH: einzelvollmachtgebende Person und Vertretungsmacht klären.

### 4. Streitwert und Gebührenvereinbarung

Standard-Streitwerte im Bereich Insolvenz- und Restrukturierungsrecht:

- Skizze: Streitwert grob abschaetzen (z.B. Hauptforderung, ggf. + Zinsen, Nebenforderungen).
- RVG-Pauschalrechnung (Berechnungstool im Plugin) oder Stundenhonorarvereinbarung.
- Beratungshilfe-/Prozesskostenhilfe-Antrag prüfen, wenn wirtschaftlich angezeigt.
- Vorschussanforderung nach § 9 RVG.

### 5. Strategie-Erstskizze

Drei Weichen am Ende des Erstgespraechs:

- **Mandat annehmen:** vollstaendig (Prüfung + Schriftsatz) oder begrenzt (nur Prüfung/Gutachten).
- **Verweisen:** wenn Spezialgebiet ausserhalb der Fachanwaltschaft, oertlich unzuständig oder Konflikt.
- **Ablehnen:** offensichtlich aussichtslos, GwG-Hit, Bauchgefuehl-Vorsicht.

## Pflicht-Output am Ende

1. **Mandatsbogen** mit Beteiligten, Konflikt-Check, GwG-Status, Streitwert.
2. **Frist-Liste** (Sofortfristen, Verjährung, Ausschlussfristen, Beweisanforderungs-Fristen).
3. **Anlagenverzeichnis** des uebergebenen Datenraums (Stand erstes Sortieren).
4. **Naechster-Schritt-Plan:** binnen 24/48/72 h, Owner, Output.
5. **Honorarvereinbarung** unterschrieben oder Vorbehalt notiert.

## Relevante Rechtsgrundlagen und Standards

- BORA, BRAO, FAO für Fachanwaltschaft Insolvenz- und Restrukturierungsrecht.
- GwG, GwGMeldV, Identifizierungsleitfaden BRAK.
- InsO, StaRUG, AnfG, EuInsVO, COVInsAG-Nachwirkungen (für fachliche Erstpruefung).
- DSGVO und BDSG für den Umgang mit Mandantendaten (Art. 6 DSGVO als Rechtsgrundlage, Art. 9 ggf. Gesundheitsdaten).

## Typische Fehler im Erstgespraech

- Frist uebersehen, weil Mandantin sie nicht selber genannt hat (immer aus jedem Schreiben Frist herausziehen).
- Konflikt-Check nur nach Personennamen, nicht nach Sachzusammenhang (gleiche Liegenschaft, gleicher Sachverhalt).
- Vollmachtsumfang unklar -> später Streit mit Mandantin über Befugnisse.
- Honorarvereinbarung muendlich -> Beweisnot bei Streitwert-/Honorar-Streit.
- GwG: kein Lichtbildausweis erfasst, kein Aktenvermerk über Risikobewertung.

## Praxis-Checkliste

- [ ] Personalien und Rolle aller Beteiligten erfasst
- [ ] Konflikt-Check durchgefuehrt
- [ ] GwG: Identifizierung + Risikobewertung notiert
- [ ] Allgemeine Vollmacht unterschrieben
- [ ] Speziale Vollmacht / Entbindungserklaerung (wo noetig) unterschrieben
- [ ] Streitwert geschaetzt
- [ ] Honorarvereinbarung unterschrieben oder ausdruecklich auf RVG verwiesen
- [ ] Fristenliste angelegt und in Kalender eingetragen
- [ ] Mandatsbogen vollstaendig
- [ ] Naechster-Schritt-Plan dem Mandanten kommuniziert (E-Mail-Zusammenfassung)

## Konkrete Praxis-Konstellationen

### Konstellation A: Eilbeduerftigkeit

Mandantin kommt am Donnerstag, Frist laeuft am Montag (Klage- oder Widerspruchsfrist im Bereich Insolvenz- und Restrukturierungsrecht). Handlungs-Sequenz:

1. Sofort-Vollmacht und Sofort-Akteneinsicht (per beA, ELSTER, Behördenportal).
2. Antrag auf Wiedereinsetzung (§ 233 ZPO, § 60 VwGO, § 110 AO) als Reserve dokumentieren.
3. Spaeteste-Stunde-Versand-Plan: beA bevorzugt, mit qualifizierter Signatur und Empfangsbekenntnis.
4. Honorarvereinbarung NICHT auf Eilzuschlag verzichten - aber transparent kommunizieren.

### Konstellation B: Komplexer Sachverhalt, Datenraum unsortiert

Mandant uebergibt 200+ Dateien (PDF-Scans, E-Mails, Excel-Listen). Vor jeder fachlichen Bewertung:

1. Datenraum-Index in Excel: Datum, Absender, Empfaenger, Aktenzeichen, kurze Inhaltszeile.
2. Chronologischer Verlauf als Zeitstrahl - Spielraum für Verjährungs- und Ausschlussfristen identifizieren.
3. Loecher im Datenraum gezielt anfordern (Mandantenfragen-Katalog).

### Konstellation C: Interessenkonflikt-Naehe

Frueheres Mandat mit derselben Gegnerin oder gleichem Sachzusammenhang. Prüfung:

1. § 43a Abs. 4 BRAO und § 3 BORA - Sachzusammenhang, nicht nur Personenidentitaet.
2. Einwilligung beider Mandanten in Textform (mit konkreter Beschreibung).
3. Bei Zweifel: Mandat ablehnen und an Kanzleikollegium ueberweisen.

## Mandanten-Erwartungsmanagement

- Realistische Erfolgs- und Kostenprognose (nicht "Wir gewinnen sicher").
- Verfahrensdauer im Bereich Insolvenz- und Restrukturierungsrecht: Erfahrungswerte nach Instanz.
- Vergleichschance vs. streitiges Urteil als Option offen halten.
- Schriftliche Zusammenfassung des Erstgespraechs binnen 48 h.

## Honorarvereinbarung - Best Practices

- RVG-Basis als Default, Stundenhonorar nur mit gesondertem Hinweis nach § 3a RVG.
- Erfolgshonorar nur in den engen Grenzen § 4a RVG.
- Vorschuss in Höhe der voraussichtlichen 1. Instanz.
- Klarstellung: Auslagen-Pauschale, USt, Reisekosten, Sachverstaendigenkosten gesondert.
- Bei PKH/Beratungshilfe-Mandant: schriftliche Belehrung, dass eigene Beitraege möglich sind.

## Mandatsbogen-Muster (Mindestinhalt)

- Mandant (Name, Geburtsdatum, Anschrift, Telefon, E-Mail)
- Gegner (Name, Anschrift, ggf. anwaltliche Vertretung)
- Kurzbeschreibung Sachverhalt (5-10 Saetze)
- Ziel des Mandats (eine Zeile)
- Strittige Fragen (bullet)
- Geprueft: Konflikt - GwG - Vollmacht
- Streitwert (Schaetzung)
- Honorarvereinbarung (RVG/Stunde/Pauschale)
- Frist-Liste
- Aktenanlage Datum
- Naechster-Schritt

## Cross-Refs

- `vergleichsverhandlung-strategie` (im selben Plugin) für den Fall, dass aussergerichtliche Loesung angestrebt wird.
- `schriftsatzkern-substantiierung` (im selben Plugin) für den Schriftsatzaufbau, wenn Klage/Widerspruch eingereicht wird.
- Kanzlei-Allgemein-Plugin `kanzlei-allgemein` für Konflikt-, GwG- und PEP-Prüfroutinen.

## Aktuelle Leitentscheidungen — Insolvenz-Erstmandat (Stand Mai 2026)

- **BGH II ZR 206/22 vom 23.07.2024** — Fortwirkende Haftung des ausgeschiedenen Geschäftsführers (§ 823 II BGB iVm § 15a InsO); für die Mandantenwarnung bei Wechsel der Geschäftsleitung.
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=23.07.2024&Aktenzeichen=II+ZR+206/22>
- **BGH IV ZR 66/25 vom 19.11.2025** — D&O-Versicherung bei verspätetem Insolvenzantrag; Hinweis auf Deckungschancen.
- **BGH 5 StR 287/24 vom 27.02.2025** — Faktischer Geschäftsführer / Firmenbestattung; Strafbarkeit auch ohne formale Bestellung.
- Im Anfechtungsmandat: **BGH IX ZR 122/23 (05.12.2024)** zur Unlauterkeit Bargeschäft; **BGH IX ZR 129/22 (18.04.2024)** zur Neuausrichtung Vorsatzanfechtung.
- Konkrete Aktenzeichen vor Ausgabe über dejure.org / openjur.de / bundesgerichtshof.de verifizieren.

## Paragrafenkette Erstmandat Insolvenz

§ 43a BRAO (Interessenkonflikt) → §§ 10 ff. GwG (Identifizierungspflicht) → § 15a InsO (Antragspflicht 3/6 Wochen) → § 15b InsO (Haftung GF für Zahlungen nach Insolvenzreife) → §§ 17-19 InsO (Eröffnungsgruende) → § 3a RVG (Honorarvereinbarung)

## Triage — Erstgespraech Insolvenzmandat

1. **Welche Partei?** Geschäftsführung/Schuldner → Antragspflicht, Haftungsberatung. Gläubiger → Antragsrecht, Forderungssicherung. Insolvenzverwalter → Beauftragung prüfen.
2. **Fristen?** Antragspflicht § 15a InsO: ab heute bis zu welchem Datum? Sofort-Frist-Alarm!
3. **GwG-Risiko?** Insolvenzmandate oft Hochrisiko-Kategorie (Geldflueisse, Verschleierungsrisiko) → gruendliche Risiobewertung.
4. **Interessenkonflikt?** Kanzlei hat Gläubiger und Schuldner im selben Verfahren → § 43a Abs. 4 BRAO Verbot.

---

## Skill: `erstpruefung-und-mandatsziel`

_Wenn es um Erstpruefung Und Mandatsziel in Fachanwalt Insolvenz- und Sanierungsrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel im Insolvenz- und Sanierungsrecht: fachlich vertieftes Modul mit Normenradar (InsO/StaRUG/IDW-S6), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: InsO §§ 1, 13-22, 35, 39, 47, 55-56, 60, 80, 87, 129, 133, 174, 175, 270 ff., 286-300, StaRUG §§ 1, 29, 31; StaRUG §§ 1, 29, 31, 39, 49-55, 84, 102, IDW S 6, IDW S 11, InsO § 270; AO §§ 38, 42, 90, 93, 153, 162, 164, 169-171, 173, 233a, 370-378, UStG, EStG, KStG, GewStG, GrEStG, ErbStG, FGO; § 14. InsO Eroeffnung Antragspflicht; § 15a Gläubigerantrag; § 14 InsO. StaRUG Restrukturierungsplan. Insolvenzanfechtung — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel im Insolvenz- und Sanierungsrecht: fachlich vertieftes Modul mit Normenradar (InsO/StaRUG/IDW-S6), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.

### Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Spezialwissen: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** FAO, InsO, StaRUG.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Fachanwalt** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `zahlungsunfaehigkeit-paragraf-17-inso-bgh-ix-zb-25-17`

_Wenn es um Zahlungsunfähigkeit nach Paragraf 17 InsO fachanwaltlich prüfen in Fachanwalt Insolvenz- und Sanierungsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt._

# Zahlungsunfähigkeit nach Paragraf 17 InsO fachanwaltlich prüfen

## Einsatzlage

Nutze diesen Skill, wenn im Mandat eine Liquiditätslücke, ein Gläubigerantrag, eine Geschäftsführerhaftung, eine Anfechtungslage oder ein Sanierungsfenster auf Zahlungsunfähigkeit geprüft werden muss. Ziel ist ein gerichtsfestes Kurzmemorandum mit Stichtag, Zahlenwerk, Belegen, Rechtsprechungsankern und einer klaren Handlungsentscheidung.

## Normenanker

- Paragraf 17 InsO: Zahlungsunfähigkeit und Zahlungseinstellung.
- Paragraf 15a InsO und Paragraf 15b InsO: Antragspflicht und Zahlungsverbot.
- Paragraf 18 InsO: drohende Zahlungsunfähigkeit als StaRUG-Schwelle.
- Paragraf 19 InsO: Überschuldung und Fortbestehensprognose.
- Paragraf 129 ff. InsO: Anfechtung, insbesondere Liquiditätslage als Vorsatz- und Kenntnisanker.
- Paragraf 14 InsO: Gläubigerantrag, Forderungsnachweis und Eröffnungsgrund.

## Rechtsprechungsanker und Quellenhygiene

- BGH, Urteil vom 23.01.2025 - IX ZR 229/22: Randnummer 34 und 35 zur objektiven Zahlungsunfähigkeit und objektiven Rechtslage bei streitigen nicht titulierten Forderungen; vorläufig vollstreckbar titulierte streitige Forderung bei eingeleiteter Vollstreckung mit Nennwert passivieren; keine Prozessrisikoquote. Randnummer 27 zum engen Irrtumstatbestand bei ungeklärter Rechtsfrage.
- BGH, Urteil vom 18.04.2024 - IX ZR 129/22: Liquiditätsstatus gegenüber einem außenstehenden Dritten einzelpostenfähig darlegen; fehlen Einzelheiten und Belege, kann einfaches Bestreiten ausreichen.
- BGH, Beschluss vom 11.03.2025 - II ZR 139/23: für die Zahlungsunfähigkeit zählt der materielle Bestand der Verbindlichkeit.
- BGH, Beschluss vom 22.05.2025 - IX ZB 38/24: bei allein titelgestütztem Gläubigerantrag kann die Beweiswirkung entfallen, wenn die Zwangsvollstreckung eingestellt ist.
- BGH, Urteil vom 28.06.2022 - II ZR 112/21: Zahlungsunfähigkeit kann auch durch mehrere aussagekräftige tagesgenaue Liquiditätsstatus dargelegt werden.
- BGH, Urteil vom 19.12.2017 - II ZR 88/16: Passiva II im Drei-Wochen-Fenster einbeziehen; keine Bugwelle stehen lassen.
- BGH, Urteil vom 24.05.2005 - IX ZR 123/04: Grundlinie Zahlungsstockung, 10-Prozent-Schwelle und Drei-Wochen-Zeitraum.

## Prüfprogramm

1. Stichtag festlegen: Eintrittsdatum, Antragstag, Zahlungstag oder Anfechtungsstichtag nicht vermischen.
2. Aktiva I erfassen: freie Bankguthaben, Kasse, ziehungsfähiger Kreditrahmen, sofort verwertbare Liquidität.
3. Aktiva II erfassen: nur binnen drei Wochen realistisch zufließende Beträge; bestrittene eigene Forderungen nur mit hartem Realisierungsbeleg.
4. Passiva I erfassen: fällige, ernsthaft eingeforderte und nicht wirksam gestundete Verbindlichkeiten.
5. Passiva II erfassen: innerhalb von drei Wochen fällig werdende Verbindlichkeiten, auch wenn sie die Lücke nur fortschreiben.
6. Streitige Forderungen entscheiden: materiell nicht bestehend oder nicht fällig gleich raus; materiell bestehend und fällig gleich Nennwert rein; vorläufig vollstreckbar tituliert und Vollstreckung eingeleitet gleich Nennwert rein; Vollstreckung eingestellt gleich gesonderte Beweiswürdigungszeile.
7. Herausnahme verteidigen: Wer eine Forderung nicht passiviert, braucht Gegenbeweis und Haftungsvermerk; ein finales Gutachten stützt den Kenntnisstand, beseitigt aber das objektive Risiko nicht sicher.
8. Darlegungstiefe prüfen: keine OPOS-Summe übernehmen, bevor Gläubiger, Fälligkeit, Rechtsgrund, Beleg, Bestreiten, Titel und Vollstreckungsstand als Einzelposten sichtbar sind.
9. Indizien der Zahlungseinstellung prüfen: Lohn, Steuern, Sozialversicherung, Rücklastschriften, geplatzte Raten, Pfändungen, Insolvenzanträge, Vollstreckungsdruck.
10. Ergebnis mit Organpflichten verbinden: Antragspflicht, Zahlungsverbot, Dokumentationspflicht, Sanierungsfenster und nächste Maßnahme.

## Ausgabematrix

| Prüffeld | Ergebnis | Beleg | Risiko | Nächster Schritt |
| --- | --- | --- | --- | --- |
| Stichtag | Datum | Buchhaltung, Kontoauszug, OPOS | falsch angesetzter Fristbeginn | Stichtag begründen |
| Aktiva I und II | Betrag | Bank, Zusage, Debitor | Scheinliquidität | Zuflussbeleg nachfordern |
| Passiva I und II | Betrag | OPOS, Mahnung, Titel | unterschätzte Lücke | Fälligkeit prüfen |
| Streitige Forderung | rein oder raus | Vertrag, Urteil, Vollstreckung | Prozessrisikoquote | Nennwertentscheidung dokumentieren |
| Herausgenommene Forderung | begründet raus | Gutachten, Einwendung, Stundung | Beweislast Geschäftsleitung | Haftungsvermerk schreiben |
| Darlegung Liquiditätsstatus | einzelpostenfähig | OPOS-Auszug, Rechnung, Kontoauszug | einfaches Bestreiten | Belegpaket nachfordern |
| Indizien | ja oder nein | Akte | Zahlungseinstellung | Antragspflicht prüfen |

## Belege und Aktenlücken

- Liquiditätsstatus zum Stichtag und innerhalb des Drei-Wochen-Fensters.
- OPOS Kreditoren und Debitoren mit Fälligkeit und Mahnstand.
- Kontoauszüge aller Konten, Kreditlinien, Kündigungen und Sperren.
- Steuer- und Sozialversicherungsrückstände mit Bescheiden, Fälligkeiten und Stundungsentscheidungen.
- Titel, Klauseln, Zustellungsnachweise, Vollstreckungsaufträge und Einstellungsentscheidungen.
- Geschäftsleitervermerke, Zahlungspriorisierung, Sanierungsbeschlüsse und Beraterhinweise.

---

## Skill: `schutzschirmverfahren`

_Wenn es um Schutzschirmverfahren Paragraf 270d InsO Eigenverwaltung in Insolvenz in Fachanwalt Insolvenz- und Sanierungsrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik._

# Schutzschirmverfahren § 270d InsO Eigenverwaltung in Insolvenz


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: InsO §§ 1, 13-22, 35, 39, 47, 55-56, 60, 80, 87, 129, 133, 174, 175, 270 ff., 286-300, StaRUG §§ 1, 29, 31; StaRUG §§ 1, 29, 31, 39, 49-55, 84, 102, IDW S 6, IDW S 11, InsO § 270; AO §§ 38, 42, 90, 93, 153, 162, 164, 169-171, 173, 233a, 370-378, UStG, EStG, KStG, GewStG, GrEStG, ErbStG, FGO; § 14. InsO Eroeffnung Antragspflicht; § 15a Gläubigerantrag; § 14 InsO. StaRUG Restrukturierungsplan. Insolvenzanfechtung — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Schutzschirmverfahren § 270d InsO Eigenverwaltung in Insolvenz. Vorlaeufige Eigenverwaltung Antrag drohende Zahlungsunfähigkeit. Sachwalter Aufsicht. Schutzschirm 3 Monate bei Voraussetzung Sanierungsfähigkeit. Insolvenz-Plan Vorbereitung. Antrag Sachwalter Plan Beschluss Aufhebung.

### Schutzschirmverfahren § 270d InsO

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Schutzschirmverfahren § 270d InsO` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## 1) Eingangs-Abfrage

1. Liquiditäts-Lage: Zahlungsunfähigkeit oder "drohend" § 18 InsO?
2. Überschuldung § 19 InsO?
3. Sanierungs-Aussicht: positive Fortbestehensprognose und belastbare Sanierungsfähigkeit?
4. Anzahl Mitarbeiter / Gläubiger?
5. Geplante Sanierungs-Maßnahmen?
6. Schutzschirm-Anwalt bereit?

## 2) Voraussetzungen § 270d InsO

| Voraussetzung | Inhalt |
|---|---|
| Drohende Zahlungsunfähigkeit oder Überschuldung | § 18 / § 19 InsO |
| **Keine** Zahlungsunfähigkeit § 17 InsO | Bei Zahlungsunfähig: nur Eigenverwaltung § 270 InsO |
| Sanierungs-Aussicht | Prüfer-Bescheinigung |
| Antrag des Schuldners | Bei Gesellschaft: Geschäftsführer/Vorstand |

### Anders als StaRUG

- StaRUG vorab in der Krise — kein Insolvenzverfahren
- Schutzschirm: bereits Insolvenz-Verfahren, aber Eigenverwaltung

## 3) Sachwalter-Aufsicht

### Bestellung

- Vorschlagsrecht des Schuldners (mit anwaltlicher Mitwirkung)
- Gericht bestellt — üblich akzeptiert Vorschlag

### Pflichten Sachwalter

- Überwachung Geschäftsführung
- Kassenprüfung
- Berichtspflicht Gericht
- Insolvenzplan-Mitwirkung

## 4) Schutzschirm-Phase (3 Monate)

### Schutz

- Vollstreckungsschutz § 21 II Nr. 3 InsO analog
- Keine Sicherheits-Verwertung
- Vorläufige Eigenverwaltung

### Schuldner-Pflichten

- Insolvenzplan vorbereiten
- Insolvenz-Geld-Anspruch sichern (Mitarbeiter)
- Sanierungs-Konzept umsetzen

### Verfahren

- Schuldner bleibt Verfügungsberechtigt
- Sachwalter berichtet Gericht
- Gläubigerausschuss eingerichtet bei groesseren Verfahren

## 5) Insolvenz-Geld

- Bundesagentur übernimmt **3 Monate** Loehne
- Wichtig für Liquidität im Sanierungs-Verfahren
- Anspruch der Mitarbeiter, NICHT Schuldner

## 6) Workflow

### Phase 1 — Vorbereitung (vor Antrag)

- Sanierungskonzept mit Krisenursachen, Leitbild, Maßnahmen, integrierter Planung und Dokumentation
- Liquiditäts-Plan 13-Wochen
- Bescheinigung Prüfer "Sanierung nicht offenbar aussichtslos"
- Sachwalter-Vorschlag
- Antrag-Entwurf

### Phase 1a — Sanierungsfähigkeits-Check

Vor Schutzschirmantrag ausdrücklich prüfen:

- **Kein § 17 InsO:** Schutzschirm ist bei eingetretener Zahlungsunfähigkeit gesperrt.
- **Fortbestehensprognose:** Zahlungsfähigkeit im Prognosezeitraum mit überwiegender Wahrscheinlichkeit.
- **Nachhaltige Sanierungsfähigkeit:** nicht nur Liquiditätsbrücke, sondern tragfähiges Geschäftsmodell nach Maßnahmen.
- **Leitbild:** Markt, Produkt, Kostenbasis, Organisation, Finanzierung und Umsetzungsfähigkeit nach Sanierung.
- **Maßnahmen:** Verantwortliche, Kosten, Timing, Wirkung, Abhängigkeiten und Belegstatus.
- **Integrierte Planung:** GuV, Bilanz und Liquidität müssen zusammenpassen; Steuern, Zinsen, SV, Working Capital und Insolvenzgeldphase einbeziehen.

Bei unklarer Lage `fachanwalt-insolvenz-idw-s6-sanierungskonzept` vorschalten und erst danach die Bescheinigung/Antragsroute finalisieren.

### Phase 2 — Antrag

- Schriftlich beim Insolvenzgericht
- Mit Bescheinigung Prüfer
- Verzeichnis Gläubiger / Vermögen
- Vorgeschlagener Sachwalter

### Phase 3 — Schutzschirm-Eröffnung

- Beschluss Insolvenzgericht (binnen Tagen)
- Schutzschirm 3 Monate ab Antrag

### Phase 4 — Sanierungs-Maßnahmen

- Insolvenzplan-Aufstellung
- Verhandlungen Lieferanten / Mitarbeiter / Bank
- Notwendige Kündigungen (BR-Konsultation)

### Phase 5 — Insolvenzplan-Verfahren

- Vorgestellt allen Gläubigern
- Abstimmung in Klassen § 222 InsO
- Mehrheits-Erfordernis 50 % nach Kopf + 50 % nach Summe je Klasse
- Bei Annahme: Gerichts-Bestätigung
- Wirkung: Gesellschaft saniert, Gläubiger erhalten Quote

### Phase 6 — Verfahrensaufhebung

- Mit Plan-Erfüllung
- Löschung Insolvenz-Vermerk

## 7) Sanierungs-Optionen im Insolvenzplan

### Sanierungs-Maßnahmen

- Gläubiger-Quote (z.B. 20 % der Forderung)
- Loehne / Pensionen senken
- Mitarbeiter-Abbau
- Verkauf nicht-betriebsnotwendiger Aktiva
- Debt-Equity-Swap (Gläubiger werden Gesellschafter)

### Investor-Modelle

- Eigenständige Investor-Suche
- Asset-Deal aus Schutzschirm
- Doppel-Nettung-Modell

## 8) Typische Fehler

1. **Antrag bei Zahlungsunfähigkeit § 17 InsO** — kein Schutzschirm
2. **Sachwalter-Vorschlag ungeeignet** — Gericht lehnt ab
3. **Liquiditäts-Plan überoptimistisch** — Bescheinigung fragwürdig
4. **Insolvenz-Geld nicht beantragt** — Liquiditäts-Engpass
5. **Insolvenzplan zu spaet** — Schutzschirm läuft aus

## 9) Vergleich StaRUG vs. Schutzschirm vs. Standard-Insolvenz

| Aspekt | StaRUG | Schutzschirm § 270d | Standard-Insolvenz |
|---|---|---|---|
| Voraussetzung | drohende Zahlungsunfähigkeit | drohende ZahlUnfaeh + Sanierungs-Aussicht | Zahlungsunfähigkeit / Überschuldung |
| Eigenverwaltung | ja (faktisch) | ja | nein (Standard) |
| Aufsicht | Restrukturierungsbeauftragter | Sachwalter | Insolvenzverwalter |
| Gläubiger-Bindung | nur betroffene | alle (Insolvenzplan) | alle |
| Dauer | flexibel | 3 Monate + Plan-Phase | meist > 1 Jahr |
| Öffentlichkeit | nicht-publik möglich | publik (Insolvenz) | publik |

## 10) BGH- und BVerfG-Linien (Stand Mai 2026)

- **BVerfG 1 BvR 418/25 vom 28.02.2025** (3. Kammer, Erster Senat — VARTA-Sanierung) — Verfassungsbeschwerde von Minderheitsaktionären gegen die gerichtliche Bestätigung eines StaRUG-Restrukturierungsplans (Kapitalherabsetzung auf Null, Bezugsrechtsausschluss) als unzulässig zurückgewiesen; die Beschwerdeführer hatten die Verletzung von Grundrechten nicht hinreichend dargelegt. Bedeutung: StaRUG-Sanierungen mit Eingriff in Aktionärsrechte sind verfassungsrechtlich nicht generell ausgeschlossen.
 Quelle: <https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2025/02/rk20250228_1bvr041825.html>
- **BGH IX ZR 127/24 vom 13.11.2025** (Wirecard) — Kapitalmarktrechtliche Schadensersatzforderungen geschädigter Aktionäre sind in der Insolvenz der AG keine einfachen Insolvenzforderungen iSd § 38 InsO; sie treten hinter die einfachen Insolvenzgläubiger zurück. Relevanz: bei börsennotierten Schuldnerinnen Anmeldung von Aktionärsforderungen klar abzugrenzen.
 Quelle: <https://www.lto.de/recht/kanzleien-unternehmen/k/bgh-ixzr12724-wirecard-insolvenzmasse-forderungen-aktionaere-urteil> (BGH-Pressemitteilung 2025/211; Az. über bundesgerichtshof.de verifizieren)
- Konkrete BGH-Linie zur Eigenverwaltung (§ 270b InsO) und Schutzschirm (§ 270d InsO), insbesondere zu Anforderungen an die Bescheinigung und zur Bestellung des Sachwalters, vor Ausgabe über dejure.org / openjur.de mit Datum und Aktenzeichen verifizieren.

## Anschluss

- `krisenfrueherkennung-starug` — bei StaRUG-Alternative
- `insolvenzplan-starug-planwerkstatt` — bei Plan-Aufstellung
- `fortbestehensprognose` — bei Prüfung Sanierung

## Triage — Schutzschirm oder Regelinsolvenz?

Bevor losgelegt wird, klaere:

1. **ZU vorhanden?** Zahlungsunfaehigkeit § 17 InsO? → Kein Schutzschirm, nur Eigenverwaltung § 270b InsO oder Regelverfahren.
2. **Prognose und Sanierungsfähigkeit positiv?** Bescheinigung "Sanierung nicht offenbar aussichtslos" § 270d Abs. 1 S. 1 InsO durch geeigneten Sachverstaendigen; zugrunde liegendes Konzept muss Fortbestehensprognose und nachhaltige Sanierungslogik plausibel tragen.
3. **Sachwalter-Vorschlag vorbereitet?** Schuldner hat Vorschlagsrecht § 270d Abs. 2 InsO — Sachwalter muss unabhaengig und geeignet sein.
4. **13-Wochen-Liquiditaetsplan?** Ohne Forecast keine Glaubhaftmachung der Fortfuehrungsfaehigkeit.
5. **Insolvenzgeld gesichert?** § 165 SGB III — Vorauszahlung durch Bank moegliich (Insolvenzgeld-Vorfinanzierung).

## Aktuelle Leitentscheidungen

- **BVerfG 1 BvR 418/25 vom 28.02.2025** (VARTA / StaRUG-Restrukturierungsplan)
 <https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2025/02/rk20250228_1bvr041825.html>
- **BGH IX ZR 127/24 vom 13.11.2025** (Wirecard / Nachrang Aktionärsschadensersatz)
- Weitere BGH-Entscheidungen zur Eigenverwaltung / Schutzschirm vor Ausgabe über dejure.org, openjur.de und bundesgerichtshof.de mit Datum und Aktenzeichen verifizieren.

## Paragrafenkette Schutzschirmverfahren

§ 270d InsO (Schutzschirm) → § 270 InsO (Eigenverwaltung) → § 270b InsO (Antrag vorläufige Eigenverwaltung) → § 21 InsO analog (Vollstreckungsschutz) → § 217 InsO (Insolvenzplan) → § 245 InsO (Obstruktionsverbot) → § 254 InsO (Planwirkung)

## — 6-Phasen-Schritt-für-Schritt

1. **Krisen-Diagnose (Woche -4 bis -2 vor Antrag):** Liquiditaet 13 Wochen direct-method erstellen; Eröffnungsgrund §§ 17-19 InsO bestimmen; Fortbestehensprognose IDW S 11 beauftragen.
2. **Bescheinigung (Woche -2 bis -1):** Sachverstaendigen mit Bescheinigung § 270d Abs. 1 InsO beauftragen; Sanierungskonzept auf IDW-S-6-Niveau als Grundlage vorbereiten und Red-Team-Lücken vorab schließen.
3. **Antragsvorbereitung (Woche -1):** Sachwalter-Kandidaten identifizieren und Vorschlag vorbereiten; Antrag schreiben mit Glaubhaftmachungs-Unterlagen; Insolvenzgeld-Vorfinanzierungs-Vereinbarung mit Hausbank abschliessen.
4. **Antragstellung (Tag 0):** Schriftlicher Antrag beim AG/Insolvenzgericht; Bescheinigung anlegen; Sachwalter-Vorschlag; Gläubiger- und Vermögensverzeichnis.
5. **Schutzschirm-Phase (3 Monate):** Insolvenzplan aufstellen (§§ 217 ff. InsO); Gläubigerklassen bilden (§ 222 InsO); Schlüssel-Gläubiger verhandeln; Insolvenzgeld sichern (§ 165 SGB III).
6. **Plan-Abstimmung und Bestaetigung:** Eroerungs- und Abstimmungstermin (§§ 235, 237 InsO); Mehrheiten je Gruppe (§ 244 InsO: 50% Kopf + 50% Summe); ggf. Obstruktionsverbot § 245 InsO; Gerichtsbestaetigung § 248 InsO.

## Entscheidungsbaum Pfadwahl

```
Krisenstadium?
├── Drohende ZU (§ 18) + positive Prognose → Schutzschirm § 270d InsO ODER StaRUG
├── ZU (§ 17) + positive Prognose → Eigenverwaltung § 270b InsO (kein Schutzschirm!)
├── ZU (§ 17) + keine Prognose → Regelverfahren
└── Ueberschuldung (§ 19) + positive Prognose → Schutzschirm § 270d InsO moeglich
```

## Output-Template Schutzschirm-Antrag (Kurzgliederung)

**Adressat:** Insolvenzgericht [ORT] — Tonfall: sachlich-juristisch

```
An das Amtsgericht [ORT] — Insolvenzgericht —

Antrag auf Anordnung des Schutzschirmverfahrens
nach § 270d Abs. 1 InsO

Schuldnerin: [FIRMA], [ANSCHRIFT], HRB [XX]
— vertreten durch Geschaeftsfuehrerin [NAME] —

I. Antrag
Die Schuldnerin beantragt:
1. Anordnung vorläufiger Eigenverwaltung § 270b Abs. 1 InsO.
2. Erlass eines Schutzschirmbeschlusses § 270d Abs. 1 InsO für eine Frist von 3 Monaten.
3. Bestellung von [VORGESCHLAGENER SACHWALTER, NAME, KANZLEI] zum vorläufigen Sachwalter.

II. Sachverhalt
[Darstellung Krisenlage, Zeitablauf, Sanierungskonzept-Kurzform]

III. Eröffnungsground: Drohende Zahlungsunfaehigkeit § 18 InsO
[Darlegung Liquiditaetsplan 13-Wochen als Anlage A1]

IV. Sanierungsaussicht
Bescheinigung [NAME SACHVERSTAENDIGER] vom [DATUM] als Anlage A2 (Sanierung nicht offenbar aussichtslos § 270d Abs. 1 S. 1 InsO).

V. Anlagen
A1: Liquiditaetsplan 13-Wochen
A2: Bescheinigung § 270d Abs. 1 InsO
A3: Glaeubiger- und Forderungsverzeichnis (vorlaeufig)
A4: Vermoegensverzeichnis (vorlaeufig)
```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

---

## Skill: `insolvenz-glaeubigerverhandlung-sanierung`

_Wenn es um Sanierungs-Verhandlung mit Gläubigern vor und in der Insolvenz nach StaRUG und InsO in Fachanwalt Insolvenz- und Sanierungsrecht geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen._

# Sanierungs-Verhandlung mit Gläubigern vor und in der Insolvenz nach StaRUG und InsO


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: InsO §§ 1, 13-22, 35, 39, 47, 55-56, 60, 80, 87, 129, 133, 174, 175, 270 ff., 286-300, StaRUG §§ 1, 29, 31; StaRUG §§ 1, 29, 31, 39, 49-55, 84, 102, IDW S 6, IDW S 11, InsO § 270; AO §§ 38, 42, 90, 93, 153, 162, 164, 169-171, 173, 233a, 370-378, UStG, EStG, KStG, GewStG, GrEStG, ErbStG, FGO; § 14. InsO Eroeffnung Antragspflicht; § 15a Gläubigerantrag; § 14 InsO. StaRUG Restrukturierungsplan. Insolvenzanfechtung — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Sanierungs-Verhandlung mit Gläubigern vor und in der Insolvenz nach StaRUG und InsO. Anwendungsfall Schuldner will außergerichtlichen Vergleich oder InsO-Plan mit Gläubigern verhandeln. Normen § 270d InsO Schutzschirm §§ 4-65 StaRUG Restrukturierungsplan §§ 112 113 BetrVG Sozialplan § 125 InsO. Prüfraster Gläubigerausschuss-Zusammensetzung Verhandlungsposition Masseverbindlichkeiten Plan-Annahme 75-Prozent-Mehrheit Cross-class Cramdown. Output Verhandlungsstrategie-Memo mit Gläubigerkorrespondenz Vergleichsangebot Plan-Grobentwurf und Zeitplan. Abgrenzung zu fachanwalt-insolvenz-sanierungsrecht-schutzschirmverfahren und fachanwalt-insolvenz-sanierungsrecht-restrukturierungsplan.

### Gläubigerverhandlung in der Sanierung — StaRUG / Schutzschirm

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Gläubigerverhandlung in der Sanierung — StaRUG / Schutzschirm` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Eingaben

- Schuldner-Lage (drohende Z-Unf. § 18 InsO, Z-Unf. § 17, Überschuldung § 19)
- Gläubigerstruktur (Bank, Lieferanten, FA, Sozialkasse, Pensionssicherungsverein)
- Sanierungskonzept-Status: Fortbestehensprognose, Sanierungsfähigkeit, Leitbild, Maßnahmen, integrierte Planung, Dokumentation
- Geplanter Pfad (StaRUG, Schutzschirm, Eigenverwaltung, Regelinsolvenz)
- Wirtschaftliches Sanierungs-Potenzial

## Rechtlicher Rahmen

- **StaRUG** §§ 4-65 (Restrukturierungs-Plan ohne Insolvenz)
- **§ 270b InsO** — Eigenverwaltung
- **§ 270d InsO** — Schutzschirm
- **§ 217 InsO** — Insolvenz-Plan
- **§ 245 InsO** — Mehrheitserfordernisse
- **§ 245a InsO** — Cross-Class Cramdown (StaRUG § 26-28)
- **IDW S 6** — Sanierungskonzept-Standard
- **INSOL Practice Statement** Mediation in Insolvency

## ADR-Pfade

### Pfad 1 — Außergerichtlicher Vergleich

- Vor Antragstellung
- Stillhalte-Vereinbarung (Standstill) typisch 90 Tage
- Vergleichs-Quoten 30-70 %
- Vorteil: Kein Stigma der Insolvenz

### Pfad 2 — StaRUG-Restrukturierungs-Plan

- Drohende Z-Unf. § 18 InsO
- 75 %-Mehrheit pro Klasse + Cross-Class Cramdown möglich
- Restrukturierungs-Gericht bestätigt
- Gläubiger werden in Klassen verhandelt

### Pfad 3 — Schutzschirm § 270d InsO

- 3-Monats-Schutz vor Vollstreckung
- Insolvenz-Plan parallel
- Eigene Sachwalter

### Pfad 4 — Eigenverwaltung § 270b InsO

- Gerichtlicher Sachwalter überwacht
- Schuldner führt weiter
- Sanierung mit Insolvenz-Plan

### Pfad 5 — Mediation (Insolvenz-Mediator)

- Bei komplexer Gläubigerstruktur
- INSOL-Standard-Mediator
- Vor Schutzschirm-Antrag

## Workflow

### Phase 1 — Lage-Analyse

- Liquiditätsstatus 3 Wochen / 13 Wochen / 24 Monate
- Fortbestehensprognose und Sanierungsfähigkeits-Check
- Pfad-Wahl

### Phase 2 — Gläubigerliste + Vergleichs-Skizze

- Gläubiger sortieren (gesichert, ungesichert, nachrangig)
- Vergleichsquoten je Klasse
- Bedingungen (Zahlungsplan, Stundung, Zinsverzicht)

### Phase 3 — Vorgerichtliche Verhandlung Schlüssel-Gläubiger

- Bank zuerst (häufig größter Sicherungsnehmer)
- Lieferanten in Gruppen
- FA / Sozialkasse (oft restriktiv)
- Pensionssicherungsverein (BetrAVG)

### Phase 4 — Plan-Aufstellung

- Schriftlicher Plan StaRUG / InsO
- Klassen-Bildung
- Mehrheits-Pflichten

### Phase 5 — Plan-Abstimmung / Bestätigung

- Erörterungs-Termin
- Klassen-Abstimmung
- Gerichtsbestätigung

## Strategie und Taktik

- **Stillhalte-Vereinbarung** als Vor-Verhandlungs-Anker
- **Bank-Sicherheiten** kostentreu verhandeln (sonst Insolvenz vorgezogen)
- **Pensionssicherungsverein** früh einbeziehen (Anwartschaften)
- **Cram-Down** mit Klassenbildung strategisch nutzen (separate Klasse renitenter Gläubiger)
- Sanierungskonzept auf IDW-S-6-Niveau als Verhandlungsbasis: Krisenursachen, Leitbild, Maßnahmen, integrierte Planung und Nachweise so aufbereiten, dass Banken und Gläubiger nicht nur eine Quote, sondern die wirtschaftliche Logik prüfen können.
- **Insolvenzgeld § 165 SGB III** als Liquiditätsbrücke nutzen
- **Steuerberater + Anwalt parallel**: stb-warnschreiben → anw-haftungswarn-15a → Sanierung

## Quellen und Updates

Stand: 05/2026. StaRUG 1.1.2021. IDW S 6 / S 11. INSOL-Standards. Bei SanInsKG-Verlängerung 31.12.2026 aktualisieren.

## Triage — Verhandlungs-Einstieg

Bevor losgelegt wird, klaere:

1. **Krisenstadium?** Drohende ZU (§ 18) → StaRUG; eingetretene ZU (§ 17) → Insolvenz; Ueberschuldung (§ 19) → InsO oder Schutzschirm.
2. **Gläubigerstruktur?** Bank (gesichert), Lieferanten (ungesichert), FA/Sozialkasse (Privilegierung § 39 InsO), PSV (Pensionen BetrAVG).
3. **BATNA der Gegenseite?** Was passiert wenn Gläubiger nicht einwilligen → Insolvenzeröffnung, Liquidation, Quote-Prognose.
4. **Zeitfenster?** Stillhalte-Vereinbarung (Standstill, typisch 90 Tage) als Verhandlungs-Voraussetzung.
5. **Handlungsunfaehigkeit der Schuldnerin?** § 15a InsO Antragspflicht — kein Verhandlungsexzess auf Kosten der Antragspflicht.

## Aktuelle Leitentscheidungen (Stand Mai 2026)

- **BGH IX ZR 122/23 vom 05.12.2024** — Bargeschäft / Unlauterkeit (§ 142 InsO). Relevanz: in Sanierungsverhandlungen vereinbarte Zahlungsmodelle (Cash-on-Delivery, Vorkasse) bleiben grundsätzlich anfechtungsfest, wenn sie gleichwertig, unmittelbar und nicht gezielt schädigend für übrige Gläubiger sind.
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=05.12.2024&Aktenzeichen=IX+ZR+122/23>
- **BGH IX ZR 129/22 vom 18.04.2024** — Neuausrichtung der Vorsatzanfechtung; Stundungs- und Ratenzahlungsvereinbarungen sind günstiger zu beurteilen, wenn keine konkrete Erwartung dauerhafter Liquiditätsunterdeckung dokumentiert ist.
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=18.04.2024&Aktenzeichen=IX+ZR+129/22>
- **BVerfG 1 BvR 418/25 vom 28.02.2025** (VARTA) — Eingriffe in Aktionärsrechte über StaRUG-Plan verfassungsrechtlich grundsätzlich zulässig (Schlechterstellungsprüfung beachten).
 <https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2025/02/rk20250228_1bvr041825.html>
- Konkrete BGH-Linien zur Sanierungsmoderation (§§ 94 ff. StaRUG) und zum Sanierungsprivileg (§ 39 Abs. 4 InsO) vor Ausgabe über offene Quellen verifizieren.

## Paragrafenkette Gläubigerverhandlung

§ 18 InsO (drohende ZU) → § 31 StaRUG (Anzeige) → §§ 7-39 StaRUG (Plan) → § 25 StaRUG (Mehrheiten) → § 26 StaRUG (Cramdown) → § 39 Abs. 4 InsO (Sanierungsprivileg) → § 142 InsO (Bargeschaeft) → § 133 InsO (Vorsatzanfechtung) → § 165 SGB III (Insolvenzgeld)

## — 5-Phasen-Gläubigerverhandlung

1. **Lageanalyse:** Liquiditaetsstatus 3-Wochen und 13-Wochen-Forecast; Fortbestehensprognose § 19 Abs. 2 InsO; Sanierungskonzept auf IDW-S-6-Niveau vorbereiten, wenn Banken, Warenkreditversicherer oder Schlüsselglaeubiger mittragen sollen.
2. **Gläubigerstruktur:** Rangtabelle erstellen: gesichert (§§ 49-51 InsO) → Masseforderungen → unsecured → Nachrang § 39 InsO; BATNA je Gläubiger errechnen.
3. **Vorverhandlung Schlüssel-Gläubiger:** Bank zuerst (groesstes Sicherheitenvolumen); Stillhalte-Vereinbarung 90 Tage; Term Sheet Vergleichsquoten.
4. **Plan-Aufstellung:** StaRUG-Plan oder InsO-Plan; Klassenbildung; Vergleichsrechnung; Mehrheiten-Simulation.
5. **Abstimmung und Bestaetigung:** Eroerungs- und Abstimmungstermin; § 25 StaRUG (75%) oder § 244 InsO (50% Kopf + Summe); Cramdown § 26 StaRUG / § 245 InsO.

## Output-Template Verhandlungsnotiz Schlüssel-Gläubiger

**Adressat:** Intern (Handakte) — Tonfall: strukturiert-sachlich

```
VERHANDLUNGSNOTIZ — VERTRAULICH
Datum: [DATUM]
Mandant: [FIRMA]
Glaeubiger: [BANK / LIEFERANT]
Vertreter: [NAME]

BATNA unserer Seite: [z.B. Antrag auf Eigenverwaltung sofort]
BATNA Gegenseite: [z.B. Vollstreckung Sicherheit, Quote ca. XX% in Liquidation]
ZOPA: [Vergleichsquote zwischen XX% und YY%]

ERGEBNIS DER VERHANDLUNG:
Forderungsbetrag: EUR [BETRAG]
Angebot Schuldnerin: [XX% in Z Raten]
Glaeubiger-Position: [...]
Naechster Schritt: [...]
Frist: [DATUM]
```

---

## Anwendungshinweise

1. Diesen Vollprüfung als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.
