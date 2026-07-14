# Vollprüfung: fachanwalt-insolvenz-sanierungsrecht

## Zusammensetzung

Diese Vollprüfung enthält top-8 von 506 Skills (gekürzt für das Arbeitsfenster) des Plugins `fachanwalt-insolvenz-sanierungsrecht`.

## Inhaltsverzeichnis

1. **insolvenz-sanierungs-versandmappe-endfertigen** — Endfertigt Insolvenz-, Eigenverwaltungs-, StaRUG-, Anfechtungs- und Tabellenfeststellungsunterlagen: trennt Insolvenzger…
2. **einstieg-routing** — Wenn es um Anwalts-Dashboard Fachanwalt Insolvenz- und Sanierungsrecht in Fachanwalt Insolvenz- und Sanierungsrecht geht…
3. **fachanwalt-insolvenz-sanierungsrecht-orientierung** — Wenn es um Fachanwalt für Insolvenz- und Sanierungsrecht — Orientierung in Fachanwalt Insolvenz- und Sanierungsrecht geh…
4. **orientierung-mandat-fachanwaltschaft** — Wenn es um Orientierung Mandat Fachanwaltschaft in Fachanwalt Insolvenz- und Sanierungsrecht geht: prüft Frist, Form, Zu…
5. **erstgespraech-mandatsannahme** — Wenn es um Erstgespraech Mandatsannahme in Fachanwalt Insolvenz- und Sanierungsrecht geht: prüft Frist, Form, Zuständigk…
6. **erstpruefung-und-mandatsziel** — Wenn es um Erstpruefung Und Mandatsziel in Fachanwalt Insolvenz- und Sanierungsrecht geht: klärt Rolle, Ziel, Frist, Unt…
7. **zahlungsunfaehigkeit-liquiditaetsstatus-streitige-forderungen** — Prüft Zahlungsunfähigkeit mit tagesgenauem Liquiditätsstatus und besonderem Fokus auf streitige oder titulierte Forderun…
8. **restschuldbefreiung-dreijahresfrist-obliegenheiten** — Steuert Restschuldbefreiung nach aktuellem Recht vom Antrag bis zur Entscheidung. Prüft Antragsdatum, Abtretungsfrist, W…

---

## Skill: `insolvenz-sanierungs-versandmappe-endfertigen`

_Endfertigt Insolvenz-, Eigenverwaltungs-, StaRUG-, Anfechtungs- und Tabellenfeststellungsunterlagen: trennt Insolvenzgericht, Restrukturierungsgericht und Prozessgericht, prüft Antrag, Planstand, Liquiditätsbelege, Gläubigergruppen und Glaubhaftmachung, erzeugt getrennte Einzel-PDFs und liefert gerichtsspezifische Versandmappen mit fortgeführtem Anlagenkreis und Eingangscheck._

# Insolvenz- und Sanierungsversandmappe endfertigen

## 1. Gericht und Verfahren

Lies sämtliche Entwürfe, Plananlagen, Liquiditätsrechnungen, Gläubigerlisten, Registerdaten, Titel und gerichtlichen Hinweise. Trenne Eröffnungsantrag, Eigenverwaltung, Schutzschirm, Restrukturierungssache nach StaRUG, Forderungsprüfung und streitige Klage. Eine Nachricht darf nicht mehrere gerichtliche Verfahren vermischen.

## 2. Produktionsprüfung

1. Schuldner, Vertretung und Registerstand mit Originalauszug abgleichen.
2. Insolvenzgrund oder drohende Zahlungsunfähigkeit mit datierter Berechnung und Belegfundstellen verbinden.
3. Eigenverwaltungsplanung, Finanzplan, Verfahrenskosten und Gläubigerinteressen auf denselben Stichtag bringen.
4. Restrukturierungsplan, Gruppen, Stimmrechte und Vergleichsrechnung versionsfest halten.
5. Bei Anfechtung oder Tabellenfeststellung Anspruch, Zahlung, Fälligkeit, Kenntnis und Bestreitensgrund belegen.

## 3. Anlagen- und Versionslogik

Gerichtsformulare und gesetzliche Pflichtanlagen bleiben eigenständig. Planfassungen erhalten eindeutigen Stand und Hashwert. Für streitige Klagen K/B fortführen; für Insolvenz- und Restrukturierungsgericht neutralen oder vorgegebenen Anlagenkreis nutzen. Jede Seite stempeln, Tabellen auf abgeschnittene Spalten und Formelfehler kontrollieren.

## 4. Auslieferung

Liefere je Verfahren einen Versandordner mit Hauptdokument, Pflichtanlagen, Stichtags- und Versionsmatrix, Gläubiger- und Betragskontrolle, Manifest, Freigabevermerk und Eingangskontrolle. Stoppe bei uneinheitlichem Stichtag, veralteter Planfassung, fehlender Pflichtanlage, unklarer Zuständigkeit oder vermischten Verfahren.

---

## Skill: `einstieg-routing`

_Wenn es um Anwalts-Dashboard Fachanwalt Insolvenz- und Sanierungsrecht in Fachanwalt Insolvenz- und Sanierungsrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Anwalts-Dashboard Fachanwalt Insolvenz- und Sanierungsrecht

> Antragspflicht, Eigenverwaltung, Anfechtung, Restrukturierung: Der Antrag ist ohne schuldhaftes Zögern zu stellen; drei Wochen bei Zahlungsunfähigkeit und sechs Wochen bei Überschuldung sind nur Höchstfristen.
>
> Sie sehen unten die Sofort-Triage. Keine Rückfragen, bis die Tabelle steht. Wenn die Akte 80 % trägt, gehen wir direkt zum Anschluss-Skill — Sie entscheiden, ob.

## Sofort-Triage

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
| --- | --- | --- |
| Rolle | Wen vertrete ich? (Mandant · Gegenseite · Mehrere) | Mandantenmail, Vertretungsbestellung |
| Verfahrensstand | Vorprozessual · außergerichtlich · Klage · Rechtsmittel · Vollstreckung | Vorhandene Schriftsätze, Eingangsstempel |
| Eilfrist | **Paragraf 15a Absatz 1 InsO:** Antrag ohne schuldhaftes Zögern, höchstens drei Wochen bei Zahlungsunfähigkeit und sechs Wochen bei Überschuldung. **Paragraf 270d InsO:** Schutzschirm nur bei drohender Zahlungsunfähigkeit oder Überschuldung und fehlender Zahlungsunfähigkeit. | Objektiven Eintritt des Insolvenzgrunds und gerichtliche Bekanntmachungen dokumentieren |
| Hauptanspruch | Antragspflicht §§ 15a, 17 ff. InsO · Anfechtung §§ 129 ff. InsO · GF-Haftung § 64 GmbHG a. F. / § 15b InsO n. F. · Gläubigeranfechtung AnfG außerhalb Insolvenz · Schutzschirm § 270d InsO · Eigenverwaltung § 270 InsO · StaRUG (Stabilisierungs- und Restrukturierungsrahmen). | Sachverhaltsabgleich mit Tatbestandsmerkmalen |
| Zuständigkeit | Insolvenzgericht (AG am Sitz, § 3 InsO). Restrukturierungsgericht nach StaRUG = LG (§§ 30 ff. StaRUG). Anfechtungsklage gegen Gläubiger: LG/AG nach Streitwert. | Gesetz, Vertrag, Gerichtsstandsklausel |

## Risiko-Ampel

- **Frist:** 🔴 Paragraf 15a InsO: ohne schuldhaftes Zögern, höchstens drei Wochen ab Zahlungsunfähigkeit und sechs Wochen ab Überschuldung. Keine Höchstfrist als Sanierungsaufschub behandeln. 🟠 Eigenverwaltung nach Paragraf 270a ff. InsO und Schutzschirm nach Paragraf 270d InsO nur bei erfüllten Voraussetzungen vorbereiten.
- **Beweislage:** 🔴 Zahlungsunfähigkeit § 17 II InsO: 3-Wochen-Liquiditätsstatus. Buchhaltungs- und Bankkontodaten sichern. 🟠 Überschuldung § 19 II InsO: Fortbestehensprognose dokumentieren.
- **Wirtschaftlich:** 🔴 Zahlungen nach Insolvenzreife unter Paragraf 15b InsO einzeln erfassen und nur nach dessen Maßstab fortführen. 🟠 Bei Paragraf 133 InsO den Grundzeitraum von zehn Jahren, den Vierjahreszeitraum für Sicherung oder Befriedigung und die Sonderregeln der Absätze 3 und 4 auseinanderhalten.

## Anschluss-Skills (Router)

| Wenn der Fall trägt … | dann Skill | Erwartung |
| --- | --- | --- |
| Fortbestehensprognose anwerfen | `insanw-fortbestehensprognose-workflow` | Liquiditätsplan 12 Monate, IDW S 11, Beweisdokument |
| Eigenverwaltung / Schutzschirm Paragraf 270d InsO | `insanw-eigenverwaltung-schutzschirm-spezial` | Eigenverwaltungsplanung, Bescheinigung, Planvorlagefrist, Sachwalter |
| **Antragspflicht Paragraf 15a InsO** | `inso-p015a-antragspflicht-bei-juristischen-personen-und-rechtsfa` | unverzüglicher Antrag, Drei-/Sechswochen-Höchstfrist, Organhaftung, Strafrecht |
| Anfechtungsmandat (Gläubiger / Verwalter) | `insanw-anfechtungsmandat-leitfaden` | Tatbestände §§ 129 ff. InsO, Verteidigungsstrategie |
| Konzerninsolvenz / Gruppenkoordination | `insanw-konzerninsolvenz-koordination-spezial` | Gruppen-Gerichtsstand § 3a InsO, Koordinationsverfahren |

## Norm-Radar

- **Paragraf 15a InsO** — Insolvenzantragspflicht ohne schuldhaftes Zögern; höchstens drei Wochen bei Zahlungsunfähigkeit und sechs Wochen bei Überschuldung
- **§ 17 InsO** — Zahlungsunfähigkeit
- **§ 19 InsO** — Überschuldung
- **§ 270 InsO** — Eigenverwaltung; § 270d Schutzschirm
- **Paragraf 133 InsO** — zehnjähriger Grundzeitraum; vier Jahre, wenn die Handlung Sicherung oder Befriedigung gewährt oder ermöglicht; Absatz 3 und 4 gesondert prüfen
- **§ 15b InsO** — Zahlungsverbot nach Insolvenzreife

## Genau eine Rückfrage (nur wenn nötig)

> Stehen wir **vor** der Antragstellung (Beratung GF / Sanierung) oder **nach** Verfahrenseröffnung (Verwalter, Gläubiger, Anfechtung)?

Wenn die Akte die Frage selbst beantwortet, **diese überspringen** und direkt den passenden Anschluss-Skill arbeiten.

## Leitentscheidungs-Anker (Such-Wegweiser, keine fertigen Zitate)

- **Verwertung und Betriebsveräußerung** — Paragrafen 159, 160 und 163 InsO nach Verfahrensstand, Sicherungsrechten, Beschlusslage und dokumentiertem Marktprozess prüfen. Einen Haftungsanker nach Paragraf 60 InsO nur verwenden, wenn Sachverhalt, Pflichtenkreis und tragende Aussage der Entscheidung tatsächlich passen.
- **Vorsatzanfechtung und Bargeschäft** — Paragraphen 133 und 142 InsO tatbestandsbezogen prüfen; erst nach Festlegung von Handlung, Deckungsart, Benachteiligung und Kenntnis die passende Entscheidung des IX. Zivilsenats auswählen.
- **Insolvenzantragspflicht und Zahlungsverbot** — Paragraphen 15a und 15b InsO strikt nach Pflichtigem, Insolvenzgrund, Frist, Zahlung und Privilegierung trennen.
- **Geschäftsveräußerung im Ganzen** — EuGH, Urteil vom 27.11.2003 - C-497/01 (Zita Modes): Übertragung einer selbständigen wirtschaftlichen Einheit, die fortgeführt werden kann. EuGH, Urteil vom 10.11.2011 - C-444/10 (Schriever): Erforderlichkeit mitübertragener Betriebsgrundlagen, insbesondere von Räumen, hängt von Art und Umständen der Tätigkeit ab.

> Diese Anker sind Sucheinstieg. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief die konkrete Entscheidung in der amtlichen Quelle öffnen und Datum, Aktenzeichen, Randnummer sowie Übertragbarkeit auf den festgestellten Sachverhalt prüfen. Kuratierte Anker-Sammlung in `references/leitentscheidungen-anker.md`.

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
- BGH, Urteil vom 18.04.2024 - IX ZR 129/22: Ein außenstehender Dritter darf einen nur pauschal aufgestellten und nicht mit Einzelpositionen oder Belegen unterlegten Liquiditätsstatus grundsätzlich einfach bestreiten. Die Entscheidung ist ein Darlegungsanker zu Paragraf 17 InsO, kein pauschaler Beleg für geringere Anfechtungsrisiken.
  <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=18.04.2024&Aktenzeichen=IX+ZR+129/22>
- **BGH IX ZR 239/22 vom 18.04.2024** — Bei der Vorsatzanfechtung lässt sich die erforderliche Deckungslücke regelmäßig nicht allein aus den bereits zur Zahlungseinstellung herangezogenen Verbindlichkeiten ableiten; wiederholte Zahlungsverzögerungen belegen für sich noch keine Zahlungseinstellung.
  <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=18.04.2024&Aktenzeichen=IX+ZR+239/22>
- **BGH IX ZR 114/23 vom 19.12.2024** — Forderungsanmeldung bei Abtretung; Individualisierung.
  <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=19.12.2024&Aktenzeichen=IX+ZR+114/23>
- **BGH IX ZR 127/24 vom 13.11.2025** (Wirecard) — Aktionärs-Schadensersatzforderungen sind in der Insolvenz der AG keine einfachen Insolvenzforderungen iSd § 38 InsO; Nachrang.
- **BGH II ZR 206/22 vom 23.07.2024** — Fortwirkende Haftung des ausgeschiedenen Geschäftsführers für Neugläubigerschäden (§ 823 II BGB iVm § 15a InsO).
  <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=23.07.2024&Aktenzeichen=II+ZR+206/22>
- **BGH IV ZR 66/25 vom 19.11.2025** — D&O-Versicherung; Wissentlichkeitsausschluss erfordert positive Kenntnis pro konkreter Pflichtverletzung; § 15a / § 15b InsO nicht koppelbar.
- **BGH 5 StR 287/24 vom 27.02.2025** — Faktischer Geschäftsführer / Firmenbestattung.
  <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=27.02.2025&Aktenzeichen=5+StR+287/24>
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
- Tragende Normen verifizieren: Zuerst den im Skilltitel bezeichneten InsO- oder StaRUG-Tatbestand im aktuellen Gesetzestext prüfen. Eröffnungsantrag nach Paragraf 13 InsO, Gläubigerantrag nach Paragraf 14 InsO und Antragspflicht organschaftlicher Vertreter nach Paragraf 15a InsO strikt trennen; Steuerrecht, IDW-Standards oder Auslandsrecht nur bei einer konkreten Schnittstelle ergänzen.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Orientierung im Insolvenz- und Sanierungsrecht für Mandate und Fachanwaltschaft nach § 14 FAO. Anwendungsfall Kanzlei will Insolvenzmandat beurteilen oder Anwalt bereitet sich auf FAO-Fachanwaltsprüfung vor. Normen §§ 17-19 InsO Eroeffnungsgründe § 15a InsO Antragspflicht §§ 270 ff. InsO Eigenverwaltung § 270d InsO Schutzschirm StaRUG EuInsVO. Prüfraster Eroeffnungsgründe Antragspflicht Plan-Verfahren Anfechtung Fachanwalt-Voraussetzungen verifizierbare Quellen. Output Rechtsgebietsuebersicht mit Normenkarte verifizierbare Quellen und Routing zu Mandatsskills. Abgrenzung zu erstgespraech-mandatsannahme und fachanwalt-insolvenz-sanierungsrecht-restrukturierungsplan.

### Fachanwalt für Insolvenz- und Sanierungsrecht — Orientierung

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Fachanwalt für Insolvenz- und Sanierungsrecht — Orientierung` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
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
- BGH, Urteil vom 18.04.2024 - IX ZR 129/22: Ein außenstehender Dritter darf einen nur pauschal aufgestellten und nicht mit Einzelpositionen oder Belegen unterlegten Liquiditätsstatus grundsätzlich einfach bestreiten. Die Entscheidung ist ein Darlegungsanker zu Paragraf 17 InsO, kein pauschaler Beleg für geringere Anfechtungsrisiken.
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=18.04.2024&Aktenzeichen=IX+ZR+129/22>
- **BGH IX ZR 239/22 vom 18.04.2024** — Bei der Vorsatzanfechtung lässt sich die erforderliche Deckungslücke regelmäßig nicht allein aus den bereits zur Zahlungseinstellung herangezogenen Verbindlichkeiten ableiten; wiederholte Zahlungsverzögerungen belegen für sich noch keine Zahlungseinstellung.
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=18.04.2024&Aktenzeichen=IX+ZR+239/22>
- **BGH IX ZR 114/23 vom 19.12.2024** — Forderungsanmeldung bei Abtretung; Individualisierung.
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=19.12.2024&Aktenzeichen=IX+ZR+114/23>
- **BGH IX ZR 127/24 vom 13.11.2025** (Wirecard) — Aktionärs-Schadensersatzforderungen sind in der Insolvenz der AG keine einfachen Insolvenzforderungen iSd § 38 InsO; Nachrang.
- **BGH II ZR 206/22 vom 23.07.2024** — Fortwirkende Haftung des ausgeschiedenen Geschäftsführers für Neugläubigerschäden (§ 823 II BGB iVm § 15a InsO).
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=23.07.2024&Aktenzeichen=II+ZR+206/22>
- **BGH IV ZR 66/25 vom 19.11.2025** — D&O-Versicherung; Wissentlichkeitsausschluss erfordert positive Kenntnis pro konkreter Pflichtverletzung; § 15a / § 15b InsO nicht koppelbar.
- **BGH 5 StR 287/24 vom 27.02.2025** — Faktischer Geschäftsführer / Firmenbestattung.
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=27.02.2025&Aktenzeichen=5+StR+287/24>
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
- Tragende Normen verifizieren: Zuerst den im Skilltitel bezeichneten InsO- oder StaRUG-Tatbestand im aktuellen Gesetzestext prüfen. Eröffnungsantrag nach Paragraf 13 InsO, Gläubigerantrag nach Paragraf 14 InsO und Antragspflicht organschaftlicher Vertreter nach Paragraf 15a InsO strikt trennen; Steuerrecht, IDW-Standards oder Auslandsrecht nur bei einer konkreten Schnittstelle ergänzen.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Strukturierter Erstgespraechsleitfaden für Insolvenz- und Restrukturierungsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen.

### Erstgespraech und Mandatsannahme im Insolvenz- und Restrukturierungsrecht

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Erstgespraech und Mandatsannahme im Insolvenz- und Restrukturierungsrecht` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
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
- Im Anfechtungsmandat: BGH, Urteil vom 05.12.2024 - IX ZR 122/23, zur Unlauterkeit beim Bargeschäft; BGH, Urteil vom 18.04.2024 - IX ZR 239/22, zur Deckungslücke und zur Erwartung künftiger Gläubigerbefriedigung; BGH, Urteil vom 18.04.2024 - IX ZR 129/22, nur zur Darlegung und zum Bestreiten eines Liquiditätsstatus.
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
- Tragende Normen verifizieren: Zuerst den im Skilltitel bezeichneten InsO- oder StaRUG-Tatbestand im aktuellen Gesetzestext prüfen. Eröffnungsantrag nach Paragraf 13 InsO, Gläubigerantrag nach Paragraf 14 InsO und Antragspflicht organschaftlicher Vertreter nach Paragraf 15a InsO strikt trennen; Steuerrecht, IDW-Standards oder Auslandsrecht nur bei einer konkreten Schnittstelle ergänzen.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel im Insolvenz- und Sanierungsrecht: fachlich vertieftes Modul mit Normenradar (InsO/StaRUG/IDW-S6), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.

### Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
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

## Skill: `zahlungsunfaehigkeit-liquiditaetsstatus-streitige-forderungen`

_Prüft Zahlungsunfähigkeit mit tagesgenauem Liquiditätsstatus und besonderem Fokus auf streitige oder titulierte Forderungen. Trennt objektiven Bestand, Fälligkeit, Einfordern, Vollstreckung und Beweislast und liefert Status, Haftungsvermerk, Antragspflichtentscheidung und gerichtsfesten Vortrag._

# Zahlungsunfähigkeit und streitige Forderungen prüfen

## 1. Einsatzlage

Eine Liquiditätslücke, Organhaftung, Insolvenzanfechtung, ein Gläubigerantrag oder ein Sanierungsfenster verlangt eine stichtagsbezogene Prüfung nach Paragraf 17 InsO. Forderungen werden nicht nach gefühltem Prozessrisiko quotiert, sondern nach objektivem Bestand, Fälligkeit und den besonderen Beweiswirkungen eines Titels behandelt.

## 2. Normenanker

- Paragraf 17 InsO: Zahlungsunfähigkeit und Zahlungseinstellung.
- Paragrafen 14, 15a und 15b InsO: Gläubigerantrag, Antragspflicht und Zahlungen nach Insolvenzreife.
- Paragrafen 18 und 19 InsO: drohende Zahlungsunfähigkeit und Überschuldung als getrennte Tatbestände.
- Paragrafen 271 und 286 BGB: Fälligkeit und Verzug; ernsthaftes Einfordern ist insolvenzrechtlich eigenständig zu würdigen.
- Paragrafen 707, 719, 769 und 775 ZPO: Vollstreckungseinstellung und Vollstreckungshindernisse, soweit ein Titel die Forderungsbehandlung beeinflusst.

## 3. Rechtsprechungsanker

- BGH, Urteil vom 23. Januar 2025 - IX ZR 229/22: Zahlungsunfähigkeit ist ein objektiver Zustand. Bei nicht titulierten streitigen Forderungen kommt es auf objektiven Bestand und Fälligkeit an. Ein vorläufig vollstreckbarer Titel ist bei eingeleiteter Vollstreckung in Höhe des Nennwerts zu berücksichtigen; eine Prozessrisikoquote gibt es dafür nicht.
- BGH, Urteil vom 18. April 2024 - IX ZR 129/22: Legt der Insolvenzverwalter gegenüber einem außenstehenden Dritten nur einen nicht einzelpostenfähig erläuterten Liquiditätsstatus vor, kann einfaches Bestreiten genügen. Status und Belege müssen deshalb Gläubiger, Grund, Fälligkeit und Betrag nachvollziehbar machen.
- BGH, Urteil vom 28. Juni 2022 - II ZR 112/21: Zahlungsunfähigkeit kann anhand mehrerer aussagekräftiger, tagesgenauer Liquiditätsstatus dargelegt werden.
- BGH, Urteil vom 19. Dezember 2017 - II ZR 88/16: Im Dreiwochenzeitraum fällig werdende Verbindlichkeiten sind in die Betrachtung einzubeziehen; eine fortgeschobene Bugwelle darf nicht ausgeblendet werden.
- BGH, Urteil vom 24. Mai 2005 - IX ZR 123/04: Grundlinie zur Abgrenzung einer bloßen Zahlungsstockung anhand Lücke, Zeitraum und begründeter Erwartung der Schließung.
- BGH, Beschluss vom 22. Mai 2025 - IX ZB 38/24: Nur für den Gläubigerantrag nach Paragraf 14 InsO gilt die besondere Aussage, dass die Beweiswirkung eines vollstreckbaren Endurteils nach gerichtlicher Einstellung der Vollstreckung entfallen kann. Das ersetzt nicht die objektive Prüfung nach Paragraf 17 InsO.

## 4. Prüfprogramm

1. Prüfzweck und Stichtag festlegen. Organhaftung, Anfechtung, Eröffnungsantrag und Sanierungsentscheidung dürfen nicht in einem unscharfen Zeitraum zusammenfallen.
2. Aktiva I erfassen: freie Kontoguthaben, Kasse und sofort ziehbare, rechtlich gesicherte Kreditlinien.
3. Aktiva II erfassen: nur innerhalb von drei Wochen mit belastbarem Zuflussnachweis realisierbare Mittel. Eigene streitige Forderungen nicht ohne Realisierungsbeleg ansetzen.
4. Passiva I und II einzelpostenfähig bilden: Gläubiger, Rechtsgrund, Nennwert, Fälligkeit, Einfordern, Stundung, Bestreiten, Titel und Vollstreckungsstand.
5. Streitige Verbindlichkeit entscheiden: objektiv nicht bestehend oder nicht fällig gleich nicht passivieren; objektiv bestehend und fällig gleich Nennwert passivieren. Keine prozentuale Abwertung nach Prozesschance.
6. Titulierte Forderung nach IX ZR 229/22 behandeln. Titel, Vollstreckbarkeit, Sicherheitsleistung, Zustellung, Vollstreckungsbeginn und gerichtliche Einstellung vollständig prüfen.
7. Wer eine Forderung herausnimmt, dokumentiert Tatsachen, Rechtsgrund und Belege. Ein Rechtsgutachten kann den subjektiven Kenntnisstand stützen, beseitigt aber nicht das objektive Haftungsrisiko, wenn die Forderung tatsächlich besteht.
8. Zahlungseinstellung zusätzlich anhand Indizien prüfen: Lohn, Steuern, Sozialversicherung, Rücklastschriften, geplatzte Raten, Pfändungen und Vollstreckungsdruck.
9. Ergebnis mit Antragspflicht, Zahlungsverbot, Sanierungsschritten und täglicher Aktualisierung verbinden.

## 5. Arbeitsergebnis

Liefere tagesgenauen Liquiditätsstatus, Dreiwochenfortschreibung, Forderungs- und Titelmatrix, Belegindex, Organhaftungsvermerk und klare Entscheidung zu Antragspflicht oder weiterem Prüfbedarf. Jede Herausnahme einer streitigen Forderung erhält eine beweisfähige Begründung.

## 6. Belege und Aktenlücken

- Kontoauszüge, Kasse und verbindliche Kreditlinien
- OPOS-Listen mit Einzelbelegen und Fälligkeiten
- Verträge, Rechnungen, Mahnungen, Stundungen und Einwendungen
- Titel, Klausel, Zustellung, Sicherheitsleistung und Vollstreckungsakte
- Zahlungspläne, Organbeschlüsse und Beratervermerke

---

## Skill: `restschuldbefreiung-dreijahresfrist-obliegenheiten`

_Steuert Restschuldbefreiung nach aktuellem Recht vom Antrag bis zur Entscheidung. Prüft Antragsdatum, Abtretungsfrist, Wiederholungsfall, Erwerbs- und Auskunftsobliegenheiten, Versagungsanträge, ausgenommene Forderungen und Nachtragsverteilung und liefert Fristenplan und vollständige Anträge._

# Restschuldbefreiung nach aktuellem Recht steuern

## 1. Einsatzlage

Eine natürliche Person beantragt Restschuldbefreiung oder muss einen Versagungsantrag abwehren. Der Workflow unterscheidet Verfahren nach Antragsdatum, laufendes Insolvenzverfahren, Abtretungszeit und bereits früher erteilte Restschuldbefreiung.

## 2. Normenanker

- Paragrafen 286, 287 und 287a InsO: Grundsatz, Antrag, Abtretung und Zulässigkeitsentscheidung.
- Paragraf 287 Absatz 2 InsO: grundsätzlich drei Jahre Abtretungsfrist ab Eröffnung; fünf Jahre im gesetzlich bezeichneten Wiederholungsfall.
- Paragrafen 287b, 290, 295, 295a, 296 bis 298 und 300 InsO: Erwerbsobliegenheit, Versagungsgründe, Obliegenheiten und Entscheidung.
- Paragrafen 301 und 302 InsO: Wirkung und ausgenommene Forderungen.
- Artikel 103k EGInsO: Übergangsrecht für vor dem 1. Oktober 2020 beantragte Verfahren.

## 3. Rechtsprechungsanker

- BGH, Beschluss vom 7. März 2024 - IX ZB 47/22: Ein Versagungsantrag nach Paragraf 290 InsO muss bis zum maßgeblichen Zeitpunkt schlüssig dargelegt und erforderlichenfalls glaubhaft gemacht sein; erst dann greift die Amtsermittlung. Ein geringer Einkommensunterschied begründete im konkreten Fall keine unangemessene Erwerbstätigkeit.
- BGH, Beschluss vom 26. September 2024 - IX ZB 5/24: Die erteilte Restschuldbefreiung hindert eine Nachtragsverteilung nicht, wenn der Gegenstand zur Insolvenzmasse gehört. Abtretung, Massezugehörigkeit und Wirkung der Restschuldbefreiung sind deshalb getrennt zu prüfen.
- Die frühere Sechsjahres- und Quotenrechtsprechung darf nicht ohne Übergangsprüfung auf einen nach dem 30. September 2020 gestellten Antrag übertragen werden.

## 4. Prüfprogramm

1. Datum des Insolvenzantrags, Eröffnungsdatum, Verfahrensart und frühere Restschuldbefreiungen feststellen. Daraus Rechtsfassung und Frist berechnen.
2. Antrag nach Paragraf 287 InsO, Abtretungserklärung und Erklärung zu Sperrgründen auf Vollständigkeit prüfen; bei Verbraucherinsolvenz Paragraf 305 InsO mitbearbeiten.
3. Drei- oder Fünfjahresfrist kalendarisch führen. Die aktuelle Dreijahresfrist verlangt keine Mindestbefriedigungsquote.
4. Pflichten phasenbezogen ordnen: Auskunft und Mitwirkung im eröffneten Verfahren, Erwerbsobliegenheit, Herausgabe- und Anzeigepflichten sowie Zahlungen nur an den Treuhänder.
5. Selbständige Tätigkeit nach Paragraf 295a InsO mit fiktivem angemessenem Dienstverhältnis und Zahlungsplan dokumentieren.
6. Jeden Versagungsantrag nach Norm, Tatsachen, Verschulden, Gläubigerbeeinträchtigung, Antragsberechtigung, Frist und Glaubhaftmachung prüfen. Tatbestände nicht vermischen.
7. Wirkungen der Restschuldbefreiung gläubigerbezogen bestimmen. Forderungen nach Paragraf 302 InsO, Rechte gegen Mitschuldner und Massegegenstände gesondert ausweisen.
8. Vor Entscheidung offene Masse, Nachtragsverteilung, Steuererstattung und noch nicht abgeschlossene Feststellungsprozesse kontrollieren.

## 5. Arbeitsergebnis

Erstelle Rechtsstands- und Fristenblatt, Obliegenheitenkalender, Einkommens- und Herausgabematrix, Stellungnahme zu Versagungsanträgen, Entscheidungsvorschlag und Liste fortbestehender Forderungen. Alt- und Neurecht werden sichtbar getrennt.

## 6. Belege und Aktenlücken

- Insolvenzantrag, Eröffnungsbeschluss und Abtretungserklärung
- frühere Verfahren und Entscheidungen zur Restschuldbefreiung
- Einkommens-, Bewerbungs- und Tätigkeitsnachweise
- Vermögenszugänge, Erbschaften, Schenkungen und Steuererstattungen
- Forderungsanmeldungen, Widersprüche und Versagungsanträge

---

## Anwendungshinweise

1. Diese Vollprüfung als Kontext einfügen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Bearbeiter anweisen, sich anhand der oben aufgeführten Skills zu orientieren.
4. Entscheidungen nur nach Prüfung von Gericht, Datum, Aktenzeichen, tragender Aussage und amtlicher oder frei zugänglicher Quelle verwenden.
