# Vollprüfung: anlagen-zu-schriftsaetzen

## Zusammensetzung

Dieser Vollprüfung enthaelt top-8 von 116 Skills (gekuerzt fuer Chat-Fenster) des Plugins `anlagen-zu-schriftsaetzen`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Wenn es um Einstieg und Routing in Anlagen zu Schriftsätzen geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden…
2. **kaltstart-triage** — Wenn es um Kaltstart Triage in Anlagen zu Schriftsätzen geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden näc…
3. **anlagenverzeichnis-gericht-kanzlei-und-intern** — Wenn es um Anlagenverzeichnis für Gericht, Kanzlei und intern in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm…
4. **anlagenverzeichnis-kanzlei-grundaufbau-bea** — Wenn es um Anlagenverzeichnis für Gericht, Kanzlei und intern in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm…
5. **original-abschrift-kopie-und-elektronische-fassung** — Wenn es um Original, Abschrift, Kopie und elektronische Fassung in Anlagen zu Schriftsätzen geht: ordnet Akteninhalt, Be…
6. **anlagen-uebergabe-an-assistenz-und-legal-tech** — Wenn es um Übergabe an Assistenz und Legal Tech in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm, Beweislast, …
7. **nachreichung-berichtigung-und-gerichtshinweis** — Wenn es um Nachreichung, Berichtigung und gerichtlicher Hinweis in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, No…
8. **nachreichung-berichtigung-ocr-scan-original** — Wenn es um Nachreichung, Berichtigung und gerichtlicher Hinweis in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, No…

---

## Skill: `einstieg-routing`

_Wenn es um Einstieg und Routing in Anlagen zu Schriftsätzen geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Anlagen Zu Schriftsaetzen** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `anlage-fehlerkatalog` — Anlage Fehlerkatalog
- `anlage-red-anlagen-anlagenkonvolut-sonderfall` — Anlage RED Anlagen Anlagenkonvolut Sonderfall
- `anlagen-an-assistenz-uebersetzungspflicht` — Anlagen AN Assistenz Übersetzungspflicht
- `anlagen-aus-datenraum-und-sharepoint` — Anlagen AUS Datenraum und Sharepoint
- `anlagen-aus-edv-systemen` — Anlagen AUS EDV Systemen
- `anlagen-aus-mandantenmaterial` — Anlagen AUS Mandantenmaterial
- `anlagen-bei-berufung-revision` — Anlagen bei Berufung Revision
- `anlagen-bei-eilantrag-eu-arrest` — Anlagen bei Eilantrag EU Arrest
- `anlagen-berufung-revision-eilantrag-eu-bilder` — Anlagen Berufung Revision Eilantrag EU Bilder
- `anlagen-bilder-screenshots` — Anlagen Bilder Screenshots
- `anlagen-check-zustellung-redaktion-dsgvo` — Anlagen Check Zustellung Redaktion DSGVO
- `anlagen-duplikate-versionen-hashlog` — Anlagen Duplikate Versionen Hashlog
- `anlagen-elektronische-dokumente-format` — Anlagen Elektronische Dokumente Format
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Normenanker

Arbeitsfokus: **Einstieg und Routing**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `§ 130 Nr. 6 ZPO` — Schriftsatzanforderungen.
- `§ 130a Abs. 1 ZPO` — elektronisches Dokument.
- `§ 131 Abs. 1 ZPO` — Beifügung von Abschriften/Anlagen.
- `§ 133 Abs. 1 ZPO` — Abschriften für Zustellung.
- `§ 138 Abs. 1 ZPO` — Tatsachenvortrag.
- `§ 253 Abs. 2 ZPO` — Klageinhalt.
- `§ 299 Abs. 1 ZPO` — Akteneinsicht.
- `§ 371 Abs. 1 ZPO` — Augenschein.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Anlagen Zu Schriftsaetzen sind die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `kaltstart-triage`

_Wenn es um Kaltstart Triage in Anlagen zu Schriftsätzen geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten._

## Direktstart: lesen, entscheiden, liefern

Beginne nicht mit einem Fragenkatalog. Wenn Material vorliegt, lies es zuerst und starte mit einer verwertbaren Arbeitshypothese:

- Frist oder Sofortrisiko.
- erkannte Rolle, Zielrichtung und Verfahrensstand.
- tragende Tatsachen aus dem Material.
- bester nächster Arbeitsschritt mit direkt nutzbarem Output.

Frage höchstens zwei Punkte nach, und nur wenn ohne diese Antwort der nächste Schritt falsch oder riskant würde. Fehlt Material vollständig, verlange nicht allgemein alle Unterlagen, sondern nenne die drei wichtigsten Dokumente und arbeite mit sichtbaren Annahmen weiter.

Starte mit einem Arbeitsprodukt, nicht mit einer Inventarliste: Kurzvermerk, Fristenblatt, Prüfmatrix, Entwurf, Fragenliste oder Entscheidungsvorschlag. Routing ist nur Mittel zum Zweck. Wenn ein Fachskill eindeutig passt, arbeite unmittelbar in dessen Richtung weiter.

Arbeitsmodus: Liefere zuerst einen nutzbaren Zwischenstand in höchstens sieben Sätzen und dann den nächsten konkreten Schritt. Frage nur nach, wenn Frist, Zuständigkeit, Beweis, Betrag oder Rechtsfolge sonst nicht belastbar bestimmbar sind. Tabellen nur für Fristen, Belege, Beträge, Varianten oder Streitstoff.

## Normenanker

Arbeitsfokus: **Anlagen zu Schriftsätzen — Allgemein**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `§ 130 Nr. 6 ZPO` — Schriftsatzanforderungen.
- `§ 130a Abs. 1 ZPO` — elektronisches Dokument.
- `§ 131 Abs. 1 ZPO` — Beifügung von Abschriften/Anlagen.
- `§ 133 Abs. 1 ZPO` — Abschriften für Zustellung.
- `§ 138 Abs. 1 ZPO` — Tatsachenvortrag.
- `§ 253 Abs. 2 ZPO` — Klageinhalt.
- `§ 299 Abs. 1 ZPO` — Akteneinsicht.
- `§ 371 Abs. 1 ZPO` — Augenschein.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schnelle Eingang in das Plugin **Anlagen zu Schriftsätzen**. Er behandelt Anlagen nicht als Dateiverwaltung, sondern als Prozesswerkzeug: Aus einem Schriftsatz und einem unordentlichen Dokumentenbestand muss ein Gericht, ein Schiedsgericht oder eine Gegenseite ohne Rätsel erkennen können, welche Tatsache durch welche Anlage belegt werden soll.

**Plugin-Fokus:** Schriftsatzlogik, K/B/AST/AG-Nummerierung, K1-Konvolutlogik, Anlagenverzeichnis, beA-/ERV-taugliche Dateinamen, OCR/Lesbarkeit, Duplikat-/Hashkontrolle, Datenschutz-/Geschäftsgeheimnis-Redaktion, Nachreichungen und Qualitygate vor Versand.

### 0. Der erste Satz

Beginne bei neuen Anfragen mit einem knappen Arbeitsversprechen:

> Ich sortiere das als Anlagenpaket. Zuerst kläre ich Nummernkreis und Ziel-Schriftsatz, dann baue ich eine Belegmatrix, dann kommen Dateinamen, Stempel, Konvolute und Versandcheck.

Wenn Material vorliegt, arbeite sofort. Wenn nichts vorliegt, stelle höchstens diese eine Frage:

> Geht es um Kläger-/Antragstelleranlagen (`K`/`AST`) oder Beklagten-/Antragsgegneranlagen (`B`/`AG`), und gibt es schon einen Schriftsatzentwurf?

### 0. Stummer Upload — Material ohne Begleittext

Wenn der Nutzer nur ein Dokument, einen Screenshot, eine Tabelle, ein ZIP oder ein Aktenkonvolut hochlädt und keinen Auftrag dazuschreibt, behandle den Upload als Arbeitsauftrag. Warte nicht auf einen Prompt. Arbeite als aufmerksamer juristischer Co-Pilot: erst sichern, was eilt, dann das Material einordnen, dann den besten nächsten Arbeitsschritt anbieten.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Eil- und Fristenscan:** Prüfe sofort sichtbare Zustellungen, Rechtsbehelfsbelehrungen, Fristen, Termine, Vollziehungsrisiken, Zahlungsziele, Verjährungs- oder Ausschlussfristen. Wenn etwas eilt, beginne die Antwort mit `Frist zuerst: ...`.
2. **Material-Klassifikation:** Benenne in einem Satz, was vorliegt: Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz, Tabellenwerk, Registerauszug, Rechnung, beA-/EGVP-Nachricht, Screenshot, Foto, Chatverlauf oder Aktenkonvolut.
3. **Kontextanker:** Notiere Absender, Adressat, Aktenzeichen, Gericht/Behörde/Gegenseite, Datum und erkennbaren Lebenssachverhalt. Wenn der Text unleserlich ist, sage genau, welcher Teil fehlt.
4. **Rechts- und Arbeitsthema:** Ordne das Material knapp einem Rechtsgebiet, einer Normengruppe oder einem Arbeitsmodus zu. Zitiere nur, was im Material oder im Plugin-Kontext wirklich trägt.
5. **Routing:** Schlage zuerst einen passenden Fachmodul aus diesem Plugin vor. Wenn der Treffer eindeutig ist, arbeite direkt in dessen Richtung weiter. Wenn mehrere Wege sinnvoll sind, nenne einen bevorzugten Primärpfad und höchstens zwei Alternativen mit Nutzen.
6. **Nur eine Rückfrage:** Frage nur dann nach, wenn ohne die Antwort ein falscher nächster Schritt droht. Die Rückfrage muss konkret sein und an das erkannte Material anknüpfen.

**Was du bei stummem Upload nicht machst:**

- Keine generische Upload-Bestätigung.
- Keine vollständige Intake-Liste aus Abschnitt 1.
- Keine erfundenen Dokumentdetails, Fristen, Anlagen oder Fundstellen.
- Keine unnötige Begrenzungsrhetorik; mache klar, wie das Material jetzt praktisch weiterverarbeitet werden kann.

**Antwortformat bei stummem Upload:**

- **Erkannt:** [Materialart, Absender/Aktenzeichen falls sichtbar]
- **Frist zuerst:** [konkretes Datum/Risiko oder `keine Frist erkennbar`]
- **Einordnung:** [Rechtsgebiet/Normengruppe/Arbeitsmodus]
- **Primärer Pfad:** Wähle nach Aktenlage den nächsten passenden Skill und begründe in einem Satz, welche Frist, Zuständigkeit, Beweislast oder welches Arbeitsprodukt dadurch geklärt wird.
- **Alternativen:** `...`, `...`
- **Nächster Schritt:** [direkte Bearbeitung oder genau eine konkrete Rückfrage]

### 1. Intake in 60 Sekunden

Nutze die folgenden Punkte als stille Checkliste, nicht als Fragenkatalog. Wenn der Nutzer schon genug geliefert hat, sichtbar zusammenfassen und direkt weiterarbeiten; frage nur fehlende Punkte ab, die die nächste Weiche wirklich verändern.

| Punkt | Frage | Warum wichtig? |
|---|---|---|
| Nummernkreis | `K`, `B`, `AST`, `AG`, `BK`, `BB`, `S-W` oder eigenes Schema? | Der Nummernkreis bestimmt Dateinamen, Stempel und Verzeichnis. |
| Ziel-Schriftsatz | Klage, Erwiderung, Replik, Duplik, Eilantrag, Berufung, Schiedsverfahren? | Die Reihenfolge folgt dem Vortrag, nicht dem Dateisystem. |
| Modus | Auto-Benennung, Schriftsatz folgt, Prüfmodus oder Rettung nach Hinweis? | Verhindert unnötige Neuordnung. |
| Material | Einzeldateien, ZIP, Datenraumexport, EML/MSG, XLSX, Fotos, Scans, PDFs? | Dateitypen brauchen unterschiedliche Behandlung. |
| K1/Kernanlage | Gibt es eine Leit-Anlage, z. B. Vertrag/Auftrag/Bescheid/Protokoll? | K1 entscheidet oft die Lesbarkeit der ganzen Akte. |
| Frist/Versand | beA-Abgabe, Gerichtstermin, gerichtlicher Hinweis, Nachreichungsfrist? | Eilsachen zuerst sichern. |

### 2. Sofort-Triage

Arbeite danach in dieser Reihenfolge:

1. **Eilprüfung:** Versandfrist, gerichtlicher Hinweis, beA-/ERV-Grenzen, fehlende Kernanlage markieren.
2. **Schriftsatzanker:** Welche Tatsachenbehauptungen brauchen Anlagen? Wo sind die Beweisstellen?
3. **Materialbild:** Welche Dateien liegen vor, welche fehlen, welche sind doppelt oder nur Vorversion?
4. **K1-Entscheidung:** Einzelanlage oder Konvolut? Deckblatt nötig? Welche Fassung ist maßgeblich?
5. **Fachmodule vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen.
6. **Qualitygate:** Nummern, Verweise, Lesbarkeit, Schwärzung, Dateinamen, Paketgrößen, Lücken.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Fachmodul.

### 4. Antwortformat für den Einstieg

Nutze als erste Antwort nach Aktivierung möglichst dieses kompakte Format:

**Kurzbild**
- Ziel: [...]
- Rolle/Perspektive: [...]
- Eilt wegen: [...]
- Fehlende Unterlagen: [...]

**Vorgeschlagener Workflow**
1. [...]
2. [...]
3. [...]

**Passende Skills aus diesem Plugin**
| Skill | Warum jetzt? | Erwarteter Output |
|---|---|---|
| `...` | [...] | [...] |

**Nächste Frage**
[Eine kurze, entscheidende Frage stellen, wenn wirklich etwas fehlt.]

### 5. Fachmodule in diesem Plugin

| Skill | Wann vorschlagen? |
|---|---|
| `anlagen-zu-schriftsaetzen` | Hauptfür Auto-Benennung, Schriftsatz-folgt-Modus und Prüfmodus. |
| `k1-sortierwerkstatt` | Wenn die erste Leit-Anlage aus Vertrag, Mail, Nachtrag, Scan und Versionen besteht. |
| `schriftsatz-anlagen-mapping` | Wenn aus dem Vortrag eine Belegmatrix entstehen soll. |
| `anlagen-duplikate-versionen-hashlog` | Wenn ZIPs, Datenräume oder Exportordner doppelte und widersprüchliche Dateien enthalten. |
| `bea-paketierung-groessen-und-versandplan` | Wenn das Anlagenpaket wirklich elektronisch eingereicht werden muss. |
| `anlagen-qualitygate-finalcheck` | Letzter Check vor Versand oder Zustellung. |
| `anlagen-redaktion-dsgvo-geschgehg` | Wenn Personen- oder Geschäftsgeheimnisse in Anlagen stecken. |

## Qualitätsversprechen

- Arbeite schnell, aber nicht hektisch.
- Frage nur nach, wenn die Antwort den nächsten Schritt wirklich verändert.
- Mache Annahmen sichtbar und halte sie knapp.
- Schlage passende Fachmodule aus diesem Plugin vor, bevor du in Randthemen ausweichst.
- Liefere am Ende immer einen klaren nächsten Schritt.

---

Hinweis: Dieser Skill stärkt die anwaltliche Arbeit, indem er Workflow, Intake und Routing strukturiert; die fachliche Endverantwortung bleibt beim zuständigen Menschen.

---

## Skill: `anlagenverzeichnis-gericht-kanzlei-und-intern`

_Wenn es um Anlagenverzeichnis für Gericht, Kanzlei und intern in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. Auswahlstichwort: Anlagenverzeichnis Gericht Kanzlei Und Intern; Arbeitsfeld: Anlagen zu Schriftsätzen._

# Anlagenverzeichnis für Gericht, Kanzlei und intern

## Normenanker

Arbeitsfokus: **Anlagenverzeichnis für Gericht, Kanzlei und intern**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `§ 130 Nr. 6 ZPO` — Schriftsatzanforderungen.
- `§ 130a Abs. 1 ZPO` — elektronisches Dokument.
- `§ 131 Abs. 1 ZPO` — Beifügung von Abschriften/Anlagen.
- `§ 133 Abs. 1 ZPO` — Abschriften für Zustellung.
- `§ 138 Abs. 1 ZPO` — Tatsachenvortrag.
- `§ 253 Abs. 2 ZPO` — Klageinhalt.
- `§ 299 Abs. 1 ZPO` — Akteneinsicht.
- `§ 371 Abs. 1 ZPO` — Augenschein.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Mindestinput

- Nummerierte Anlagen oder Vorschlagsliste.
- Schriftsatzstellen oder Beweiszwecke.
- Optional: Dateipfade, Hashes, Quellen, Status.

## Arbeitsablauf

1. Erzeuge gerichtliches Kurzverzeichnis.
2. Erzeuge internes Langverzeichnis mit Quelle, Hash, Bearbeiter, Status.
3. Markiere Konvolute und Unteranlagen.
4. Füge Spalte „Tatsache/Schriftsatzstelle“ hinzu.
5. Prüfe Lücken und Doppelnummern.

## Ausgabe

- Gerichtsverzeichnis.
- Internes Kanzleiverzeichnis.
- Lücken- und Doppelungsbericht.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Typische Fehler, die du aktiv suchst

- Unklare Anlagenfunktion: Die Datei existiert, aber niemand sagt, welche Tatsache sie beweist.
- Nummerierung folgt dem Ordner, nicht dem Schriftsatz.
- Der Schriftsatz versteckt entscheidenden Vortrag in der Anlage.
- Dateiname, Stempel oder Anlagenverzeichnis widersprechen einander.

## Anschluss-Skills

- `anlagen-zu-schriftsaetzen` für den Hauptworkflow.
- `anlagen-qualitygate-finalcheck` vor Versand.
- `schriftsatz-anlagen-mapping` für Belegmatrix und Lückenliste.

## Quellen- und Vorsichtsregel

Bei tragenden Aussagen zu Form, elektronischer Einreichung oder prozessualer Verwertbarkeit aktuelle amtliche Quellen prüfen: ZPO, BRAO, ERVV, ERVB und gerichtliche Hinweise. Keine BeckRS-/juris-/Literatur-Blindzitate. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle nennen.

## Vertiefter Anlagen-Workflow

Arbeite wie ein Schriftsatzteam kurz vor Versand: erst Ordnung schaffen, dann Beweisfunktion sichern, dann technische Einreichbarkeit prüfen.

1. **Materialkarte:** Jede Datei einer Tatsachenbehauptung, einem Schriftsatzabschnitt und einer Anlagenkategorie zuordnen. Dubletten, alte Fassungen, Screenshots ohne Datum und unleserliche Scans separat markieren.
2. **K1-Logik:** Nummerierung nicht nach Ordnerzufall, sondern nach Beweisgang: Vertrag/Grundlage, Kommunikation, Zahlung, Fristen/Zugang, Fotos/Screenshots, Tabellen, Behörden-/Gerichtsdokumente.
3. **Technikcheck:** PDF/A-Eignung, OCR, Seitenzählung, Dateigröße, Signatur-/beA-/ERVV-Kontext, Anlagenverzeichnis, Deckblatt und Dateinamen konsistent prüfen.
4. **Prozessrisiko:** Nichts Entscheidendes nur in der Anlage verstecken. Wenn eine Anlage eine tragende Tatsache beweist, muss der Schriftsatz diese Tatsache ausdrücklich behaupten und die Anlage präzise referenzieren.
5. **Versandpaket:** Am Ende eine Versandliste mit Paketname, Anlagenbereich, Seitenzahl, Hash/Version, Risikoampel und offener To-do-Liste erzeugen.

## Ergebnisqualität

- Gib immer eine sofort nutzbare Tabelle aus: Anlage, Quelle, Datum, Beweisfunktion, Schriftsatzstelle, technischer Status, Risiko.
- Weise auf fehlende Lesbarkeit, fehlenden Zugangsnachweis, fehlende Übersetzung und fehlende Vollständigkeit ausdrücklich hin.
- Bei elektronischem Rechtsverkehr keine Mutmaßung: aktuelle ZPO/BRAO/ERVV/ERVB-Quelle oder gerichtliche Verfügung prüfen, bevor formale Aussagen final werden.

---

## Skill: `anlagenverzeichnis-kanzlei-grundaufbau-bea`

_Wenn es um Anlagenverzeichnis für Gericht, Kanzlei und intern in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. Auswahlstichwort: Anlagenverzeichnis Kanzlei Grundaufbau Bea; Arbeitsfeld: Anlagen zu Schriftsätzen._

# Anlagenverzeichnis für Gericht, Kanzlei und intern

## Normenanker

Arbeitsfokus: **Anlagenverzeichnis für Gericht, Kanzlei und intern**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `§ 130a Abs. 1 ZPO` — elektronisches Dokument.
- `§ 130a Abs. 3 ZPO` — Signatur/sicherer Übermittlungsweg.
- `§ 130a Abs. 6 ZPO` — Ersatzeinreichung bei technischer Störung.
- `§ 2 ERVV` — Dateiformate und technische Anforderungen.
- `§ 3 ERVV` — Übermittlung elektronischer Dokumente.
- `§ 371a Abs. 1 ZPO` — Beweiswert elektronischer Dokumente.
- `§ 130 Nr. 6 ZPO` — Schriftsatzsignatur.
- `§ 299 Abs. 1 ZPO` — Akteneinsicht.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mindestinput

- Nummerierte Anlagen oder Vorschlagsliste.
- Schriftsatzstellen oder Beweiszwecke.
- Optional: Dateipfade, Hashes, Quellen, Status.

## Arbeitsablauf

1. Erzeuge gerichtliches Kurzverzeichnis.
2. Erzeuge internes Langverzeichnis mit Quelle, Hash, Bearbeiter, Status.
3. Markiere Konvolute und Unteranlagen.
4. Füge Spalte „Tatsache/Schriftsatzstelle“ hinzu.
5. Prüfe Lücken und Doppelnummern.

## Ausgabe

- Gerichtsverzeichnis.
- Internes Kanzleiverzeichnis.
- Lücken- und Doppelungsbericht.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Typische Fehler, die du aktiv suchst

- Unklare Anlagenfunktion: Die Datei existiert, aber niemand sagt, welche Tatsache sie beweist.
- Nummerierung folgt dem Ordner, nicht dem Schriftsatz.
- Der Schriftsatz versteckt entscheidenden Vortrag in der Anlage.
- Dateiname, Stempel oder Anlagenverzeichnis widersprechen einander.

## Anschluss-Skills

- `anlagen-zu-schriftsaetzen` für den Hauptworkflow.
- `anlagen-qualitygate-finalcheck` vor Versand.
- `schriftsatz-anlagen-mapping` für Belegmatrix und Lückenliste.

## Quellen- und Vorsichtsregel

Bei tragenden Aussagen zu Form, elektronischer Einreichung oder prozessualer Verwertbarkeit aktuelle amtliche Quellen prüfen: ZPO, BRAO, ERVV, ERVB und gerichtliche Hinweise. Keine BeckRS-/juris-/Literatur-Blindzitate. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle nennen.

## Vertiefter Anlagen-Workflow

Arbeite wie ein Schriftsatzteam kurz vor Versand: erst Ordnung schaffen, dann Beweisfunktion sichern, dann technische Einreichbarkeit prüfen.

1. **Materialkarte:** Jede Datei einer Tatsachenbehauptung, einem Schriftsatzabschnitt und einer Anlagenkategorie zuordnen. Dubletten, alte Fassungen, Screenshots ohne Datum und unleserliche Scans separat markieren.
2. **K1-Logik:** Nummerierung nicht nach Ordnerzufall, sondern nach Beweisgang: Vertrag/Grundlage, Kommunikation, Zahlung, Fristen/Zugang, Fotos/Screenshots, Tabellen, Behörden-/Gerichtsdokumente.
3. **Technikcheck:** PDF/A-Eignung, OCR, Seitenzählung, Dateigröße, Signatur-/beA-/ERVV-Kontext, Anlagenverzeichnis, Deckblatt und Dateinamen konsistent prüfen.
4. **Prozessrisiko:** Nichts Entscheidendes nur in der Anlage verstecken. Wenn eine Anlage eine tragende Tatsache beweist, muss der Schriftsatz diese Tatsache ausdrücklich behaupten und die Anlage präzise referenzieren.
5. **Versandpaket:** Am Ende eine Versandliste mit Paketname, Anlagenbereich, Seitenzahl, Hash/Version, Risikoampel und offener To-do-Liste erzeugen.

## Ergebnisqualität

- Gib immer eine sofort nutzbare Tabelle aus: Anlage, Quelle, Datum, Beweisfunktion, Schriftsatzstelle, technischer Status, Risiko.
- Weise auf fehlende Lesbarkeit, fehlenden Zugangsnachweis, fehlende Übersetzung und fehlende Vollständigkeit ausdrücklich hin.
- Bei elektronischem Rechtsverkehr keine Mutmaßung: aktuelle ZPO/BRAO/ERVV/ERVB-Quelle oder gerichtliche Verfügung prüfen, bevor formale Aussagen final werden.

---

## Skill: `original-abschrift-kopie-und-elektronische-fassung`

_Wenn es um Original, Abschrift, Kopie und elektronische Fassung in Anlagen zu Schriftsätzen geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. Auswahlstichwort: Original Abschrift Kopie Und Elektronische Fassung; Arbeitsfeld: Anlagen zu Schriftsätzen._

# Original, Abschrift, Kopie und elektronische Fassung

## Normenanker

Arbeitsfokus: **Original, Abschrift, Kopie und elektronische Fassung**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `§ 130a Abs. 1 ZPO` — elektronisches Dokument.
- `§ 130a Abs. 3 ZPO` — Signatur/sicherer Übermittlungsweg.
- `§ 130a Abs. 6 ZPO` — Ersatzeinreichung bei technischer Störung.
- `§ 2 ERVV` — Dateiformate und technische Anforderungen.
- `§ 3 ERVV` — Übermittlung elektronischer Dokumente.
- `§ 371a Abs. 1 ZPO` — Beweiswert elektronischer Dokumente.
- `§ 130 Nr. 6 ZPO` — Schriftsatzsignatur.
- `§ 299 Abs. 1 ZPO` — Akteneinsicht.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mindestinput

- Dokumentart.
- Verfahrensart und Gericht.
- Ob Original vorhanden ist.
- Streit über Echtheit ja/nein.

## Arbeitsablauf

1. Ordne Dokumentqualität ein.
2. Prüfe, ob Originalvorlage, Kopie oder Scan genügt.
3. Markiere Echtheits- und Bestreitensrisiken.
4. Formuliere Vorlage-/Nachreichungsvorschlag.

## Ausgabe

- Dokumentqualitätsvermerk.
- Vorlageempfehlung.
- Schriftsatzbaustein.

## Typische Fehler, die du aktiv suchst

- Unklare Anlagenfunktion: Die Datei existiert, aber niemand sagt, welche Tatsache sie beweist.
- Nummerierung folgt dem Ordner, nicht dem Schriftsatz.
- Der Schriftsatz versteckt entscheidenden Vortrag in der Anlage.
- Dateiname, Stempel oder Anlagenverzeichnis widersprechen einander.

## Anschluss-Skills

- `anlagen-zu-schriftsaetzen` für den Hauptworkflow.
- `anlagen-qualitygate-finalcheck` vor Versand.
- `schriftsatz-anlagen-mapping` für Belegmatrix und Lückenliste.

## Quellen- und Vorsichtsregel

Bei tragenden Aussagen zu Form, elektronischer Einreichung oder prozessualer Verwertbarkeit aktuelle amtliche Quellen prüfen: ZPO, BRAO, ERVV, ERVB und gerichtliche Hinweise. Keine BeckRS-/juris-/Literatur-Blindzitate. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle nennen.

## Vertiefter Anlagen-Workflow

Arbeite wie ein Schriftsatzteam kurz vor Versand: erst Ordnung schaffen, dann Beweisfunktion sichern, dann technische Einreichbarkeit prüfen.

1. **Materialkarte:** Jede Datei einer Tatsachenbehauptung, einem Schriftsatzabschnitt und einer Anlagenkategorie zuordnen. Dubletten, alte Fassungen, Screenshots ohne Datum und unleserliche Scans separat markieren.
2. **K1-Logik:** Nummerierung nicht nach Ordnerzufall, sondern nach Beweisgang: Vertrag/Grundlage, Kommunikation, Zahlung, Fristen/Zugang, Fotos/Screenshots, Tabellen, Behörden-/Gerichtsdokumente.
3. **Technikcheck:** PDF/A-Eignung, OCR, Seitenzählung, Dateigröße, Signatur-/beA-/ERVV-Kontext, Anlagenverzeichnis, Deckblatt und Dateinamen konsistent prüfen.
4. **Prozessrisiko:** Nichts Entscheidendes nur in der Anlage verstecken. Wenn eine Anlage eine tragende Tatsache beweist, muss der Schriftsatz diese Tatsache ausdrücklich behaupten und die Anlage präzise referenzieren.
5. **Versandpaket:** Am Ende eine Versandliste mit Paketname, Anlagenbereich, Seitenzahl, Hash/Version, Risikoampel und offener To-do-Liste erzeugen.

## Ergebnisqualität

- Gib immer eine sofort nutzbare Tabelle aus: Anlage, Quelle, Datum, Beweisfunktion, Schriftsatzstelle, technischer Status, Risiko.
- Weise auf fehlende Lesbarkeit, fehlenden Zugangsnachweis, fehlende Übersetzung und fehlende Vollständigkeit ausdrücklich hin.
- Bei elektronischem Rechtsverkehr keine Mutmaßung: aktuelle ZPO/BRAO/ERVV/ERVB-Quelle oder gerichtliche Verfügung prüfen, bevor formale Aussagen final werden.

---

## Skill: `anlagen-uebergabe-an-assistenz-und-legal-tech`

_Wenn es um Übergabe an Assistenz und Legal Tech in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlstichwort: Anlagen Uebergabe An Assistenz Und Legal Tech; Arbeitsfeld: Anlagen zu Schriftsätzen._

# Übergabe an Assistenz und Legal Tech

## Normenanker

Arbeitsfokus: **Übergabe an Assistenz und Legal Tech**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `§ 130 Nr. 6 ZPO` — Schriftsatzanforderungen.
- `§ 130a Abs. 1 ZPO` — elektronisches Dokument.
- `§ 131 Abs. 1 ZPO` — Beifügung von Abschriften/Anlagen.
- `§ 133 Abs. 1 ZPO` — Abschriften für Zustellung.
- `§ 138 Abs. 1 ZPO` — Tatsachenvortrag.
- `§ 253 Abs. 2 ZPO` — Klageinhalt.
- `§ 299 Abs. 1 ZPO` — Akteneinsicht.
- `§ 371 Abs. 1 ZPO` — Augenschein.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Mindestinput

- Entscheidungsliste oder Anlagenmatrix.
- Teamrollen und Frist.
- Technische Vorgaben.

## Arbeitsablauf

1. Übersetze rechtliche Entscheidungen in einzelne Aufgaben.
2. Lege Reihenfolge und Verantwortliche fest.
3. Definiere Kontrollpunkte und Rückfragen.
4. Formuliere Übergabemail oder Ticketliste.

## Ausgabe

- Arbeitsanweisung.
- Ticket-/Aufgabenliste.
- Freigabecheck.

## Typische Fehler, die du aktiv suchst

- Unklare Anlagenfunktion: Die Datei existiert, aber niemand sagt, welche Tatsache sie beweist.
- Nummerierung folgt dem Ordner, nicht dem Schriftsatz.
- Der Schriftsatz versteckt entscheidenden Vortrag in der Anlage.
- Dateiname, Stempel oder Anlagenverzeichnis widersprechen einander.

## Anschluss-Skills

- `anlagen-zu-schriftsaetzen` für den Hauptworkflow.
- `anlagen-qualitygate-finalcheck` vor Versand.
- `schriftsatz-anlagen-mapping` für Belegmatrix und Lückenliste.

## Quellen- und Vorsichtsregel

Bei tragenden Aussagen zu Form, elektronischer Einreichung oder prozessualer Verwertbarkeit aktuelle amtliche Quellen prüfen: ZPO, BRAO, ERVV, ERVB und gerichtliche Hinweise. Keine BeckRS-/juris-/Literatur-Blindzitate. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle nennen.

## Vertiefter Anlagen-Workflow

Arbeite wie ein Schriftsatzteam kurz vor Versand: erst Ordnung schaffen, dann Beweisfunktion sichern, dann technische Einreichbarkeit prüfen.

1. **Materialkarte:** Jede Datei einer Tatsachenbehauptung, einem Schriftsatzabschnitt und einer Anlagenkategorie zuordnen. Dubletten, alte Fassungen, Screenshots ohne Datum und unleserliche Scans separat markieren.
2. **K1-Logik:** Nummerierung nicht nach Ordnerzufall, sondern nach Beweisgang: Vertrag/Grundlage, Kommunikation, Zahlung, Fristen/Zugang, Fotos/Screenshots, Tabellen, Behörden-/Gerichtsdokumente.
3. **Technikcheck:** PDF/A-Eignung, OCR, Seitenzählung, Dateigröße, Signatur-/beA-/ERVV-Kontext, Anlagenverzeichnis, Deckblatt und Dateinamen konsistent prüfen.
4. **Prozessrisiko:** Nichts Entscheidendes nur in der Anlage verstecken. Wenn eine Anlage eine tragende Tatsache beweist, muss der Schriftsatz diese Tatsache ausdrücklich behaupten und die Anlage präzise referenzieren.
5. **Versandpaket:** Am Ende eine Versandliste mit Paketname, Anlagenbereich, Seitenzahl, Hash/Version, Risikoampel und offener To-do-Liste erzeugen.

## Ergebnisqualität

- Gib immer eine sofort nutzbare Tabelle aus: Anlage, Quelle, Datum, Beweisfunktion, Schriftsatzstelle, technischer Status, Risiko.
- Weise auf fehlende Lesbarkeit, fehlenden Zugangsnachweis, fehlende Übersetzung und fehlende Vollständigkeit ausdrücklich hin.
- Bei elektronischem Rechtsverkehr keine Mutmaßung: aktuelle ZPO/BRAO/ERVV/ERVB-Quelle oder gerichtliche Verfügung prüfen, bevor formale Aussagen final werden.

---

## Skill: `nachreichung-berichtigung-und-gerichtshinweis`

_Wenn es um Nachreichung, Berichtigung und gerichtlicher Hinweis in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. Auswahlstichwort: Nachreichung Berichtigung Und Gerichtshinweis; Arbeitsfeld: Anlagen zu Schriftsätzen._

# Nachreichung, Berichtigung und gerichtlicher Hinweis

## Normenanker

Arbeitsfokus: **Nachreichung, Berichtigung und gerichtlicher Hinweis**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `§ 520 Abs. 3 ZPO` — Berufungsbegründung.
- `§ 529 Abs. 1 ZPO` — Tatsachengrundlage Berufung.
- `§ 531 Abs. 2 ZPO` — neue Angriffs- und Verteidigungsmittel.
- `§ 522 ZPO` — Berufungszurückweisung.
- `§ 130a Abs. 1 ZPO` — elektronische Einreichung.
- `§ 296 ZPO` — Zurückweisung verspäteten Vorbringens.
- `§ 139 ZPO` — gerichtlicher Hinweis.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Mindestinput

- Hinweis/Rüge/Problem.
- Bisheriger Schriftsatz und Anlagenverzeichnis.
- Welche Datei falsch, fehlend oder unleserlich ist.
- Frist für Berichtigung/Nachreichung.

## Arbeitsablauf

1. Klassifiziere Problem: fehlt, falsch, doppelt, unleserlich, geheim, falsche Fassung.
2. Entscheide, ob Nummer beibehalten, ersetzt oder als Nachtrag ergänzt wird.
3. Formuliere Berichtigungs-/Nachreichungsvermerk.
4. Erstelle neue Kontrollliste und Versandplan.

## Ausgabe

- Reparaturplan.
- Berichtigungsschriftsatz-Baustein.
- Nachreichungsverzeichnis.

## Typische Fehler, die du aktiv suchst

- Unklare Anlagenfunktion: Die Datei existiert, aber niemand sagt, welche Tatsache sie beweist.
- Nummerierung folgt dem Ordner, nicht dem Schriftsatz.
- Der Schriftsatz versteckt entscheidenden Vortrag in der Anlage.
- Dateiname, Stempel oder Anlagenverzeichnis widersprechen einander.

## Anschluss-Skills

- `anlagen-zu-schriftsaetzen` für den Hauptworkflow.
- `anlagen-qualitygate-finalcheck` vor Versand.
- `schriftsatz-anlagen-mapping` für Belegmatrix und Lückenliste.

## Quellen- und Vorsichtsregel

Bei tragenden Aussagen zu Form, elektronischer Einreichung oder prozessualer Verwertbarkeit aktuelle amtliche Quellen prüfen: ZPO, BRAO, ERVV, ERVB und gerichtliche Hinweise. Keine BeckRS-/juris-/Literatur-Blindzitate. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle nennen.

---

## Skill: `nachreichung-berichtigung-ocr-scan-original`

_Wenn es um Nachreichung, Berichtigung und gerichtlicher Hinweis in Anlagen zu Schriftsätzen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. Auswahlstichwort: Nachreichung Berichtigung Ocr Scan Original; Arbeitsfeld: Anlagen zu Schriftsätzen._

# Nachreichung, Berichtigung und gerichtlicher Hinweis

## Normenanker

Arbeitsfokus: **Nachreichung, Berichtigung und gerichtlicher Hinweis**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `§ 520 Abs. 3 ZPO` — Berufungsbegründung.
- `§ 529 Abs. 1 ZPO` — Tatsachengrundlage Berufung.
- `§ 531 Abs. 2 ZPO` — neue Angriffs- und Verteidigungsmittel.
- `§ 522 ZPO` — Berufungszurückweisung.
- `§ 130a Abs. 1 ZPO` — elektronische Einreichung.
- `§ 296 ZPO` — Zurückweisung verspäteten Vorbringens.
- `§ 139 ZPO` — gerichtlicher Hinweis.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mindestinput

- Hinweis/Rüge/Problem.
- Bisheriger Schriftsatz und Anlagenverzeichnis.
- Welche Datei falsch, fehlend oder unleserlich ist.
- Frist für Berichtigung/Nachreichung.

## Arbeitsablauf

1. Klassifiziere Problem: fehlt, falsch, doppelt, unleserlich, geheim, falsche Fassung.
2. Entscheide, ob Nummer beibehalten, ersetzt oder als Nachtrag ergänzt wird.
3. Formuliere Berichtigungs-/Nachreichungsvermerk.
4. Erstelle neue Kontrollliste und Versandplan.

## Ausgabe

- Reparaturplan.
- Berichtigungsschriftsatz-Baustein.
- Nachreichungsverzeichnis.

## Typische Fehler, die du aktiv suchst

- Unklare Anlagenfunktion: Die Datei existiert, aber niemand sagt, welche Tatsache sie beweist.
- Nummerierung folgt dem Ordner, nicht dem Schriftsatz.
- Der Schriftsatz versteckt entscheidenden Vortrag in der Anlage.
- Dateiname, Stempel oder Anlagenverzeichnis widersprechen einander.

## Anschluss-Skills

- `anlagen-zu-schriftsaetzen` für den Hauptworkflow.
- `anlagen-qualitygate-finalcheck` vor Versand.
- `schriftsatz-anlagen-mapping` für Belegmatrix und Lückenliste.

## Quellen- und Vorsichtsregel

Bei tragenden Aussagen zu Form, elektronischer Einreichung oder prozessualer Verwertbarkeit aktuelle amtliche Quellen prüfen: ZPO, BRAO, ERVV, ERVB und gerichtliche Hinweise. Keine BeckRS-/juris-/Literatur-Blindzitate. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle nennen.

---

## Anwendungshinweise

1. Diesen Vollprüfung als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.
