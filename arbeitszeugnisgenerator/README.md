# Arbeitszeugnisgenerator

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Erstellt deutsche Arbeitszeugnisse Schritt für Schritt: Rolle, Stammdaten, Tätigkeiten, Leistungs- und Verhaltensbewertung, Notenwahl per Ampelsystem, Schlussformeln. Wahlweise vorgegebene Note oder geführte Einschätzung. Mehrere Harnesses: qualifiziert, einfach, Ausbildung.

Dieses Plugin gehört zum Marketplace mit 235 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Direktnavigation: [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/arbeitszeugnisgenerator.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`arbeitszeugnisgenerator.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnisgenerator.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnisgenerator/arbeitszeugnisgenerator-werkstatt.md" download><code>arbeitszeugnisgenerator-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnisgenerator/arbeitszeugnisgenerator-schnellstart.md" download><code>arbeitszeugnisgenerator-schnellstart.md</code></a> |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| Pluginlokale Akte | [Gesamt-PDF](testakte/gesamt-pdf/testakte_gesamt.pdf) | [`arbeitszeugnisgenerator-testakte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnisgenerator-testakte.zip) | [`arbeitszeugnisgenerator-testakte-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnisgenerator-testakte-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du ein deutsches Arbeitszeugnis Schritt für Schritt erstellen — rechtssicher, mit korrekter Zeugnissprache, in der gewünschten Notenstufe.

## Wenn du das brauchst

- **Personalabteilung** muss für einen ausscheidenden Mitarbeiter ein qualifiziertes Arbeitszeugnis erstellen und braucht passende Formeln zur Wunschnote.
- **Geschäftsführer einer kleinen Firma** schreibt zum ersten Mal ein Arbeitszeugnis und will nicht versehentlich Geheimcodes einbauen, die die Note kippen.
- **Arbeitnehmer** möchte einen sauberen Vorschlag für das Wunschzeugnis erstellen und der HR-Abteilung vorlegen.
- **Auszubildender oder Ausbilder** braucht ein Ausbildungszeugnis nach Paragraf 16 BBiG.

## Was du am Ende in der Hand hast

Ein vollständiges Arbeitszeugnis im richtigen Format — qualifiziertes Zeugnis, einfaches Zeugnis, Zwischenzeugnis oder Ausbildungszeugnis — mit Kopfdaten, Tätigkeitsbeschreibung, Leistungs- und Verhaltensbewertung in der Wunschnote, Schlussformel und Beendigungsgrund. Auf Wunsch mit Begründung pro Satz, welche Notenwirkung er entfaltet.

## Der Weg dorthin

Rolle und Anliegen klären → Zeugnisart und Harness wählen → Stammdaten erfassen → Tätigkeiten erheben → Notenwahl (vorgeben oder durch Fragen ermitteln lassen) → satzweise Generierung mit Ampel-Vorschau → Schlussformel und Beendigungsgrund → Revision und Feinschliff.

## Workflows

Drei Modi zur Wahl:

- **Direkt-Modus**: Du gibst die Wunschnote pro Bewertungsfeld vor (Leistung, Verhalten, Führung). Der Generator setzt die passenden Formeln.
- **Geführter Modus**: Der Generator stellt gezielte Fragen zu Leistung, Engagement, Verhalten — und schlägt am Ende eine Note vor ("das klingt nach Note 2 bis 3, soll ich so schreiben?"). Du bestätigst oder korrigierst.
- **Hybrid-Modus**: Du gibst die Gesamtnote vor, der Generator fragt nur noch die offenen Details ab (typische Tätigkeiten, besondere Projekte, Beendigungsgrund).

## Was dich aufhält

- **Wohlwollensgrundsatz versus Wahrheitspflicht**: Beides muss eingehalten werden, kein Schönschreiben um den Preis der Wahrheit.
- **Geheimcodes**: Versehentlich eingebaute Negativcodes ("bemüht sich", "im Großen und Ganzen", "lernte schnell kennen und schätzen") kippen die Note. Der Generator vermeidet sie aktiv.
- **Zeugnisklarheit (objektiver Empfängerhorizont, BAG 9 AZR 352.04)**: Keine doppelten Böden, keine widersprüchlichen Aussagen.
- **Äußere Form**: Briefkopf, Datum, Unterschrift, kein Knick, keine Streichungen.
- **Schlussformel-Wirkung**: Schlussformeln wirken oft stärker als die Bewertungssätze. Eine schwache Schlussformel zieht die Gesamtnote.

## Rechtlicher Anker

- Paragraf 109 GewO (Zeugnisanspruch)
- Paragraf 16 BBiG (Ausbildungszeugnis)
- Paragrafen 241 Absatz 2, 280 Absatz 1 BGB (Nebenpflicht und Schadensersatz)
- BAG-Leitentscheidungen zu Notenstufen, Beweislast, Schlussformel und Zeugnisklarheit (im Werkstatt-Prompt ausführlich)

## KI-Verordnung: mögliche Einstufung als Hochrisiko-KI

Wird dieses Plugin im Personalwesen produktiv eingesetzt, kann es ein Hochrisiko-KI-System nach Artikel 6 Absatz 2 in Verbindung mit Anhang III Nummer 4 Buchstabe b der Verordnung (EU) 2024/1689 (KI-Verordnung) sein. Anhang III Nummer 4 Buchstabe b erfasst KI-Systeme, die bestimmungsgemäß für Entscheidungen über die Bedingungen von Arbeitsverhältnissen, für die Bewertung der Arbeitsleistung und des Arbeitsverhaltens oder für vergleichbare Personalentscheidungen verwendet werden. Ein automatisiert erstelltes Arbeitszeugnis betrifft genau diese Bewertungs- und Bedingungsdimension. Anhang III Nummer 4 Buchstabe a erfasst dagegen die Personalauswahl und Bewerbungsphase und greift hier in der Regel nicht.

Folgen einer Einstufung als Hochrisiko-KI können sein: Pflicht zu menschlicher Aufsicht, Dokumentations- und Transparenzpflichten, Risikomanagement, Information der Beschäftigten beziehungsweise des Betriebsrats und gegebenenfalls eine Grundrechte-Folgenabschätzung. Die genaue Reichweite hängt vom Einsatzkontext, von der Rolle als Anbieter oder Betreiber und vom Geltungsbeginn nach Artikel 113 KI-VO ab. Diese Hinweise sind keine Rechtsberatung; im Zweifel ist eine arbeitsrechtliche und KI-rechtliche Bewertung im Einzelfall geboten.

## Hinweise

Generischer Entwurfsstand, alle Angaben ohne Gewähr. Jede Nutzerin und jeder Nutzer prüft den generierten Text auf Plausibilität und Eignung im konkreten Einzelfall. Keine Rechtsberatung. Keine Garantie für Vollständigkeit oder Aktualität der Rechtsprechung. Bei streitigen Fällen Fachanwalt für Arbeitsrecht hinzuziehen.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 2. Unterlagen, Sachverhalt und Quellen | [`bag-leitentscheidungen-beweislast`](skills/bag-leitentscheidungen-beweislast/SKILL.md), [`kopfdaten-und-aussere-form`](skills/kopfdaten-und-aussere-form/SKILL.md), [`stammdaten-erhebung`](skills/stammdaten-erhebung/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`fuehrungskraft-bewertung`](skills/fuehrungskraft-bewertung/SKILL.md) |
| 4. Gestaltung, Strategie und Verhandlung | [`compliance-integritaet-formeln`](skills/compliance-integritaet-formeln/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`auslassungen-vermeiden`](skills/auslassungen-vermeiden/SKILL.md), [`bag-leitentscheidungen-notenstufen`](skills/bag-leitentscheidungen-notenstufen/SKILL.md), [`beendigungsgrund-formulieren`](skills/beendigungsgrund-formulieren/SKILL.md), [`belastbarkeit-formeln`](skills/belastbarkeit-formeln/SKILL.md), [`besondere-leistungen-projekte`](skills/besondere-leistungen-projekte/SKILL.md), [`drift-und-schaufenster-vermeiden`](skills/drift-und-schaufenster-vermeiden/SKILL.md), [`einfuehrung-mandantenanliegen`](skills/einfuehrung-mandantenanliegen/SKILL.md), [`engagement-motivation-formeln`](skills/engagement-motivation-formeln/SKILL.md), [`frequenzadverbien-katalog`](skills/frequenzadverbien-katalog/SKILL.md), [`geheimcodes-vermeiden`](skills/geheimcodes-vermeiden/SKILL.md), [`langzeit-arbeitsverhaeltnis`](skills/langzeit-arbeitsverhaeltnis/SKILL.md), [`mehrere-positionen-im-zeugnis`](skills/mehrere-positionen-im-zeugnis/SKILL.md), [`note-1-formeln-leistung`](skills/note-1-formeln-leistung/SKILL.md), [`note-2-formeln-leistung`](skills/note-2-formeln-leistung/SKILL.md), [`note-3-formeln-leistung`](skills/note-3-formeln-leistung/SKILL.md), [`note-4-formeln-leistung`](skills/note-4-formeln-leistung/SKILL.md), [`note-5-formeln-leistung`](skills/note-5-formeln-leistung/SKILL.md), [`notenwahl-modus`](skills/notenwahl-modus/SKILL.md), ... plus 17 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 40 Skills in diesem Plugin. Jeder Skillname öffnet die zugehörige `SKILL.md`; Beschreibungen stammen aus deren `description`-Feld.

| Skill | Beschreibung |
| --- | --- |
| [`auslassungen-vermeiden`](skills/auslassungen-vermeiden/SKILL.md) | Wenn es um Auslassungen vermeiden in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`bag-leitentscheidungen-beweislast`](skills/bag-leitentscheidungen-beweislast/SKILL.md) | Wenn es um BAG-Leitentscheidungen zur Beweislast in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`bag-leitentscheidungen-notenstufen`](skills/bag-leitentscheidungen-notenstufen/SKILL.md) | Wenn es um BAG-Leitentscheidungen zu Notenstufen in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`beendigungsgrund-formulieren`](skills/beendigungsgrund-formulieren/SKILL.md) | Wenn es um Beendigungsgrund formulieren in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`belastbarkeit-formeln`](skills/belastbarkeit-formeln/SKILL.md) | Wenn es um Belastbarkeit-Formeln in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`besondere-leistungen-projekte`](skills/besondere-leistungen-projekte/SKILL.md) | Wenn es um Besondere Leistungen und Projekte in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`compliance-integritaet-formeln`](skills/compliance-integritaet-formeln/SKILL.md) | Wenn es um Compliance- und Integritäts-Formeln in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`drift-und-schaufenster-vermeiden`](skills/drift-und-schaufenster-vermeiden/SKILL.md) | Wenn es um Drift und Schaufenster vermeiden in Arbeitszeugnisgenerator geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Sch... |
| [`einfuehrung-mandantenanliegen`](skills/einfuehrung-mandantenanliegen/SKILL.md) | Wenn es um Einführung und Mandantenanliegen in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`engagement-motivation-formeln`](skills/engagement-motivation-formeln/SKILL.md) | Wenn es um Engagement- und Motivations-Formeln in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`frequenzadverbien-katalog`](skills/frequenzadverbien-katalog/SKILL.md) | Wenn es um Frequenzadverbien-Katalog in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`fuehrungskraft-bewertung`](skills/fuehrungskraft-bewertung/SKILL.md) | Wenn es um Führungskraft-Bewertung in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`geheimcodes-vermeiden`](skills/geheimcodes-vermeiden/SKILL.md) | Wenn es um Geheimcodes vermeiden in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`kopfdaten-und-aussere-form`](skills/kopfdaten-und-aussere-form/SKILL.md) | Wenn es um Kopfdaten und äußere Form in Arbeitszeugnisgenerator geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`langzeit-arbeitsverhaeltnis`](skills/langzeit-arbeitsverhaeltnis/SKILL.md) | Wenn es um Langzeit-Arbeitsverhältnis in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`mehrere-positionen-im-zeugnis`](skills/mehrere-positionen-im-zeugnis/SKILL.md) | Wenn es um Mehrere Positionen im Zeugnis in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`note-1-formeln-leistung`](skills/note-1-formeln-leistung/SKILL.md) | Wenn es um Note 1 — Formeln Leistung in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`note-2-formeln-leistung`](skills/note-2-formeln-leistung/SKILL.md) | Wenn es um Note 2 — Formeln Leistung in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`note-3-formeln-leistung`](skills/note-3-formeln-leistung/SKILL.md) | Wenn es um Note 3 — Formeln Leistung in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`note-4-formeln-leistung`](skills/note-4-formeln-leistung/SKILL.md) | Wenn es um Note 4 — Formeln Leistung in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`note-5-formeln-leistung`](skills/note-5-formeln-leistung/SKILL.md) | Wenn es um Note 5 — Formeln Leistung in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`notenwahl-modus`](skills/notenwahl-modus/SKILL.md) | Wenn es um Notenwahl-Modus in Arbeitszeugnisgenerator geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| [`rechtlicher-anker-109-gewo`](skills/rechtlicher-anker-109-gewo/SKILL.md) | Wenn es um Rechtlicher Anker — Paragraf 109 GewO und verwandte Normen in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`revision-und-aenderungswuensche`](skills/revision-und-aenderungswuensche/SKILL.md) | Wenn es um Revision und Änderungswünsche in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`rollen-und-harness-wahl`](skills/rollen-und-harness-wahl/SKILL.md) | Wenn es um Rollen und Harness-Wahl in Arbeitszeugnisgenerator geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| [`schlussformel-baukasten`](skills/schlussformel-baukasten/SKILL.md) | Wenn es um Schlussformel-Baukasten in Arbeitszeugnisgenerator geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| [`schlussformel-notenwirkung`](skills/schlussformel-notenwirkung/SKILL.md) | Wenn es um Schlussformel-Notenwirkung in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`stammdaten-erhebung`](skills/stammdaten-erhebung/SKILL.md) | Wenn es um Stammdaten-Erhebung in Arbeitszeugnisgenerator geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| [`steigerungsadverbien-katalog`](skills/steigerungsadverbien-katalog/SKILL.md) | Wenn es um Steigerungsadverbien-Katalog in Arbeitszeugnisgenerator geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| [`taetigkeitsbeschreibung-erheben`](skills/taetigkeitsbeschreibung-erheben/SKILL.md) | Wenn es um Tätigkeitsbeschreibung erheben in Arbeitszeugnisgenerator geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`teamarbeit-formeln`](skills/teamarbeit-formeln/SKILL.md) | Wenn es um Teamarbeit-Formeln in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`teilzeit-elternzeit-darstellung`](skills/teilzeit-elternzeit-darstellung/SKILL.md) | Wenn es um Teilzeit und Elternzeit im Zeugnis in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verhalten-vorgesetzte-kollegen-kunden`](skills/verhalten-vorgesetzte-kollegen-kunden/SKILL.md) | Wenn es um Verhalten gegenüber Vorgesetzten, Kollegen und Kunden in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`wohlwollensgrundsatz-und-wahrheit`](skills/wohlwollensgrundsatz-und-wahrheit/SKILL.md) | Wenn es um Wohlwollensgrundsatz und Wahrheit in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`zeugnisart-ausbildungszeugnis-16-bbig`](skills/zeugnisart-ausbildungszeugnis-16-bbig/SKILL.md) | Wenn es um Zeugnisart: Ausbildungszeugnis nach Paragraf 16 BBiG in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`zeugnisart-einfach`](skills/zeugnisart-einfach/SKILL.md) | Wenn es um Zeugnisart: Einfaches Arbeitszeugnis in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`zeugnisart-praktikum`](skills/zeugnisart-praktikum/SKILL.md) | Wenn es um Zeugnisart: Praktikumszeugnis in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`zeugnisart-qualifiziert`](skills/zeugnisart-qualifiziert/SKILL.md) | Wenn es um Zeugnisart: Qualifiziertes Arbeitszeugnis in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`zeugnisart-zwischenzeugnis`](skills/zeugnisart-zwischenzeugnis/SKILL.md) | Wenn es um Zeugnisart: Zwischenzeugnis in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`zeugnisklarheit-objektiver-empfaengerhorizont`](skills/zeugnisklarheit-objektiver-empfaengerhorizont/SKILL.md) | Wenn es um Zeugnisklarheit — objektiver Empfängerhorizont (BAG 9 AZR 352/04; 9 AZR 386/10) in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofort... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
