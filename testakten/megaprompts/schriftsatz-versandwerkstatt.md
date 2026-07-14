# Vollprüfung: schriftsatz-versandwerkstatt

## Zusammensetzung

Diese Vollprüfung enthält alle 9 Skills des Plugins `schriftsatz-versandwerkstatt`.

## Inhaltsverzeichnis

1. **versandmappe-endfertigen** — Orchestriert die vollständige Endfertigung eines bereits geschriebenen Schriftsatzes mit gemischten Anlagen: liest den A…
2. **signaturweg-und-absender-pruefen** — Klärt vor der Freigabe die verantwortende Person, den tatsächlichen Versender, das verwendete sichere Postfach und die v…
3. **anlagen-konvertieren-und-sichtpruefen** — Konvertiert bereits ausgewählte Anlagen aus Office-, Tabellen-, Bild-, E-Mail-, Text- und Webformaten in getrennte PDFs,…
4. **stoerung-und-nachreichung-dokumentieren** — Erstellt bei technischer Übermittlungsstörung, ungeeignetem elektronischem Dokument oder gerichtlichem Nachreichungshinw…
5. **versandfreigabe-und-eingang-sichern** — Führt die letzte technische und organisatorische Freigabe der Versandmappe durch: öffnet jede Enddatei, gleicht Empfänge…
6. **dateinamen-und-paketgrenzen-pruefen** — Vergibt robuste, sprechende beA-Dateinamen mit ASCII, Unterstrichen, logischer Reihenfolge und höchstens 80 Zeichen eins…
7. **ordneraufnahme-und-produktionsmatrix** — Liest einen vorhandenen Schriftsatz- und Anlagenordner vor jeder Rückfrage, erkennt Hauptdokument, Fassungen, bereits ve…
8. **hauptdokument-pdf-endfertigen** — Endfertigt den bereits freigegebenen Schriftsatz technisch als separates PDF: sichert die maßgebliche Quelldatei, konver…
9. **anlagen-nummerieren-und-stempeln** — Führt den vorhandenen Anlagenkreis K, B, AST oder AG ohne Kollision fort, gleicht jede Kennung mit Schriftsatz und Anlag…

---

## Skill: `versandmappe-endfertigen`

_Orchestriert die vollständige Endfertigung eines bereits geschriebenen Schriftsatzes mit gemischten Anlagen: liest den Arbeitsordner zuerst, erzeugt eine Produktionsmatrix, konvertiert Quellen kontrolliert in PDF, stempelt und benennt Anlagen, prüft ERVB-Grenzen, Absender und Signaturroute und liefert Versandordner, Manifest, Freigabevermerk und Eingangskontrolle, ohne selbst zu versenden._

# Versandmappe endfertigen

## 1. Einsatz

Nutze diesen Skill als Standardroute, sobald der Nutzer einen fertigen oder nahezu fertigen Schriftsatz und einen Ordner mit Anlagen für die elektronische Gerichtseinreichung vorbereitet haben will. Nutze ihn auch bei Formulierungen wie „mach versandfertig“, „alles liegt im Ordner“, „PDF-Paket“, „Anlagen stempeln“ oder „beA-Mappe“.

Keine inhaltliche Rechtsprüfung eröffnen. Keine Rechtsprechung recherchieren. Den Schriftsatz nicht neu schreiben, solange der Nutzer das nicht ausdrücklich verlangt.

## 2. Direktstart

Wenn ein Ordner oder Dateien vorliegen, beginne ohne Interview:

1. Dateien rekursiv inventarisieren, ohne Originale zu verändern.
2. wahrscheinlichstes Hauptdokument nach Dateiname, Änderungsdatum und Inhalt erkennen.
3. Anlagenkennungen aus Schriftsatz und Dateinamen abgleichen.
4. sofort eine Produktionsmatrix mit Status `bereit`, `prüfen`, `fehlt` oder `stop` ausgeben.
5. nur Angaben nachfragen, die sich nicht aus dem Material ergeben und den nächsten Schritt sperren.

Blockierende Angaben sind Empfängergericht, Aktenzeichen oder Neueingang, Frist, gewünschter Nummernkreis, verantwortender Anwalt, tatsächlicher Versender und Signaturroute. Fasse offene Punkte in höchstens zwei Fragen zusammen.

## 3. Produktionslauf

1. `ordneraufnahme-und-produktionsmatrix` für Inventar, Fassungen und Konflikte.
2. `hauptdokument-pdf-endfertigen` für die unveränderte finale Schriftsatz-PDF.
3. `anlagen-konvertieren-und-sichtpruefen` für Office, Tabellen, Bilder, E-Mail und Textformate.
4. `anlagen-nummerieren-und-stempeln` für K, B, AST oder AG und den Stempel auf jeder Seite.
5. `dateinamen-und-paketgrenzen-pruefen` für ASCII-Namen, 80-Zeichen-Profil und Paketierung.
6. `signaturweg-und-absender-pruefen` für verantwortende Person, Versender und Formroute.
7. `versandfreigabe-und-eingang-sichern` für Schlusskontrolle und Eingangsnachweis.
8. Nur bei technischer Störung oder gerichtlichem Formhinweis `stoerung-und-nachreichung-dokumentieren` zuschalten.

Arbeite die Schritte in einem Durchgang ab. Wiederhole keine bereits aus Dateien beantwortete Frage.

## 4. Produktionsmatrix

| Position | Quelle | Zielformat | Anlagenkennung | Seiten | Sichtkontrolle | Versandname | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Hauptdokument | Datei und Fassung | PDF | keine | Zahl | offen oder geprüft | `00_...pdf` | Status |
| Anlage | Datei | PDF | K/B/AST/AG | Zahl | offen oder geprüft | `01_...pdf` | Status |

Kennzeichne jede automatische Konvertierung bis zur Sichtkontrolle als `prüfen`. Aus Dateierweiterung oder erfolgreichem Programmende folgt noch keine inhaltlich richtige Wiedergabe.

## 5. Werkzeuglauf

Nutze nach Sichtung das mitgelieferte Werkzeug `werkzeuge/build_versandmappe.py`. Verwende `--strict`. Arbeite in einem neuen Zielordner und überschreibe niemals Originale. Übergib Signaturroute, verantwortende Person und Versender ausdrücklich.

Das Werkzeug darf nur dann als technisch erfolgreich gelten, wenn:

1. der Prozess mit Status null endet,
2. keine Stop-Befunde im Preflight stehen,
3. jede erzeugte PDF geöffnet und visuell geprüft wurde,
4. Seitenzahlen und erwartete Dokumentgrenzen stimmen,
5. die Versanddateien dem Anlagenverzeichnis entsprechen.

## 6. Ausgabe

Liefere:

```text
ausgang/
  versandfertig/
    00_..._Schriftsatz_....pdf
    01_..._AnlageK1_....pdf
  intern/
    Anlagenverzeichnis.md
    Anlagenverzeichnis.pdf
    Anlagenkonvolut_Prueffassung.pdf
    Versandmanifest.csv
    Versandmanifest.json
    Preflight-Bericht.md
    Freigabevermerk.md
    Eingangskontrolle.md
```

`intern/` wird nicht versandt, sofern sein Inhalt nicht ausdrücklich eingereicht werden soll.

## 7. Stop-Regeln

Stoppe die Freigabe bei unklarem Empfänger, offener Frist, nicht finalem Hauptdokument, unlesbarer oder verschlüsselter PDF, fehlender Anlage, Nummernkollision, ungeklärtem Versender, ungeklärter Signaturroute, fehlender Sichtkontrolle oder überschrittener Paketgrenze. Liefere dann die bereits erzeugbaren Dateien plus eine kurze, priorisierte Stop-Liste. Löse niemals selbst einen Versand aus.

---

## Skill: `signaturweg-und-absender-pruefen`

_Klärt vor der Freigabe die verantwortende Person, den tatsächlichen Versender, das verwendete sichere Postfach und die verfahrensbezogene Formroute; unterscheidet persönlichen sicheren Versand mit einfacher Signatur von der qualifizierten elektronischen Signatur, prüft die Namenszeile im Hauptdokument und stoppt bei fremdem Postfach, Mitarbeiter-Versand oder ungeklärter Verantwortung._

# Signaturweg und Absender prüfen

## 1. Pflichtangaben

Ermittle aus Schriftsatz und Auftrag:

1. verantwortender Anwalt,
2. Name in der einfachen Signatur am Dokumentende,
3. tatsächlicher Versender,
4. verwendetes persönlich zugeordnetes Postfach,
5. einschlägige Verfahrensordnung,
6. gewählte Route `persönlich-sicher` oder `qualifizierte elektronische Signatur`.

Frage diese Punkte nur nach, soweit sie nicht bereits eindeutig vorliegen. Fasse die Frage zusammen: `Verantwortet und versendet [Name] persönlich aus seinem zugeordneten Postfach, oder wird das Dokument vor Versand qualifiziert elektronisch signiert?`

## 2. Formroute

ZPO Paragraf 130a Absatz 3 verlangt für das Hauptdokument entweder:

1. qualifizierte elektronische Signatur der verantwortenden Person oder
2. Signatur durch die verantwortende Person und Einreichung auf einem sicheren Übermittlungsweg.

Anlagen benötigen danach keine eigene Signatur. Wähle bei Arbeits-, Sozial-, Verwaltungs-, Finanz- oder Strafverfahren die entsprechende Vorschrift der Verfahrensordnung und dokumentiere sie im Freigabevermerk.

## 3. Entscheidungsmatrix

| Verantwortung und Versand | Route | Status |
| --- | --- | --- |
| dieselbe Person, eigenes sicheres Postfach, Name im Dokument | persönlich-sicher | nach Schlusskontrolle möglich |
| Mitarbeiter löst Versand aus | qualifizierte elektronische Signatur des Verantwortlichen | ohne geprüfte Signatur stop |
| anderer Anwalt versendet aus eigenem Postfach | qualifizierte elektronische Signatur des Verantwortlichen oder neue eindeutige Verantwortung | bis Klärung stop |
| Postfach, Person oder Namenszeile unklar | keine Route | stop |

## 4. Grenze

Dieser Skill bringt keine qualifizierte elektronische Signatur an und behauptet nicht, eine Signatur technisch validiert zu haben. Er dokumentiert nur die getroffene Route und den Prüfstatus. Übergib das Ergebnis an `versandfreigabe-und-eingang-sichern`.

---

## Skill: `anlagen-konvertieren-und-sichtpruefen`

_Konvertiert bereits ausgewählte Anlagen aus Office-, Tabellen-, Bild-, E-Mail-, Text- und Webformaten in getrennte PDFs, ohne Beweisinhalt zu verändern: protokolliert Quelle und Hash, erhält Absender- und Zeitangaben, meldet Anhänge und nicht unterstützte Container, vergleicht jede Ausgabeseite visuell und stoppt bei Beschnitt, fehlenden Blättern oder unlesbarer Darstellung._

# Anlagen konvertieren und sichtprüfen

## 1. Grundsatz

Eine erfolgreich erzeugte PDF ist noch keine freigegebene Anlage. Jede Konvertierung bleibt bis zum Seitenvergleich im Status `prüfen`.

## 2. Formatroute

| Quelle | Route | besondere Kontrolle |
| --- | --- | --- |
| DOC, DOCX, ODT, RTF | LibreOffice nach PDF | Kommentare, Änderungen, Kopf-/Fußzeilen, Seitenumbruch |
| XLS, XLSX, ODS | LibreOffice nach PDF | alle Tabellenblätter, Druckbereiche, Spalten, Formelergebnisse, wiederholte Kopfzeilen |
| PPT, PPTX, ODP | LibreOffice nach PDF | Folgenreihenfolge, Notizen nur bei ausdrücklichem Auftrag |
| JPG, JPEG, PNG | A4-PDF ohne Beschnitt | Orientierung, Auflösung, Farbinhalt, mehrere Bilder als getrennte Quellen |
| EML | Kopfzeilen plus Nachrichtentext | Absender, Empfänger, Datum, Betreff, Text und Hinweis auf Anhänge |
| TXT, CSV, TSV, Markdown, HTML | paginierte Textfassung | Zeichensatz, Spaltentrenner, Zeilenumbrüche, Vollständigkeit |
| PDF | technische Prüfung | Verschlüsselung, aktive Inhalte, Leerseiten, Lesbarkeit |

## 3. E-Mail

Für jede EML-Datei müssen Von, An, Cc, Datum, Betreff und Nachrichtentext sichtbar sein. Liste eingebettete Anhänge im PDF-Kopf. Anhänge werden nicht unsichtbar Teil der E-Mail-PDF; erforderliche Anhänge sind als eigene Anlagenquelle bereitzustellen.

MSG, PST, MBOX und vergleichbare Container werden nicht improvisiert ausgelesen. Verlange einen Export als EML oder überprüfbares PDF und die benötigten Anhänge separat.

## 4. Tabellen

Stoppe, wenn Spalten abgeschnitten, Formeln als Fehlerwerte dargestellt, Tabellenblätter ausgelassen oder Zahlen durch wissenschaftliche Schreibweise verändert erscheinen. Eine Tabelle darf auf Querformat oder mehrere Seiten verteilt werden, muss aber ihre Kopfzeilen und Zuordnung behalten.

## 5. Protokoll

| Anlage | Quelle | Quellhash | Konverter | Zielseiten | Sichtkontrolle | Abweichung |
| --- | --- | --- | --- | --- | --- | --- |

Keine Quelle überschreiben. Bewahre nur die Versand-PDF im Versandordner auf; Quell- und Prüfdateien bleiben intern. Übergib freigegebene PDFs an `anlagen-nummerieren-und-stempeln`.

---

## Skill: `stoerung-und-nachreichung-dokumentieren`

_Erstellt bei technischer Übermittlungsstörung, ungeeignetem elektronischem Dokument oder gerichtlichem Nachreichungshinweis eine belastbare Ereignis- und Dateichronologie: sichert Fehlermeldungen, Versandversuche, Systemstatus, Ersatzweg, Inhaltsgleichheit, korrigierte PDF, Frist und Eingangsnachweise und hält Störung, Formmangel und bloßen Bedienfehler strikt auseinander._

# Störung und Nachreichung dokumentieren

## 1. Aktivierung

Nutze diesen Skill nur, wenn eine Einreichung technisch scheitert, das Gericht ein Dokument als ungeeignet beanstandet oder eine korrigierte Fassung nachgereicht werden muss. Er ist keine vorsorgliche Standardstation.

## 2. Trennung

Unterscheide:

1. vorübergehende technische Unmöglichkeit der elektronischen Übermittlung,
2. bereits übermitteltes, aber für die Bearbeitung ungeeignetes Dokument,
3. falscher Empfänger, falsche Datei, fehlende Signatur oder sonstiger Form-/Bedienfehler.

Vermische diese Kategorien nicht. Wähle die einschlägige Vorschrift der Verfahrensordnung und lasse die rechtliche Freigabe beim verantwortenden Anwalt.

## 3. Minutenchronologie

| Zeit | Handlung | System/Postfach | Ergebnis | Beleg | nächster Schritt |
| --- | --- | --- | --- | --- | --- |

Sichere sofort Fehlermeldung, Bildschirmabzug, Exportnachricht, Systemstatus, Supportmeldung, Dateihash und Namen des Handelnden. Dokumentiere, wann die Störung erkannt, welcher Ersatzweg gewählt und wann erneut übermittelt wurde.

## 4. Nachreichung

Bei einer korrigierten PDF:

1. beanstandete Datei unverändert archivieren,
2. Ursache benennen,
3. korrigierte Datei neu erzeugen und vollständig sichtprüfen,
4. Inhaltsgleichheit oder bewusste Abweichung eindeutig erklären,
5. neuen Hash, Dateinamen und Versandzeit dokumentieren,
6. neue Eingangsbestätigung prüfen.

## 5. Ergebnis

Liefere Ereignisprotokoll, Belegliste, korrigierte Versandmatrix, Entwurf des technischen Begleitvermerks und Stop-Liste für die anwaltliche Formprüfung. Erfinde keine Störungsursache und lösche keine ursprüngliche Datei.

---

## Skill: `versandfreigabe-und-eingang-sichern`

_Führt die letzte technische und organisatorische Freigabe der Versandmappe durch: öffnet jede Enddatei, gleicht Empfänger, Aktenzeichen, Frist, Schriftsatzfassung, Anlagenfolge, Bytes, Hashes, Signaturroute und Nachrichtenteile ab, erzeugt einen unterschriftsreifen Freigabevermerk und bereitet die Prüfung und Ablage der automatisierten Eingangsbestätigung vor._

# Versandfreigabe und Eingang sichern

## 1. Vorversandkontrolle

Öffne die finalen Dateien aus `versandfertig/`, nicht die Quellen. Prüfe:

1. richtiges Gericht und richtiges Aktenzeichen oder eindeutig `Neueingang`,
2. finale Schriftsatzfassung und sichtbare einfache Signatur,
3. lückenlose Anlagenfolge und Übereinstimmung mit dem Schriftsatz,
4. jede PDF lesbar, unverschlüsselt, druckbar und ohne aktive Inhalte,
5. Dateinamen, Anzahl und Gesamtbytes,
6. verantwortende Person, tatsächlicher Versender und Signaturroute,
7. Frist mit Datum, Uhrzeit und Sicherheitsreserve,
8. bei mehreren Nachrichten Teilfolge und Anlagenbereich.

## 2. Ampel

- `rot`: Formroute, Empfänger, Frist, Hauptdokument oder Anlage offen; keine Freigabe.
- `gelb`: rein organisatorischer Punkt mit ausreichend Zeit offen; Verantwortlichen und Termin nennen.
- `grün`: technische Produktion abgeschlossen und anwaltliche Freigabe dokumentiert; Versand bleibt eine bewusste Handlung außerhalb des Werkzeugs.

## 3. Freigabevermerk

Erzeuge aus `assets/freigabevermerk.md` einen konkreten Vermerk. Keine Kästchen als erledigt markieren, wenn der Prüfschritt nicht tatsächlich erfolgt ist. Nenne Hauptdokument, Anlagenbereich, Dateien, Bytes, Hash des Hauptdokuments, Frist, Signaturroute, Verantwortlichen und Versender.

## 4. Eingangskontrolle

Bereite vor dem Versand eine Zeile je Nachricht vor:

| Teil | Empfänger | Versandzeit | Eingangszeit | Status | Dateien | Prüfender | Frist erledigt |
| --- | --- | --- | --- | --- | --- | --- | --- |

Nach Versand die automatisierte Eingangsbestätigung auf richtigen Empfänger, Zeitstempel, positiven Status und vollständige Nachricht prüfen. Speichere Exportnachricht, Eingangsbestätigung, Versanddateien und Freigabevermerk gemeinsam. Eine Frist darf erst nach positiver Prüfung erledigt werden.

## 5. Ausgabe

Liefere Freigabeampel, ausgefüllten Freigabevermerk, offene Stop-Punkte und Eingangskontrollblatt. Löse niemals selbst einen Versand aus.

---

## Skill: `dateinamen-und-paketgrenzen-pruefen`

_Vergibt robuste, sprechende beA-Dateinamen mit ASCII, Unterstrichen, logischer Reihenfolge und höchstens 80 Zeichen einschließlich Endung, prüft jede Datei gegen die ERVB-Höchstgrenze von 90 Zeichen sowie die Nachrichtengrenzen von 1.000 Dateien und 200 MB und erstellt bei Bedarf einen lückenlosen, quittierbaren Mehrteil-Versandplan._

# Dateinamen und Paketgrenzen prüfen

## 1. Regeln

Die ERVB 2025 erlaubt höchstens 90 Zeichen einschließlich Dateiendung, höchstens 1.000 Dateien und höchstens 200 MB je Nachricht. Dieses Plugin nutzt vorsorglich:

1. höchstens 80 Zeichen einschließlich `.pdf`,
2. ausschließlich `A-Z`, `a-z`, `0-9` und Unterstrich im Stamm,
3. keine Leerzeichen, Umlaute, scharfes S, Klammern oder Sonderzeichen,
4. zweistellige, bei mindestens 100 Dateien dreistellige logische Reihenfolge,
5. sprechenden Inhalt nach Dokumentart oder Anlagenkennung.

## 2. Transliteration

`ä` wird `ae`, `ö` wird `oe`, `ü` wird `ue`, `ß` wird `ss`. Mehrere Trennzeichen werden zu einem Unterstrich. Kürze zuerst Füllwörter und erst danach die Sachbezeichnung. Anlagenkennung und Dateiendung dürfen nie abgeschnitten werden.

## 3. Muster

```text
00_20260714_Klageerwiderung_12_O_34_26.pdf
01_20260714_AnlageB1_Kaufvertrag.pdf
02_20260714_AnlageB2_E_Mail_Abnahme.pdf
```

## 4. Paketierung

Berechne Anzahl und Bytes aus den finalen Dateien, nicht aus Quellen oder Schätzungen. Wird eine Grenze erreicht, bilde Teilnachrichten mit Sicherheitsreserve. Teile keine mehrseitige Anlage. Halte Hauptdokument, Anlagenverzeichnis und den zuerst benötigten Anlagenbereich logisch zusammen.

| Teil | Dateien | Anlagenbereich | Bytes | Begleittext | Eingangsbestätigung |
| --- | --- | --- | --- | --- | --- |
| 1 von 2 | Zahl | B 1 bis B 40 | Zahl | fertig | offen |

Für jede Nachricht ist eine eigene Eingangskontrolle nötig. Übergib Dateiliste und Versandplan an `versandfreigabe-und-eingang-sichern`.

---

## Skill: `ordneraufnahme-und-produktionsmatrix`

_Liest einen vorhandenen Schriftsatz- und Anlagenordner vor jeder Rückfrage, erkennt Hauptdokument, Fassungen, bereits verwendete Anlagenkennungen, Dubletten, fehlende Belege und nicht unterstützte Formate und liefert eine konkrete Produktionsmatrix mit Quelle, Ziel-PDF, Nummer, Status und einzig noch blockierenden Entscheidungen._

# Ordneraufnahme und Produktionsmatrix

## 1. Aktivierung

Nutze diesen Skill bei einem Ordner, ZIP-Inhalt oder Dateisatz, dessen Rollen noch nicht vollständig klar sind. Er ist die erste Station von `versandmappe-endfertigen`, kein allgemeines Aktenanalysewerkzeug.

## 2. Aufnahme ohne Vorinterview

1. Originalpfad, Dateiname, Erweiterung, Bytes, Änderungsdatum und Hash erfassen.
2. Verzeichnisse wie `alt`, `entwurf`, `final`, `anlagen`, `versandt` und `intern` als Fassungsindikatoren behandeln.
3. DOCX, ODT, RTF oder PDF mit Schriftsatzkopf, Anträgen und Signaturzeile als Hauptdokument-Kandidaten markieren.
4. Anlagenverweise im Hauptdokument mit Dateinamen abgleichen.
5. inhaltsgleiche Dateien anhand Hash gruppieren; keine Datei löschen.
6. passwortgeschützte Archive, verschlüsselte PDFs, eingebettete Objekte und proprietäre Container als Stop-Befund markieren.

## 3. Fassungsentscheidung

Bei mehreren Schriftsatzfassungen nicht nach jedem Dokument fragen. Lege eine Rangfolge vor:

1. ausdrücklich als final oder unterschriftsreif bezeichnete Fassung,
2. jüngste Fassung mit vollständigem Rubrum und Anträgen,
3. versandte oder signierte Fassung nur als Vergleich, niemals stillschweigend überschreiben.

Frage einmal: `Soll [Dateiname, Stand] als Hauptdokument endgefertigt werden?` Nur bei gleichwertigen Kandidaten ist diese Rückfrage zwingend.

## 4. Produktionsmatrix

| Rolle | Quelle | Fassung | erkannte Kennung | Ziel | Konverter | Kontrolle | Befund |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Hauptdokument | Pfad | Datum/Hash | keine | PDF | Office oder direkt | visuell | Status |
| Anlage | Pfad | Datum/Hash | B 3 | PDF | Bild/Office/E-Mail | visuell | Status |

## 5. Lückenlogik

- Im Schriftsatz genannt, aber keine Datei vorhanden: `stop`.
- Datei mit Anlagenkennung, aber nicht im Schriftsatz genannt: `prüfen`, nicht automatisch versenden.
- Nummernlücke: `stop`, bis Fortsetzung oder bewusste Lücke bestätigt ist.
- Dublette: eine Versandfassung vorschlagen, alle Quellen im internen Log behalten.
- Dateityp nicht unterstützt: Quellanwendung und erforderlichen Export nennen.

## 6. Übergabe

Liefere Produktionsmatrix, Konfliktliste und höchstens zwei gebündelte Rückfragen. Übergib anschließend ohne erneute Inventur an `hauptdokument-pdf-endfertigen` und `anlagen-konvertieren-und-sichtpruefen`.

---

## Skill: `hauptdokument-pdf-endfertigen`

_Endfertigt den bereits freigegebenen Schriftsatz technisch als separates PDF: sichert die maßgebliche Quelldatei, konvertiert ohne inhaltliche Umschreibung, prüft Rubrum, Anträge, Seitenfolge, einfache Signatur, Schriften, Umbrüche, Metadaten und aktive Inhalte und liefert die visuell kontrollierte Datei mit dokumentiertem Hash._

# Hauptdokument als PDF endfertigen

## 1. Grenze

Bearbeite nur die technische Endfassung. Ändere keinen Antrag, Tatsachenvortrag, Betrag, Namen oder Termin ohne ausdrückliche Freigabe. Ein entdeckter Inhaltswiderspruch wird gemeldet, nicht still korrigiert.

## 2. Konvertierung

1. Quellhash und Fassungsstand protokollieren.
2. DOC, DOCX, ODT oder RTF mit LibreOffice headless in PDF ausgeben; vorhandene PDF unverändert in den Arbeitsbereich kopieren.
3. keine Druckdialoge verwenden, die Kommentare, Änderungsverfolgung oder ausgeblendete Ebenen unkontrolliert einbeziehen.
4. Ergebnis erneut öffnen und mit der Quelle vergleichen.

## 3. Sichtkontrolle

Prüfe jede Seite, mindestens aber systematisch:

| Kontrollpunkt | Erwartung |
| --- | --- |
| Rubrum | Gericht, Parteien, Aktenzeichen und Parteistellung vollständig sichtbar |
| Anträge | keine abgeschnittene Zeile, keine verlorene Nummerierung |
| Seiten | richtige Reihenfolge, keine Leer- oder Doppelseite |
| Fußzeile | Seitenzahl und Kanzleiangaben nicht überlagert |
| Tabellen/Bilder | vollständig, lesbar und nicht über den Rand verschoben |
| einfache Signatur | Name der verantwortenden Person am Dokumentende sichtbar |
| PDF | unverschlüsselt, druckbar, ohne eingebettete Dateien oder ausführbare Inhalte |

## 4. Benennung

Das Hauptdokument beginnt mit `00_`, enthält Datum und Dokumentart und endet mit `.pdf`, etwa `00_20260714_Klageerwiderung_12_O_34_26.pdf`. Nutze ASCII, Unterstriche und höchstens 80 Zeichen einschließlich Endung.

## 5. Übergabe

Liefere Dateiname, Seitenzahl, Bytes, SHA-256, Quellfassung, Sichtprüfer und Prüfergebnis. Leite die Formentscheidung an `signaturweg-und-absender-pruefen` weiter; ein sichtbarer Namenszug allein entscheidet die Signaturroute nicht.

---

## Skill: `anlagen-nummerieren-und-stempeln`

_Führt den vorhandenen Anlagenkreis K, B, AST oder AG ohne Kollision fort, gleicht jede Kennung mit Schriftsatz und Anlagenverzeichnis ab, stempelt die Bezeichnung gut lesbar rechts oben auf jede PDF-Seite, schützt vorhandenen Inhalt vor Überdeckung und liefert getrennte Versand-PDFs sowie ein lückenloses Anlagenverzeichnis._

# Anlagen nummerieren und stempeln

## 1. Nummernkreis

Nutze nur den für die Rolle und das Verfahren bestätigten Kreis:

- `K` für Klägerseite,
- `B` für Beklagtenseite,
- `AST` für Antragstellerseite,
- `AG` für Antragsgegnerseite.

Übernimm einen bereits verwendeten Kreis aus den Akten. Beginne nicht erneut bei 1, wenn frühere Einreichungen vorliegen. Bei unklarer Fortsetzung stoppe und frage nach letztem Anlagenverzeichnis oder letzter Einreichung.

## 2. Drei-Wege-Abgleich

Für jede Anlage müssen übereinstimmen:

1. Bezeichnung an der Schriftsatzstelle,
2. Zeile im Anlagenverzeichnis,
3. Stempel und Dateiname der PDF.

Eine Datei, die nur im Ordner liegt, wird nicht automatisch versandt. Eine im Schriftsatz genannte, aber fehlende Datei ist ein Stop-Befund.

## 3. Stempel

Stemple `Anlage K 1`, `Anlage B 3`, `Anlage AST 2` oder `Anlage AG 4` rechts oben auf jede Seite. Prüfe danach jede Seite auf:

- sichtbaren, richtigen Stempel,
- keine Überdeckung von Briefkopf, Datum, Seitenzahl, Unterschrift oder Bildinhalt,
- unverändertes Seitenformat und richtige Rotation,
- unveränderte Seitenzahl.

Wenn rechts oben kein freier Bereich besteht, verwende nach ausdrücklicher Festlegung einen gleichbleibenden anderen Randbereich oder ein vorgeschaltetes Deckblatt. Nicht still über Inhalt stempeln.

## 4. Ergebnis

Liefere getrennte Anlagen-PDFs, ein Anlagenverzeichnis und eine Kontrolltabelle mit Schriftsatzfundstelle, Kennung, Versanddatei, Seitenzahl und Sichtprüfung. Übergib anschließend an `dateinamen-und-paketgrenzen-pruefen`.

---

## Anwendungshinweise

1. Diese Vollprüfung als Kontext einfügen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Bearbeiter anweisen, sich anhand der oben aufgeführten Skills zu orientieren.
4. Entscheidungen nur nach Prüfung von Gericht, Datum, Aktenzeichen, tragender Aussage und amtlicher oder frei zugänglicher Quelle verwenden.
