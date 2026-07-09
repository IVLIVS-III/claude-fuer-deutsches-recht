# Vollprüfung: fachanwalt-arbeitsrecht

## Zusammensetzung

Dieser Vollprüfung enthaelt top-8 von 120 Skills (gekuerzt fuer Chat-Fenster) des Plugins `fachanwalt-arbeitsrecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Wenn es um Anwalts-Dashboard Fachanwalt Arbeitsrecht in Fachanwalt Arbeitsrecht geht: klärt Rolle, Ziel, Frist, Unterlag…
2. **fachanwalt-arbeitsrecht-orientierung** — Wenn es um Fachanwalt für Arbeitsrecht — Orientierung in Fachanwalt Arbeitsrecht geht: prüft Frist, Form, Zuständigkeit,…
3. **orientierung-mandat-fachanwaltschaft** — Wenn es um Orientierung Mandat Fachanwaltschaft in Fachanwalt Arbeitsrecht geht: prüft Frist, Form, Zuständigkeit, Recht…
4. **erstgespraech-mandatsannahme** — Wenn es um Erstgespraech Mandatsannahme in Fachanwalt Arbeitsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und…
5. **erstpruefung-und-mandatsziel** — Wenn es um Erstpruefung Und Mandatsziel in Fachanwalt Arbeitsrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den pa…
6. **fachanwalt-arbeitsrecht-bag-freistellungsklausel-unwirksam** — Wenn es um Rechtsprechung live prüfen in Fachanwalt Arbeitsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und S…
7. **fachanwalt-arbeitsrecht-bag-mindesturlaub-kein-verzicht** — Wenn es um Rechtsprechung live prüfen in Fachanwalt Arbeitsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und S…
8. **befristung-tzbfg** — Wenn es um Befristungskontrolle und Befristungsgestaltung nach TzBfG für Arbeitgeber und Arbeitnehmer in Fachanwalt Arbe…

---

## Skill: `einstieg-routing`

_Wenn es um Anwalts-Dashboard Fachanwalt Arbeitsrecht in Fachanwalt Arbeitsrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Anwalts-Dashboard Fachanwalt Arbeitsrecht

> Kündigung, Aufhebungsvertrag, Befristung, Betriebsrat, Betriebsübergang — sieben Eilfristen, ein Klagestrang.
>
> Sie sehen unten die Sofort-Triage. Keine Rückfragen, bis die Tabelle steht. Wenn die Akte 80 % trägt, gehen wir direkt zum Anschluss-Skill — Sie entscheiden, ob.

## Sofort-Triage

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
| --- | --- | --- |
| Rolle | Wen vertrete ich? (Mandant · Gegenseite · Mehrere) | Mandantenmail, Vertretungsbestellung |
| Verfahrensstand | Vorprozessual · außergerichtlich · Klage · Rechtsmittel · Vollstreckung | Vorhandene Schriftsätze, Eingangsstempel |
| Eilfrist | **Paragraf 4 KSchG: 3 Wochen** ab Zugang Kündigung. Daneben Paragraf 626 II BGB (außerordentlich, 2 Wochen ab Kenntnis), Paragraf 15 IV AGG (2 Monate Geltendmachung), Paragraf 17 KSchG (Massenentlassungsanzeige), Paragraf 9 MuSchG, Paragraf 613a VI BGB (1 Monat Widerspruch). | Frist aus Zugangs-/Kenntnisdatum berechnen |
| Hauptanspruch | Kündigungsschutz Paragrafen 1, 4, 7 KSchG · Lohn Paragrafen 611a, 614, 615 BGB (Annahmeverzug) · Schadensersatz Paragrafen 280 I, 823 BGB · AGG-Entschädigung Paragrafen 7, 15 AGG · Betriebsübergang Paragraf 613a BGB. | Sachverhaltsabgleich mit Tatbestandsmerkmalen |
| Zuständigkeit | Arbeitsgericht am Arbeitsort (Paragraf 48 ArbGG, Paragraf 17 ZPO). Streitwert KSchG-Klage: 1/4 Bruttojahresgehalt (Paragraf 42 II GKG). | Gesetz, Vertrag, Gerichtsstandsklausel |

## Risiko-Ampel

- **Frist:** 🔴 Kündigung mit laufender 3-Wochen-Frist: heute Klageschrift. 🟠 Aufhebungsvertrag mit Widerrufsoption: 14 Tage prüfen. 🟢 Lohnklage ohne Verfallsklausel.
- **Beweislage:** 🟠 Zugang der Kündigung trägt der Arbeitgeber (Paragraf 130 BGB); Zustellungsnachweis sichern. 🔴 Bei mündlicher Kündigung: Zeugen organisieren.
- **Wirtschaftlich:** 🔴 Lohnverlust > 3 Monate + Verlust SV-Pflicht: Eilantrag Weiterbeschäftigung (Paragraf 102 V BetrVG) prüfen. 🟠 Abfindung ≈ 0,5 Monatsgehälter pro BJ als Verhandlungsstart.

## Anschluss-Skills (Router)

| Wenn der Fall trägt … | dann Skill | Erwartung |
| --- | --- | --- |
| **Kündigung erhalten — Schutzklage prüfen** | `ar-kuendigungspruefung-workflow` | Klageschrift mit Anträgen, Streitwertangabe, Antrag auf vorläufige Weiterbeschäftigung |
| Aufhebungsvertrag angeboten | `ar-aufhebungsvertrag-praxis` | Risikomatrix, Abfindungs-Range, Sperrzeit Paragraf 159 SGB III |
| Befristung soll geprüft werden | `befristung-tzbfg` | Sachgrund- vs. sachgrundlose Befristung, Anschlussverbot Paragraf 14 II 2 TzBfG |
| Betriebsrats-Beteiligung streitig | `beteiligung-betriebsrat-102-betrvg` | Anhörungsfehler, Heilung, Folge der Unwirksamkeit |
| Betriebsübergang im Raum | `ar-betriebsuebergang-spezial` | Widerspruchsfrist Paragraf 613a VI BGB (1 Monat), Informationsanspruch |

## Norm-Radar (live verifizieren)

- **Paragraf 4 KSchG** — 3-Wochen-Frist Kündigungsschutzklage
- **Paragraf 626 BGB** — außerordentliche Kündigung, 2-Wochen-Frist Abs. 2
- **Paragraf 1 KSchG** — Sozialwidrigkeit; KSchG-Anwendung ab 10 AN (Kleinbetrieb)
- **Paragrafen 611a, 615 BGB** — Arbeitsvertrag, Annahmeverzug
- **Paragraf 613a BGB** — Betriebsübergang; Widerspruchsrecht Abs. 6
- **Paragraf 102 BetrVG** — Anhörung Betriebsrat; Folge der Unwirksamkeit

## Genau eine Rückfrage (nur wenn nötig)

> Liegt eine **Kündigung mit Zugangsdatum** vor — oder ist der Triggerpunkt ein anderer (Befristung, Lohn, Aufhebungsvertrag, AGG)?

Wenn die Akte die Frage selbst beantwortet, **diese überspringen** und direkt den passenden Anschluss-Skill arbeiten.

## Leitentscheidungs-Anker (Such-Wegweiser, keine fertigen Zitate)

- **Kündigungsschutz Paragraf 1 KSchG; Sozialwidrigkeit** — BAG 2. Senat — *live verifizieren auf* `bundesarbeitsgericht.de`
- **Betriebsübergang Paragraf 613a BGB; Identitätswahrung** — BAG 8. Senat (Spijkers-/Süzen-Linie) — *live verifizieren auf* `bundesarbeitsgericht.de + EuGH curia.europa.eu`
- **Befristung ohne Sachgrund; Vorbeschäftigung Paragraf 14 II 2 TzBfG** — BAG 7. Senat; BVerfG 1. Senat — *live verifizieren auf* `bundesarbeitsgericht.de + bundesverfassungsgericht.de`
- **AGG-Entschädigung Paragraf 15 II; 2-Monats-Frist** — BAG 8. Senat — *live verifizieren auf* `bundesarbeitsgericht.de`

> Diese Anker sind Sucheinstieg. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle prüfen und Datum, Aktenzeichen, Randnummer abklären. Kuratierte Anker-Sammlung in `references/leitentscheidungen-anker.md`.

## Hinweis

Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Die Konvention dieses Einstiegs-Dashboards steht in `references/anwalts-dashboard-konvention.md`.

## Aktuelle BAG-Linie 2025/2026 (live verifizieren vor Schriftsatzverwendung)

Drei aktuelle Leitentscheidungen, die über das Arbeitsrecht in den letzten zwoelf Monaten besonders weit ausstrahlen:

| Entscheidung | Tragende Aussage | Skill-Vertiefung |
| --- | --- | --- |
| **BAG, Urt. v. 23.10.2025 - 8 AZR 300/24** | **Equal Pay - Paarvergleich genuegt.** Eine einzige besser bezahlte Vergleichsperson des anderen Geschlechts mit gleicher oder gleichwertiger Arbeit reicht, um die Vermutung des $ 22 AGG auszuloesen. Der Arbeitgeber muss konkret darlegen, dass die Differenz ausschließlich auf objektiven, geschlechtsneutralen Gruenden beruht. Pauschale Hinweise auf Medianwerte, Durchschnittsbetrachtungen oder Verhandlungsgeschick reichen nicht. Art. 157 AEUV bekommt damit Schaerfe. | `bag-equal-pay-paarvergleich` (fachanwalt-arbeitsrecht) / `bag-equal-pay-paarvergleich-8azr30024` (arbeitsrecht) |
| **BAG, Urt. v. 03.06.2025 - 9 AZR 104/24** | **Kein Verzicht auf gesetzlichen Mindesturlaub.** Im bestehenden Arbeitsverhaeltnis können Arbeitnehmer:innen auf den gesetzlichen Mindesturlaub nicht wirksam verzichten - auch nicht durch gerichtlichen Vergleich. Gilt selbst dann, wenn die Beendigung bereits feststeht und absehbar ist, dass der Urlaub krankheitsbedingt nicht mehr genommen werden kann. Ausgleichs-/Erledigungs-/Abgeltungsklauseln müssen sauber zwischen gesetzlichem Mindesturlaub, vertraglichem Mehrurlaub und bereits entstandener Urlaubsabgeltung unterscheiden. | `bag-mindesturlaub-kein-verzicht` (fachanwalt-arbeitsrecht) / `bag-mindesturlaub-kein-verzicht-9azr10424` (arbeitsrecht) |
| **BAG, Urt. v. 25.03.2026 - 5 AZR 108/25** | **Pauschale Freistellungsklauseln in Arbeitsvertragsformularen unwirksam.** Eine formularmaessige Freistellungsklausel, die dem Arbeitgeber das einseitige Recht gibt, Beschäftigte nach Kuendigung unter Fortzahlung der Vergütung freizustellen, ist nach AGB-Kontrolle unwirksam, wenn sie Arbeitnehmer:innen unangemessen benachteiligt. Freistellung bleibt im konkreten Fall möglich - braucht aber einen tragfaehigen Grund (ueberwiegende schutzwuerdige Arbeitgeberinteressen). Die pauschale Vorratsklausel reicht nicht. | `bag-freistellungsklausel-unwirksam` (fachanwalt-arbeitsrecht) / `bag-freistellungsklausel-unwirksam-5azr10825` (arbeitsrecht) |

> Diese drei Aktenzeichen sind Sucheinstieg. Vor Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle (bundesarbeitsgericht.de, dejure.org) live verifizieren - Datum, Aktenzeichen, Randnummer, Fortgeltung. Spezial-Skills oben enthalten Prüfschemata, Klagebausteine und Verteidigungsmuster.

---

## Skill: `fachanwalt-arbeitsrecht-orientierung`

_Wenn es um Fachanwalt für Arbeitsrecht — Orientierung in Fachanwalt Arbeitsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Fachanwalt für Arbeitsrecht — Orientierung

## FAO-Voraussetzungen (Paragraf 10 FAO)

- Lehrgang 120 Stunden + drei Klausuren.
- 100 Fälle in den letzten drei Jahren aus dem Arbeitsrecht; davon mindestens 50 Mandate im Individualarbeitsrecht, mindestens 10 Mandate im Kollektivarbeitsrecht, mindestens 20 rechtsförmliche Verfahren.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| Individualarbeitsrecht | BGB Paragrafen 611a ff. (Arbeitsvertrag); KSchG (Kündigungsschutz); BUrlG (Urlaub); EFZG (Entgeltfortzahlung); TzBfG (Teilzeit und Befristung); NachwG (Nachweisgesetz, idF Aug. 2022); MuSchG; BEEG; ArbZG; ArbStättV |
| Kollektivarbeitsrecht | BetrVG (Betriebsverfassung); TVG (Tarifvertrag); MitbestG; DrittelbG; SprAuG |
| Diskriminierung | AGG (Paragrafen 1, 7, 15) |
| Arbeitsschutz | ArbSchG; ArbStättV; ArbMedVV |
| Insolvenz | InsO Paragrafen 113, 125 ff. |
| Verfahren | ArbGG (Arbeitsgerichtsgesetz) |
| Internationale Bezüge | Rom I-VO; AEntG; AÜG |

## Typische Mandate

- Kündigungsschutzklage (Paragraf 4 KSchG).
- Aufhebungsvertrag (Verhandlung, Sozialplan).
- Befristungskontrollklage (Paragraf 17 TzBfG).
- Sozialplan / Interessenausgleich nach Paragraf 112 BetrVG (Kollektivseite).
- Betriebsratsanhörung nach Paragraf 102 BetrVG.
- Zeugnisstreitigkeit (Paragraf 109 GewO).
- AGG-Entschädigungsklage (Paragraf 15 AGG).
- Lohn- und Gehaltsklage.
- Mobbing und Schadensersatzklage (Paragraf 280 Abs. 1 BGB iVm Schutzpflicht Paragraf 241 Abs. 2 BGB).

## Fristen (Auswahl)

- **Kündigungsschutzklage** Paragraf 4 KSchG — drei Wochen ab Zugang der schriftlichen Kündigung.
- **Befristungskontrollklage** Paragraf 17 TzBfG — drei Wochen nach vereinbartem Ende.
- **AGG-Entschädigung** Paragraf 15 Abs. 4 AGG — schriftliche Geltendmachung binnen zwei Monaten; Klagefrist Paragraf 61b ArbGG drei Monate.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Anhörung des Betriebsrats** Paragraf 102 BetrVG — eine Woche bei ordentlicher, drei Tage bei außerordentlicher Kündigung.
- **Sozialplanverhandlungen** Paragraf 112 Abs. 2, 3 BetrVG — Einigungsstelle nach Scheitern.

## Hauptgerichte

- Arbeitsgericht (ArbG) — erste Instanz, Kammern.
- Landesarbeitsgericht (LAG) — Berufungsinstanz.
- Bundesarbeitsgericht (BAG) — Revisionsinstanz, Erfurt.
- BVerfG bei Grundrechtsfragen.
- EuGH bei unionsrechtlichen Fragen (Befristung, Arbeitszeit, Gleichbehandlung).

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Berufsverband

- Arbeitsgemeinschaft Arbeitsrecht im DAV.

## Schnittstellen

- **`arbeitsrecht`** für operative Mandatsführung, Vorlagen.
- **`kanzlei-allgemein`** für Fristen und Versand.
- **`fachanwalt-sozialrecht`** bei Schnittstellen zur Arbeitslosenversicherung und Sperrzeit.
- **`fachanwalt-insolvenz-sanierungsrecht`** bei Betriebsübergang Paragraf 613a BGB und Insolvenz.

## Aktuelle Rechtsprechung - Ueberblick wichtiger Leitentscheidungen (Stand Mai 2026)

Folgende Leitentscheidungen sind im aktuellen Plugin-Stand mit offener Quelle (dejure.org / bundesarbeitsgericht.de) belegt:

- **BAG, 23.10.2025 - 8 AZR 300/24** (Paarvergleich Equal Pay): Ein einzelner Vergleichskollege des anderen Geschlechts genuegt zur Vermutung nach Paragraf 22 AGG. Siehe Skill `fachanwalt-arbeitsrecht-bag-equal-pay-paarvergleich`.
- **BAG, 03.06.2025 - 9 AZR 104/24** (kein Urlaubsverzicht durch Prozessvergleich): Mindesturlaub waehrend laufenden Arbeitsverhaeltnisses nicht disponibel. Siehe Skill `fachanwalt-arbeitsrecht-bag-mindesturlaub-kein-verzicht`.
- **BAG, 25.03.2026 - 5 AZR 108/25** (Freistellungsklausel unwirksam): Pauschale formularmaessige Freistellungsklausel verstoesst gegen Paragraf 307 BGB. Siehe Skill `fachanwalt-arbeitsrecht-bag-freistellungsklausel-unwirksam`.
- **BAG, 01.04.2026 - 6 AZR 152/22 und 6 AZR 157/22** (Massenentlassung): Fehlerhafte oder verfruehte Massenentlassungsanzeige fuehrt zur Unwirksamkeit aller Kuendigungen. Siehe Skill `fachanwalt-arbeitsrecht-massenentlassung-17-kschg`.
- **EuGH, 30.10.2025 - C-134/24 und C-402/24** (Massenentlassung): Keine Heilung fehlender oder verfruehter Anzeige nach Kuendigungsausspruch.
- **BAG, 20.02.2025 - 8 AZR 61/24** (DSGVO-Schadensersatz): "Stoergefuehl" allein begruendet keinen Anspruch nach Art. 82 DSGVO.
- **BAG, 18.06.2025 - 7 AZR 50/24** (Befristung Betriebsratsmitglieder): Paragraf 14 Abs. 2 TzBfG anwendbar; Schadensersatz auf Folgevertrag bei Mandatsbenachteiligung.
- **BAG, 22.09.2022 - 8 AZR 4/21** (NachweisG): Schadensersatz neben Bussgeld bei Pflichtverletzung des Arbeitgebers nach NachwG.
- **BAG, 13.09.2022 - 1 ABR 22/21** (Arbeitszeiterfassung): Pflicht des Arbeitgebers zur systematischen Arbeitszeiterfassung aus Paragraf 3 Abs. 2 Nr. 1 ArbSchG.

Vor Schriftsatzverwendung jeweils Volltext und ggf. neuere Rechtsprechung in offenen Quellen (dejure.org, openjur.de, bundesarbeitsgericht.de) verifizieren.

## Paragrafenkette Kernbereiche Individualarbeitsrecht

- Paragraf 611a BGB — Arbeitsvertrag
- Paragraf 626 BGB — Außerordentliche Kündigung
- Paragrafen 1 ff. KSchG — Kündigungsschutz; Paragraf 4 KSchG — Klagefrist drei Wochen
- Paragraf 102 BetrVG — Betriebsratsanhörung
- Paragrafen 1, 3 BUrlG — Urlaubsanspruch; Paragraf 7 Abs. 3 BUrlG — Verfall
- Paragraf 14 TzBfG — Befristung; Paragraf 17 TzBfG — Kontrollklage drei Wochen

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

---

## Skill: `orientierung-mandat-fachanwaltschaft`

_Wenn es um Orientierung Mandat Fachanwaltschaft in Fachanwalt Arbeitsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Orientierung im Individualarbeitsrecht und kollektiven Arbeitsrecht für Mandate und Fachanwaltschaft nach Paragraf 10 FAO


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: KSchG; BetrVG; TzBfG; EntgTranspG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Orientierung im Individualarbeitsrecht und kollektiven Arbeitsrecht für Mandate und Fachanwaltschaft nach Paragraf 10 FAO. Anwendungsfall Kanzlei will Arbeitsrechtsmandat beurteilen oder Anwalt bereitet sich auf Fachanwaltsprüfung vor. Normen BGB Paragrafen 611a ff. KSchG BetrVG TVG BUrlG EFZG TzBfG AGG ArbGG. Prüfraster Individualarbeitsrecht Kollektivarbeitsrecht Diskriminierungsschutz Verfahren ArbGG LAG BAG verifizierbare Quellen. Output Rechtsgebietsuebersicht mit Normenhierarchie Pflichtliteratur und Mandatstriage-Hinweisen. Abgrenzung zu erstgespraech-mandatsannahme und mandat-triage-Skill.

### Fachanwalt für Arbeitsrecht — Orientierung

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Fachanwalt für Arbeitsrecht — Orientierung` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB Paragrafen 611a, 613a, 615, 623; KSchG Paragrafen 1, 4, 7; TzBfG Paragrafen 14, 15, 16; AGG Paragrafen 1, 3, 7, 15, 22; EntgTranspG Paragrafen 3, 5, 7; BUrlG Paragrafen 1, 3, 7; BetrVG Paragrafen 87, 99, 102; ArbZG; NachwG; SGB IX Paragrafen 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer Paragraf 623 BGB, Zugang nach Paragraf 130 BGB, Dreiwochenfrist Paragrafen 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## FAO-Voraussetzungen (Paragraf 10 FAO)

- Lehrgang 120 Stunden + drei Klausuren.
- 100 Fälle in den letzten drei Jahren aus dem Arbeitsrecht; davon mindestens 50 Mandate im Individualarbeitsrecht, mindestens 10 Mandate im Kollektivarbeitsrecht, mindestens 20 rechtsförmliche Verfahren.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| Individualarbeitsrecht | BGB Paragrafen 611a ff. (Arbeitsvertrag); KSchG (Kündigungsschutz); BUrlG (Urlaub); EFZG (Entgeltfortzahlung); TzBfG (Teilzeit und Befristung); NachwG (Nachweisgesetz, idF Aug. 2022); MuSchG; BEEG; ArbZG; ArbStättV |
| Kollektivarbeitsrecht | BetrVG (Betriebsverfassung); TVG (Tarifvertrag); MitbestG; DrittelbG; SprAuG |
| Diskriminierung | AGG (Paragrafen 1, 7, 15) |
| Arbeitsschutz | ArbSchG; ArbStättV; ArbMedVV |
| Insolvenz | InsO Paragrafen 113, 125 ff. |
| Verfahren | ArbGG (Arbeitsgerichtsgesetz) |
| Internationale Bezüge | Rom I-VO; AEntG; AÜG |

## Typische Mandate

- Kündigungsschutzklage (Paragraf 4 KSchG).
- Aufhebungsvertrag (Verhandlung, Sozialplan).
- Befristungskontrollklage (Paragraf 17 TzBfG).
- Sozialplan / Interessenausgleich nach Paragraf 112 BetrVG (Kollektivseite).
- Betriebsratsanhörung nach Paragraf 102 BetrVG.
- Zeugnisstreitigkeit (Paragraf 109 GewO).
- AGG-Entschädigungsklage (Paragraf 15 AGG).
- Lohn- und Gehaltsklage.
- Mobbing und Schadensersatzklage (Paragraf 280 Abs. 1 BGB iVm Schutzpflicht Paragraf 241 Abs. 2 BGB).

## Fristen (Auswahl)

- **Kündigungsschutzklage** Paragraf 4 KSchG — drei Wochen ab Zugang der schriftlichen Kündigung.
- **Befristungskontrollklage** Paragraf 17 TzBfG — drei Wochen nach vereinbartem Ende.
- **AGG-Entschädigung** Paragraf 15 Abs. 4 AGG — schriftliche Geltendmachung binnen zwei Monaten; Klagefrist Paragraf 61b ArbGG drei Monate.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Anhörung des Betriebsrats** Paragraf 102 BetrVG — eine Woche bei ordentlicher, drei Tage bei außerordentlicher Kündigung.
- **Sozialplanverhandlungen** Paragraf 112 Abs. 2, 3 BetrVG — Einigungsstelle nach Scheitern.

## Hauptgerichte

- Arbeitsgericht (ArbG) — erste Instanz, Kammern.
- Landesarbeitsgericht (LAG) — Berufungsinstanz.
- Bundesarbeitsgericht (BAG) — Revisionsinstanz, Erfurt.
- BVerfG bei Grundrechtsfragen.
- EuGH bei unionsrechtlichen Fragen (Befristung, Arbeitszeit, Gleichbehandlung).

## Berufsverband

- Arbeitsgemeinschaft Arbeitsrecht im DAV.

## Schnittstellen

- **`arbeitsrecht`** für operative Mandatsführung, Vorlagen.
- **`kanzlei-allgemein`** für Fristen und Versand.
- **`fachanwalt-sozialrecht`** bei Schnittstellen zur Arbeitslosenversicherung und Sperrzeit.
- **`fachanwalt-insolvenz-sanierungsrecht`** bei Betriebsübergang Paragraf 613a BGB und Insolvenz.

## Aktuelle Rechtsprechung - Überblick wichtiger Leitentscheidungen (Stand Mai 2026)

Folgende Leitentscheidungen sind im aktuellen Plugin-Stand mit offener Quelle (dejure.org / bundesarbeitsgericht.de) belegt:

- **BAG, 23.10.2025 - 8 AZR 300/24** (Paarvergleich Equal Pay): Ein einzelner Vergleichskollege des anderen Geschlechts genuegt zur Vermutung nach Paragraf 22 AGG. Siehe Skill `fachanwalt-arbeitsrecht-bag-equal-pay-paarvergleich`.
- **BAG, 03.06.2025 - 9 AZR 104/24** (kein Urlaubsverzicht durch Prozessvergleich): Mindesturlaub waehrend laufenden Arbeitsverhaeltnisses nicht disponibel. Siehe Skill `fachanwalt-arbeitsrecht-bag-mindesturlaub-kein-verzicht`.
- **BAG, 25.03.2026 - 5 AZR 108/25** (Freistellungsklausel unwirksam): Pauschale formularmäßige Freistellungsklausel verstoesst gegen Paragraf 307 BGB. Siehe Skill `fachanwalt-arbeitsrecht-bag-freistellungsklausel-unwirksam`.
- **BAG, 01.04.2026 - 6 AZR 152/22 und 6 AZR 157/22** (Massenentlassung): Fehlerhafte oder verfruehte Massenentlassungsanzeige fuehrt zur Unwirksamkeit aller Kuendigungen. Siehe Skill `fachanwalt-arbeitsrecht-massenentlassung-17-kschg`.
- **EuGH, 30.10.2025 - C-134/24 und C-402/24** (Massenentlassung): Keine Heilung fehlender oder verfruehter Anzeige nach Kuendigungsausspruch.
- **BAG, 20.02.2025 - 8 AZR 61/24** (DSGVO-Schadensersatz): "Stoergefuehl" allein begruendet keinen Anspruch nach Art. 82 DSGVO.
- **BAG, 18.06.2025 - 7 AZR 50/24** (Befristung Betriebsratsmitglieder): Paragraf 14 Abs. 2 TzBfG anwendbar; Schadensersatz auf Folgevertrag bei Mandatsbenachteiligung.
- **BAG, 22.09.2022 - 8 AZR 4/21** (NachweisG): Schadensersatz neben Bussgeld bei Pflichtverletzung des Arbeitgebers nach NachwG.
- **BAG, 13.09.2022 - 1 ABR 22/21** (Arbeitszeiterfassung): Pflicht des Arbeitgebers zur systematischen Arbeitszeiterfassung aus Paragraf 3 Abs. 2 Nr. 1 ArbSchG.

Vor Schriftsatzverwendung jeweils Volltext und ggf. neuere Rechtsprechung in offenen Quellen (dejure.org, openjur.de, bundesarbeitsgericht.de) verifizieren.

## Paragrafenkette Kernbereiche Individualarbeitsrecht

- Paragraf 611a BGB — Arbeitsvertrag
- Paragraf 626 BGB — Außerordentliche Kündigung
- Paragrafen 1 ff. KSchG — Kündigungsschutz; Paragraf 4 KSchG — Klagefrist drei Wochen
- Paragraf 102 BetrVG — Betriebsratsanhörung
- Paragrafen 1, 3 BUrlG — Urlaubsanspruch; Paragraf 7 Abs. 3 BUrlG — Verfall
- Paragraf 14 TzBfG — Befristung; Paragraf 17 TzBfG — Kontrollklage drei Wochen

---

## Skill: `erstgespraech-mandatsannahme`

_Wenn es um Erstgespraech Mandatsannahme in Fachanwalt Arbeitsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Strukturierter Erstgespraechsleitfaden für Individual- und kollektives Arbeitsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen.


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: KSchG; BetrVG; TzBfG; EntgTranspG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Strukturierter Erstgespraechsleitfaden für Individual- und kollektives Arbeitsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen.

### Erstgespraech und Mandatsannahme im Individual- und kollektives Arbeitsrecht

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Erstgespraech und Mandatsannahme im Individual- und kollektives Arbeitsrecht` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB Paragrafen 611a, 613a, 615, 623; KSchG Paragrafen 1, 4, 7; TzBfG Paragrafen 14, 15, 16; AGG Paragrafen 1, 3, 7, 15, 22; EntgTranspG Paragrafen 3, 5, 7; BUrlG Paragrafen 1, 3, 7; BetrVG Paragrafen 87, 99, 102; ArbZG; NachwG; SGB IX Paragrafen 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer Paragraf 623 BGB, Zugang nach Paragraf 130 BGB, Dreiwochenfrist Paragrafen 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Wann dieser Arbeitsgang greift

- Neue Anfrage aus dem Bereich Individual- und kollektives Arbeitsrecht (Telefon, Mail, Empfehlung, Walk-in).
- Mandantin oder Mandant beschreibt Sachverhalt unstrukturiert; viele Anlagen ohne System.
- Vor jeder weiteren fachlichen Bearbeitung: erst Annahme klären, Konflikt- und GwG-Prüfung, Vollmacht, Streitwert/Vereinbarung, Fristen.

## Phasen des Erstgespraechs

### 1. Aufnahme der Konstellation (10-15 Min.)

Standard-Fragenraster für Individual- und kollektives Arbeitsrecht:

- Beteiligte (Vor-/Nachname, Geburtsdatum, Anschrift, Rolle: Klägerin/Beklagter, Antragsteller, Beschuldigter)
- Konflikt-Kern in einem Satz ("Was ist Ihr Ziel?")
- Konkrete fachliche Stossrichtung: Kuendigung, Abmahnung, Befristung, Aufhebungsvertrag, Lohn, Urlaub, BR-Sachen
- Bisherige Korrespondenz (Bescheide, Schreiben der Gegenseite, anwaltliche Vertretung der Gegenseite?)
- **Fristenscreening sofort:** anstehende Klage-/Widerspruchs-/Einspruchsfristen aus den vorgelegten Schreiben (z.B. Kuendigungsschutzklage, Befristungskontrollklage, Zahlungsklage Arbeitsgericht). Frist-Alarm an die Vorbereitung weitergeben.

### 2. Konflikt-Prüfung und GwG-Check (5 Min.)

- Konflikt-Check über Mandantsystem: Gegnerin, Streitgegenstand, frueherer Mandant?
- GwG-Identifizierung: amtlicher Lichtbildausweis (Ausweisscan), bei juristischer Person Handelsregister-/Transparenzregister-Auszug, ggf. wirtschaftlich Berechtigte/n.
- Risikobewertung (niedrig/mittel/hoch) abhaengig von Mandatscharakter, Bargeld, Auslandsbezug.
- Doku im Mandatsbogen (Pflicht nach Paragrafen 10 ff. GwG i.V.m. Paragraf 2 Abs. 1 Nr. 10 GwG für RA-Mandate).

### 3. Vollmacht und Schweigepflichtentbindung

- Allgemeine Prozess-/Aussenvollmacht (BORA, ZPO, FamFG, je nach Fachgebiet).
- Spezielle Vollmachten: ggf. Akteneinsicht Strafakte, KV-Abrechnungsdaten, Sozialdaten (Schweigepflichtentbindung gegenueber Krankenkasse, Arzt, Behörde).
- Bei Eheleuten/GbR/GmbH: einzelvollmachtgebende Person und Vertretungsmacht klären.

### 4. Streitwert und Gebührenvereinbarung

Standard-Streitwerte im Bereich Individual- und kollektives Arbeitsrecht:

- Skizze: Streitwert grob abschaetzen (z.B. Hauptforderung, ggf. + Zinsen, Nebenforderungen).
- RVG-Pauschalrechnung (Berechnungstool im Plugin) oder Stundenhonorarvereinbarung.
- Beratungshilfe-/Prozesskostenhilfe-Antrag prüfen, wenn wirtschaftlich angezeigt.
- Vorschussanforderung nach Paragraf 9 RVG.

### 5. Strategie-Erstskizze

Drei Weichen am Ende des Erstgespraechs:

- **Mandat annehmen:** vollstaendig (Prüfung + Schriftsatz) oder begrenzt (nur Prüfung/Gutachten).
- **Verweisen:** wenn Spezialgebiet ausserhalb der Fachanwaltschaft, oertlich unzuständig oder Konflikt.
- **Ablehnen:** offensichtlich aussichtslos, GwG-Hit, Bauchgefuehl-Vorsicht.

## Pflicht-Output am Ende

1. **Mandatsbogen** mit Beteiligten, Konflikt-Check, GwG-Status, Streitwert.
2. **Frist-Liste** (Sofortfristen, Verjährung, Ausschlussfristen, Beweisanforderungs-Fristen).
3. **Anlagenverzeichnis** des uebergebenen Datenraums (Stand erstes Sortieren).
4. **Naechster-Schritt-Plan:** binnen 24/48/72 h, Owner, Output.
5. **Honorarvereinbarung** unterschrieben oder Vorbehalt notiert.

## Relevante Rechtsgrundlagen und Standards

- BORA, BRAO, FAO für Fachanwaltschaft Individual- und kollektives Arbeitsrecht.
- GwG, GwGMeldV, Identifizierungsleitfaden BRAK.
- KSchG, TzBfG, BetrVG, BGB, EFZG, BUrlG, AGG, NachwG (für fachliche Erstpruefung).
- DSGVO und BDSG für den Umgang mit Mandantendaten (Art. 6 DSGVO als Rechtsgrundlage, Art. 9 ggf. Gesundheitsdaten).

## Typische Fehler im Erstgespraech

- Frist uebersehen, weil Mandantin sie nicht selber genannt hat (immer aus jedem Schreiben Frist herausziehen).
- Konflikt-Check nur nach Personennamen, nicht nach Sachzusammenhang (gleiche Liegenschaft, gleicher Sachverhalt).
- Vollmachtsumfang unklar -> später Streit mit Mandantin über Befugnisse.
- Honorarvereinbarung muendlich -> Beweisnot bei Streitwert-/Honorar-Streit.
- GwG: kein Lichtbildausweis erfasst, kein Aktenvermerk über Risikobewertung.

## Praxis-Checkliste

- [ ] Personalien und Rolle aller Beteiligten erfasst
- [ ] Konflikt-Check durchgefuehrt
- [ ] GwG: Identifizierung + Risikobewertung notiert
- [ ] Allgemeine Vollmacht unterschrieben
- [ ] Speziale Vollmacht / Entbindungserklaerung (wo noetig) unterschrieben
- [ ] Streitwert geschaetzt
- [ ] Honorarvereinbarung unterschrieben oder ausdruecklich auf RVG verwiesen
- [ ] Fristenliste angelegt und in Kalender eingetragen
- [ ] Mandatsbogen vollstaendig
- [ ] Naechster-Schritt-Plan dem Mandanten kommuniziert (E-Mail-Zusammenfassung)

## Konkrete Praxis-Konstellationen

### Konstellation A: Eilbeduerftigkeit

Mandantin kommt am Donnerstag, Frist laeuft am Montag (Klage- oder Widerspruchsfrist im Bereich Individual- und kollektives Arbeitsrecht). Handlungs-Sequenz:

1. Sofort-Vollmacht und Sofort-Akteneinsicht (per beA, ELSTER, Behördenportal).
2. Antrag auf Wiedereinsetzung (Paragraf 233 ZPO, Paragraf 60 VwGO, Paragraf 110 AO) als Reserve dokumentieren.
3. Spaeteste-Stunde-Versand-Plan: beA bevorzugt, mit qualifizierter Signatur und Empfangsbekenntnis.
4. Honorarvereinbarung NICHT auf Eilzuschlag verzichten - aber transparent kommunizieren.

### Konstellation B: Komplexer Sachverhalt, Datenraum unsortiert

Mandant uebergibt 200+ Dateien (PDF-Scans, E-Mails, Excel-Listen). Vor jeder fachlichen Bewertung:

1. Datenraum-Index in Excel: Datum, Absender, Empfaenger, Aktenzeichen, kurze Inhaltszeile.
2. Chronologischer Verlauf als Zeitstrahl - Spielraum für Verjährungs- und Ausschlussfristen identifizieren.
3. Loecher im Datenraum gezielt anfordern (Mandantenfragen-Katalog).

### Konstellation C: Interessenkonflikt-Naehe

Frueheres Mandat mit derselben Gegnerin oder gleichem Sachzusammenhang. Prüfung:

1. Paragraf 43a Abs. 4 BRAO und Paragraf 3 BORA - Sachzusammenhang, nicht nur Personenidentitaet.
2. Einwilligung beider Mandanten in Textform (mit konkreter Beschreibung).
3. Bei Zweifel: Mandat ablehnen und an Kanzleikollegium ueberweisen.

## Mandanten-Erwartungsmanagement

- Realistische Erfolgs- und Kostenprognose (nicht "Wir gewinnen sicher").
- Verfahrensdauer im Bereich Individual- und kollektives Arbeitsrecht: Erfahrungswerte nach Instanz.
- Vergleichschance vs. streitiges Urteil als Option offen halten.
- Schriftliche Zusammenfassung des Erstgespraechs binnen 48 h.

## Honorarvereinbarung - Best Practices

- RVG-Basis als Default, Stundenhonorar nur mit gesondertem Hinweis nach Paragraf 3a RVG.
- Erfolgshonorar nur in den engen Grenzen Paragraf 4a RVG.
- Vorschuss in Höhe der voraussichtlichen 1. Instanz.
- Klarstellung: Auslagen-Pauschale, USt, Reisekosten, Sachverstaendigenkosten gesondert.
- Bei PKH/Beratungshilfe-Mandant: schriftliche Belehrung, dass eigene Beitraege möglich sind.

## Mandatsbogen-Muster (Mindestinhalt)

- Mandant (Name, Geburtsdatum, Anschrift, Telefon, E-Mail)
- Gegner (Name, Anschrift, ggf. anwaltliche Vertretung)
- Kurzbeschreibung Sachverhalt (5-10 Saetze)
- Ziel des Mandats (eine Zeile)
- Strittige Fragen (bullet)
- Geprueft: Konflikt - GwG - Vollmacht
- Streitwert (Schaetzung)
- Honorarvereinbarung (RVG/Stunde/Pauschale)
- Frist-Liste
- Aktenanlage Datum
- Naechster-Schritt

## Audit-Hinweis (27.05.2026)

Im Halluzinations-Audit 2026-05-27 wurden in diesem Skill folgende
Aktenzeichen geprueft und korrigiert:

## Cross-Refs

- `vergleichsverhandlung-strategie` (im selben Plugin) für den Fall, dass aussergerichtliche Loesung angestrebt wird.
- `schriftsatzkern-substantiierung` (im selben Plugin) für den Schriftsatzaufbau, wenn Klage/Widerspruch eingereicht wird.
- Kanzlei-Allgemein-Plugin `kanzlei-allgemein` für Konflikt-, GwG- und PEP-Prüfroutinen.

## Aktuelle Rechtsprechung (Stand Mai 2026)

Im Plugin verifizierte Leitentscheidungen mit offener Quelle (dejure.org / bundesarbeitsgericht.de):

- BAG, 23.10.2025 - 8 AZR 300/24 (Paarvergleich Equal Pay)
- BAG, 03.06.2025 - 9 AZR 104/24 (Mindesturlaub kein Verzicht)
- BAG, 25.03.2026 - 5 AZR 108/25 (Freistellungsklausel unwirksam)
- BAG, 01.04.2026 - 6 AZR 152/22 + 157/22 (Massenentlassung)
- EuGH, 30.10.2025 - C-134/24 + C-402/24 (Massenentlassung)

Weitere Entscheidungen siehe Themenskills. Im Erstgespraech keine Rechtsprechung aus Modellwissen zitieren; bei Bedarf vor Verwendung in dejure.org / openjur.de / bundesarbeitsgericht.de verifizieren.

## Paragrafenkette Fristen Arbeitsrecht

- **Paragraf 4 KSchG** — Klage auf Kündigungsschutz: drei Wochen ab Zugang der schriftlichen Kündigung
- **Paragraf 17 TzBfG** — Befristungskontrollklage: drei Wochen ab vereinbartem Ende
- **Paragraf 15 Abs. 4 AGG** — Geltendmachung AGG-Entschädigung schriftlich innerhalb zwei Monate
- **Paragraf 61b ArbGG** — Klage auf AGG-Entschädigung: drei Monate ab schriftlicher Geltendmachung
- **Paragraf 102 Abs. 2 BetrVG** — Betriebsratsanhörung: eine Woche ordentlich, drei Tage außerordentlich

## Triage — Erstgespräch-Einstieg

1. Liegt eine sofortige Klagefrist vor? (Kündigung → Paragraf 4 KSchG, Befristungsende → Paragraf 17 TzBfG)
2. GwG-Identifizierung abgeschlossen? (Lichtbildausweis, bei juristischer Person Handelsregister)
3. Interessenkonflikt geprüft? (Paragraf 43a Abs. 4 BRAO)
4. Honorarvereinbarung: RVG oder Stundensatz? Vorschuss anfordern!
5. Welche weiteren Fristen sind aus den vorgelegten Unterlagen erkennbar?

---

## Skill: `erstpruefung-und-mandatsziel`

_Wenn es um Erstpruefung Und Mandatsziel in Fachanwalt Arbeitsrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Fachanwalt Erstprüfung und Mandatsziel: systematische Erstaufnahme im arbeitsrechtlichen Mandat, Rollenklärung, Zielformulierung, Interessenkonflikt-Check, Mandatsumfang, Kostenhinweis RVG, erste Risikoampel.


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: KSchG; BetrVG; TzBfG; EntgTranspG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Fachanwalt Erstprüfung und Mandatsziel: systematische Erstaufnahme im arbeitsrechtlichen Mandat, Rollenklärung, Zielformulierung, Interessenkonflikt-Check, Mandatsumfang, Kostenhinweis RVG, erste Risikoampel.

### Spezial: Fachanwalt Erstprüfung und Mandatsziel

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Spezial: Fachanwalt Erstprüfung und Mandatsziel` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB Paragrafen 611a, 613a, 615, 623; KSchG Paragrafen 1, 4, 7; TzBfG Paragrafen 14, 15, 16; AGG Paragrafen 1, 3, 7, 15, 22; EntgTranspG Paragrafen 3, 5, 7; BUrlG Paragrafen 1, 3, 7; BetrVG Paragrafen 87, 99, 102; ArbZG; NachwG; SGB IX Paragrafen 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer Paragraf 623 BGB, Zugang nach Paragraf 130 BGB, Dreiwochenfrist Paragrafen 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Einstieg
Wenn ein Mandat vorliegt oder angeboten wird, folgende Punkte klären:

1. **Wer ist der Mandant?** Name, Stellung (Arbeitnehmer, Arbeitgeber, Betriebsrat, Gewerkschaft)?
2. **Was ist das Kernproblem?** Kündigung, Vergütung, Diskriminierung, Betriebsverfassung, Vertragsgestaltung?
3. **Gibt es laufende Fristen?** 3-Wochen-Frist Paragraf 4 KSchG, Paragraf 17 TzBfG, AGG-Frist Paragraf 15 Abs. 4 AGG?
4. **Interessenkonflikt?** Vertritt die Kanzlei oder die Fachanwältin/den Fachanwalt bereits die Gegenseite?
5. **Was ist das Ziel des Mandanten?** Bestandsschutz, Abfindung, Schadensersatz, Vertragsänderung?

## Phase 1: Interessenkonflikt-Prüfung (Paragraf 43a BRAO, Paragraf 3 BORA)

### Prüfpflicht
Vor jeder Mandatsannahme muss geprüft werden:
- Vertritt die Kanzlei die Gegenseite in derselben oder einer verwandten Angelegenheit?
- Hat ein Anwalt der Kanzlei früher die Gegenseite beraten?
- Gibt es sonstige Interessenkollisionen (Eigeninteressen, familiäre Verbindungen)?

**Rechtsfolge Verstoß:** Paragraf 356 StGB (Parteiverrat); berufsrechtliche Sanktionen; Anwaltsvertrag nichtig.

### Dokumentation
Interessenkonflikt-Check in der Kanzleisoftware; schriftliche Bestätigung der Prüfung in der Akte.

## Phase 2: Sachverhaltsaufnahme

### Grunddaten

| Feld | Inhalt |
|---|---|
| Mandantenname | |
| Arbeitgeber/Arbeitnehmer | |
| Betriebsname und -ort | |
| Branche | |
| Betriebsgröße (ca.) | |
| Beginn Arbeitsverhältnis | |
| Letzte Vergütung (brutto) | |
| Besonderer Kündigungsschutz? | |
| Besteht Betriebsrat? | |
| Kündigung erhalten? Datum? | |

### Fristenüberblick (sofort beim Erstgespräch)
- Liegt eine Kündigung vor? → Paragraf 4 KSchG-Frist berechnen
- Ist das Befristungsende abgelaufen? → Paragraf 17 TzBfG-Frist
- Diskriminierungsfall? → Paragraf 15 Abs. 4 AGG-Frist (2 Monate)

## Phase 3: Mandatsziel und Interessenlage

### Mandatsziel klären — vier Grundoptionen

| Option | Beschreibung | Typisch wenn |
|---|---|---|
| Bestandsschutz | Fortsetzung des Arbeitsverhältnisses erzwingen | Mandant will unbedingt weiterarbeiten |
| Abfindung | Hohe Abfindung aushandeln; schnelle Einigung | Neue Stelle in Aussicht; wirtschaftliches Interesse |
| Beides prüfen lassen | Strategie offen halten; im Gütermin entscheiden | Lage noch unklar |
| Schadensersatz/Entschädigung | AGG-Ansprüche, EntgTranspG, sonstige Ansprüche | Diskriminierung, Mobbing, verweigerte Gehaltserhöhung |

### Fragen zur Interessenlage
- Will der Mandant nach Verfahrensabschluss im Betrieb bleiben, oder lieber weg?
- Wie ist die finanzielle Situation? Kann er/sie sich eine Prozessdauer von 6–18 Monaten leisten?
- Besteht Rechtschutzversicherung? (Falls ja: Deckungsanfrage stellen)
- Wie ist das Verhältnis zum Arbeitgeber/Vorgesetzten — sachlich oder eskaliert?

## Phase 4: Erste Risikoampel

### Grün — Starke Position
- Formfehler bei der Kündigung (kein Original, fehlende Vollmacht, keine BR-Anhörung)
- Sonderkündigungsschutz (Schwangerschaft, Elternzeit, Betriebsrat) ohne behördliche Zustimmung
- Massenentlassungsanzeige fehlerhaft (post-BAG 6 AZR 152/22)
- Befristungsabrede nicht schriftlich oder nach Dienstantritt unterzeichnet

### Gelb — Mittlere Lage
- KSchG anwendbar; Kündigung hat Angriffspunkte, aber Ausgang unsicher
- Sozialauswahl ist anfechtbar, aber dokumentiert
- Sachgrundbefristung ist schwach, aber nicht offensichtlich unwirksam

### Rot — Schwache Position
- KSchG nicht anwendbar (Betriebsgröße unter Schwelle, kurze Betriebszugehörigkeit)
- Kündigung formal korrekt; Kündigungsgrund stark (schweres Fehlverhalten mit Beweisen)
- Klagefrist bereits abgelaufen; Paragraf 7 KSchG-Fiktion

## Phase 5: Mandatsumfang und Kostenhinweis

### RVG-Werte im Arbeitsrecht
- Streitwert Kündigungsschutzklage: Paragraf 42 Abs. 2 GKG = 1 Vierteljahresverdienst
- Abfindungsvergleich: Streitwert kann höher sein (abhängig von Vergleichswert)
- Beratungsgebühr: nach RVG Paragraf 34 frei vereinbar oder nach Stundensatz

### Kostenhinweis-Pflicht (Paragraf 49b BRAO, Paragraf 3a RVG)
Vor Mandatsannahme: Hinweis auf voraussichtliche Kosten; Vergütungsvereinbarung schriftlich wenn von RVG-Sätzen abgewichen wird.

### Rechtsschutzversicherung
Falls RSV vorhanden: Deckungsanfrage sofort stellen; RSV-Selbstbehalt klären; RSV kann Vergleich beeinflussen (häufig RSV-Limit für Vergleichsabfindung).

## Anschluss-Skills
- `ar-einfuehrung-mandantenanliegen` für Themen-Routing nach Erstprüfung
- `ar-kuendigungspruefung-workflow` wenn Kündigung das Kernproblem ist
- `workflow-kaltstart-und-routing` für weiteres Routing.
- Keine Steuerberatung zur steuerlichen Behandlung von Abfindungen.

---

## Skill: `fachanwalt-arbeitsrecht-bag-freistellungsklausel-unwirksam`

_Wenn es um Rechtsprechung live prüfen in Fachanwalt Arbeitsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Fachanwalt Arbeitsrecht Bag Freistellungsklausel Unwirksam; Arbeitsfeld: Fachanwalt Arbeitsrecht._

# Rechtsprechung live prüfen

## Kaltstart-Rückfragen

1. **Liegt eine schriftliche Kündigung vor?** — Datum und Zugangstag; Freistellung parallel oder erst danach erklärt?
2. **Welchen Wortlaut hat die Freistellungsklausel im Arbeitsvertrag?** — Pauschale Klausel ("nach Kündigung freigestellt") versus konkrete Begründung im Einzelfall.
3. **Hat der Arbeitgeber zusätzlich zum Klausel-Verweis einen konkreten Grund für die Freistellung genannt?** — Geheimhaltung, Konkurrenz, Vertrauensverlust, Betriebsfrieden — nur diese tragen.
4. **Will die Mandantin tatsächlich weiterarbeiten?** — Oder ist der Beschäftigungsanspruch nur Verhandlungsmasse für den Vergleich?
5. **Wie lange läuft die Kündigungsfrist noch?** — Kurze Restlaufzeit: Weiterbeschäftigungsantrag praktisch wenig wert; Verhandlungshebel im Vergleich umso stärker.
6. **Ist Annahmeverzug bereits eingetreten?** — Ab welchem Datum hat AG die tatsächliche Beschäftigung verweigert?
7. **Plant die Mandantin eine Wettbewerbs-Tätigkeit?** — Konkurrenzschutz-Vereinbarung im AV? Post-kontraktuelles Wettbewerbsverbot?
8. **Wurde ein Aufhebungsvertrag angeboten?** — Freistellungsklausel in Aufhebungsvertrag im Einzelfall konkret formulieren.
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Kernaussage des Urteils

Leitentscheidung: BAG, Urteil vom 25.03.2026 - 5 AZR 108/25 (Wirksamkeit einer Freistellungsklausel; Widerruf der Dienstwagennutzung).

Tragende Aussage: Eine vom Arbeitgeber vorformulierte (formularmaessige) Klausel, die diesen ohne weitere Voraussetzungen berechtigt, den Arbeitnehmer nach Ausspruch einer Kuendigung bis zum Ablauf der Kuendigungsfrist von der Arbeitsleistung unter Fortzahlung der Verguetung freizustellen, ist nach Paragraf 307 Abs. 1 Satz 1 BGB unwirksam. Der verfassungsrechtlich geschuetzte Beschaeftigungsanspruch des Arbeitnehmers ueberwiegt das pauschale Freistellungsinteresse. Eine Freistellung verlangt einen konkreten Anlasstatbestand (z.B. Geheimhaltungs-, Konkurrenz- oder Vertrauensschutz) und Interessenabwaegung im Einzelfall.

Offene Quelle: dejure.org, Vernetzung BAG 25.03.2026 - 5 AZR 108/25; BAG-Pressemitteilung "Wirksamkeit einer Freistellungsklausel - Widerruf der Dienstwagennutzung". Status: Volltext zum Stand der Bearbeitung noch nicht voll veroeffentlicht - vor Schriftsatzverwendung Volltext pruefen.

Der Beschäftigungsanspruch des Arbeitnehmers darf nur mit verifizierter Rechtsprechung begründet werden. Vor einer Ausgabe ist zu prüfen, welche Entscheidung die tragende Aussage wirklich trägt und ob sie für Freistellung nach Kündigung, AGB-Kontrolle und Annahmeverzug passt.

## Rechtsgrundlagen

| Norm | Inhalt |
|---|---|
| Paragraf 307 Abs. 1 BGB | AGB-Inhaltskontrolle: unangemessene Benachteiligung |
| Paragraf 307 Abs. 2 Nr. 1 BGB | Abweichung vom wesentlichen Grundgedanken der gesetzlichen Regelung |
| Paragraf 615 BGB | Annahmeverzug: AG schuldet Vergütung bei verweigerter Beschäftigung |
| Paragraf 611a BGB | Beschäftigungspflicht als vertragliche Hauptpflicht |
| Art. 1, 2 GG | Persönlichkeitsrecht und allgemeines Persönlichkeitsrecht als Grundlage des Beschäftigungsanspruchs |

### Leitentscheidungen

| Gericht | Aktenzeichen | Datum | Kernaussage |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Wann ist Freistellung weiterhin zulässig

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

| Freistellungsgrund | Anforderung |
|---|---|
| Geheimhaltungsbedenken | Konkreter Zugang zu schutzbedürftigen Informationen (Kundendaten, Produktentwicklung, Preisstrategien) |
| Konkurrenzsorge | Konkrete Tatsachen für geplanten Wechsel zu Mitbewerber; bloßer Branchenwechsel genügt nicht |
| Vertrauensverlust | Pflichtenverletzung, die die Kündigung trägt; schwere Loyalitätsverletzung |
| Störung Betriebsfrieden | Konkrete erhebliche Störung, dokumentiert; bloße Antipathie reicht nicht |
| Überlapping-Beschäftigung nicht möglich | Stelle bereits neu besetzt; Tätigkeiten physisch nicht mehr vorhanden |

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Anwaltliche Strategie

### Aus Arbeitnehmer-Sicht

| Konstellation | Empfehlung |
|---|---|
| Mandantin will weiterzuarbeiten (Reputation, laufende Projekte) | Beschäftigungsanspruch geltend machen; AG in Annahmeverzug setzen |
| Mandantin will nicht weiterarbeiten, aber Vergleich | Beschäftigungsanspruch als Verhandlungsmasse nutzen; höhere Abfindung fordern |
| Aufhebungsvertrag in Vorbereitung | Freistellungsklausel konkret formulieren; Einzelfall begründen |

### Aus Arbeitgeber-Sicht

| Konstellation | Empfehlung |
|---|---|
| Freistellung notwendig wegen Konkurrenz | Konkrete Tatsachen dokumentieren; Freistellung mit schriftlicher Begründung erklären |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Neue Freistellungsklausel im AV | Klausel mit offenem Tatbestand ("soweit sachlich begründeter Anlass besteht") formulieren; Inhaltskontrolle prüfen |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — widerrufliche Freistellungsklausel in Klageschrift ruegen | Ruege-Baustein nach Template unten |
| Variante A — Mandant will trotzdem Freistellung | Freistellungs-Vereinbarung mit klarer Vergaetungspflicht statt ruegen |
| Variante B — Arbeitgeber hat Klausel nicht aktiviert | Praeventivruegeung in Klageschrift aufnehmen |
| Variante C — Klausel wurde bereits aktiviert | Lohnfortzahlungsklage unverzueglich erheben |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbaustein — Beschäftigungsanspruch geltend machen

```
Die Beklagte hat das Arbeitsverhältnis am [Datum] gekündigt
und die Klägerin gleichzeitig unter Hinweis auf Paragraf [X] des
Arbeitsvertrags von der Arbeitsleistung freigestellt.

Die in Paragraf [X] enthaltene Klausel ist eine formularmaessige
Standardklausel, die den Arbeitgeber pauschal und ohne
weitere Voraussetzung zur einseitigen Freistellung
berechtigen soll. Diese Klausel ist nach der Rechtsprechung
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
unwirksam, weil sie die Klägerin unangemessen benachteiligt
im Sinne des Paragraf 307 Abs. 1 BGB.

Konkrete tragfaehige Gründe fuer eine Freistellung legt die
Beklagte nicht dar. Pauschale Hinweise genuegen nicht.

Der Beschaeftigungsanspruch der Klaegerin (BAG GS,
nach verifizierter Rechtsprechung besteht bis zum Ablauf der
Kuendigungsfrist am [Datum] fort.

Die Beklagte befindet sich seit [Datum der Freistellung]
in Annahmeverzug nach Paragraf 615 BGB.
```

## Schriftsatzbaustein — Annahmeverzug-Antrag

```
Es wird beantragt:

1. Die Beklagte wird verurteilt, die Klägerin zu
   den bisherigen Arbeitsbedingungen als [Tätigkeit]
   tatsächlich zu beschäftigen.

2. Die Beklagte wird verurteilt, an die Klägerin
   EUR [Betrag] brutto (Vergütung für den Zeitraum
   [Datum] bis [Datum]) nebst Zinsen in Höhe von
   5 Prozentpunkten über dem Basiszinssatz ab
   Fälligkeit zu zahlen.

Begründung:
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
unwirksam. Die Beklagte ist seit [Datum] in Annahme-
verzug. Die Vergütung für den Annahmeverzugszeitraum
berechnet sich wie folgt: [Monat x Brutto-Monatsgehalt].
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]


## Beweislast und Darlegungslast

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- AGB-Inhaltskontrolle prüft das Gericht von Amts wegen; keine Beweislast der Parteien.

## Prüfschema Freistellung

**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.


| Schritt | Prüfpunkt | Norm | Rechtsfolge bei Fehler |
|---|---|---|---|
| 1 | Freistellungsklausel im AV vorhanden? | Paragraf 307 BGB | Nur Einzelfall-Freistellung möglich |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| 3 | Konkreter Freistellungsgrund? (Tabelle oben) | Paragraf 307 Abs. 1 BGB | Ohne Grund: Freistellung unwirksam |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| 5 | AG in Annahmeverzug? | Paragraf 615 BGB | Vergütungspflicht trotz Freistellung |
| 6 | Wettbewerbsverbot relevant? | Paragrafen 74 ff. HGB | Bei nachvertr. Wettbewerbsverbot: Karenzentschädigung |

## Fristen

| Frist | Dauer | Rechtsgrundlage |
|---|---|---|
| Annahmeverzug | Ab Zeitpunkt der Freistellung, wenn kein Grund | Paragraf 615 BGB |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Schadensersatz bei unwirksamer Freistellung | 3 Jahre | Paragrafen 195, 199 BGB |

## Streitwert und Kosten

- **Weiterbeschäftigungsantrag**: Bruttomonatsverdienst (Paragraf 42 Abs. 2 GKG).
- **Annahmeverzug-Anspruch**: Summe der ausstehenden Vergütung.
- **Erste Instanz**: Paragraf 12a ArbGG — keine Kostenerstattung.
- **Wirtschaftlicher Hauptwert**: meist im Vergleich (Abfindungs-Erhöhung wegen Beschäftigungsanspruch).

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

| Klausel-Wortlaut | Bewertung |
|---|---|
| "Der Arbeitnehmer wird nach Kündigung freigestellt." | Unwirksam — pauschal, kein Tatbestand |
| "Bei betriebsbedingter Kündigung kann der AG freistellen." | Wahrscheinlich unwirksam — kein konkreter Anlass |
| "Freistellung erfolgt, wenn berechtigte Geheimhaltungsinteressen vorliegen." | Wirksam — konkreter offener Tatbestand |
| "Freistellung erfolgt bei konkreter Gefährdung von Geschäftsgeheimnissen." | Wirksam — hinreichend konkret |

## Anschluss-Skills

- `fachanwalt-arbeitsrecht-kuendigungsschutzklage` — parallele Kündigungsschutzklage
- `fachanwalt-arbeitsrecht-betriebsratsanhoerung` — bei Fragen zur BR-Anhörung
- `fachanwalt-arbeitsrecht-hinschg-whistleblower-repressalie` — wenn Freistellung als Repressalie

## Quellen

- BGB Paragrafen 307, 615, 611a
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

---

## Skill: `fachanwalt-arbeitsrecht-bag-mindesturlaub-kein-verzicht`

_Wenn es um Rechtsprechung live prüfen in Fachanwalt Arbeitsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Fachanwalt Arbeitsrecht Bag Mindesturlaub Kein Verzicht; Arbeitsfeld: Fachanwalt Arbeitsrecht._

# Rechtsprechung live prüfen

## Kaltstart-Rueckfragen

1. Besteht das Arbeitsverhaeltnis noch oder ist es bereits beendet?
2. Wie hoch ist der gesetzliche Mindesturlaub (24 Werktage Sechstagewoche, anteilig bei Teilzeit)?
3. Wie viele Urlaubstage sind bereits genommen worden, wie viele stehen noch offen?
1. Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
5. Geht es um Aufhebungsvertrag, Prozessvergleich oder isolierte Verzichtserklaerung?
6. Liegt Arbeitsunfaehigkeit vor, die die Urlaubsgewaehrung in natura verhindert?

## Kernaussage des Urteils

Leitentscheidung: BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (Kein Urlaubsverzicht durch Prozessvergleich).

Tragende Aussage: Im laufenden Arbeitsverhaeltnis ist ein Verzicht auf den gesetzlichen Mindesturlaub - auch in einem gerichtlichen Vergleich - unwirksam, soweit der Arbeitnehmer den Urlaub aufgrund Arbeitsunfaehigkeit oder anderer tatsaechlicher Hindernisse nicht in natura nehmen kann. Eine Klausel, wonach der gesetzliche Mindesturlaub "in natura gewaehrt" gilt, ist nach Paragraf 13 Abs. 1 Satz 3 BUrlG i.V.m. Art. 7 RL 2003/88/EG nichtig, soweit sie den gesetzlichen Mindesturlaub betrifft.

Offene Quelle: dejure.org, Vernetzung BAG 03.06.2025 - 9 AZR 104/24; BAG-Pressemitteilung "Kein Urlaubsverzicht durch Prozessvergleich".

Erst mit Beendigung des Arbeitsverhaeltnisses entsteht der Anspruch auf Urlaubsabgeltung in Geld (Paragraf 7 Absatz 4 BUrlG). Dieser ist als reiner Geldanspruch dispositiv und kann grundsaetzlich vergleichsweise erledigt werden — allerdings nur mit klarer, konkret bezifferter Klausel.

## Konsequenz fuer Vergleiche und Aufhebungsvertraege

Die Entscheidung trifft jeden Aufhebungsvertrag und jeden Prozessvergleich. Eine pauschale Erledigungsklausel vom Typ "mit Erfuellung dieses Vergleichs sind saemtliche Anspruechte aus dem Arbeitsverhaeltnis abgegolten" ist hinsichtlich des gesetzlichen Mindesturlaubs unwirksam, soweit der Vergleich noch im bestehenden Arbeitsverhaeltnis geschlossen wird.

Die saubere Vergleichsformulierung trennt drei Schichten:
1. **Gesetzlicher Mindesturlaub** — Paragraf 3 BUrlG, unabdingbar nach Paragraf 13 Absatz 1 BUrlG.
2. **Vertraglicher Mehrurlaub** — frei verhandelbar, kann verzichtet werden.
3. **Urlaubsabgeltung nach Beendigung** — Geldanspruch, dispositiv, muss konkret beziffert sein.

## Pruefschema

| Schritt | Pruefung |
| --- | --- |
| 1 | Hoehe Mindesturlaub feststellen |
| 2 | Bereits genommene Urlaubstage abziehen |
| 3 | Resturlaubsanspruch ermitteln |
| 4 | Verfallspruefung Paragraf 7 Absatz 3 BUrlG mit Hinweispflicht des Arbeitgebers |
| 5 | Krankheit und Uebertragungsfrist pruefen |
| 6 | Vergleichsformulierung pruefen: Mindesturlaub gesondert ausgewiesen |
| 7 | Bei Aufhebungsvertrag: Freistellung in natura oder Geldabgeltung klar geregelt |
| 8 | Bei bereits geschlossenem Vergleich mit Pauschalklausel: Nachforderung moeglich |

## Empfohlene Vergleichsformulierung

Die Parteien sind sich darueber einig, dass das Arbeitsverhaeltnis zum [Datum] endet. Bis zum Beendigungstermin ist die Klaegerin unwiderruflich von der Arbeitsleistung freigestellt. Saemtliche Urlaubsansprueche, einschliesslich des gesetzlichen Mindesturlaubs nach Paragraf 3 BUrlG sowie des vertraglichen Mehrurlaubs, werden waehrend der Freistellung in natura gewaehrt und sind damit erfuellt. Sollten Urlaubsansprueche aufgrund von Arbeitsunfaehigkeit nicht in natura gewaehrt werden koennen, werden diese zum Beendigungstermin als Urlaubsabgeltung nach Paragraf 7 Absatz 4 BUrlG in Hoehe von brutto [Betrag] Euro ausgezahlt.

## Klausel-Verbote

| Formulierung | Problem |
| --- | --- |
| "Saemtliche Urlaubsansprueche sind abgegolten." | Pauschal, erfasst Mindesturlaub im laufenden Arbeitsverhaeltnis unwirksam |
| "Die Klaegerin verzichtet auf restlichen Urlaub." | Verzicht im laufenden Verhaeltnis unwirksam |
| "Urlaubsabgeltung ist mit der Abfindung abgegolten." | Keine konkrete Bezifferung, keine Trennung |

## Nachforderungsmoeglichkeit

Liegt eine pauschale Erledigungsklausel vor, kann die Mandantin den Urlaubsabgeltungsanspruch nach Paragraf 7 Absatz 4 BUrlG fuer den gesetzlichen Mindesturlaub trotz Vergleich noch geltend machen. Die Bezifferung erfolgt nach dem zuletzt bezogenen Bruttoentgelt. Verjaehrung nach Paragraf 195 BGB (drei Jahre ab Schluss des Jahres, in dem der Anspruch entstanden ist).

## Anschluss

Verbindung mit `fachanwalt-arbeitsrecht-aufhebungsvertrag-sperrzeit` fuer die Aufhebungsvertragsgestaltung und mit `vergleichsverhandlung-strategie` fuer den Prozessvergleich. Bei Klage auf Urlaubsabgeltung nach pauschalem Vergleich ergaenzend `schriftsatzkern-substantiierung` heranziehen.

## Aktuelle Rechtsprechung (Ergaenzung v14.2)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette

- Paragrafen 1, 3 BUrlG — Urlaubsanspruch (20 Werktage Mindesturlaub)
- Paragraf 7 Abs. 3 BUrlG — Übertragung und Verfall
- Paragraf 7 Abs. 4 BUrlG — Abgeltungsanspruch bei Beendigung
- Paragraf 13 Abs. 1 BUrlG — Unabdingbarkeit des Mindesturlaubs
- Paragrafen 195, 199 BGB — Verjährung

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

---

## Skill: `befristung-tzbfg`

_Wenn es um Befristungskontrolle und Befristungsgestaltung nach TzBfG für Arbeitgeber und Arbeitnehmer in Fachanwalt Arbeitsrecht geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Befristungskontrolle und Befristungsgestaltung nach TzBfG für Arbeitgeber und Arbeitnehmer


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: KSchG; BetrVG; TzBfG; EntgTranspG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Befristungskontrolle und Befristungsgestaltung nach TzBfG für Arbeitgeber und Arbeitnehmer. Anwendungsfall befristeter Arbeitsvertrag soll geprüft oder neuer Befristungsvertrag gestaltet werden. Normen Paragraf 14 TzBfG Sachgrundbefristung sachgrundlose Befristung Paragraf 14 Abs. 4 TzBfG Schriftform vor Beschäftigungsbeginn Paragraf 17 TzBfG Klagefrist drei Wochen. Prüfraster Schriftform-Zeitpunkt Sachgrund Vorbeschaeftigungsverbot Paragraf 14 Abs. 2 S. 2 BAG-Linie. Output Befristungsprüf-Protokoll oder Befristungsvertrags-Entwurf mit Klagefrist-Hinweis. Abgrenzung zu fachanwalt-arbeitsrecht-kündigungsschutzklage und fachanwalt-arbeitsrecht-betriebsratsanhoerung.

### Befristung nach TzBfG (Teilzeit- und Befristungsgesetz)

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Befristung nach TzBfG (Teilzeit- und Befristungsgesetz)` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB Paragrafen 611a, 613a, 615, 623; KSchG Paragrafen 1, 4, 7; TzBfG Paragrafen 14, 15, 16; AGG Paragrafen 1, 3, 7, 15, 22; EntgTranspG Paragrafen 3, 5, 7; BUrlG Paragrafen 1, 3, 7; BetrVG Paragrafen 87, 99, 102; ArbZG; NachwG; SGB IX Paragrafen 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer Paragraf 623 BGB, Zugang nach Paragraf 130 BGB, Dreiwochenfrist Paragrafen 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Kaltstart-Rückfragen

1. Liegt schriftlicher Arbeitsvertrag mit Befristung **vor** Beschäftigungsbeginn vor?
2. Sachgrundbefristung (Paragraf 14 Abs. 1 TzBfG) oder sachgrundlos (Paragraf 14 Abs. 2 TzBfG)?
3. Bei sachgrundloser Befristung: Vorbeschäftigung bei diesem Arbeitgeber?
4. Verlängerungen oder echte Neubefristung?
5. Wann endet die Befristung?

## Rechtsgrundlagen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Sachgrundbefristung:** Paragraf 14 Abs. 1 TzBfG, sachliche Gründe in S. 2 Nr. 1 bis 8.
- **Sachgrundlos:** Paragraf 14 Abs. 2 TzBfG — bis zu zwei Jahre, höchstens dreimalige Verlängerung in dieser Zeit.
- **Form der Befristungsabrede:** Paragraf 14 Abs. 4 TzBfG verlangt weiterhin Schriftform. Zulässig sind Papieroriginal mit eigenhändiger Unterschrift beider Parteien (Paragraf 126 BGB) oder echte qES beider Parteien (Paragraf 126a BGB). Textform, E-Mail, PDF-Scan, einfache Signatur und fortgeschrittene Signatur ohne qualifiziertes Zertifikat genügen nicht.
- **Befristungskontrollklage:** Paragraf 17 TzBfG — drei Wochen nach vereinbartem Ende; Versäumung führt zur Fiktion der Wirksamkeit (Paragraf 17 S. 2 iVm Paragraf 7 KSchG).
- **Neueinstellung Älterer:** Paragraf 14 Abs. 3 TzBfG — sachgrundlose Befristung bis fünf Jahre, wenn der Arbeitnehmer bei Beginn des befristeten Arbeitsverhältnisses das 52. Lebensjahr vollendet hat **und** unmittelbar vor Beginn des Arbeitsverhältnisses **mindestens vier Monate** beschäftigungslos war (Paragraf 138 SGB III), Transferkurzarbeitergeld bezog oder an einer Maßnahme nach SGB II/III teilgenommen hat. Mehrfachverlaengerung innerhalb der Gesamtdauer von fünf Jahren zulässig.
- **Wissenschaftszeitvertragsgesetz (WissZeitVG):** Sondergesetz für Wissenschaft.

## Sachgründe (Paragraf 14 Abs. 1 S. 2 TzBfG)

| Nr. | Sachgrund |
|---|---|
| 1 | Vorübergehender betrieblicher Bedarf |
| 2 | Befristung im Anschluss an Ausbildung/Studium zur Erleichterung des Übergangs |
| 3 | Vertretung anderer Arbeitnehmer (Krankheit, Elternzeit, Mutterschutz) |
| 4 | Eigenart der Arbeitsleistung (z. B. Künstler, Profisport) |
| 5 | Erprobung |
| 6 | In der Person des Arbeitnehmers liegende Gründe |
| 7 | Vergütung aus Haushaltsmitteln, die für eine befristete Beschäftigung bestimmt sind |
| 8 | Gerichtlicher Vergleich |

## Prüfschema

```
1. Schriftform Paragraf 14 Abs. 4 TzBfG
 - Papieroriginal mit eigenhändiger Unterschrift beider Parteien oder echte qES beider Parteien vor Beschäftigungsbeginn?
 - Bei Plattformsignatur: qualifiziertes Zertifikat, Identifizierung, Zeitstempel, Dokumentbezug und Prüfprotokoll sichern; Standard-DocuSign/Adobe-Sign ohne qES-Stufe genügt nicht.
2. Verlängerungen oder Neubefristung?
 - Verlängerung iSd Paragraf 14 Abs. 2 S. 1 Hs. 2 TzBfG ist nur die nahtlose Anschluss-Befristung ohne inhaltliche Änderung.
3. Sachgrund oder sachgrundlos?
 - Bei sachgrundlos: Vorbeschäftigung prüfen (BAG-Linie post-BVerfG).
 - Bei Sachgrund: Stichhaltigkeit der konkreten Gründe.
4. Höchstdauer
 - Paragraf 14 Abs. 2 TzBfG zwei Jahre / drei Verlängerungen.
 - Tarifvertragliche Abweichungen Paragraf 14 Abs. 2 S. 3, 4 TzBfG.
5. Klagefrist Paragraf 17 TzBfG
 - Drei Wochen ab vereinbartem Ende.
6. Folge bei Unwirksamkeit
 - Arbeitsverhältnis als unbefristet abgeschlossen.
 - Kündigung nur nach KSchG.
```

## Schreibvorlage (Befristungskontrollklage)

```
An das Arbeitsgericht [Ort]
[Anschrift] [Ort, Datum]

In dem Rechtsstreit
[Klagepartei] ./. [Beklagte]
 - wegen Befristungskontrolle -

erheben wir namens und in Vollmacht der Klagepartei

 Befristungskontrollklage

und beantragen,

1. Es wird festgestellt, dass das Arbeitsverhältnis der Parteien nicht aufgrund der Befristung im Arbeitsvertrag vom [Datum] mit Ablauf des [Datum] geendet hat, sondern auf unbestimmte Zeit fortbesteht.
2. Hilfsweise: Es wird festgestellt, dass das Arbeitsverhältnis nicht aufgrund einer auflösenden Bedingung beendet ist.
3. Die Beklagte trägt die Kosten des Rechtsstreits.

Sachverhalt: [Einstellung, Vertragsverlauf, Befristungen, Verlängerungen, ggf. Vorbeschäftigung]

Rechtliche Bewertung:
1. Klagefrist Paragraf 17 TzBfG ist gewahrt (vereinbartes Ende: [Datum]).
2. Befristung ist unwirksam, weil [Schriftformverstoß / Vorbeschäftigung / fehlender Sachgrund].
3. Folge: Arbeitsverhältnis besteht unbefristet fort.

[Anwalt, Fachanwalt für Arbeitsrecht]
```

## Übergabe

- Klagefrist Paragraf 17 TzBfG **ab vereinbartem Ende** — anders als Paragraf 4 KSchG (ab Zugang).
- Bei einvernehmlicher Verlängerung Schriftform peinlich genau wahren (Originale, Unterschriften vor Beginn).
- Zitierweise nach `zitierweise-deutsches-recht` v3.0.

## Aktuelle Rechtsprechung (Stand Mai 2026)

- **BAG, Urteil vom 18.06.2025 - 7 AZR 50/24**: Paragraf 14 Abs. 2 TzBfG ist uneingeschraenkt auf Betriebsratsmitglieder anwendbar; eine teleologische Reduktion zur Begruenstigung von Betriebsratsmitgliedern findet nicht statt. Verweigert der Arbeitgeber dem befristet beschäftigten Betriebsratsmitglied jedoch wegen des Mandats einen Folgevertrag, hat das Mitglied einen Schadensersatzanspruch gerichtet auf Abschluss des verweigerten Folgevertrags (Paragraf 78 BetrVG i.V.m. Paragraf 280 BGB). Quelle: dejure.org / luther-lawfirm.com Newsroom; vor Schriftsatzverwendung Volltextpruefung empfohlen.
- **ArbG Berlin, Urteil vom 28.09.2021 - 36 Ca 15296/20**: Elektronische Signatur ohne qES genügt Paragraf 14 Abs. 4 TzBfG nicht; die Befristung ist unwirksam und Paragraf 16 TzBfG greift.
- **LAG Berlin-Brandenburg, Urteil vom 16.03.2022 - 23 Sa 1133/21**: Eingescannte Unterschrift wahrt die Schriftform der Befristungsabrede nicht; spätere Originalunterzeichnung heilt nicht rückwirkend.
- **ArbG Gera, Urteil vom 07.03.2024 - 2 Ca 936/23**: Echte qES per DocuSign-qES kann Paragraf 14 Abs. 4 TzBfG wahren; maßgeblich ist die qualifizierte Signatur, nicht der Plattformname.
- Hinweis: Aeltere Leitentscheidungen zur sachgrundlosen Befristung (z.B. BVerfG, Beschl. vom 06.06.2018 - 1 BvL 7/14 u.a., zur Verfassungsmaessigkeit des Vorbeschaeftigungsverbots; BAG-Folgerechtsprechung) bleiben massgeblich; Aktenzeichen vor Zitat über dejure.org / openjur.de verifizieren.

## Paragrafenkette

- Paragraf 14 Abs. 1 TzBfG — Sachgrundbefristung (Nr. 1-8)
- Paragraf 14 Abs. 2 TzBfG — Sachgrundlose Befristung (max. zwei Jahre, drei Verlängerungen)
- Paragraf 14 Abs. 2 S. 2 TzBfG — Vorbeschäftigungsverbot
- Paragraf 14 Abs. 4 TzBfG i.V.m. Paragraf 126 BGB — Schriftformerfordernis
- Paragraf 126a BGB — elektronische Form nur bei echter qualifizierter elektronischer Signatur beider Parteien
- Paragraf 17 TzBfG — Befristungskontrollklage (Frist drei Wochen ab vereinbartem Ende)
- Paragraf 16 TzBfG — Rechtsfolge Unwirksamkeit: Arbeitsverhältnis gilt als unbefristet geschlossen

---

## Anwendungshinweise

1. Diesen Vollprüfung als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.
