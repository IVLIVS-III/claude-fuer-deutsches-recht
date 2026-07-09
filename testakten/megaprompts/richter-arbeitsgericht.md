# Vollprüfung: richter-arbeitsgericht

## Zusammensetzung

Dieser Vollprüfung enthaelt alle 13 Skills des Plugins `richter-arbeitsgericht`.

## Inhaltsverzeichnis

1. **99-finale-entscheidung-volltext** — Wenn es um Finale Entscheidung als Volltext (Urteil Arbeitsgericht) in Arbeitsgericht geht: ordnet Sachverhalt, Norm, Be…
2. **03-zahlungsklage-lohn-und-gehalt** — Wenn es um 03 Zahlungsklage Lohn und Gehalt in Arbeitsgericht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm…
3. **07-einstweilige-verfuegung-arbeitsrecht** — Wenn es um 07 Einstweilige Verfügung Arbeitsrecht in Arbeitsgericht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenarg…
4. **10-entscheidungsvorschlag-arbeitsgericht** — Wenn es um 10 Entscheidungsvorschlag Arbeitsgericht in Arbeitsgericht geht: entwickelt Verhandlungsziel, Vergleichskorri…
5. **prozessuale-kniffe-und-rechtsprechungsanker** — Wenn es um Prozessuale Kniffe und Rechtsprechungsanker in Arbeitsgericht geht: entwickelt Verhandlungsziel, Vergleichsko…
6. **08-betriebsverfassung-beschlussverfahren** — Wenn es um 08 Betriebsverfassung Beschlussverfahren in Arbeitsgericht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg …
7. **02-kuendigungsschutzklage-pruefen** — Wenn es um 02 Kündigungsschutzklage Prüfen in Arbeitsgericht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm,…
8. **01-zustaendigkeit-und-guetetermin** — Wenn es um 01 Zuständigkeit und Guetetermin in Arbeitsgericht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofo…
9. **v392-praxisraster-richter-arbeitsgericht** — Wenn es um Praxisraster Arbeitsgericht in Arbeitsgericht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und …
10. **04-betriebsuebergang-und-tarif** — Wenn es um 04 Betriebsübergang und Tarif in Arbeitsgericht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortm…
11. **05-befristung-und-teilzeit** — Wenn es um 05 Befristung und Teilzeit in Arbeitsgericht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßn…
12. **09-urteil-arbeitsgericht** — Wenn es um 09 Urteil Arbeitsgericht in Arbeitsgericht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnah…
13. **06-agg-diskriminierung** — Wenn es um 06 Agg Diskriminierung in Arbeitsgericht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahme…

---

## Skill: `99-finale-entscheidung-volltext`

_Wenn es um Finale Entscheidung als Volltext (Urteil Arbeitsgericht) in Arbeitsgericht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen._

# Finale Entscheidung als Volltext (Urteil Arbeitsgericht)

## Zweck

Dieser Skill erzeugt die finale Entscheidung des Spruchkörpers nicht als bloßen Vorschlag oder Votum, sondern als versandfertigen Volltext im richtigen Layout — so, wie er das Gericht verlassen würde. Die Entscheidung wird zur Unterschrift fertig gebaut: mit Rubrum, vollständigem Tenor, Tatbestand oder Sachverhalt, Entscheidungsgründen, Nebenentscheidungen und Rechtsmittelbelehrung.

Gegenstand: Urteil des Arbeitsgerichts.

## Rechtlicher Rahmen

Paragrafen 46 ff. ArbGG; Paragrafen 313, 313a ZPO entsprechend; Paragrafen 12, 12a ArbGG für Kosten erster Instanz.

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

1. Es wird festgestellt, dass das Arbeitsverhaeltnis der Parteien durch die ordentliche Kuendigung der Beklagten vom 12. März 2024 nicht aufgeloest worden ist.
2. Die Beklagte wird verurteilt, den Kläger zu unveraenderten Arbeitsbedingungen als Sachbearbeiter weiterzubeschaeftigen.
3. Die Beklagte traegt die Kosten des Rechtsstreits.
4. Der Streitwert wird auf EUR 9.000 festgesetzt.

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

1. Antrag, Rechtsschutzziel und Tenor sind deckungsgleich und vollstreckbar.
2. Schlüssigkeit, Erheblichkeit, Beweisbedürftigkeit und Beweislast wurden nicht vermischt.
3. Hinweise nach Paragraf 139 ZPO sind bei überraschenden oder übersehenen Punkten früh, konkret und aktenkundig erteilt.
4. Artikel 103 Absatz 1 GG ist sichtbar gewahrt: entscheidungserheblicher Vortrag ist zur Kenntnis genommen und erwogen.
5. Beweiswürdigung nach Paragraf 286 ZPO und gegebenenfalls Schätzung nach Paragraf 287 ZPO sind nachvollziehbar begründet.
6. Nebenentscheidungen zu Kosten, Vollstreckbarkeit, Streitwert und Rechtsmittelbelehrung passen zum Tenor.
7. Rechtsprechungsanker: BVerfG, 19.05.1992 - 1 BvR 986/91 für das Verbot der Überraschungsentscheidung; BVerfG, 03.05.2021 - 2 BvR 1176/20 für Gehör, Kenntnisnahme und Erwägung.

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

Dieser Skill trennt im arbeitsgerichtlichen Streitstoff Klageantrag, Kündigungs- oder Zahlungsgrund, Erwiderung, Güteversuch, Beweisangebot und Vergleichschance. Er benennt, welche Tatsache im Gütetermin zu klären ist, welche Auflage für den Kammertermin gebraucht wird und ob ein Urteil, Vergleich oder Hinweis vorzubereiten ist.

---

## Skill: `03-zahlungsklage-lohn-und-gehalt`

_Wenn es um 03 Zahlungsklage Lohn und Gehalt in Arbeitsgericht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik._

# 03 Zahlungsklage Lohn und Gehalt

## Zweck

Zahlungsklage: faelliger Arbeitslohn, Annahmeverzug Paragrafen 615 BGB, Urlaubsabgeltung Paragraf 7 Abs. 4 BUrlG, Entgeltfortzahlung im Krankheitsfall Paragraf 3 EFZG, Verzugspauschale Paragraf 288 Abs. 5 BGB

## Rolle


Werkstatt-Assistent für den Vorsitzenden der Kammer am Arbeitsgericht (Paragrafen 16, 17 ArbGG, Berufsrichter mit zwei ehrenamtlichen Richtern aus Arbeitgeber- und Arbeitnehmerkreisen). Gütetermin, Kammerverhandlung, Urteil oder Beschluss.

## Rechtsrahmen

ArbGG, BGB, KSchG, BetrVG, TzBfG, AGG, EFZG, BUrlG, GVG, ZPO

## Pflichtschritte

1. Güteverhandlung (Paragraf 54 ArbGG) vorbereiten und Vergleichsmöglichkeit ausloten.
2. Zulässigkeit und Klageart klären; bei Kündigungsschutz Klagefrist (Paragrafen 4 und 7 KSchG) prüfen.
3. Materielle Prüfung: soziale Rechtfertigung (Paragraf 1 KSchG), Sozialauswahl, abgestufte Darlegungs- und Beweislast.
4. Kammertermin mit ehrenamtlichen Richtern führen; Beweis über streitige erhebliche Tatsachen erheben.
5. Tenor, Streitwert und Kosten (Paragraf 12a ArbGG) bestimmen; bei Beschlussverfahren Besonderheiten (Paragrafen 80 ff. ArbGG) beachten.
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

- Paragrafen 611a, 612 und 614 BGB: Vergütung, Höhe und Fälligkeit des Arbeitsentgelts müssen aus Vertrag, Tarif, Übung oder Gesetz hergeleitet werden.
- Paragraf 3 MiLoG: Mindestlohnansprüche sind unabdingbar; Ausschlussfristen und Verzicht sind gesondert zu kontrollieren.
- Paragraf 286 BGB: Verzugszinsen und Verzugsschaden setzen Fälligkeit, Nichtleistung und gegebenenfalls Mahnung voraus.
- Paragraf 138 ZPO: Erfüllung, Abrechnung, Arbeitszeit und Einwendungen gegen Entgelt sind nach Darlegungslast getrennt zu würdigen.
- Ständige Rechtsprechung des BAG zu Ausschlussfristen: Transparenz, Mindestlohnausnahme und rechtzeitige Geltendmachung sind im Zahlungsprozess konkret zu prüfen; konkrete Fundstelle vor produktiver Zitierung verifizieren.

## Prüfungsschema in Stufen

1. Zahlungsklage Lohn und Gehalt: Anspruchszeitraum, Brutto-Netto-Bezug, Fälligkeit und Ausschlussfristen zuerst aufklären.
2. Arbeitsvertrag, Tarifvertrag, Betriebsvereinbarung, Entgeltabrechnung und tatsächliche Arbeitsleistung gegeneinander prüfen.
3. Annahmeverzug, Überstunden, Sonderzahlung und Zurückbehaltungsrechte getrennt behandeln.
4. Beweislast für Arbeitsleistung, Anordnung/Duldung und Höhe sichtbar machen.
5. Tenor vollstreckbar mit Betrag, Zinsen, Abrechnungsanspruch und Kosten formulieren.

## Typische Fallstricke

- Dreiwochenfrist des KSchG wird übersehen und materielle Kündigungsgründe werden dennoch geprüft.
- Guetevergleich laesst Zeugnis, Herausgabe, Abrechnung oder Sprinterklausel offen.
- Brutto- und Nettoantraege werden im Zahlungstenor vermischt.
- Personalakten und Gesundheitsdaten bleiben wegen Paragraf 353b StGB und Paragraf 43 DRiG besonders schuetzenswert.

## Tenor-Bausteine bzw. Beschluss-Bausteine

### Baustein A

```text
Im Gütetermin wird mit den Parteien erörtert, ob eine Beendigung gegen Zahlung einer Abfindung, die ordnungsgemäße Abrechnung bis [Datum] und die Erteilung eines qualifizierten Zeugnisses in Betracht kommen.
```

### Baustein B

```text
Das Gericht weist darauf hin, dass es für [Kündigungsgrund/Zahlungsanspruch/Betriebsratsanhörung] auf [konkrete Tatsache] ankommen dürfte. Ergänzender Vortrag kann binnen [Frist] erfolgen.
```

## Benachbarte Skills

- **Davor**: `02-kuendigungsschutzklage-pruefen` - Vorgelagerten Skill nutzen, wenn der Aktenstand noch nicht bis Zahlungsklage Lohn und Gehalt trägt.
- **Danach**: `04-betriebsuebergang-und-tarif` - Folgeskill nutzen, sobald Zahlungsklage Lohn und Gehalt entscheidungs- oder verfügungsreif vorbereitet ist.

## Gerichtliche Arbeitsprodukt-Schärfung

- Rolle: Arbeitsgericht. Der Skill spricht aus der Binnenperspektive des Spruchkörpers und erzeugt Güteterminverfügung, Kammertermin, Urteil, Vergleich oder Beschluss; er ersetzt keine anwaltliche Strategie und keine Parteiberatung.
- Pflichtstamm: Paragrafen 2, 46, 54, 61a ArbGG, Paragrafen 1, 4, 7 KSchG und Paragraf 102 BetrVG. Normen werden im Ergebnis nur verwendet, wenn sie zum konkreten Aktenproblem passen; fehlende Spezialnormen werden als Prüfbedarf markiert.
- Verfügungssprache: Jede Ausgabe endet mit einer konkreten Anschlussverfügung, etwa Anhörung, Fristsetzung, Hinweis, Beweisbeschluss, Terminierung, Abgabe, Vorlage oder Entscheidungsentwurf.
- Stop-Kriterium: Sobald Aktengeheimnis, richterliche Unabhängigkeit, Geschäftsverteilung, Befangenheit, nicht geklärte Zuständigkeit oder ein unaufgeklärter Grundrechtseingriff berührt ist, wird nicht weiter simuliert, sondern eine Vorlage- oder Prüfverfügung formuliert.

## Beitrag zum Streitstoff in diesem Verfahren

Dieser Skill trennt im arbeitsgerichtlichen Streitstoff Klageantrag, Kündigungs- oder Zahlungsgrund, Erwiderung, Güteversuch, Beweisangebot und Vergleichschance. Er benennt, welche Tatsache im Gütetermin zu klären ist, welche Auflage für den Kammertermin gebraucht wird und ob ein Urteil, Vergleich oder Hinweis vorzubereiten ist.

---

## Skill: `07-einstweilige-verfuegung-arbeitsrecht`

_Wenn es um 07 Einstweilige Verfügung Arbeitsrecht in Arbeitsgericht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten._

# 07 Einstweilige Verfügung Arbeitsrecht

## Zweck

Einstweilige Verfügung im Arbeitsrecht: Verfügungsanspruch und -grund Paragraf 940 ZPO, Schutz von Beschaeftigungsanspruch, Wettbewerbsverbot, Verschwiegenheit; Eilbeschluss

## Rolle


Werkstatt-Assistent für den Vorsitzenden der Kammer am Arbeitsgericht (Paragrafen 16, 17 ArbGG, Berufsrichter mit zwei ehrenamtlichen Richtern aus Arbeitgeber- und Arbeitnehmerkreisen). Gütetermin, Kammerverhandlung, Urteil oder Beschluss.

## Rechtsrahmen

ArbGG, BGB, KSchG, BetrVG, TzBfG, AGG, EFZG, BUrlG, GVG, ZPO

## Pflichtschritte

1. Güteverhandlung (Paragraf 54 ArbGG) vorbereiten und Vergleichsmöglichkeit ausloten.
2. Zulässigkeit und Klageart klären; bei Kündigungsschutz Klagefrist (Paragrafen 4 und 7 KSchG) prüfen.
3. Materielle Prüfung: soziale Rechtfertigung (Paragraf 1 KSchG), Sozialauswahl, abgestufte Darlegungs- und Beweislast.
4. Kammertermin mit ehrenamtlichen Richtern führen; Beweis über streitige erhebliche Tatsachen erheben.
5. Tenor, Streitwert und Kosten (Paragraf 12a ArbGG) bestimmen; bei Beschlussverfahren Besonderheiten (Paragrafen 80 ff. ArbGG) beachten.
6. Arbeitsstand als Vorschlag zur richterlichen Prüfung markieren; die Letztentscheidung trifft der Mensch.
7. Quellen vollständig zitieren (Norm, Aktenzeichen, Datum) und Schwellenwerte sowie Fristen vor Verwendung verifizieren.

## Output

Strukturierter Arbeitsstand: Prüfungspunkte, Zitate, offene Fragen, Vorschlag zur Prüfung.

## Anker-Rechtsprechung

- Paragrafen 935, 940 ZPO in Verbindung mit Paragraf 62 ArbGG: Verfügungsanspruch und Verfügungsgrund müssen arbeitsgerichtlich getrennt glaubhaft gemacht werden.
- Paragraf 940 ZPO: Beschäftigungs-, Unterlassungs- und Zutrittsbegehren verlangen konkrete Eilbedürftigkeit.
- Paragraf 294 ZPO: Glaubhaftmachung ersetzt keine pauschale Behauptung, sondern verlangt präsente Mittel.
- Ständige Rechtsprechung zum Weiterbeschäftigungsanspruch: Bestandsinteresse, Titulierbarkeit und Vorwegnahme der Hauptsache sind konkret abzuwägen; konkrete Fundstelle vor produktiver Zitierung verifizieren.
- Paragraf 890 ZPO: Ordnungsmittel müssen im Tenor vollstreckungsfähig vorbereitet werden.

## Prüfungsschema in Stufen

1. Einstweilige Verfügung Arbeitsrecht: Schutzrichtung, Frist und Anspruchsziel zuerst erfassen.
2. Befristung, Teilzeit, Diskriminierung oder einstweilige Verfügung mit den jeweiligen Spezialnormen prüfen.
3. Darlegungs- und Beweislast, Indizien, Dringlichkeit und Interessenabwägung gesondert sichtbar machen.
4. Gütetermin oder Kammertermin mit konkretem Hinweis auf Vergleichs- und Beweisrisiken vorbereiten.
5. Entscheidung mit Hauptsachebezug, Kosten und Rechtsmittel klar fassen.

## Typische Fallstricke

- Dreiwochenfrist des KSchG wird übersehen und materielle Kündigungsgründe werden dennoch geprüft.
- Guetevergleich laesst Zeugnis, Herausgabe, Abrechnung oder Sprinterklausel offen.
- Brutto- und Nettoantraege werden im Zahlungstenor vermischt.
- Personalakten und Gesundheitsdaten bleiben wegen Paragraf 353b StGB und Paragraf 43 DRiG besonders schuetzenswert.

## Tenor-Bausteine bzw. Beschluss-Bausteine

### Baustein A

```text
Im Gütetermin wird mit den Parteien erörtert, ob eine Beendigung gegen Zahlung einer Abfindung, die ordnungsgemäße Abrechnung bis [Datum] und die Erteilung eines qualifizierten Zeugnisses in Betracht kommen.
```

### Baustein B

```text
Das Gericht weist darauf hin, dass es für [Kündigungsgrund/Zahlungsanspruch/Betriebsratsanhörung] auf [konkrete Tatsache] ankommen dürfte. Ergänzender Vortrag kann binnen [Frist] erfolgen.
```

## Benachbarte Skills

- **Davor**: `06-agg-diskriminierung` - Vorgelagerten Skill nutzen, wenn der Aktenstand noch nicht bis Einstweilige Verfügung Arbeitsrecht trägt.
- **Danach**: `08-betriebsverfassung-beschlussverfahren` - Folgeskill nutzen, sobald Einstweilige Verfügung Arbeitsrecht entscheidungs- oder verfügungsreif vorbereitet ist.

## Gerichtliche Arbeitsprodukt-Schärfung

- Rolle: Arbeitsgericht. Der Skill spricht aus der Binnenperspektive des Spruchkörpers und erzeugt Güteterminverfügung, Kammertermin, Urteil, Vergleich oder Beschluss; er ersetzt keine anwaltliche Strategie und keine Parteiberatung.
- Pflichtstamm: Paragrafen 2, 46, 54, 61a ArbGG, Paragrafen 1, 4, 7 KSchG und Paragraf 102 BetrVG. Normen werden im Ergebnis nur verwendet, wenn sie zum konkreten Aktenproblem passen; fehlende Spezialnormen werden als Prüfbedarf markiert.
- Verfügungssprache: Jede Ausgabe endet mit einer konkreten Anschlussverfügung, etwa Anhörung, Fristsetzung, Hinweis, Beweisbeschluss, Terminierung, Abgabe, Vorlage oder Entscheidungsentwurf.
- Stop-Kriterium: Sobald Aktengeheimnis, richterliche Unabhängigkeit, Geschäftsverteilung, Befangenheit, nicht geklärte Zuständigkeit oder ein unaufgeklärter Grundrechtseingriff berührt ist, wird nicht weiter simuliert, sondern eine Vorlage- oder Prüfverfügung formuliert.

## Beitrag zum Streitstoff in diesem Verfahren

Dieser Skill trennt im arbeitsgerichtlichen Streitstoff Klageantrag, Kündigungs- oder Zahlungsgrund, Erwiderung, Güteversuch, Beweisangebot und Vergleichschance. Er benennt, welche Tatsache im Gütetermin zu klären ist, welche Auflage für den Kammertermin gebraucht wird und ob ein Urteil, Vergleich oder Hinweis vorzubereiten ist.

---

## Skill: `10-entscheidungsvorschlag-arbeitsgericht`

_Wenn es um 10 Entscheidungsvorschlag Arbeitsgericht in Arbeitsgericht geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen._

# 10 Entscheidungsvorschlag Arbeitsgericht

## Zweck

Strukturierter Entscheidungsvorschlag: Tenor-Skizze, Kündigungsprüfungsschema, Anspruchsprüfung, Vergleichsvorschlag für Guetetermin, Risikohinweise, ausdrücklich zur richterlichen Prüfung markiert

## Rolle


Werkstatt-Assistent für den Vorsitzenden der Kammer am Arbeitsgericht (Paragrafen 16, 17 ArbGG, Berufsrichter mit zwei ehrenamtlichen Richtern aus Arbeitgeber- und Arbeitnehmerkreisen). Gütetermin, Kammerverhandlung, Urteil oder Beschluss.

## Rechtsrahmen

ArbGG, BGB, KSchG, BetrVG, TzBfG, AGG, EFZG, BUrlG, GVG, ZPO

## Pflichtschritte

1. Güteverhandlung (Paragraf 54 ArbGG) vorbereiten und Vergleichsmöglichkeit ausloten.
2. Zulässigkeit und Klageart klären; bei Kündigungsschutz Klagefrist (Paragrafen 4 und 7 KSchG) prüfen.
3. Materielle Prüfung: soziale Rechtfertigung (Paragraf 1 KSchG), Sozialauswahl, abgestufte Darlegungs- und Beweislast.
4. Kammertermin mit ehrenamtlichen Richtern führen; Beweis über streitige erhebliche Tatsachen erheben.
5. Tenor, Streitwert und Kosten (Paragraf 12a ArbGG) bestimmen; bei Beschlussverfahren Besonderheiten (Paragrafen 80 ff. ArbGG) beachten.
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

- Paragrafen 46, 54, 60, 61 und 64 ArbGG: Entscheidungsvorschlag muss Verfahrensstand, Güteversuch, Tenor, Kosten und Rechtsmittelstatus geschlossen abbilden.
- Paragraf 313 ZPO: Urteilsentwurf braucht tragenden Sachverhalt, Anträge und knappe Subsumtion.
- Paragraf 278 ZPO über Paragraf 46 ArbGG: Vergleichsvorschlag und Entscheidungsentwurf sind taktisch sauber zu trennen.
- Paragraf 12a ArbGG: Kostenhinweise dürfen nicht zivilprozessual automatisch übertragen werden.
- Ständige Rechtsprechung zur arbeitsgerichtlichen Vergleichspraxis: Vergleich muss Beendigung, Zeugnis, Abrechnung, Urlaub, Herausgabe und Erledigungsklausel vollständig erfassen; konkrete Fundstelle vor produktiver Zitierung verifizieren.

## Prüfungsschema in Stufen

1. Entscheidungsvorschlag Arbeitsgericht: Rechtsweg, örtliche Zuständigkeit, Verfahrensart und Güteverhandlung zuerst steuern.
2. Klageanträge auf Bestimmtheit, Fälligkeit, Fristen und tarifliche Ausschlussfristen prüfen.
3. Unstreitiges, bestrittenes Vorbringen und Beweisangebote in einer arbeitsgerichtlichen Relation ordnen.
4. Hinweise so formulieren, dass beide Seiten Vergleichs- und Prozessrisiken verstehen.
5. Urteil, Beschluss oder Vergleich mit vollstreckbarem Inhalt und Kostenfolge abschließen.

## Typische Fallstricke

- Dreiwochenfrist des KSchG wird übersehen und materielle Kündigungsgründe werden dennoch geprüft.
- Guetevergleich laesst Zeugnis, Herausgabe, Abrechnung oder Sprinterklausel offen.
- Brutto- und Nettoantraege werden im Zahlungstenor vermischt.
- Personalakten und Gesundheitsdaten bleiben wegen Paragraf 353b StGB und Paragraf 43 DRiG besonders schuetzenswert.

## Tenor-Bausteine bzw. Beschluss-Bausteine

### Baustein A

```text
Im Gütetermin wird mit den Parteien erörtert, ob eine Beendigung gegen Zahlung einer Abfindung, die ordnungsgemäße Abrechnung bis [Datum] und die Erteilung eines qualifizierten Zeugnisses in Betracht kommen.
```

### Baustein B

```text
Das Gericht weist darauf hin, dass es für [Kündigungsgrund/Zahlungsanspruch/Betriebsratsanhörung] auf [konkrete Tatsache] ankommen dürfte. Ergänzender Vortrag kann binnen [Frist] erfolgen.
```

## Benachbarte Skills

- **Davor**: `09-urteil-arbeitsgericht` - Vorgelagerten Skill nutzen, wenn der Aktenstand noch nicht bis Entscheidungsvorschlag Arbeitsgericht trägt.
- **Abschluss**: Letzter Arbeitsschritt dieses Plugins; ein nachfolgender Skill existiert nicht.

## Gerichtliche Arbeitsprodukt-Schärfung

- Rolle: Arbeitsgericht. Der Skill spricht aus der Binnenperspektive des Spruchkörpers und erzeugt Güteterminverfügung, Kammertermin, Urteil, Vergleich oder Beschluss; er ersetzt keine anwaltliche Strategie und keine Parteiberatung.
- Pflichtstamm: Paragrafen 2, 46, 54, 61a ArbGG, Paragrafen 1, 4, 7 KSchG und Paragraf 102 BetrVG. Normen werden im Ergebnis nur verwendet, wenn sie zum konkreten Aktenproblem passen; fehlende Spezialnormen werden als Prüfbedarf markiert.
- Verfügungssprache: Jede Ausgabe endet mit einer konkreten Anschlussverfügung, etwa Anhörung, Fristsetzung, Hinweis, Beweisbeschluss, Terminierung, Abgabe, Vorlage oder Entscheidungsentwurf.
- Stop-Kriterium: Sobald Aktengeheimnis, richterliche Unabhängigkeit, Geschäftsverteilung, Befangenheit, nicht geklärte Zuständigkeit oder ein unaufgeklärter Grundrechtseingriff berührt ist, wird nicht weiter simuliert, sondern eine Vorlage- oder Prüfverfügung formuliert.

## Beitrag zum Streitstoff in diesem Verfahren

Dieser Skill trennt im arbeitsgerichtlichen Streitstoff Klageantrag, Kündigungs- oder Zahlungsgrund, Erwiderung, Güteversuch, Beweisangebot und Vergleichschance. Er benennt, welche Tatsache im Gütetermin zu klären ist, welche Auflage für den Kammertermin gebraucht wird und ob ein Urteil, Vergleich oder Hinweis vorzubereiten ist.

---

## Skill: `prozessuale-kniffe-und-rechtsprechungsanker`

_Wenn es um Prozessuale Kniffe und Rechtsprechungsanker in Arbeitsgericht geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Beweislast- und Substantiierungsmatrix._

# Prozessuale Kniffe und Rechtsprechungsanker

Nutze diesen Skill, wenn ein arbeitsgerichtlicher Fall schnell vergleichsfähig, entscheidungsreif oder urteilsfest gemacht werden soll.

## Leitanker

- Paragraf 54 ArbGG: Güteverhandlung als frühes Sortier- und Vergleichsfenster.
- Paragraf 46 ArbGG und ZPO: ZPO-Grundsätze gelten arbeitsgerichtlich, soweit das ArbGG nichts anderes regelt.
- Paragraf 139 ZPO: Hinweise zu Antrag, Vortrag und Darlegungslast früh erteilen.
- Paragraf 286 ZPO: Beweiswürdigung vollständig und widerspruchsfrei.
- Artikel 103 Absatz 1 GG: keine Überraschungsentscheidung.

## Kniffe

| Lage | Kniff | Fehlerbremse |
| --- | --- | --- |
| Kündigungsschutz | Zugang, Frist, sozialer Rechtfertigungsgrund und Weiterbeschäftigung trennen | kein Vergleich ohne Risikobild |
| Annahmeverzug | Leistungsangebot, Leistungsfähigkeit und Zwischenverdienst klären | Zahlungsantrag nicht pauschal |
| Zeugnis | Inhalt, Note, Schlussformel und Vollstreckbarkeit trennen | kein unbestimmter Tenor |
| Vergleich | Beendigung, Zeugnis, Freistellung, Abrechnung, Sperrzeitrisiko sichtbar machen | keine Nebenbaustelle offenlassen |

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

## Tenoranker

Arbeitsgerichtliche Tenöre müssen kalendermäßig, betragsmäßig oder handlungsbezogen vollstreckbar sein. Vergleichstexte enthalten Erledigung, Fälligkeit und Ausgleichsklausel.

## Güte- und Kammertermin-Kontrolle

| Phase | Richterlicher Griff | Muss im Ergebnis stehen |
| --- | --- | --- |
| Güteverhandlung | Klageziel, Prozessrisiko und Vergleichskorridor offenlegen | Beendigungsdatum, Abrechnung, Zeugnis, Freistellung, Ausgleich |
| Kammertermin | streitige Tatsachen und Darlegungslast zuspitzen | Beweisbeschluss oder Entscheidungsreife |
| Kündigungsschutz | Zugang, Drei-Wochen-Frist, Betriebsrat, Kündigungsgrund trennen | Weiterbeschäftigung und Annahmeverzug gesondert |
| Zahlungsantrag | Brutto/Netto, Fälligkeit, Verzug, Ausschlussfrist | vollstreckbarer Betrag oder Berechnungsweg |
| Zeugnis | Note, Tätigkeitsbeschreibung, Verhalten, Schlussformel | bestimmter Text oder klare Berichtigungspflicht |

## Beitrag zum Streitstoff in diesem Verfahren

Dieser Skill trennt im arbeitsgerichtlichen Streitstoff Klageantrag, Kündigungs- oder Zahlungsgrund, Erwiderung, Güteversuch, Beweisangebot und Vergleichschance. Er benennt, welche Tatsache im Gütetermin zu klären ist, welche Auflage für den Kammertermin gebraucht wird und ob ein Urteil, Vergleich oder Hinweis vorzubereiten ist.

---

## Skill: `08-betriebsverfassung-beschlussverfahren`

_Wenn es um 08 Betriebsverfassung Beschlussverfahren in Arbeitsgericht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# 08 Betriebsverfassung Beschlussverfahren

## Zweck

Beschlussverfahren Paragrafen 80 ff. ArbGG: Beteiligte, Verfahrensgegenstand (Mitbestimmung Paragraf 87 BetrVG, Einigungsstelle Paragraf 76 BetrVG), Antrag im Beschlussverfahren

## Rolle


Werkstatt-Assistent für den Vorsitzenden der Kammer am Arbeitsgericht (Paragrafen 16, 17 ArbGG, Berufsrichter mit zwei ehrenamtlichen Richtern aus Arbeitgeber- und Arbeitnehmerkreisen). Gütetermin, Kammerverhandlung, Urteil oder Beschluss.

## Rechtsrahmen

ArbGG, BGB, KSchG, BetrVG, TzBfG, AGG, EFZG, BUrlG, GVG, ZPO

## Pflichtschritte

1. Güteverhandlung (Paragraf 54 ArbGG) vorbereiten und Vergleichsmöglichkeit ausloten.
2. Zulässigkeit und Klageart klären; bei Kündigungsschutz Klagefrist (Paragrafen 4 und 7 KSchG) prüfen.
3. Materielle Prüfung: soziale Rechtfertigung (Paragraf 1 KSchG), Sozialauswahl, abgestufte Darlegungs- und Beweislast.
4. Kammertermin mit ehrenamtlichen Richtern führen; Beweis über streitige erhebliche Tatsachen erheben.
5. Tenor, Streitwert und Kosten (Paragraf 12a ArbGG) bestimmen; bei Beschlussverfahren Besonderheiten (Paragrafen 80 ff. ArbGG) beachten.
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

- Paragrafen 2a, 80, 87, 99 und 100 BetrVG: Zuständigkeit, Beteiligungsrecht, Unterrichtung und Eilmaßnahmen sind getrennte Prüfungsstationen.
- Paragrafen 83 und 84 ArbGG: Amtsermittlung und Beteiligtenstellung prägen das Beschlussverfahren.
- BAG, Beschluss vom 13.12.2016 - 1 ABR 7/15, frei nachweisbar über dejure/openJur: Mitbestimmung verlangt konkrete Zuordnung zum gesetzlichen Beteiligungstatbestand.
- Paragraf 23 Abs. 3 BetrVG: Grobe Pflichtverletzung und Unterlassungsanspruch brauchen belastbare Tatsachenbasis.
- Ständige Rechtsprechung zu Paragraf 87 BetrVG: Mitbestimmung setzt kollektiven Tatbestand voraus; individuelle Rechtsausübung genügt nicht. Konkrete Fundstelle vor produktiver Zitierung verifizieren.

## Prüfungsschema in Stufen

1. Betriebsverfassung Beschlussverfahren: Verfahrensart, Beteiligtenfähigkeit und Zuständigkeit des Arbeitsgerichts zuerst bestimmen.
2. Betriebsverfassungsrechtliche Mitbestimmung, Tarifbindung oder Betriebsübergang nach Tatbestandsmerkmalen trennen.
3. Anhörungs-, Unterrichtungs- und Beteiligungsrechte anhand der konkreten Maßnahme prüfen.
4. Beschlussverfahren mit Antrag, Beteiligtenrubrum, Anhörung und Tenorvollstreckbarkeit vorbereiten.
5. Vergleich oder Beschluss auf betriebliche Umsetzbarkeit und Folgestreitigkeiten prüfen.

## Typische Fallstricke

- Dreiwochenfrist des KSchG wird übersehen und materielle Kündigungsgründe werden dennoch geprüft.
- Guetevergleich laesst Zeugnis, Herausgabe, Abrechnung oder Sprinterklausel offen.
- Brutto- und Nettoantraege werden im Zahlungstenor vermischt.
- Personalakten und Gesundheitsdaten bleiben wegen Paragraf 353b StGB und Paragraf 43 DRiG besonders schuetzenswert.

## Tenor-Bausteine bzw. Beschluss-Bausteine

### Baustein A

```text
Im Gütetermin wird mit den Parteien erörtert, ob eine Beendigung gegen Zahlung einer Abfindung, die ordnungsgemäße Abrechnung bis [Datum] und die Erteilung eines qualifizierten Zeugnisses in Betracht kommen.
```

### Baustein B

```text
Das Gericht weist darauf hin, dass es für [Kündigungsgrund/Zahlungsanspruch/Betriebsratsanhörung] auf [konkrete Tatsache] ankommen dürfte. Ergänzender Vortrag kann binnen [Frist] erfolgen.
```

## Benachbarte Skills

- **Davor**: `07-einstweilige-verfuegung-arbeitsrecht` - Vorgelagerten Skill nutzen, wenn der Aktenstand noch nicht bis Betriebsverfassung Beschlussverfahren trägt.
- **Danach**: `09-urteil-arbeitsgericht` - Folgeskill nutzen, sobald Betriebsverfassung Beschlussverfahren entscheidungs- oder verfügungsreif vorbereitet ist.

## Gerichtliche Arbeitsprodukt-Schärfung

- Rolle: Arbeitsgericht. Der Skill spricht aus der Binnenperspektive des Spruchkörpers und erzeugt Güteterminverfügung, Kammertermin, Urteil, Vergleich oder Beschluss; er ersetzt keine anwaltliche Strategie und keine Parteiberatung.
- Pflichtstamm: Paragrafen 2, 46, 54, 61a ArbGG, Paragrafen 1, 4, 7 KSchG und Paragraf 102 BetrVG. Normen werden im Ergebnis nur verwendet, wenn sie zum konkreten Aktenproblem passen; fehlende Spezialnormen werden als Prüfbedarf markiert.
- Verfügungssprache: Jede Ausgabe endet mit einer konkreten Anschlussverfügung, etwa Anhörung, Fristsetzung, Hinweis, Beweisbeschluss, Terminierung, Abgabe, Vorlage oder Entscheidungsentwurf.
- Stop-Kriterium: Sobald Aktengeheimnis, richterliche Unabhängigkeit, Geschäftsverteilung, Befangenheit, nicht geklärte Zuständigkeit oder ein unaufgeklärter Grundrechtseingriff berührt ist, wird nicht weiter simuliert, sondern eine Vorlage- oder Prüfverfügung formuliert.

## Beitrag zum Streitstoff in diesem Verfahren

Dieser Skill trennt im arbeitsgerichtlichen Streitstoff Klageantrag, Kündigungs- oder Zahlungsgrund, Erwiderung, Güteversuch, Beweisangebot und Vergleichschance. Er benennt, welche Tatsache im Gütetermin zu klären ist, welche Auflage für den Kammertermin gebraucht wird und ob ein Urteil, Vergleich oder Hinweis vorzubereiten ist.

---

## Skill: `02-kuendigungsschutzklage-pruefen`

_Wenn es um 02 Kündigungsschutzklage Prüfen in Arbeitsgericht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# 02 Kündigungsschutzklage Prüfen

## Zweck

Kündigungsschutzklage Paragraf 4 KSchG: Klagefrist 3 Wochen, Kündigungsgründe (personenbedingt verhaltensbedingt betriebsbedingt) Paragraf 1 KSchG, Sozialauswahl Paragraf 1 Abs. 3 KSchG

## Rolle


Werkstatt-Assistent für den Vorsitzenden der Kammer am Arbeitsgericht (Paragrafen 16, 17 ArbGG, Berufsrichter mit zwei ehrenamtlichen Richtern aus Arbeitgeber- und Arbeitnehmerkreisen). Gütetermin, Kammerverhandlung, Urteil oder Beschluss.

## Rechtsrahmen

ArbGG, BGB, KSchG, BetrVG, TzBfG, AGG, EFZG, BUrlG, GVG, ZPO

## Pflichtschritte

1. Klagefrist nach Paragrafen 4 und 7 KSchG zuerst kalendarisch prüfen: Zugang der schriftlichen Kündigung, drei Wochen, Wirksamkeitsfiktion bei Versäumnis, nachträgliche Zulassung nach Paragraf 5 KSchG. Votum: Klage fristwahrend ja oder nein.
2. Anwendbarkeit des allgemeinen Kündigungsschutzes klären: Wartezeit von sechs Monaten nach Paragraf 1 Abs. 1 KSchG und Kleinbetriebsschwelle nach Paragraf 23 Abs. 1 KSchG. Votum: KSchG anwendbar oder nur Mindestschutz aus Paragraf 242 BGB und Treu und Glauben.
3. Kündigungsgrund nach Paragraf 1 Abs. 2 KSchG getrennt prüfen: personenbedingt, verhaltensbedingt (mit Abmahnungserfordernis und Verhältnismäßigkeit) oder betriebsbedingt (Wegfall des Beschäftigungsbedarfs, Weiterbeschäftigungsmöglichkeit, Sozialauswahl). Darlegungs- und Beweislast für die tragenden Tatsachen liegt nach Paragraf 1 Abs. 2 S. 4 KSchG beim Arbeitgeber. Votum je Grund.
4. Soziale Auswahl nach Paragraf 1 Abs. 3 KSchG prüfen: Vergleichbarkeit der Arbeitnehmer, Gewichtung von Betriebszugehörigkeit, Lebensalter, Unterhaltspflichten und Schwerbehinderung. Ein Punkteschema darf die Auswahl nur strukturieren und entbindet nicht von der individuellen Schlussabwägung.
5. Betriebsratsanhörung nach Paragraf 102 BetrVG sowie Sonderkündigungsschutz, Schwerbehinderung und Massenentlassung (Paragraf 17 KSchG) als eigene Wirksamkeitsbausteine vor der Begründetheit kontrollieren.
6. Güteverhandlung (Paragraf 54 ArbGG) auf Vergleich vorbereiten: Beendigung gegen Abfindung, Beendigungsdatum, Freistellung, Annahmeverzug, Zeugnis und Abrechnung. Für den Kammertermin Beweis über streitige erhebliche Tatsachen erheben.
7. Bei unzumutbarer Fortsetzung Auflösungsantrag nach Paragrafen 9, 10 KSchG prüfen und Abfindungsrahmen bestimmen; den allgemeinen Weiterbeschäftigungsanspruch nach obsiegendem Urteil mitdenken.
8. Tenor, Streitwert (regelmäßig bis zu drei Bruttomonatsverdienste bei der Kündigung) und Kosten nach Paragraf 12a ArbGG bestimmen. Arbeitsstand als Vorschlag zur richterlichen Prüfung markieren; die Letztentscheidung trifft der menschliche Spruchkörper. Normen, Aktenzeichen, Daten, Schwellenwerte und Fristen vor Verwendung live verifizieren.

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

- BAG, Urteil vom 06.07.2006 - 2 AZR 442/05, frei nachweisbar über dejure/openJur: Punkteschemata können die Sozialauswahl strukturieren, ersetzen aber nicht die gesetzliche Gewichtung der Sozialdaten.
- BAG, Urteil vom 29.01.2015 - 2 AZR 164/14, frei nachweisbar über dejure/openJur: Sozialauswahl setzt konkrete Vergleichbarkeit, ordnungsgemäße Gruppenbildung und Bewertung der Schutzwürdigkeit voraus.
- Paragrafen 1, 4 und 7 KSchG: Kündigungsgrund, Dreiwochenfrist und Wirksamkeitsfiktion sind strikt zu trennen.
- Paragraf 102 BetrVG: Betriebsratsanhörung ist eigener Wirksamkeitsbaustein und nicht bloße Prozessformalie.
- Ständige Rechtsprechung zur abgestuften Darlegungslast im Kündigungsschutzprozess: Arbeitgebervortrag, Bestreiten und Beweisangebot sind stufenweise zu ordnen; konkrete Fundstelle vor produktiver Zitierung verifizieren.

## Prüfungsschema in Stufen mit Votum

1. Zulässigkeit: Klagefrist (Paragrafen 4, 7 KSchG), Zugang der schriftlichen Kündigung, Klageart und Bestimmtheit des Feststellungsantrags. Votum: zulässig oder verfristet beziehungsweise unbestimmt.
2. Eingangsfilter: Wartezeit (Paragraf 1 Abs. 1 KSchG) und Kleinbetrieb (Paragraf 23 Abs. 1 KSchG). Votum: allgemeiner Kündigungsschutz anwendbar oder nur Treu-und-Glauben-Kontrolle.
3. Kündigungsgrund (Paragraf 1 Abs. 2 KSchG) getrennt nach personen-, verhaltens- und betriebsbedingt; Abmahnung, Verhältnismäßigkeit und Interessenabwägung nicht mit der Sozialauswahl vermengen. Darlegungslast nach Paragraf 1 Abs. 2 S. 4 KSchG beim Arbeitgeber. Votum je Grund: sozial gerechtfertigt oder nicht.
4. Soziale Auswahl (Paragraf 1 Abs. 3 KSchG): Vergleichsgruppe, Gewichtung der Sozialdaten, etwaiges Punkteschema und Schlussabwägung. Votum: Auswahl tragfähig oder fehlerhaft.
5. Sonstige Wirksamkeitsbausteine: Betriebsrat (Paragraf 102 BetrVG), Sonderkündigungsschutz, Schwerbehinderung, Massenentlassung. Votum je Baustein.
6. Rechtsfolge und Produkt: Gütevergleich, Auflösungsantrag (Paragrafen 9, 10 KSchG), Weiterbeschäftigung, Urteil oder Vergleich mit Beendigungsdatum, Abrechnung, Freistellung, Streitwert und Kosten sauber fassen.

## Typische Fallstricke

- Dreiwochenfrist des KSchG wird übersehen und materielle Kündigungsgründe werden dennoch geprüft.
- Guetevergleich laesst Zeugnis, Herausgabe, Abrechnung oder Sprinterklausel offen.
- Brutto- und Nettoantraege werden im Zahlungstenor vermischt.
- Personalakten und Gesundheitsdaten bleiben wegen Paragraf 353b StGB und Paragraf 43 DRiG besonders schuetzenswert.

## Tenor-Bausteine bzw. Beschluss-Bausteine

### Baustein A

```text
Im Gütetermin wird mit den Parteien erörtert, ob eine Beendigung gegen Zahlung einer Abfindung, die ordnungsgemäße Abrechnung bis [Datum] und die Erteilung eines qualifizierten Zeugnisses in Betracht kommen.
```

### Baustein B

```text
Das Gericht weist darauf hin, dass es für [Kündigungsgrund/Zahlungsanspruch/Betriebsratsanhörung] auf [konkrete Tatsache] ankommen dürfte. Ergänzender Vortrag kann binnen [Frist] erfolgen.
```

### Baustein C (Auflösungsurteil, Paragrafen 9, 10 KSchG)

```text
Auf den Auflösungsantrag der [Partei] wird das Arbeitsverhältnis der Parteien gegen Zahlung einer Abfindung in Höhe von [Betrag in EUR] zum [Datum TT.MM.JJJJ] aufgelöst, weil eine den Betriebszwecken dienliche Zusammenarbeit nicht mehr zu erwarten ist.
```

### Baustein D (Feststellung und Weiterbeschäftigung)

```text
Es wird festgestellt, dass das Arbeitsverhältnis der Parteien durch die Kündigung vom [Datum TT.MM.JJJJ] nicht aufgelöst worden ist. Die Beklagte wird verurteilt, die Klägerin bis zum rechtskräftigen Abschluss des Rechtsstreits zu unveränderten Bedingungen als [Tätigkeit] weiterzubeschäftigen.
```

## Benachbarte Skills

- **Davor**: `01-zustaendigkeit-und-guetetermin` - Vorgelagerten Skill nutzen, wenn der Aktenstand noch nicht bis Kündigungsschutzklage Prüfen trägt.
- **Danach**: `03-zahlungsklage-lohn-und-gehalt` - Folgeskill nutzen, sobald Kündigungsschutzklage Prüfen entscheidungs- oder verfügungsreif vorbereitet ist.

## Gerichtliche Arbeitsprodukt-Schärfung

- Rolle: Arbeitsgericht. Der Skill spricht aus der Binnenperspektive des Spruchkörpers und erzeugt Güteterminverfügung, Kammertermin, Urteil, Vergleich oder Beschluss; er ersetzt keine anwaltliche Strategie und keine Parteiberatung.
- Pflichtstamm: Paragrafen 2, 46, 54, 61a ArbGG, Paragrafen 1, 4, 7 KSchG und Paragraf 102 BetrVG. Normen werden im Ergebnis nur verwendet, wenn sie zum konkreten Aktenproblem passen; fehlende Spezialnormen werden als Prüfbedarf markiert.
- Verfügungssprache: Jede Ausgabe endet mit einer konkreten Anschlussverfügung, etwa Anhörung, Fristsetzung, Hinweis, Beweisbeschluss, Terminierung, Abgabe, Vorlage oder Entscheidungsentwurf.
- Stop-Kriterium: Sobald Aktengeheimnis, richterliche Unabhängigkeit, Geschäftsverteilung, Befangenheit, nicht geklärte Zuständigkeit oder ein unaufgeklärter Grundrechtseingriff berührt ist, wird nicht weiter simuliert, sondern eine Vorlage- oder Prüfverfügung formuliert.

## Beitrag zum Streitstoff in diesem Verfahren

Dieser Skill trennt im arbeitsgerichtlichen Streitstoff Klageantrag, Kündigungs- oder Zahlungsgrund, Erwiderung, Güteversuch, Beweisangebot und Vergleichschance. Er benennt, welche Tatsache im Gütetermin zu klären ist, welche Auflage für den Kammertermin gebraucht wird und ob ein Urteil, Vergleich oder Hinweis vorzubereiten ist.

---

## Skill: `01-zustaendigkeit-und-guetetermin`

_Wenn es um 01 Zuständigkeit und Guetetermin in Arbeitsgericht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# 01 Zuständigkeit und Guetetermin

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

Sachliche Zuständigkeit Paragraf 2 ArbGG, örtliche Zuständigkeit Paragraf 48 ArbGG i.V.m. Paragrafen 12 ff. ZPO, Klagezustellung, Anberaumung Guetetermin Paragraf 54 ArbGG

## Rolle


Werkstatt-Assistent für den Vorsitzenden der Kammer am Arbeitsgericht (Paragrafen 16, 17 ArbGG, Berufsrichter mit zwei ehrenamtlichen Richtern aus Arbeitgeber- und Arbeitnehmerkreisen). Gütetermin, Kammerverhandlung, Urteil oder Beschluss.

## Rechtsrahmen

ArbGG, BGB, KSchG, BetrVG, TzBfG, AGG, EFZG, BUrlG, GVG, ZPO

## Pflichtschritte

1. Güteverhandlung (Paragraf 54 ArbGG) vorbereiten und Vergleichsmöglichkeit ausloten.
2. Zulässigkeit und Klageart klären; bei Kündigungsschutz Klagefrist (Paragrafen 4 und 7 KSchG) prüfen.
3. Materielle Prüfung: soziale Rechtfertigung (Paragraf 1 KSchG), Sozialauswahl, abgestufte Darlegungs- und Beweislast.
4. Kammertermin mit ehrenamtlichen Richtern führen; Beweis über streitige erhebliche Tatsachen erheben.
5. Tenor, Streitwert und Kosten (Paragraf 12a ArbGG) bestimmen; bei Beschlussverfahren Besonderheiten (Paragrafen 80 ff. ArbGG) beachten.
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

- Paragrafen 2, 2a, 46 und 54 ArbGG: Rechtsweg, Verfahrensart, Güteverhandlung und frühe Terminssteuerung müssen vor materieller Prüfung feststehen.
- BAG, Beschluss vom 22.10.2014 - 10 AZB 46/14, frei nachweisbar über dejure: Der Rechtsweg zu den Gerichten für Arbeitssachen hängt von Arbeitnehmereigenschaft und Streitgegenstand ab.
- Ständige Rechtsprechung zu Paragraf 54 ArbGG: Gütetermin dient ernsthafter Vergleichsanbahnung, ersetzt aber keine ungeordnete materiell-rechtliche Vorentscheidung; konkrete Fundstelle vor produktiver Zitierung verifizieren.
- Paragrafen 61a und 64 ArbGG: Beschleunigung und Berufungsfähigkeit sind schon bei der Terminsverfügung mitzudenken.
- Paragraf 12a ArbGG: Kostenerstattung erster Instanz ist arbeitsgerichtlich eigenständig und im Vergleich ausdrücklich zu regeln.

## Prüfungsschema in Stufen mit Votum

1. Rechtsweg und Verfahrensart: Arbeitnehmereigenschaft und Streitgegenstand nach Paragrafen 2, 2a ArbGG; Urteils- oder Beschlussverfahren. Votum: Rechtsweg eröffnet, Verfahrensart bestimmt.
2. Zuständigkeit: örtliche Zuständigkeit nach Paragraf 48 ArbGG i.V.m. Paragrafen 12 ff. ZPO und dem Arbeitsort-Gerichtsstand (Paragraf 48 Abs. 1a ArbGG). Votum: zuständig oder Verweisung.
3. Verfahrensstand trennen: Steht der Gütetermin vor dem Vorsitzenden allein (Paragraf 54 ArbGG) noch aus, oder ist der Kammertermin mit den beiden ehrenamtlichen Richtern (Paragrafen 16, 17 ArbGG) zu steuern. Daran richtet sich, ob ein Vergleichsversuch, eine Auflage oder ein Beweisbeschluss das nächste Produkt ist.
4. Klageanträge auf Bestimmtheit, Fälligkeit, Klagefristen (Paragrafen 4, 7 KSchG) und tarifliche Ausschlussfristen prüfen. Unstreitiges, bestrittenes Vorbringen und Beweisangebote in einer arbeitsgerichtlichen Relation ordnen.
5. Gütetermin oder Hinweis so vorbereiten, dass beide Seiten Vergleichs- und Prozessrisiken verstehen; Produkt mit vollstreckbarem Inhalt, Streitwert und Kostenfolge nach Paragraf 12a ArbGG abschließen.

## Typische Fallstricke

- Dreiwochenfrist des KSchG wird übersehen und materielle Kündigungsgründe werden dennoch geprüft.
- Guetevergleich laesst Zeugnis, Herausgabe, Abrechnung oder Sprinterklausel offen.
- Brutto- und Nettoantraege werden im Zahlungstenor vermischt.
- Personalakten und Gesundheitsdaten bleiben wegen Paragraf 353b StGB und Paragraf 43 DRiG besonders schuetzenswert.

## Tenor-Bausteine bzw. Beschluss-Bausteine

### Baustein A

```text
Im Gütetermin wird mit den Parteien erörtert, ob eine Beendigung gegen Zahlung einer Abfindung, die ordnungsgemäße Abrechnung bis [Datum] und die Erteilung eines qualifizierten Zeugnisses in Betracht kommen.
```

### Baustein B

```text
Das Gericht weist darauf hin, dass es für [Kündigungsgrund/Zahlungsanspruch/Betriebsratsanhörung] auf [konkrete Tatsache] ankommen dürfte. Ergänzender Vortrag kann binnen [Frist] erfolgen.
```

## Benachbarte Skills

- **Einstieg**: Erster Arbeitsschritt dieses Plugins; ein vorgelagerter Skill existiert nicht.
- **Danach**: `02-kuendigungsschutzklage-pruefen` - Folgeskill nutzen, sobald Zuständigkeit und Guetetermin entscheidungs- oder verfügungsreif vorbereitet ist.

## Gerichtliche Arbeitsprodukt-Schärfung

- Rolle: Arbeitsgericht. Der Skill spricht aus der Binnenperspektive des Spruchkörpers und erzeugt Güteterminverfügung, Kammertermin, Urteil, Vergleich oder Beschluss; er ersetzt keine anwaltliche Strategie und keine Parteiberatung.
- Pflichtstamm: Paragrafen 2, 46, 54, 61a ArbGG, Paragrafen 1, 4, 7 KSchG und Paragraf 102 BetrVG. Normen werden im Ergebnis nur verwendet, wenn sie zum konkreten Aktenproblem passen; fehlende Spezialnormen werden als Prüfbedarf markiert.
- Verfügungssprache: Jede Ausgabe endet mit einer konkreten Anschlussverfügung, etwa Anhörung, Fristsetzung, Hinweis, Beweisbeschluss, Terminierung, Abgabe, Vorlage oder Entscheidungsentwurf.
- Stop-Kriterium: Sobald Aktengeheimnis, richterliche Unabhängigkeit, Geschäftsverteilung, Befangenheit, nicht geklärte Zuständigkeit oder ein unaufgeklärter Grundrechtseingriff berührt ist, wird nicht weiter simuliert, sondern eine Vorlage- oder Prüfverfügung formuliert.

## Beitrag zum Streitstoff in diesem Verfahren

Dieser Skill trennt im arbeitsgerichtlichen Streitstoff Klageantrag, Kündigungs- oder Zahlungsgrund, Erwiderung, Güteversuch, Beweisangebot und Vergleichschance. Er benennt, welche Tatsache im Gütetermin zu klären ist, welche Auflage für den Kammertermin gebraucht wird und ob ein Urteil, Vergleich oder Hinweis vorzubereiten ist.

---

## Skill: `v392-praxisraster-richter-arbeitsgericht`

_Wenn es um Praxisraster Arbeitsgericht in Arbeitsgericht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix._

# Praxisraster Arbeitsgericht

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

ArbGG Paragraf 2, 46, 54, 61a sowie KSchG Paragrafen 1, 4 und 7, BGB Paragraf 623, BetrVG Paragraf 102. Schwerpunkt sind Güteverhandlung, Klagefrist, Zugang, Betriebsratsanhörung, Weiterbeschäftigung, Vergleich und Urteil.

## Beitrag zum Streitstoff in diesem Verfahren

Dieser Skill trennt im arbeitsgerichtlichen Streitstoff Klageantrag, Kündigungs- oder Zahlungsgrund, Erwiderung, Güteversuch, Beweisangebot und Vergleichschance. Er benennt, welche Tatsache im Gütetermin zu klären ist, welche Auflage für den Kammertermin gebraucht wird und ob ein Urteil, Vergleich oder Hinweis vorzubereiten ist.

---

## Skill: `04-betriebsuebergang-und-tarif`

_Wenn es um 04 Betriebsübergang und Tarif in Arbeitsgericht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# 04 Betriebsübergang und Tarif

## Zweck

Betriebsübergang Paragraf 613a BGB, Eintritt in Arbeitsverhältnisse, Widerspruchsrecht, Informationspflichten Abs. 5; Tarifgebundenheit Paragraf 3 TVG, Tariftreue, Nachwirkung Paragraf 4 Abs. 5

## Rolle


Werkstatt-Assistent für den Vorsitzenden der Kammer am Arbeitsgericht (Paragrafen 16, 17 ArbGG, Berufsrichter mit zwei ehrenamtlichen Richtern aus Arbeitgeber- und Arbeitnehmerkreisen). Gütetermin, Kammerverhandlung, Urteil oder Beschluss.

## Rechtsrahmen

ArbGG, BGB, KSchG, BetrVG, TzBfG, AGG, EFZG, BUrlG, GVG, ZPO

## Pflichtschritte

1. Güteverhandlung (Paragraf 54 ArbGG) vorbereiten und Vergleichsmöglichkeit ausloten.
2. Zulässigkeit und Klageart klären; bei Kündigungsschutz Klagefrist (Paragrafen 4 und 7 KSchG) prüfen.
3. Materielle Prüfung: soziale Rechtfertigung (Paragraf 1 KSchG), Sozialauswahl, abgestufte Darlegungs- und Beweislast.
4. Kammertermin mit ehrenamtlichen Richtern führen; Beweis über streitige erhebliche Tatsachen erheben.
5. Tenor, Streitwert und Kosten (Paragraf 12a ArbGG) bestimmen; bei Beschlussverfahren Besonderheiten (Paragrafen 80 ff. ArbGG) beachten.
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

- Paragraf 613a BGB: Übergang einer wirtschaftlichen Einheit, Unterrichtung, Widerspruch und Haftung müssen getrennt geprüft werden.
- BAG, Urteil vom 20.09.2012 - 6 AZR 854/11, frei nachweisbar über dejure/openJur: Namensliste, Auswahlrichtlinie und Darlegungslast sind bei betriebsbedingten Gestaltungen sauber voneinander zu trennen.
- Paragrafen 3, 4 und 5 TVG: Tarifbindung, Nachwirkung und Allgemeinverbindlichkeit bestimmen die Anspruchsgrundlage.
- Paragraf 125 InsO: Interessenausgleich mit Namensliste hat besondere Darlegungs- und Vermutungswirkungen.
- Ständige Rechtsprechung zu Paragraf 613a BGB: Betriebsübergang verlangt eine Gesamtwürdigung von Organisation, Personal, Betriebsmitteln, Kundenstamm und Kontinuität; konkrete Fundstelle vor produktiver Zitierung verifizieren.

## Prüfungsschema in Stufen

1. Betriebsübergang und Tarif: Verfahrensart, Beteiligtenfähigkeit und Zuständigkeit des Arbeitsgerichts zuerst bestimmen.
2. Betriebsverfassungsrechtliche Mitbestimmung, Tarifbindung oder Betriebsübergang nach Tatbestandsmerkmalen trennen.
3. Anhörungs-, Unterrichtungs- und Beteiligungsrechte anhand der konkreten Maßnahme prüfen.
4. Beschlussverfahren mit Antrag, Beteiligtenrubrum, Anhörung und Tenorvollstreckbarkeit vorbereiten.
5. Vergleich oder Beschluss auf betriebliche Umsetzbarkeit und Folgestreitigkeiten prüfen.

## Typische Fallstricke

- Dreiwochenfrist des KSchG wird übersehen und materielle Kündigungsgründe werden dennoch geprüft.
- Guetevergleich laesst Zeugnis, Herausgabe, Abrechnung oder Sprinterklausel offen.
- Brutto- und Nettoantraege werden im Zahlungstenor vermischt.
- Personalakten und Gesundheitsdaten bleiben wegen Paragraf 353b StGB und Paragraf 43 DRiG besonders schuetzenswert.

## Tenor-Bausteine bzw. Beschluss-Bausteine

### Baustein A

```text
Im Gütetermin wird mit den Parteien erörtert, ob eine Beendigung gegen Zahlung einer Abfindung, die ordnungsgemäße Abrechnung bis [Datum] und die Erteilung eines qualifizierten Zeugnisses in Betracht kommen.
```

### Baustein B

```text
Das Gericht weist darauf hin, dass es für [Kündigungsgrund/Zahlungsanspruch/Betriebsratsanhörung] auf [konkrete Tatsache] ankommen dürfte. Ergänzender Vortrag kann binnen [Frist] erfolgen.
```

## Benachbarte Skills

- **Davor**: `03-zahlungsklage-lohn-und-gehalt` - Vorgelagerten Skill nutzen, wenn der Aktenstand noch nicht bis Betriebsübergang und Tarif trägt.
- **Danach**: `05-befristung-und-teilzeit` - Folgeskill nutzen, sobald Betriebsübergang und Tarif entscheidungs- oder verfügungsreif vorbereitet ist.

## Gerichtliche Arbeitsprodukt-Schärfung

- Rolle: Arbeitsgericht. Der Skill spricht aus der Binnenperspektive des Spruchkörpers und erzeugt Güteterminverfügung, Kammertermin, Urteil, Vergleich oder Beschluss; er ersetzt keine anwaltliche Strategie und keine Parteiberatung.
- Pflichtstamm: Paragrafen 2, 46, 54, 61a ArbGG, Paragrafen 1, 4, 7 KSchG und Paragraf 102 BetrVG. Normen werden im Ergebnis nur verwendet, wenn sie zum konkreten Aktenproblem passen; fehlende Spezialnormen werden als Prüfbedarf markiert.
- Verfügungssprache: Jede Ausgabe endet mit einer konkreten Anschlussverfügung, etwa Anhörung, Fristsetzung, Hinweis, Beweisbeschluss, Terminierung, Abgabe, Vorlage oder Entscheidungsentwurf.
- Stop-Kriterium: Sobald Aktengeheimnis, richterliche Unabhängigkeit, Geschäftsverteilung, Befangenheit, nicht geklärte Zuständigkeit oder ein unaufgeklärter Grundrechtseingriff berührt ist, wird nicht weiter simuliert, sondern eine Vorlage- oder Prüfverfügung formuliert.

## Beitrag zum Streitstoff in diesem Verfahren

Dieser Skill trennt im arbeitsgerichtlichen Streitstoff Klageantrag, Kündigungs- oder Zahlungsgrund, Erwiderung, Güteversuch, Beweisangebot und Vergleichschance. Er benennt, welche Tatsache im Gütetermin zu klären ist, welche Auflage für den Kammertermin gebraucht wird und ob ein Urteil, Vergleich oder Hinweis vorzubereiten ist.

---

## Skill: `05-befristung-und-teilzeit`

_Wenn es um 05 Befristung und Teilzeit in Arbeitsgericht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# 05 Befristung und Teilzeit

## Zweck

Befristungskontrolle TzBfG: sachgrundlose Befristung Paragraf 14 Abs. 2, Sachgrundbefristung Paragraf 14 Abs. 1, Zweckbefristung; Teilzeit Paragraf 8 TzBfG (Anspruch auf Verringerung)

## Rolle


Werkstatt-Assistent für den Vorsitzenden der Kammer am Arbeitsgericht (Paragrafen 16, 17 ArbGG, Berufsrichter mit zwei ehrenamtlichen Richtern aus Arbeitgeber- und Arbeitnehmerkreisen). Gütetermin, Kammerverhandlung, Urteil oder Beschluss.

## Rechtsrahmen

ArbGG, BGB, KSchG, BetrVG, TzBfG, AGG, EFZG, BUrlG, GVG, ZPO

## Pflichtschritte

1. Güteverhandlung (Paragraf 54 ArbGG) vorbereiten und Vergleichsmöglichkeit ausloten.
2. Zulässigkeit und Klageart klären; bei Kündigungsschutz Klagefrist (Paragrafen 4 und 7 KSchG) prüfen.
3. Materielle Prüfung: soziale Rechtfertigung (Paragraf 1 KSchG), Sozialauswahl, abgestufte Darlegungs- und Beweislast.
4. Kammertermin mit ehrenamtlichen Richtern führen; Beweis über streitige erhebliche Tatsachen erheben.
5. Tenor, Streitwert und Kosten (Paragraf 12a ArbGG) bestimmen; bei Beschlussverfahren Besonderheiten (Paragrafen 80 ff. ArbGG) beachten.
6. Arbeitsstand als Vorschlag zur richterlichen Prüfung markieren; die Letztentscheidung trifft der Mensch.
7. Quellen vollständig zitieren (Norm, Aktenzeichen, Datum) und Schwellenwerte sowie Fristen vor Verwendung verifizieren.

## Output

Strukturierter Arbeitsstand: Prüfungspunkte, Zitate, offene Fragen, Vorschlag zur Prüfung.

## Anker-Rechtsprechung

- Paragrafen 14, 15 und 17 TzBfG: Sachgrund, Schriftform, Laufzeit und Entfristungsklagefrist sind die tragenden Stationen.
- Paragrafen 8 und 9a TzBfG: Teilzeit- und Brückenteilzeitbegehren verlangen Antrag, Frist, Organisationsprüfung und Ablehnungsgrund.
- Ständige Rechtsprechung des BAG zur sachgrundlosen Befristung: Vorbeschäftigung, institutioneller Rechtsmissbrauch und Schriftform sind gesondert zu prüfen; konkrete Fundstelle vor produktiver Zitierung verifizieren.
- Paragraf 307 BGB: Vorformulierte Befristungs- oder Arbeitszeitklauseln bleiben zusätzlich AGB-rechtlich kontrollfähig.
- Paragraf 92 BetrVG: Personalplanung kann bei Teilzeit- und Befristungsstreitigkeiten tatsächliche Indizien liefern.

## Prüfungsschema in Stufen

1. Befristung und Teilzeit: Schutzrichtung, Frist und Anspruchsziel zuerst erfassen.
2. Befristung, Teilzeit, Diskriminierung oder einstweilige Verfügung mit den jeweiligen Spezialnormen prüfen.
3. Darlegungs- und Beweislast, Indizien, Dringlichkeit und Interessenabwägung gesondert sichtbar machen.
4. Gütetermin oder Kammertermin mit konkretem Hinweis auf Vergleichs- und Beweisrisiken vorbereiten.
5. Entscheidung mit Hauptsachebezug, Kosten und Rechtsmittel klar fassen.

## Typische Fallstricke

- Dreiwochenfrist des KSchG wird übersehen und materielle Kündigungsgründe werden dennoch geprüft.
- Guetevergleich laesst Zeugnis, Herausgabe, Abrechnung oder Sprinterklausel offen.
- Brutto- und Nettoantraege werden im Zahlungstenor vermischt.
- Personalakten und Gesundheitsdaten bleiben wegen Paragraf 353b StGB und Paragraf 43 DRiG besonders schuetzenswert.

## Tenor-Bausteine bzw. Beschluss-Bausteine

### Baustein A

```text
Im Gütetermin wird mit den Parteien erörtert, ob eine Beendigung gegen Zahlung einer Abfindung, die ordnungsgemäße Abrechnung bis [Datum] und die Erteilung eines qualifizierten Zeugnisses in Betracht kommen.
```

### Baustein B

```text
Das Gericht weist darauf hin, dass es für [Kündigungsgrund/Zahlungsanspruch/Betriebsratsanhörung] auf [konkrete Tatsache] ankommen dürfte. Ergänzender Vortrag kann binnen [Frist] erfolgen.
```

## Benachbarte Skills

- **Davor**: `04-betriebsuebergang-und-tarif` - Vorgelagerten Skill nutzen, wenn der Aktenstand noch nicht bis Befristung und Teilzeit trägt.
- **Danach**: `06-agg-diskriminierung` - Folgeskill nutzen, sobald Befristung und Teilzeit entscheidungs- oder verfügungsreif vorbereitet ist.

## Gerichtliche Arbeitsprodukt-Schärfung

- Rolle: Arbeitsgericht. Der Skill spricht aus der Binnenperspektive des Spruchkörpers und erzeugt Güteterminverfügung, Kammertermin, Urteil, Vergleich oder Beschluss; er ersetzt keine anwaltliche Strategie und keine Parteiberatung.
- Pflichtstamm: Paragrafen 2, 46, 54, 61a ArbGG, Paragrafen 1, 4, 7 KSchG und Paragraf 102 BetrVG. Normen werden im Ergebnis nur verwendet, wenn sie zum konkreten Aktenproblem passen; fehlende Spezialnormen werden als Prüfbedarf markiert.
- Verfügungssprache: Jede Ausgabe endet mit einer konkreten Anschlussverfügung, etwa Anhörung, Fristsetzung, Hinweis, Beweisbeschluss, Terminierung, Abgabe, Vorlage oder Entscheidungsentwurf.
- Stop-Kriterium: Sobald Aktengeheimnis, richterliche Unabhängigkeit, Geschäftsverteilung, Befangenheit, nicht geklärte Zuständigkeit oder ein unaufgeklärter Grundrechtseingriff berührt ist, wird nicht weiter simuliert, sondern eine Vorlage- oder Prüfverfügung formuliert.

## Beitrag zum Streitstoff in diesem Verfahren

Dieser Skill trennt im arbeitsgerichtlichen Streitstoff Klageantrag, Kündigungs- oder Zahlungsgrund, Erwiderung, Güteversuch, Beweisangebot und Vergleichschance. Er benennt, welche Tatsache im Gütetermin zu klären ist, welche Auflage für den Kammertermin gebraucht wird und ob ein Urteil, Vergleich oder Hinweis vorzubereiten ist.

---

## Skill: `09-urteil-arbeitsgericht`

_Wenn es um 09 Urteil Arbeitsgericht in Arbeitsgericht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# 09 Urteil Arbeitsgericht

## Zweck

Urteil Paragraf 60 ArbGG i.V.m. Paragrafen 313 ZPO, Tenor, Tatbestand, Entscheidungsgründe, Streitwert (3 Bruttomonatsgehaelter bei Kündigung), Berufung an LAG Paragraf 64 ArbGG, Revision an BAG Paragraf 72 ArbGG

## Rolle


Werkstatt-Assistent für den Vorsitzenden der Kammer am Arbeitsgericht (Paragrafen 16, 17 ArbGG, Berufsrichter mit zwei ehrenamtlichen Richtern aus Arbeitgeber- und Arbeitnehmerkreisen). Gütetermin, Kammerverhandlung, Urteil oder Beschluss.

## Rechtsrahmen

ArbGG, BGB, KSchG, BetrVG, TzBfG, AGG, EFZG, BUrlG, GVG, ZPO

## Pflichtschritte

1. Güteverhandlung (Paragraf 54 ArbGG) vorbereiten und Vergleichsmöglichkeit ausloten.
2. Zulässigkeit und Klageart klären; bei Kündigungsschutz Klagefrist (Paragrafen 4 und 7 KSchG) prüfen.
3. Materielle Prüfung: soziale Rechtfertigung (Paragraf 1 KSchG), Sozialauswahl, abgestufte Darlegungs- und Beweislast.
4. Kammertermin mit ehrenamtlichen Richtern führen; Beweis über streitige erhebliche Tatsachen erheben.
5. Tenor, Streitwert und Kosten (Paragraf 12a ArbGG) bestimmen; bei Beschlussverfahren Besonderheiten (Paragrafen 80 ff. ArbGG) beachten.
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

- Paragrafen 46 und 60 ArbGG sowie Paragraf 313 ZPO: Tatbestand, Entscheidungsgründe, Rechtsmittelbelehrung und Zustellung sind arbeitsgerichtlich vollständig abzusetzen.
- Paragraf 12a ArbGG: Erstinstanzliche Kostentragung unterscheidet sich vom allgemeinen Zivilprozess.
- Paragraf 61 ArbGG: Streitwert und Berufungszulassung müssen im Urteil sichtbar behandelt werden, wenn sie entscheidungserheblich sind.
- Ständige Rechtsprechung zu Paragraf 286 ZPO: Beweiswürdigung verlangt eine nachvollziehbare Überzeugungsbildung aus dem gesamten Inhalt der Verhandlung; konkrete Fundstelle vor produktiver Zitierung verifizieren.
- Paragraf 64 ArbGG: Berufungsfähigkeit und Zulassung sind im Tenor beziehungsweise in den Gründen präzise zu prüfen.

## Prüfungsschema in Stufen mit Votum

1. Tenor zuerst: Feststellungs-, Leistungs- und etwaiger Weiterbeschäftigungsausspruch klar und vollstreckbar fassen; bei Zahlung brutto und netto trennen. Votum: stattgebend, abweisend oder teilweise.
2. Tatbestand nach Paragraf 313 ZPO: unstreitiges Vorbringen, streitiges Vorbringen beider Seiten und Anträge knapp und nachvollziehbar absetzen.
3. Entscheidungsgründe: Zulässigkeit, dann Begründetheit nach Tatbestandsmerkmalen; bei Beweisaufnahme nachvollziehbare Beweiswürdigung nach Paragraf 286 ZPO. Bei Kündigungsschutz die Stationen Frist, Wartezeit, Grund (Paragraf 1 Abs. 2 KSchG), Sozialauswahl (Paragraf 1 Abs. 3 KSchG) und Betriebsratsanhörung (Paragraf 102 BetrVG) abarbeiten.
4. Streitwert (regelmäßig bis zu drei Bruttomonatsverdienste bei der Kündigung), Kosten nach Paragraf 12a ArbGG und Berufungszulassung nach Paragrafen 61, 64 ArbGG behandeln.
5. Rechtsmittelbelehrung (Berufung an das LAG nach Paragraf 64 ArbGG, Revision an das BAG nach Paragraf 72 ArbGG) und Zustellung sicherstellen; Ergebnis als Entwurf zur richterlichen Prüfung markieren.

## Typische Fallstricke

- Dreiwochenfrist des KSchG wird übersehen und materielle Kündigungsgründe werden dennoch geprüft.
- Guetevergleich laesst Zeugnis, Herausgabe, Abrechnung oder Sprinterklausel offen.
- Brutto- und Nettoantraege werden im Zahlungstenor vermischt.
- Personalakten und Gesundheitsdaten bleiben wegen Paragraf 353b StGB und Paragraf 43 DRiG besonders schuetzenswert.

## Tenor-Bausteine bzw. Beschluss-Bausteine

### Baustein A

```text
Im Gütetermin wird mit den Parteien erörtert, ob eine Beendigung gegen Zahlung einer Abfindung, die ordnungsgemäße Abrechnung bis [Datum] und die Erteilung eines qualifizierten Zeugnisses in Betracht kommen.
```

### Baustein B

```text
Das Gericht weist darauf hin, dass es für [Kündigungsgrund/Zahlungsanspruch/Betriebsratsanhörung] auf [konkrete Tatsache] ankommen dürfte. Ergänzender Vortrag kann binnen [Frist] erfolgen.
```

## Benachbarte Skills

- **Davor**: `08-betriebsverfassung-beschlussverfahren` - Vorgelagerten Skill nutzen, wenn der Aktenstand noch nicht bis Urteil Arbeitsgericht trägt.
- **Danach**: `10-entscheidungsvorschlag-arbeitsgericht` - Folgeskill nutzen, sobald Urteil Arbeitsgericht entscheidungs- oder verfügungsreif vorbereitet ist.

## Gerichtliche Arbeitsprodukt-Schärfung

- Rolle: Arbeitsgericht. Der Skill spricht aus der Binnenperspektive des Spruchkörpers und erzeugt Güteterminverfügung, Kammertermin, Urteil, Vergleich oder Beschluss; er ersetzt keine anwaltliche Strategie und keine Parteiberatung.
- Pflichtstamm: Paragrafen 2, 46, 54, 61a ArbGG, Paragrafen 1, 4, 7 KSchG und Paragraf 102 BetrVG. Normen werden im Ergebnis nur verwendet, wenn sie zum konkreten Aktenproblem passen; fehlende Spezialnormen werden als Prüfbedarf markiert.
- Verfügungssprache: Jede Ausgabe endet mit einer konkreten Anschlussverfügung, etwa Anhörung, Fristsetzung, Hinweis, Beweisbeschluss, Terminierung, Abgabe, Vorlage oder Entscheidungsentwurf.
- Stop-Kriterium: Sobald Aktengeheimnis, richterliche Unabhängigkeit, Geschäftsverteilung, Befangenheit, nicht geklärte Zuständigkeit oder ein unaufgeklärter Grundrechtseingriff berührt ist, wird nicht weiter simuliert, sondern eine Vorlage- oder Prüfverfügung formuliert.

## Beitrag zum Streitstoff in diesem Verfahren

Dieser Skill trennt im arbeitsgerichtlichen Streitstoff Klageantrag, Kündigungs- oder Zahlungsgrund, Erwiderung, Güteversuch, Beweisangebot und Vergleichschance. Er benennt, welche Tatsache im Gütetermin zu klären ist, welche Auflage für den Kammertermin gebraucht wird und ob ein Urteil, Vergleich oder Hinweis vorzubereiten ist.

---

## Skill: `06-agg-diskriminierung`

_Wenn es um 06 Agg Diskriminierung in Arbeitsgericht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# 06 Agg Diskriminierung

## Zweck

AGG Paragraf 7: Benachteiligungsverbot, geschuetzte Merkmale Paragraf 1, Beweislastregel Paragraf 22, Entschaedigung und Schadensersatz Paragraf 15, Ausschlussfrist Paragraf 15 Abs. 4

## Rolle


Werkstatt-Assistent für den Vorsitzenden der Kammer am Arbeitsgericht (Paragrafen 16, 17 ArbGG, Berufsrichter mit zwei ehrenamtlichen Richtern aus Arbeitgeber- und Arbeitnehmerkreisen). Gütetermin, Kammerverhandlung, Urteil oder Beschluss.

## Rechtsrahmen

ArbGG, BGB, KSchG, BetrVG, TzBfG, AGG, EFZG, BUrlG, GVG, ZPO

## Pflichtschritte

1. Güteverhandlung (Paragraf 54 ArbGG) vorbereiten und Vergleichsmöglichkeit ausloten.
2. Zulässigkeit und Klageart klären; bei Kündigungsschutz Klagefrist (Paragrafen 4 und 7 KSchG) prüfen.
3. Materielle Prüfung: soziale Rechtfertigung (Paragraf 1 KSchG), Sozialauswahl, abgestufte Darlegungs- und Beweislast.
4. Kammertermin mit ehrenamtlichen Richtern führen; Beweis über streitige erhebliche Tatsachen erheben.
5. Tenor, Streitwert und Kosten (Paragraf 12a ArbGG) bestimmen; bei Beschlussverfahren Besonderheiten (Paragrafen 80 ff. ArbGG) beachten.
6. Arbeitsstand als Vorschlag zur richterlichen Prüfung markieren; die Letztentscheidung trifft der Mensch.
7. Quellen vollständig zitieren (Norm, Aktenzeichen, Datum) und Schwellenwerte sowie Fristen vor Verwendung verifizieren.

## Output

Strukturierter Arbeitsstand: Prüfungspunkte, Zitate, offene Fragen, Vorschlag zur Prüfung.

## Anker-Rechtsprechung

- Paragrafen 1, 2, 7, 15 und 22 AGG: Merkmal, Benachteiligung, Rechtfertigung, Entschädigung und Beweiserleichterung sind strikt zu trennen.
- EuGH, Urteil vom 17.07.2008 - C-303/06, Coleman: Diskriminierungsschutz kann auch bei Benachteiligung wegen Nähe zu einer geschützten Person eingreifen.
- BAG, Urteil vom 19.02.2015 - 8 AZR 1007/13, frei nachweisbar über dejure/openJur: Indizien nach Paragraf 22 AGG müssen eine überwiegende Wahrscheinlichkeit für Benachteiligung tragen.
- Paragraf 61b ArbGG: Klagefrist für Entschädigungsansprüche ist gesondert von der schriftlichen Geltendmachung zu prüfen.
- Ständige Rechtsprechung zu Stellenausschreibungen und Indizien: Wortlaut, Auswahlvermerk und Vergleichspersonen müssen aktenbezogen ausgewertet werden; konkrete Fundstelle vor produktiver Zitierung verifizieren.

## Prüfungsschema in Stufen

1. Agg Diskriminierung: Schutzrichtung, Frist und Anspruchsziel zuerst erfassen.
2. Befristung, Teilzeit, Diskriminierung oder einstweilige Verfügung mit den jeweiligen Spezialnormen prüfen.
3. Darlegungs- und Beweislast, Indizien, Dringlichkeit und Interessenabwägung gesondert sichtbar machen.
4. Gütetermin oder Kammertermin mit konkretem Hinweis auf Vergleichs- und Beweisrisiken vorbereiten.
5. Entscheidung mit Hauptsachebezug, Kosten und Rechtsmittel klar fassen.

## Typische Fallstricke

- Dreiwochenfrist des KSchG wird übersehen und materielle Kündigungsgründe werden dennoch geprüft.
- Guetevergleich laesst Zeugnis, Herausgabe, Abrechnung oder Sprinterklausel offen.
- Brutto- und Nettoantraege werden im Zahlungstenor vermischt.
- Personalakten und Gesundheitsdaten bleiben wegen Paragraf 353b StGB und Paragraf 43 DRiG besonders schuetzenswert.

## Tenor-Bausteine bzw. Beschluss-Bausteine

### Baustein A

```text
Im Gütetermin wird mit den Parteien erörtert, ob eine Beendigung gegen Zahlung einer Abfindung, die ordnungsgemäße Abrechnung bis [Datum] und die Erteilung eines qualifizierten Zeugnisses in Betracht kommen.
```

### Baustein B

```text
Das Gericht weist darauf hin, dass es für [Kündigungsgrund/Zahlungsanspruch/Betriebsratsanhörung] auf [konkrete Tatsache] ankommen dürfte. Ergänzender Vortrag kann binnen [Frist] erfolgen.
```

## Benachbarte Skills

- **Davor**: `05-befristung-und-teilzeit` - Vorgelagerten Skill nutzen, wenn der Aktenstand noch nicht bis Agg Diskriminierung trägt.
- **Danach**: `07-einstweilige-verfuegung-arbeitsrecht` - Folgeskill nutzen, sobald Agg Diskriminierung entscheidungs- oder verfügungsreif vorbereitet ist.

## Gerichtliche Arbeitsprodukt-Schärfung

- Rolle: Arbeitsgericht. Der Skill spricht aus der Binnenperspektive des Spruchkörpers und erzeugt Güteterminverfügung, Kammertermin, Urteil, Vergleich oder Beschluss; er ersetzt keine anwaltliche Strategie und keine Parteiberatung.
- Pflichtstamm: Paragrafen 2, 46, 54, 61a ArbGG, Paragrafen 1, 4, 7 KSchG und Paragraf 102 BetrVG. Normen werden im Ergebnis nur verwendet, wenn sie zum konkreten Aktenproblem passen; fehlende Spezialnormen werden als Prüfbedarf markiert.
- Verfügungssprache: Jede Ausgabe endet mit einer konkreten Anschlussverfügung, etwa Anhörung, Fristsetzung, Hinweis, Beweisbeschluss, Terminierung, Abgabe, Vorlage oder Entscheidungsentwurf.
- Stop-Kriterium: Sobald Aktengeheimnis, richterliche Unabhängigkeit, Geschäftsverteilung, Befangenheit, nicht geklärte Zuständigkeit oder ein unaufgeklärter Grundrechtseingriff berührt ist, wird nicht weiter simuliert, sondern eine Vorlage- oder Prüfverfügung formuliert.

## Beitrag zum Streitstoff in diesem Verfahren

Dieser Skill trennt im arbeitsgerichtlichen Streitstoff Klageantrag, Kündigungs- oder Zahlungsgrund, Erwiderung, Güteversuch, Beweisangebot und Vergleichschance. Er benennt, welche Tatsache im Gütetermin zu klären ist, welche Auflage für den Kammertermin gebraucht wird und ob ein Urteil, Vergleich oder Hinweis vorzubereiten ist.

---

## Anwendungshinweise

1. Diesen Vollprüfung als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.
