# Vollprüfung: arbeitszeugnis-analyse

## Zusammensetzung

Diese Vollprüfung enthält top-15 von 50 Skills des Plugins `arbeitszeugnis-analyse`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Wenn es um Einstieg und Routing in Arbeitszeugnis-Analyse geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden n…
2. **kaltstart-triage** — Wenn es um Kaltstart Triage in Arbeitszeugnis-Analyse geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächs…
3. **widerspruechliche-bewertungen** — Wenn es um Widersprüchliche Bewertungen erkennen und kommentieren in Arbeitszeugnis-Analyse geht: ordnet Sachverhalt, No…
4. **bereichs-drift-detektor** — Wenn es um Bereichs-Drift-Detektor (Schaufenster-Pattern) in Arbeitszeugnis-Analyse geht: ordnet Sachverhalt, Norm, Bewe…
5. **arbeitszeugnis-ampelsystem-dokumentenmatrix-lueckenliste** — Wenn es um Ampelsystem: Dokumentenmatrix, Lückenliste und Nachforderung in Arbeitszeugnis-Analyse geht: zerlegt Ergebnis…
6. **arbeitszeugnis-zeugnisanalyse-wortlaut-codes** — Wenn es um Arbeitszeugnisse: Fristen, Form, Zuständigkeit und Rechtsweg in Arbeitszeugnis-Analyse geht: zerlegt Ergebnis…
7. **arbeitszeugnis-orange-risikoampel-gegenargumente** — Wenn es um Orange: Risikoampel, Gegenargumente und Verteidigungslinien in Arbeitszeugnis-Analyse geht: zerlegt Ergebnis,…
8. **arbeitszeugnis-deutscher-tatbestandsmerkmale-beweisfragen** — Wenn es um Deutscher: Tatbestandsmerkmale, Beweisfragen und Beleglage in Arbeitszeugnis-Analyse geht: zerlegt Ergebnis, …
9. **muster-arbeitszeugnis-gemischte-noten** — Wenn es um Muster-Arbeitszeugnis mit gemischten Noten (Schulungsmaterial) in Arbeitszeugnis-Analyse geht: prüft Frist, F…
10. **rechtliche-bewertung-bag-rechtsprechung** — Wenn es um Rechtliche Bewertung und BAG-Rechtsprechung zum Arbeitszeugnis in Arbeitszeugnis-Analyse geht: prüft Frist, F…
11. **erstpruefung-rollenklaerung-mandatsziel** — Wenn es um Analyse: Erstprüfung, Rollenklärung und Mandatsziel in Arbeitszeugnis-Analyse geht: klärt Rolle, Ziel, Frist,…
12. **klage-strategie-zeugnisberichtigung** — Wenn es um Klagestrategie Zeugnisberichtigung in Arbeitszeugnis-Analyse geht: erstellt den passenden Entwurf aus Sachver…
13. **zeugnis-problem-sortieren** — Wenn es um Zeugnisproblem Sortieren in Arbeitszeugnis-Analyse geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente…
14. **arbeitszeugnis-geheimcodes-schriftsatz-brief-memo-bausteine** — Wenn es um Geheimcodes: Schriftsatz-, Brief- und Memo-Bausteine in Arbeitszeugnis-Analyse geht: erstellt den passenden E…
15. **muster-arbeitszeugnis-mit-roten-flaggen** — Wenn es um Muster-Arbeitszeugnis mit roten Flaggen (Schulungsmaterial) in Arbeitszeugnis-Analyse geht: prüft Frist, Form…

---

## Skill: `einstieg-routing`

_Wenn es um Einstieg und Routing in Arbeitszeugnis-Analyse geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Arbeitszeugnis Analyse** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `ampelsystem-tabellenausgabe` — Ampelsystem Tabellenausgabe
- `arbeitszeugnis-ampelsystem-dokumentenmatrix-lueckenliste` — Arbeitszeugnis Ampelsystem Dokumentenmatrix Lueckenliste
- `arbeitszeugnis-codeworte-compliance-dokumentation-aktenvermerk` — Arbeitszeugnis Codeworte Compliance Dokumentation Aktenvermerk
- `arbeitszeugnis-deutscher-tatbestandsmerkmale-beweisfragen` — Arbeitszeugnis Deutscher Tatbestandsmerkmale Beweisfragen
- `arbeitszeugnis-geheimcodes-schriftsatz-brief-memo-bausteine` — Arbeitszeugnis Geheimcodes Schriftsatz Brief Memo Bausteine
- `arbeitszeugnis-gruen-behoerden-gerichts-registerweg` — Arbeitszeugnis Gruen Behoerden Gerichts Registerweg
- `arbeitszeugnis-negative-zahlen-schwellenwerte-berechnung` — Arbeitszeugnis Negative Zahlen Schwellenwerte Berechnung
- `arbeitszeugnis-orange-risikoampel-gegenargumente` — Arbeitszeugnis Orange Risikoampel Gegenargumente
- `arbeitszeugnis-schaufenster-verhandlung-vergleich-eskalation` — Arbeitszeugnis Schaufenster Verhandlung Vergleich Eskalation
- `arbeitszeugnis-zeugnisanalyse-wortlaut-codes` — Arbeitszeugnis Zeugnisanalyse Wortlaut Codes
- `aufforderungsschreiben-arbeitgeber` — Aufforderungsschreiben Arbeitgeber
- `azubi-zeugnis-analyse` — Azubi Zeugnis Analyse
- `bereichs-drift-detektor` — Bereichs Drift Detektor
- `dokumente-intake` — Dokumente Intake
- `output-waehlen` — Output Waehlen

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Arbeitszeugnis Analyse sind die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.


## Leitentscheidungs-Anker (Übersicht, vor Schriftsatzverwendung live verifizieren)

> Diese Entscheidungen sind als Sucheinstieg gepflegt. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle (`bundesarbeitsgericht.de`, `dejure.org`, Rechtsprechungsportal des Bundes) live verifizieren - Datum, Aktenzeichen, Randnummer, Fortgeltung.

| Entscheidung | Tragende Aussage | Freie Quelle |
| --- | --- | --- |
| **BAG, Urt. v. 14.10.2003 - 9 AZR 12/03** | Zur vollen Zufriedenheit bescheinigt durchschnittliche Leistung (Note 3); Beweislast für bessere Note beim Arbeitnehmer, für schlechtere beim Arbeitgeber. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 18.11.2014 - 9 AZR 584/13** | "Befriedigend" als Mitte der Skala; Arbeitnehmer traegt Beweislast für bessere Note; Branchenueblichkeit guter Noten verschiebt die Beweislast nicht. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 20.02.2001 - 9 AZR 44/00** | Beginn der staendigen Linie: kein Anspruch auf Schlussformel mit Dank und guten Wuenschen; Fehlen kein unzulaessiges Geheimzeichen. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 11.12.2012 - 9 AZR 227/11** | Kein Anspruch auf Dank/Wuensche; bei unzufriedener Mandantschaft mit erteilter Schlussformel ist nur ein Zeugnis OHNE Schlussformel einklagbar - keine Umformulierung. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 25.01.2022 - 9 AZR 146/21** | Bestaetigung der Linie; Abwaegung mit Meinungsfreiheit des Arbeitgebers (Art. 5 I GG). | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 06.06.2023 - 9 AZR 272/22** | Massregelungsverbot $ 612a BGB: eine einmal erteilte Dankes-/Wunschformel darf nicht in spaeterer Fassung gestrichen werden, nur weil der Arbeitnehmer berechtigte Änderungswuensche geltend gemacht hat. | bundesarbeitsgericht.de / dejure.org |


## Sofortstart und Rueckfrage-Disziplin

**Der häufigste Fall ist der einfachste: jemand fuegt ein Zeugnis ein - sonst nichts.** Dann gilt:

1. **Sofort loslegen.** Fuegt der Nutzer nur ein Zeugnis ein (Text, PDF, Foto), ohne Anweisung, laeuft ohne Nachfrage die **Vollanalyse**: Kopfdaten, Einschaetzungsmatrix, Drift-/Auslassungspruefung, Gesamtnotenspanne, Handlungsempfehlung.
2. **Fehlende Angaben sind kein Blocker.** Was das Intake nicht hergibt, wird aus dem Zeugnis selbst abgeleitet (Position, Branche, Beendigungsanlass, Zeugnisart) und als **gekennzeichnete Annahme** gefuehrt ("Annahme: Vertriebsposition mit Kundenkontakt - bitte korrigieren, falls falsch.").
3. **Hoechstens eine Rueckfrage**, und nur bei echtem Verstaendnisblocker (Text unleserlich, zwei Zeugnisse vermischt, Sprache unklar). Mehrere offene Punkte in **eine einzige gebuendelte Rueckfrage** packen - niemals seriell nachfragen.
4. **Wuenschefragen ans Ende.** Ob der Nutzer auch ein Aufforderungsschreiben oder eine Klagestrategie will, wird nicht vorab gefragt, sondern am Schluss der Analyse als Option angeboten ("Auf Wunsch erstelle ich daraus das Aufforderungsschreiben.").
5. **Rollenvermutung:** Ohne anderslautende Angabe wird angenommen, dass der Einsender die beurteilte Person ist (Arbeitnehmerperspektive).

---

## Skill: `kaltstart-triage`

_Wenn es um Kaltstart Triage in Arbeitszeugnis-Analyse geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten._

## Wenn nur ein Zeugnis hochgeladen wird

Wenn der Nutzer nur ein PDF, Foto, Screenshot oder Textauszug hochlädt, beginne direkt. Keine generische Empfangsbestätigung, keine lange Intake-Liste.

**Erste Antwort:**

- **Erkannt:** Zeugnisart, Arbeitgeber, Arbeitnehmer, Zeitraum, Datum, Seitenumfang, soweit sichtbar.
- **Eilt:** Verjährung, Ausschlussfrist, laufende Bewerbung, Vergleichsfrist, bevorstehender Gerichtstermin oder `keine Eilfrist erkennbar`.
- **Erster Eindruck:** nicht als Endnote, sondern als Arbeitshypothese: freundlich-glatt, auffällig knapp, gemischt, streitig, lückenhaft, auffällig codiert.
- **Primärer Pfad:** ein passender Fachmodul aus diesem Plugin mit einem Satz, warum gerade dieser Skill jetzt trägt.
- **Nächster Schritt:** direkt weiterarbeiten oder genau eine konkrete Rückfrage stellen.

## Intake in 60 Sekunden

Frage nur, was den Weg ändert. Wenn die Information schon im Material steht, fasse sie zusammen und frage nicht erneut.

| Punkt | Frage |
|---|---|
| Rolle | Arbeitnehmer, Anwalt/Kanzlei, Betriebsrat, Arbeitgeber, Personalabteilung oder Rechtsabteilung? |
| Ziel | Nur verstehen, nachverhandeln, Arbeitgeber anschreiben, Klage prüfen, Vergleichstext bauen oder Schulungsfall analysieren? |
| Zeugnisart | Einfaches Zeugnis, qualifiziertes Endzeugnis, Zwischenzeugnis, Ausbildungszeugnis oder Entwurf? |
| Zeitpunkt | Wann ausgestellt, wann erhalten, gibt es Bewerbungs- oder Vergleichsdruck? |
| Kontext | Kündigung, Aufhebungsvertrag, Eigenkündigung, Elternzeit, Wechsel, Ruhestand, Streit oder gute Trennung? |
| Vergleichsmaterial | Vorzeugnis, Zwischenzeugnis, Beurteilungen, Zielvereinbarungen, Bonusunterlagen, E-Mails mit Lob, Vergleichstext? |

## Fünf Arbeitswege

Wähle einen dieser Wege und sage dem Nutzer, welchen Weg du nimmst.

1. **Schnellscan:** Für eine erste Einschätzung. Nutze `zeugnisart-erkennung`, `zeugnis-überblick-extraktion`, `zufriedenheitsformel-decodierung` und `schlussformel-bewertung`.
2. **Vollanalyse:** Für belastbare Mandatsarbeit. Nutze zusätzlich `notenrelevante-saetze-identifizieren`, `satzweise-notenmatrix`, `leistungsbeurteilung-analyse`, `verhaltensbeurteilung-analyse`, `steigerungsadverbien-katalog`, `bereichs-drift-detektor`, `widerspruechliche-bewertungen` und `gesamtnoten-aggregation`.
3. **Verhandlung:** Wenn ein besseres Zeugnis erreicht werden soll. Nutze `verbesserungsvorschlaege-formulieren`, `mandantenbericht-zeugnisanalyse` und danach `aufforderungsschreiben-arbeitgeber`.
4. **Klageprüfung:** Wenn der Arbeitgeber nicht korrigiert oder ein Vergleich gescheitert ist. Nutze `rechtliche-bewertung-bag-rechtsprechung` und `klage-strategie-zeugnisberichtigung`.
5. **Sonderfall:** Bei Führungskräften, Ausbildung oder branchentypischen Codes nutze früh `leitende-positionen-zeugnisse`, `azubi-zeugnis-analyse` oder `branchen-spezifische-formulierungen`.

## Routing nach Befund

| Befund | Nächster Skill | Warum |
|---|---|---|
| Zeugnisart oder Kopfdaten unklar | `zeugnisart-erkennung`, `zeugnis-überblick-extraktion` | Erst wissen, welches Dokument geprüft wird. |
| Hauptnote unklar | `zufriedenheitsformel-decodierung`, `satzweise-notenmatrix` | Die Kernformel allein reicht oft nicht. |
| Viele scheinbar gute Sätze, aber komisches Gefühl | `bereichs-drift-detektor`, `widerspruechliche-bewertungen` | Schaufenster-Sätze und Brüche im Gesamtbild erkennen. |
| Fehlendes Bedauern, knapper Dank, kalter Schluss | `schlussformel-bewertung` | Signalwirkung und rechtliche Durchsetzbarkeit getrennt bewerten. |
| Wörter wie "bemüht", "korrekt", "gesellig", "im Großen und Ganzen" | `rote-flaggen-katalog`, `negative-codeworte-katalog` | Kodierte Abwertung herausarbeiten. |
| Zeugnis einer Führungskraft | `leitende-positionen-zeugnisse` | Führung, Budget, Strategie und Loyalität gesondert prüfen. |
| Zeugnis soll verbessert werden | `verbesserungsvorschlaege-formulieren` | Konkrete Ersatzformulierungen bauen, aber nur soweit belegbar. |
| Arbeitgeber soll angeschrieben werden | `aufforderungsschreiben-arbeitgeber` | Beanstandungen in verwertbare Korrespondenz übersetzen. |
| Gerichtliche Durchsetzung steht im Raum | `rechtliche-bewertung-bag-rechtsprechung`, `klage-strategie-zeugnisberichtigung` | Beweislast, Antrag und Kostenrisiko sauber trennen. |

## Juristische Leitplanken

- **Paragraf 109 GewO:** Anspruch auf einfaches oder qualifiziertes Zeugnis; bei qualifiziertem Zeugnis Angaben zu Leistung und Verhalten.
- **Paragraf 16 BBiG:** Ausbildungszeugnis; auf Verlangen auch Angaben zu Verhalten und Leistung.
- **Wahrheit vor Wohlwollen:** Ein gutes Zeugnis darf nicht unwahr sein. Wohlwollen steuert die Ausdrucksweise, ersetzt aber keine Tatsachen.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Geheimcode:** Nicht jede unglückliche Formulierung ist automatisch ein unzulässiger Code. Prüfe den objektiven Empfängerhorizont und den Gesamtzusammenhang.
- **Keine Mathematik-Illusion:** Ampel, Note und Drift sind Arbeitsinstrumente. Die Ausgabe muss als begründete Spanne erscheinen, nicht als Scheingenauigkeit.

## Antwortformate

### Kurzscan

**Kurzbild**
- Zeugnisart:
- Erste Notentendenz:
- Kritische Stellen:
- Eilt wegen:

**Nächster sinnvoller Skill**
Wähle nach Aktenlage den nächsten passenden Skill und begründe in einem Satz, welche Frist, Zuständigkeit, Beweislast oder welches Arbeitsprodukt dadurch geklärt wird.

### Vollanalyse

**Arbeitsplan**
1. Kopfdaten und Zeugnisart sichern.
2. Notenrelevante Sätze markieren.
3. Leistung, Verhalten, Schluss und Auslassungen getrennt bewerten.
4. Drift und Widersprüche prüfen.
5. Gesamtnotenspanne bilden.
6. Handlungsoptionen und konkrete Ersatzformulierungen ausgeben.

**Fachmodule**
Nenne zwei bis fünf Skills, nicht die ganze Plugin-Liste. Zu jedem Skill: Input, Zweck, Output.

### Mandatsoutput

Wenn der Nutzer anwaltliche Weiterverarbeitung will, liefere:

- Zusammenfassung für Mandant oder Mandantin.
- Streitstellen mit Originalwortlaut und gewünschter Neufassung.
- Beweislast und Belegbedarf pro Streitstelle.
- Empfehlung: akzeptieren, nachverhandeln, auffordern, klagen oder Vergleich nutzen.

## Qualitätsgate

Vor jeder abschließenden Antwort prüfe:

- Sind Umlaute, ß, Namen, Daten und Zitate sauber übernommen?
- Ist die Zeugnisart korrekt bestimmt?
- Sind Schlussformel-Signal und Schlussformel-Anspruch getrennt?
- Ist die Beweislast richtig herum dargestellt?
- Gibt es keine erfundenen Fundstellen, Zeugnisinhalte oder Noten?
- Sind die vorgeschlagenen Skills wirklich aus diesem Plugin?
- Wirkt das Ergebnis wie eine verwendbare anwaltliche Arbeitsfassung und nicht wie ein Schema?

## Testakten nutzen

Für Schulung und Regression eignet sich die Arbeitsakte `arbeitszeugnis-analyse-bluehendes-leben`. Nutze sie nicht als vorgefertigte Lösung, sondern als lebendiges Material: erst lesen, dann Hypothese bilden, dann mit den Fachmodule absichern. Die Fälle sollen zeigen, dass Arbeitszeugnisse oft höflich aussehen und trotzdem in einzelnen Abschnitten hart abwerten.


## Leitentscheidungs-Anker (Übersicht, vor Schriftsatzverwendung live verifizieren)

> Diese Entscheidungen sind als Sucheinstieg gepflegt. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle (`bundesarbeitsgericht.de`, `dejure.org`, Rechtsprechungsportal des Bundes) live verifizieren - Datum, Aktenzeichen, Randnummer, Fortgeltung.

| Entscheidung | Tragende Aussage | Freie Quelle |
| --- | --- | --- |
| **BAG, Urt. v. 14.10.2003 - 9 AZR 12/03** | Zur vollen Zufriedenheit bescheinigt durchschnittliche Leistung (Note 3); Beweislast für bessere Note beim Arbeitnehmer, für schlechtere beim Arbeitgeber. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 18.11.2014 - 9 AZR 584/13** | "Befriedigend" als Mitte der Skala; Arbeitnehmer traegt Beweislast für bessere Note; Branchenueblichkeit guter Noten verschiebt die Beweislast nicht. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 20.02.2001 - 9 AZR 44/00** | Beginn der staendigen Linie: kein Anspruch auf Schlussformel mit Dank und guten Wuenschen; Fehlen kein unzulaessiges Geheimzeichen. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 11.12.2012 - 9 AZR 227/11** | Kein Anspruch auf Dank/Wuensche; bei unzufriedener Mandantschaft mit erteilter Schlussformel ist nur ein Zeugnis OHNE Schlussformel einklagbar - keine Umformulierung. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 25.01.2022 - 9 AZR 146/21** | Bestaetigung der Linie; Abwaegung mit Meinungsfreiheit des Arbeitgebers (Art. 5 I GG). | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 06.06.2023 - 9 AZR 272/22** | Massregelungsverbot $ 612a BGB: eine einmal erteilte Dankes-/Wunschformel darf nicht in spaeterer Fassung gestrichen werden, nur weil der Arbeitnehmer berechtigte Änderungswuensche geltend gemacht hat. | bundesarbeitsgericht.de / dejure.org |


## Sofortstart und Rueckfrage-Disziplin

**Der häufigste Fall ist der einfachste: jemand fuegt ein Zeugnis ein - sonst nichts.** Dann gilt:

1. **Sofort loslegen.** Fuegt der Nutzer nur ein Zeugnis ein (Text, PDF, Foto), ohne Anweisung, laeuft ohne Nachfrage die **Vollanalyse**: Kopfdaten, Einschaetzungsmatrix, Drift-/Auslassungspruefung, Gesamtnotenspanne, Handlungsempfehlung.
2. **Fehlende Angaben sind kein Blocker.** Was das Intake nicht hergibt, wird aus dem Zeugnis selbst abgeleitet (Position, Branche, Beendigungsanlass, Zeugnisart) und als **gekennzeichnete Annahme** gefuehrt ("Annahme: Vertriebsposition mit Kundenkontakt - bitte korrigieren, falls falsch.").
3. **Hoechstens eine Rueckfrage**, und nur bei echtem Verstaendnisblocker (Text unleserlich, zwei Zeugnisse vermischt, Sprache unklar). Mehrere offene Punkte in **eine einzige gebuendelte Rueckfrage** packen - niemals seriell nachfragen.
4. **Wuenschefragen ans Ende.** Ob der Nutzer auch ein Aufforderungsschreiben oder eine Klagestrategie will, wird nicht vorab gefragt, sondern am Schluss der Analyse als Option angeboten ("Auf Wunsch erstelle ich daraus das Aufforderungsschreiben.").
5. **Rollenvermutung:** Ohne anderslautende Angabe wird angenommen, dass der Einsender die beurteilte Person ist (Arbeitnehmerperspektive).

---

## Skill: `widerspruechliche-bewertungen`

_Wenn es um Widersprüchliche Bewertungen erkennen und kommentieren in Arbeitszeugnis-Analyse geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen._

# Widersprüchliche Bewertungen erkennen und kommentieren

## Fachlicher Anker

- **Normen:** Paragraf 109 GewO; ergänzend Paragraf 630 BGB für nicht von Paragraf 109 GewO erfasste Dienstverhältnisse und Paragraf 16 BBiG für Auszubildende.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Geheimcode-Regeln

| Widerspruchstyp | Signalwirkung | Ampel |
|---|---|---|
| Leistung grün, Schlussformel rot | Uneinvernehmliche Trennung | Orange-Rot |
| Verhalten grün, Leistung rot | Netter, aber leistungsschwacher Mitarbeiter | Rot |
| Eigeninitiative und "nach Anweisung" im selben Zeugnis | Inkonsistenz | Orange |
| Sehr warme Schlussformel bei schwacher Leistungsbeurteilung | Verdacht auf Gefälligkeitsformel | Orange |
| Positive Einzelsätze, negative Gesamtzufriedenheitsformel | Bewusste Irreführung | Rot |
| Spitzensatz und Durchschnittssatz im selben Themenbereich | Schaufenster-Pattern (siehe bereichs-drift-detektor) | Rot |

## Beispiele

**Beispiel 1 – Leistung grün, Schlussformel rot:** "Die Leistungen waren stets hervorragend" (Grün) + keine Schlussformel (Rot) → deutet auf Streit beim Ausscheiden oder feindseligen Abgang.

**Beispiel 2 – Innere Inkonsistenz:** "Herr Braun arbeitete stets eigenverantwortlich" (Satz 3) vs. "Er erledigte die ihm nach Anweisung zugewiesenen Aufgaben zuverlässig" (Satz 7) → direkte inhaltliche Contradiction.

**Beispiel 3 – Warme Schlussformel bei Note-4-Leistung:** Leistung mit "bemüht" (Rot, Note 4), Schlussformel vollständig und warm → vermutlich persönliches Gefälligkeitszeugnis, nicht authentisch.

**Beispiel 4 – Reihenfolge-Anomalie:** Abschnitt 1 (Leistung): hervorragend. Abschnitt 2 (Verhalten): Kollegen vor Vorgesetzten + "direkte Kommunikationsweise". Abschnitt 3 (Schlussformel): vollständig. → Einstellender wird Verhaltensteil isoliert bewerten.

**Beispiel 5 – Positiver Leistungsteil, fehlende Integrität:** Alle Leistungsaussagen grün, kein einziges Wort zu Zuverlässigkeit oder Vertrauen bei einem Buchhalter → der Widerspruch zwischen Lob und Schweigen ist das rote Signal.

## Rechtliche Einordnung und Normen

- **Paragraf 109 GewO** — Anspruch auf qualifiziertes wohlwollendes Zeugnis
- **Paragraf 109 Abs. 2 GewO** — Klarheits- und Wahrheitspflicht; kodierte Negativaussagen unzulässig

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.


## Leitentscheidungs-Anker (Empfaengerhorizont, Grenzen der Decodierung)

> Diese Entscheidungen sind als Sucheinstieg gepflegt. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle (`bundesarbeitsgericht.de`, `dejure.org`, Rechtsprechungsportal des Bundes) live verifizieren - Datum, Aktenzeichen, Randnummer, Fortgeltung.

| Entscheidung | Tragende Aussage | Freie Quelle |
| --- | --- | --- |
| **BAG, Urt. v. 21.06.2005 - 9 AZR 352/04** | Gebot der Zeugnisklarheit ($ 109 II GewO): massgeblich ist der objektive Empfaengerhorizont, nicht die Absicht des Arbeitgebers. "Kennen gelernt" allein ist kein Geheimcode. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 15.11.2011 - 9 AZR 386/10** | Bestaetigung: "kennen gelernt" ist allein und losgeloest vom uebrigen Zeugnisinhalt kein unzulaessiger Geheimcode; Werturteile-Spielraum mit Grenze Zeugniswahrheit/-klarheit. | bundesarbeitsgericht.de / dejure.org |

---

## Skill: `bereichs-drift-detektor`

_Wenn es um Bereichs-Drift-Detektor (Schaufenster-Pattern) in Arbeitszeugnis-Analyse geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen._

# Bereichs-Drift-Detektor (Schaufenster-Pattern)

## Fachlicher Anker

- **Normen:** Paragraf 109 GewO; ergänzend Paragraf 630 BGB für nicht von Paragraf 109 GewO erfasste Dienstverhältnisse und Paragraf 16 BBiG für Auszubildende.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Geheimcode-Regeln

| Drift-Befund | Signalwirkung | Ampel |
|---|---|---|
| Note eins und Note drei zum selben Themenbereich direkt aufeinanderfolgend | Schaufenster-Eroeffnung mit kodierter Korrektur | Rot |
| Spreizung zwei Stufen innerhalb eines Bereichs | Systematische Abwertung | Rot |
| Spreizung eine Stufe innerhalb eines Bereichs | Bewusste Vorsicht | Orange |
| Drift bei Lernbereitschaft trotz starker Fachkenntnisse | Stagnationssignal | Rot |
| Drift bei Sozialverhalten trotz starker Leistungsteile | Konfliktsignal | Rot |
| Drift bei Innovation trotz starker Arbeitsweise | Routinesignal | Orange |
| Bereichsuebergreifend konstante Note eins | Authentisch grün | Grün |

## Beispiele

**Beispiel 1 – Klassische Schaufenster-Drift bei Lernbereitschaft:** Satz A: "verfuegt auch in Randbereichen seines vielfaeltigen Aufgabenbereiches über aeusserst profundes Fachwissen" (Note 1). Satz B unmittelbar darauf: "nahm in eigener Initiative regelmaessig erfolgreich an internen und externen Weiterbildungsseminaren teil" (Note 3). Beide gehoeren zum Themenbereich Fachwissen/Lernen. Drift zwei Stufen, Rot.

**Beispiel 2 – Drift bei Arbeitsweise und Innovation:** Satz A: "fuehrte er jederzeit vollkommen selbststaendig, aeusserst sorgfaeltig und planvoll durchdacht aus" (Note 1). Satz B: "war Neuem gegenueber aufgeschlossen, fand gute neue Ideen und innovative Ansaetze" (Note 3, da "gute" statt "hervorragende" und keine Steigerungsadverbien). Drift zwei Stufen im weichen Bereich, Rot.

**Beispiel 3 – Drift im Sozialverhalten trotz Top-Erfolg:** Satz A: "Arbeitsergebnisse lagen stets sehr weit über unseren Anforderungen" (Note 1). Satz B im Sozialteil: "war ein geschaetzter Ansprechpartner, sein persönliches Verhalten war einwandfrei" (Note 3, da "einwandfrei" ohne "stets" und "geschaetzt" ohne Steigerung). Themen unterschiedlich, aber Drift in einem heiklen Bereich, Rot.

**Beispiel 4 – Drift eine Stufe:** "aeusserst motiviert die gesetzten Ziele beharrlich zu verfolgen" (Note 1) und kurz darauf "zeigte eine hohe Lernbereitschaft" (Note 2 bis 3). Eine Stufe, Orange.

**Beispiel 5 – Keine Drift, authentisch:** Alle Saetze im Bereich Fachkenntnisse tragen durchgehend Steigerungsadverbien und Superlative auf Note-1-Niveau. Keine Drift, Grün.

## Rechtliche Einordnung und Normen

- **Paragraf 109 Abs. 2 GewO** — Zeugnis muss klar und verständlich sein; widersprüchliche Bewertungen im selben Themenbereich verstoßen gegen Wohlwollensgebot
- **Paragraf 242 BGB** — Treu und Glauben; innerhalb desselben Zeugnisabschnitts darf der Arbeitgeber nicht gleichzeitig Bestnoten und Mängel bescheinigen

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Triage — vor der Drift-Prüfung

1. Welche Themenblöcke sind im Zeugnis enthalten? (Fachkenntnisse, Motivation, Qualität, Teamverhalten, Führung, Schluss)
2. Wurde die Zufriedenheitsformel bereits ausgewertet? (Satzweise-Notenmatrix-Skill?)
3. Ziel der Drift-Analyse: Klageantrag-Vorbereitung oder Mandantenberatung?


## Leitentscheidungs-Anker (Empfaengerhorizont, Grenzen der Decodierung)

> Diese Entscheidungen sind als Sucheinstieg gepflegt. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle (`bundesarbeitsgericht.de`, `dejure.org`, Rechtsprechungsportal des Bundes) live verifizieren - Datum, Aktenzeichen, Randnummer, Fortgeltung.

| Entscheidung | Tragende Aussage | Freie Quelle |
| --- | --- | --- |
| **BAG, Urt. v. 21.06.2005 - 9 AZR 352/04** | Gebot der Zeugnisklarheit ($ 109 II GewO): massgeblich ist der objektive Empfaengerhorizont, nicht die Absicht des Arbeitgebers. "Kennen gelernt" allein ist kein Geheimcode. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 15.11.2011 - 9 AZR 386/10** | Bestaetigung: "kennen gelernt" ist allein und losgeloest vom uebrigen Zeugnisinhalt kein unzulaessiger Geheimcode; Werturteile-Spielraum mit Grenze Zeugniswahrheit/-klarheit. | bundesarbeitsgericht.de / dejure.org |

---

## Skill: `arbeitszeugnis-ampelsystem-dokumentenmatrix-lueckenliste`

_Wenn es um Ampelsystem: Dokumentenmatrix, Lückenliste und Nachforderung in Arbeitszeugnis-Analyse geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Ampelsystem: Dokumentenmatrix, Lückenliste und Nachforderung

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `Paragraf 611a Abs. 1 BGB` — Arbeitsvertrag und Weisungsbindung.
- `Paragraf 241 Abs. 2 BGB` — Rücksichtnahmepflichten.
- `Paragraf 626 Abs. 1 BGB` — fristlose Kuendigung.
- `Paragraf 1 Abs. 2 KSchG` — soziale Rechtfertigung.
- `Paragraf 4 Satz 1 KSchG` — Klagefrist.
- `Paragraf 7 KSchG` — Fiktionswirkung.
- `Paragraf 102 Abs. 1 BetrVG` — Betriebsratsanhoerung.
- `Paragraf 2 Abs. 1 NachwG` — Nachweis wesentlicher Arbeitsbedingungen.
- `Paragraf 46 Abs. 2 ArbGG` — ZPO-Anwendung im arbeitsgerichtlichen Verfahren.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Fachlicher Anker

- **Normen:** Paragraf 109 GewO; ergänzend Paragraf 630 BGB für nicht von Paragraf 109 GewO erfasste Dienstverhältnisse und Paragraf 16 BBiG für Auszubildende.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Spezialwissen: Ampelsystem: Dokumentenmatrix, Lückenliste und Nachforderung
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Ampelsystem** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Ampelsystem-Notenmatrix (Auszug)

| Formulierung | Bereich | Ampel | Note |
| --- | --- | --- | --- |
| stets zur vollsten Zufriedenheit | Leistung | Grün | 1 |
| stets zur vollen Zufriedenheit | Leistung | Grün | 2 |
| zur vollen Zufriedenheit | Leistung | Orange | 3 |
| stets zur Zufriedenheit | Leistung | Orange-Rot | 3-4 |
| zur Zufriedenheit | Leistung | Rot | 4 |
| war stets bemüht | Leistung | Rot | 4-5 |
| im Wesentlichen / im Großen und Ganzen zur Zufriedenheit | Leistung | Rot | 5 |
| stets einwandfrei | Verhalten | Grün | 1 |
| einwandfrei / korrekt | Verhalten | Orange | 3 |
| korrekt gegenüber Kollegen UND Vorgesetzten (Reihenfolge!) | Verhalten | Orange-Rot | falsche Reihenfolge = Note 3-4 |
| Schlussformel mit Bedauern, Dank, Zukunftswünschen | Schluss | Grün | wärmend |
| Schlussformel ohne Bedauern | Schluss | Orange-Rot | kühl |
| Auslassung relevanter Aufgaben (z.B. Kunden trotz Vertriebsjob) | Aufgaben | Rot | Indizwirkung |

## Dokumentenmatrix für Lückenanalyse

| Pflichtbaustein | Im Zeugnis vorhanden? | Ampel | Wirkung |
| --- | --- | --- | --- |
| Briefkopf (Unternehmen, Anschrift) | ja/nein | bei Fehlen Rot | Formfehler |
| Persönliche Daten (Name, Geb-Datum, ggf. Anschrift) | ja/nein | nein = Rot | Identitätszweifel |
| Eintritts- und Austrittsdatum | ja/nein | Pflicht | Klarheit Beschäftigungszeitraum |
| Stellenbezeichnung und Aufgabenkatalog | vollständig? | Lücken = Rot | bei Auslassungen Indizwirkung |
| Leistungsbeurteilung | vorhanden, vollständig? | Lücken = Rot | "stillschweigende Schlechtbewertung" |
| Verhaltensbeurteilung | vorhanden, Reihenfolge der Personennennung? | Reihenfolge entscheidend | Vorgesetzte zuerst, dann Mitarbeiter, Kollegen, Kunden |
| Schlussformel | mit Bedauern, Dank, Zukunftswünschen? | fehlend = Orange-Rot | Kontextsignal |
| Unterschrift (Geschäftsführung/HR) | ja, mit Funktion? | Rangsignal | je höher, desto wertvoller |
| Ausstellungsdatum | sinnvoll vor Beendigung? | nach Beendigung normal | sehr lange nach Beendigung = Indizwirkung |

## Lückenliste / Nachforderung

Typische Nachforderungen an den Arbeitgeber:
1. Erweiterung des Aufgabenkatalogs (insbesondere fehlende Kundenbetreuung bei Vertriebsmitarbeitern).
2. Hinzufügung quantifizierter Erfolge (Umsatzsteigerung, Projektabschlüsse, Auszeichnungen).
3. Verbesserung der Note auf "stets zur vollen Zufriedenheit" (Note 2) mit Beurteilungsbeiträgen als Belegen.
4. Verhaltensformel mit "stets einwandfrei" und korrekter Personennennung (Vorgesetzte zuerst).
5. Warme Schlussformel mit Bedauern, Dank und Zukunftswünschen.
6. Korrektur Auslassungen — Stellung im Unternehmen, Verantwortungsumfang, Disziplinarbefugnis.

## Praktiker-Tipp

Bei Note 3 trägt Arbeitnehmer die Beweislast für bessere Note (BAG ständige Rechtsprechung). Daher Klage auf Note 2 nur bei vollständig dokumentierten Beurteilungsbeiträgen. Sonst lieber Vergleich in der Güteverhandlung: typisches Kompromisspaket: "stets zur vollen Zufriedenheit", "stets einwandfrei", warme Schlussformel.

---

## Skill: `arbeitszeugnis-zeugnisanalyse-wortlaut-codes`

_Wenn es um Arbeitszeugnisse: Fristen, Form, Zuständigkeit und Rechtsweg in Arbeitszeugnis-Analyse geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Arbeitszeugnisse: Fristen, Form, Zuständigkeit und Rechtsweg

## Fachlicher Anker

- **Normen:** Paragraf 109 GewO; ergänzend Paragraf 630 BGB für nicht von Paragraf 109 GewO erfasste Dienstverhältnisse und Paragraf 16 BBiG für Auszubildende.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Spezialwissen: Arbeitszeugnisse: Fristen, Form, Zuständigkeit und Rechtsweg
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Anspruch und Form:** Paragraf 109 GewO Anspruch auf schriftliches Zeugnis bei Beendigung; Paragraf 109 Abs. 2 Satz 1 GewO Schriftform (eigenhändige Unterschrift); elektronische Form ausdrücklich ausgeschlossen Paragraf 109 Abs. 3 GewO. Anspruch auf einfaches oder qualifiziertes Zeugnis (Wahlrecht des Arbeitnehmers).
3. **Fristen prüfen:** Zeugnisanspruch verjährt regelmäßig nach 3 Jahren (Paragrafen 195, 199 BGB). Vorsicht: tarifliche oder einzelvertragliche Ausschlussfristen (häufig 2- bis 6-monatig, zweistufig) verkürzen Anspruch erheblich; Mindestlohnverwirkungsklauseln BAG ständige Rechtsprechung unwirksam. Bei Zwischenzeugnis: Anspruch bei berechtigtem Interesse (Vorgesetztenwechsel, Bewerbung, Beförderung).
4. **Zuständigkeit:** ArbG erstinstanzlich (Paragraf 2 Abs. 1 Nr. 3a ArbGG); Streitwert ein Bruttomonatsgehalt analog Paragraf 42 Abs. 2 GKG; keine Anwaltspflicht erste Instanz (Paragraf 11 ArbGG); Klagegegner ist Arbeitgeber, bei Betriebsübergang nach Paragraf 613a BGB der Erwerber.
5. **Anschluss:** Aufforderungsschreiben mit Fristsetzung (2-4 Wochen üblich), bei Untätigkeit Klage; Antrag konkretisieren ("verurteilt, ein qualifiziertes Arbeitszeugnis mit folgendem Inhalt zu erteilen ..." oder unbestimmter Antrag mit Notenangabe).

---

## Skill: `arbeitszeugnis-orange-risikoampel-gegenargumente`

_Wenn es um Orange: Risikoampel, Gegenargumente und Verteidigungslinien in Arbeitszeugnis-Analyse geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Orange: Risikoampel, Gegenargumente und Verteidigungslinien

## Fachlicher Anker

- **Normen:** Paragraf 109 GewO; ergänzend Paragraf 630 BGB für nicht von Paragraf 109 GewO erfasste Dienstverhältnisse und Paragraf 16 BBiG für Auszubildende.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Spezialwissen: Orange: Risikoampel, Gegenargumente und Verteidigungslinien
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Orange-Phänomene identifizieren:** Stille (fehlende Aussage zu wesentlichen Tätigkeitsmerkmalen), Schaufenster-Drift (positive Auftaktphrase ohne inhaltliche Substanz), abgeschwächte Steigerungsadverbien ("im Wesentlichen", "weitgehend"), fehlende Schlussformel (Dank/Bedauern/Zukunftswünsche).
3. **Gegenargumente Arbeitgeberseite prüfen:** Paragraf 109 GewO Pflicht zu Wahrheit + Wohlwollen; BAG ständige Rechtsprechung: Wohlwollensgebot tritt nur dort zurück, wo der Wahrheitsgehalt es zwingend erfordert. Arbeitgeber muss Verfehlungen darlegen und beweisen, die schlechtere Bewertung tragen.
4. **Risikoampel:** Orange wenn 2 oder mehr Schwachstellen kumulieren ohne klares Notenwort (Note unklar zwischen 3 und 4); Rot bei expliziten Negativcodes (z.B. "bemüht", "kennt seine Pflichten"); Grün bei klarer Notenformel und vollständiger Schlussformel.
5. **Verteidigungslinien Arbeitnehmer:** Mit Beurteilungen aus Mitarbeitergesprächen, E-Mail-Lob, Bonusabrechnungen und Beförderungen gegenargumentieren. Vergleich vor Klage: Notenkompromiss "gut" statt "sehr gut" oft besser als ungewisser Prozess.

---

## Skill: `arbeitszeugnis-deutscher-tatbestandsmerkmale-beweisfragen`

_Wenn es um Deutscher: Tatbestandsmerkmale, Beweisfragen und Beleglage in Arbeitszeugnis-Analyse geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Deutscher: Tatbestandsmerkmale, Beweisfragen und Beleglage

## Fachlicher Anker

- **Normen:** Paragraf 109 GewO; ergänzend Paragraf 630 BGB für nicht von Paragraf 109 GewO erfasste Dienstverhältnisse und Paragraf 16 BBiG für Auszubildende.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Spezialwissen: Deutscher: Tatbestandsmerkmale, Beweisfragen und Beleglage
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Tatbestand Paragraf 109 GewO:** Anspruchsvoraussetzungen Arbeitsverhältnis, Beendigung oder berechtigtes Interesse (Zwischenzeugnis), Wahlrecht einfach/qualifiziert. Pflichtinhalt qualifiziertes Zeugnis: Art und Dauer der Tätigkeit, Leistungsbeurteilung, Verhaltensbeurteilung.
3. **Beweislastverteilung (BAG ständige Rechtsprechung):** Note "befriedigend" (3) ist Mittelmaß; bessere Note muss Arbeitnehmer darlegen und beweisen, schlechtere Note der Arbeitgeber. Beweislastregel ändert sich nicht durch Branchen-Durchschnittsnote oberhalb von 3.
4. **Belege sammeln:** Mitarbeitergespräche, Zielvereinbarungen, Bonusabrechnungen, schriftliches Lob (E-Mail, Karte), Beförderungen, Auszeichnungen, Kundenstimmen, Beurteilungen Dritter (Vorgesetzte, Projektleiter). Negativbelege: Abmahnungen, Krankenstand, Versetzungen, Konfliktdokumentation.
5. **Anschluss:** Aufforderungsschreiben mit Beleg-Anhang, dann Klage; alternativ Vergleich mit Notenkompromiss und Standard-Schlussformel.

---

## Skill: `muster-arbeitszeugnis-gemischte-noten`

_Wenn es um Muster-Arbeitszeugnis mit gemischten Noten (Schulungsmaterial) in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Muster-Arbeitszeugnis mit gemischten Noten (Schulungsmaterial)

## Fachlicher Anker

- **Normen:** Paragraf 109 GewO; ergänzend Paragraf 630 BGB für nicht von Paragraf 109 GewO erfasste Dienstverhältnisse und Paragraf 16 BBiG für Auszubildende.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Geheimcode-Regeln

| Satz im Muster | Themenbereich | Note | Befund |
|---|---|---|---|
| "verfuegt auch in Randbereichen über aeusserst profundes Fachwissen" | Fachkenntnisse | 1 | Steigerer plus Maximalbereich |
| "nahm regelmaessig erfolgreich an Weiterbildungsseminaren teil" | Lernbereitschaft | 3 | Kein Steigerungsadverb |
| "ausgeprägt strategisches Denkvermoegen, stets in kuerzester Zeit optimale Loesungen" | Strategisches Denken | 1 | "stets" plus Superlativ |
| "zeigte sich bei neuen Aufgabenbereichen flexibel und aufgeschlossen" | Flexibilitaet | 3 | "zeigte" ohne Steigerung |
| "besonders hohe Arbeitsmoral, stets aeusserst motiviert, beharrlich zu verfolgen" | Engagement | 1 | Drei Steigerer |
| "zeigte eine hohe Lernbereitschaft" | Lernbereitschaft | 3 | "hohe" ohne Adverb |
| "jederzeit vollkommen selbststaendig, aeusserst sorgfaeltig, planvoll durchdacht" | Arbeitsweise | 1 | Drei Steigerer |
| "fand gute neue Ideen und innovative Ansaetze" | Innovation | 3 | "gute" statt "hervorragende" |
| "Arbeitsergebnisse lagen stets sehr weit über unseren Anforderungen" | Arbeitsergebnis | 1 | Maximalvergleich |
| "war in der Lage, Konflikte erfolgreich zu bewaeltigen" | Sozialverhalten | 3 | "war in der Lage" |
| "vollsten Zufriedenheit erfuellt und teilweise sogar übertroffen" | Gesamtbeurteilung | 1 | Maximalformel |
| "geschaetzter Ansprechpartner, persönliches Verhalten war einwandfrei" | Sozialverhalten | 3 | "einwandfrei" ohne "stets" |
| "stets ausgezeichnete Mitarbeit" plus volles Bedauern und voller Dank | Schlussformel | 1 | Vollstaendig auf Spitze |

## Beispiele

### Vollstaendiges Muster-Schulungszeugnis

---

**Beispiel GmbH, Beispielstrasse 5, 20000 Beispielstadt**

**Arbeitszeugnis**

Herr Albert Beispiel, geboren am neunten Juni neunzehnhundertsiebzig, war vom ersten Januar zweitausendelf bis zum dreissigsten September zweitausenddreizehn als Baumeister im Bereich Geschäftsleitung unseres Unternehmens tätig.

Herr Beispiel verfuegt auch in Randbereichen seines vielfaeltigen Aufgabenbereiches über aeusserst profundes Fachwissen.

Herr Beispiel nahm in eigener Initiative regelmaessig erfolgreich an internen und externen Weiterbildungsseminaren teil.

Hervorzuheben ist sein ausgeprägt strategisches Denkvermoegen, das es ihm ermoeglichte, auch bei neuen geschäftlichen Entwicklungen stets in kuerzester Zeit optimale Loesungen zu entwickeln.

Er zeigte sich auch bei der Bewaeltigung neuer Aufgabenbereiche flexibel und aufgeschlossen.

Herr Beispiel verfuegt über eine besonders hohe Arbeitsmoral und war stets aeusserst motiviert, die gesetzten Ziele beharrlich zu verfolgen.

Herr Beispiel zeigte eine hohe Lernbereitschaft.

Alle Aufgaben fuehrte er jederzeit vollkommen selbststaendig, aeusserst sorgfaeltig und planvoll durchdacht aus. Er agierte immer ruhig, überlegt und zielorientiert und in höchstem Masse präzise.

Herr Beispiel war Neuem gegenueber aufgeschlossen, fand gute neue Ideen und innovative Ansaetze.

Die von Herrn Beispiel entwickelten Arbeitsergebnisse lagen stets sehr weit über unseren Anforderungen.

Herr Beispiel war in der Lage, Konflikte erfolgreich zu bewaeltigen. Durch sein konstruktives Verhalten und überlegtes Handeln konnte er so ein gutes Arbeitsklima in seinem Team schaffen.

Herr Beispiel hat die an ihn gestellten sehr hohen Erwartungen zu unserer vollsten Zufriedenheit erfuellt und teilweise sogar übertroffen.

Wegen seines freundlichen und hilfsbereiten Auftretens war Herr Beispiel ein geschaetzter Ansprechpartner. Sein persönliches Verhalten gegenueber Vorgesetzten, Mitarbeitern und Externen war einwandfrei.

Das Arbeitsverhaeltnis endet aus betriebsbedingten Gruenden zum dreissigsten September zweitausenddreizehn. Wir bedanken uns für seine stets ausgezeichnete Mitarbeit in unserem Unternehmen. Sein Ausscheiden bedauern wir sehr und wuenschen ihm für seine Zukunft beruflich und privat weiterhin viel Erfolg und alles Gute.

---

### Bereichs-Drift-Analyse

| Themenbereich | Hoechste Note | Niedrigste Note | Drift | Ampel |
|---|---|---|---|---|
| Fachkenntnisse | 1 | 1 | keine | Grün |
| Lernbereitschaft | 1 (indirekt aus Engagement) | 3 | zwei Stufen | Rot |
| Strategisches Denken | 1 | 1 | keine | Grün |
| Flexibilitaet | 3 | 3 | keine | Orange |
| Engagement | 1 | 1 | keine | Grün |
| Arbeitsweise | 1 | 1 | keine | Grün |
| Innovation | 3 | 3 | keine | Orange |
| Arbeitsergebnis | 1 | 1 | keine | Grün |
| Sozialverhalten | 3 | 3 | keine | Orange |
| Gesamtbeurteilung und Schlussformel | 1 | 1 | keine | Grün |

### Gesamtnoten-Aggregation

Gewichteter Wert vor Drift-Penalty: Note 1 bis 2. Drift-Penalty Lernbereitschaft (zwei Stufen, weicher Bereich): minus eine halbe Stufe. Konstante Note 3 in Innovation und Sozialverhalten (heikle weiche Bereiche): minus eine halbe Stufe. Gesamtnote nach Aggregation: Note 2 bis Note 3.

### Empfehlung

Spitzensaetze sind authentisch (Fachkenntnisse, Arbeitsweise, Arbeitsergebnis, Engagement). Drift bei Lernbereitschaft, konstant niedrige Note bei Innovation und Sozialverhalten. Nachverhandelbar: Saetze zu Lernbereitschaft, Innovation und Sozialverhalten. Beweislast nach BAG: Gesamtnote schlechter als befriedigend muesste der Arbeitgeber beweisen, Gesamtnote besser als befriedigend muss der Arbeitnehmer beweisen — bei diesem Zeugnis ist die Drei in den weichen Bereichen aus den Formulierungen selbst herauslesbar.

## Rechtliche Einordnung und Normen

- **Paragraf 109 GewO** — Anspruch auf qualifiziertes wohlwollendes Zeugnis
- **Paragraf 109 Abs. 2 GewO** — Klarheits- und Wahrheitspflicht; kodierte Negativaussagen unzulässig

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Skill: `rechtliche-bewertung-bag-rechtsprechung`

_Wenn es um Rechtliche Bewertung und BAG-Rechtsprechung zum Arbeitszeugnis in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Rechtliche Bewertung und BAG-Rechtsprechung zum Arbeitszeugnis

## Fachlicher Anker

- **Normen:** Paragraf 109 GewO; ergänzend Paragraf 630 BGB für nicht von Paragraf 109 GewO erfasste Dienstverhältnisse und Paragraf 16 BBiG für Auszubildende.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Geheimcode-Regeln (Rechtliche Ebene)

| Rechtsproblem | Rechtsgrundlage | Handlungsempfehlung |
|---|---|---|
| Anspruch auf qualifiziertes Zeugnis | Paragraf 109 Abs. 1 Satz 3 GewO | Schriftlich verlangen |
| Verdeckte negative Aussage | Paragraf 109 Absatz 2 Satz 2 GewO | Wortlaut, Stellung und objektiven Empfängerhorizont prüfen |
| Zeugnis verletzt Wahrheit oder Klarheit | Paragraf 109 GewO | Konkreten Zielwortlaut verlangen; Ausschlussfrist, Verjährung und Verwirkung prüfen |
| Codewort verstößt gegen Klarheit oder Wohlwollen | Paragraf 109 Abs. 2 GewO, BAG-Linie | Berichtigung verlangen, Kontext begründen |
| Drift im selben Themenbereich | Wohlwollensgebot | Aufwertung der schwachen Sätze verlangen |
| Streitwert Berichtigungsklage | Paragraf 3 ZPO in Verbindung mit Paragraf 46 Absatz 2 ArbGG | Antrag, wirtschaftliches Interesse und örtliche Gerichtspraxis prüfen; kein starrer Monatswert |
| Verjährung des Berichtigungsanspruchs | Paragrafen 195, 199 BGB | drei Jahre ab Schluss des Jahres |
| Verwirkung trotz nicht abgelaufener Verjährung | Treu und Glauben Paragraf 242 BGB | Berichtigung innerhalb weniger Monate stellen |

## Beispiele

**Beispiel 1 – Anspruch auf Berichtigung:** Ein Zeugnis enthält "bemüht" und liegt damit unter einer durchschnittlichen Leistungsbewertung. Nach der Linie des BAG vom 14.10.2003 - 9 AZR 12/03 muss der Arbeitgeber die Tatsachen darlegen und beweisen, die eine unterdurchschnittliche Bewertung tragen. Der Arbeitnehmer benennt dennoch seine Gegenbelege und beantragt einen bestimmten Zielwortlaut.

**Beispiel 2 – Beweislast beim Arbeitnehmer:** Der Arbeitnehmer begehrt die Note "sehr gut" (Note 1 bis 2). Er muss konkrete Leistungsnachweise erbringen, die eine Übererfüllung der Anforderungen belegen — allgemeine Zufriedenheitsbekundungen reichen nicht.

**Beispiel 3 – verspätete Geltendmachung:** Beanstandet ein Arbeitnehmer das Zeugnis erst Jahre später, sind zuerst vertragliche oder tarifliche Ausschlussfristen und die Regelverjährung nach Paragrafen 195, 199 BGB zu prüfen. Verwirkung nach Paragraf 242 BGB setzt zusätzlich zum Zeitablauf konkrete Umstände voraus, aus denen der Arbeitgeber auf die Nichtausübung vertrauen durfte.

**Beispiel 4 – Schlussformel als Signal, nicht Automatismus:** Ein Zeugnis enthält "Wir wünschen ihm alles Gute" ohne Bedauern und ohne Dank. Der Arbeitnehmer war nachweislich beliebt und leistungsstark. Das ist ein Distanzsignal und ein guter Verhandlungspunkt. Als Klagepunkt ist es nur tragfähig, wenn zusätzliche Umstände hinzukommen, etwa ein Vergleichstext, ein bindendes Zwischenzeugnis, eine betriebliche Übung oder ein widersprüchliches Gesamtbild.

**Beispiel 5 – kein allgemeiner Begründungsanspruch:** Der Arbeitgeber muss seine Wortwahl außergerichtlich nicht generell erläutern. Im Berichtigungsprozess greifen Darlegungs- und Beweislastregeln; ein eigenständiger Auskunftsanspruch aus Paragraf 242 BGB kommt nur unter engen Voraussetzungen in Betracht und darf die gesetzliche Beweislast nicht verschieben.

**Beispiel 6 – Codewort als Klarheitsproblem:** Ein Zeugnis enthält bei einem Buchhalter ohne Kassentätigkeit die isolierte Aussage "war ehrlich und korrekt". Die Aussage kann wahr sein, kann aber nach Stellung im Zeugnis und Branchenkontext einen Verdacht wecken. Der Angriff sollte nicht behaupten, jedes Wort "ehrlich" sei verboten, sondern begründen, warum gerade diese Platzierung im Gesamtzusammenhang eine verdeckte negative Aussage erzeugt.

**Beispiel 7 – Drift-Berichtigung:** Ein Zeugnis enthält im Fachbereich eine Maximalformulierung und im Bereich Lernbereitschaft einen Standardsatz. Der Arbeitnehmer kann die Aufwertung der schwachen Sätze verlangen, soweit er die entsprechenden Leistungen substantiiert. Eine uneinheitliche Bewertung ohne Tatsachengrund wird als Widerspruch im Gesamtbild geführt, nicht als bloßes Rechenproblem.

**Beispiel 8 – Streitwert und Vertretungspflicht:** Das Gericht setzt den Streitwert nach Paragraf 3 ZPO fest; landesrechtliche Streitwertkataloge und örtliche Praxis können Orientierung geben, ersetzen aber keine Einzelfallprüfung. Eine anwaltliche Vertretung ist im ersten Rechtszug vor dem Arbeitsgericht möglich, aber nicht erforderlich. Der Klageantrag muss den verlangten Wortlaut so bestimmt wiedergeben, dass ein stattgebender Titel vollstreckbar ist.

## Ergänzende Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.


## Leitentscheidungs-Anker (vollstaendige BAG-Linie)

> Diese Entscheidungen sind als Sucheinstieg gepflegt. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle (`bundesarbeitsgericht.de`, `dejure.org`, Rechtsprechungsportal des Bundes) live verifizieren - Datum, Aktenzeichen, Randnummer, Fortgeltung.

| Entscheidung | Tragende Aussage | Freie Quelle |
| --- | --- | --- |
| **BAG, Urt. v. 14.10.2003 - 9 AZR 12/03** | Zur vollen Zufriedenheit bescheinigt durchschnittliche Leistung (Note 3); Beweislast für bessere Note beim Arbeitnehmer, für schlechtere beim Arbeitgeber. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 18.11.2014 - 9 AZR 584/13** | "Befriedigend" als Mitte der Skala; Arbeitnehmer traegt Beweislast für bessere Note; Branchenueblichkeit guter Noten verschiebt die Beweislast nicht. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 20.02.2001 - 9 AZR 44/00** | Beginn der staendigen Linie: kein Anspruch auf Schlussformel mit Dank und guten Wuenschen; Fehlen kein unzulaessiges Geheimzeichen. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 11.12.2012 - 9 AZR 227/11** | Kein Anspruch auf Dank/Wuensche; bei unzufriedener Mandantschaft mit erteilter Schlussformel ist nur ein Zeugnis OHNE Schlussformel einklagbar - keine Umformulierung. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 25.01.2022 - 9 AZR 146/21** | Bestaetigung der Linie; Abwaegung mit Meinungsfreiheit des Arbeitgebers (Art. 5 I GG). | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 06.06.2023 - 9 AZR 272/22** | Massregelungsverbot $ 612a BGB: eine einmal erteilte Dankes-/Wunschformel darf nicht in spaeterer Fassung gestrichen werden, nur weil der Arbeitnehmer berechtigte Änderungswuensche geltend gemacht hat. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 21.06.2005 - 9 AZR 352/04** | Gebot der Zeugnisklarheit ($ 109 II GewO): massgeblich ist der objektive Empfaengerhorizont, nicht die Absicht des Arbeitgebers. "Kennen gelernt" allein ist kein Geheimcode. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 15.11.2011 - 9 AZR 386/10** | Bestaetigung: "kennen gelernt" ist allein und losgeloest vom uebrigen Zeugnisinhalt kein unzulaessiger Geheimcode; Werturteile-Spielraum mit Grenze Zeugniswahrheit/-klarheit. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 21.09.1999 - 9 AZR 893/98** | Aeussere Form: zweimaliges Falten zulässig, wenn Original kopierfaehig bleibt und Knicke nicht durchschlagen. Wer mit Maschinenname unterzeichnet, muss eigenhaendig unterschreiben. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 27.04.2021 - 9 AZR 262/20** | Tabellarische Ankreuz-/Schulnotenformulare erfuellen $ 109 GewO regelmaessig nicht - individuelle Hervorhebung verlangt Fliesstext. | bundesarbeitsgericht.de / dejure.org |
| **LAG Hamm, Beschl. v. 14.11.2016 - 12 Ta 475/16** | Ironisch überzogenes Lob ist unzulaessig; Arbeitnehmer hat Anspruch auf geschaeftsuebliche Unterschrift des Ausstellers; quer-laufende Unterschrift weckt Zweifel an Ernsthaftigkeit. | nrwe.de / justiz.nrw.de |
| **ArbG Kiel, Urt. v. 18.04.2013 - 5 Ca 80 b/13** | In die Unterschrift eingearbeiteter Smiley mit herabgezogenen Mundwinkeln ist ein unzulaessiges Geheimzeichen ($ 109 II 2 GewO). | frei publiziert / dejure-Suche |
| **BAG, Beschl. v. 07.05.2026 - 8 AZB 25/25** | Im gerichtlichen Vergleich übernommene Pflicht, Zeugnis nach dem ENTWURF des Arbeitnehmers zu erteilen mit Abweichungs-Vorbehalt aus wichtigem Grund, hat vollstreckungsfaehigen Inhalt. | bundesarbeitsgericht.de / dejure.org (vor Schriftsatzverwendung live verifizieren - Entscheidung aus 2026) |
| **BAG, Urt. v. 08.03.1995 - 5 AZR 848/93** | Zeugniserteilung ist Holschuld ($ 269 BGB): Arbeitnehmer holt im Betrieb ab; nur ausnahmsweise (Unzumutbarkeit, $ 242 BGB) Schickschuld. | bundesarbeitsgericht.de / dejure.org |

---

## Skill: `erstpruefung-rollenklaerung-mandatsziel`

_Wenn es um Analyse: Erstprüfung, Rollenklärung und Mandatsziel in Arbeitszeugnis-Analyse geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Analyse: Erstprüfung, Rollenklärung und Mandatsziel

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `Paragraf 611a Abs. 1 BGB` — Arbeitsvertrag und Weisungsbindung.
- `Paragraf 241 Abs. 2 BGB` — Rücksichtnahmepflichten.
- `Paragraf 626 Abs. 1 BGB` — fristlose Kuendigung.
- `Paragraf 1 Abs. 2 KSchG` — soziale Rechtfertigung.
- `Paragraf 4 Satz 1 KSchG` — Klagefrist.
- `Paragraf 7 KSchG` — Fiktionswirkung.
- `Paragraf 102 Abs. 1 BetrVG` — Betriebsratsanhoerung.
- `Paragraf 2 Abs. 1 NachwG` — Nachweis wesentlicher Arbeitsbedingungen.
- `Paragraf 46 Abs. 2 ArbGG` — ZPO-Anwendung im arbeitsgerichtlichen Verfahren.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Fachlicher Anker

- **Normen:** Paragraf 109 GewO; ergänzend Paragraf 630 BGB für nicht von Paragraf 109 GewO erfasste Dienstverhältnisse und Paragraf 16 BBiG für Auszubildende.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Spezialwissen: Analyse: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Analyse** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `klage-strategie-zeugnisberichtigung`

_Wenn es um Klagestrategie Zeugnisberichtigung in Arbeitszeugnis-Analyse geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik._

# Klagestrategie Zeugnisberichtigung

## Fachlicher Anker

- **Normen:** Paragraf 109 GewO; ergänzend Paragraf 630 BGB für nicht von Paragraf 109 GewO erfasste Dienstverhältnisse und Paragraf 16 BBiG für Auszubildende.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Geheimcode-Regeln

### Erfolgsaussichten je Befundtyp

| Befund | Klagbarkeit | Erfolgsaussicht |
|---|---|---|
| "bemüht" als Leistungsformel | Klagbar, wenn die Aussage die Leistung nicht wahrheitsgemäß abbildet | Nach Beleglage |
| Auffällige Reihenfolge im Sozialverhalten | Nur bei verdeckter negativer Aussage im Gesamtkontext tragfähig | Nach Kontext |
| Unvollständige Schlussformel | Meist Verhandlungspunkt, Klage nur mit Zusatzkontext | Niedrig bis Mittel |
| Mutmaßliches Codewort | Nur bei objektiv erkennbarer verdeckter Aussage nach Paragraf 109 Absatz 2 Satz 2 GewO | Nach Kontext |
| Drift im selben Themenbereich | Klagbar (bei nachgewiesenem Schaufenster) | Mittel |
| Konstante Note 3 in einzelnen Bereichen | Nur mit Tatsachen für eine bessere Bewertung | Nach Beleglage |
| Note 3 bei aktenkundig besserer Leistung | Klagbar (Arbeitnehmer beweisbelastet) | Mittel |
| Note 4 im Standardfall | Klagbar (Arbeitgeber beweisbelastet) | Hoch |

### Beweislastregel

| Streitfrage | Beweislast |
|---|---|
| Note schlechter als befriedigend | Arbeitgeber |
| Note besser als befriedigend | Arbeitnehmer |
| Bessere Einzel- oder Gesamtbewertung | Arbeitnehmer trägt und beweist die besseren Leistungen |
| Unterdurchschnittliche Einzel- oder Gesamtbewertung | Arbeitgeber trägt und beweist die schlechteren Leistungen |
| Verdeckte negative Aussage oder unrichtige Tatsache | Ausgangspunkt ist der konkrete Wortlaut; die Last richtet sich nach Anspruch und Einlassung, nicht nach einer starren Codewortregel |

### Streitwert

| Klagegegenstand | Streitwert |
|---|---|
| Vollständige Zeugnisberichtigung | Nach Paragraf 3 ZPO, Antrag, Bedeutung und örtlicher Gerichtspraxis |
| Einzelne Note im Hauptteil | Anteiliger Wert nach Bedeutung der beanstandeten Passage |
| Schlussformel | Regelmäßig geringerer Wert; fehlender gesetzlicher Anspruch mitprüfen |
| Mehrere Punkte | Gesamtwert ohne automatische Addition jedes Satzes |
| Erstmalige Erteilung des Zeugnisses | Einzelfallwert nach wirtschaftlichem Interesse und Gerichtspraxis |

## Beispiele

### Beispiel 1 – Aussergerichtliches Berichtigungsverlangen

Sehr geehrte Damen und Herren,

das mir unter dem aktuellen Datum erteilte Arbeitszeugnis habe ich erhalten. Mit folgenden Formulierungen bin ich nicht einverstanden und bitte um Berichtigung mit den jeweils vorgeschlagenen Wortlauten:

Statt "war stets bemüht, die ihm übertragenen Aufgaben zur vollen Zufriedenheit zu erledigen": "erledigte die ihm übertragenen Aufgaben stets zu unserer vollen Zufriedenheit".

Statt "sein Verhalten gegenüber Kollegen und Vorgesetzten war korrekt": "sein Verhalten gegenüber Vorgesetzten, Kollegen und Kunden war stets einwandfrei". Dieser Zielwortlaut setzt Tatsachen für die verlangte Bewertung voraus; die Reihenfolge allein begründet keinen Automatismus.

Als Vergleichsvorschlag zur knappen Schlussformel: "Wir bedauern sein Ausscheiden, danken ihm für die geleistete Arbeit und wünschen ihm für seinen weiteren beruflichen und privaten Lebensweg alles Gute und weiterhin viel Erfolg". Nur als Klageantrag verwenden, wenn der Einzelfall dafür tragfähige Umstände bietet.

Ich bitte um Übersendung des berichtigten Zeugnisses innerhalb von zwei Wochen ab Zugang dieses Schreibens.

Mit freundlichen Gruessen

### Beispiel 2 – Klageantrag bei Berichtigungsstreit

Der Beklagte wird verurteilt, der Klägerin ein qualifiziertes Arbeitszeugnis zu erteilen, das auf dem Briefkopf der Beklagten ausgestellt wird, vom Tag des Beendigungsdatums datiert und vom dazu Befugten unterschrieben ist und folgenden Inhalt aufweist:

Erstens, in der Leistungsbeurteilung statt "war stets bemueht" die Formulierung "erledigte die ihr übertragenen Aufgaben stets zu unserer vollen Zufriedenheit".

Zweitens, in der Verhaltensbeurteilung statt "Kollegen und Vorgesetzten" die Reihenfolge "Vorgesetzten, Kollegen und Kunden" mit dem Steigerer "stets" und dem Praedikat "einwandfrei".

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Beispiel 3 – Streitwertbegründung

Der Streitwert ist nach Paragraf 3 ZPO in Verbindung mit Paragraf 46 Absatz 2 ArbGG anhand des konkreten Antrags und des wirtschaftlichen Interesses festzusetzen. Als Orientierung wird die für das zuständige Arbeitsgericht veröffentlichte Streitwertpraxis herangezogen. Mehrere beanstandete Passagen werden nicht schematisch addiert; ihre eigenständige wirtschaftliche Bedeutung ist darzulegen.

### Beispiel 4 – Beweisangebote des Arbeitnehmers für bessere Note

Bei dem Begehren einer Note besser als befriedigend kommen folgende Beweisangebote in Betracht: zuständige Zwischenzeugnisse mit guter oder sehr guter Bewertung, Beurteilungsbeleg aus Jahresgespraechen, Boni und Praemien im Zeitraum, ausgezeichnete Performancereports, schriftliche Lob-E-Mails von Vorgesetzten, Zeugenaussagen unmittelbarer Vorgesetzter, Kundenfeedback in dokumentierter Form.

### Beispiel 5 – Verwirkung als Risiko

Wartet der Arbeitnehmer zwei Jahre, bevor er das Berichtigungsverlangen erhebt, ohne plausiblen Grund für die Verzoegerung, kann der Anspruch nach den Grundsaetzen der Verwirkung untergehen, auch wenn die Verjährungsfrist nicht abgelaufen ist. Empfehlung: Berichtigungsverlangen innerhalb der ersten Monate nach Zeugnisuebergabe stellen.

## Rechtliche Einordnung und Normen

- **Paragraf 109 GewO** — Anspruch auf Berichtigung; Grundlage der Klage
- **Paragrafen 195, 199 BGB** — regelmäßige Verjährung; Beginn mit Schluss des Jahres von Anspruchsentstehung und Kenntnis
- **Paragraf 242 BGB** — Verwirkung verlangt Zeit- und Umstandsmoment; Zeitablauf allein genügt nicht

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.


## Leitentscheidungs-Anker (Vollstreckung, Holschuld, Form)

> Diese Entscheidungen sind als Sucheinstieg gepflegt. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle (`bundesarbeitsgericht.de`, `dejure.org`, Rechtsprechungsportal des Bundes) live verifizieren - Datum, Aktenzeichen, Randnummer, Fortgeltung.

| Entscheidung | Tragende Aussage | Freie Quelle |
| --- | --- | --- |
| **BAG, Urt. v. 21.09.1999 - 9 AZR 893/98** | Aeussere Form: zweimaliges Falten zulässig, wenn Original kopierfaehig bleibt und Knicke nicht durchschlagen. Wer mit Maschinenname unterzeichnet, muss eigenhaendig unterschreiben. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 27.04.2021 - 9 AZR 262/20** | Tabellarische Ankreuz-/Schulnotenformulare erfuellen $ 109 GewO regelmaessig nicht - individuelle Hervorhebung verlangt Fliesstext. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Beschl. v. 07.05.2026 - 8 AZB 25/25** | Im gerichtlichen Vergleich übernommene Pflicht, Zeugnis nach dem ENTWURF des Arbeitnehmers zu erteilen mit Abweichungs-Vorbehalt aus wichtigem Grund, hat vollstreckungsfaehigen Inhalt. | bundesarbeitsgericht.de / dejure.org (vor Schriftsatzverwendung live verifizieren - Entscheidung aus 2026) |
| **BAG, Urt. v. 08.03.1995 - 5 AZR 848/93** | Zeugniserteilung ist Holschuld ($ 269 BGB): Arbeitnehmer holt im Betrieb ab; nur ausnahmsweise (Unzumutbarkeit, $ 242 BGB) Schickschuld. | bundesarbeitsgericht.de / dejure.org |


## Vollstreckung des Zeugnisanspruchs

Wenn Urteil oder Vergleich vorliegt, der Arbeitgeber aber nicht oder falsch erfuellt:

| Lage | Instrument |
| --- | --- |
| Titulierter Zeugnisanspruch wird nicht erfuellt | Zwangsgeld, ersatzweise Zwangshaft ($ 888 ZPO - nicht vertretbare Handlung) |
| Vergleich mit Entwurfsklausel ("Zeugnis nach Entwurf des Arbeitnehmers, Abweichung nur aus wichtigem Grund") | Unmittelbar vollstreckbar (BAG 07.05.2026 - 8 AZB 25/25 - vor Verwendung live verifizieren) |
| Erteiltes Zeugnis weicht vom Titel ab | Im Vollstreckungsverfahren ruegen; ironische Übererfuellung ist Nichterfuellung (LAG Hamm 12 Ta 475/16) |
| Streit über "wichtigen Grund" der Abweichung | Arbeitgeber muss den wichtigen Grund darlegen; sonst Zwangsmittel |

**Praxisregel:** Schon beim Vergleichsschluss an die Vollstreckung denken - die Entwurfsklausel mit Wichtiger-Grund-Vorbehalt macht aus dem Vergleich einen scharfen Titel.

---

## Skill: `zeugnis-problem-sortieren`

_Wenn es um Zeugnisproblem Sortieren in Arbeitszeugnis-Analyse geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen._

# Zeugnisproblem Sortieren

## Fachlicher Anker

- **Normen:** Paragraf 109 GewO; ergänzend Paragraf 630 BGB für nicht von Paragraf 109 GewO erfasste Dienstverhältnisse und Paragraf 16 BBiG für Auszubildende.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Vier Pflichtbausteine

1. Ziel klären: Was soll entschieden, geprueft, entworfen, verbessert oder verhandelt werden?
2. Kontext sichern: Rolle, Frist, Dokumente, Beteiligte, Vorgeschichte und Belege.
3. Grenzen setzen: keine Blindzitate, keine erfundenen Tatsachen, keine ungewollten Zugestaendnisse.
4. Ausgabeformat bestimmen: Memo, Tabelle, Schriftsatz, Brief, Beschluss, TOP, Checkliste oder Red-Team-Liste.

## Zeugnis-spezifische Ersttriage (vor jeder Detailprüfung)

- **Anspruchsgrundlage:** Paragraf 109 GewO (qualifiziertes wohlwollendes Zeugnis), für Arbeiter zusätzlich Paragraf 630 BGB.
- **Notenstufen-Matrix nach BAG ständiger Rechtsprechung:**
 - Note 1: "stets zur vollsten Zufriedenheit"
 - Note 2: "stets zur vollen Zufriedenheit"
 - Note 3: "zur vollen Zufriedenheit" (ohne "stets")
 - Note 4: "zur Zufriedenheit" / "war stets bemüht"
 - Note 5: "im Wesentlichen / im Großen und Ganzen zur Zufriedenheit"
- **Wahrheit und Wohlwollen:** Paragraf 109 Abs. 2 GewO (kein Geheimcode, keine Doppeldeutigkeit). Beweislast: bis Note 3 trägt **Arbeitnehmer** die Beweislast für bessere Note; ab Note 4 (befriedigend) trägt **Arbeitgeber** die Beweislast für die schlechtere Beurteilung (BAG ständige Rechtsprechung).
- **Geheimcode-Warnsignale:** "bemüht", "im Wesentlichen", fehlende Steigerungen, falsche Reihenfolge ("Kollegen und Vorgesetzte" statt "Vorgesetzten, Kollegen"), kühle Schlussformel ohne Bedauern/Dank/Erfolgswünsche, Auslassung relevanter Aufgabenbereiche.
- **Fristen:** Verfall des Zeugnisanspruchs nach Verwirkung (ca. 10 Monate nach Beendigung, abhängig vom Einzelfall) und ggf. tarifvertragliche Ausschlussfristen.

## Trade-off-Hinweis

Bei Note 3 versus Note 2 trägt der Arbeitnehmer die Beweislast. Wer auf "stets zur vollen Zufriedenheit" klagt ohne Beurteilungsbeiträge, Beurteilungsbögen oder Zeugen, verliert prozessual. Lieber **Vergleichsweise** in der Güteverhandlung: Note 2 plus warme Schlussformel als Standardpaket.

## Workflow

1. Material erfassen und sichtbar zwischen Tatsache, Behauptung und Bewertung trennen.
2. Eilige Punkte vorziehen (Verwirkung, tarifvertragliche Ausschlussfristen).
3. Schwachstellen und Gegenargumente benennen (Beweislage, Beurteilungsbeiträge).
4. Passende Folge-Skills aus demselben Plugin vorschlagen.
5. Einen verwendbaren Output liefern und offene Punkte mit `[noch klaeren]` markieren.

## Ausgabe

| Punkt | Befund | Risiko | Naechster Schritt |
| --- | --- | --- | --- |
| ... | ... | ... | ... |

## Qualitaetsgate

Ist die Antwort handlungsorientiert, knapp, respektvoll, belegnah und ohne erfundene Quellen? Sind Fristen und offene Tatsachen sichtbar? Ist der nächste Schritt eindeutig?

---

## Skill: `arbeitszeugnis-geheimcodes-schriftsatz-brief-memo-bausteine`

_Wenn es um Geheimcodes: Schriftsatz-, Brief- und Memo-Bausteine in Arbeitszeugnis-Analyse geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Geheimcodes: Schriftsatz-, Brief- und Memo-Bausteine

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `Paragraf 611a Abs. 1 BGB` — Arbeitsvertrag und Weisungsbindung.
- `Paragraf 241 Abs. 2 BGB` — Rücksichtnahmepflichten.
- `Paragraf 626 Abs. 1 BGB` — fristlose Kuendigung.
- `Paragraf 1 Abs. 2 KSchG` — soziale Rechtfertigung.
- `Paragraf 4 Satz 1 KSchG` — Klagefrist.
- `Paragraf 7 KSchG` — Fiktionswirkung.
- `Paragraf 102 Abs. 1 BetrVG` — Betriebsratsanhoerung.
- `Paragraf 2 Abs. 1 NachwG` — Nachweis wesentlicher Arbeitsbedingungen.
- `Paragraf 46 Abs. 2 ArbGG` — ZPO-Anwendung im arbeitsgerichtlichen Verfahren.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Fachlicher Anker

- **Normen:** Paragraf 109 GewO; ergänzend Paragraf 630 BGB für nicht von Paragraf 109 GewO erfasste Dienstverhältnisse und Paragraf 16 BBiG für Auszubildende.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Spezialwissen: Geheimcodes: Schriftsatz-, Brief- und Memo-Bausteine
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Geheimcodes** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `muster-arbeitszeugnis-mit-roten-flaggen`

_Wenn es um Muster-Arbeitszeugnis mit roten Flaggen (Schulungsmaterial) in Arbeitszeugnis-Analyse geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Muster-Arbeitszeugnis mit roten Flaggen (Schulungsmaterial)

## Fachlicher Anker

- **Normen:** Paragraf 109 GewO; ergänzend Paragraf 630 BGB für nicht von Paragraf 109 GewO erfasste Dienstverhältnisse und Paragraf 16 BBiG für Auszubildende.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Geheimcode-Regeln

| Satz | Signal | Ampel | Note |
|---|---|---|---|
| "zur vollen Zufriedenheit" ohne "stets" | Fehlende Steigerung | Orange | Note 3 |
| "war stets bemüht" | Klassisches Note-4-Signal | Rot | Note 4 |
| "Kollegen und Vorgesetzte" (Reihenfolge) | Falsche Reihenfolge | Orange | Note 3 |
| "direkte Kommunikationsweise" | Euphemismus für schwieriges Verhalten | Rot | Note 4-5 |
| Schlussformel ohne Bedauern | Kühles Distanzsignal | Orange-Rot | Kontextsignal |

## Beispiele

### Vollständiges Muster-Zeugnis mit roten Flaggen

---

**[Briefkopf]**
Beispiel GmbH | Beispielstraße 5 | 20000 Beispielstadt

**Arbeitszeugnis**

Herr Thomas Beispiel, geboren am 15. Juni 1980, war vom 1. Januar 2020 bis zum 30. Juni 2024 in unserem Unternehmen als Vertriebsmitarbeiter beschäftigt.

**Aufgaben:**
Herr Beispiel war im Außendienst tätig und betreute einen definierten Kundenkreis im Bereich Industriebedarf. Er war für die regelmäßige Kundenbesuche, die Angebotserstellung und die Bearbeitung von Reklamationen zuständig.

**Leistungsbeurteilung:**
Herr Beispiel verfügt über ausreichende Fachkenntnisse für seinen Aufgabenbereich. Er war stets bemüht, die ihm übertragenen Aufgaben zur vollen Zufriedenheit zu erledigen, und zeigte dabei durchgehend guten Willen. Seine Arbeitsweise war im Wesentlichen strukturiert.

*(Analyse: "bemüht" = Rot/Note 4; "zur vollen Zufriedenheit" ohne "stets" = Orange/Note 3; "im Wesentlichen" = Rot/Note 4; Gesamttendenz Leistung: Note 4)*

**Verhaltensbeurteilung:**
Gegenüber Kollegen und Vorgesetzten verhielt sich Herr Beispiel korrekt. Er zeichnete sich durch eine direkte Kommunikationsweise aus.

*(Analyse: Reihenfolge falsch — Kollegen vor Vorgesetzten = Orange; "korrekt" statt "einwandfrei" = Orange/Note 3; "direkte Kommunikationsweise" = Rot/Note 4-5; Kein Wort zu Kunden trotz Kundenjob = Rot)*

**Schlussformel:**
Wir danken Herrn Beispiel für seine Mitarbeit und wünschen ihm für die Zukunft alles Gute.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

### Gesamtbewertung des Schulungsbeispiels

| Bereich | Ampel | Note |
|---|---|---|
| Leistungsbeurteilung | Rot | Note 4 |
| Verhaltensbeurteilung | Rot | Note 4 |
| Schlussformel | Orange | Note 3-4 |
| **Gesamtnote** | **Rot** | **Note 4** |

**Handlungsempfehlung:** Nachverhandlung aller Leistungs- und Verhaltensformulierungen sowie wärmere Schlussformel als Vergleichspunkt empfohlen. Bei Weigerung: Klage vor allem zu Leistungs- und Verhaltensformulierungen prüfen; Schlussformel nur mit Zusatzkontext.

## Rechtliche Einordnung und Normen

- **Paragraf 109 GewO** — Anspruch auf qualifiziertes wohlwollendes Zeugnis
- **Paragraf 109 Abs. 2 GewO** — Klarheits- und Wahrheitspflicht; kodierte Negativaussagen unzulässig

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Anwendungshinweise

1. Diese Vollprüfung als Kontext einfügen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Bearbeiter anweisen, sich anhand der oben aufgeführten Skills zu orientieren.
4. Entscheidungen nur nach Prüfung von Gericht, Datum, Aktenzeichen, tragender Aussage und amtlicher oder frei zugänglicher Quelle verwenden.
