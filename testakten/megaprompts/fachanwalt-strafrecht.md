# Vollprüfung: fachanwalt-strafrecht

## Zusammensetzung

Dieser Vollprüfung enthaelt top-8 von 240 Skills (gekuerzt fuer Chat-Fenster) des Plugins `fachanwalt-strafrecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Wenn es um Anwalts-Dashboard Fachanwalt Strafrecht in Fachanwalt Strafrecht geht: klärt Rolle, Ziel, Frist, Unterlagen u…
2. **mandat-triage-strafrecht** — Wenn es um Strukturierte Eingangs-Abfrage für Strafmandate in Fachanwalt Strafrecht geht: klärt Rolle, Ziel, Frist, Unte…
3. **fachanwalt-strafrecht-orientierung** — Wenn es um Fachanwalt für Strafrecht — Orientierung in Fachanwalt Strafrecht geht: klärt Rolle, Ziel, Frist, Unterlagen …
4. **orientierung-fristen-form-und-zustaendigkeit** — Wenn es um Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg in Fachanwalt Strafrecht geht: prüft Frist, Form, Zu…
5. **orientierung-mandat-fachanwaltschaft** — Wenn es um Orientierung Mandat Fachanwaltschaft in Fachanwalt Strafrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsw…
6. **erstgespraech-mandatsannahme** — Wenn es um Erstgespraech Mandatsannahme in Fachanwalt Strafrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und S…
7. **erstpruefung-und-mandatsziel** — Wenn es um Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel in Fachanwalt Strafrecht geht: klärt Rolle, Ziel, Fris…
8. **strafr-wirtschaftsstrafrecht-leitfaden** — Wenn es um Leitfaden Wirtschaftsstrafrecht: Untreue Paragraf 266 StGB, Betrug Paragraf 263, Bilanzdelikte Paragrafen 331…

---

## Skill: `einstieg-routing`

_Wenn es um Anwalts-Dashboard Fachanwalt Strafrecht in Fachanwalt Strafrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Anwalts-Dashboard Fachanwalt Strafrecht

> Vorladung, Durchsuchung, U-Haft, Anklage, Revision — Verfahrensphase entscheidet alles. Identität des Beschuldigten zuerst klären.
>
> Sie sehen unten die Sofort-Triage. Keine Rückfragen, bis die Tabelle steht. Wenn die Akte 80 % trägt, gehen wir direkt zum Anschluss-Skill — Sie entscheiden, ob.

## Sofort-Triage

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
| --- | --- | --- |
| Rolle | Wen vertrete ich? (Mandant · Gegenseite · Mehrere) | Mandantenmail, Vertretungsbestellung |
| Verfahrensstand | Vorprozessual · außergerichtlich · Klage · Rechtsmittel · Vollstreckung | Vorhandene Schriftsätze, Eingangsstempel |
| Eilfrist | **§ 311 II StPO: 1 Woche** sofortige Beschwerde. § 314 StPO: Berufung 1 Woche ab Verkündung. § 341 StPO: Revision 1 Woche ab Verkündung; § 345 StPO: Begründung 1 Monat ab Zustellung. § 33a StPO (Haftprüfung jederzeit). § 67 OWiG: Einspruch Bußgeld 2 Wochen. | Frist aus Zugangs-/Kenntnisdatum berechnen |
| Hauptanspruch | Hier kein klassischer Anspruch: Tatvorwurf benennen (Norm + StGB- bzw. Nebenstrafrechts-§). Mitwirkung: Akteneinsicht § 147 StPO, Beweisantrag § 244 StPO, Verteidigerwahl § 137 StPO, Pflichtverteidigung § 140 StPO. | Sachverhaltsabgleich mit Tatbestandsmerkmalen |
| Zuständigkeit | AG Strafrichter / Schöffengericht (§§ 24 ff. GVG), LG große Strafkammer (§ 74 GVG), OLG (Staatsschutz, § 120 GVG). Bei Jugendlichen: JGG-Spruchkörper. | Gesetz, Vertrag, Gerichtsstandsklausel |

## Risiko-Ampel

- **Frist:** 🔴 Sofortige Beschwerde (1 Woche), Revisionsfrist (1 Woche / 1 Monat) tickt ab Verkündung/Zustellung. 🟠 Hauptverhandlung in 30 Tagen — Beweisanträge vorbereiten.
- **Beweislage:** 🟠 Beschuldigtenaussage NIE ohne Akteneinsicht. 🔴 Belastungszeugen: Konfrontationsrecht Art. 6 III d EMRK ausnutzen. 🟢 Selbstanzeige § 371 AO nur nach umfassender Aktenlage.
- **Wirtschaftlich:** 🔴 Berufstauglichkeit gefährdet (Beamte, Heilberufe, Approbation): parallel berufsrechtliche Schiene mitdenken. 🟠 Vermögensabschöpfung §§ 73 ff. StGB im Blick.

## Anschluss-Skills (Router)

| Wenn der Fall trägt … | dann Skill | Erwartung |
| --- | --- | --- |
| **Untersuchungshaft / Haftbefehl** | `strafr-haftpruefung-haftbeschwerde-workflow` | Haftbeschwerde § 304 StPO, Haftprüfung § 117 StPO, mündliche Verhandlung erzwingen |
| Akteneinsicht & Strategie | `akteneinsicht-beantragen` | Antrag § 147 StPO, Wahl Verfahrensschiene, ggf. Schweigen / Einlassungsmemo |
| Beweisantrag vorbereiten | `strafr-dysfunk-beweisantrag-fundament` | Substantiierte Tatsachenbehauptung, Beweismittel, Konnexität |
| Revision prüfen | `revisionsbegruendung-paragraf-344-stpo` | Sach- vs. Verfahrensrüge, absolute Revisionsgründe § 338 StPO |
| Wirtschafts-/Vermögensabschöpfung | `strafr-vermoegensabschoepfung-spezial` | Einziehung §§ 73 ff. StGB, vermögenssichernde Maßnahmen § 111b StPO |

## Norm-Radar (live verifizieren)

- **§ 147 StPO** — Akteneinsicht des Verteidigers
- **§ 137 StPO** — Recht auf Verteidiger jederzeit
- **§ 244 StPO** — Beweisantragsrecht
- **§ 117 StPO** — Haftprüfung
- **§ 341 StPO** — Revisions-Einlegungsfrist (1 Woche)
- **§ 73 StGB** — Einziehung von Taterträgen

## Genau eine Rückfrage (nur wenn nötig)

> Welche **Verfahrensphase** läuft (Ermittlung · Anklage · Hauptverhandlung · Rechtsmittel · Vollstreckung), und sitzt der Mandant **in Haft**?

Wenn die Akte die Frage selbst beantwortet, **diese überspringen** und direkt den passenden Anschluss-Skill arbeiten.

## Leitentscheidungs-Anker (Such-Wegweiser, keine fertigen Zitate)

- **Verständigung § 257c StPO; Mitteilungspflichten** — BVerfG 2. Senat; BGH-Strafsenate — *live verifizieren auf* `bundesverfassungsgericht.de + bundesgerichtshof.de`
- **Beweisantragsrecht § 244 StPO; Konnexität** — BGH-Strafsenate — *live verifizieren auf* `bundesgerichtshof.de`
- **Faires Verfahren / Konfrontationsrecht Art. 6 III d EMRK** — EGMR — *live verifizieren auf* `hudoc.echr.coe.int`
- **Einziehung §§ 73 ff. StGB; verfassungsrechtliche Grenzen** — BVerfG / BGH-Strafsenate — *live verifizieren auf* `bundesverfassungsgericht.de + bundesgerichtshof.de`

> Diese Anker sind Sucheinstieg. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle prüfen und Datum, Aktenzeichen, Randnummer abklären. Kuratierte Anker-Sammlung in `references/leitentscheidungen-anker.md`.

## Hinweis

Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Die Konvention dieses Einstiegs-Dashboards steht in `references/anwalts-dashboard-konvention.md`.

---

## Skill: `mandat-triage-strafrecht`

_Wenn es um Strukturierte Eingangs-Abfrage für Strafmandate in Fachanwalt Strafrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Strukturierte Eingangs-Abfrage für Strafmandate


## Direktstart: lesen, entscheiden, liefern

Beginne nicht mit einem Fragenkatalog. Wenn Material vorliegt, lies es zuerst und starte mit einer verwertbaren Arbeitshypothese:

- Frist oder Sofortrisiko.
- erkannte Rolle, Zielrichtung und Verfahrensstand.
- tragende Tatsachen aus dem Material.
- bester nächster Arbeitsschritt mit direkt nutzbarem Output.

Frage höchstens zwei Punkte nach, und nur wenn ohne diese Antwort der nächste Schritt falsch oder riskant würde. Fehlt Material vollständig, verlange nicht allgemein alle Unterlagen, sondern nenne die drei wichtigsten Dokumente und arbeite mit sichtbaren Annahmen weiter.

Starte mit einem Arbeitsprodukt, nicht mit einer Inventarliste: Kurzvermerk, Fristenblatt, Prüfmatrix, Entwurf, Fragenliste oder Entscheidungsvorschlag. Routing ist nur Mittel zum Zweck. Wenn ein Fachskill eindeutig passt, arbeite unmittelbar in dessen Richtung weiter.

Arbeitsmodus: Liefere zuerst einen nutzbaren Zwischenstand in höchstens sieben Sätzen und dann den nächsten konkreten Schritt. Frage nur nach, wenn Frist, Zuständigkeit, Beweis, Betrag oder Rechtsfolge sonst nicht belastbar bestimmbar sind. Tabellen nur für Fristen, Belege, Beträge, Varianten oder Streitstoff.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StPO; StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Strukturierte Eingangs-Abfrage für Strafmandate. Klaert Verfahrensstadium (Ermittlungs- Zwischen- Hauptverfahren Vollstreckung) Tatvorwurf nach Strafrahmen (Vergehen Verbrechen) Haftsituation (Untersuchungshaft Vollzug Hausverbot) Beschuldigtenrechte § 136 § 137 § 140 § 141 StPO Pflichtverteidiger-Bestellung Mitbeschuldigte (Konflikt-Check § 43a BRAO § 146 StPO). Sofort-Fristen-Check Haftprüfung § 117 StPO, Haftbeschwerde § 304 StPO, Akteneinsicht § 147 StPO, Rechtsmittel und U-Haft-Eskalation. Routing zu Akteneinsicht, Haftmanagement und Strafprozess-Cockpit.

### Mandat-Triage Strafrecht

## Ablauf — acht Fragen

### Frage 1 — Wer ruft an und für wen?

- Beschuldigter selbst
- Angehöriger
- Polizei (selten — Notdienst)
- Anderer Anwalt (Vertretung)

### Frage 2 — Akute Eilbedürftigkeit?

- Festnahme erfolgt — Vorführung läuft heute
- Untersuchungshaft seit Stunden / Tagen
- Durchsuchung läuft / steht bevor
- Aussage bei Polizei für heute terminiert
- Hauptverhandlung beginnt morgen

**Eskalation:** Festnahme U-Haft Durchsuchung → Telefon-Sofort an Anwalt; binnen einer Stunde Beistand; Anwesenheit bei Vernehmung Pflicht.

### Frage 3 — Verfahrensstadium?

- Ermittlungsverfahren bei Polizei (kein Aktenzeichen StA noch nicht)
- Ermittlungsverfahren bei Staatsanwaltschaft (Az StA vorhanden)
- Zwischenverfahren (Anklage zugestellt — Eröffnungsbeschluss?)
- Hauptverfahren (Hauptverhandlungstermin)
- Berufung / Revision
- Strafvollstreckung
- Strafvollzug (Vollzugsplan Lockerungen Strafaussetzung)

### Frage 4 — Tatvorwurf?

- Norm (§ ggf. StGB Nebengesetz)
- Strafrahmen — Vergehen unter ein Jahr Vergehen ab ein Jahr Verbrechen ab ein Jahr Mindeststrafe (§ 12 StGB)
- Bei Verbrechen oder Strafrahmen ab ein Jahr — notwendige Verteidigung § 140 StPO

### Frage 5 — Haftsituation?

- In Freiheit
- Vorgeführt — Vorführungsbeschluss / Haftbefehl?
- Untersuchungshaft — Haftgründe (Flucht-, Verdunkelungs-, Wiederholungs-)
- Strafvollzug

### Frage 6 — Mitbeschuldigte?

- Wer ist mitbeschuldigt?
- Ist Mitbeschuldigter bereits anwaltlich vertreten?
- Konflikt-Check § 43a Abs. 4 BRAO § 146 StPO Mehrfachverteidigung verboten

### Frage 7 — Aktenstand?

- Aktenstand nachgefragt?
- Akteneinsicht beantragt § 147 StPO
- Bei U-Haft haftrelevante Informationen nach § 147 Abs. 2 S. 2 StPO sichern; in der Regel Akteneinsicht

### Frage 8 — Wirtschaftliche Verhältnisse / Pflichtverteidigung?

- Pflichtverteidigung § 140 § 141 StPO bei notwendiger Verteidigung
- Vergütung nach RVG plus eventuell Honorarvereinbarung

## Routing-Matrix

| Verfahrensstadium | Folge-Skill | Frist-Sofort-Check |
|---|---|---|
| U-Haft | `strafprozess-haft-und-besuchsmanagement` | Haftprüfung § 117 StPO, Haftbeschwerde § 304 StPO, Sechs-Monats-Kontrolle § 121 StPO |
| Vorfeld Durchsuchung | Beschwerde § 304 StPO | ggf. nicht statthaft wenn beendet — Feststellungsantrag |
| Polizei-Vernehmung steht an | Verteidigerbeistand § 168c StPO | Termin verlegen oder begleiten |
| Anklage zugestellt | Stellungnahme zur Eröffnung | Frist nach § 201 StPO |
| Anzeige/Anklage § 188 StGB | `strafrecht-spezial-188-stgb-easy-verteidigung` | Strafantrag/besonderes öffentliches Interesse § 194 StGB, vollständiger Äußerungskontext, Art. 5 GG |
| Strafbefehl § 188 StGB | `strafrecht-spezial-188-stgb-anklage-und-strafbefehl` | Einspruch § 410 StPO binnen zwei Wochen ab Zustellung |
| Hauptverhandlung | `akteneinsicht-strafrecht-auswerten` | Beweisanträge vor Schluss Beweisaufnahme |
| Berufung/Revision | `strafprozess-rechtsmittel-und-notfristencockpit` | Berufung/Revision Einlegung binnen 1 Woche; Revisionsbegründung § 345 StPO gesondert berechnen |

## Konflikt-Check

- Mehrfachverteidigung verboten § 146 StPO
- § 43a Abs. 4 BRAO Interessenkollision
- Frühere Vertretung von Mitbeschuldigtem oder Geschädigtem prüfen

## Sofort-Fristen

- **Haftprüfung** § 117 Abs. 1 StPO — jederzeit
- **Haftbeschwerde** § 304 StPO — keine gesetzliche Wochenfrist wie bei sofortiger Beschwerde, aber praktisch sofort vorbereiten
- **Sechs-Monats-Prüfung** OLG § 121 StPO
- **Einspruch Strafbefehl** § 410 StPO zwei Wochen
- **Berufung** § 314 StPO eine Woche
- **Revision** § 341 StPO eine Woche; Revisionsbegründung § 345 StPO grundsätzlich ein Monat nach Ablauf der Einlegungsfrist, bei späterer Urteilszustellung ab Zustellung

## Eskalationspfad

- **Telefon-Sofort** Vorführung Untersuchungshaft Durchsuchung Vernehmung-Termin heute
- **Binnen einer Stunde** Anfahrt zur Vernehmung — Verteidigerbeistand
- **Heute** Akteneinsichtsantrag § 147 StPO, Haftprüfung § 117 StPO oder Haftbeschwerde § 304 StPO prüfen
- **Diese Woche** Stellungnahme Anklage Berufungseinlegung

## Ausgabe

- `triage-protokoll-strafrecht.md` mit acht Fragen
- Aktenanlage Az-Vorschlag
- Fristenbuch-Eintrag (Hauptfrist Vorfrist)
- Mandatsvereinbarung Vorlage mit Pflichtverteidigerbestellungs-Antrag falls notwendig
- Empfehlung Folge-Skill plus Begründung

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Quellen

- StPO §§ 117 121 137 140 141 146 147 168c 201 304 314 341 410
- StGB § 12 (Verbrechen-Vergehen)
- BRAO § 43a
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Aktuelle Rechtsprechung Mandat-Triage

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Normen Triage-Check

- § 112 StPO — Haftbefehl (Flucht-, Verdunkelungs-, Wiederholungsgefahr)
- § 117 StPO — Haftpruefungsantrag (jederzeit)
- § 118a StPO — Haftpruefungstermin mit muendlicher Verhandlung
- § 140 StPO — notwendige Verteidigung (Bestellungsgrunde)
- § 141 StPO — Pflichtverteidiger-Bestellung (Zeitpunkt, Ablauf)
- § 146 StPO — Verbot Mehrfachverteidigung
- §§ 10 ff. GwG — Identifizierungspflichten Sorgfaltspflichten Rechtsanwalt

---

## Skill: `fachanwalt-strafrecht-orientierung`

_Wenn es um Fachanwalt für Strafrecht — Orientierung in Fachanwalt Strafrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen._

# Fachanwalt für Strafrecht — Orientierung

## FAO-Voraussetzungen

- **Theoretischer Lehrgang** 120 Stunden.
- **Drei Klausuren** zum Strafrecht.
- **60 Fälle** in den letzten drei Jahren, davon mindestens 40 Hauptverhandlungen mit eigener Beteiligung.
- Anmeldung bei der Rechtsanwaltskammer.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| StGB Allgemeiner Teil | §§ 1 ff. StGB |
| StGB Besonderer Teil | §§ 80 ff. StGB |
| Strafverfahren | StPO §§ 1 ff. |
| Strafvollstreckung | StVollstrO StVollzG |
| Nebenstrafrecht | BtMG WaffG AO § 370 (Steuerhinterziehung) |
| Strafrecht Wirtschaft | §§ 263 263a 266 299 StGB GwG |
| Jugendstrafrecht | JGG |
| Beruf Strafverteidiger | § 137 StPO § 138 StPO § 142 StPO Pflichtverteidigung § 140 StPO |

## Typische Mandate

- Ermittlungsverfahren Erstvernehmung
- Untersuchungshaft (§§ 112 ff. StPO Haftprüfungsantrag § 117 StPO Haftbeschwerde § 304 StPO)
- Hauptverhandlung Strafrichter Schöffengericht Schwurgericht
- Verteidigung in Wirtschaftsstrafsachen (Wirtschaftsstrafkammer Landgericht)
- Berufung Revision Verfassungsbeschwerde
- Strafvollstreckung Bewährung Reststrafenaussetzung

## Notfristen

- **Berufung** § 314 StPO — **eine Woche** Notfrist.
- **Revision** § 341 StPO — **eine Woche** Notfrist.
- **Revisionsbegründung** § 345 StPO — **ein Monat**.
- **Beschwerde** § 311 StPO — **eine Woche**.
- **Verfassungsbeschwerde** § 93 BVerfGG — **ein Monat**.
- **Wiedereinsetzung** § 44 StPO — eine Woche.

## Hauptgerichte

- **Amtsgericht** Strafrichter § 25 GVG (Vergehen Privatklage oder keine höhere Strafe als zwei Jahre zu erwarten) Schöffengericht § 28 GVG (bis vier Jahre Straferwartung).
- **Landgericht** Große Strafkammer Wirtschaftsstrafkammer Schwurgericht.
- **OLG** Berufungs- und Revisionsinstanz; Anklage erstinstanzlich bei Staatsschutzdelikten.
- **BGH 1.–5. Strafsenat** Revisionsinstanz.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Berufsverband

- Deutscher Strafverteidiger e. V. (DSV).
- Vereinigung Berliner Strafverteidiger.
- Strafverteidigervereinigung Niedersachsen / NRW / Bayern.

## Schnittstellen

- **aktenaufbereiter-strafrecht** für Aktenaufbereitung.
- **kanzlei-allgemein** für Fristenbuch und Versand.

## Hinweis

Plugin fuer Fachanwaltschaft-Orientierung. Tiefe Verteidigung erfordert die Erfahrung des Fachanwalts; insbesondere bei Schwurgerichts- und Wirtschaftsstrafrecht.

## Zentrale Strafrecht-Normen im Ueberblick

- §§ 1-2 StGB — Gesetzlichkeitsprinzip; keine Strafe ohne Gesetz (nullum crimen)
- §§ 13-16 StGB — Begehungs-/Unterlassungsdelikt, Vorsatz, Irrtum
- §§ 20-21 StGB — Schuldunfaehigkeit, verminderte Schuldfaehigkeit
- §§ 46-49 StGB — Strafzumessung, besonderer Milderungsgrund
- § 78 StGB — Verjaehrungsfristen (z.B. 30 Jahre bei Mord)
- §§ 112-130 StPO — Untersuchungshaft, Haftbefehl, Haftgruende, Haftpruefung
- §§ 136-136a StPO — Beschuldigtenbelehrung, Aussageverweigerungsrecht, Beweisverwertungsverbote
- §§ 140-142 StPO — notwendige Verteidigung, Pflichtverteidiger

## Aktuelle Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

---

## Skill: `orientierung-fristen-form-und-zustaendigkeit`

_Wenn es um Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg in Fachanwalt Strafrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StPO; StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg.

## Spezialwissen: Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg
- **Normen-/Quellenanker:** StPO.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Orientierung** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Strafrecht-Orientierung Fristen / Form / Zuständigkeit Bausteine
- **Sachliche Zuständigkeit GVG:**
 - **Strafrichter § 25 GVG:** Privatklagen § 374 StPO; allgemein bis Freiheitsstrafe 2 Jahre, sofern nicht hoeher beantragt.
 - **Schoeffengericht § 28 GVG:** bis Freiheitsstrafe 4 Jahre; alle Strafsachen, die nicht zu hoher Strafkammer oder Strafrichter gehoeren.
 - **Große Strafkammer § 76 GVG:** alle Strafsachen ab 4 Jahre erwarteter Freiheitsstrafe; bestimmte Wirtschaftsstrafsachen.
 - **Schwurgericht § 74 II GVG:** Toetungsdelikte §§ 211 ff. StGB, Eingriff in Verkehr mit Todesfolge.
 - **Oberlandesgericht § 120 GVG:** Staatsschutzdelikte (Hochverrat, Landesverrat, Terror).
- **Oertliche Zuständigkeit StPO:**
 - **§ 7 StPO:** Tatort - regelmaessig massgeblich.
 - **§ 8 StPO:** Wohnsitz Beschuldigter.
 - **§ 9 StPO:** Ergreifungsort.
 - **§ 13 StPO:** Verbundene Verfahren.
- **Fristen-Übersicht (StPO):**
 - **Einspruch Strafbefehl § 410 StPO: 2 Wochen** ab Zustellung.
 - **Berufung § 314 StPO: 1 Woche** ab Verkuendung; Begruendung optional.
 - **Revision § 341 StPO: 1 Woche** Einlegung + § 345 StPO **1 Monat** Begruendung ab Zustellung schriftliche Urteilsausfertigung.
 - **Beschwerde § 311 StPO: 1 Woche** sofortige; § 304 StPO einfache unbefristet.
 - **Wiedereinsetzung § 44 StPO: 1 Woche** ab Wegfall des Hindernisses.
 - **Klageerzwingungsverfahren § 172 II StPO: Antrag 1 Monat** ab Bescheid GenStA.
- **Form-Re-Check:**
 - **Schriftform** zwingend für Rechtsmittel (Berufung, Revision, Beschwerde) und Einspruch.
 - **Unterschrift** Verteidiger / Mandant.
 - **Vollmacht** bei Vertretung.
 - **Begruendungs-Pflicht** Revision (Sach- oder Verfahrensruege; § 344 II StPO Substantiierung Verfahrensruege).
- **Rechtsweg:**
 - AG -> LG (Berufung § 312 StPO) -> OLG (Revision § 333 StPO bei LG-Urteil 1. Instanz oder Berufungsurteil).
 - **Sprungrevision § 335 StPO** möglich (Sprung Berufung).
 - **Wiederaufnahme § 359 StPO** bei neuen Tatsachen / Beweismitteln.
- **EMRK Art. 6:** angemessene Verfahrensdauer als Korrektiv (Strafmilderung BGH-Linie).

---

## Skill: `orientierung-mandat-fachanwaltschaft`

_Wenn es um Orientierung Mandat Fachanwaltschaft in Fachanwalt Strafrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Orientierung im Strafrecht-Mandat und Fallrouting: Anwendungsfall Strafverteidiger erhaelt neue Anfrage und muss Strafrechts-Konstellation einordnen und passendes Fachmodul finden


## Arbeitsbereich

**Orientierung** ordnet den Fall über die tragenden Prüfungslinien: Orientierung im Strafrecht-Mandat und Fallrouting, Untersuchungshaft und Haftprüfung nach §§ 112 ff, Verständigung § 257c StPO und Taeter-Opfer-Ausgleich § 46a. Arbeite zuerst die tragende Rechtsfrage heraus; Nebenaspekte werden nur verarbeitet, soweit sie Frist, Zuständigkeit, Beweislast oder das konkrete Arbeitsprodukt tatsächlich beeinflussen.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StPO; StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Orientierung im Strafrecht-Mandat und Fallrouting: Anwendungsfall Strafverteidiger erhaelt neue Anfrage und muss Strafrechts-Konstellation einordnen und passendes Fachmodul finden. § 136 StPO Belehrung, § 137 StPO Verteidigerrecht, StGB Straftatbestaende. Prüfraster Deliktstyp allgemeines oder Wirtschaftsstrafrecht, Verfahrensstand Ermittlung Anklage Hauptverhandlung, Mandantenrolle Beschuldigter Zeuge Nebenklaeger. Output Mandat-Einordnung mit Weiterleitung zur richtigen Prüfungslinie. Abgrenzung zu Mandat-Triage-Strafrecht für ausführliche Erstaufnahme.

### Fachanwalt für Strafrecht — Orientierung

## FAO-Voraussetzungen

- **Theoretischer Lehrgang** 120 Stunden.
- **Drei Klausuren** zum Strafrecht.
- **60 Fälle** in den letzten drei Jahren, davon mindestens 40 Hauptverhandlungen mit eigener Beteiligung.
- Anmeldung bei der Rechtsanwaltskammer.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| StGB Allgemeiner Teil | §§ 1 ff. StGB |
| StGB Besonderer Teil | §§ 80 ff. StGB |
| Strafverfahren | StPO §§ 1 ff. |
| Strafvollstreckung | StVollstrO StVollzG |
| Nebenstrafrecht | BtMG WaffG AO § 370 (Steuerhinterziehung) |
| Strafrecht Wirtschaft | §§ 263 263a 266 299 StGB GwG |
| Jugendstrafrecht | JGG |
| Beruf Strafverteidiger | § 137 StPO § 138 StPO § 142 StPO Pflichtverteidigung § 140 StPO |

## Typische Mandate

- Ermittlungsverfahren Erstvernehmung
- Untersuchungshaft (§§ 112 ff. StPO Haftprüfungsantrag § 117 StPO Haftbeschwerde § 304 StPO)
- Hauptverhandlung Strafrichter Schöffengericht Schwurgericht
- Verteidigung in Wirtschaftsstrafsachen (Wirtschaftsstrafkammer Landgericht)
- Berufung Revision Verfassungsbeschwerde
- Strafvollstreckung Bewährung Reststrafenaussetzung

## Notfristen

- **Berufung** § 314 StPO — **eine Woche** Notfrist.
- **Revision** § 341 StPO — **eine Woche** Notfrist.
- **Revisionsbegründung** § 345 StPO — **ein Monat**.
- **Beschwerde** § 311 StPO — **eine Woche**.
- **Verfassungsbeschwerde** § 93 BVerfGG — **ein Monat**.
- **Wiedereinsetzung** § 44 StPO — eine Woche.

## Hauptgerichte

- **Amtsgericht** Strafrichter § 25 GVG (Vergehen Privatklage oder keine höhere Strafe als zwei Jahre zu erwarten) Schöffengericht § 28 GVG (bis vier Jahre Straferwartung).
- **Landgericht** Große Strafkammer Wirtschaftsstrafkammer Schwurgericht.
- **OLG** Berufungs- und Revisionsinstanz; Anklage erstinstanzlich bei Staatsschutzdelikten.
- **BGH 1.–5. Strafsenat** Revisionsinstanz.

## Berufsverband

- Deutscher Strafverteidiger e. V. (DSV).
- Vereinigung Berliner Strafverteidiger.
- Strafverteidigervereinigung Niedersachsen / NRW / Bayern.

## Schnittstellen

- **aktenaufbereiter-strafrecht** für Aktenaufbereitung.
- **kanzlei-allgemein** für Fristenbuch und Versand.

## Hinweis

Plugin für Fachanwaltschaft-Orientierung. Tiefe Verteidigung erfordert die Erfahrung des Fachanwalts; insbesondere bei Schwurgerichts- und Wirtschaftsstrafrecht.

## Zentrale Strafrecht-Normen im Überblick

- §§ 1-2 StGB — Gesetzlichkeitsprinzip; keine Strafe ohne Gesetz (nullum crimen)
- §§ 13-16 StGB — Begehungs-/Unterlassungsdelikt, Vorsatz, Irrtum
- §§ 20-21 StGB — Schuldunfaehigkeit, verminderte Schuldfaehigkeit
- §§ 46-49 StGB — Strafzumessung, besonderer Milderungsgrund
- § 78 StGB — Verjährungsfristen (z.B. 30 Jahre bei Mord)
- §§ 112-130 StPO — Untersuchungshaft, Haftbefehl, Haftgruende, Haftpruefung
- §§ 136-136a StPO — Beschuldigtenbelehrung, Aussageverweigerungsrecht, Beweisverwertungsverbote
- §§ 140-142 StPO — notwendige Verteidigung, Pflichtverteidiger

## Aktuelle Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Skill: `erstgespraech-mandatsannahme`

_Wenn es um Erstgespraech Mandatsannahme in Fachanwalt Strafrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Erstgespraeach und Mandatsannahme im Strafrecht: Anwendungsfall Beschuldigter oder Verdaechtiger meldet sich nach Polizeivorladung oder Festnahme und Strafverteidiger muss Mandat strukturiert aufnehmen


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StPO; StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Erstgespraeach und Mandatsannahme im Strafrecht: Anwendungsfall Beschuldigter oder Verdaechtiger meldet sich nach Polizeivorladung oder Festnahme und Strafverteidiger muss Mandat strukturiert aufnehmen. § 136 StPO Belehrung Schweigerecht, § 137 StPO Verteidigerrecht, § 147 StPO Akteneinsicht. Prüfraster Konflikt-Check, Schweigerecht kommunizieren, Sachverhalt aufnehmen, Akteneinsicht beantragen, Honorarvereinbarung treffen. Output Mandats-Aufnahmeprotokoll mit Sofortmassnahmen-Liste und Belehrungsprotokoll. Abgrenzung zu Wahlverteidiger-Mandat für spezifischen Mandatstyp und zu Mandat-Triage.

### Erstgespraech und Mandatsannahme im Allgemeines und Wirtschaftsstrafrecht

## Wann dieser Arbeitsgang greift

- Neue Anfrage aus dem Bereich Allgemeines und Wirtschaftsstrafrecht (Telefon, Mail, Empfehlung, Walk-in).
- Mandantin oder Mandant beschreibt Sachverhalt unstrukturiert; oft mit Vorladung, Strafbefehl, Durchsuchungsbeschluss, Anklageschrift, U-Haft-Anordnung, Anhörung als Zeuge oder Anklageschrift mit Nebenklage-Option.
- Vor jeder weiteren Bearbeitung: erst Annahme klären, Rolle bestimmen (Beschuldigte/r, Verletzte/r oder Nebenklage, Zeuge/in mit Beistand), Konflikt- und GwG-Prüfung, Vollmacht, Gebührenvereinbarung, Fristen.

## Phasen des Erstgespraechs

### 1. Rollenklarheit und Konstellation (10-15 Min.)

Erste Frage: Wofür braucht Mandantschaft Sie?

- **Beschuldigte oder Angeklagte** - Verteidigung im Strafverfahren.
- **Verletzte oder Anzeigeerstattende** - Beratung, Strafanzeige, Akteneinsicht der Verletzten, ggf. Nebenklage-Anschluss.
- **Zeuginnen oder Zeugen** - Zeugenbeistand gemäß § 68b StPO, Auskunftsverweigerungsrecht gemäß § 55 StPO.
- **Insolvenzverwalter/Geschäftsführung** mit StA-Berlin-Beruehrung - paralleles Insolvenz-/Strafverfahren.

Standard-Fragenraster:

- Beteiligte (Vor-/Nachname, Geburtsdatum, Anschrift, Rolle und Aktenzeichen StA / Gericht).
- Tatvorwurf in einem Satz (StGB-Paragraf, OWiG, Nebenstrafrecht).
- Konkrete fachliche Stossrichtung: Akteneinsicht, Beschuldigtenvernehmung, U-Haft, Strafbefehl-Einspruch, Hauptverhandlung, Revision, Anklage gegen Beschuldigte/n als Nebenklage.
- Bisherige Korrespondenz (Vorladung, Anhörungsbogen, Durchsuchung, Bescheide).
- **Fristenscreening sofort:** Einspruch gegen Strafbefehl 2 Wochen (§ 410 Abs. 1 StPO), Revisionseinlegung 1 Woche (§ 341 StPO), Revisionsbegruendung 1 Monat (§ 345 StPO), Klageerzwingung 1 Monat (§ 172 Abs. 2 StPO), Antrag auf gerichtliche Entscheidung (§ 23 EGGVG) 1 Monat, Beschwerdefristen § 311 StPO.

### 2. Konflikt-Prüfung und GwG-Check (5 Min.)

- Konflikt-Check über Mandantsystem: Mit-Beschuldigte, Verletzte, frueheres Mandat?
- Bei Mehrfach-Beschuldigten zwingend pro Person eigene Verteidigung (§ 146 StPO).
- GwG-Identifizierung: amtlicher Lichtbildausweis, bei juristischer Person Handelsregister-/Transparenzregister-Auszug, ggf. wirtschaftlich Berechtigte/n.
- Risikobewertung (niedrig/mittel/hoch) abhaengig von Auslandsbezug, Vermögensherkunft, Tatvorwurf (insbesondere § 261 StGB Geldwaesche, § 370 AO Steuerhinterziehung).
- Doku im Mandatsbogen (Pflicht nach §§ 10 ff. GwG, BRAK-Identifizierungsleitfaden).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### 3. Vollmacht und Akteneinsicht

- Strafprozessvollmacht (§§ 137 ff. StPO, BORA, RVG).
- Akteneinsichtsantrag gemäß § 147 StPO (Verteidigung) oder § 406e StPO (Verletzten-/Nebenklagevertretung) oder ohne Sondervorschrift für Zeugenbeistand.
- Bei Pflichtverteidigerbestellung Antrag gemäß § 141 StPO frueh stellen (Belehrung gemäß § 136 Abs. 1 S. 3 StPO).
- Bei Nebenklage: Anschlusserklaerung gemäß § 396 StPO und Prüfung der Nebenklage-Befugnis gemäß § 395 StPO.

### 4. Gebührenvereinbarung im Strafverfahren

Strafrechtsspezifische Gebührentatbestaende statt zivilrechtlicher Streitwert-Logik:

- **RVG-Strafsachen-Tatbestaende** (VV-RVG Teil 4 Abschnitt 1): Grundgebuehr Nr. 4100, Verfahrensgebuehr Ermittlungsverfahren Nr. 4104, Verfahrensgebuehr Gerichtsverfahren erster Instanz Nr. 4106 oder 4112 bzw. 4118 je nach Gericht, Terminsgebuehr Nr. 4108 bzw. Nr. 4114 bzw. Nr. 4120, Hauptverhandlungstag-Zuschlag bei Strafkammer.
- **Bei Bussgeldverfahren:** VV-RVG Teil 5 (Nrn. 5100 ff.).
- **Pflichtverteidigung:** Festgebuehren gemäß RVG-Tabelle Teil 4 Abschnitt 1 mit besonderem Gebührentatbestand für den bestellten Verteidiger.
- **Vereinbarungshonorar / Stundenhonorar:** zulässig nach § 3a RVG mit Schriftform und ausdruecklichem Hinweis; oberhalb der gesetzlichen Gebuehr ueblich bei Wirtschaftsstrafrecht.
- **Erfolgshonorar:** nur in engen Grenzen gemäß § 4a RVG; im Strafverfahren regelmaessig problematisch (kein Erfolg im klassischen Sinne, Risiko des Wertungs-Widerspruchs).
- **Vorschuss:** Vorschussanforderung nach § 9 RVG, in Strafsachen ueblich pro Instanz oder pro Hauptverhandlungstag.
- **Bei Nebenklage:** Gebühren VV-RVG Teil 4 Abschnitt 2 (Nrn. 4124 ff.). Streitwert-Äquivalent nur für adhaesionsrechtliche Anspruche relevant.
- **Bei Adhaesion (§§ 403 ff. StPO):** Gebühren VV-RVG Teil 4 Abschnitt 6 (Nrn. 4143-4147), berechnet nach Gegenstandswert des geltend gemachten Anspruchs.

### 5. Strategie-Erstskizze

Drei Weichen am Ende des Erstgespraechs:

- **Mandat annehmen:** vollstaendig (Verteidigung durch alle Instanzen) oder begrenzt (nur Akteneinsicht und Gutachten, nur Erstellung Einspruch gegen Strafbefehl, nur Zeugenbeistand für einen Vernehmungstermin).
- **Verweisen:** wenn Spezialgebiet ausserhalb (Wirtschaftsstrafrecht vs. allgemeines Strafrecht), oertlich unzuständig oder Mehrfachbeschuldigtenkonstellation.
- **Ablehnen:** Konflikt mit § 146 StPO, GwG-Hit beim Honorar, fehlende Vertrauensbasis.

## Pflicht-Output am Ende

1. **Mandatsbogen** mit Beteiligten, Rolle, Konflikt-Check, GwG-Status, Tatvorwurf, Aktenzeichen.
2. **Frist-Liste** (Einspruch, Revisionseinlegung, Revisionsbegruendung, Beschwerdefristen, Anschluss-Frist Nebenklage, U-Haft-Prüfungsfristen § 121 StPO).
3. **Anlagenverzeichnis** des uebergebenen Datenraums (Bescheide, Schreiben, Anhörungsbogen).
4. **Naechster-Schritt-Plan:** binnen 24 / 48 / 72 h, Owner, Output (Akteneinsicht stellen, Pflichtverteidigerbeiordnung beantragen, U-Haft-Beschwerde).
5. **Honorarvereinbarung** unterschrieben oder Hinweis auf RVG-Festgebuehr / Pflichtverteidiger-Beiordnung.

## Relevante Rechtsgrundlagen und Standards

- BORA, BRAO, FAO Strafrecht (§ 13 FAO).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- StGB, StPO, BtMG, AO (§§ 369 ff.), OWiG, JGG, Nebenstrafrecht (StVG, WaffG, KCanG, AWG, WiStrG 1954).
- RVG mit VV-RVG Teil 4 (Strafsachen) und Teil 5 (Bussgeldsachen).
- DSGVO und BDSG für den Umgang mit Mandanten- und Verletzten-Daten.

## Typische Fehler im Erstgespraech

- Rolle der Mandantschaft nicht klar getrennt - Mehrfachvertretung Beschuldigter und Nebenklaegerin im gleichen Verfahren ist berufsrechtswidrig.
- Frist uebersehen, weil Mandantschaft sie nicht selber genannt hat (immer aus jedem Schreiben Frist herausziehen, insbesondere Strafbefehl mit Zustellungsdatum).
- Pflichtverteidiger-Antrag erst spaet gestellt - Vergutungsrisiko für Wahlverteidiger bis Beiordnung.
- Akteneinsicht zu spaet beantragt - Hauptverhandlungsvorbereitung leidet.
- Honorarvereinbarung muendlich oder ohne § 3a-RVG-Form - Honorar nur in Höhe der gesetzlichen Gebuehr durchsetzbar.
- GwG-Prüfung verfehlt - Risiko § 261 StGB beim Honorar-Bezug aus inkriminierter Quelle.

## Praxis-Checkliste

- [ ] Rolle der Mandantschaft eindeutig festgestellt
- [ ] Personalien und Aktenzeichen aller Beteiligten erfasst
- [ ] Konflikt-Check durchgefuehrt (auch Mit-Beschuldigte gemäß § 146 StPO)
- [ ] GwG: Identifizierung + Risikobewertung notiert
- [ ] Strafprozessvollmacht unterschrieben
- [ ] Akteneinsicht beantragt (§ 147 oder § 406e StPO)
- [ ] Pflichtverteidigerbestellung beantragt, soweit Voraussetzungen vorliegen (§ 140 StPO)
- [ ] Honorarvereinbarung schriftlich (§ 3a RVG) oder Hinweis auf RVG-Festgebuehr
- [ ] Fristenliste angelegt und in Kalender eingetragen
- [ ] Mandatsbogen vollstaendig
- [ ] Naechster-Schritt-Plan kommuniziert (E-Mail-Zusammenfassung)

## Konkrete Praxis-Konstellationen

### Konstellation A: Strafbefehl mit Einspruchsfrist

Mandantschaft bringt Strafbefehl am Donnerstag, Einspruchsfrist 2 Wochen ab Zustellung. Handlungs-Sequenz:

1. Zustellungsdatum aus Strafbefehl auslesen (Zustellungsurkunde, EB).
2. Akteneinsicht (§ 147 StPO) sofort schicken.
3. Einspruch fristwahrend einlegen, Begruendung nachreichen.
4. Wiedereinsetzung in den vorigen Stand (§§ 44 ff. StPO) als Reserve dokumentieren.

### Konstellation B: U-Haft

Mandantschaft sitzt seit Wochen in U-Haft. Pflichtverteidiger noch nicht beantragt.

1. Pflichtverteidigerbestellung beantragen (§ 140 Abs. 1 Nr. 4 StPO).
2. Akteneinsicht beantragen, soweit § 147 Abs. 2 StPO nicht entgegensteht.
3. Haftpruefung (§ 117 StPO) oder Haftbeschwerde (§ 304 StPO).
4. Mandantengespraech in der JVA terminieren (Sprecherlaubnis).

### Konstellation C: Verletzte/r mit Nebenklage-Option

Mandantschaft ist Opfer einer Sexualstraftat oder schweren Koerperverletzung.

1. Akteneinsichtsantrag für Verletztenvertretung (§ 406e StPO).
2. Prüfung Nebenklagebefugnis (§ 395 StPO).
3. Antrag auf Beiordnung als Opferanwalt (§ 397a StPO).
4. Adhaesion (§§ 403 ff. StPO) und psychosoziale Prozessbegleitung (§ 406g StPO) erwaegen.
5. Cross-Ref: `fachanwalt-strafrecht-nebenklage-opfervertretung`.

### Konstellation D: Zeuge mit Auskunftsverweigerungsrecht

Mandantschaft hat Vorladung als Zeuge in einem Verfahren erhalten, ist aber selber Mit-Beschuldigte/r in anderer Sache.

1. Prüfung § 55 StPO (Selbstbelastungsgefahr) und § 52 StPO (Angehoerigenstellung).
2. Zeugenbeistand gemäß § 68b StPO; Beiordnung gemäß § 68b Abs. 2 StPO bei Bedrohung.
3. Vorbereitung der Aussage und Auskunftsverweigerung in der Vernehmung.
4. Cross-Ref: `fachanwalt-strafrecht-zeugenbeistand`.

### Konstellation E: Wirtschaftsstrafverfahren mit Insolvenzantrag der StA

Mandantschaft ist Geschäftsführer/in einer GmbH; StA hat Insolvenzantrag gemäß § 14 InsO gestellt, parallel laeuft Strafverfahren wegen Insolvenzverschleppung (§ 15a InsO) oder Untreue (§ 266 StGB).

1. Doppelgleisige Strategie: Strafverteidigung + Insolvenzverteidigung.
2. Prüfung Anhörungsantraege im InsO-Verfahren.
3. Vermögensabschoepfung gemäß §§ 73 ff. StGB und Beschlagnahme gemäß § 111b StPO im Auge behalten.
4. Cross-Ref: `fachanwalt-strafrecht-insolvenzantrag-staatsanwaltschaft`.

## Mandanten-Erwartungsmanagement

- Realistische Strafmass- und Bewaehrungs-Prognose (nicht: "Wir bekommen sicher Freispruch").
- Verfahrensdauer: Ermittlungsverfahren Wochen bis Monate, Hauptverhandlung Termine pro Instanz, Revision mehrere Monate.
- Verstaendigungschance gemäß § 257c StPO und Einstellung gemäß § 153a StPO als Option offen halten.
- Schriftliche Zusammenfassung des Erstgespraechs binnen 48 h.

## Mandatsbogen-Muster (Mindestinhalt für Strafsachen)

- Mandantschaft (Name, Geburtsdatum, Anschrift, Telefon, E-Mail).
- Rolle (Beschuldigte, Nebenklaegerin, Zeugin, Insolvenzschuldnerin/GF).
- Aktenzeichen StA / Gericht / Polizei.
- Tatvorwurf (Paragraf, Tatzeit, Tatort).
- Kurzbeschreibung Sachverhalt (5-10 Saetze).
- Ziel des Mandats (eine Zeile).
- Strittige Fragen (bullet).
- Geprueft: Konflikt - GwG - Vollmacht.
- Gebührentatbestaende (Nrn. 4100 ff. VV-RVG / Vereinbarung).
- Frist-Liste.
- Aktenanlage Datum.
- Naechster-Schritt.

## Cross-Refs

- `vergleichsverhandlung-strategie` (im selben Plugin) für Verstaendigung gemäß § 257c StPO, Einstellung gemäß § 153a StPO und Adhaesion.
- `schriftsatzkern-substantiierung` (im selben Plugin) für Verteidigungsschriftsaetze (Einspruch, Revision, Klageerzwingung).
- `fachanwalt-strafrecht-nebenklage-opfervertretung` (im selben Plugin) für Verletzten- und Nebenklagevertretung.
- `fachanwalt-strafrecht-zeugenbeistand` (im selben Plugin) für Zeugenbeistand gemäß § 68b StPO.
- `fachanwalt-strafrecht-adhaesionsverfahren` (im selben Plugin) für Adhaesion.
- `fachanwalt-strafrecht-insolvenzantrag-staatsanwaltschaft` (im selben Plugin) für parallelen Insolvenzantrag der StA.
- `kanzlei-allgemein` für Konflikt-, GwG- und Aktenanlage-Routinen.

## Aktuelle Rechtsprechung Erstgespraech / Mandatsannahme

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Erstgespraech Normen-Check

- § 136 Abs. 1 StPO — Beschuldigtenbelehrung: Schweigerecht, Verteidigerwahl
- § 137 StPO — freie Wahl des Verteidigers
- § 140 StPO — notwendige Verteidigung: Katalog der Pflichtfaelle
- § 146 StPO — Verbot Mehrfachvertretung
- §§ 10-17 GwG — Identifizierung, Risikoeinschaetzung, Dokumentation
- § 261 StGB — Geldwaesche: Strafbarkeit auch des Verteidigers bei Vorsatz/Leichtfertigkeit
- § 3a RVG — schriftliche Honorarvereinbarung; Mindestangaben

---

## Skill: `erstpruefung-und-mandatsziel`

_Wenn es um Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel in Fachanwalt Strafrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StPO; StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel.

## Spezialwissen: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** StPO.

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

## Strafrecht-Fachanwalt Erstpruefung Bausteine
- **Mandantenrolle praezisieren:**
 - **Beschuldigter / Angeklagter:** Verteidigerbestellung § 137 StPO; ggf. notwendige Verteidigung §§ 140-141 StPO.
 - **Geschaedigter / Nebenklage § 395 StPO:** Antrag Anschluss; Antragsdelikte (§§ 174-184k StGB, § 230 StGB, § 263a StGB); Zeugnis-Beistand § 68b StPO.
 - **Adhaesionsverfahren §§ 403-406c StPO:** zivilrechtliche Anspruchsverfolgung im Strafverfahren.
 - **Zeuge:** §§ 52 StPO Angehoerigenzeugnis; § 55 StPO Auskunftsverweigerung; Zeugnisbeistand.
 - **Klageerzwingung § 172 StPO:** Verletzter beantragt Erhebung der öffentlichen Klage.
- **Verfahrensstand-Triage:**
 - **Ermittlungsverfahren:** Akteneinsicht § 147 StPO; Stellungnahme StA; Schweigerecht § 136 StPO.
 - **Zwischenverfahren §§ 199-211 StPO:** Eroeffnungsbeschluss-Prüfung; Einwaende § 201 StPO; Hilfsbeweisantraege.
 - **Hauptverhandlung:** Beweisantraege § 244 StPO; Verstaendigung § 257c StPO; Schlussvortrag.
 - **Rechtsmittel:** Berufung § 314 StPO (1 Woche); Revision §§ 341, 345 StPO (1 Woche / 1 Monat); Beschwerde § 304 StPO.
 - **Vollstreckungsverfahren:** Strafrest § 57 StGB; Bewaehrungswiderruf § 56f StGB.
- **Tatvorwurfsklasse:**
 - **Vergehen § 12 II StGB** (Mindeststrafe unter 1 Jahr): Strafbefehl § 407 StPO möglich.
 - **Verbrechen § 12 I StGB** (Mindeststrafe 1 Jahr): notwendige Verteidigung § 140 I Nr. 2 StPO; Schwurgericht / große Strafkammer.
- **Mandantenziel-Hierarchie:**
 - Schuldspruch vermeiden (Freispruch).
 - Einstellung §§ 153, 153a StPO.
 - Strafmilderung.
 - Bewaehrung sichern (§ 56 StGB).
 - Reputation schuetzen (BZRG, FZR, Berufsrecht).
- **Honoraranfrage / Verguetungsvereinbarung § 3a RVG schriftlich** wenn Wahlanwaltsmandat; bei Pflichtverteidigung Festbetragstarif RVG VV 4100 ff.

---

## Skill: `strafr-wirtschaftsstrafrecht-leitfaden`

_Wenn es um Leitfaden Wirtschaftsstrafrecht: Untreue Paragraf 266 StGB, Betrug Paragraf 263, Bilanzdelikte Paragrafen 331 ff in Fachanwalt Strafrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Leitfaden Wirtschaftsstrafrecht: Untreue § 266 StGB, Betrug § 263, Bilanzdelikte §§ 331 ff


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StPO; StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Leitfaden Wirtschaftsstrafrecht: Untreue § 266 StGB, Betrug § 263, Bilanzdelikte §§ 331 ff. HGB / § 400 AktG, Compliance-Verteidigung. Prüfraster Wirtschaftsstrafkammer.

### StrafR: Wirtschaftsstrafrecht

## Spezialwissen: StrafR: Wirtschaftsstrafrecht
- **Normen-/Quellenanker:** HGB, AktG.

## Fallweichen
Frage zu Beginn nur ab, was für den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Verträge, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, für wen, in welcher Tonalitaet?

## Prüfraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Prüfung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Prüfvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei prüfbarem Link.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

---

## Anwendungshinweise

1. Diesen Vollprüfung als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.
