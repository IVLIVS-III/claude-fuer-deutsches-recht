# Bauträgervertragsprüfer


<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`bautraegervertragspruefer`) | [`bautraegervertragspruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bautraegervertragspruefer.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

### Demonstrations-Akte

| Akte | Download |
| --- | --- |
| Pluginlokale Testakte | [`bautraegervertragspruefer-testakte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bautraegervertragspruefer-testakte.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Prüft deutsche Bauträgerverträge: MaBV-Ratenplan und Sicherheiten, Paragrafen 650u und 650v BGB, AGB-Kontrolle, Baubeschreibung, Abnahme Gemeinschaftseigentum, Bauzeit, Preisanpassung, Teilungserklärung. Liefert Mandantengutachten und Aufforderungsschreiben an Bauträger und Notar.

Dieses Plugin gehört zum Marketplace mit 234 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`bautraegervertragspruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bautraegervertragspruefer.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/bautraegervertragspruefer/bautraegervertragspruefer-werkstatt.md" download><code>bautraegervertragspruefer-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/bautraegervertragspruefer/bautraegervertragspruefer-schnellstart.md" download><code>bautraegervertragspruefer-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [Gesamt-PDF](testakte/gesamt-pdf/testakte_gesamt.pdf), [`bautraegervertragspruefer-testakte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bautraegervertragspruefer-testakte.zip), [`bautraegervertragspruefer-testakte-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bautraegervertragspruefer-testakte-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 234 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du einen deutschen Bauträgervertrag verbraucherseitig prüfen: Ratenplan, Sicherheiten, Baubeschreibung, Abnahme, Bauzeit, Preisanpassung, Teilungserklärung — und am Ende ein Gutachten plus ein Aufforderungsschreiben an Bauträger und Notar in der Hand haben.

**Schwester-Plugin:** [`bautraegervertrag-pruefer`](../bautraegervertrag-pruefer) (mit Bindestrich) deckt dasselbe Mandat mit einzeln ladbaren Spezial-Skills samt references-Workflow ab; dieses Plugin hier bietet Megaprompt-Original und zwei Testakten. Für ein Mandat genügt eines von beiden.

## Wenn du das brauchst

- **Verbraucher** hat einen Bauträgervertrag erhalten und will vor der notariellen Beurkundung wissen, welche Klauseln unwirksam sind und welche Streichungen er fordern muss.
- **Fachanwalt für Bau- und Architektenrecht** prüft einen Bauträgervertrag im Mandat und braucht eine vollständige Klauselmatrix mit MaBV-Prüfung und AGB-Kontrolle.
- **Notar** will den Entwurf gegen die Pflichten aus Paragraf 14 BNotO und gegen die MaBV-Schutzstruktur durchsehen.
- **Finanzierende Bank** prüft den Vertrag auf Auszahlungsrisiken nach dem Ratenplan und auf die Werthaltigkeit der Sicherheiten.

## Was du am Ende in der Hand hast

Eine Klauselmatrix Satz für Satz mit Ampel-Einschätzung (rot, orange, grün), ein Mandantengutachten mit paragraphenbezogener Begründung, ein Aufforderungsschreiben an Bauträger und Notar mit konkreter richtiger Fassung pro beanstandeter Klausel sowie eine Verhandlungsstrategie mit Gegenargument-Antwort.

## Der Weg dorthin

Vertrag und Anlagen einlesen → Fall-Fingerabdruck erstellen (Parteien, Einheit, Projekt, Preis, Ratenplan, Sicherheiten) → MaBV-Ratenplan und Sicherheiten prüfen → AGB-Kontrolle Klausel für Klausel → Baubeschreibung gegen Bausoll und anerkannte Regeln der Technik halten → Abnahme Gemeinschaftseigentum und Schlussrate prüfen → Bauzeit, Preisanpassung, Teilungserklärung kontrollieren → Mandantengutachten und Aufforderungsschreiben ausgeben.

## Workflows

Drei Modi zur Wahl:

- **Schnellprüfung**: Top-Zehn-Auffälligkeiten, geschätztes Risikoprofil, Empfehlung in wenigen Sätzen.
- **Vollprüfung**: Fall-Fingerabdruck, Klauselmatrix, AGB-Kontrolle, MaBV-Prüfung, Mandantengutachten.
- **Verhandlungspfad**: Vollprüfung plus Aufforderungsschreiben an Bauträger und Notar mit konkreter richtiger Fassung pro Klausel und Verhandlungsstrategie.

## Was dich aufhält

- **MaBV-Ratenplan**: Überhöhte Vorleistungen, falsche Verteilung der Raten auf Bauabschnitte, fehlende Sicherheit nach Paragraf 7 MaBV.
- **Verbraucherbauvertrag**: Paragrafen 650u und 650v BGB, Baubeschreibung als Pflichtinhalt, verbindliche Angabe zum Bauzeitende.
- **AGB-Kontrolle**: Notarielle Beurkundung schliesst AGB-Kontrolle nicht aus; geltungserhaltende Reduktion findet bei unwirksamen Verbraucher-AGB nicht statt.
- **Abnahme Gemeinschaftseigentum**: Verklammerung der Abnahme mit der Schlussrate gefährdet die werthaltige Sicherung.
- **Baubeschreibung**: Pauschale Verweise auf anerkannte Regeln der Technik ohne konkrete Spezifikation lassen das Bausoll offen.

## Rechtlicher Anker

- Paragrafen 650u und 650v BGB (Bauträgervertrag, Baubeschreibung)
- Paragrafen 305 bis 310 BGB (AGB-Kontrolle)
- Makler- und Bauträgerverordnung (MaBV), insbesondere Paragrafen 3, 7
- Paragraf 14 BNotO (Belehrungspflichten Notar)
- Wohnungseigentumsgesetz (Teilungserklärung, Abnahme Gemeinschaftseigentum)
- HOAI (Leistungsphasen Objektüberwachung)
- BGH-Leitentscheidungen zu Bauträgervertrag, MaBV und Abnahmeklauseln (im Werkstatt-Prompt ausführlich)

## Hinweise

Generischer Prüfstand, alle Angaben ohne Gewähr. Jede Nutzerin und jeder Nutzer prüft den Prüfbericht auf Plausibilität und Eignung im konkreten Einzelfall. Keine Rechtsberatung. Keine Garantie für Vollständigkeit oder Aktualität der Rechtsprechung. Bei streitigen Fällen Fachanwalt für Bau- und Architektenrecht oder Notar hinzuziehen.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 2. Unterlagen, Sachverhalt und Quellen | `drei-dokumente-paket-erzeugen`, `mandantengutachten-aufbau` |
| 3. Prüfung, Anspruch und Subsumtion | `verbraucherstatus-pruefen` |
| 4. Gestaltung, Strategie und Verhandlung | `agb-kontrolle-klauseln`, `bautraegervertrag-qualifikation`, `bauzeitenplan-verzug`, `mabv-ratenplan-pruefen` |
| 5. Verfahren, Behörde und Gericht | `weg-beschluss-anfechtung` |
| 6. Ergebnis, Schreiben und Kommunikation | `aufforderungsschreiben-bautraeger-und-notar` |
| 8. Spezialmodule und Schnittstellen | `abnahme-gemeinschaftseigentum`, `abnahme-sondereigentum-paragraf-640`, `auflassungsvormerkung-und-grundbuch`, `baubeschreibung-bausoll-pruefen`, `faelligkeitsmitteilung-pruefen`, `fall-fingerabdruck-erstellen`, `fertigstellungssicherheit-650m-pruefen`, `gemeinschaft-zieht-maengelrechte-an-sich`, `gesamtnichtigkeit-paragraf-306-bgb`, `hoai-bauueberwachung-private-bauueberwachung`, `insolvenzrisiken-bautraeger`, `mabv-sicherheit-paragraf-7-pruefen`, `maengelrechte-633-634-bgb`, `mittlere-art-und-guete-und-din`, `notarbelehrung-paragraf-14-bnoto-17-beurkg`, `paragraf-308-nr-4-bgb-leistungsaenderung`, `paragraf-309-nr-12-bgb-tatsachenbestaetigung`, `preisanpassung-und-sonderwuensche`, ... plus 3 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 30 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abnahme-gemeinschaftseigentum` | Wenn es um Abnahme Gemeinschaftseigentum in Bauträgervertragsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `abnahme-sondereigentum-paragraf-640` | Wenn es um Abnahme Sondereigentum Paragraf 640 BGB in Bauträgervertragsprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `agb-kontrolle-klauseln` | Wenn es um AGB-Kontrolle Klauseln in Bauträgervertragsprüfer geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `aufforderungsschreiben-bautraeger-und-notar` | Wenn es um Aufforderungsschreiben an Bauträger und Notar in Bauträgervertragsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `auflassungsvormerkung-und-grundbuch` | Wenn es um Auflassungsvormerkung und Grundbuch in Bauträgervertragsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `baubeschreibung-bausoll-pruefen` | Wenn es um Baubeschreibung und Bausoll prüfen in Bauträgervertragsprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bautraegervertrag-qualifikation` | Wenn es um Bauträgervertrag-Qualifikation in Bauträgervertragsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bauzeitenplan-verzug` | Wenn es um Bauzeitenplan und Verzug in Bauträgervertragsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `drei-dokumente-paket-erzeugen` | Wenn es um Drei-Dokumente-Paket erzeugen in Bauträgervertragsprüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `faelligkeitsmitteilung-pruefen` | Wenn es um Fälligkeitsmitteilung prüfen in Bauträgervertragsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fall-fingerabdruck-erstellen` | Wenn es um Fall-Fingerabdruck erstellen in Bauträgervertragsprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `fertigstellungssicherheit-650m-pruefen` | Wenn es um Fertigstellungssicherheit Paragraf 650m Absatz 2 BGB prüfen in Bauträgervertragsprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkt... |
| `gemeinschaft-zieht-maengelrechte-an-sich` | Wenn es um Gemeinschaft zieht Mängelrechte an sich in Bauträgervertragsprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und näch... |
| `gesamtnichtigkeit-paragraf-306-bgb` | Wenn es um Gesamtnichtigkeit Paragraf 306 BGB in Bauträgervertragsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `hoai-bauueberwachung-private-bauueberwachung` | Wenn es um HOAI, Bauüberwachung und private Bauüberwachung in Bauträgervertragsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `insolvenzrisiken-bautraeger` | Wenn es um Insolvenzrisiken Bauträger in Bauträgervertragsprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `mabv-ratenplan-pruefen` | Wenn es um MaBV-Ratenplan prüfen in Bauträgervertragsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `mabv-sicherheit-paragraf-7-pruefen` | Wenn es um MaBV-Sicherheit Paragraf 7 prüfen in Bauträgervertragsprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem S... |
| `maengelrechte-633-634-bgb` | Wenn es um Mängelrechte Paragrafen 633 und 634 BGB in Bauträgervertragsprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und näch... |
| `mandantengutachten-aufbau` | Wenn es um Mandantengutachten Aufbau in Bauträgervertragsprüfer geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `mittlere-art-und-guete-und-din` | Wenn es um Mittlere Art und Güte und DIN-Normen in Bauträgervertragsprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächste... |
| `notarbelehrung-paragraf-14-bnoto-17-beurkg` | Wenn es um Notarbelehrung Paragraf 14 BNotO und Paragraf 17 BeurkG in Bauträgervertragsprüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfr... |
| `paragraf-308-nr-4-bgb-leistungsaenderung` | Wenn es um Leistungsänderungsvorbehalte Paragraf 308 Nummer 4 BGB in Bauträgervertragsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `paragraf-309-nr-12-bgb-tatsachenbestaetigung` | Wenn es um Paragraf 309 Nummer 12 BGB — Tatsachenbestätigung und Beweislast in Bauträgervertragsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `preisanpassung-und-sonderwuensche` | Wenn es um Preisanpassung und Sonderwünsche in Bauträgervertragsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `teilungserklaerung-gemeinschaftsordnung` | Wenn es um Teilungserklärung und Gemeinschaftsordnung in Bauträgervertragsprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und n... |
| `verbraucherstatus-pruefen` | Wenn es um Verbraucherstatus prüfen in Bauträgervertragsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `verjaehrung-634a-bgb-hemmung` | Wenn es um Verjährung Paragraf 634a BGB und Hemmung in Bauträgervertragsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `weg-beschluss-anfechtung` | Wenn es um WEG-Beschluss-Anfechtung in Bauträgervertragsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `wohnflaeche-pruefen` | Wenn es um Wohnfläche prüfen in Bauträgervertragsprüfer geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
