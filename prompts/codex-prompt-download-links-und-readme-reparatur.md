# Codex-Prompt: Download-Links und Plugin-READMEs reparieren

Stand: v395.0.0 + zwei Folge-Commits auf main (HEAD 0a347fd829).
Repo: https://github.com/Klotzkette/claude-fuer-deutsches-recht
Branch: main
Author fuer alle Commits: `Klotzkette <39582916+Klotzkette@users.noreply.github.com>`

---

## Worum es geht

Beim Ausrollen von v395.0.0 wurden die Plugin-Tabellen in den READMEs aus marketplace.json neu aufgebaut und 29 Marketplace-Beschreibungen mit plugin.json synchronisiert. Ein anschliessender Vollaudit (Markdown-Links, Anker, Workflow-Builds, Stilkonsistenz) hat sechs Befundklassen ergeben. Die Befunde sind unten als B1 bis B6 aufgelistet. B6 ist kein Bug und darf nicht angefasst werden. B1 bis B5 muessen repariert werden.

Es wurde noch nichts repariert. Du sollst die Reparatur jetzt machen, sauber strukturiert, mit klaren Commits, und am Ende einen neuen Release schneiden (Patch-Bump auf v395.1.0 oder v396.0.0, je nachdem wie tief die Aenderungen reichen, siehe Abschnitt "Release am Ende").

---

## Permanent-Rules (NICHT verhandelbar)

- Author fuer alle Commits: `Klotzkette <39582916+Klotzkette@users.noreply.github.com>`
- KEINE Erwaehnung von Claude, AI, Codex, Assistant, Perplexity in Dateien oder Commit-Messages
- Echte Umlaute (aeoeuess) in Prosa; ae oe ue ss nur in Slugs und JSON-Feldern
- Werkstatt und Schnellstart NUR als Markdown-Download, niemals ZIP
- HTML-Download-Tags `<a href="..." download>` statt Markdown-Links fuer Werkstatt und Schnellstart
- Niemals "scrape" oder "crawl"
- Paragraf statt Paragrafen-Zeichen
- Validator-Regeln einhalten: Skill-description hoechstens 1024 Zeichen; plugin.json und marketplace.json description hoechstens 300 Zeichen; KEIN `\d,\d` (also keine Zahl-Komma-Zahl-Folgen); KEINE XML-Brackets; KEINE Emojis; Slug hoechstens 64 Zeichen und nur `[a-z0-9-]`; Frontmatter nur `name`, `description`, optional `allowed-tools`
- Vor jedem Push: `git fetch origin`
- "Ich will auf KEINEN FALL die validation failed"
- KI-VO, Aktengeheimnis, DSGVO nur in Repo-README, nicht in Plugin-READMEs

---

## Befundliste

### B1 (kritisch): Alle 232 Plugin-READMEs stehen noch im alten Stil

Symptom: Die READMEs enthalten weiterhin Formulierungen wie "Alternative ohne Plugin-Setup" und "hoechstens 7500 Zeichen, Spar-Alternative". Versprochen war: rund um den autogenerierten Block `<!-- BEGIN direkt-loslegen (autogen) -->` ... `<!-- END direkt-loslegen (autogen) -->` soll der Vorbild-Block aus v395 erscheinen (siehe Schema unten). Der letzte Inject-Lauf hat aber nur die Tabelle innerhalb des Blocks ausgetauscht, nicht den umliegenden Direkt-Loslegen-Text.

Soll-Schema fuer den autogenerierten Block:

```markdown
<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

[Plugin-Beschreibung in zwei bis drei Saetzen, mit dem Hinweis, dass es Teil eines Marketplaces mit 232 Plugins ist und dass die zwei Markdown-Prompts eine vollwertige Alternative zum Plugin-Setup sind.]

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`<plugin>.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/<plugin>.zip) |
| Grosser Prompt (Werkstatt) | Markdown | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/<plugin>-werkstatt.md" download><code><plugin>-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/<plugin>-schnellstart.md" download><code><plugin>-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`<plugin>-testakte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/<plugin>-testakte.zip) |

> Marketplace-Hinweis: Dieses Plugin gehoert zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.

<!-- END direkt-loslegen (autogen) -->
```

Aufgabe:
- Skript `scripts/inject-direkt-loslegen-section.py` so erweitern, dass es den kompletten Block zwischen den Markern austauscht, nicht nur die Tabelle.
- Den Block fuer alle 232 Plugins neu rendern.
- Plugin-Beschreibung kommt aus `plugin.json` `description` (gleich wie im Marketplace nach dem Sync).
- Fuer Plugins ohne eigene Testakte (siehe B2 und Sonderfaelle ohne testakte/-Verzeichnis): in der Tabelle Zeile "Testakte(n) als ZIP" auf `alle-testakten.zip` zeigen lassen, mit dem Hinweis "(zentrale Sammlung)".
- Alle alten Formulierungen "Alternative ohne Plugin-Setup", "hoechstens 7500 Zeichen", "Spar-Alternative" muessen weg.

### B2 (kritisch): Drei Plugins mit testakten/ (Plural) statt testakte/ (Singular)

Betroffen:
- `arbeitszeugnisgenerator`
- `arbeitszeugnispruefer`
- `bautraegervertragspruefer`

Symptom: `scripts/build-plugin-testakte-bundles.py` Zeile 52 prueft nur auf `testakte/` Singular. Fuer diese drei Plugins wird daher keine `<plugin>-testakte.zip` gebaut. Die READMEs muessten heute auf `alle-testakten.zip` zeigen.

Aufgabe:
- Drei Verzeichnisse umbenennen: `testakten/` -> `testakte/` per `git mv`.
- Sicherstellen, dass nach dem Umbenennen alle Pfade in YAML-Frontmatter und Skill-Anweisungen weiterhin stimmen (vor allem in `commands/` und `skills/`).
- Lokal Workflow trocken testen: `python scripts/build-plugin-testakte-bundles.py` muss die drei neuen ZIPs erzeugen.
- Im Anschluss laeuft B1 ohnehin neu durch und setzt die Tabellen-Zeile automatisch auf die eigene Plugin-ZIP.

### B3 (kritisch): 875 leere Markdown-Links in 23 Dateien

Symptom: `[Text]()` ohne Ziel, ueberwiegend in generierten Indizes.

Verteilung:
- `SKILLS.md`: 699
- `ASSET_INDEX.md`: 40
- `README.md`: 15 (zum Beispiel "latest Release auf GitHub", "alle-testakten.zip", "aktuellen Release")
- `wahlkampfrecht-praxis/README.md`: 16
- `lobbyregister-bundestag/README.md`: 12
- `geldwaeschepraevention-aml-kyc/README.md`: 11
- `common-law-kompass/README.md`: 10
- `europarecht-kompass/README.md`: 10
- `hoai-leistungsphasen-praxis/README.md`: 9
- `aussenwirtschaft-zoll-sanktionen/README.md`: 8
- restliche Plugins kleiner

Aufgabe:
- Quelle finden: vermutlich die Index-Generatoren `scripts/build-skills-index.py` (oder analog) und `scripts/build-asset-index.py`. Bug ist mit hoher Wahrscheinlichkeit "Link-Text gesetzt, Ziel-URL nicht aufgeloest". Bug fixen, sodass Ziele entweder eine echte URL bekommen oder die Klammern komplett wegfallen.
- Im Root-README die 15 leeren Links auf echte Ziele setzen: latest Release -> `https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest`, `alle-testakten.zip` -> `https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten.zip`, etc.
- In den 10 Plugin-READMEs (wahlkampfrecht-praxis bis aussenwirtschaft-zoll-sanktionen) sind die leeren Links innerhalb von handgeschriebenen Inhaltsabschnitten ausserhalb des autogen-Blocks. Vermutlich Querverweise auf andere Skills oder Testakten. Pruefen, ob die gemeinten Ziele existieren, dann setzen. Falls kein sinnvolles Ziel existierte, in normalen Fliesstext umwandeln (keine Klammern).
- Nach Reparatur: Validator `grep -RnE '\[[^]]+\]\(\)' .` muss null Treffer liefern.

### B4 (mittel): Referenzierte ZIPs ohne Workflow-Build

B4a: `alle-werkstatt-prompts.zip` und `alle-schnellstart-prompts.zip` werden in `prompts/codex-prompt-werkstatt-und-schnellstart-prompts.md` erwaehnt, aber im Release-Workflow nicht gebaut.

B4b: Zwei zentrale Testakten ohne `einzelpdfs.zip`-Referenz: `testakten/formatvorlagen-paradebeispiele` und `testakten/megaprompts`.

Aufgabe:
- B4a: Neues Skript `scripts/build-werkstatt-schnellstart-sammelzips.py` schreiben, das aus allen 232 Plugin-Verzeichnissen die `<plugin>-werkstatt.md` bzw. `<plugin>-schnellstart.md` einsammelt und je eine Sammel-ZIP baut. Workflow `.github/workflows/release-plugin-zips.yml` erweitern, sodass beide ZIPs als Release-Asset hochgeladen werden.
- B4b: Pruefen, ob fuer die beiden Testakten ueberhaupt einzelne PDFs erzeugt werden. Wenn nein, im Top-README den `einzelpdfs.zip`-Verweis dort nicht ergaenzen. Wenn ja, im `scripts/build-testakten-einzelpdf-zips.py` die beiden Slugs nachziehen.

### B5 (klein): Zwei Plugins mit Stil-Mischung in Code-Tags

Betroffen:
- `bautraegervertrag-pruefer/README.md`
- `verhaeltnismaessigkeitspruefer/README.md`

Symptom: Inhalt von `<code>...</code>` enthaelt Umlaute (zum Beispiel `verhaeltnismaessigkeitspruefer-werkstatt.md` korrekt ASCII, aber an manchen Stellen wurden Umlaute reingerutscht). Funktional bricht nichts, aber inkonsistent zum restlichen Repo, wo Slugs immer ASCII sind.

Aufgabe:
- Beide Dateien durchgehen und in allen `<code>...</code>` ausschliesslich ASCII-Slugs lassen.
- Pruefen, ob das B1-Reparaturskript denselben Bug erneut erzeugen wuerde. Wenn ja, im Skript haerten (Slugs immer ASCII, auch wenn die Plugin-Beschreibung Umlaute hat).

### B6 (NICHT REPARIEREN): Vier gewollte Backtick-Anker

Diese Dateien sind ausserhalb der autogen-Tabellen und enthalten Plugin-Referenzen als Backtick-Anker. Das ist beabsichtigt, nicht anfassen:
- `references/rechtsgebiete-uebersicht.md`
- `verwaltete-agentenrezepte/gerichtskalender-monitor/README.md`
- Beide arbeitszeugnis-bluehendes-leben-READMEs

---

## Nicht kaputt (Stand bestaetigt)

- 217 Plugin-ZIP-Direktlinks vorhanden
- 230 von 232 Plugin-READMEs mit korrekten HTML-Download-Tags fuer Werkstatt und Schnellstart (die zwei Ausnahmen siehe B5)
- Alle 232 Werkstatt- und Schnellstart-Markdowns physisch auf Disk
- 210 von 212 Top-Testakten mit `einzelpdfs.zip`-Referenz (siehe B4b)
- Null tote relative Markdown-Pfade
- Validatoren `validate-plugin-structure` und `validate-yaml-frontmatter` gruen
- marketplace.json vs plugin.json: null description-Mismatches

---

## Empfohlene Reihenfolge

1. B2 zuerst: `testakten/` -> `testakte/` umbenennen fuer die drei Plugins. Workflow erkennt sie dann automatisch.
2. B3a: Index-Generatoren reparieren, `SKILLS.md` und `ASSET_INDEX.md` neu bauen.
3. B3b: Manuelle Reparatur der 15 Root-README-Links und der zehn Plugin-READMEs mit handgeschriebenen leeren Links.
4. B4a: Sammel-ZIP-Skript schreiben, Workflow erweitern.
5. B4b: Einzelpdfs fuer die zwei zentralen Testakten pruefen und ggf. ergaenzen.
6. B1: Inject-Skript haerten, Vorbild-Block fuer alle 232 Plugins ausrollen. Dabei automatisch B5 mit erschlagen, weil das Skript dann sauber ASCII-Slugs in die Tabelle setzt. Anschliessend B5 in den beiden handgeschriebenen Bereichen der zwei Plugin-READMEs separat nachziehen.
7. Validatoren laufen: `python scripts/validate-plugin-structure.py`, `python scripts/validate-yaml-frontmatter.py`, plus `grep -RnE '\[[^]]+\]\(\)' .` darf null Treffer liefern.

---

## Commits und Release

Atomare Commits pro Befund, jeweils mit Author Klotzkette:

- `B2: testakten -> testakte fuer arbeitszeugnisgenerator, arbeitszeugnispruefer, bautraegervertragspruefer`
- `B3: leere Markdown-Links in SKILLS.md, ASSET_INDEX.md, README.md und 10 Plugin-READMEs reparieren`
- `B4a: Sammel-ZIPs alle-werkstatt-prompts und alle-schnellstart-prompts im Release-Workflow bauen`
- `B4b: einzelpdfs-ZIPs fuer formatvorlagen-paradebeispiele und megaprompts ergaenzen` (falls anwendbar)
- `B1: Vorbild-Block in allen 232 Plugin-READMEs ausrollen, Inject-Skript haertet den gesamten Block zwischen den Markern`
- `B5: ASCII-Slugs in <code>-Tags fuer bautraegervertrag-pruefer und verhaeltnismaessigkeitspruefer vereinheitlichen`

Vor jedem Push: `git fetch origin`.

Release am Ende:
- Wenn nur Doku und Skripte: v395.1.0 als Tag
- Wenn marketplace.json oder plugin.json beruehrt wurde: v396.0.0 als Tag
- Tag pushen, GitHub Actions soll automatisch alle Release-Assets bauen (Plugin-ZIPs, Testakte-ZIPs, einzelpdfs-ZIPs, Skills-Markdown-ZIPs, Sammel-ZIPs, neu: Werkstatt- und Schnellstart-Sammel-ZIPs)

---

## Kontrollfragen vor Push

- Validatoren beide gruen?
- `grep -RnE '\[[^]]+\]\(\)' .` null Treffer?
- Drei `<plugin>-testakte.zip` neu im Build?
- Alle 232 Plugin-READMEs enthalten den Vorbild-Block ohne alte Formulierungen?
- `alle-werkstatt-prompts.zip` und `alle-schnellstart-prompts.zip` im Workflow?
- Keine Erwaehnung von Claude, AI, Codex, Assistant, Perplexity in Dateien oder Commit-Messages?
- Author ueberall Klotzkette?
