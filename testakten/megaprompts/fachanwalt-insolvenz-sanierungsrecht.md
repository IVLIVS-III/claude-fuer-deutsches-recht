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
7. **inso-p245a-schlechterstellung-bei-naturlichen-personen** — Prüft Paragraf 245a InsO als besondere Vergleichsannahme bei Insolvenzplänen natürlicher Personen. Ermittelt Einkommens-…
8. **restrukturierungsplan** — Führt ein StaRUG-Mandat vom Insolvenzreifetest über Planbetroffenenauswahl, Gruppen, Vergleichsrechnung und Abstimmung b…

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
| Zuständigkeit | Insolvenzgericht nach Paragraf 3 InsO bestimmen. Restrukturierungsgericht ist nach Paragraf 34 StaRUG grundsätzlich das Amtsgericht am Sitz eines Oberlandesgerichts; landesrechtliche Konzentration und die örtliche Zuständigkeit nach Paragraf 35 StaRUG aktuell prüfen. Anfechtungsklage gegen Gläubiger: Amts- oder Landgericht nach Zuständigkeit und Streitwert. | Gesetz, Landesverordnung, Register, Gerichtsverzeichnis |

## Risiko-Ampel

- **Frist:** Paragraf 15a InsO verlangt den Antrag ohne schuldhaftes Zögern; drei Wochen ab Zahlungsunfähigkeit und sechs Wochen ab Überschuldung sind nur Höchstfristen. Antrag und Planung der Eigenverwaltung nach Paragraf 270a InsO, vorläufige Anordnung nach Paragraf 270b InsO und Schutzschirm nach Paragraf 270d InsO nur bei erfüllten Voraussetzungen vorbereiten.
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

## Skill: `inso-p245a-schlechterstellung-bei-naturlichen-personen`

_Prüft Paragraf 245a InsO als besondere Vergleichsannahme bei Insolvenzplänen natürlicher Personen. Ermittelt Einkommens-, Vermögens- und Familienverhältnisse am Abstimmungstag, bildet das Ohne-Plan-Szenario mit oder ohne zulässigen Restschuldbefreiungsantrag und liefert Schlechterstellungsrechnung, Belegmatrix und gerichtsfesten Planbaustein._

# 1. Schlechterstellung bei natürlichen Personen

## 1.1 Direktstart

Lies Insolvenzplan, Gruppenübersicht, Vergleichsrechnung, Abstimmungsunterlagen, Antrag auf Restschuldbefreiung, Einkommensnachweise, Vermögensverzeichnis, Unterhaltspflichten und Verfahrenschronologie. Beginne mit einer Vergleichsrechnung; frage nur nach fehlenden Werten, die das Ergebnis verändern können.

## 1.2 Normfunktion

Paragraf 245a InsO ist keine allgemeine Absolute-Priority-Regel und kein eigener Cram-down-Tatbestand. Die Norm konkretisiert bei einem Schuldner, der eine natürliche Person ist, die voraussichtliche Schlechterstellung nach Paragraf 245 Absatz 1 Nummer 1 InsO. Über Paragraf 251 Absatz 2 Satz 2 InsO gilt sie auch beim individuellen Minderheitenschutz entsprechend.

Im Zweifel sind zwei Annahmen zu verwenden:

1. Die Einkommens-, Vermögens- und Familienverhältnisse am Tag der Abstimmung bleiben für die Verfahrensdauer und den anschließenden Zeitraum maßgeblich, in dem Insolvenzgläubiger ihre Restforderungen unbeschränkt geltend machen können.
2. Hat der Schuldner einen zulässigen Antrag auf Restschuldbefreiung gestellt, wird im Zweifel angenommen, dass die Restschuldbefreiung mit Ablauf der Abtretungsfrist des Paragrafen 287 Absatz 2 InsO erteilt wird.

## 1.3 Eingangstore

| Frage | Ergebnis | Beleg |
| --- | --- | --- |
| Ist der Schuldner eine natürliche Person? | [ja/nein] | [Eröffnungsbeschluss oder Stammdaten] |
| Wird die Zustimmungsfiktion nach Paragraf 245 InsO geprüft? | [ja/nein] | [Abstimmungsergebnis] |
| Oder liegt ein Antrag nach Paragraf 251 InsO vor? | [ja/nein] | [Widerspruch, Antrag und Protokoll] |
| Ist ein Antrag auf Restschuldbefreiung gestellt und zulässig? | [ja/nein/offen] | [Antrag und gerichtliche Verfügung] |
| Welcher Zeitpunkt war für die Abstimmung maßgeblich? | [Datum] | [Protokoll] |

Ohne natürliche Person oder ohne Schlechterstellungsprüfung nach Paragraf 245 beziehungsweise 251 InsO ist Paragraf 245a InsO nicht das richtige Werkzeug.

## 1.4 Tatsachenmatrix am Abstimmungstag

| Bereich | Ist-Zustand | Monatlicher oder einmaliger Wert | Beleg | Streitpunkt |
| --- | --- | ---: | --- | --- |
| Nettoeinkommen und variable Bezüge | [Angabe] | [EUR] | [Abrechnung] | [offen] |
| Selbständige Einkünfte | [Angabe] | [EUR] | [Auswertung und Bescheid] | [offen] |
| Pfändbarer Betrag | [Berechnung] | [EUR] | [Berechnungsblatt] | [offen] |
| Unterhaltsberechtigte Personen | [Angabe] | [Auswirkung] | [Urkunde und Zahlung] | [offen] |
| Verwertbares Vermögen | [Gegenstand] | [EUR] | [Bewertung] | [offen] |
| Absonderungsrechte und Kosten | [Angabe] | [EUR] | [Vertrag und Abrechnung] | [offen] |
| Neuerwerb und erwartbare Änderungen | [Angabe] | [EUR] | [Vertrag oder Prognose] | [offen] |

Änderungen gegenüber dem Abstimmungstag nicht frei erfinden. Wer von den gesetzlichen Zweifelsannahmen abweichen will, muss die konkrete Entwicklung und ihre belastbare Grundlage offenlegen.

## 1.5 Vergleichsrechnung

Rechne mindestens:

1. Planleistung je betroffener Gruppe und je widersprechendem Beteiligten.
2. Ohne-Plan-Erlös aus vorhandener Masse nach Kosten und Absonderung.
3. Erwartete pfändbare Bezüge während des maßgeblichen Zeitraums.
4. Wirkung eines zulässigen Restschuldbefreiungsantrags auf die Durchsetzbarkeit restlicher Forderungen.
5. Sensitivität für nachweisbar absehbare Änderungen von Einkommen, Vermögen oder Unterhalt.
6. Differenz aus Planwert und Ohne-Plan-Wert ohne Saldierung ungleichartiger Vorteile.

```text
Planwert des Beteiligten                         [EUR]
Ohne-Plan-Verteilung aus vorhandener Masse       [EUR]
Pfändbare Bezüge im Vergleichszeitraum            [EUR]
Sonstige belegte Erlöse                           [EUR]
Abzüglich Kosten und vorrangige Belastungen       [EUR]
Ohne-Plan-Wert gesamt                             [EUR]
Differenz Planwert minus Ohne-Plan-Wert            [EUR]
Ergebnis                                          [nicht schlechter/schlechter/offen]
```

## 1.6 Plan- und Gerichtsbaustein

```text
Der Schuldner ist eine natürliche Person. Für die Prüfung nach
Paragraf [245 Absatz 1 Nummer 1 / 251] InsO wird gemäß Paragraf 245a
InsO im Zweifel von den Einkommens-, Vermögens- und
Familienverhältnissen am Abstimmungstag [Datum] ausgegangen.

Ein zulässiger Antrag auf Restschuldbefreiung [liegt vor/liegt nicht
vor/ist aus folgenden Gründen noch offen]. [Bei zulässigem Antrag: Für
die Vergleichsrechnung wird im Zweifel die Erteilung mit Ablauf der
Abtretungsfrist nach Paragraf 287 Absatz 2 InsO zugrunde gelegt.]

Die Planleistung beträgt [EUR]. Der ohne Plan voraussichtlich
erreichbare Wert beträgt nach Abzug von [Kosten und Belastungen] [EUR].
Die Berechnung beruht auf den Anlagen [Bezeichnungen]. Offene
Sensitivitäten bestehen bei [Punkte].
```

## 1.7 Fehlerbremsen

1. Paragraf 245a InsO nicht als allgemeines Obstruktionsverbot bezeichnen; dieses steht in Paragraf 245 InsO.
2. Restschuldbefreiung nur bei zulässigem Antrag in die gesetzliche Zweifelsannahme einbeziehen.
3. Abtretungsfrist, Verfahrensdauer und Zeitraum unbeschränkter Restforderungsdurchsetzung nicht vermischen.
4. Pfändbares Einkommen nicht aus Bruttoeinkommen oder pauschalen Quoten ableiten.
5. Familienverhältnisse und Unterhaltspflichten am Abstimmungstag belegen.
6. Gruppen-Cram-down nach Paragraf 245 InsO und individuellen Minderheitenschutz nach Paragraf 251 InsO getrennt prüfen.
7. Vergleichsannahme und tatsächlich bewiesene abweichende Entwicklung kenntlich machen.

## 1.8 Quelle

- [Paragraf 245a InsO](https://www.gesetze-im-internet.de/inso/__245a.html)
- [Paragraf 245 InsO](https://www.gesetze-im-internet.de/inso/__245.html)
- [Paragraf 251 InsO](https://www.gesetze-im-internet.de/inso/__251.html)

---

## Skill: `restrukturierungsplan`

_Führt ein StaRUG-Mandat vom Insolvenzreifetest über Planbetroffenenauswahl, Gruppen, Vergleichsrechnung und Abstimmung bis zu Anzeige, Stabilisierung, Bestätigung und Vollzug. Liefert Verfahrensentscheidung, Planstruktur, Gruppen- und Mehrheitsmatrix, gerichtliche Anträge sowie einen belastbaren Fristenplan._

# 1. Restrukturierungsplan im Fachanwaltsmandat

## 1.1. Arbeitsstart

Lies zuerst Liquiditätsplanung, OPOS, Finanzierungsverträge, Sicherheiten, Planentwurf, Verhandlungsstand und Organbeschlüsse. Liefere aus dem vorhandenen Material eine Krisenampel, eine Gruppen- und Mehrheitsvorschau und den nächsten antrags- oder verhandlungsreifen Baustein. Frage nur nach Tatsachen, die Verfahrensweg, Planinhalt oder Frist ändern.

## 1.2. Erste Entscheidungsweichen

1. Liegt heute Zahlungsunfähigkeit nach Paragraf 17 InsO oder Überschuldung nach Paragraf 19 InsO vor?
2. Besteht nur drohende Zahlungsunfähigkeit nach Paragraf 18 InsO?
3. Reicht eine einvernehmliche außergerichtliche Sanierung oder ein privates Planangebot?
4. Welches gerichtliche Instrument nach Paragraf 29 Absatz 2 StaRUG wird benötigt?
5. Welche Rechte sind gestaltbar und welche Gläubiger müssen geschäftlich weiter vollständig bedient werden?
6. Ist eine Gruppenmehrheit nach Paragraf 25 StaRUG erreichbar oder muss Paragraf 26 StaRUG vorbereitet werden?

## 2. Normenkarte

| Station | Norm | Praxisfrage |
| --- | --- | --- |
| Insolvenzreife | Paragrafen 17 bis 19 und 15a InsO | Ist der präventive Weg noch offen und läuft eine Antragspflicht? |
| Gestaltbare Rechte | Paragrafen 2 bis 4 StaRUG | Was darf der Plan verändern? |
| Planinhalt | Paragrafen 5 bis 15 StaRUG | Sind Darstellung, Gestaltung und Anlagen vollständig? |
| Auswahl und Gruppen | Paragrafen 8 bis 10 StaRUG | Sind Auswahl, Rechtsstellung und Gleichbehandlung sachgerecht? |
| Planangebot | Paragrafen 17 bis 22 StaRUG | Sind Hinweise, Frist, Erörterung und Dokumentation ordnungsgemäß? |
| Stimmrecht und Mehrheiten | Paragrafen 24 bis 28 StaRUG | Stimmen Wertansätze, Gruppenmehrheit und Cram-down? |
| Instrumente und Anzeige | Paragrafen 29 bis 31 StaRUG | Welches Instrument wird genutzt und ist das Vorhaben angezeigt? |
| Stabilisierung | Paragrafen 49 bis 59 StaRUG | Welche Vollstreckung oder Verwertung muss gesperrt werden? |
| Bestätigung | Paragrafen 60 bis 67 StaRUG | Bestehen Versagungs-, Minderheiten- oder Beschwerderisiken? |
| Überwachung | Paragraf 72 StaRUG | Soll die Planerfüllung überwacht werden? |
| Beauftragter | Paragrafen 73 bis 79 StaRUG | Ist Bestellung zwingend oder wird sie beantragt? |

## 3. Verfahrensworkflow

### 3.1. Insolvenzreifetest

Erstelle zuerst den Liquiditätsstatus nach Paragraf 17 InsO, die regelmäßige 24-Monats-Prognose nach Paragraf 18 Absatz 2 InsO und die Überschuldungsprüfung nach Paragraf 19 InsO. Die Insolvenzantragspflicht ist ohne schuldhaftes Zögern zu erfüllen; die Höchstfristen betragen drei Wochen bei Zahlungsunfähigkeit und sechs Wochen bei Überschuldung.

Eine Stabilisierungsanordnung oder die Rechtshängigkeit der Restrukturierungssache setzt Paragraf 15a InsO nicht außer Kraft.

### 3.2. Planbetroffene auswählen

Arbeitnehmerforderungen einschließlich betrieblicher Altersversorgung sowie die weiteren Forderungen nach Paragraf 4 StaRUG sind nicht gestaltbar. Steuer- und Sozialversicherungsforderungen sind nicht pauschal ausgeschlossen; ihre Einbeziehung ist rechtsverhältnisbezogen zu prüfen.

Dokumentiere für jede Ein- und Nichteinbeziehung die sachgerechten Kriterien des Paragrafen 8 StaRUG. Operative Bedeutung allein ersetzt die gesetzliche Begründung nicht.

### 3.3. Plan und Anlagen erstellen

1. Planstruktur nach Paragraf 5 StaRUG.
2. Darstellender Teil einschließlich Vergleichsrechnung nach Paragraf 6 StaRUG.
3. Gestaltender Teil mit eindeutiger Rechtsänderung nach Paragraf 7 StaRUG.
4. Gruppenbildung nach Paragraf 9 StaRUG.
5. Gleichbehandlung innerhalb der Gruppe nach Paragraf 10 StaRUG.
6. Bestandsfähigkeits-, Vermögens- und Finanzunterlagen nach Paragraf 14 StaRUG.
7. Erklärungen von Gesellschaftern, Gläubigern, Dritten oder Sicherungsgebern nach Paragraf 15 StaRUG.

Ein Debt-to-Equity-Swap gegen den Willen des betroffenen Gläubigers ist nach Paragraf 7 Absatz 4 StaRUG ausgeschlossen.

### 3.4. Abstimmung und Cram-down

Nach Paragraf 25 StaRUG müssen mindestens drei Viertel der Stimmrechte jeder Gruppe zustimmen. Bei einer ablehnenden Gruppe prüfe Paragrafen 26 bis 28 StaRUG: keine Schlechterstellung ohne Plan, angemessene Beteiligung am Planwert, gesetzliche Gruppenmehrheit und Rangfolge mit den engen Ausnahmen des Paragrafen 28 StaRUG.

Der individuelle Minderheitenschutz nach Paragraf 64 StaRUG ist gesondert zu prüfen. Er setzt rechtzeitige Ablehnung, Widerspruch und Geltendmachung beziehungsweise Glaubhaftmachung der Schlechterstellung voraus.

### 3.5. Gerichtliche Instrumente

Ein privater Plan kann ohne gerichtliches Instrument vorbereitet und angeboten werden. Soll eine gerichtliche Planabstimmung, Vorprüfung, Stabilisierung oder Planbestätigung genutzt werden, ist das Vorhaben vorher nach Paragraf 31 StaRUG anzuzeigen. Mit der Anzeige wird die Restrukturierungssache rechtshängig.

Die Anzeige verliert grundsätzlich nach sechs Monaten ihre Wirkung; wurde sie vorher erneuert, nach zwölf Monaten. Das ist keine allgemeine 24-Monats-Verfahrensdauer.

## 4. Gruppen- und Mehrheitsmatrix

| Gläubiger | Recht | Betrag oder Wert | Sicherheit | Gestaltbar | Auswahlgrund | Gruppe | Stimmrecht | Zustimmung |
| --- | --- | ---: | --- | --- | --- | --- | ---: | --- |
| [Name] | [Recht] | [EUR] | [Sicherheit] | [ja/nein] | [Paragraf 8] | [Gruppe] | [EUR] | [ja/nein/offen] |

## 5. Anzeige nach Paragraf 31 StaRUG

```text
An das Amtsgericht [Ort] als Restrukturierungsgericht

1. Anzeige
Die Schuldnerin zeigt ihr Restrukturierungsvorhaben nach Paragraf 31
Absatz 1 StaRUG an.

2. Restrukturierungsziel
[Ziel, Planbetroffene, vorgesehene Maßnahmen und Instrumente]

3. Krise
[Art, Ausmaß und Ursachen; Paragrafen 17 bis 19 InsO mit Stichtag]

4. Planentwurf oder Restrukturierungskonzept
[Anlage A]

5. Verhandlungsstand
[Gläubiger, Anteilsinhaber, Dritte, Zustimmungsprognose]

6. Vorkehrungen zur Pflichterfüllung
[Organisation, Liquiditätsüberwachung, Berichtsweg]

7. Pflichtangaben
[Verbraucher sowie kleine und mittlere Unternehmen, erwarteter
Gruppenwiderstand, frühere Restrukturierungssachen]
```

## 6. Antrag auf Planbestätigung

```text
Antrag nach Paragraf 60 StaRUG

1. Plan und Anlagen
[Fassung, Datum, Anlagenverzeichnis]

2. Abstimmungsweg und Dokumentation
[außergerichtlich oder gerichtlicher Termin; Nachweise]

3. Gruppen und Stimmrechte
[Tabelle nach Paragrafen 9, 24 und 25 StaRUG]

4. Gruppenübergreifende Mehrheitsentscheidung
[nur falls erforderlich: Prüfung Paragrafen 26 bis 28 StaRUG]

5. Versagungsgründe
[Prüfung Paragraf 63 StaRUG]

6. Minderheitenschutz
[Widersprüche, Glaubhaftmachung, Ausgleichsmittel nach Paragraf 64]

7. Antrag
Der Restrukturierungsplan vom [Datum] wird bestätigt.
```

## 7. Fristen- und Wirkungsplan

| Vorgang | Regel | Arbeitsfolge |
| --- | --- | --- |
| Insolvenzantrag | unverzüglich; höchstens drei beziehungsweise sechs Wochen nach Paragraf 15a InsO | Fristbeginn und Sanierungsaussicht täglich prüfen |
| Außergerichtliches Planangebot | Annahmefrist grundsätzlich mindestens 14 Tage nach Paragraf 19 StaRUG | vollständigen Plan und Hinweise rechtzeitig zustellen |
| Gerichtlicher Abstimmungstermin | Ladungsfrist mindestens 14 Tage nach Paragraf 45 StaRUG | Zustellung und elektronischen Dokumentzugang sichern |
| Anzeige | Wirkungsverlust grundsätzlich nach sechs Monaten, nach Erneuerung nach zwölf Monaten | Long-Stop und Erneuerungsentscheidung kalendrieren |
| Stabilisierungsanordnung | zunächst bis drei Monate; Erweiterungen nur nach Paragraf 53 StaRUG | Planangebot und Bestätigungsantrag rechtzeitig vorbereiten |
| Planwirkungen | mit Bestätigung nach Paragraf 67 Absatz 1 StaRUG | Vollzugsvoraussetzungen und Rechtsmittelrisiko prüfen |

## 8. Rechtsprechungsanker

1. BVerfG, Beschluss vom 28.02.2025 - 1 BvR 418/25: Nichtannahme; keine Aussage zur generellen Verfassungsmäßigkeit oder materiellen Planrichtigkeit. Eine Beschwerde nach Paragraf 66 Absatz 2 Nummer 3 StaRUG verlangt konkrete Darlegung einer wesentlichen Schlechterstellung und des Ohne-Plan-Szenarios.
2. BGH, Beschluss vom 23.04.2026 - IX ZB 18/25: Bei Insolvenzreife während der Restrukturierung trägt der Schuldner die Darlegung für ein ausnahmsweises Absehen von der Aufhebung nach Paragraf 33 Absatz 2 StaRUG; freiwillige, rechtlich nicht gesicherte Drittbeiträge tragen die Fortführungsprognose des Vorhabens nicht zuverlässig.

## 9. Fehlerbremse

1. Paragraf 29 StaRUG nicht als Anzeigevorschrift verwenden.
2. Arbeitnehmer- und Betriebsrentenforderungen nicht in den Plan aufnehmen.
3. Paragraf 64 StaRUG nicht als allgemeinen Gruppen-Cram-down behandeln.
4. Keine allgemeine Prüferbescheinigung als gesetzliche Voraussetzung behaupten.
5. Restrukturierungsbeauftragten nicht pauschal als immer erforderlich darstellen; Paragrafen 73 und 77 getrennt prüfen.
6. Keine Kostenwerte oder Verfahrensdauer ohne aktenbezogene Grundlage versprechen.
7. Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle verwenden.

---

## Anwendungshinweise

1. Diese Vollprüfung als Kontext einfügen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Bearbeiter anweisen, sich anhand der oben aufgeführten Skills zu orientieren.
4. Entscheidungen nur nach Prüfung von Gericht, Datum, Aktenzeichen, tragender Aussage und amtlicher oder frei zugänglicher Quelle verwenden.
