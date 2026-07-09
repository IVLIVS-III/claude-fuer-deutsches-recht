# Vollprüfung: status-navigator-step-plan

## Zusammensetzung

Dieser Vollprüfung enthaelt top-15 von 35 Skills des Plugins `status-navigator-step-plan`.

## Inhaltsverzeichnis

1. **ampel-system** — Wenn es um Ampelsystem für Status in Plugin: status-navigator-step-plan geht: ordnet Sachverhalt, Norm, Beweislast, Gege…
2. **dokumententyp-beschluesse** — Wenn es um Dokumententyp Gesellschafterbeschluesse in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Beleg…
3. **dokumententyp-erklaerungen** — Wenn es um Dokumententyp einseitige Erklaerungen in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege,…
4. **ziel-praezisieren** — Wenn es um Ziel praezisieren in Plugin: status-navigator-step-plan geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargu…
5. **erweiterung-hyperlinks** — Wenn es um Erweiterung Hyperlinks zur Ablage in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lüc…
6. **status-navigator-einstieg** — Wenn es um Einstieg: Was haben wir und was muss geschehen in Plugin: status-navigator-step-plan geht: klärt Rolle, Ziel,…
7. **luecken-notifizieren** — Wenn es um Luecken in Tabellen notifizieren in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lück…
8. **dokumententyp-korrespondenz** — Wenn es um Dokumententyp Korrespondenz in Plugin: status-navigator-step-plan geht: erstellt den passenden Entwurf aus Sa…
9. **dokumententyp-vertraege** — Wenn es um Dokumententyp Verträge erkennen in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücke…
10. **excel-reiter-1-ueberblick** — Wenn es um Reiter 1 Überblick Statuslage in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken …
11. **excel-reiter-2-vorhanden** — Wenn es um Reiter 2 Vorhandene Dokumente in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken …
12. **excel-reiter-3-fehlend** — Wenn es um Reiter 3 Fehlende Dokumente in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken un…
13. **excel-reiter-4-workflow** — Wenn es um Reiter 4 Workflow Step-Plan in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken un…
14. **szenario-mandatsuebernahme** — Wenn es um Szenario Mandatsuebernahme in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und…
15. **dokumententyp-cap-tables** — Wenn es um Dokumententyp Cap Tables in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und N…

---

## Skill: `ampel-system`

_Wenn es um Ampelsystem für Status in Plugin: status-navigator-step-plan geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt._

# Ampelsystem für Status

## Rolle und Fokus
Dreistufige Ampel (gruen/gelb/rot) als bedingte Formatierung in der Excel-Arbeitsmappe und als Farbtag in Padlet-Karten. Verdichtet komplexe Statuslagen auf einen Blick.

## Anwendungsbeispiel
LausitzStorage-Akte Stand 02.06.2026: 4 rote Eintraege (Drawstop NordCap, Anlage 4 Konsortialvertrag fehlt, Zugangsnachweis LEAG-Kuendigungsdrohung unklar, Avalstatus 50Hertz unbestaetigt), 7 gelbe (drei Cap-Table-Versionen mit Abweichungen, zwei Unterschriften fragwuerdig, ein Gesellschafterbeschluss inhaltlich unklar, Drawstop-Schreiben unklar zugegangen), Rest gruen.

## Output-Module
- Bedingte-Formatierung-Regeln je Reiter (Hintergrundfarbe auf Status-Spalte)
- Restzeit-Ampel im Fristen-Reiter mit Schwellen 30/8 Tage
- Ampel-Konsistenz-Prüfung zwischen Reiter 2 und 3

---

## Skill: `dokumententyp-beschluesse`

_Wenn es um Dokumententyp Gesellschafterbeschluesse in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt._

# Dokumententyp Gesellschafterbeschluesse

## Rolle und Fokus
Erkennt Beschlüsse als Dokumentenklasse. Gesellschafterbeschluss, Aufsichtsrats-, Hauptversammlungs-, Vorstandsbeschluss. Erfasst Beschlussdatum, beschliessende Organe, Beschlussgegenstand und Formerfordernis.

## Anwendungsbeispiel
Gesellschafterbeschluss vom 17.10.2025: Zustimmung zum Senior-Darlehensvertrag NordCap und zur Bestellung der Sicherheiten. Beschluss vorhanden, aber Schriftform statt Umlaufbeschluss mit Originalunterschriften aller Gesellschafter — Form steht in der GmbH-Satzung § 11 (verlangt notarielles Protokoll für Sicherheitenbestellung > 50 Mio EUR). Klärungsbedarf.

## Output-Module
- Eintrag in Reiter 2 mit Typ-Tag Beschluss
- Querverweis auf zustimmungspflichtige Verträge (Reiter 2 Anmerkungsspalte)
- Hinweisliste an `unterschriftspruefung` und ggf. Reiter 3 wenn Form fragwuerdig

---

## Skill: `dokumententyp-erklaerungen`

_Wenn es um Dokumententyp einseitige Erklaerungen in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt._

# Dokumententyp einseitige Erklaerungen

## Rolle und Fokus
Erkennt einseitige Willenserklaerungen: Kuendigungen, Faelligstellungen, Anfechtungen, Ruecktritte, Widerrufe, Wandlungserklaerungen. Markiert besonders zugangsbeduerftige Erklaerungen.

## Anwendungsbeispiel
Drawstop-Schreiben NordCap vom 22.05.2026: einseitige Erklaerung der Auszahlungsverweigerung gestuetzt auf 'material adverse change' und 'documentation gaps'. Versand per E-Mail an Bauernfeind; Zugangsnachweis fehlt; Vertretungsbefugnis des Unterzeichners (NordCap-Investment-Director) ist im Senior-Darlehensvertrag nicht eindeutig geregelt.

## Output-Module
- Eintrag in Reiter 2 mit Typ-Tag Erklaerung und Untertyp
- Pflicht-Querverweis an `zugang-zustellung-pruefung`
- Bei Vollmachtsfrage: Querverweis an `unterschriftspruefung`

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

---

## Skill: `ziel-praezisieren`

_Wenn es um Ziel praezisieren in Plugin: status-navigator-step-plan geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt._

# Ziel praezisieren

## Rolle und Fokus
Klaert mit der Mandantin das konkrete Ziel des Status-Navigators. Faelligstellung, Bereinigung, Due Diligence, Mandatsuebernahme — das Ziel bestimmt die Reiterstruktur, Erweiterungen und Priorisierung.

## Anwendungsbeispiel
LausitzStorage Ziel laut Mandantenwunsch: (1) vollstaendige Bestandsaufnahme aller Verträge und Genehmigungen, (2) Excel-Tracker, (3) Strategiepapier 14 Tage, (4) Zugangspruefung Drawstop-Schreiben. Daraus folgt Reiterstruktur mit Sicherheiten- und Fristen-Reiter (Pflicht), Cap-Table-Versionsregister noetig, BImSchG-Cluster eigenstaendig.

## Output-Module
- Schriftliche Zielnotiz (eine halbe Seite)
- Reiter- und Erweiterungs-Auswahl daraus abgeleitet
- Priorisierungsregel für Reiter 4 (Workflow)

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

---

## Skill: `erweiterung-hyperlinks`

_Wenn es um Erweiterung Hyperlinks zur Ablage in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt._

# Erweiterung Hyperlinks zur Ablage

## Rolle und Fokus
Verknuepft Tabelleneintraege mit Originaldokumenten in der Ablage. Sprung von der Tabelle zum Volltext spart Sucherei bei jeder Folgepruefung.

## Anwendungsbeispiel
LausitzStorage-Akte: Reiter 1 verlinkt alle 19 Hauptdokumente in den Mandantsfileshare. Anlage 4 zum Konsortialvertrag bekommt Platzhalter-Link `_FEHLT_` damit beim Klick sofort sichtbar ist dass die Anlage in Reiter 3 nachverfolgt wird.

## Output-Module
- Hyperlink-Spalte je Reiter (relativer Pfad)
- Platzhalter-Link `_FEHLT_` für in Reiter 3 verfolgte Luecken
- Wartungspruefung als Eintrag in `erweiterung-laufende-aktualisierung`

---

## Skill: `status-navigator-einstieg`

_Wenn es um Einstieg: Was haben wir und was muss geschehen in Plugin: status-navigator-step-plan geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Einstieg: Was haben wir und was muss geschehen

## Direktstart: lesen, entscheiden, liefern

Beginne nicht mit einem Fragenkatalog. Wenn Material vorliegt, lies es zuerst und starte mit einer verwertbaren Arbeitshypothese:

- Frist oder Sofortrisiko.
- erkannte Rolle, Zielrichtung und Verfahrensstand.
- tragende Tatsachen aus dem Material.
- bester nächster Arbeitsschritt mit direkt nutzbarem Output.

Frage höchstens zwei Punkte nach, und nur wenn ohne diese Antwort der nächste Schritt falsch oder riskant würde. Fehlt Material vollständig, verlange nicht allgemein alle Unterlagen, sondern nenne die drei wichtigsten Dokumente und arbeite mit sichtbaren Annahmen weiter.

Starte mit einem Arbeitsprodukt, nicht mit einer Inventarliste: Kurzvermerk, Fristenblatt, Prüfmatrix, Entwurf, Fragenliste oder Entscheidungsvorschlag. Routing ist nur Mittel zum Zweck. Wenn ein Fachskill eindeutig passt, arbeite unmittelbar in dessen Richtung weiter.

Arbeitsmodus: Liefere zuerst einen nutzbaren Zwischenstand in höchstens sieben Sätzen und dann den nächsten konkreten Schritt. Frage nur nach, wenn Frist, Zuständigkeit, Beweis, Betrag oder Rechtsfolge sonst nicht belastbar bestimmbar sind. Tabellen nur für Fristen, Belege, Beträge, Varianten oder Streitstoff.

## Rolle und Fokus
Erstes Sichten und grobes Strukturieren der Dokumentenlage. Setzt den Rahmen für alle Folgeschritte und beantwortet die zwei Kernfragen: Was haben wir? Was muss als Naechstes geschehen?

## Anwendungsbeispiel
LausitzStorage Erstsichtung 02.06.2026 nach Mandatsannahme: 80 PDFs aus drei Quellen; nach 90 Minuten liegt eine erste Reiter-1-Liste mit 28 Eintraegen, drei Sofortmassnahmen (Zugangsnachweis Drawstop sichern, Anlage 4 Konsortial nachfordern, Wandlungsfrist Wandeldarlehen prüfen) und ein Cluster-Ampelbild vor.

## Output-Module
- Erstrunde-Reiter-1 mit grober Verfuegbarkeit
- Liste der zwei bis drei Sofortmassnahmen
- Auftrag für Folgeskills (Inventur, Dokumententypen, Zustellung)

---

## Skill: `luecken-notifizieren`

_Wenn es um Luecken in Tabellen notifizieren in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt._

# Luecken in Tabellen notifizieren

## Rolle und Fokus
Notifiziert direkt in den Tabellen, wo Fehler, Luecken oder Unklarheiten bestehen. Standard-Notes umfassen die haeufigsten Befunde aus Restrukturierungs- und Vollstreckungsmandaten.

## Anwendungsbeispiel
LausitzStorage: 23 Notes über alle Reiter. Wiederholte Notes: `Zustellung unklar` (Drawstop-Schreiben, LEAG-Kuendigungsdrohung), `Anlage fehlt` (Anlage 4 Konsortialvertrag, BImSchG-Auflagenliste), `Beschluss-Form fragwuerdig` (Gesellschafterbeschluss 17.10.2025 ohne notarielles Protokoll), `Unterschrift Vertretung unklar` (zwei Pachtvertragsnachtraege).

## Output-Module
- Standard-Notes-Vokabular als Vorblatt
- Anmerkungsspalten in Reiter 2 und 3 konsistent befuellt
- Bruecke zu Reiter 4 (jede Note erzeugt einen Workflow-Schritt)

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

---

## Skill: `dokumententyp-korrespondenz`

_Wenn es um Dokumententyp Korrespondenz in Plugin: status-navigator-step-plan geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik._

# Dokumententyp Korrespondenz

## Rolle und Fokus
Erkennt Korrespondenz: E-Mails, Briefe, Aktenvermerke, Faxprotokolle, Telefonnotizen. Erfasst Absender, Empfaenger, Datum, Betreff, Bezug.

## Anwendungsbeispiel
E-Mail-Korrespondenz LEAG vom 19.05.2026: Drohung mit Pachtvertragskuendigung wegen verspaeteter Vorlage der BImSchG-Genehmigungsunterlagen. Thread enthaelt vier Mails, einen Anhang (Auflistung der vermissten Unterlagen), keine Empfangsbestaetigung; im Bezug steht § 12 Abs. 3 Pachtvertrag (Beibringungspflicht).

## Output-Module
- Eintrag in Reiter 2 mit Typ-Tag Schreiben oder Korrespondenz
- Thread-Mapping in Anmerkungsspalte
- Querverweis an `dokumententyp-erklaerungen` falls Korrespondenz tatsaechlich eine Erklaerung enthaelt

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

---

## Skill: `dokumententyp-vertraege`

_Wenn es um Dokumententyp Verträge erkennen in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt._

# Dokumententyp Verträge erkennen

## Rolle und Fokus
Erkennt Verträge als Dokumentenklasse. Pachtvertraege, Darlehensvertraege, Konsortialvertraege, Sicherungsvertraege, Gesellschaftervereinbarungen. Ordnet nach Vertragspartei, Datum, Vertragstyp.

## Anwendungsbeispiel
LausitzStorage-Vertragslandschaft: Pachtvertrag LEAG mit 2 Nachtraegen, Senior-Darlehen NordCap, Wandeldarlehen NordCap, Konsortialvertrag Stadtwerke Cottbus, Avalrahmenvertrag ILB, Netzanschluss 50Hertz. Sieben Verträge mit teils ueberlappenden Sicherheiten und Zustimmungserfordernissen — eine Vertragslandkarte vor der Reiterpflege ist Pflicht.

## Output-Module
- Vertragslandkarte (Bezugsgraph) als Vorblatt
- Eintraege in Reiter 2 mit Typ-Tag Vertrag und Untertyp
- Querverweise auf abhaengige Beschlüsse, Vollmachten und Sicherheitenbestellungen

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

---

## Skill: `excel-reiter-1-ueberblick`

_Wenn es um Reiter 1 Überblick Statuslage in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt._

# Reiter 1 Überblick Statuslage

## Rolle und Fokus
Reiter 1 ist die Gesamtsituation auf einen Blick. Alle für die Durchsetzung erforderlichen Dokumente in einer Zeile mit den wichtigsten Statusfeldern.

## Anwendungsbeispiel
LausitzStorage Reiter 1: 28 Zeilen über 4 Cluster, davon 4 rot (NordCap-Drawstop-Schreiben Zugang, Anlage 4 Konsortial, BImSchG-Vorbescheid Auflagen, Avalstatus 50Hertz), 7 gelb (Cap-Table-Versionen, drei Unterschriftsbefunde, ein Beschluss-Formfrage), Rest gruen. Pro Cluster eine Subsumtionszeile mit Cluster-Gesamtstatus.

## Output-Module
- Reiter 1 als Master-Index mit Querverweis in jede Detailpruefung
- Cluster-Gesamtstatuszeile je Vertragsebene
- Spalte Querverweis zu Reiter 2/3/4

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

---

## Skill: `excel-reiter-2-vorhanden`

_Wenn es um Reiter 2 Vorhandene Dokumente in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt._

# Reiter 2 Vorhandene Dokumente

## Rolle und Fokus
Reiter 2 ist die Detailansicht aller tatsaechlich vorliegenden Dokumente,
mit Augenmerk auf Vertretungsbefugnis und Unterschriftsstatus. Hier wird
genauer hingeschaut als auf Reiter 1.

## Vorlage-Bezug
Reiter 2 folgt der Excel-Vorlage. Spalten:

| Spalte | Inhalt |
|---|---|
| Dokument (Bezeichnung) | sprechend |
| Datum | Vertragsdatum |
| Typ | Vertrag, Bescheid, Erklaerung, Beschluss, Schreiben, Cap Table |
| Unterzeichnet von (Partei und Funktion) | konkret, mit Funktion |
| Unterschriftsstatus | vollstaendig / fragwuerdig / Entwurf |
| Anmerkung | Fundort, Urkundsnummer, Auffaelligkeiten |

## Anwendungsbeispiel
LausitzStorage-Akte: Reiter 2 enthaelt 16 vorliegende Dokumente. Drei
davon haben `fragwuerdig` als Unterschriftsstatus:
- 1. Nachtrag Pacht: Prokuristin Kosturek allein (Gesamtprokura mit GF
  erforderlich, § 177 BGB schwebend unwirksam) – Hinweis in Anmerkung
- 2. Nachtrag Pacht: GF Vansel allein (nur gemeinschaftliche Vertretung) – Hinweis
- Wandeldarlehen NordCap: § 4 verweist auf nicht existenten
  Gesellschafterbeschluss (Copy-Paste-Fehler) – Hinweis

## Output-Module
- Tabelleneintraege für Reiter 2
- Hinweisliste für Reiter 3 (was ist als Anlage zu beschaffen)
- Querliste für den Skill unterschriftspruefung
- Querliste für den Skill copy-paste-fehler-erkennung

## Grenzen
- **Keine rechtliche Wirksamkeitspruefung.** Schwebende Unwirksamkeit nach
  § 177 BGB ist nur ein Hinweis, kein Befund – Heilung prüfen anwaltlich.
- **Keine Vollmachts-Beurteilung.** Der Skill kann nur sichtbare Abweichungen
  vom HR-Eintrag herausarbeiten; gewillkuerte Vollmachten müssen aktiv
  abgefragt werden.

## Plugin-Kontext
Reiter 2 ist die Lieferquelle für die Skills unterschriftspruefung,
copy-paste-fehler-erkennung, diskrepanzen-aufdecken. Sauber gebauter
Reiter 2 spart Stunden in den Folgeschritten.

---

## Skill: `excel-reiter-3-fehlend`

_Wenn es um Reiter 3 Fehlende Dokumente in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt._

# Reiter 3 Fehlende Dokumente

## Rolle und Fokus
Reiter 3 listet alles, was fehlt oder noch nicht endgueltig vorliegt.
Jede Zeile hier ist eine offene Position, die in den Workflow von
Reiter 4 ueberfuehrt werden muss.

## Vorlage-Bezug
Reiter 3 folgt der Excel-Vorlage. Spalten:

| Spalte | Inhalt |
|---|---|
| Erforderliches Dokument / erforderlicher Nachweis | sprechend |
| Angefordert von | Person oder Kanzlei intern |
| Zu beschaffen von | Quelle: Behoerde, Notar, Vertragspartner |
| Grund der Erforderlichkeit | warum brauchen wir es, mit Querverweis Klausel oder Paragraph |
| Status | offen / Anforderung raus / in Bearbeitung / vorzubereiten / Frist |

## Anwendungsbeispiel
LausitzStorage-Akte: Reiter 3 enthaelt 12 Positionen, sortiert nach Frist:
- 09.06.: Aushaendigung LEAG-Aval (Frist § 11 Pacht ueberzogen)
- 10.06.: Notartermin Klarstellungs-Nachtrag Pacht
- 11.06.: Klarstellungs-Side-Letter Anlage 4
- 18.06.: ILB-Komitee Einzelaval 50Hertz
- 30.06.: BImSchG-Hauptantrag (Drohfrist LEAG)

## Output-Module
- Tabelleneintraege für Reiter 3
- Frist-Liste aufsteigend
- Eingangsstapel für Reiter 4 (Workflow)
- Optional Reiter 5 (Fristenkontrolle) mit Querverweis

## Grenzen
- **Beschaffungswege können sich verschieben.** Behoerdliche Bearbeitungszeiten
  realistisch ansetzen, nicht idealisieren.
- **Frist-Tracking ersetzt keinen Fristenkalender.** Anwaltlicher Fristenkalender
  bleibt verbindlich.

## Plugin-Kontext
Reiter 3 ist die Voraussetzung für Reiter 4. Ohne saubere Liste der
fehlenden Stuecke kann kein Workflow gebaut werden.

---

## Skill: `excel-reiter-4-workflow`

_Wenn es um Reiter 4 Workflow Step-Plan in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt._

# Reiter 4 Workflow Step-Plan

## Rolle und Fokus
Reiter 4 ist das Herzstueck. Hier wird aus jedem fehlenden Dokument ein
konkreter Step-Plan: welche Schritte in welcher Reihenfolge, mit welcher
Rechtsgrundlage, von wem zu unterzeichnen, an wen zu versenden.

## Vorlage-Bezug
Reiter 4 folgt der Excel-Vorlage. Spalten:

| Spalte | Inhalt |
|---|---|
| Erforderliches Dokument | aus Reiter 3 uebernommen |
| Schritte zur Beschaffung (in Reihenfolge) | nummeriert 1. 2. 3. ... |
| Rechtsgrundlage (Klausel im zugrunde liegenden Vertrag) | Klausel oder Paragraph |
| Unterzeichnet von | die Personen, die zeichnen müssen |
| Versendet an | Empfaenger, ggfs mit Sendeweg (Bote, Einschreiben, Notar, HR) |

## Anwendungsbeispiel
LausitzStorage-Akte, Reiter 4 enthaelt 12 Beschaffungs-Workflows.
Beispiele:
- Einzelaval 50Hertz: 1. Antwort ILB-Rueckfrage 18.04. ergaenzen,
  2. ILB-Komitee 18.06. abwarten, 3. Backup-Antrag Berliner Sparkasse
  parallel halten, 4. Aval-Urkunde an 50Hertz.
- Reparaturvereinbarung Wandeldarlehen NordCap: 1. Entwurf Akte 22
  finalisieren, 2. NordCap-Anwalt Mitzeichnung, 3. Bauernfeind
  unterzeichnet.

## Output-Module
- Tabelleneintraege für Reiter 4
- Reihenfolge-Visualisierung als Gantt-aehnliche Liste (Datumsspalte
  optional)
- Verantwortlichkeiten-Liste pro Person
- Eingangsstapel für optionale Reiter (Fristen, Beteiligte)

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Grenzen
- **Workflow ist Vorschlag, kein Anwaltsplan.** Anwaeltliche Prüfung der
  Rechtsgrundlagen-Spalte erforderlich.
- **Versendungswege sind Vorschlag.** Tatsaechlicher Zugangsweg muss
  haendisch abgesichert werden.
- **Zeitschaetzungen sind grob.** Behoerdliche Bearbeitungszeiten variieren.

## Plugin-Kontext
Reiter 4 ist der Action-Plan. Wenn Reiter 1 bis 3 sauber sind, schreibt
Reiter 4 sich fast von selbst. Optional ergaenzbar durch Reiter 5
(Fristen), Reiter 6 (Beteiligte), Reiter 7 (Rangfolge) und Reiter 8
(Sicherheiten).

---

## Skill: `szenario-mandatsuebernahme`

_Wenn es um Szenario Mandatsuebernahme in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt._

# Szenario Mandatsuebernahme

## Rolle und Fokus
Uebernahme eines Mandats mit ungeordneter Dokumentenlage. Status-Navigator erzeugt schnell Klarheit über Status und naechste Schritte. Markiert Sofortpflichten und uebersehene Fristen.

## Anwendungsbeispiel
LausitzStorage waere bei hypothetischer Mandatsuebernahme von Pohlmann & Pohlmann an andere Kanzlei: Übergabenotiz nennt 4 rote Reiter-1-Eintraege und 1 gelbe Frist (Wandlungsfenster 30.09.2026). Sofortmassnahmen: Zugangsnachweis Drawstop sichern, Anlage 4 Konsortial nachfordern, Avalstatus 50Hertz klären — alles innerhalb 5 Werktagen.

## Output-Module
- Uebernahme-Reiter mit roten und gelben Eintraegen aus Vorgaengerakte
- Frist-Soforterhebung mit Restzeit-Ampel
- Erstkontaktliste für den Tag nach Mandatsuebernahme

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

---

## Skill: `dokumententyp-cap-tables`

_Wenn es um Dokumententyp Cap Tables in Plugin: status-navigator-step-plan geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt._

# Dokumententyp Cap Tables

## Rolle und Fokus
Erkennt Cap Tables in beliebigem Format (Excel, PDF, eingebettete Tabellen). Erfasst Stichdatum, Gesellschafter, Anteile. Vorbereitung für Konsistenzvergleich mehrerer Versionen.

## Anwendungsbeispiel
LausitzStorage: drei Cap-Table-Versionen liegen vor. v1 (31.12.2025, von Mandantin), v2 (30.04.2026, von NordCap-Datenraum), v3 (Mai 2026, aus Investor-Update). Vergleich liefert die in `diskrepanzen-aufdecken` aufgenommene 48/51/48-Abweichung.

## Output-Module
- Versionsregister mit Stichdatum, Quelle, Status
- Normalisierte Cap-Table als Vorlage für den Konsistenzvergleich
- Querliste an `szenario-cap-table-bereinigung` wenn Abweichungen materiell

---

## Anwendungshinweise

1. Diesen Vollprüfung als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.
