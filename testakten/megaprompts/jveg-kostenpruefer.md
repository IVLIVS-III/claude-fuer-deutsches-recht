# Vollprüfung: jveg-kostenpruefer

## Zusammensetzung

Dieser Vollprüfung enthaelt top-15 von 60 Skills des Plugins `jveg-kostenpruefer`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Wenn es um Einstieg und Routing in JVEG-Kostenprüfer geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächst…
2. **freistehender-erstpruefung-und-mandatsziel** — Wenn es um Freistehender: Erstprüfung, Rollenklärung und Mandatsziel in JVEG-Kostenprüfer geht: klärt Rolle, Ziel, Frist…
3. **uebernachtung-verdienstausfall-vorschuss** — Wenn es um Uebernachtung: Schriftsatz-, Brief- und Memo-Bausteine in JVEG-Kostenprüfer geht: erstellt den passenden Entw…
4. **pruefung-sachverstaendigengutachten-ki-deklaration** — Wenn es um Prüfung Sachverständigengutachten — digitale Werkzeuge-Deklaration und JVEG in JVEG-Kostenprüfer geht: prüft …
5. **dolmetscherkosten-zahlen-schwellen-und-berechnung** — Wenn es um Dolmetscherkosten: Zahlen, Schwellenwerte und Berechnung in JVEG-Kostenprüfer geht: rechnet Schwellen, Beträg…
6. **vorschuss-kostenrisiko-spezial** — Wenn es um JVEG: Vorschuss Kostenrisiko in JVEG-Kostenprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente …
7. **vorschuss-risikoampel-und-gegenargumente** — Wenn es um Vorschuss: Risikoampel, Gegenargumente und Verteidigungslinien in JVEG-Kostenprüfer geht: zerlegt Ergebnis, F…
8. **verdienstausfall-verhandlung-vergleich-und-eskalation** — Wenn es um Verdienstausfall: Verhandlung, Vergleich und Eskalation in JVEG-Kostenprüfer geht: entwickelt Verhandlungszie…
9. **kostenpruefer-fristen-form-und-zustaendigkeit** — Wenn es um Kostenpruefer: Fristen, Form, Zuständigkeit und Rechtsweg in JVEG-Kostenprüfer geht: prüft Frist, Form, Zustä…
10. **quality-mandantenkommunikation-entscheidungsvorlage** — Wenn es um Quality: Mandantenkommunikation und Entscheidungsvorlage in JVEG-Kostenprüfer geht: prüft Frist, Form, Zustän…
11. **sonstige-aufwendungen-uebernachtung** — Wenn es um JVEG-Sonstige-Aufwendungen-Belege in JVEG-Kostenprüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforde…
12. **spezial-sachverstaendigen-livequellen-und-rechtsprechungscheck** — Wenn es um Sachverstaendigen: Livequellen- und Rechtsprechungscheck in JVEG-Kostenprüfer geht: prüft Frist, Form, Zustän…
13. **zeugenentschaedigung-dokumentenmatrix-und-lueckenliste** — Wenn es um Zeugenentschaedigung: Dokumentenmatrix, Lückenliste und Nachforderung in JVEG-Kostenprüfer geht: ordnet Akten…
14. **festsetzung-mehrparteien-konflikt-und-interessen** — Wenn es um Festsetzung: Mehrparteienkonflikt und Interessenmatrix in JVEG-Kostenprüfer geht: prüft Frist, Form, Zuständi…
15. **spezial-rechenprotokolle-red-team-und-qualitaetskontrolle** — Wenn es um Rechenprotokolle: Red-Team und Qualitätskontrolle in JVEG-Kostenprüfer geht: zerlegt Ergebnis, Frist, Zuständ…

---

## Skill: `einstieg-routing`

_Wenn es um Einstieg und Routing in JVEG-Kostenprüfer geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Jveg Kostenpruefer** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `aktenstripper` — Aktenstripper
- `anspruchsberechtigung-antragsgenerator` — Anspruchsberechtigung Antragsgenerator
- `antragsgenerator` — Antragsgenerator
- `belegfeste-formular-portal-und-einreichung` — Belegfeste Formular Portal und Einreichung
- `beschwerde-dolmetscher-sonderfall` — Beschwerde Dolmetscher Sonderfall
- `dolmetscher-sonderfall-und-edge-case` — Dolmetscher Sonderfall und Edge Case
- `dolmetscher-uebersetzer` — Dolmetscher Übersetzer
- `dolmetscher-uebersetzer-fahrtkosten` — Dolmetscher Übersetzer Fahrtkosten
- `dolmetscherkosten-zahlen-schwellen-und-berechnung` — Dolmetscherkosten Zahlen Schwellen und Berechnung
- `fahrtkosten` — Fahrtkosten
- `fahrtkosten-festsetzung-interessen` — Fahrtkosten Festsetzung Interessen
- `festsetzung-beschwerde` — Festsetzung Beschwerde
- `festsetzung-mehrparteien-konflikt-und-interessen` — Festsetzung Mehrparteien Konflikt und Interessen
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Jveg Kostenpruefer sind JVEG. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `freistehender-erstpruefung-und-mandatsziel`

_Wenn es um Freistehender: Erstprüfung, Rollenklärung und Mandatsziel in JVEG-Kostenprüfer geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Freistehender: Erstprüfung, Rollenklärung und Mandatsziel

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
- Fristen und Eilrisiken zuerst markieren: JVEG § 2 Antragsfrist 3 Monate nach Beendigung der Tätigkeit, § 4 Erinnerung 2 Wochen, Beschwerde § 4 Abs. 3 unbefristet.
- Tragende Normen verifizieren: JVEG §§ 1, 2, 4, 5, 7, 8, 9, 10, 12, 13, 14, 19, 22, 23, RVG (Anwalt), ZSEG (alt), KostO/GNotKG, GG Art. 12 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Sachverständiger, Dolmetscher, Übersetzer, Geschäftsstelle, Kostenbeamter, Bezirksrevisor, Festsetzungsrichter, Erinnerung-/Beschwerdesenat.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Vergütungsantrag, Stundennachweis, Reisekostenabrechnung, Festsetzungsbeschluss, Erinnerung, Beschwerde, Sachverständigenrechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Freistehender: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Freistehender** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `uebernachtung-verdienstausfall-vorschuss`

_Wenn es um Uebernachtung: Schriftsatz-, Brief- und Memo-Bausteine in JVEG-Kostenprüfer geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik._

# Uebernachtung: Schriftsatz-, Brief- und Memo-Bausteine

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: JVEG § 2 Antragsfrist 3 Monate nach Beendigung der Tätigkeit, § 4 Erinnerung 2 Wochen, Beschwerde § 4 Abs. 3 unbefristet.
- Tragende Normen verifizieren: JVEG §§ 1, 2, 4, 5, 7, 8, 9, 10, 12, 13, 14, 19, 22, 23, RVG (Anwalt), ZSEG (alt), KostO/GNotKG, GG Art. 12 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Sachverständiger, Dolmetscher, Übersetzer, Geschäftsstelle, Kostenbeamter, Bezirksrevisor, Festsetzungsrichter, Erinnerung-/Beschwerdesenat.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Vergütungsantrag, Stundennachweis, Reisekostenabrechnung, Festsetzungsbeschluss, Erinnerung, Beschwerde, Sachverständigenrechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Uebernachtung: Schriftsatz-, Brief- und Memo-Bausteine
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Uebernachtung** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `pruefung-sachverstaendigengutachten-ki-deklaration`

_Wenn es um Prüfung Sachverständigengutachten — digitale Werkzeuge-Deklaration und JVEG in JVEG-Kostenprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Prüfung Sachverständigengutachten — KI-Deklaration und JVEG

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: JVEG § 2 Antragsfrist 3 Monate nach Beendigung der Tätigkeit, § 4 Erinnerung 2 Wochen, Beschwerde § 4 Abs. 3 unbefristet.
- Tragende Normen verifizieren: JVEG §§ 1, 2, 4, 5, 7, 8, 9, 10, 12, 13, 14, 19, 22, 23, RVG (Anwalt), ZSEG (alt), KostO/GNotKG, GG Art. 12 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Sachverständiger, Dolmetscher, Übersetzer, Geschäftsstelle, Kostenbeamter, Bezirksrevisor, Festsetzungsrichter, Erinnerung-/Beschwerdesenat.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Vergütungsantrag, Stundennachweis, Reisekostenabrechnung, Festsetzungsbeschluss, Erinnerung, Beschwerde, Sachverständigenrechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Prüfung Sachverständigengutachten — KI-Deklaration und JVEG
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.

## Triage — kläre vor der Prüfung

1. **Indizienlage:** Welche konkreten Anhaltspunkte für KI-Einsatz liegen vor (Stilauffälligkeiten, fehlende Anknüpfungstatsachen)?
2. **Anhörung:** Wurde der Sachverständige bereits zu Hilfsmitteln und persönlicher Erstellung gehört?
3. **Verwertbarkeit:** Ist das Gutachten unabhängig vom KI-Verdacht methodisch verwertbar?
4. **Vergütungshöhe:** Welchen Betrag macht der Sachverständige geltend — gibt es einen genehmigten Vorschuss?
5. **Beschwerdestadium:** Ist bereits ein Festsetzungsbeschluss ergangen oder steht er noch aus?

## Rechtsprechung
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zweck dieses Skills

Wenn dem Gericht ein Sachverständigengutachten zur Vergütungsfestsetzung vorgelegt wird und Anhaltspunkte für KI-Einsatz bestehen, strukturiert dieser Skill die richterliche Prüfung. Er greift im JVEG-Kostenprüfungsverfahren ebenso wie bei der Verwertbarkeitsprüfung im Hauptverfahren.

## Rechtsgrundlagen

- **§ 4 Abs. 1 S. 1 JVEG** — Vergütungsfestsetzung durch das Gericht
- **§ 8a Abs. 2 S. 1 Nr. 1 JVEG** — Wegfall der Vergütung bei unklarer Identität des Erstellers
- **§ 8a Abs. 2 S. 1 Nr. 2 JVEG** — Wegfall bei objektiver Unverwertbarkeit
- **§ 407a Abs. 1 ZPO** — höchstpersönliche Erstellungspflicht
- **§ 407a Abs. 3 ZPO** — Mitarbeiterbenennung
- **§ 407a Abs. 5 ZPO** — Aktenherausgabe
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- **Keine generelle KI-Kennzeichnungspflicht**; Anker ist die persönliche Verantwortlichkeit

## Prüfungsschema für das Gericht

### Schritt 1: Aktenstudium und Indizienlage

```
□ Ist im Gutachten ein Hinweis auf eingesetzte Hilfsmittel
 enthalten?
□ Sind Mitarbeiter benannt (§ 407a Abs. 3 ZPO)?
□ Gibt es Anhaltspunkte, dass das Gutachten nicht persönlich
 erstellt wurde?
 - Gleichförmige Satzanfänge in mehrfacher Wiederholung
 - Dreifach-Strukturen in Aufzählungen ohne sachlichen Grund
 - Sachverständiger nennt sich selbst als Adressat
 - Halbsatzkonstruktionen, die wie Prompt-Nachschärfungen
 wirken
 - Stilbrüche zwischen Kapiteln
 - Generische Standardformulierungen ohne Fallbezug
 - Fehlende Auseinandersetzung mit konkreten
 Anknüpfungstatsachen
□ Wurde eine Untersuchung der Beteiligten durchgeführt, wenn
 erforderlich?
```

→ Einzelne Indizien tragen nicht. Erst das **Gesamtbild** kann eine ernsthafte Prüfung rechtfertigen.

### Schritt 2: Anhörung des Sachverständigen

Vor einer Vergütungssperre ist der Sachverständige in der Regel anzuhören:

- Ladung zur mündlichen Erläuterung (§ 411 Abs. 3 ZPO) oder schriftliche Stellungnahme
- Konkrete Fragen:
 - Welche Erstellungsschritte hat er persönlich vorgenommen?
 - Wurden Hilfskräfte oder technische Hilfsmittel eingesetzt? Welche?
 - Wer ist verantwortlich für welche Passagen des Gutachtens?
 - Wie ist eine Auffälligkeit konkret zu erklären?

→ Die Antworten sind ins Protokoll aufzunehmen.

### Schritt 3: Bewertung nach § 8a Abs. 2 S. 1 JVEG

Zwei eigenständige Tatbestände:

**Nr. 1 — unklare Identität des Erstellers**:
- Wenn auch nach Anhörung nicht klar ist, wer das Gutachten tatsächlich erstellt hat
- Wenn der Sachverständige die persönliche Erstellung nicht plausibilisieren kann
- Wenn KI-Einsatz in einem Umfang erfolgte, dass die persönliche Verantwortung verloren geht

→ Erst-recht-Schluss aus § 407a Abs. 3 ZPO (Mitarbeiterbenennung) und § 407a Abs. 5 ZPO (Aktenherausgabe): Wenn schon menschliche Mitarbeiter zu benennen sind, muss erst recht offen sein, ob und in welchem Umfang KI-Systeme an der Erstellung beteiligt waren.

**Nr. 2 — objektive Unverwertbarkeit**:
- Methodische Mängel
- Nichtbeantwortung der Beweisfrage
- Innere Widersprüche
- Fehlende Anknüpfungstatsachen oder Untersuchung
- → Unabhängig vom KI-Verdacht festzustellen

### Schritt 4: Entscheidung

| Befund | Konsequenz |
|----|----|
| Persönliche Erstellung plausibilisiert, keine Mängel | Vergütung wie beantragt festsetzen |
| Persönliche Erstellung plausibilisiert, aber methodische Mängel | Vergütung kürzen oder bei objektiver Unverwertbarkeit (Nr. 2) auf 0 Euro |
| Identität des Erstellers unklar trotz Anhörung | Festsetzung auf 0 Euro nach § 8a Abs. 2 S. 1 Nr. 1 JVEG erwägen |
| Beides — unklare Identität + Unverwertbarkeit | Festsetzung auf 0 Euro klar tragbar |
| Hilfsmittel zulässig eingesetzt, Verantwortlichkeit klar | Vergütung wie beantragt |

### Schritt 5: Begründung des Beschlusses

Der Beschluss muss tragend begründen:

- Welche **konkreten Indizien** liegen vor (seitengenau)?
- Welche **Antworten** hat der Sachverständige in der Anhörung gegeben?
- Welche **konkreten Mängel** sind objektiv festgestellt?
- Welche **Norm** trägt die Sanktion (§ 8a Abs. 2 S. 1 Nr. 1 oder Nr. 2 JVEG)?
- Warum **rechtfertigt der erhebliche KI-Einsatz ohne Deklaration** allein oder im Zusammenspiel mit Mängeln die Vergütungssperre?

### Schritt 6: Beschwerdeverfahren

- Sachverständiger kann gegen die Festsetzung Beschwerde einlegen (§ 4 Abs. 3 JVEG)
- Das Gericht prüft die Beschwerde und entscheidet über Abhilfe oder Nichtabhilfe
- Bei Nichtabhilfe: Vorlage an das Beschwerdegericht (regelmäßig OLG)
- Im Nichtabhilfebeschluss insbesondere darauf eingehen, ob die Argumentation des Sachverständigen die Identitäts- oder Unverwertbarkeitsfrage ausräumt

## Checkliste — Indizien für KI-Einsatz im Gutachten

```
□ Wiederholung identischer Satzanfänge (drei- oder mehrfach)
□ Generische, austauschbare Standardformulierungen
□ Dreifach-Strukturen ohne sachlichen Grund
□ Stilbrüche zwischen Kapiteln
□ Sachverständiger nennt sich selbst als Adressat
□ Halbsätze, die wie Prompt-Nachschärfungen wirken
□ Fehlende Würdigung konkreter Anknüpfungstatsachen
□ Belegketten, die nicht zur konkreten Akte passen
□ Auffällige Übereinstimmungen mit anderen, dem Gericht
 bekannten Gutachten desselben Sachverständigen
□ Standard-Floskeln aus generativen Modellen
 ("Es ist wichtig zu beachten…", "Zusammenfassend lässt sich
 festhalten…") in unangemessener Häufung
```

## Hinweise zur höchstpersönlichen Erstellung

**Was bleibt zulässig?**

- KI als Recherchewerkzeug (Literaturrecherche, Übersetzung)
- KI als Korrekturhilfe (Rechtschreibung, Grammatik)
- KI als Strukturierungshilfe
- Diktiersysteme, auch KI-gestützt

→ Voraussetzung: Der Sachverständige **prüft und verantwortet** den Inhalt persönlich. Die gedankliche Durchdringung der konkreten Beweisfrage bleibt seine Aufgabe.

**Was ist nicht mehr zulässig?**

- Generierung ganzer Gutachtenpassagen durch KI mit nur oberflächlicher Reviewfunktion
- Beantwortung der Beweisfrage durch KI ohne eigene fachliche Würdigung
- Auslagerung der Anknüpfungstatsachen-Würdigung an KI
- Verschweigen von KI-Einsatz in einem Umfang, der die persönliche Verantwortung in Frage stellt

## Templates

### Anhörungsverfügung bei KI-Verdacht

```
Verfügung:

Der Sachverständige [Name] wird gebeten, bis [Datum] schriftlich
zu folgenden Fragen Stellung zu nehmen:

1. Welche Untersuchungs- und Erhebungsschritte haben Sie
 persönlich durchgeführt?
2. Welche Hilfsmittel haben Sie bei der Erstellung des Gutachtens
 eingesetzt? Bitte konkretisieren Sie etwaige technische
 Werkzeuge.
3. Wer war an der Erstellung beteiligt? Bitte benennen Sie
 sämtliche Mitarbeiter gemäß § 407a Abs. 3 ZPO.
4. Wie ist die mehrfach gleichförmige Formulierung an folgenden
 Stellen zu erklären: [konkrete Fundstellen].
5. Bitte legen Sie gemäß § 407a Abs. 5 ZPO sämtliche Unterlagen
 vor, die der Begutachtung zugrunde liegen, einschließlich
 etwaiger Recherche- und Vorbereitungsdokumentation.

Auf die Folgen einer Vergütungssperre nach § 8a Abs. 2 S. 1
JVEG wird hingewiesen.
```

### Beschluss-Tenor (Vergütung auf 0 Euro)

```
Tenor:

Die Vergütung des Sachverständigen [Name] für das Gutachten vom
[Datum] wird gemäß § 4 Abs. 1 S. 1 JVEG i.V.m. § 8a Abs. 2 S. 1
[Nr. 1 / Nr. 2 / Nr. 1 und Nr. 2] JVEG auf 0,00 Euro festgesetzt.

Gründe:
[Indizienlage darstellen — seitengenau]
[Antwort des Sachverständigen aus der Anhörung]
[Konkrete Feststellungen zu § 8a Abs. 2 S. 1 Nr. 1 / Nr. 2 JVEG]
[Erst-recht-Schluss aus § 407a Abs. 3 und Abs. 5 ZPO]
[Keine generelle KI-Kennzeichnungspflicht — der Anker liegt in
 der höchstpersönlichen Erstellungspflicht des § 407a Abs. 1 ZPO]
```

### Nichtabhilfebeschluss

```
Tenor:

Der Beschwerde des Sachverständigen [Name] vom [Datum] gegen den
Beschluss vom [Datum] wird nicht abgeholfen. Die Akte wird dem
Oberlandesgericht [Sitz] zur Entscheidung über die Beschwerde
vorgelegt.

Gründe:
[Auseinandersetzung mit den Argumenten des Sachverständigen]
[Persönliche Verantwortlichkeit bleibt offen, insbesondere die
 Rolle etwaiger Mitarbeiter oder technischer Hilfsmittel]
[Festhalten an den Mängeln nach § 8a Abs. 2 S. 1 JVEG]
[Kein Anhaltspunkt für eine andere Beurteilung]
```

## Fallstricke und Hinweise

- **Eigenständigkeit der beiden Tatbestände**: Nr. 1 und Nr. 2 sind getrennt zu prüfen. Im Beschluss klar herausarbeiten, welche Norm trägt.
- **Verhältnismäßigkeit**: Vor einer 0-Euro-Festsetzung muss ein Anhörungstermin oder eine schriftliche Stellungnahme gewährt worden sein.
- **Keine Schematismus**: Der bloße Einsatz von KI rechtfertigt keine Vergütungssperre. Erforderlich ist entweder die Identitätsunklarheit (Nr. 1) oder die objektive Unverwertbarkeit (Nr. 2) oder beides.
- **Erfahrungswerte aus aktueller Instanzrechtsprechung**: Erhebliche, nicht deklarierte KI-Einsätze können bereits allein die Festsetzung auf 0 Euro tragen, wenn die persönliche Erstellung nicht mehr plausibel ist.
- **Kollegen einbinden**: Bei grundsätzlicher Bedeutung Anregung an die Kammer oder das Präsidium, Leitlinien zu entwickeln.
- **Externe Berichterstattung**: Beschlüsse mit 0-Euro-Festsetzung können öffentliche Aufmerksamkeit erzeugen — Vorsicht bei der Anonymisierung.

---

## Skill: `dolmetscherkosten-zahlen-schwellen-und-berechnung`

_Wenn es um Dolmetscherkosten: Zahlen, Schwellenwerte und Berechnung in JVEG-Kostenprüfer geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen._

# Dolmetscherkosten: Zahlen, Schwellenwerte und Berechnung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: JVEG § 2 Antragsfrist 3 Monate nach Beendigung der Tätigkeit, § 4 Erinnerung 2 Wochen, Beschwerde § 4 Abs. 3 unbefristet.
- Tragende Normen verifizieren: JVEG §§ 1, 2, 4, 5, 7, 8, 9, 10, 12, 13, 14, 19, 22, 23, RVG (Anwalt), ZSEG (alt), KostO/GNotKG, GG Art. 12 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Sachverständiger, Dolmetscher, Übersetzer, Geschäftsstelle, Kostenbeamter, Bezirksrevisor, Festsetzungsrichter, Erinnerung-/Beschwerdesenat.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Vergütungsantrag, Stundennachweis, Reisekostenabrechnung, Festsetzungsbeschluss, Erinnerung, Beschwerde, Sachverständigenrechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Dolmetscherkosten: Zahlen, Schwellenwerte und Berechnung
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Dolmetscherkosten** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Dolmetscher- und Übersetzersätze nach JVEG (Stand prüfen!)
- **§ 9 Abs. 3 JVEG -- Stundensätze Dolmetscher:** simultanes Dolmetschen 85 EUR/h, konsekutives Dolmetschen 75 EUR/h (Stand prüfen unter `gesetze-im-internet.de/jveg`; KostRÄG-Anpassungen beachten).
- **§ 11 JVEG -- Übersetzer:** Grundbetrag pro 55-Zeichen-Zeile (Standardzeile) je nach Schwierigkeitsgrad gestaffelt; bei besonders schwierigen Texten höhere Sätze; bei elektronisch editierbar gelieferten Ausgangstexten ggf. niedriger.
- **Wartezeit (§ 19 JVEG):** auch Wartezeit ist vergütungspflichtig, soweit dem Dolmetscher zumutbar.
- **Fahrtkosten (§ 5 JVEG):** Pkw 0,42 EUR/km, alternativ Bahn 2. Klasse / BC100.
- **Tagegeld / Übernachtung (§ 6 JVEG):** wie für Sachverständige, Verweis auf BRKG.
- **Umsatzsteuer (§ 12 JVEG):** zusätzlich; bei Kleinunternehmer § 19 UStG keine Ust.

## Berechnungs-Pflichtschritte
1. Heranziehungsbeschluss prüfen: Stundensatz festgelegt oder Standardsatz?
2. Tatsächliche Stundenzahl mit Tätigkeitsbeschreibung; Wartezeit gesondert ausweisen.
3. Auslagen mit Belegen (Tickets, Hotelrechnungen).
4. Umsatzsteuer-Status klären.
5. Summenkontrolle und Antrag (§ 4 Abs. 1 JVEG); Fristnotierung Erinnerung (6 Monate § 4 Abs. 4 JVEG).

---

## Skill: `vorschuss-kostenrisiko-spezial`

_Wenn es um JVEG: Vorschuss Kostenrisiko in JVEG-Kostenprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt._

# JVEG: Vorschuss Kostenrisiko

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: JVEG § 2 Antragsfrist 3 Monate nach Beendigung der Tätigkeit, § 4 Erinnerung 2 Wochen, Beschwerde § 4 Abs. 3 unbefristet.
- Tragende Normen verifizieren: JVEG §§ 1, 2, 4, 5, 7, 8, 9, 10, 12, 13, 14, 19, 22, 23, RVG (Anwalt), ZSEG (alt), KostO/GNotKG, GG Art. 12 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Sachverständiger, Dolmetscher, Übersetzer, Geschäftsstelle, Kostenbeamter, Bezirksrevisor, Festsetzungsrichter, Erinnerung-/Beschwerdesenat.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Vergütungsantrag, Stundennachweis, Reisekostenabrechnung, Festsetzungsbeschluss, Erinnerung, Beschwerde, Sachverständigenrechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: JVEG: Vorschuss Kostenrisiko
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.

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

## Skill: `vorschuss-risikoampel-und-gegenargumente`

_Wenn es um Vorschuss: Risikoampel, Gegenargumente und Verteidigungslinien in JVEG-Kostenprüfer geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Vorschuss: Risikoampel, Gegenargumente und Verteidigungslinien

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: JVEG § 2 Antragsfrist 3 Monate nach Beendigung der Tätigkeit, § 4 Erinnerung 2 Wochen, Beschwerde § 4 Abs. 3 unbefristet.
- Tragende Normen verifizieren: JVEG §§ 1, 2, 4, 5, 7, 8, 9, 10, 12, 13, 14, 19, 22, 23, RVG (Anwalt), ZSEG (alt), KostO/GNotKG, GG Art. 12 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Sachverständiger, Dolmetscher, Übersetzer, Geschäftsstelle, Kostenbeamter, Bezirksrevisor, Festsetzungsrichter, Erinnerung-/Beschwerdesenat.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Vergütungsantrag, Stundennachweis, Reisekostenabrechnung, Festsetzungsbeschluss, Erinnerung, Beschwerde, Sachverständigenrechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Vorschuss: Risikoampel, Gegenargumente und Verteidigungslinien
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Vorschuss** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `verdienstausfall-verhandlung-vergleich-und-eskalation`

_Wenn es um Verdienstausfall: Verhandlung, Vergleich und Eskalation in JVEG-Kostenprüfer geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen._

# Verdienstausfall: Verhandlung, Vergleich und Eskalation

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: JVEG § 2 Antragsfrist 3 Monate nach Beendigung der Tätigkeit, § 4 Erinnerung 2 Wochen, Beschwerde § 4 Abs. 3 unbefristet.
- Tragende Normen verifizieren: JVEG §§ 1, 2, 4, 5, 7, 8, 9, 10, 12, 13, 14, 19, 22, 23, RVG (Anwalt), ZSEG (alt), KostO/GNotKG, GG Art. 12 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Sachverständiger, Dolmetscher, Übersetzer, Geschäftsstelle, Kostenbeamter, Bezirksrevisor, Festsetzungsrichter, Erinnerung-/Beschwerdesenat.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Vergütungsantrag, Stundennachweis, Reisekostenabrechnung, Festsetzungsbeschluss, Erinnerung, Beschwerde, Sachverständigenrechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Verdienstausfall: Verhandlung, Vergleich und Eskalation
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Verdienstausfall** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `kostenpruefer-fristen-form-und-zustaendigkeit`

_Wenn es um Kostenpruefer: Fristen, Form, Zuständigkeit und Rechtsweg in JVEG-Kostenprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Kostenpruefer: Fristen, Form, Zuständigkeit und Rechtsweg

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: JVEG § 2 Antragsfrist 3 Monate nach Beendigung der Tätigkeit, § 4 Erinnerung 2 Wochen, Beschwerde § 4 Abs. 3 unbefristet.
- Tragende Normen verifizieren: JVEG §§ 1, 2, 4, 5, 7, 8, 9, 10, 12, 13, 14, 19, 22, 23, RVG (Anwalt), ZSEG (alt), KostO/GNotKG, GG Art. 12 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Sachverständiger, Dolmetscher, Übersetzer, Geschäftsstelle, Kostenbeamter, Bezirksrevisor, Festsetzungsrichter, Erinnerung-/Beschwerdesenat.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Vergütungsantrag, Stundennachweis, Reisekostenabrechnung, Festsetzungsbeschluss, Erinnerung, Beschwerde, Sachverständigenrechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Kostenpruefer: Fristen, Form, Zuständigkeit und Rechtsweg
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Kostenpruefer** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `quality-mandantenkommunikation-entscheidungsvorlage`

_Wenn es um Quality: Mandantenkommunikation und Entscheidungsvorlage in JVEG-Kostenprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Quality: Mandantenkommunikation und Entscheidungsvorlage

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: JVEG § 2 Antragsfrist 3 Monate nach Beendigung der Tätigkeit, § 4 Erinnerung 2 Wochen, Beschwerde § 4 Abs. 3 unbefristet.
- Tragende Normen verifizieren: JVEG §§ 1, 2, 4, 5, 7, 8, 9, 10, 12, 13, 14, 19, 22, 23, RVG (Anwalt), ZSEG (alt), KostO/GNotKG, GG Art. 12 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Sachverständiger, Dolmetscher, Übersetzer, Geschäftsstelle, Kostenbeamter, Bezirksrevisor, Festsetzungsrichter, Erinnerung-/Beschwerdesenat.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Vergütungsantrag, Stundennachweis, Reisekostenabrechnung, Festsetzungsbeschluss, Erinnerung, Beschwerde, Sachverständigenrechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Quality: Mandantenkommunikation und Entscheidungsvorlage
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Quality** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `sonstige-aufwendungen-uebernachtung`

_Wenn es um JVEG-Sonstige-Aufwendungen-Belege in JVEG-Kostenprüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt._

# JVEG-Sonstige-Aufwendungen-Belege

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: JVEG § 2 Antragsfrist 3 Monate nach Beendigung der Tätigkeit, § 4 Erinnerung 2 Wochen, Beschwerde § 4 Abs. 3 unbefristet.
- Tragende Normen verifizieren: JVEG §§ 1, 2, 4, 5, 7, 8, 9, 10, 12, 13, 14, 19, 22, 23, RVG (Anwalt), ZSEG (alt), KostO/GNotKG, GG Art. 12 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Sachverständiger, Dolmetscher, Übersetzer, Geschäftsstelle, Kostenbeamter, Bezirksrevisor, Festsetzungsrichter, Erinnerung-/Beschwerdesenat.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Vergütungsantrag, Stundennachweis, Reisekostenabrechnung, Festsetzungsbeschluss, Erinnerung, Beschwerde, Sachverständigenrechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: JVEG-Sonstige-Aufwendungen-Belege
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.

## Triage — kläre vor der Prüfung

1. **Aufwendungsart:** Kopien, Dateien, Begleitperson, Vertretungskosten oder sonstige bare Auslagen?
2. **Notwendigkeit:** Waren die Aufwendungen für die Auftragserfüllung notwendig (Wirtschaftlichkeitsgebot)?
3. **Belege:** Liegen Originalquittungen oder sonstige Belege vor?
4. **Begleitperson:** Ist die Mitnahme einer Begleitperson medizinisch oder faktisch notwendig nachgewiesen?
5. **Normgrundlage:** Ist die konkrete Aufwendung im JVEG geregelt oder nur analog zu behandeln?

## Zentrale Normen
- § 7 Abs. 2 JVEG (Reisenebenkosten, bare Auslagen)
- § 12 JVEG (Nebenkosten Sachverständige: Kopien, Dateien, Lichtbilder)
- § 5 Abs. 4 JVEG (Parkkosten und Sonderreisenebenkosten)
- § 6 JVEG (Sonderfall Begleitperson bei Reise)

## Rechtsprechung
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Startet bei
Rechnung enthält Positionen jenseits von Honorar, Reisezeit und Fahrtkosten.

## Output-Template

| Position | Norm | Betrag geltend (EUR) | Beleg | Notwendig | Anerkannt (EUR) |
|---|---|---|---|---|---|
| Kopien [X × Y EUR] | § 12 JVEG | 00,00 | Ja/Nein | Ja/Nein | 00,00 |
| Begleitperson | § 6 JVEG | 00,00 | Ja/Nein | Ja/Nein | 00,00 |
| Sonstige bare Auslagen | § 7 Abs. 2 JVEG | 00,00 | Ja/Nein | Ja/Nein | 00,00 |
| **Gesamt** | | **00,00** | | | **00,00** |

## Ausgabe
Prüfergebnis für Sammelposition sonstige Aufwendungen mit Belegstatus.

## Leitplanken
- Kein Ansatz ohne Normgrundlage; Analogie nur in engen Grenzen.
- Hinweis: Keine Rechtsberatung. Ausgaben dienen der internen Arbeitsvorbereitung.

---

## Skill: `spezial-sachverstaendigen-livequellen-und-rechtsprechungscheck`

_Wenn es um Sachverstaendigen: Livequellen- und Rechtsprechungscheck in JVEG-Kostenprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Sachverstaendigen: Livequellen- und Rechtsprechungscheck

## Aufgabe
Dieser Skill ist ein konkreter Fachbaustein für `jveg-kostenpruefer`. Ausgangspunkt ist: Freistehender JVEG-Kostenprüfer für Zeugenentschädigung, Vorschuss, Fahrtkosten, Übernachtung, Verdienstausfall, Sachverständigen- und Dolmetscherkosten, Fristen, Festsetzung, Beschwerde und belegfeste Rechenprotokolle.

Er führt durch **Livequellen- und Rechtsprechungscheck** im Themenfeld **Sachverstaendigen**. Ziel ist nicht ein abstrakter Lexikontext, sondern ein belastbares Arbeitsprodukt für die nächste anwaltliche, behördliche, gerichtliche, organisatorische oder mandantenbezogene Entscheidung.


## Fachlicher Zuschnitt

- **Thema:** Sachverstaendigen.
- **Arbeitsfokus:** Livequellen- und Rechtsprechungscheck.
- **Plugin-Rahmen:** Freistehender JVEG-Kostenprüfer für Zeugenentschädigung, Vorschuss, Fahrtkosten, Übernachtung, Verdienstausfall, Sachverständigen- und Dolmetscherkosten....
- **Qualitätsanspruch:** Antworte nicht mit einer austauschbaren Standard-Checkliste. Nutze die Fachlogik dieses Plugins, benenne die konkret einschlägigen Normgruppen, Behörden, Register, Fristen, Dokumente oder Verfahrenshandlungen und trenne sichere Punkte von Live-Check-Bedarf.
- **Eloquenz und Nutzen:** Führe die Nutzerin oder den Nutzer wie eine erfahrene Fachperson: kurze Orientierung, präzise Rückfragen, dann ein verwertbares Produkt mit Varianten, Gegenargumenten und nächstem Handgriff.

## Kaltstart
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Sachverstaendigen** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

---

## Skill: `zeugenentschaedigung-dokumentenmatrix-und-lueckenliste`

_Wenn es um Zeugenentschaedigung: Dokumentenmatrix, Lückenliste und Nachforderung in JVEG-Kostenprüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste._

# Zeugenentschaedigung: Dokumentenmatrix, Lückenliste und Nachforderung


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: JVEG § 2 Antragsfrist 3 Monate nach Beendigung der Tätigkeit, § 4 Erinnerung 2 Wochen, Beschwerde § 4 Abs. 3 unbefristet.
- Tragende Normen verifizieren: JVEG §§ 1, 2, 4, 5, 7, 8, 9, 10, 12, 13, 14, 19, 22, 23, RVG (Anwalt), ZSEG (alt), KostO/GNotKG, GG Art. 12 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Sachverständiger, Dolmetscher, Übersetzer, Geschäftsstelle, Kostenbeamter, Bezirksrevisor, Festsetzungsrichter, Erinnerung-/Beschwerdesenat.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Vergütungsantrag, Stundennachweis, Reisekostenabrechnung, Festsetzungsbeschluss, Erinnerung, Beschwerde, Sachverständigenrechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Zeugenentschaedigung: Dokumentenmatrix, Lückenliste und Nachforderung.

## Fachkern: Zeugenentschaedigung: Dokumentenmatrix, Lückenliste und Nachforderung
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Zeugenentschaedigung** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `festsetzung-mehrparteien-konflikt-und-interessen`

_Wenn es um Festsetzung: Mehrparteienkonflikt und Interessenmatrix in JVEG-Kostenprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Festsetzung: Mehrparteienkonflikt und Interessenmatrix

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: JVEG § 2 Antragsfrist 3 Monate nach Beendigung der Tätigkeit, § 4 Erinnerung 2 Wochen, Beschwerde § 4 Abs. 3 unbefristet.
- Tragende Normen verifizieren: JVEG §§ 1, 2, 4, 5, 7, 8, 9, 10, 12, 13, 14, 19, 22, 23, RVG (Anwalt), ZSEG (alt), KostO/GNotKG, GG Art. 12 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Sachverständiger, Dolmetscher, Übersetzer, Geschäftsstelle, Kostenbeamter, Bezirksrevisor, Festsetzungsrichter, Erinnerung-/Beschwerdesenat.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Vergütungsantrag, Stundennachweis, Reisekostenabrechnung, Festsetzungsbeschluss, Erinnerung, Beschwerde, Sachverständigenrechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Festsetzung: Mehrparteienkonflikt und Interessenmatrix
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Festsetzung** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `spezial-rechenprotokolle-red-team-und-qualitaetskontrolle`

_Wenn es um Rechenprotokolle: Red-Team und Qualitätskontrolle in JVEG-Kostenprüfer geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Rechenprotokolle: Red-Team und Qualitätskontrolle

## Aufgabe
Dieser Skill ist ein konkreter Fachbaustein für `jveg-kostenpruefer`. Ausgangspunkt ist: Freistehender JVEG-Kostenprüfer für Zeugenentschädigung, Vorschuss, Fahrtkosten, Übernachtung, Verdienstausfall, Sachverständigen- und Dolmetscherkosten, Fristen, Festsetzung, Beschwerde und belegfeste Rechenprotokolle.

Er führt durch **Red-Team und Qualitätskontrolle** im Themenfeld **Rechenprotokolle**. Ziel ist nicht ein abstrakter Lexikontext, sondern ein belastbares Arbeitsprodukt für die nächste anwaltliche, behördliche, gerichtliche, organisatorische oder mandantenbezogene Entscheidung.


## Fachlicher Zuschnitt

- **Thema:** Rechenprotokolle.
- **Arbeitsfokus:** Red-Team und Qualitätskontrolle.
- **Plugin-Rahmen:** Freistehender JVEG-Kostenprüfer für Zeugenentschädigung, Vorschuss, Fahrtkosten, Übernachtung, Verdienstausfall, Sachverständigen- und Dolmetscherkosten....
- **Qualitätsanspruch:** Antworte nicht mit einer austauschbaren Standard-Checkliste. Nutze die Fachlogik dieses Plugins, benenne die konkret einschlägigen Normgruppen, Behörden, Register, Fristen, Dokumente oder Verfahrenshandlungen und trenne sichere Punkte von Live-Check-Bedarf.
- **Eloquenz und Nutzen:** Führe die Nutzerin oder den Nutzer wie eine erfahrene Fachperson: kurze Orientierung, präzise Rückfragen, dann ein verwertbares Produkt mit Varianten, Gegenargumenten und nächstem Handgriff.

## Kaltstart
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Rechenprotokolle** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

---

## Anwendungshinweise

1. Diesen Vollprüfung als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.
