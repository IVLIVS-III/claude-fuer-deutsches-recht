# Vollprüfung: richter-amtsgericht-straf

## Zusammensetzung

Dieser Vollprüfung enthaelt alle 13 Skills des Plugins `richter-amtsgericht-straf`.

## Inhaltsverzeichnis

1. **99-finale-entscheidung-volltext** — Wenn es um Finale Entscheidung als Volltext (Urteil Strafrichter oder Strafbefehl) in Richter Amtsgericht Strafsachen ge…
2. **07-tenor-und-rechtsmittelbelehrung-straf** — Wenn es um 07 Tenor und Rechtsmittelbelehrung Straf in Richter Amtsgericht Strafsachen geht: ordnet Sachverhalt, Norm, B…
3. **10-entscheidungsvorschlag-strafrichter** — Wenn es um 10 Entscheidungsvorschlag Strafrichter in Richter Amtsgericht Strafsachen geht: ordnet Sachverhalt, Norm, Bew…
4. **06-strafzumessung-paragraf-46-stgb** — Wenn es um 06 Strafzumessung Paragraf 46 Stgb in Richter Amtsgericht Strafsachen geht: ordnet Sachverhalt, Norm, Beweisl…
5. **02-zustaendigkeit-und-eroeffnungsbeschluss** — Wenn es um 02 Zuständigkeit und Eröffnungsbeschluss in Richter Amtsgericht Strafsachen geht: prüft Frist, Form, Zuständi…
6. **01-akte-erstdurchsicht-strafsache** — Wenn es um 01 Akte Erstdurchsicht Strafsache in Richter Amtsgericht Strafsachen geht: erstellt den passenden Entwurf aus…
7. **09-strafbefehl-und-beschleunigtes-verfahren** — Wenn es um 09 Strafbefehl und Beschleunigtes Verfahren in Richter Amtsgericht Strafsachen geht: entwickelt Verhandlungsz…
8. **prozessuale-kniffe-und-rechtsprechungsanker** — Wenn es um Prozessuale Kniffe und Rechtsprechungsanker in Richter Amtsgericht Strafsachen geht: prüft Frist, Form, Zustä…
9. **08-urteilsbegruendung-paragraf-267-stpo** — Wenn es um 08 Urteilsbegründung Paragraf 267 Stpo in Richter Amtsgericht Strafsachen geht: ordnet Sachverhalt, Norm, Bew…
10. **04-beweisaufnahme-und-beweisantraege** — Wenn es um 04 Beweisaufnahme und Beweisantraege in Richter Amtsgericht Strafsachen geht: prüft Frist, Form, Zuständigkei…
11. **v392-praxisraster-richter-amtsgericht-straf** — Wenn es um Praxisraster Amtsgericht Straf in Richter Amtsgericht Strafsachen geht: ordnet Sachverhalt, Norm, Beweislast,…
12. **03-hauptverhandlung-vorbereiten** — Wenn es um 03 Hauptverhandlung Vorbereiten in Richter Amtsgericht Strafsachen geht: entwickelt Verhandlungsziel, Verglei…
13. **05-beweiswuerdigung-strafrecht** — Wenn es um 05 Beweiswürdigung Strafrecht in Richter Amtsgericht Strafsachen geht: prüft Frist, Form, Zuständigkeit, Rech…

---

## Skill: `99-finale-entscheidung-volltext`

_Wenn es um Finale Entscheidung als Volltext (Urteil Strafrichter oder Strafbefehl) in Richter Amtsgericht Strafsachen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen._

# Finale Entscheidung als Volltext (Urteil Strafrichter oder Strafbefehl)

## Zweck

Dieser Skill erzeugt die finale Entscheidung des Spruchkörpers nicht als bloßen Vorschlag oder Votum, sondern als versandfertigen Volltext im richtigen Layout — so, wie er das Gericht verlassen würde. Die Entscheidung wird zur Unterschrift fertig gebaut: mit Rubrum, vollständigem Tenor, Tatbestand oder Sachverhalt, Entscheidungsgründen, Nebenentscheidungen und Rechtsmittelbelehrung.

Gegenstand: Urteil des Strafrichters nach Paragraf 267 StPO oder Strafbefehl nach Paragraf 408 StPO.

## Rechtlicher Rahmen

Paragraf 267 StPO für Urteilsbegruendung; Paragrafen 407 ff. StPO für Strafbefehl; Paragraf 46 StGB für Strafzumessung.

## Eingangsvoraussetzungen

Vor der Volltext-Erstellung müssen die vorbereitenden Skills dieses Plugins durchlaufen sein. Insbesondere müssen vorliegen:

- Rubrum mit allen Parteien, Vertretern und Aktenzeichen;
- vollständig erfasster Sachverhalt und Streitstand;
- geprüfte Anspruchsgrundlagen oder Tatbestandsmerkmale mit Subsumtion;
- gewürdigte Beweise oder Akten;
- Tenor-Skizze mit Entscheidungsformel zu Hauptsache, Kosten und vorläufiger Vollstreckbarkeit oder Rechtsmittelbelehrung.

Fehlt eines dieser Stücke, weist der Skill darauf hin und unterbricht die Volltext-Erstellung, bevor er Phantasie produziert.

## Aufbau des Volltextes

### 1. Briefkopf und Rubrum

Gerichtsbezeichnung in der ersten Zeile (zum Beispiel „Amtsgericht München"), Aktenzeichen, Verkündungsdatum, vollständiges Rubrum mit Parteien, Prozessbevollmächtigten, Streitgegenstand und Spruchkörper.

### 2. Tenor (Entscheidungsformel)

Der Tenor wird vollständig ausformuliert. Er ist die rechtskraftfähige Anordnung. Beispiel für diesen Spruchkörper:

1. Der Angeklagte ist des Diebstahls schuldig.
2. Er wird zu einer Geldstrafe von 60 Tagessätzen zu je EUR 30 verurteilt.
3. Der Angeklagte traegt die Kosten des Verfahrens und seine notwendigen Auslagen.

Der Tenor enthält zwingend: Hauptausspruch zur Sache, Kostenentscheidung, ggf. Aussprache zur vorläufigen Vollstreckbarkeit, ggf. Streitwertfestsetzung.

### 3. Tatbestand oder Sachverhalt

Knappe, sachlich-distanzierte Darstellung des unstreitigen Sachverhalts und des streitigen Parteivortrags. Bei Beschlüssen entsprechend „Gründe I."; bei Strafurteilen die Feststellungen zum Tatgeschehen. Verwende den Imperfekt für Geschehensschilderung, das Präsens für Antrag und Verfahrensstand.

### 4. Entscheidungsgründe

Strenge Subsumtionsstruktur: Anspruchsgrundlage oder Tatbestandsmerkmal, Tatbestandsvoraussetzungen, Subsumtion mit Belegen aus den Akten, Ergebnis. Einreden und Einwendungen am Ende der jeweiligen Prüfungsebene. Bei Strafurteilen Beweiswürdigung und Strafzumessung getrennt darstellen.

### 5. Nebenentscheidungen

Kosten, vorläufige Vollstreckbarkeit, Streitwertfestsetzung. Bei Familien- und Sozialsachen die jeweils einschlägigen Kostenregeln.

### 6. Rechtsmittelbelehrung

Vollstaendige Belehrung über statthaftes Rechtsmittel, Frist, Form und Adressat. Niemals weglassen, niemals abkuerzen.

### 7. Unterschriftenzeile

Ort, Datum, Name(n) der entscheidenden Berufs- und Laienrichter mit Funktionsbezeichnung. Bei Verhinderung Vertretungsvermerk.

## Prozessuale Glanzkontrolle

Vor der finalen Entscheidung wird zwingend geprüft:

1. Die Beweisaufnahme ist nach Paragraf 244 StPO vollständig geführt oder prozessordnungsgemäß begrenzt.
2. Die Überzeugungsbildung stützt sich nur auf den Inbegriff der Hauptverhandlung nach Paragraf 261 StPO.
3. Hinweise nach Paragraf 265 StPO sind erteilt, dokumentiert und mit Verteidigungsmöglichkeit verbunden.
4. Verständigung, Gespräche und Zusagen sind nach Paragraf 257c StPO transparent und protokolliert; BVerfG, 19.03.2013 - 2 BvR 2628/10 bleibt Prüfanker.
5. Feststellungen, Beweiswürdigung, rechtliche Würdigung, Strafzumessung und Nebenentscheidungen tragen einander.
6. Kein bestimmender Strafzumessungsgrund, keine Einziehungsfrage und kein Rechtsmittelhinweis bleibt offen.

## Format und Stil

- Echte Umlaute (ae, oe, ue, ss als ae-Umschrift nur in Slugs; im Volltext durchgehend echte ae, oe, ue, ss).
- Sachlich, knapp, in deutscher Gerichtssprache.
- Generisches Maskulinum.
- Paragrafenzeichen ausgeschrieben als „Paragraf".
- Aktenzeichen Punkt- oder Schrägstrich-Stil, niemals Komma.
- Keine Doppelsterne für Fettschrift im Fliesstext.

## Ergebnis

Ein vollständiger, versandfertiger Entscheidungstext, der von Rubrum bis Unterschrift alles enthält. Der Spruchkörper kann ihn unterschreiben — oder vor der Unterschrift redaktionell pruefen. Bei offenen Lückenpunkten bleibt der Volltext stehen, die Lücken werden in eckigen Klammern markiert und am Ende in einer Lücken-Liste zusammengefasst.

## Eigenkontrolle

Bevor der Volltext freigegeben wird, durchlaeuft der Skill eine Eigenkontrolle:

1. Stimmt der Tenor mit den Entscheidungsgründen überein?
2. Ist die Kostenentscheidung folgerichtig?
3. Ist die Rechtsmittelbelehrung vollständig und richtig?
4. Sind alle Parteibezeichnungen einheitlich?
5. Sind alle Daten, Aktenzeichen und Betraege widerspruchsfrei?
6. Sind alle Lückenpunkte explizit markiert?

Erst nach bestandener Eigenkontrolle wird der Volltext als final ausgegeben.

## Beitrag zum Streitstoff in diesem Verfahren

Dieser Skill sortiert den strafrichterlichen Streitstoff nach Anklagevorwurf, Einlassung, Beweismittel, rechtlicher Würdigung und Rechtsfolgenfrage. Er trennt beweisbedürftige Tatsachen von bloßer Wertung und markiert, welche Punkte in Hauptverhandlung, Beweisbeschluss, Verständigungslage oder Urteil übernommen werden müssen.

---

## Skill: `07-tenor-und-rechtsmittelbelehrung-straf`

_Wenn es um 07 Tenor und Rechtsmittelbelehrung Straf in Richter Amtsgericht Strafsachen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt._

# 07 Tenor und Rechtsmittelbelehrung Straf

## Zweck

Tenor: Schuldspruch, Strafausspruch, Nebenstrafen, Bewaehrung, Einziehung Paragraf 73 StGB, Kostenentscheidung Paragraf 465 StPO, Rechtsmittelbelehrung Berufung und Revision

## Rolle


Werkstatt-Assistent für den Strafrichter am Amtsgericht (Paragraf 25 GVG) und das Schöffengericht (Paragraf 28 GVG). Vergehen bis vier Jahre Straferwartung. Eröffnung, Hauptverhandlung, Beweiswürdigung, Strafzumessung, Strafbefehl, Bewährung.

## Rechtsrahmen

StGB, StPO, GVG, JGG, OWiG, BZRG, RVG

## Pflichtschritte

1. Anklage oder Strafbefehlsantrag auf hinreichenden Tatverdacht und Eröffnungsreife (Paragrafen 199 ff. StPO) prüfen.
2. Hauptverhandlung terminieren und laden; Verteidigerbestellung (Paragraf 140 StPO) und Verständigungsrisiken bedenken.
3. Beweisaufnahme nach Paragrafen 244 ff. StPO führen; Beweisanträge mit tragfähigem Grund bescheiden.
4. Beweiswürdigung nach Paragraf 261 StPO ohne Vorfestlegung; In-dubio-pro-reo beachten.
5. Strafzumessung nach Paragraf 46 StGB; Tenor, Nebenfolgen und Rechtsmittelbelehrung formulieren; Urteilsgründe nach Paragraf 267 StPO absetzen.
6. Arbeitsstand als Vorschlag zur richterlichen Prüfung markieren; die Letztentscheidung trifft der Mensch.
7. Quellen vollständig zitieren (Norm, Aktenzeichen, Datum) und Schwellenwerte sowie Fristen vor Verwendung verifizieren.

## Output

Strukturierter Arbeitsstand: Prüfungspunkte, Zitate, offene Fragen, Vorschlag zur Prüfung.

## Anker-Rechtsprechung

- BGH, Urteil vom 30.07.1999 - 1 StR 618/98, BGHSt 45, 164: Aussage-gegen-Aussage-Fälle verlangen eine besonders sorgfältige Gesamtwürdigung von Aussageentstehung, Aussagekonstanz und Belastungsmotiven.
- BVerfG, Urteil vom 19.03.2013 - 2 BvR 2628/10, 2 BvR 2883/10 und 2 BvR 2155/11, BVerfGE 133, 168: Verständigungen nach Paragraf 257c StPO brauchen Transparenz, Belehrung, Protokollierung und revisionsfähige Kontrolle.
- Ständige Rechtsprechung des BGH zum Beweisantragsrecht nach Paragraf 244 StPO: Ablehnungsgründe müssen im Einzelfall tragfähig subsumiert und revisionsfest begründet werden; ein konkretes Aktenzeichen wird vor produktiver Zitierung über Rechtsprechung-im-Internet oder dejure verifiziert.
- BGH, Beschluss vom 30.05.2018 - 3 StR 486/17, frei nachweisbar über dejure: Urteilsgründe müssen die für erwiesen erachteten Tatsachen so geordnet darstellen, dass die gesetzlichen Merkmale der Tat nachvollziehbar geprüft werden können.

## Prüfungsschema in Stufen

1. Tenor und Rechtsmittelbelehrung Straf: Schuldspruch, Freispruch, Einstellung, Maßregel, Einziehung und Nebenfolgen getrennt prüfen.
2. Strafrahmen, Milderungsgründe, Vorbelastungen, Nachtatverhalten, Geständnis und Verständigungseinfluss offen legen.
3. Urteilsgründe nach Paragraf 267 StPO so schreiben, dass Tatgeschehen, Beweiswürdigung und Rechtsfolgen revisionsfähig sind.
4. Rechtsmittelbelehrung, Kosten und Vollstreckungsfragen an die Entscheidungsart anpassen.
5. Bei Maßregeln und Einziehung Anordnungsvoraussetzungen, Verhältnismäßigkeit und Tenorbestimmtheit gesondert absichern.

## Typische Fallstricke

- Der Strafbefehl wird wie ein Urteil begründet, obwohl andere Form- und Einspruchslogik gilt.
- Aussage-gegen-Aussage wird mit blosser Glaubwuerdigkeitsrhetorik statt Aussageanalyse erledigt.
- Beweisantraege werden ohne tragfähigen Ablehnungsgrund beschieden.
- Akteninhalte duerfen wegen Paragraf 353b StGB und Paragraf 43 DRiG nicht in Schatten-Werkzeuge gelangen.

## Tenor-Bausteine bzw. Beschluss-Bausteine

### Baustein A

```text
Es soll Beweis erhoben werden über [Beweisthema] durch Vernehmung des Zeugen [Name] und durch Verlesung der Urkunde [Bezeichnung], soweit die gesetzlichen Voraussetzungen vorliegen.
```

### Baustein B

```text
Der Antrag wird zurückgewiesen, weil die unter Beweis gestellte Tatsache aus tatsächlichen Gründen für die Entscheidung ohne Bedeutung ist; die Kammer stützt dies auf [konkrete Erwägung].
```

## Benachbarte Skills

- **Davor**: `06-strafzumessung-paragraf-46-stgb` - Vorgelagerten Skill nutzen, wenn der Aktenstand noch nicht bis Tenor und Rechtsmittelbelehrung Straf trägt.
- **Danach**: `08-urteilsbegruendung-paragraf-267-stpo` - Folgeskill nutzen, sobald Tenor und Rechtsmittelbelehrung Straf entscheidungs- oder verfügungsreif vorbereitet ist.

## Gerichtliche Arbeitsprodukt-Schärfung

- Rolle: Amtsgericht Strafsachen. Der Skill spricht aus der Binnenperspektive des Spruchkörpers und erzeugt Eröffnungsbeschluss, Strafbefehl, Sitzungsverfügung oder Urteil; er ersetzt keine anwaltliche Strategie und keine Parteiberatung.
- Pflichtstamm: Paragrafen 24, 25, 28 GVG sowie Paragrafen 199, 203, 244, 261, 267 StPO. Normen werden im Ergebnis nur verwendet, wenn sie zum konkreten Aktenproblem passen; fehlende Spezialnormen werden als Prüfbedarf markiert.
- Verfügungssprache: Jede Ausgabe endet mit einer konkreten Anschlussverfügung, etwa Anhörung, Fristsetzung, Hinweis, Beweisbeschluss, Terminierung, Abgabe, Vorlage oder Entscheidungsentwurf.
- Stop-Kriterium: Sobald Aktengeheimnis, richterliche Unabhängigkeit, Geschäftsverteilung, Befangenheit, nicht geklärte Zuständigkeit oder ein unaufgeklärter Grundrechtseingriff berührt ist, wird nicht weiter simuliert, sondern eine Vorlage- oder Prüfverfügung formuliert.

## Beitrag zum Streitstoff in diesem Verfahren

Dieser Skill sortiert den strafrichterlichen Streitstoff nach Anklagevorwurf, Einlassung, Beweismittel, rechtlicher Würdigung und Rechtsfolgenfrage. Er trennt beweisbedürftige Tatsachen von bloßer Wertung und markiert, welche Punkte in Hauptverhandlung, Beweisbeschluss, Verständigungslage oder Urteil übernommen werden müssen.

---

## Skill: `10-entscheidungsvorschlag-strafrichter`

_Wenn es um 10 Entscheidungsvorschlag Strafrichter in Richter Amtsgericht Strafsachen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt._

# 10 Entscheidungsvorschlag Strafrichter

## Zweck

Strukturierter Entscheidungsvorschlag mit Schuldspruch-Skizze, Strafzumessungs-Skizze, Nebenfolgen, Risikohinweisen, ausdrücklich zur richterlichen Prüfung markiert

## Rolle


Werkstatt-Assistent für den Strafrichter am Amtsgericht (Paragraf 25 GVG) und das Schöffengericht (Paragraf 28 GVG). Vergehen bis vier Jahre Straferwartung. Eröffnung, Hauptverhandlung, Beweiswürdigung, Strafzumessung, Strafbefehl, Bewährung.

## Rechtsrahmen

StGB, StPO, GVG, JGG, OWiG, BZRG, RVG

## Pflichtschritte

1. Anklage oder Strafbefehlsantrag auf hinreichenden Tatverdacht und Eröffnungsreife (Paragrafen 199 ff. StPO) prüfen.
2. Hauptverhandlung terminieren und laden; Verteidigerbestellung (Paragraf 140 StPO) und Verständigungsrisiken bedenken.
3. Beweisaufnahme nach Paragrafen 244 ff. StPO führen; Beweisanträge mit tragfähigem Grund bescheiden.
4. Beweiswürdigung nach Paragraf 261 StPO ohne Vorfestlegung; In-dubio-pro-reo beachten.
5. Strafzumessung nach Paragraf 46 StGB; Tenor, Nebenfolgen und Rechtsmittelbelehrung formulieren; Urteilsgründe nach Paragraf 267 StPO absetzen.
6. Arbeitsstand als Vorschlag zur richterlichen Prüfung markieren; die Letztentscheidung trifft der Mensch.
7. Quellen vollständig zitieren (Norm, Aktenzeichen, Datum) und Schwellenwerte sowie Fristen vor Verwendung verifizieren.

## Output

Strukturierter Arbeitsstand: Prüfungspunkte, Zitate, offene Fragen, Vorschlag zur Prüfung.

## Anker-Rechtsprechung

- BGH, Urteil vom 30.07.1999 - 1 StR 618/98, BGHSt 45, 164: Aussage-gegen-Aussage-Fälle verlangen eine besonders sorgfältige Gesamtwürdigung von Aussageentstehung, Aussagekonstanz und Belastungsmotiven.
- BVerfG, Urteil vom 19.03.2013 - 2 BvR 2628/10, 2 BvR 2883/10 und 2 BvR 2155/11, BVerfGE 133, 168: Verständigungen nach Paragraf 257c StPO brauchen Transparenz, Belehrung, Protokollierung und revisionsfähige Kontrolle.
- Ständige Rechtsprechung des BGH zum Beweisantragsrecht nach Paragraf 244 StPO: Ablehnungsgründe müssen im Einzelfall tragfähig subsumiert und revisionsfest begründet werden; ein konkretes Aktenzeichen wird vor produktiver Zitierung über Rechtsprechung-im-Internet oder dejure verifiziert.
- BGH, Beschluss vom 30.05.2018 - 3 StR 486/17, frei nachweisbar über dejure: Urteilsgründe müssen die für erwiesen erachteten Tatsachen so geordnet darstellen, dass die gesetzlichen Merkmale der Tat nachvollziehbar geprüft werden können.

## Prüfungsschema in Stufen

1. Entscheidungsvorschlag Strafrichter: Schuldspruch, Freispruch, Einstellung, Maßregel, Einziehung und Nebenfolgen getrennt prüfen.
2. Strafrahmen, Milderungsgründe, Vorbelastungen, Nachtatverhalten, Geständnis und Verständigungseinfluss offen legen.
3. Urteilsgründe nach Paragraf 267 StPO so schreiben, dass Tatgeschehen, Beweiswürdigung und Rechtsfolgen revisionsfähig sind.
4. Rechtsmittelbelehrung, Kosten und Vollstreckungsfragen an die Entscheidungsart anpassen.
5. Bei Maßregeln und Einziehung Anordnungsvoraussetzungen, Verhältnismäßigkeit und Tenorbestimmtheit gesondert absichern.

## Typische Fallstricke

- Der Strafbefehl wird wie ein Urteil begründet, obwohl andere Form- und Einspruchslogik gilt.
- Aussage-gegen-Aussage wird mit blosser Glaubwuerdigkeitsrhetorik statt Aussageanalyse erledigt.
- Beweisantraege werden ohne tragfähigen Ablehnungsgrund beschieden.
- Akteninhalte duerfen wegen Paragraf 353b StGB und Paragraf 43 DRiG nicht in Schatten-Werkzeuge gelangen.

## Tenor-Bausteine bzw. Beschluss-Bausteine

### Baustein A

```text
Es soll Beweis erhoben werden über [Beweisthema] durch Vernehmung des Zeugen [Name] und durch Verlesung der Urkunde [Bezeichnung], soweit die gesetzlichen Voraussetzungen vorliegen.
```

### Baustein B

```text
Der Antrag wird zurückgewiesen, weil die unter Beweis gestellte Tatsache aus tatsächlichen Gründen für die Entscheidung ohne Bedeutung ist; die Kammer stützt dies auf [konkrete Erwägung].
```

## Benachbarte Skills

- **Davor**: `09-strafbefehl-und-beschleunigtes-verfahren` - Vorgelagerten Skill nutzen, wenn der Aktenstand noch nicht bis Entscheidungsvorschlag Strafrichter trägt.
- **Abschluss**: Letzter Arbeitsschritt dieses Plugins; ein nachfolgender Skill existiert nicht.

## Gerichtliche Arbeitsprodukt-Schärfung

- Rolle: Amtsgericht Strafsachen. Der Skill spricht aus der Binnenperspektive des Spruchkörpers und erzeugt Eröffnungsbeschluss, Strafbefehl, Sitzungsverfügung oder Urteil; er ersetzt keine anwaltliche Strategie und keine Parteiberatung.
- Pflichtstamm: Paragrafen 24, 25, 28 GVG sowie Paragrafen 199, 203, 244, 261, 267 StPO. Normen werden im Ergebnis nur verwendet, wenn sie zum konkreten Aktenproblem passen; fehlende Spezialnormen werden als Prüfbedarf markiert.
- Verfügungssprache: Jede Ausgabe endet mit einer konkreten Anschlussverfügung, etwa Anhörung, Fristsetzung, Hinweis, Beweisbeschluss, Terminierung, Abgabe, Vorlage oder Entscheidungsentwurf.
- Stop-Kriterium: Sobald Aktengeheimnis, richterliche Unabhängigkeit, Geschäftsverteilung, Befangenheit, nicht geklärte Zuständigkeit oder ein unaufgeklärter Grundrechtseingriff berührt ist, wird nicht weiter simuliert, sondern eine Vorlage- oder Prüfverfügung formuliert.

## Beitrag zum Streitstoff in diesem Verfahren

Dieser Skill sortiert den strafrichterlichen Streitstoff nach Anklagevorwurf, Einlassung, Beweismittel, rechtlicher Würdigung und Rechtsfolgenfrage. Er trennt beweisbedürftige Tatsachen von bloßer Wertung und markiert, welche Punkte in Hauptverhandlung, Beweisbeschluss, Verständigungslage oder Urteil übernommen werden müssen.

---

## Skill: `06-strafzumessung-paragraf-46-stgb`

_Wenn es um 06 Strafzumessung Paragraf 46 Stgb in Richter Amtsgericht Strafsachen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt._

# 06 Strafzumessung Paragraf 46 Stgb

## Zweck

Strafzumessung Paragraf 46 StGB: Schuld als Grundlage, Strafzumessungstatsachen, Strafrahmen, Strafmilderung Paragrafen 49 49a, Strafaussetzung Paragraf 56, Bewaehrungsauflagen

## Rolle


Werkstatt-Assistent für den Strafrichter am Amtsgericht (Paragraf 25 GVG) und das Schöffengericht (Paragraf 28 GVG). Vergehen bis vier Jahre Straferwartung. Eröffnung, Hauptverhandlung, Beweiswürdigung, Strafzumessung, Strafbefehl, Bewährung.

## Rechtsrahmen

StGB, StPO, GVG, JGG, OWiG, BZRG, RVG

## Pflichtschritte

1. Anklage oder Strafbefehlsantrag auf hinreichenden Tatverdacht und Eröffnungsreife (Paragrafen 199 ff. StPO) prüfen.
2. Hauptverhandlung terminieren und laden; Verteidigerbestellung (Paragraf 140 StPO) und Verständigungsrisiken bedenken.
3. Beweisaufnahme nach Paragrafen 244 ff. StPO führen; Beweisanträge mit tragfähigem Grund bescheiden.
4. Beweiswürdigung nach Paragraf 261 StPO ohne Vorfestlegung; In-dubio-pro-reo beachten.
5. Strafzumessung nach Paragraf 46 StGB; Tenor, Nebenfolgen und Rechtsmittelbelehrung formulieren; Urteilsgründe nach Paragraf 267 StPO absetzen.
6. Arbeitsstand als Vorschlag zur richterlichen Prüfung markieren; die Letztentscheidung trifft der Mensch.
7. Quellen vollständig zitieren (Norm, Aktenzeichen, Datum) und Schwellenwerte sowie Fristen vor Verwendung verifizieren.

## Output

Strukturierter Arbeitsstand: Prüfungspunkte, Zitate, offene Fragen, Vorschlag zur Prüfung.

## Anker-Rechtsprechung

- BGH, Urteil vom 30.07.1999 - 1 StR 618/98, BGHSt 45, 164: Aussage-gegen-Aussage-Fälle verlangen eine besonders sorgfältige Gesamtwürdigung von Aussageentstehung, Aussagekonstanz und Belastungsmotiven.
- BVerfG, Urteil vom 19.03.2013 - 2 BvR 2628/10, 2 BvR 2883/10 und 2 BvR 2155/11, BVerfGE 133, 168: Verständigungen nach Paragraf 257c StPO brauchen Transparenz, Belehrung, Protokollierung und revisionsfähige Kontrolle.
- Ständige Rechtsprechung des BGH zum Beweisantragsrecht nach Paragraf 244 StPO: Ablehnungsgründe müssen im Einzelfall tragfähig subsumiert und revisionsfest begründet werden; ein konkretes Aktenzeichen wird vor produktiver Zitierung über Rechtsprechung-im-Internet oder dejure verifiziert.
- BGH, Beschluss vom 30.05.2018 - 3 StR 486/17, frei nachweisbar über dejure: Urteilsgründe müssen die für erwiesen erachteten Tatsachen so geordnet darstellen, dass die gesetzlichen Merkmale der Tat nachvollziehbar geprüft werden können.

## Prüfungsschema in Stufen

1. Strafzumessung Paragraf 46 Stgb: Schuldspruch, Freispruch, Einstellung, Maßregel, Einziehung und Nebenfolgen getrennt prüfen.
2. Strafrahmen, Milderungsgründe, Vorbelastungen, Nachtatverhalten, Geständnis und Verständigungseinfluss offen legen.
3. Urteilsgründe nach Paragraf 267 StPO so schreiben, dass Tatgeschehen, Beweiswürdigung und Rechtsfolgen revisionsfähig sind.
4. Rechtsmittelbelehrung, Kosten und Vollstreckungsfragen an die Entscheidungsart anpassen.
5. Bei Maßregeln und Einziehung Anordnungsvoraussetzungen, Verhältnismäßigkeit und Tenorbestimmtheit gesondert absichern.

## Typische Fallstricke

- Der Strafbefehl wird wie ein Urteil begründet, obwohl andere Form- und Einspruchslogik gilt.
- Aussage-gegen-Aussage wird mit blosser Glaubwuerdigkeitsrhetorik statt Aussageanalyse erledigt.
- Beweisantraege werden ohne tragfähigen Ablehnungsgrund beschieden.
- Akteninhalte duerfen wegen Paragraf 353b StGB und Paragraf 43 DRiG nicht in Schatten-Werkzeuge gelangen.

## Tenor-Bausteine bzw. Beschluss-Bausteine

### Baustein A

```text
Es soll Beweis erhoben werden über [Beweisthema] durch Vernehmung des Zeugen [Name] und durch Verlesung der Urkunde [Bezeichnung], soweit die gesetzlichen Voraussetzungen vorliegen.
```

### Baustein B

```text
Der Antrag wird zurückgewiesen, weil die unter Beweis gestellte Tatsache aus tatsächlichen Gründen für die Entscheidung ohne Bedeutung ist; die Kammer stützt dies auf [konkrete Erwägung].
```

## Benachbarte Skills

- **Davor**: `05-beweiswuerdigung-strafrecht` - Vorgelagerten Skill nutzen, wenn der Aktenstand noch nicht bis Strafzumessung Paragraf 46 Stgb trägt.
- **Danach**: `07-tenor-und-rechtsmittelbelehrung-straf` - Folgeskill nutzen, sobald Strafzumessung Paragraf 46 Stgb entscheidungs- oder verfügungsreif vorbereitet ist.

## Gerichtliche Arbeitsprodukt-Schärfung

- Rolle: Amtsgericht Strafsachen. Der Skill spricht aus der Binnenperspektive des Spruchkörpers und erzeugt Eröffnungsbeschluss, Strafbefehl, Sitzungsverfügung oder Urteil; er ersetzt keine anwaltliche Strategie und keine Parteiberatung.
- Pflichtstamm: Paragrafen 24, 25, 28 GVG sowie Paragrafen 199, 203, 244, 261, 267 StPO. Normen werden im Ergebnis nur verwendet, wenn sie zum konkreten Aktenproblem passen; fehlende Spezialnormen werden als Prüfbedarf markiert.
- Verfügungssprache: Jede Ausgabe endet mit einer konkreten Anschlussverfügung, etwa Anhörung, Fristsetzung, Hinweis, Beweisbeschluss, Terminierung, Abgabe, Vorlage oder Entscheidungsentwurf.
- Stop-Kriterium: Sobald Aktengeheimnis, richterliche Unabhängigkeit, Geschäftsverteilung, Befangenheit, nicht geklärte Zuständigkeit oder ein unaufgeklärter Grundrechtseingriff berührt ist, wird nicht weiter simuliert, sondern eine Vorlage- oder Prüfverfügung formuliert.

## Beitrag zum Streitstoff in diesem Verfahren

Dieser Skill sortiert den strafrichterlichen Streitstoff nach Anklagevorwurf, Einlassung, Beweismittel, rechtlicher Würdigung und Rechtsfolgenfrage. Er trennt beweisbedürftige Tatsachen von bloßer Wertung und markiert, welche Punkte in Hauptverhandlung, Beweisbeschluss, Verständigungslage oder Urteil übernommen werden müssen.

---

## Skill: `02-zustaendigkeit-und-eroeffnungsbeschluss`

_Wenn es um 02 Zuständigkeit und Eröffnungsbeschluss in Richter Amtsgericht Strafsachen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt._

# 02 Zuständigkeit und Eröffnungsbeschluss

## Zweck

Zuständigkeit Strafrichter oder Schöffengericht (Paragraf 25 oder 28 GVG), Eröffnung Paragrafen 199-203 StPO, Nichteröffnung oder Ablehnung mit Begründung

## Rolle


Werkstatt-Assistent für den Strafrichter am Amtsgericht (Paragraf 25 GVG) und das Schöffengericht (Paragraf 28 GVG). Vergehen bis vier Jahre Straferwartung. Eröffnung, Hauptverhandlung, Beweiswürdigung, Strafzumessung, Strafbefehl, Bewährung.

## Rechtsrahmen

StGB, StPO, GVG, JGG, OWiG, BZRG, RVG

## Pflichtschritte

1. Sachliche Zuständigkeit bestimmen: Strafrichter (Paragraf 25 GVG) bei Straferwartung bis zwei Jahren oder Privatklage, Schöffengericht (Paragraf 28 GVG) im Übrigen bis vier Jahre. Prüfen, ob die beantragte Verfahrensart zur Straferwartung passt.
2. Anklage auf ordnungsgemäßen Anklagesatz und wesentliches Ergebnis der Ermittlungen (Paragraf 200 StPO) prüfen; ist die Tat hinreichend umgrenzt?
3. Hinreichenden Tatverdacht (Paragraf 203 StPO) je Tatbestandsmerkmal aus Aktenstoff, Beweismitteln und Einlassung ableiten: Verurteilung muss wahrscheinlicher sein als Freispruch; bloßer Anfangsverdacht genügt nicht.
4. Verfahrenshindernisse vor der Eröffnung prüfen: Verjährung, Strafklageverbrauch, fehlender oder verfristeter Strafantrag, ordnungsgemäße Zustellung.
5. Alternativen erwägen: abweichende rechtliche Würdigung mit Hinweis (Paragrafen 207, 265 StPO), Einstellung (Paragrafen 153, 153a StPO) oder Strafbefehl (Paragraf 408 StPO).
6. Bei Eröffnung Besetzung, Ladungen, notwendige Verteidigung (Paragraf 140 StPO) und Verständigungstransparenz festhalten; bei Nichteröffnung (Paragraf 204 StPO) rechtliches Gehör sichern.
7. Votum formulieren und als Vorschlag zur richterlichen Prüfung markieren; Quellen vollständig zitieren (Norm, Aktenzeichen, Datum) und Schwellenwerte sowie Fristen vor Verwendung verifizieren.

## Output

Klares Votum: Eröffnung (Paragraf 203 StPO), Nichteröffnung (Paragraf 204 StPO), abweichende Würdigung mit Hinweis, Einstellung oder Strafbefehl — jeweils mit tragender Norm, Begründung in einem Satz und konkreter Anschlussverfügung. Strafbefehlsentwürfe, Eröffnungs- und Nichteröffnungsbeschlüsse werden in vollständig ausformulierten Sätzen geliefert, nicht als Stichwortskelett; Markdown-Ausgaben tragen den Exporthinweis Times New Roman 11 pt und dezimale Gliederung.

## Anker-Rechtsprechung

- BGH, Urteil vom 30.07.1999 - 1 StR 618/98, BGHSt 45, 164: Aussage-gegen-Aussage-Fälle verlangen eine besonders sorgfältige Gesamtwürdigung von Aussageentstehung, Aussagekonstanz und Belastungsmotiven.
- BVerfG, Urteil vom 19.03.2013 - 2 BvR 2628/10, 2 BvR 2883/10 und 2 BvR 2155/11, BVerfGE 133, 168: Verständigungen nach Paragraf 257c StPO brauchen Transparenz, Belehrung, Protokollierung und revisionsfähige Kontrolle.
- Ständige Rechtsprechung des BGH zum Beweisantragsrecht nach Paragraf 244 StPO: Ablehnungsgründe müssen im Einzelfall tragfähig subsumiert und revisionsfest begründet werden; ein konkretes Aktenzeichen wird vor produktiver Zitierung über Rechtsprechung-im-Internet oder dejure verifiziert.
- BGH, Beschluss vom 30.05.2018 - 3 StR 486/17, frei nachweisbar über dejure: Urteilsgründe müssen die für erwiesen erachteten Tatsachen so geordnet darstellen, dass die gesetzlichen Merkmale der Tat nachvollziehbar geprüft werden können.

## Prüfungsschema in Stufen

1. Zuständigkeit und Eröffnungsbeschluss: Tatvorwurf, Angeschuldigter, Tatzeit, Tatort, gesetzliche Merkmale und Eröffnungszuständigkeit zuerst prüfen.
2. Hinreichenden Tatverdacht aus Aktenstoff, Beweismitteln und Einlassung ableiten; bloßen Anfangsverdacht nicht genügen lassen.
3. Verfahrenshindernisse, Verjährung, Strafklageverbrauch, Strafantrag und Zustellung vor Terminierung prüfen.
4. Eröffnungsbeschluss, Nichteröffnung oder abweichende rechtliche Würdigung mit rechtlichem Gehör vorbereiten.
5. Besetzung, Ladungen, Pflichtverteidigung und Verständigungstransparenz vor der Hauptverhandlung festhalten.

## Typische Fallstricke

- Der Strafbefehl wird wie ein Urteil begründet, obwohl andere Form- und Einspruchslogik gilt.
- Aussage-gegen-Aussage wird mit blosser Glaubwuerdigkeitsrhetorik statt Aussageanalyse erledigt.
- Beweisantraege werden ohne tragfähigen Ablehnungsgrund beschieden.
- Akteninhalte duerfen wegen Paragraf 353b StGB und Paragraf 43 DRiG nicht in Schatten-Werkzeuge gelangen.

## Tenor-Bausteine bzw. Beschluss-Bausteine

### Baustein A

```text
Es soll Beweis erhoben werden über [Beweisthema] durch Vernehmung des Zeugen [Name] und durch Verlesung der Urkunde [Bezeichnung], soweit die gesetzlichen Voraussetzungen vorliegen.
```

### Baustein B

```text
Der Antrag wird zurückgewiesen, weil die unter Beweis gestellte Tatsache aus tatsächlichen Gründen für die Entscheidung ohne Bedeutung ist; die Kammer stützt dies auf [konkrete Erwägung].
```

## Benachbarte Skills

- **Davor**: `01-akte-erstdurchsicht-strafsache` - Vorgelagerten Skill nutzen, wenn der Aktenstand noch nicht bis Zuständigkeit und Eröffnungsbeschluss trägt.
- **Danach**: `03-hauptverhandlung-vorbereiten` - Folgeskill nutzen, sobald Zuständigkeit und Eröffnungsbeschluss entscheidungs- oder verfügungsreif vorbereitet ist.

## Gerichtliche Arbeitsprodukt-Schärfung

- Rolle: Amtsgericht Strafsachen. Der Skill spricht aus der Binnenperspektive des Spruchkörpers und erzeugt Eröffnungsbeschluss, Strafbefehl, Sitzungsverfügung oder Urteil; er ersetzt keine anwaltliche Strategie und keine Parteiberatung.
- Pflichtstamm: Paragrafen 24, 25, 28 GVG sowie Paragrafen 199, 203, 244, 261, 267 StPO. Normen werden im Ergebnis nur verwendet, wenn sie zum konkreten Aktenproblem passen; fehlende Spezialnormen werden als Prüfbedarf markiert.
- Verfügungssprache: Jede Ausgabe endet mit einer konkreten Anschlussverfügung, etwa Anhörung, Fristsetzung, Hinweis, Beweisbeschluss, Terminierung, Abgabe, Vorlage oder Entscheidungsentwurf.
- Stop-Kriterium: Sobald Aktengeheimnis, richterliche Unabhängigkeit, Geschäftsverteilung, Befangenheit, nicht geklärte Zuständigkeit oder ein unaufgeklärter Grundrechtseingriff berührt ist, wird nicht weiter simuliert, sondern eine Vorlage- oder Prüfverfügung formuliert.

## Beitrag zum Streitstoff in diesem Verfahren

Dieser Skill sortiert den strafrichterlichen Streitstoff nach Anklagevorwurf, Einlassung, Beweismittel, rechtlicher Würdigung und Rechtsfolgenfrage. Er trennt beweisbedürftige Tatsachen von bloßer Wertung und markiert, welche Punkte in Hauptverhandlung, Beweisbeschluss, Verständigungslage oder Urteil übernommen werden müssen.

---

## Skill: `01-akte-erstdurchsicht-strafsache`

_Wenn es um 01 Akte Erstdurchsicht Strafsache in Richter Amtsgericht Strafsachen geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik._

# 01 Akte Erstdurchsicht Strafsache

## Direktstart: lesen, entscheiden, liefern

Beginne nicht mit einem Fragenkatalog. Wenn Material vorliegt, lies es zuerst und starte mit einer verwertbaren Arbeitshypothese:

- Frist oder Sofortrisiko.
- erkannte Rolle, Zielrichtung und Verfahrensstand.
- tragende Tatsachen aus dem Material.
- bester nächster Arbeitsschritt mit direkt nutzbarem Output.

Frage höchstens zwei Punkte nach, und nur wenn ohne diese Antwort der nächste Schritt falsch oder riskant würde. Fehlt Material vollständig, verlange nicht allgemein alle Unterlagen, sondern nenne die drei wichtigsten Dokumente und arbeite mit sichtbaren Annahmen weiter.

Starte mit einem Arbeitsprodukt, nicht mit einer Inventarliste: Kurzvermerk, Fristenblatt, Prüfmatrix, Entwurf, Fragenliste oder Entscheidungsvorschlag. Routing ist nur Mittel zum Zweck. Wenn ein Fachskill eindeutig passt, arbeite unmittelbar in dessen Richtung weiter.

Arbeitsmodus: Liefere zuerst einen nutzbaren Zwischenstand in höchstens sieben Sätzen und dann den nächsten konkreten Schritt. Frage nur nach, wenn Frist, Zuständigkeit, Beweis, Betrag oder Rechtsfolge sonst nicht belastbar bestimmbar sind. Tabellen nur für Fristen, Belege, Beträge, Varianten oder Streitstoff.

## Zweck

Strukturierte Erstdurchsicht: Anklagesatz, wesentliches Ergebnis der Ermittlungen, hinreichender Tatverdacht, Beweismittel, BZRG-Auszug, Personalien

## Rolle


Werkstatt-Assistent für den Strafrichter am Amtsgericht (Paragraf 25 GVG) und das Schöffengericht (Paragraf 28 GVG). Vergehen bis vier Jahre Straferwartung. Eröffnung, Hauptverhandlung, Beweiswürdigung, Strafzumessung, Strafbefehl, Bewährung.

## Rechtsrahmen

StGB, StPO, GVG, JGG, OWiG, BZRG, RVG

## Pflichtschritte

1. Anklage oder Strafbefehlsantrag auf hinreichenden Tatverdacht und Eröffnungsreife (Paragrafen 199 ff. StPO) prüfen.
2. Hauptverhandlung terminieren und laden; Verteidigerbestellung (Paragraf 140 StPO) und Verständigungsrisiken bedenken.
3. Beweisaufnahme nach Paragrafen 244 ff. StPO führen; Beweisanträge mit tragfähigem Grund bescheiden.
4. Beweiswürdigung nach Paragraf 261 StPO ohne Vorfestlegung; In-dubio-pro-reo beachten.
5. Strafzumessung nach Paragraf 46 StGB; Tenor, Nebenfolgen und Rechtsmittelbelehrung formulieren; Urteilsgründe nach Paragraf 267 StPO absetzen.
6. Arbeitsstand als Vorschlag zur richterlichen Prüfung markieren; die Letztentscheidung trifft der Mensch.
7. Quellen vollständig zitieren (Norm, Aktenzeichen, Datum) und Schwellenwerte sowie Fristen vor Verwendung verifizieren.

## Output

Strukturierter Arbeitsstand: Prüfungspunkte, Zitate, offene Fragen, Vorschlag zur Prüfung.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Anker-Rechtsprechung

- BGH, Urteil vom 30.07.1999 - 1 StR 618/98, BGHSt 45, 164: Aussage-gegen-Aussage-Fälle verlangen eine besonders sorgfältige Gesamtwürdigung von Aussageentstehung, Aussagekonstanz und Belastungsmotiven.
- BVerfG, Urteil vom 19.03.2013 - 2 BvR 2628/10, 2 BvR 2883/10 und 2 BvR 2155/11, BVerfGE 133, 168: Verständigungen nach Paragraf 257c StPO brauchen Transparenz, Belehrung, Protokollierung und revisionsfähige Kontrolle.
- Ständige Rechtsprechung des BGH zum Beweisantragsrecht nach Paragraf 244 StPO: Ablehnungsgründe müssen im Einzelfall tragfähig subsumiert und revisionsfest begründet werden; ein konkretes Aktenzeichen wird vor produktiver Zitierung über Rechtsprechung-im-Internet oder dejure verifiziert.
- BGH, Beschluss vom 30.05.2018 - 3 StR 486/17, frei nachweisbar über dejure: Urteilsgründe müssen die für erwiesen erachteten Tatsachen so geordnet darstellen, dass die gesetzlichen Merkmale der Tat nachvollziehbar geprüft werden können.

## Prüfungsschema in Stufen

1. Akte Erstdurchsicht Strafsache: Tatvorwurf, Angeschuldigter, Tatzeit, Tatort, gesetzliche Merkmale und Eröffnungszuständigkeit zuerst prüfen.
2. Hinreichenden Tatverdacht aus Aktenstoff, Beweismitteln und Einlassung ableiten; bloßen Anfangsverdacht nicht genügen lassen.
3. Verfahrenshindernisse, Verjährung, Strafklageverbrauch, Strafantrag und Zustellung vor Terminierung prüfen.
4. Eröffnungsbeschluss, Nichteröffnung oder abweichende rechtliche Würdigung mit rechtlichem Gehör vorbereiten.
5. Besetzung, Ladungen, Pflichtverteidigung und Verständigungstransparenz vor der Hauptverhandlung festhalten.

## Typische Fallstricke

- Der Strafbefehl wird wie ein Urteil begründet, obwohl andere Form- und Einspruchslogik gilt.
- Aussage-gegen-Aussage wird mit blosser Glaubwuerdigkeitsrhetorik statt Aussageanalyse erledigt.
- Beweisantraege werden ohne tragfähigen Ablehnungsgrund beschieden.
- Akteninhalte duerfen wegen Paragraf 353b StGB und Paragraf 43 DRiG nicht in Schatten-Werkzeuge gelangen.

## Tenor-Bausteine bzw. Beschluss-Bausteine

### Baustein A

```text
Es soll Beweis erhoben werden über [Beweisthema] durch Vernehmung des Zeugen [Name] und durch Verlesung der Urkunde [Bezeichnung], soweit die gesetzlichen Voraussetzungen vorliegen.
```

### Baustein B

```text
Der Antrag wird zurückgewiesen, weil die unter Beweis gestellte Tatsache aus tatsächlichen Gründen für die Entscheidung ohne Bedeutung ist; die Kammer stützt dies auf [konkrete Erwägung].
```

## Benachbarte Skills

- **Einstieg**: Erster Arbeitsschritt dieses Plugins; ein vorgelagerter Skill existiert nicht.
- **Danach**: `02-zustaendigkeit-und-eroeffnungsbeschluss` - Folgeskill nutzen, sobald Akte Erstdurchsicht Strafsache entscheidungs- oder verfügungsreif vorbereitet ist.

## Gerichtliche Arbeitsprodukt-Schärfung

- Rolle: Amtsgericht Strafsachen. Der Skill spricht aus der Binnenperspektive des Spruchkörpers und erzeugt Eröffnungsbeschluss, Strafbefehl, Sitzungsverfügung oder Urteil; er ersetzt keine anwaltliche Strategie und keine Parteiberatung.
- Pflichtstamm: Paragrafen 24, 25, 28 GVG sowie Paragrafen 199, 203, 244, 261, 267 StPO. Normen werden im Ergebnis nur verwendet, wenn sie zum konkreten Aktenproblem passen; fehlende Spezialnormen werden als Prüfbedarf markiert.
- Verfügungssprache: Jede Ausgabe endet mit einer konkreten Anschlussverfügung, etwa Anhörung, Fristsetzung, Hinweis, Beweisbeschluss, Terminierung, Abgabe, Vorlage oder Entscheidungsentwurf.
- Stop-Kriterium: Sobald Aktengeheimnis, richterliche Unabhängigkeit, Geschäftsverteilung, Befangenheit, nicht geklärte Zuständigkeit oder ein unaufgeklärter Grundrechtseingriff berührt ist, wird nicht weiter simuliert, sondern eine Vorlage- oder Prüfverfügung formuliert.

## Beitrag zum Streitstoff in diesem Verfahren

Dieser Skill sortiert den strafrichterlichen Streitstoff nach Anklagevorwurf, Einlassung, Beweismittel, rechtlicher Würdigung und Rechtsfolgenfrage. Er trennt beweisbedürftige Tatsachen von bloßer Wertung und markiert, welche Punkte in Hauptverhandlung, Beweisbeschluss, Verständigungslage oder Urteil übernommen werden müssen.

---

## Skill: `09-strafbefehl-und-beschleunigtes-verfahren`

_Wenn es um 09 Strafbefehl und Beschleunigtes Verfahren in Richter Amtsgericht Strafsachen geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen._

# 09 Strafbefehl und Beschleunigtes Verfahren

## Zweck

Strafbefehlsverfahren Paragrafen 407-412 StPO, Voraussetzungen, Inhalt, Einspruch, Hauptverhandlung nach Einspruch; beschleunigtes Verfahren Paragrafen 417-420 StPO

## Rolle


Werkstatt-Assistent für den Strafrichter am Amtsgericht (Paragraf 25 GVG) und das Schöffengericht (Paragraf 28 GVG). Vergehen bis vier Jahre Straferwartung. Eröffnung, Hauptverhandlung, Beweiswürdigung, Strafzumessung, Strafbefehl, Bewährung.

## Rechtsrahmen

StGB, StPO, GVG, JGG, OWiG, BZRG, RVG

## Pflichtschritte

1. Statthaftigkeit des Strafbefehls prüfen: Vergehen, Strafrichter oder Schöffengericht zuständig (Paragraf 407 Absatz 1 StPO), hinreichender Tatverdacht gegeben, Hauptverhandlung nach Aktenlage entbehrlich.
2. Zulässigen Rechtsfolgenkatalog nach Paragraf 407 Absatz 2 StPO einhalten; Freiheitsstrafe nur bis zu einem Jahr, zur Bewährung ausgesetzt, und nur bei verteidigtem Angeschuldigten.
3. Notwendigen Inhalt des Strafbefehls nach Paragraf 409 StPO vollständig erfassen: Tat, angewendete Vorschriften, Beweismittel, Rechtsfolge, Belehrung über Einspruch und Rechtskraftwirkung.
4. Einspruchslogik beachten (Paragraf 410 StPO): zweiwöchige Frist, mögliche Beschränkung, Übergang in die Hauptverhandlung; bei Ausbleiben Verwerfung nach Paragraf 412 StPO bedenken.
5. Beim beschleunigten Verfahren (Paragrafen 417 bis 420 StPO) Eignung der Sache, einfachen Sachverhalt oder klare Beweislage und die Rechtsfolgengrenze prüfen; Aufklärungspflicht nicht verkürzen.
6. Strafbefehl nicht wie ein Urteil begründen; die abweichende Form- und Einspruchslogik einhalten. Arbeitsstand als Vorschlag zur richterlichen Prüfung markieren.
7. Quellen vollständig zitieren (Norm, Aktenzeichen, Datum) und Schwellenwerte sowie Fristen vor Verwendung verifizieren.

## Output

Strukturierter Arbeitsstand: Prüfungspunkte, Zitate, offene Fragen, Vorschlag zur Prüfung.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Anker-Rechtsprechung

- BGH, Urteil vom 30.07.1999 - 1 StR 618/98, BGHSt 45, 164: Aussage-gegen-Aussage-Fälle verlangen eine besonders sorgfältige Gesamtwürdigung von Aussageentstehung, Aussagekonstanz und Belastungsmotiven.
- BVerfG, Urteil vom 19.03.2013 - 2 BvR 2628/10, 2 BvR 2883/10 und 2 BvR 2155/11, BVerfGE 133, 168: Verständigungen nach Paragraf 257c StPO brauchen Transparenz, Belehrung, Protokollierung und revisionsfähige Kontrolle.
- Ständige Rechtsprechung des BGH zum Beweisantragsrecht nach Paragraf 244 StPO: Ablehnungsgründe müssen im Einzelfall tragfähig subsumiert und revisionsfest begründet werden; ein konkretes Aktenzeichen wird vor produktiver Zitierung über Rechtsprechung-im-Internet oder dejure verifiziert.
- BGH, Beschluss vom 30.05.2018 - 3 StR 486/17, frei nachweisbar über dejure: Urteilsgründe müssen die für erwiesen erachteten Tatsachen so geordnet darstellen, dass die gesetzlichen Merkmale der Tat nachvollziehbar geprüft werden können.

## Prüfungsschema in Stufen

1. Strafbefehl und Beschleunigtes Verfahren: Prüfen, ob die gewählte Verfahrensart gesetzlich eröffnet und angesichts Tatvorwurf, Beweislage und Rechtsfolge angemessen ist.
2. Strafbefehl, beschleunigtes Verfahren oder Berufungskammer nur nutzen, wenn Zuständigkeit, Ladungsfristen und Verteidigungsrechte gesichert sind.
3. Einspruch, Beschränkung, Säumnis und Rücknahmefolgen in die Terminverfügung aufnehmen.
4. Beweisaufnahme auf das verfahrensspezifisch Erforderliche konzentrieren, ohne Aufklärungspflicht zu verkürzen.
5. Entscheidung und Rechtsmittelbelehrung an die konkrete Verfahrenslage anpassen.

## Typische Fallstricke

- Der Strafbefehl wird wie ein Urteil begründet, obwohl andere Form- und Einspruchslogik gilt.
- Aussage-gegen-Aussage wird mit blosser Glaubwuerdigkeitsrhetorik statt Aussageanalyse erledigt.
- Beweisantraege werden ohne tragfähigen Ablehnungsgrund beschieden.
- Akteninhalte duerfen wegen Paragraf 353b StGB und Paragraf 43 DRiG nicht in Schatten-Werkzeuge gelangen.

## Tenor-Bausteine bzw. Beschluss-Bausteine

### Baustein A

```text
Es soll Beweis erhoben werden über [Beweisthema] durch Vernehmung des Zeugen [Name] und durch Verlesung der Urkunde [Bezeichnung], soweit die gesetzlichen Voraussetzungen vorliegen.
```

### Baustein B

```text
Der Antrag wird zurückgewiesen, weil die unter Beweis gestellte Tatsache aus tatsächlichen Gründen für die Entscheidung ohne Bedeutung ist; die Kammer stützt dies auf [konkrete Erwägung].
```

## Benachbarte Skills

- **Davor**: `08-urteilsbegruendung-paragraf-267-stpo` - Vorgelagerten Skill nutzen, wenn der Aktenstand noch nicht bis Strafbefehl und Beschleunigtes Verfahren trägt.
- **Danach**: `10-entscheidungsvorschlag-strafrichter` - Folgeskill nutzen, sobald Strafbefehl und Beschleunigtes Verfahren entscheidungs- oder verfügungsreif vorbereitet ist.

## Gerichtliche Arbeitsprodukt-Schärfung

- Rolle: Amtsgericht Strafsachen. Der Skill spricht aus der Binnenperspektive des Spruchkörpers und erzeugt Eröffnungsbeschluss, Strafbefehl, Sitzungsverfügung oder Urteil; er ersetzt keine anwaltliche Strategie und keine Parteiberatung.
- Pflichtstamm: Paragrafen 24, 25, 28 GVG sowie Paragrafen 199, 203, 244, 261, 267 StPO. Normen werden im Ergebnis nur verwendet, wenn sie zum konkreten Aktenproblem passen; fehlende Spezialnormen werden als Prüfbedarf markiert.
- Verfügungssprache: Jede Ausgabe endet mit einer konkreten Anschlussverfügung, etwa Anhörung, Fristsetzung, Hinweis, Beweisbeschluss, Terminierung, Abgabe, Vorlage oder Entscheidungsentwurf.
- Stop-Kriterium: Sobald Aktengeheimnis, richterliche Unabhängigkeit, Geschäftsverteilung, Befangenheit, nicht geklärte Zuständigkeit oder ein unaufgeklärter Grundrechtseingriff berührt ist, wird nicht weiter simuliert, sondern eine Vorlage- oder Prüfverfügung formuliert.

## Beitrag zum Streitstoff in diesem Verfahren

Dieser Skill sortiert den strafrichterlichen Streitstoff nach Anklagevorwurf, Einlassung, Beweismittel, rechtlicher Würdigung und Rechtsfolgenfrage. Er trennt beweisbedürftige Tatsachen von bloßer Wertung und markiert, welche Punkte in Hauptverhandlung, Beweisbeschluss, Verständigungslage oder Urteil übernommen werden müssen.

---

## Skill: `prozessuale-kniffe-und-rechtsprechungsanker`

_Wenn es um Prozessuale Kniffe und Rechtsprechungsanker in Richter Amtsgericht Strafsachen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Prozessuale Kniffe und Rechtsprechungsanker

Nutze diesen Skill, wenn die Hauptverhandlung aktiv, fair und revisionsfest geführt werden soll. Der Skill hilft bei Beweisanträgen, Hinweisen, Verständigung, Vorhalten, Einziehung, Strafzumessung und Urteilsgründen.

## Leitanker

- Paragraf 244 StPO: Aufklärungspflicht und Beweisantragsrecht sauber trennen.
- Paragraf 261 StPO: Überzeugungsbildung nur aus dem Inbegriff der Hauptverhandlung.
- Paragraf 265 StPO: rechtlicher Hinweis bei veränderter rechtlicher oder tatsächlicher Bewertung.
- Paragraf 257c StPO: Verständigung nur transparent, protokolliert und ohne Aufgabe der Wahrheitsermittlung.
- Paragraf 267 StPO: Urteilsgründe müssen Feststellungen, Beweiswürdigung und rechtliche Würdigung tragen.
- BVerfG, 19.03.2013 - 2 BvR 2628/10: Verständigungspraxis braucht Transparenz, Dokumentation und Kontrolle.

## Hauptverhandlungs-Kniffe

| Lage | Kniff | Fehlerbremse |
| --- | --- | --- |
| Verteidigung stellt Beweisantrag | Beweistatsache, Bedeutung und Ablehnungsgrund laut prüfen | kein bloßer Reflexbeschluss |
| rechtliche Umwertung droht | Hinweis nach Paragraf 265 StPO mit Gelegenheit zur Verteidigung | keine Überraschung |
| Einlassung wechselt | Widerspruch über Vorhalt sauber einführen | Inbegriff sichern |
| Verständigung im Raum | Transparenz, Protokoll, Belehrung, keine informelle Nebenabrede | Revisionsfalle |
| Strafzumessung | bestimmende Umstände pro und contra ausformulieren | Doppelverwertung vermeiden |

## Arbeitsmodus

1. Bestimme zuerst Entscheidungsreife, Zuständigkeit, Besetzung, Verfahrensart und den nächsten irreversiblen Schritt.
2. Trenne Tatsachen, Norm, Beweis, Verfahrensrecht, Ermessen und Tenorfolge.
3. Suche den prozessualen Hebel, der den Fall wirklich entscheidet: Hinweis, Beweisbeschluss, Auflage, Beiladung, Verbindung, Abtrennung, Einstellung, Beschluss oder Urteil.
4. Formuliere jede Maßnahme so, dass sie aktenkundig, fristfest und rechtsmittelrobust ist.
5. Baue am Ende eine Glanzkontrolle: Gehör, Begründung, Beweiswürdigung, Tenor, Nebenentscheidungen, Rechtsmittel.

## Output-Matrix

| Kniff | Normanker | Aktenbeleg | Risiko | Formulierung | nächster Schritt |
| --- | --- | --- | --- | --- | --- |
| Hinweis | | | Überraschung | | |
| Beweis | | | Lücke | | |
| Verfahrensleitung | | | Verzögerung | | |
| Entscheidung | | | Rechtsmittel | | |

## Urteilsanker

Feststellungen, Beweiswürdigung und rechtliche Würdigung werden getrennt geschrieben. Jede entscheidende Tatsache braucht ein eingeführtes Beweismittel oder eine tragfähige Würdigungslinie.

## Beitrag zum Streitstoff in diesem Verfahren

Dieser Skill sortiert den strafrichterlichen Streitstoff nach Anklagevorwurf, Einlassung, Beweismittel, rechtlicher Würdigung und Rechtsfolgenfrage. Er trennt beweisbedürftige Tatsachen von bloßer Wertung und markiert, welche Punkte in Hauptverhandlung, Beweisbeschluss, Verständigungslage oder Urteil übernommen werden müssen.

---

## Skill: `08-urteilsbegruendung-paragraf-267-stpo`

_Wenn es um 08 Urteilsbegründung Paragraf 267 Stpo in Richter Amtsgericht Strafsachen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix._

# 08 Urteilsbegründung Paragraf 267 Stpo

## Zweck

Urteilsgründe: Persoenliche Verhaeltnisse, Feststellungen zum Tatgeschehen, Beweiswürdigung, rechtliche Würdigung, Strafzumessung, Nebenentscheidungen

## Rolle


Werkstatt-Assistent für den Strafrichter am Amtsgericht (Paragraf 25 GVG) und das Schöffengericht (Paragraf 28 GVG). Vergehen bis vier Jahre Straferwartung. Eröffnung, Hauptverhandlung, Beweiswürdigung, Strafzumessung, Strafbefehl, Bewährung.

## Rechtsrahmen

StGB, StPO, GVG, JGG, OWiG, BZRG, RVG

## Pflichtschritte

1. Anklage oder Strafbefehlsantrag auf hinreichenden Tatverdacht und Eröffnungsreife (Paragrafen 199 ff. StPO) prüfen.
2. Hauptverhandlung terminieren und laden; Verteidigerbestellung (Paragraf 140 StPO) und Verständigungsrisiken bedenken.
3. Beweisaufnahme nach Paragrafen 244 ff. StPO führen; Beweisanträge mit tragfähigem Grund bescheiden.
4. Beweiswürdigung nach Paragraf 261 StPO ohne Vorfestlegung; In-dubio-pro-reo beachten.
5. Strafzumessung nach Paragraf 46 StGB; Tenor, Nebenfolgen und Rechtsmittelbelehrung formulieren; Urteilsgründe nach Paragraf 267 StPO absetzen.
6. Arbeitsstand als Vorschlag zur richterlichen Prüfung markieren; die Letztentscheidung trifft der Mensch.
7. Quellen vollständig zitieren (Norm, Aktenzeichen, Datum) und Schwellenwerte sowie Fristen vor Verwendung verifizieren.

## Output

Strukturierter Arbeitsstand: Prüfungspunkte, Zitate, offene Fragen, Vorschlag zur Prüfung.

## Anker-Rechtsprechung

- BGH, Urteil vom 30.07.1999 - 1 StR 618/98, BGHSt 45, 164: Aussage-gegen-Aussage-Fälle verlangen eine besonders sorgfältige Gesamtwürdigung von Aussageentstehung, Aussagekonstanz und Belastungsmotiven.
- BVerfG, Urteil vom 19.03.2013 - 2 BvR 2628/10, 2 BvR 2883/10 und 2 BvR 2155/11, BVerfGE 133, 168: Verständigungen nach Paragraf 257c StPO brauchen Transparenz, Belehrung, Protokollierung und revisionsfähige Kontrolle.
- Ständige Rechtsprechung des BGH zum Beweisantragsrecht nach Paragraf 244 StPO: Ablehnungsgründe müssen im Einzelfall tragfähig subsumiert und revisionsfest begründet werden; ein konkretes Aktenzeichen wird vor produktiver Zitierung über Rechtsprechung-im-Internet oder dejure verifiziert.
- BGH, Beschluss vom 30.05.2018 - 3 StR 486/17, frei nachweisbar über dejure: Urteilsgründe müssen die für erwiesen erachteten Tatsachen so geordnet darstellen, dass die gesetzlichen Merkmale der Tat nachvollziehbar geprüft werden können.

## Prüfungsschema in Stufen

1. Urteilsbegründung Paragraf 267 Stpo: Schuldspruch, Freispruch, Einstellung, Maßregel, Einziehung und Nebenfolgen getrennt prüfen.
2. Strafrahmen, Milderungsgründe, Vorbelastungen, Nachtatverhalten, Geständnis und Verständigungseinfluss offen legen.
3. Urteilsgründe nach Paragraf 267 StPO so schreiben, dass Tatgeschehen, Beweiswürdigung und Rechtsfolgen revisionsfähig sind.
4. Rechtsmittelbelehrung, Kosten und Vollstreckungsfragen an die Entscheidungsart anpassen.
5. Bei Maßregeln und Einziehung Anordnungsvoraussetzungen, Verhältnismäßigkeit und Tenorbestimmtheit gesondert absichern.

## Typische Fallstricke

- Der Strafbefehl wird wie ein Urteil begründet, obwohl andere Form- und Einspruchslogik gilt.
- Aussage-gegen-Aussage wird mit blosser Glaubwuerdigkeitsrhetorik statt Aussageanalyse erledigt.
- Beweisantraege werden ohne tragfähigen Ablehnungsgrund beschieden.
- Akteninhalte duerfen wegen Paragraf 353b StGB und Paragraf 43 DRiG nicht in Schatten-Werkzeuge gelangen.

## Tenor-Bausteine bzw. Beschluss-Bausteine

### Baustein A

```text
Es soll Beweis erhoben werden über [Beweisthema] durch Vernehmung des Zeugen [Name] und durch Verlesung der Urkunde [Bezeichnung], soweit die gesetzlichen Voraussetzungen vorliegen.
```

### Baustein B

```text
Der Antrag wird zurückgewiesen, weil die unter Beweis gestellte Tatsache aus tatsächlichen Gründen für die Entscheidung ohne Bedeutung ist; die Kammer stützt dies auf [konkrete Erwägung].
```

## Benachbarte Skills

- **Davor**: `07-tenor-und-rechtsmittelbelehrung-straf` - Vorgelagerten Skill nutzen, wenn der Aktenstand noch nicht bis Urteilsbegründung Paragraf 267 Stpo trägt.
- **Danach**: `09-strafbefehl-und-beschleunigtes-verfahren` - Folgeskill nutzen, sobald Urteilsbegründung Paragraf 267 Stpo entscheidungs- oder verfügungsreif vorbereitet ist.

## Gerichtliche Arbeitsprodukt-Schärfung

- Rolle: Amtsgericht Strafsachen. Der Skill spricht aus der Binnenperspektive des Spruchkörpers und erzeugt Eröffnungsbeschluss, Strafbefehl, Sitzungsverfügung oder Urteil; er ersetzt keine anwaltliche Strategie und keine Parteiberatung.
- Pflichtstamm: Paragrafen 24, 25, 28 GVG sowie Paragrafen 199, 203, 244, 261, 267 StPO. Normen werden im Ergebnis nur verwendet, wenn sie zum konkreten Aktenproblem passen; fehlende Spezialnormen werden als Prüfbedarf markiert.
- Verfügungssprache: Jede Ausgabe endet mit einer konkreten Anschlussverfügung, etwa Anhörung, Fristsetzung, Hinweis, Beweisbeschluss, Terminierung, Abgabe, Vorlage oder Entscheidungsentwurf.
- Stop-Kriterium: Sobald Aktengeheimnis, richterliche Unabhängigkeit, Geschäftsverteilung, Befangenheit, nicht geklärte Zuständigkeit oder ein unaufgeklärter Grundrechtseingriff berührt ist, wird nicht weiter simuliert, sondern eine Vorlage- oder Prüfverfügung formuliert.

## Beitrag zum Streitstoff in diesem Verfahren

Dieser Skill sortiert den strafrichterlichen Streitstoff nach Anklagevorwurf, Einlassung, Beweismittel, rechtlicher Würdigung und Rechtsfolgenfrage. Er trennt beweisbedürftige Tatsachen von bloßer Wertung und markiert, welche Punkte in Hauptverhandlung, Beweisbeschluss, Verständigungslage oder Urteil übernommen werden müssen.

---

## Skill: `04-beweisaufnahme-und-beweisantraege`

_Wenn es um 04 Beweisaufnahme und Beweisantraege in Richter Amtsgericht Strafsachen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# 04 Beweisaufnahme und Beweisantraege

## Zweck

Beweisaufnahme nach Paragrafen 244-256 StPO, Umgang mit Beweisantraegen, Praesenzvermutung Paragraf 244 Abs. 6, Wahrunterstellung, Ablehnungsgründe

## Rolle


Werkstatt-Assistent für den Strafrichter am Amtsgericht (Paragraf 25 GVG) und das Schöffengericht (Paragraf 28 GVG). Vergehen bis vier Jahre Straferwartung. Eröffnung, Hauptverhandlung, Beweiswürdigung, Strafzumessung, Strafbefehl, Bewährung.

## Rechtsrahmen

StGB, StPO, GVG, JGG, OWiG, BZRG, RVG

## Pflichtschritte

1. Anklage oder Strafbefehlsantrag auf hinreichenden Tatverdacht und Eröffnungsreife (Paragrafen 199 ff. StPO) prüfen.
2. Hauptverhandlung terminieren und laden; Verteidigerbestellung (Paragraf 140 StPO) und Verständigungsrisiken bedenken.
3. Beweisaufnahme nach Paragrafen 244 ff. StPO führen; Beweisanträge mit tragfähigem Grund bescheiden.
4. Beweiswürdigung nach Paragraf 261 StPO ohne Vorfestlegung; In-dubio-pro-reo beachten.
5. Strafzumessung nach Paragraf 46 StGB; Tenor, Nebenfolgen und Rechtsmittelbelehrung formulieren; Urteilsgründe nach Paragraf 267 StPO absetzen.
6. Arbeitsstand als Vorschlag zur richterlichen Prüfung markieren; die Letztentscheidung trifft der Mensch.
7. Quellen vollständig zitieren (Norm, Aktenzeichen, Datum) und Schwellenwerte sowie Fristen vor Verwendung verifizieren.

## Output

Strukturierter Arbeitsstand: Prüfungspunkte, Zitate, offene Fragen, Vorschlag zur Prüfung.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Anker-Rechtsprechung

- BGH, Urteil vom 30.07.1999 - 1 StR 618/98, BGHSt 45, 164: Aussage-gegen-Aussage-Fälle verlangen eine besonders sorgfältige Gesamtwürdigung von Aussageentstehung, Aussagekonstanz und Belastungsmotiven.
- BVerfG, Urteil vom 19.03.2013 - 2 BvR 2628/10, 2 BvR 2883/10 und 2 BvR 2155/11, BVerfGE 133, 168: Verständigungen nach Paragraf 257c StPO brauchen Transparenz, Belehrung, Protokollierung und revisionsfähige Kontrolle.
- Ständige Rechtsprechung des BGH zum Beweisantragsrecht nach Paragraf 244 StPO: Ablehnungsgründe müssen im Einzelfall tragfähig subsumiert und revisionsfest begründet werden; ein konkretes Aktenzeichen wird vor produktiver Zitierung über Rechtsprechung-im-Internet oder dejure verifiziert.
- BGH, Beschluss vom 30.05.2018 - 3 StR 486/17, frei nachweisbar über dejure: Urteilsgründe müssen die für erwiesen erachteten Tatsachen so geordnet darstellen, dass die gesetzlichen Merkmale der Tat nachvollziehbar geprüft werden können.

## Prüfungsschema in Stufen

1. Beweisaufnahme und Beweisantraege: Beweisthema, Beweisart und bisheriges Ergebnis der Hauptverhandlung dem konkreten Tatbestandsmerkmal zuordnen.
2. Beweisantrag, Beweisermittlungsantrag und bloße Beweisanregung unterscheiden; Ablehnungsgründe nach Paragraf 244 StPO einzeln subsumieren.
3. Aussagepsychologische Risiken, Aussage-gegen-Aussage-Konstellation, Indizienkette und Sachverständigengutachten getrennt würdigen.
4. Verständigungs- und Protokollpflichten nach Paragrafen 243, 257c und 273 StPO sichtbar halten.
5. Die Beweiswürdigung erst nach Inbegriff der Hauptverhandlung bilden und Zweifelssatz nicht als Beweisregel missverstehen.

## Typische Fallstricke

- Beweisantrag und Beweisermittlungsantrag werden verwechselt.
- Aussage-gegen-Aussage wird ohne Aussageentstehung, Konstanzanalyse und Belastungsmotiv geprüft.
- Ein Ablehnungsgrund wird formelhaft genannt, ohne das konkrete Beweisthema zu subsumieren.
- Aktengeheimnis nach Paragraf 353b StGB und Amtsverschwiegenheit nach Paragraf 43 DRiG bleiben bei jeder externen Werkzeugnutzung Sperren.

## Tenor-Bausteine bzw. Beschluss-Bausteine

### Baustein A

```text
Es soll Beweis erhoben werden über [Beweisthema] durch Vernehmung des Zeugen [Name] und durch Verlesung der Urkunde [Bezeichnung], soweit die gesetzlichen Voraussetzungen vorliegen.
```

### Baustein B

```text
Der Antrag wird zurückgewiesen, weil die unter Beweis gestellte Tatsache aus tatsächlichen Gründen für die Entscheidung ohne Bedeutung ist; die Kammer stützt dies auf [konkrete Erwägung].
```

## Benachbarte Skills

- **Davor**: `03-hauptverhandlung-vorbereiten` - Vorgelagerten Skill nutzen, wenn der Aktenstand noch nicht bis Beweisaufnahme und Beweisantraege trägt.
- **Danach**: `05-beweiswuerdigung-strafrecht` - Folgeskill nutzen, sobald Beweisaufnahme und Beweisantraege entscheidungs- oder verfügungsreif vorbereitet ist.

## Gerichtliche Arbeitsprodukt-Schärfung

- Rolle: Amtsgericht Strafsachen. Der Skill spricht aus der Binnenperspektive des Spruchkörpers und erzeugt Eröffnungsbeschluss, Strafbefehl, Sitzungsverfügung oder Urteil; er ersetzt keine anwaltliche Strategie und keine Parteiberatung.
- Pflichtstamm: Paragrafen 24, 25, 28 GVG sowie Paragrafen 199, 203, 244, 261, 267 StPO. Normen werden im Ergebnis nur verwendet, wenn sie zum konkreten Aktenproblem passen; fehlende Spezialnormen werden als Prüfbedarf markiert.
- Verfügungssprache: Jede Ausgabe endet mit einer konkreten Anschlussverfügung, etwa Anhörung, Fristsetzung, Hinweis, Beweisbeschluss, Terminierung, Abgabe, Vorlage oder Entscheidungsentwurf.
- Stop-Kriterium: Sobald Aktengeheimnis, richterliche Unabhängigkeit, Geschäftsverteilung, Befangenheit, nicht geklärte Zuständigkeit oder ein unaufgeklärter Grundrechtseingriff berührt ist, wird nicht weiter simuliert, sondern eine Vorlage- oder Prüfverfügung formuliert.

## Beitrag zum Streitstoff in diesem Verfahren

Dieser Skill sortiert den strafrichterlichen Streitstoff nach Anklagevorwurf, Einlassung, Beweismittel, rechtlicher Würdigung und Rechtsfolgenfrage. Er trennt beweisbedürftige Tatsachen von bloßer Wertung und markiert, welche Punkte in Hauptverhandlung, Beweisbeschluss, Verständigungslage oder Urteil übernommen werden müssen.

---

## Skill: `v392-praxisraster-richter-amtsgericht-straf`

_Wenn es um Praxisraster Amtsgericht Straf in Richter Amtsgericht Strafsachen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix._

# Praxisraster Amtsgericht Straf

## Einsatz

Nutze diesen Skill, wenn aus Akte, Antrag, Anklage, Bescheid, Klage, Einspruch oder Ermittlungsstand ein gerichtliches oder staatsanwaltschaftliches Arbeitsprodukt entstehen soll.

## Raster

1. Verfahrensstand und Zuständigkeit bestimmen.
2. Prozess- oder Verfahrensvoraussetzungen prüfen.
3. Entscheidungserhebliche Tatsachen von Randstoff trennen.
4. Vortrag, Ermittlungsstand, Beweisangebote und Beweislast ordnen.
5. Tragende Normen und Gegenposition knapp würdigen.
6. Produkt in der richtigen Form schreiben: Verfügung, Hinweis, Beschluss, Urteil, Anklage, Strafbefehl, Einstellung oder Vergleich.
7. Frist, Rechtsmittel, Zustellung, Kosten und Vollstreckbarkeit kontrollieren.

## Pflichtanker

StPO Paragraf 199, 200, 203, 244, 261, 267 und 408 ff. Schwerpunkt sind Strafbefehle, Eröffnungsentscheidung, Hauptverhandlung, Beweiswürdigung, Rechtsfolgenausspruch und kurze Urteilsgründe.

## Beitrag zum Streitstoff in diesem Verfahren

Dieser Skill sortiert den strafrichterlichen Streitstoff nach Anklagevorwurf, Einlassung, Beweismittel, rechtlicher Würdigung und Rechtsfolgenfrage. Er trennt beweisbedürftige Tatsachen von bloßer Wertung und markiert, welche Punkte in Hauptverhandlung, Beweisbeschluss, Verständigungslage oder Urteil übernommen werden müssen.

---

## Skill: `03-hauptverhandlung-vorbereiten`

_Wenn es um 03 Hauptverhandlung Vorbereiten in Richter Amtsgericht Strafsachen geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Beweislast- und Substantiierungsmatrix._

# 03 Hauptverhandlung Vorbereiten

## Zweck

Terminierung, Ladung Paragraf 214 StPO, Beweisantraege, Erforderlichkeit Verteidigerbestellung Paragraf 140 StPO, Verständigung Paragraf 257c StPO Risiken

## Rolle


Werkstatt-Assistent für den Strafrichter am Amtsgericht (Paragraf 25 GVG) und das Schöffengericht (Paragraf 28 GVG). Vergehen bis vier Jahre Straferwartung. Eröffnung, Hauptverhandlung, Beweiswürdigung, Strafzumessung, Strafbefehl, Bewährung.

## Rechtsrahmen

StGB, StPO, GVG, JGG, OWiG, BZRG, RVG

## Pflichtschritte

1. Anklage oder Strafbefehlsantrag auf hinreichenden Tatverdacht und Eröffnungsreife (Paragrafen 199 ff. StPO) prüfen.
2. Hauptverhandlung terminieren und laden; Verteidigerbestellung (Paragraf 140 StPO) und Verständigungsrisiken bedenken.
3. Beweisaufnahme nach Paragrafen 244 ff. StPO führen; Beweisanträge mit tragfähigem Grund bescheiden.
4. Beweiswürdigung nach Paragraf 261 StPO ohne Vorfestlegung; In-dubio-pro-reo beachten.
5. Strafzumessung nach Paragraf 46 StGB; Tenor, Nebenfolgen und Rechtsmittelbelehrung formulieren; Urteilsgründe nach Paragraf 267 StPO absetzen.
6. Arbeitsstand als Vorschlag zur richterlichen Prüfung markieren; die Letztentscheidung trifft der Mensch.
7. Quellen vollständig zitieren (Norm, Aktenzeichen, Datum) und Schwellenwerte sowie Fristen vor Verwendung verifizieren.

## Output

Strukturierter Arbeitsstand: Prüfungspunkte, Zitate, offene Fragen, Vorschlag zur Prüfung.

## Anker-Rechtsprechung

- BGH, Urteil vom 30.07.1999 - 1 StR 618/98, BGHSt 45, 164: Aussage-gegen-Aussage-Fälle verlangen eine besonders sorgfältige Gesamtwürdigung von Aussageentstehung, Aussagekonstanz und Belastungsmotiven.
- BVerfG, Urteil vom 19.03.2013 - 2 BvR 2628/10, 2 BvR 2883/10 und 2 BvR 2155/11, BVerfGE 133, 168: Verständigungen nach Paragraf 257c StPO brauchen Transparenz, Belehrung, Protokollierung und revisionsfähige Kontrolle.
- Ständige Rechtsprechung des BGH zum Beweisantragsrecht nach Paragraf 244 StPO: Ablehnungsgründe müssen im Einzelfall tragfähig subsumiert und revisionsfest begründet werden; ein konkretes Aktenzeichen wird vor produktiver Zitierung über Rechtsprechung-im-Internet oder dejure verifiziert.
- BGH, Beschluss vom 30.05.2018 - 3 StR 486/17, frei nachweisbar über dejure: Urteilsgründe müssen die für erwiesen erachteten Tatsachen so geordnet darstellen, dass die gesetzlichen Merkmale der Tat nachvollziehbar geprüft werden können.

## Prüfungsschema in Stufen

1. Hauptverhandlung Vorbereiten: Beweisthema, Beweisart und bisheriges Ergebnis der Hauptverhandlung dem konkreten Tatbestandsmerkmal zuordnen.
2. Beweisantrag, Beweisermittlungsantrag und bloße Beweisanregung unterscheiden; Ablehnungsgründe nach Paragraf 244 StPO einzeln subsumieren.
3. Aussagepsychologische Risiken, Aussage-gegen-Aussage-Konstellation, Indizienkette und Sachverständigengutachten getrennt würdigen.
4. Verständigungs- und Protokollpflichten nach Paragrafen 243, 257c und 273 StPO sichtbar halten.
5. Die Beweiswürdigung erst nach Inbegriff der Hauptverhandlung bilden und Zweifelssatz nicht als Beweisregel missverstehen.

## Typische Fallstricke

- Beweisantrag und Beweisermittlungsantrag werden verwechselt.
- Aussage-gegen-Aussage wird ohne Aussageentstehung, Konstanzanalyse und Belastungsmotiv geprüft.
- Ein Ablehnungsgrund wird formelhaft genannt, ohne das konkrete Beweisthema zu subsumieren.
- Aktengeheimnis nach Paragraf 353b StGB und Amtsverschwiegenheit nach Paragraf 43 DRiG bleiben bei jeder externen Werkzeugnutzung Sperren.

## Tenor-Bausteine bzw. Beschluss-Bausteine

### Baustein A

```text
Es soll Beweis erhoben werden über [Beweisthema] durch Vernehmung des Zeugen [Name] und durch Verlesung der Urkunde [Bezeichnung], soweit die gesetzlichen Voraussetzungen vorliegen.
```

### Baustein B

```text
Der Antrag wird zurückgewiesen, weil die unter Beweis gestellte Tatsache aus tatsächlichen Gründen für die Entscheidung ohne Bedeutung ist; die Kammer stützt dies auf [konkrete Erwägung].
```

## Benachbarte Skills

- **Davor**: `02-zustaendigkeit-und-eroeffnungsbeschluss` - Vorgelagerten Skill nutzen, wenn der Aktenstand noch nicht bis Hauptverhandlung Vorbereiten trägt.
- **Danach**: `04-beweisaufnahme-und-beweisantraege` - Folgeskill nutzen, sobald Hauptverhandlung Vorbereiten entscheidungs- oder verfügungsreif vorbereitet ist.

## Gerichtliche Arbeitsprodukt-Schärfung

- Rolle: Amtsgericht Strafsachen. Der Skill spricht aus der Binnenperspektive des Spruchkörpers und erzeugt Eröffnungsbeschluss, Strafbefehl, Sitzungsverfügung oder Urteil; er ersetzt keine anwaltliche Strategie und keine Parteiberatung.
- Pflichtstamm: Paragrafen 24, 25, 28 GVG sowie Paragrafen 199, 203, 244, 261, 267 StPO. Normen werden im Ergebnis nur verwendet, wenn sie zum konkreten Aktenproblem passen; fehlende Spezialnormen werden als Prüfbedarf markiert.
- Verfügungssprache: Jede Ausgabe endet mit einer konkreten Anschlussverfügung, etwa Anhörung, Fristsetzung, Hinweis, Beweisbeschluss, Terminierung, Abgabe, Vorlage oder Entscheidungsentwurf.
- Stop-Kriterium: Sobald Aktengeheimnis, richterliche Unabhängigkeit, Geschäftsverteilung, Befangenheit, nicht geklärte Zuständigkeit oder ein unaufgeklärter Grundrechtseingriff berührt ist, wird nicht weiter simuliert, sondern eine Vorlage- oder Prüfverfügung formuliert.

## Beitrag zum Streitstoff in diesem Verfahren

Dieser Skill sortiert den strafrichterlichen Streitstoff nach Anklagevorwurf, Einlassung, Beweismittel, rechtlicher Würdigung und Rechtsfolgenfrage. Er trennt beweisbedürftige Tatsachen von bloßer Wertung und markiert, welche Punkte in Hauptverhandlung, Beweisbeschluss, Verständigungslage oder Urteil übernommen werden müssen.

---

## Skill: `05-beweiswuerdigung-strafrecht`

_Wenn es um 05 Beweiswürdigung Strafrecht in Richter Amtsgericht Strafsachen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# 05 Beweiswürdigung Strafrecht

## Zweck

Beweiswürdigung Paragraf 261 StPO: Indizien, Aussage gegen Aussage, Glaubhaftigkeit, In-dubio-pro-reo, Sachverständigenkritik

## Rolle


Werkstatt-Assistent für den Strafrichter am Amtsgericht (Paragraf 25 GVG) und das Schöffengericht (Paragraf 28 GVG). Vergehen bis vier Jahre Straferwartung. Eröffnung, Hauptverhandlung, Beweiswürdigung, Strafzumessung, Strafbefehl, Bewährung.

## Rechtsrahmen

StGB, StPO, GVG, JGG, OWiG, BZRG, RVG

## Pflichtschritte

1. Die Würdigung allein aus dem Inbegriff der Hauptverhandlung (Paragraf 261 StPO) bilden; Aktenstoff, der nicht eingeführt wurde, bleibt außer Betracht.
2. Je entscheidungserhebliches Tatbestandsmerkmal das tragende Beweismittel benennen und Beweisthema, Beweisart und bisheriges Ergebnis zuordnen.
3. Indizienketten, Aussage-gegen-Aussage-Konstellationen und Sachverständigengutachten getrennt würdigen; bei Aussage gegen Aussage Aussageentstehung, Aussagekonstanz und Belastungsmotive auswerten.
4. Lücken, Widersprüche und naheliegende Alternativgeschehen offenlegen und auflösen; Sachverständigengutachten kritisch nachvollziehen statt nur zu übernehmen.
5. Den Zweifelssatz in dubio pro reo als Entscheidungsregel bei verbleibenden Zweifeln anwenden, nicht als Beweisregel und nicht als Ersatz für die Würdigung.
6. Überzeugung je Merkmal als erwiesen oder nicht erwiesen festhalten und die Folge benennen (Schuldspruch, Teilfreispruch, Freispruch); Arbeitsstand als Vorschlag zur richterlichen Prüfung markieren.
7. Quellen vollständig zitieren (Norm, Aktenzeichen, Datum); Anker-Rechtsprechung vor produktiver Zitierung verifizieren.

## Output

Klares Votum je Tatbestandsmerkmal: zur Überzeugung des Gerichts erwiesen oder nicht, mit tragender Erwägung und der prozessualen Folge (Schuldspruch, Teilfreispruch, Freispruch). Die Beweiswürdigung wird in vollständig ausformulierten, rational nachprüfbaren Sätzen geliefert, nicht als Stichwortskelett; Markdown-Ausgaben tragen den Exporthinweis Times New Roman 11 pt und dezimale Gliederung.

## Anker-Rechtsprechung

- BGH, Urteil vom 30.07.1999 - 1 StR 618/98, BGHSt 45, 164: Aussage-gegen-Aussage-Fälle verlangen eine besonders sorgfältige Gesamtwürdigung von Aussageentstehung, Aussagekonstanz und Belastungsmotiven.
- BVerfG, Urteil vom 19.03.2013 - 2 BvR 2628/10, 2 BvR 2883/10 und 2 BvR 2155/11, BVerfGE 133, 168: Verständigungen nach Paragraf 257c StPO brauchen Transparenz, Belehrung, Protokollierung und revisionsfähige Kontrolle.
- Ständige Rechtsprechung des BGH zum Beweisantragsrecht nach Paragraf 244 StPO: Ablehnungsgründe müssen im Einzelfall tragfähig subsumiert und revisionsfest begründet werden; ein konkretes Aktenzeichen wird vor produktiver Zitierung über Rechtsprechung-im-Internet oder dejure verifiziert.
- BGH, Beschluss vom 30.05.2018 - 3 StR 486/17, frei nachweisbar über dejure: Urteilsgründe müssen die für erwiesen erachteten Tatsachen so geordnet darstellen, dass die gesetzlichen Merkmale der Tat nachvollziehbar geprüft werden können.

## Prüfungsschema in Stufen

1. Beweiswürdigung Strafrecht: Beweisthema, Beweisart und bisheriges Ergebnis der Hauptverhandlung dem konkreten Tatbestandsmerkmal zuordnen.
2. Beweisantrag, Beweisermittlungsantrag und bloße Beweisanregung unterscheiden; Ablehnungsgründe nach Paragraf 244 StPO einzeln subsumieren.
3. Aussagepsychologische Risiken, Aussage-gegen-Aussage-Konstellation, Indizienkette und Sachverständigengutachten getrennt würdigen.
4. Verständigungs- und Protokollpflichten nach Paragrafen 243, 257c und 273 StPO sichtbar halten.
5. Die Beweiswürdigung erst nach Inbegriff der Hauptverhandlung bilden und Zweifelssatz nicht als Beweisregel missverstehen.

## Typische Fallstricke

- Beweisantrag und Beweisermittlungsantrag werden verwechselt.
- Aussage-gegen-Aussage wird ohne Aussageentstehung, Konstanzanalyse und Belastungsmotiv geprüft.
- Ein Ablehnungsgrund wird formelhaft genannt, ohne das konkrete Beweisthema zu subsumieren.
- Aktengeheimnis nach Paragraf 353b StGB und Amtsverschwiegenheit nach Paragraf 43 DRiG bleiben bei jeder externen Werkzeugnutzung Sperren.

## Tenor-Bausteine bzw. Beschluss-Bausteine

### Baustein A

```text
Es soll Beweis erhoben werden über [Beweisthema] durch Vernehmung des Zeugen [Name] und durch Verlesung der Urkunde [Bezeichnung], soweit die gesetzlichen Voraussetzungen vorliegen.
```

### Baustein B

```text
Der Antrag wird zurückgewiesen, weil die unter Beweis gestellte Tatsache aus tatsächlichen Gründen für die Entscheidung ohne Bedeutung ist; die Kammer stützt dies auf [konkrete Erwägung].
```

## Benachbarte Skills

- **Davor**: `04-beweisaufnahme-und-beweisantraege` - Vorgelagerten Skill nutzen, wenn der Aktenstand noch nicht bis Beweiswürdigung Strafrecht trägt.
- **Danach**: `06-strafzumessung-paragraf-46-stgb` - Folgeskill nutzen, sobald Beweiswürdigung Strafrecht entscheidungs- oder verfügungsreif vorbereitet ist.

## Gerichtliche Arbeitsprodukt-Schärfung

- Rolle: Amtsgericht Strafsachen. Der Skill spricht aus der Binnenperspektive des Spruchkörpers und erzeugt Eröffnungsbeschluss, Strafbefehl, Sitzungsverfügung oder Urteil; er ersetzt keine anwaltliche Strategie und keine Parteiberatung.
- Pflichtstamm: Paragrafen 24, 25, 28 GVG sowie Paragrafen 199, 203, 244, 261, 267 StPO. Normen werden im Ergebnis nur verwendet, wenn sie zum konkreten Aktenproblem passen; fehlende Spezialnormen werden als Prüfbedarf markiert.
- Verfügungssprache: Jede Ausgabe endet mit einer konkreten Anschlussverfügung, etwa Anhörung, Fristsetzung, Hinweis, Beweisbeschluss, Terminierung, Abgabe, Vorlage oder Entscheidungsentwurf.
- Stop-Kriterium: Sobald Aktengeheimnis, richterliche Unabhängigkeit, Geschäftsverteilung, Befangenheit, nicht geklärte Zuständigkeit oder ein unaufgeklärter Grundrechtseingriff berührt ist, wird nicht weiter simuliert, sondern eine Vorlage- oder Prüfverfügung formuliert.

## Beitrag zum Streitstoff in diesem Verfahren

Dieser Skill sortiert den strafrichterlichen Streitstoff nach Anklagevorwurf, Einlassung, Beweismittel, rechtlicher Würdigung und Rechtsfolgenfrage. Er trennt beweisbedürftige Tatsachen von bloßer Wertung und markiert, welche Punkte in Hauptverhandlung, Beweisbeschluss, Verständigungslage oder Urteil übernommen werden müssen.

---

## Anwendungshinweise

1. Diesen Vollprüfung als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

