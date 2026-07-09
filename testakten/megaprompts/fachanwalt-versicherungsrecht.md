# Vollprüfung: fachanwalt-versicherungsrecht

## Zusammensetzung

Dieser Vollprüfung enthaelt top-10 von 91 Skills des Plugins `fachanwalt-versicherungsrecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Wenn es um Anwalts-Dashboard Fachanwalt Versicherungsrecht in Fachanwalt Versicherungsrecht geht: klärt Rolle, Ziel, Fri…
2. **mandat-triage-versicherungsrecht** — Wenn es um Mandat Triage Versicherungsrecht in Fachanwalt Versicherungsrecht geht: klärt Rolle, Ziel, Frist, Unterlagen …
3. **orientierung-mandat-fachanwaltschaft** — Wenn es um Orientierung im Versicherungsvertragsrecht für Mandate und Fachanwaltschaft nach FAO in Fachanwalt Versicheru…
4. **fachanwalt-versicherungsrecht-orientierung** — Wenn es um Fachanwalt für Versicherungsrecht — Orientierung in Fachanwalt Versicherungsrecht geht: prüft Frist, Form, Zu…
5. **erstgespraech-mandatsannahme** — Wenn es um Erstgespraech Mandatsannahme in Fachanwalt Versicherungsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsw…
6. **erstpruefung-und-mandatsziel** — Wenn es um Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel in Fachanwalt Versicherungsrecht geht: klärt Rolle, Zi…
7. **fachanwalt-versicherungsrecht-deckungsklage** — Wenn es um Deckungsklage in Fachanwalt Versicherungsrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Be…
8. **deckungsklage** — Wenn es um Deckungsklage in Fachanwalt Versicherungsrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Be…
9. **versr-bafin-ombudsmann-aufsichtsbeschwerde** — Wenn es um BaFin-Beschwerde, Versicherungsombudsmann, PKV-Ombudsmann und Klage taktisch wählen. in Fachanwalt Versicheru…
10. **klage-versicherer-strategie** — Wenn es um Klagestrategie gegen Versicherer nach erfolgloser außergerichtlicher Korrespondenz in Fachanwalt Versicherung…

---

## Skill: `einstieg-routing`

_Wenn es um Anwalts-Dashboard Fachanwalt Versicherungsrecht in Fachanwalt Versicherungsrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Anwalts-Dashboard Fachanwalt Versicherungsrecht

> Leistungsablehnung, BU, D&O, Rechtsschutz, Obliegenheiten — Bedingungen prüfen, Obliegenheit prüfen, Beweislast verteilen.
>
> Sie sehen unten die Sofort-Triage. Keine Rückfragen, bis die Tabelle steht. Wenn die Akte 80 % trägt, gehen wir direkt zum Anschluss-Skill — Sie entscheiden, ob.

## Sofort-Triage

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
| --- | --- | --- |
| Rolle | Wen vertrete ich? (Mandant · Gegenseite · Mehrere) | Mandantenmail, Vertretungsbestellung |
| Verfahrensstand | Vorprozessual · außergerichtlich · Klage · Rechtsmittel · Vollstreckung | Vorhandene Schriftsätze, Eingangsstempel |
| Eilfrist | **§ 12 VVG: 1 Monat** (a. F.) ist überholt; Klagefrist gibt es nicht mehr. Aber: § 195 BGB Verjährung 3 Jahre. § 28 IV VVG: Obliegenheitsverletzung — Belehrungspflicht des Versicherers. § 19 VVG: Anzeigepflicht vorvertraglich; Rücktritt 1 Monat ab Kenntnis. § 14 VVG: Fälligkeit nach Erhebung der nötigen Erhebungen. | Frist aus Zugangs-/Kenntnisdatum berechnen |
| Hauptanspruch | Versicherungsleistung aus jeweiligem Vertrag (BU, D&O, RS, Kasko, Haftpflicht, KH); §§ 1, 100, 115 VVG; § 86 VVG Regress; § 28 VVG Obliegenheitsverletzung; § 19 VVG Anzeigepflicht; § 215 VVG Gerichtsstand. | Sachverhaltsabgleich mit Tatbestandsmerkmalen |
| Zuständigkeit | § 215 VVG: Wohnsitz Versicherungsnehmer (zwingend für Verbraucher). Sonst §§ 12, 17 ZPO. Bei BU/PKV häufig LG (Streitwert). | Gesetz, Vertrag, Gerichtsstandsklausel |

## Risiko-Ampel

- **Frist:** 🟠 Verjährung 3 Jahre ab Kenntnis (§ 199 BGB). 🔴 D&O Claims-made: Eintrittsdatum innerhalb Versicherungsperiode — Melde-Obliegenheit!
- **Beweislage:** 🔴 Obliegenheit § 28 VVG: Belehrungserfordernis und Kausalitätsgegenbeweis. 🟠 Anzeigepflicht § 19 VVG: Vorvertragliche Fragen Wortlaut konkret abgleichen.
- **Wirtschaftlich:** 🔴 BU-Anerkennung: Rückwirkung der Leistungspflicht bei verspäteter Anerkenntnis. 🟠 RS: Stichentscheid-/Schiedsgutachten.

## Anschluss-Skills (Router)

| Wenn der Fall trägt … | dann Skill | Erwartung |
| --- | --- | --- |
| **BU-Leistung verweigert** | `versr-bu-leistungspruefung-spezial` | Definition Beruf, Prognose 6 Monate, Verweisung, Anerkenntnisstrategie |
| D&O-Anspruch / Claims-made | `versr-d-und-o-spezialfall` | Versicherungsfall-Definition, Anzeigepflicht, Verteidigungskosten |
| Rechtsschutzdeckung verweigert | `versr-rechtsschutz-deckungsklage-spezial` | Deckungsklage § 3 ARB, Stichentscheid, vorvertraglich |
| Obliegenheitsverletzung Vorwurf | `versr-obliegenheitsverletzung-praxis` | Belehrungserfordernis § 28 IV VVG, Kausalitätsgegenbeweis |
| Anzeigepflicht § 19 VVG / Rücktritt | `versr-vvg-anzeigepflicht-19-arglist` | Frage-/Fragebogenklarheit, Arglist, Rücktritt 1 Monat |

## Norm-Radar (live verifizieren)

- **§ 1 VVG** — Hauptleistung des Versicherers
- **§ 19 VVG** — vorvertragliche Anzeigepflicht; Rücktritt
- **§ 28 VVG** — Obliegenheitsverletzung; Belehrungserfordernis
- **§ 100 VVG** — Haftpflichtversicherung: Versicherungsschutz
- **§ 115 VVG** — Direktanspruch gegen KH-Versicherer
- **§ 215 VVG** — Gerichtsstand am Wohnsitz VN

## Genau eine Rückfrage (nur wenn nötig)

> Welche **Sparte** (BU · D&O · KH/Haftpflicht · RS · Sachversicherung) — und welcher **Streitpunkt**: Deckung, Obliegenheit, Anzeigepflicht oder Höhe?

Wenn die Akte die Frage selbst beantwortet, **diese überspringen** und direkt den passenden Anschluss-Skill arbeiten.

## Leitentscheidungs-Anker (Such-Wegweiser, keine fertigen Zitate)

- **BU-Anerkenntnis / Nachprüfung** — BGH IV. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Anzeigepflicht § 19 VVG; Arglistanfechtung** — BGH IV. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Obliegenheitsverletzung § 28 VVG; Belehrungserfordernis Abs. 4** — BGH IV. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **D&O; Versicherungsfall (Claims-made)** — BGH IV. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`

> Diese Anker sind Sucheinstieg. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle prüfen und Datum, Aktenzeichen, Randnummer abklären. Kuratierte Anker-Sammlung in `references/leitentscheidungen-anker.md`.

## Hinweis

Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Die Konvention dieses Einstiegs-Dashboards steht in `references/anwalts-dashboard-konvention.md`.

---

## Skill: `mandat-triage-versicherungsrecht`

_Wenn es um Mandat Triage Versicherungsrecht in Fachanwalt Versicherungsrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Strukturierte Eingangs-Abfrage für versicherungsrechtliche Mandate mit Fristen-Sofort-Check


## Direktstart: lesen, entscheiden, liefern

Beginne nicht mit einem Fragenkatalog. Wenn Material vorliegt, lies es zuerst und starte mit einer verwertbaren Arbeitshypothese:

- Frist oder Sofortrisiko.
- erkannte Rolle, Zielrichtung und Verfahrensstand.
- tragende Tatsachen aus dem Material.
- bester nächster Arbeitsschritt mit direkt nutzbarem Output.

Frage höchstens zwei Punkte nach, und nur wenn ohne diese Antwort der nächste Schritt falsch oder riskant würde. Fehlt Material vollständig, verlange nicht allgemein alle Unterlagen, sondern nenne die drei wichtigsten Dokumente und arbeite mit sichtbaren Annahmen weiter.

Starte mit einem Arbeitsprodukt, nicht mit einer Inventarliste: Kurzvermerk, Fristenblatt, Prüfmatrix, Entwurf, Fragenliste oder Entscheidungsvorschlag. Routing ist nur Mittel zum Zweck. Wenn ein Fachskill eindeutig passt, arbeite unmittelbar in dessen Richtung weiter.

Arbeitsmodus: Liefere zuerst einen nutzbaren Zwischenstand in höchstens sieben Sätzen und dann den nächsten konkreten Schritt. Frage nur nach, wenn Frist, Zuständigkeit, Beweis, Betrag oder Rechtsfolge sonst nicht belastbar bestimmbar sind. Tabellen nur für Fristen, Belege, Beträge, Varianten oder Streitstoff.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: SGB V §§ 27, 39, 92, 109, 137, 295, 301, RisikoStruktAusglV, SGB IV, SGB X, SGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Strukturierte Eingangs-Abfrage für versicherungsrechtliche Mandate mit Fristen-Sofort-Check. Anwendungsfall neues Versicherungsmandat geht ein und muss schnell triagiert werden. Normen § 195 BGB Verjährung drei Jahre §§ 12 14 VVG Fälligkeit Schadensmeldung AVB-Klagefristen. Prüfraster Sparte Ereignis Stichtag Deckungsablehnung Höhe Frist-Sofort-Check Eskalation bei BU-Ablehnung oder lebensbedrohlichen Krankheitskosten. Output Triage-Ergebnis mit Routing zu deckungsanfrage-prüfen und Fristen-Eskalationshinweis. Abgrenzung zu deckungsanfrage-prüfen und erstgespraech-mandatsannahme.

### Mandat-Triage Versicherungsrecht

## Ablauf — sieben Fragen

### Frage 1 — Versicherungsnehmer oder Anspruchsteller?

- Versicherungsnehmer gegen eigene Versicherung (Erstrisikomandant)
- Geschädigter gegen Haftpflichtversicherer (Direktanspruch § 115 VVG)
- Versicherer als Mandant (Deckungsklage)
- Vermittler-Haftung

### Frage 2 — Sparte?

- KFZ-Vollkasko / Teilkasko / Haftpflicht
- Privathaftpflicht
- Hausrat / Gebäude
- Berufshaftpflicht
- Lebensversicherung (Erlebensfall Todesfall)
- Berufsunfähigkeit BU
- Krankenversicherung gesetzlich / privat
- Krankentagegeld
- Pflegeversicherung
- Rechtsschutz
- Insassenunfallversicherung
- Rentenversicherung (privat)
- Industrieversicherung Sonder-Industriedeckungen
- D&O Direktoren- und Manager-Haftpflicht
- Cyber-Versicherung

### Frage 3 — Akute Eilbedürftigkeit?

- BU-Ablehnung — kein Einkommen drohend
- Krankenversicherung weigert lebenswichtige Behandlung
- Hausrat-Brand kein Vorschuss
- Gewerbe-Betriebsunterbrechung
- Rechtsschutz-Deckungsablehnung mit drohender Verjährung Hauptverfahren

### Frage 4 — Versicherungsfall genau?

- Datum Ereignis
- Schadens-Höhe geschätzt
- Anzeige beim Versicherer Datum
- Bisherige Reaktion (Ablehnung Stillschweigen Teilzahlung)

### Frage 5 — Bedingungswerk?

- Police vorhanden?
- AVB welche Fassung?
- Tarif konkret bezeichnet?
- Risikofragebogen beim Vertragsschluss vorhanden?
- Versicherungsbeginn — technisch / formell

### Frage 6 — Frist?

- **Verjährung Versicherungsleistung** drei Jahre § 195 BGB ab Schluss des Jahres der Anspruchsentstehung und Kenntnis (§ 199 BGB)
- **AVB-Klagefrist** früher § 12 Abs. 3 VVG sechs Monate — seit VVG-Reform 2008 entfallen; aber manche älteren Verträge prüfen
- **Anzeigefrist** Schaden je nach AVB sieben Tage bis sofort
- **Wahrung der Frist durch Klage** bei Verjährung

### Frage 7 — Hauptaktenstand?

- Vollständiger Schriftwechsel?
- Bedingungswerk komplett?
- Schadensgutachten vorhanden?
- Bei BU ärztliches Gutachten?

## Routing-Matrix

| Sparte/Vorgang | Folge-Skill | Frist |
|---|---|---|
| Deckungsablehnung Sachsparte | `deckungsanfrage-pruefen` | drei Jahre Verjährung |
| BU-Ablehnung | `deckungsanfrage-pruefen` plus medizinische Gegenbegutachtung | drei Jahre |
| Leben Todesfall | `deckungsanfrage-pruefen` | drei Jahre |
| Krankenversicherung medizinische Notwendigkeit | (Skill kv-prüfung — perspektivisch) | drei Jahre |
| Rechtsschutz Deckungsablehnung | (Skill rs-deckung — perspektivisch) | drei Jahre |
| Direktanspruch Geschädigter | Skill aus `fachanwalt-verkehrsrecht` `unfall-haftungsquote-berechnen` | drei Jahre |
| Vermittlerhaftung | (Skill vermittler-haftung — perspektivisch) | drei Jahre |
| Industrieversicherung | (Skill industriedeckung — perspektivisch) | drei Jahre |

## Mandatsannahme

- **Konflikt-Check** — keine Mandate auf beiden Seiten der Versicherungs-Beziehung
- **Streitwert** ab EUR 10000 LG
- **Rechtsschutz-Deckungsanfrage** prüfen vor Mandatsannahme
- **Komplexität** AVB-Auslegung BGH-Urteilskette

## Eskalation

- **Telefon-Sofort** lebensbedrohliche KV-Ablehnung
- **Binnen einer Stunde** drohende Verjährung
- **Heute** Stellungnahme an Versicherung Rechtsschutz-Deckungsanfrage
- **Diese Woche** Klage-Erstentwurf

## Ausgabe

- `triage-protokoll-versicherungsrecht.md`
- Aktenanlage
- Rechtsschutz-Deckungsanfrage als Entwurf
- Frist im Fristenbuch
- Mandatsvereinbarung mit Honorarvereinbarung über RVG
- Empfehlung Folge-Skill

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Quellen

- VVG §§ 1 ff.
- BGB §§ 195 199 305 ff.
- BGH IV. Zivilsenat
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Vertiefung — Rechtsprechung und Normenkette Triage

### Leitsatz-Zitate (Stand Mai 2026)

Vor Versand jeweils Volltext in juris.bundesgerichtshof.de oder dejure.org aufrufen:

- BGH IV ZR 32/24, Urt. v. 12.3.2025 — Krankentagegeld; Klauselersetzung nach Intransparenz unzulässig (Pressemitteilung Nr. 47/25 v. 12.3.2025)
- BGH IV ZR 70/25 — PKV-Beitragsanpassung; Mitteilungspflicht
- BGH IV ZR 86/24, Urt. v. 15.10.2025 — PKV-Beitragsanpassung; Prüfungsmaßstab
- BGH IV ZR 153/20, Urt. v. 14.7.2021 — Versicherungsfall BU nach Ablauf der sechs-monatigen Prognosezeit
- BGH VI ZR 183/22, Urt. v. 28.1.2025 — DSGVO-Schadensersatz Art. 82 hat nur Ausgleichs-, keine Straffunktion

### Normen-Ergänzung

§ 195 BGB (Verjährung 3 Jahre) i.V.m. § 199 BGB (Kenntnis-Beginn) → § 203 BGB (Hemmung Verhandlungen) → § 28 VVG (Obliegenheit Schadensanzeige) → § 115 VVG (Direktklage Haftpflicht) → § 204 BGB (Hemmung Mahnbescheid, Klage, Schlichtungsantrag) → § 214 VVG (Ombudsmann-Verjährungshemmung)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

---

## Skill: `orientierung-mandat-fachanwaltschaft`

_Wenn es um Orientierung im Versicherungsvertragsrecht für Mandate und Fachanwaltschaft nach FAO in Fachanwalt Versicherungsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Orientierung im Versicherungsvertragsrecht für Mandate und Fachanwaltschaft nach FAO


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: SGB V §§ 27, 39, 92, 109, 137, 295, 301, RisikoStruktAusglV, SGB IV, SGB X, SGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Orientierung im Versicherungsvertragsrecht für Mandate und Fachanwaltschaft nach FAO. Anwendungsfall Kanzlei will Versicherungsmandat beurteilen oder Anwalt bereitet sich auf Fachanwaltsprüfung Versicherungsrecht vor. Normen VVG VAG GDV-Musterbedingungen AVB-Sparten BU KV LV Sach-Haftpflicht D-und-O. Prüfraster Sparten Normen FAO-Voraussetzungen verifizierbare Quellen typische Mandate Fristen. Output Rechtsgebietsuebersicht Normen verifizierbare Quellen und Routing zu Versicherungsmandats-Skills. Abgrenzung zu mandat-triage-versicherungsrecht und fachanwalt-versicherungsrecht-deckungsklage.

### Fachanwalt für Versicherungsrecht — Orientierung

## FAO-Voraussetzungen

- Lehrgang 120 Stunden + drei Klausuren.
- 80 Fälle in den letzten drei Jahren, davon mindestens 40 streitige.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| Versicherungsvertrag | VVG §§ 1 ff. Anzeigepflicht §§ 19 ff. Praemienpflicht § 33 Leistungspflicht §§ 100 ff. |
| Versicherungsaufsicht | VAG |
| Pflichtversicherung Kfz | PflVG |
| Berufsunfähigkeit | §§ 172 ff. VVG |
| Krankenversicherung privat | §§ 192 ff. VVG MB/KK |
| Lebensversicherung | §§ 150 ff. VVG |
| Allgemeines Vertragsrecht | §§ 305 ff. BGB AGB-Kontrolle |
| Verjährung | § 195 BGB (drei Jahre) — Sonderregel § 12 VVG aufgehoben |

## Typische Mandate

- BU-Streitigkeiten (Leistungsablehnung)
- Krankheitskostenversicherung (Erstattung Pflegestufen)
- Lebensversicherung (Rückkaufswert Auszahlung im Todesfall)
- Hausratversicherung (Einbruchsdiebstahl Wasserschaden)
- Haftpflichtversicherung (Deckungsstreit)
- D-und-O-Versicherung für Organe Geschäftsleiter
- Berufshaftpflicht Anwaltshaftpflicht

## Fristen

- **Klagefrist** keine spezifische — Verjährung drei Jahre (§ 195 BGB).
- **Beschwerdefrist** zum BaFin gegen Versicherer regelmäßig keine Frist.
- **Anzeigepflichten** Versicherungsnehmer Unverzueglich (§ 19 VVG).
- **Frist nach Schadensfall** vertraglich vereinbart (Obliegenheiten § 28 VVG).

## Hauptgerichte

- Amtsgericht Landgericht (regulaere ZPO-Streitwertgrenze 10.000 EUR ab 01.01.2026).
- OLG / BGH IV. Zivilsenat für Versicherungssachen.

## Berufsverband

- ARGE Versicherungsrecht DAV.

## Schnittstellen

- **kanzlei-allgemein** für Fristen und Versand.
- **fachanwalt-verkehrsrecht** bei Kfz-Haftpflicht.
- **fachanwalt-medizinrecht** bei Krankenversicherung.

## Vertiefung — Aktuelle Rechtsprechung und Normen

### Leitsatz-Zitate (Stand Mai 2026; offene Quellen)

Vor Versand jeweils Volltext in offener Quelle aufrufen (juris.bundesgerichtshof.de, dejure.org, openjur.de):

1. **BGH, Urt. v. 12.3.2025, IV ZR 32/24** — Krankentagegeldversicherung: Klauselersetzung nach Unwirksamkeit nicht ohne Weiteres zulässig; Versicherer kann unwirksame Tagessatz-Herabsetzung nicht durch im Kern gleiche neue Klausel ersetzen. Pressemitteilung Nr. 47/25 vom 12.3.2025.
2. **BGH, IV ZR 70/25, 2025** — PKV-Beitragsanpassung: Mitteilungsschreiben muss die konkrete Rechnungsgrundlage benennen (§ 203 Abs. 5 VVG).
3. **BGH, IV ZR 86/24, Urt. v. 15.10.2025** — Beitragsanpassung PKV; Prüfungsmaßstab. Quelle: bundesgerichtshof.de.
4. **BGH, Urt. v. 14.7.2021, IV ZR 153/20** — Versicherungsfall BU: Eintritt nach Ablauf der bedingungsgemäßen sechs-monatigen Prognosezeit.
5. **BGH, Urt. v. 28.1.2025, VI ZR 183/22** — DSGVO-Schadensersatz hat reine Ausgleichsfunktion; SCHUFA-Meldung bei streitiger Forderung unzulässig.

### Paragrafenkette (Überblick VVG-Struktur)

§§ 1–21 VVG (allgemeine Vorschriften, Informationspflichten, Widerruf) → §§ 28–32 VVG (Obliegenheiten, Rechtsfolgen) → §§ 74–99 VVG (Schadensversicherung) → §§ 100–112 VVG (Haftpflichtversicherung) → §§ 150–171 VVG (Lebensversicherung) → §§ 172–177 VVG (Berufsunfähigkeitsversicherung) → §§ 192–215 VVG (Krankenversicherung, Ombudsmann) → §§ 305–310 BGB (AGB-Kontrolle AVB) → § 215 VVG (örtliche Zuständigkeit Klage VN)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### Fristen-Übersicht

| Bereich | Frist | Norm |
|---|---|---|
| Verjährung Versicherungsleistung | 3 Jahre ab Schluss Kenntnisjahr | §§ 195, 199 BGB |
| Widerruf (korrekte Belehrung) | 30 Tage | § 8 Abs. 1 VVG |
| Widerruf Lebensversicherung (falsche/fehlende Belehrung) | unbegrenzt (EuGH/BGH-Linie; Volltext vor Versand verifizieren) | § 8 VVG, EuGH C-209/12 (Endress) |
| Anzeigepflicht-Schadensfall | laut AVB (meist unverzüglich) | § 28 VVG |
| Hemmung durch Schlichtungsantrag | bis Entscheidung Ombudsmann | § 204 BGB i.V.m. § 214 VVG |

## Triage — Orientierungs-Routing

1. **Sachgebiet/Sparte identifizieren** (BU → `fachanwalt-versicherungsrecht-berufsunfaehigkeit-klage`; LV → `fachanwalt-versicherungsrecht-lebensversicherung-rueckkauf`; D&O → `fachanwalt-versicherungsrecht-do-deckungsabwehr`; Cyber → `fachanwalt-versicherungsrecht-cyber-loesegeld-sanktionsrecht`).
2. **Ablehnungsschreiben eingegangen?** → `fachanwalt-versicherungsrecht-leistungsablehnung-pruefen`.
3. **Klage vorbereiten?** → `fachanwalt-versicherungsrecht-deckungsklage` + `klage-versicherer-strategie`.
4. **Schlichtung zuerst?** → `fachanwalt-versicherungsrecht-ombudsmann-gdv-schlichtung`.
5. **Regress-Abwehr gegen Sozialversicherungsträger?** → `fachanwalt-versicherungsrecht-regress-abwehr`.

---

## Skill: `fachanwalt-versicherungsrecht-orientierung`

_Wenn es um Fachanwalt für Versicherungsrecht — Orientierung in Fachanwalt Versicherungsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Fachanwalt für Versicherungsrecht — Orientierung

## FAO-Voraussetzungen

- Lehrgang 120 Stunden + drei Klausuren.
- 80 Fälle in den letzten drei Jahren, davon mindestens 40 streitige.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| Versicherungsvertrag | VVG §§ 1 ff. Anzeigepflicht §§ 19 ff. Praemienpflicht § 33 Leistungspflicht §§ 100 ff. |
| Versicherungsaufsicht | VAG |
| Pflichtversicherung Kfz | PflVG |
| Berufsunfähigkeit | §§ 172 ff. VVG |
| Krankenversicherung privat | §§ 192 ff. VVG MB/KK |
| Lebensversicherung | §§ 150 ff. VVG |
| Allgemeines Vertragsrecht | §§ 305 ff. BGB AGB-Kontrolle |
| Verjährung | § 195 BGB (drei Jahre) — Sonderregel § 12 VVG aufgehoben |

## Typische Mandate

- BU-Streitigkeiten (Leistungsablehnung)
- Krankheitskostenversicherung (Erstattung Pflegestufen)
- Lebensversicherung (Rückkaufswert Auszahlung im Todesfall)
- Hausratversicherung (Einbruchsdiebstahl Wasserschaden)
- Haftpflichtversicherung (Deckungsstreit)
- D-und-O-Versicherung für Organe Geschäftsleiter
- Berufshaftpflicht Anwaltshaftpflicht

## Fristen

- **Klagefrist** keine spezifische — Verjährung drei Jahre (§ 195 BGB).
- **Beschwerdefrist** zum BaFin gegen Versicherer regelmäßig keine Frist.
- **Anzeigepflichten** Versicherungsnehmer Unverzueglich (§ 19 VVG).
- **Frist nach Schadensfall** vertraglich vereinbart (Obliegenheiten § 28 VVG).

## Hauptgerichte

- Amtsgericht Landgericht (regulaere ZPO-Streitwertgrenze 10.000 EUR ab 01.01.2026).
- OLG / BGH IV. Zivilsenat für Versicherungssachen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Berufsverband

- ARGE Versicherungsrecht DAV.

## Schnittstellen

- **kanzlei-allgemein** für Fristen und Versand.
- **fachanwalt-verkehrsrecht** bei Kfz-Haftpflicht.
- **fachanwalt-medizinrecht** bei Krankenversicherung.

## Vertiefung — Aktuelle Rechtsprechung und Normen

### Leitsatz-Zitate (Stand Mai 2026; offene Quellen)

Vor Versand jeweils Volltext in offener Quelle aufrufen (juris.bundesgerichtshof.de, dejure.org, openjur.de):

1. **BGH, Urt. v. 12.3.2025, IV ZR 32/24** — Krankentagegeldversicherung: Klauselersetzung nach Unwirksamkeit nicht ohne Weiteres zulässig; Versicherer kann unwirksame Tagessatz-Herabsetzung nicht durch im Kern gleiche neue Klausel ersetzen. Pressemitteilung Nr. 47/25 vom 12.3.2025.
2. **BGH, IV ZR 70/25, 2025** — PKV-Beitragsanpassung: Mitteilungsschreiben muss die konkrete Rechnungsgrundlage benennen (§ 203 Abs. 5 VVG).
3. **BGH, IV ZR 86/24, Urt. v. 15.10.2025** — Beitragsanpassung PKV; Prüfungsmaßstab. Quelle: bundesgerichtshof.de.
4. **BGH, Urt. v. 14.7.2021, IV ZR 153/20** — Versicherungsfall BU: Eintritt nach Ablauf der bedingungsgemäßen sechs-monatigen Prognosezeit.
5. **BGH, Urt. v. 28.1.2025, VI ZR 183/22** — DSGVO-Schadensersatz hat reine Ausgleichsfunktion; SCHUFA-Meldung bei streitiger Forderung unzulässig.

### Paragrafenkette (Überblick VVG-Struktur)

§§ 1–21 VVG (allgemeine Vorschriften, Informationspflichten, Widerruf) → §§ 28–32 VVG (Obliegenheiten, Rechtsfolgen) → §§ 74–99 VVG (Schadensversicherung) → §§ 100–112 VVG (Haftpflichtversicherung) → §§ 150–171 VVG (Lebensversicherung) → §§ 172–177 VVG (Berufsunfähigkeitsversicherung) → §§ 192–215 VVG (Krankenversicherung, Ombudsmann) → §§ 305–310 BGB (AGB-Kontrolle AVB) → § 215 VVG (örtliche Zuständigkeit Klage VN)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### Fristen-Übersicht

| Bereich | Frist | Norm |
|---|---|---|
| Verjährung Versicherungsleistung | 3 Jahre ab Schluss Kenntnisjahr | §§ 195, 199 BGB |
| Widerruf (korrekte Belehrung) | 30 Tage | § 8 Abs. 1 VVG |
| Widerruf Lebensversicherung (falsche/fehlende Belehrung) | unbegrenzt (EuGH/BGH-Linie; Volltext vor Versand verifizieren) | § 8 VVG, EuGH C-209/12 (Endress) |
| Anzeigepflicht-Schadensfall | laut AVB (meist unverzüglich) | § 28 VVG |
| Hemmung durch Schlichtungsantrag | bis Entscheidung Ombudsmann | § 204 BGB i.V.m. § 214 VVG |

## Triage — Orientierungs-Routing

1. **Sachgebiet/Sparte identifizieren** (BU → `fachanwalt-versicherungsrecht-berufsunfaehigkeit-klage`; LV → `fachanwalt-versicherungsrecht-lebensversicherung-rueckkauf`; D&O → `fachanwalt-versicherungsrecht-do-deckungsabwehr`; Cyber → `fachanwalt-versicherungsrecht-cyber-loesegeld-sanktionsrecht`).
2. **Ablehnungsschreiben eingegangen?** → `fachanwalt-versicherungsrecht-leistungsablehnung-pruefen`.
3. **Klage vorbereiten?** → `fachanwalt-versicherungsrecht-deckungsklage` + `klage-versicherer-strategie`.
4. **Schlichtung zuerst?** → `fachanwalt-versicherungsrecht-ombudsmann-gdv-schlichtung`.
5. **Regress-Abwehr gegen Sozialversicherungsträger?** → `fachanwalt-versicherungsrecht-regress-abwehr`.

---

## Skill: `erstgespraech-mandatsannahme`

_Wenn es um Erstgespraech Mandatsannahme in Fachanwalt Versicherungsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Strukturierter Erstgespraechsleitfaden für Versicherungsvertragsrecht (Personen- und Sachversicherung): Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen.


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: SGB V §§ 27, 39, 92, 109, 137, 295, 301, RisikoStruktAusglV, SGB IV, SGB X, SGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Strukturierter Erstgespraechsleitfaden für Versicherungsvertragsrecht (Personen- und Sachversicherung): Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen.

### Erstgespraech und Mandatsannahme im Versicherungsvertragsrecht (Personen- und Sachversicherung)

## Wann dieser Arbeitsgang greift

- Neue Anfrage aus dem Bereich Versicherungsvertragsrecht (Personen- und Sachversicherung) (Telefon, Mail, Empfehlung, Walk-in).
- Mandantin oder Mandant beschreibt Sachverhalt unstrukturiert; viele Anlagen ohne System.
- Vor jeder weiteren fachlichen Bearbeitung: erst Annahme klären, Konflikt- und GwG-Prüfung, Vollmacht, Streitwert/Vereinbarung, Fristen.

## Phasen des Erstgespraechs

### 1. Aufnahme der Konstellation (10-15 Min.)

Standard-Fragenraster für Versicherungsvertragsrecht (Personen- und Sachversicherung):

- Beteiligte (Vor-/Nachname, Geburtsdatum, Anschrift, Rolle: Klägerin/Beklagter, Antragsteller, Beschuldigter)
- Konflikt-Kern in einem Satz ("Was ist Ihr Ziel?")
- Konkrete fachliche Stossrichtung: Berufsunfaehigkeit, Unfallversicherung, Sachversicherung, RSV, Haftpflicht
- Bisherige Korrespondenz (Bescheide, Schreiben der Gegenseite, anwaltliche Vertretung der Gegenseite?)
- **Fristenscreening sofort:** anstehende Klage-/Widerspruchs-/Einspruchsfristen aus den vorgelegten Schreiben (z.B. Deckungsklage, Klage BU/UB, Klage Sachversicherung, RSV-Deckungsklage). Frist-Alarm an die Vorbereitung weitergeben.

### 2. Konflikt-Prüfung und GwG-Check (5 Min.)

- Konflikt-Check über Mandantsystem: Gegnerin, Streitgegenstand, frueherer Mandant?
- GwG-Identifizierung: amtlicher Lichtbildausweis (Ausweisscan), bei juristischer Person Handelsregister-/Transparenzregister-Auszug, ggf. wirtschaftlich Berechtigte/n.
- Risikobewertung (niedrig/mittel/hoch) abhaengig von Mandatscharakter, Bargeld, Auslandsbezug.
- Doku im Mandatsbogen (Pflicht nach §§ 10 ff. GwG i.V.m. § 2 Abs. 1 Nr. 10 GwG für RA-Mandate).

### 3. Vollmacht und Schweigepflichtentbindung

- Allgemeine Prozess-/Aussenvollmacht (BORA, ZPO, FamFG, je nach Fachgebiet).
- Spezielle Vollmachten: ggf. Akteneinsicht Strafakte, KV-Abrechnungsdaten, Sozialdaten (Schweigepflichtentbindung gegenueber Krankenkasse, Arzt, Behörde).
- Bei Eheleuten/GbR/GmbH: einzelvollmachtgebende Person und Vertretungsmacht klären.

### 4. Streitwert und Gebührenvereinbarung

Standard-Streitwerte im Bereich Versicherungsvertragsrecht (Personen- und Sachversicherung):

- Skizze: Streitwert grob abschaetzen (z.B. Hauptforderung, ggf. + Zinsen, Nebenforderungen).
- RVG-Pauschalrechnung (Berechnungstool im Plugin) oder Stundenhonorarvereinbarung.
- Beratungshilfe-/Prozesskostenhilfe-Antrag prüfen, wenn wirtschaftlich angezeigt.
- Vorschussanforderung nach § 9 RVG.

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

- BORA, BRAO, FAO für Fachanwaltschaft Versicherungsvertragsrecht (Personen- und Sachversicherung).
- GwG, GwGMeldV, Identifizierungsleitfaden BRAK.
- VVG, AVB, BU-/UV-Bedingungen, ARB, PflVG (für fachliche Erstpruefung).
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

Mandantin kommt am Donnerstag, Frist laeuft am Montag (Klage- oder Widerspruchsfrist im Bereich Versicherungsvertragsrecht (Personen- und Sachversicherung)). Handlungs-Sequenz:

1. Sofort-Vollmacht und Sofort-Akteneinsicht (per beA, ELSTER, Behördenportal).
2. Antrag auf Wiedereinsetzung (§ 233 ZPO, § 60 VwGO, § 110 AO) als Reserve dokumentieren.
3. Spaeteste-Stunde-Versand-Plan: beA bevorzugt, mit qualifizierter Signatur und Empfangsbekenntnis.
4. Honorarvereinbarung NICHT auf Eilzuschlag verzichten - aber transparent kommunizieren.

### Konstellation B: Komplexer Sachverhalt, Datenraum unsortiert

Mandant uebergibt 200+ Dateien (PDF-Scans, E-Mails, Excel-Listen). Vor jeder fachlichen Bewertung:

1. Datenraum-Index in Excel: Datum, Absender, Empfaenger, Aktenzeichen, kurze Inhaltszeile.
2. Chronologischer Verlauf als Zeitstrahl - Spielraum für Verjährungs- und Ausschlussfristen identifizieren.
3. Loecher im Datenraum gezielt anfordern (Mandantenfragen-Katalog).

### Konstellation C: Interessenkonflikt-Naehe

Frueheres Mandat mit derselben Gegnerin oder gleichem Sachzusammenhang. Prüfung:

1. § 43a Abs. 4 BRAO und § 3 BORA - Sachzusammenhang, nicht nur Personenidentitaet.
2. Einwilligung beider Mandanten in Textform (mit konkreter Beschreibung).
3. Bei Zweifel: Mandat ablehnen und an Kanzleikollegium ueberweisen.

## Mandanten-Erwartungsmanagement

- Realistische Erfolgs- und Kostenprognose (nicht "Wir gewinnen sicher").
- Verfahrensdauer im Bereich Versicherungsvertragsrecht (Personen- und Sachversicherung): Erfahrungswerte nach Instanz.
- Vergleichschance vs. streitiges Urteil als Option offen halten.
- Schriftliche Zusammenfassung des Erstgespraechs binnen 48 h.

## Honorarvereinbarung - Best Practices

- RVG-Basis als Default, Stundenhonorar nur mit gesondertem Hinweis nach § 3a RVG.
- Erfolgshonorar nur in den engen Grenzen § 4a RVG.
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

## Cross-Refs

- `vergleichsverhandlung-strategie` (im selben Plugin) für den Fall, dass aussergerichtliche Loesung angestrebt wird.
- `schriftsatzkern-substantiierung` (im selben Plugin) für den Schriftsatzaufbau, wenn Klage/Widerspruch eingereicht wird.
- Kanzlei-Allgemein-Plugin `kanzlei-allgemein` für Konflikt-, GwG- und PEP-Prüfroutinen.

## Vertiefung — Normenkette und Rechtsprechung Erstgespräch Versicherungsrecht

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normenkette Erstgespräch / Mandatsannahme Versicherungsrecht

§ 6 VVG (Beratungspflicht Versicherer; Anwalt analog für Mandant) → §§ 195, 199, 203, 204 BGB (Verjährung, Hemmung) → § 215 VVG (Zuständigkeit bei Klage) → §§ 43a, 45 BRAO (Konfliktprüfung) → §§ 3, 3a RVG (Vergütungsvereinbarung) → §§ 10, 11 GwG (Identifizierungspflicht) → § 9 RVG (Vorschuss)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

---

## Skill: `erstpruefung-und-mandatsziel`

_Wenn es um Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel in Fachanwalt Versicherungsrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel


## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 241 Abs. 2 BGB` — Rücksichtnahme-, Schutz- und Organisationspflichten.
- `§ 242 BGB` — Treu und Glauben als Korrektiv enger Klausel- und Anspruchsarbeit.
- `§ 280 Abs. 1 BGB` — Pflichtverletzung, Vertretenmuessen, Schaden.
- `§ 286 Abs. 1 BGB` — Verzug und Fristlogik.
- `§ 195 BGB` — regelmäßige Verjährung.
- `§ 199 Abs. 1 BGB` — Beginn der regelmäßigen Verjährung.
- `§ 253 Abs. 2 ZPO` — Bestimmtheit von Antrag und Klagegrund.
- `§ 138 Abs. 1 ZPO` — Wahrheitspflicht und vollstaendiger Tatsachenvortrag.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: SGB V §§ 27, 39, 92, 109, 137, 295, 301, RisikoStruktAusglV, SGB IV, SGB X, SGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel.

## Spezialwissen: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** VVG, VAG.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Fachanwalt** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `fachanwalt-versicherungsrecht-deckungsklage`

_Wenn es um Deckungsklage in Fachanwalt Versicherungsrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. Auswahlstichwort: Fachanwalt Versicherungsrecht Deckungsklage; Arbeitsfeld: Fachanwalt Versicherungsrecht._

# Deckungsklage

## Kaltstart-Rückfragen

1. Wurde außergerichtlich vollständig die Leistung gefordert und ist die Ablehnung endgültig? Liegt ein ausdrückliches Ablehnungsschreiben vor?
2. Bei BU-Versicherung: Liegt ein Berufsunfähigkeitsgutachten und liegen ärztliche Atteste vor? Ist der Grad der BU von mindestens 50 % ärztlich belegt?
3. Welche Klageart ist erforderlich — Leistungsklage auf bezifferten Betrag oder Feststellungsklage auf künftige Rentenpflicht (§ 256 ZPO)?
4. Welcher Streitwert ergibt sich — bei wiederkehrenden Leistungen 3,5-facher Jahreswert (§ 9 ZPO); gedeckelt wenn Restlaufzeit kürzer?
5. Besteht Rechtsschutzversicherung — Deckungszusage eingeholt? Oder ist PKH (§ 114 ZPO) zu beantragen?
6. Sind alle Vertragsunterlagen (Police, AVB-Fassung zum Vertragsschluss, Antragsformular, sämtliche Schriftwechsel) vorhanden?
7. Droht Verjährung (3 Jahre ab Jahresende der Kenntnis §§ 195, 199 BGB)? Hemmung durch Ombudsstelle § 204 BGB aktiv?
8. Ist eine Streitverkündung an den Versicherungsmakler/Vermittler erforderlich (bei Beratungsfehlern)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

### Normtexte (Kernauszug)

- **§ 1 VVG** — Materielle Anspruchsgrundlage; Versicherungspflicht des VR.
- **§ 14 VVG** — Fälligkeit nach Abschluss der zur Feststellung nötigen Erhebungen; Verzug ab Mahnung oder Fristablauf.
- **§ 215 VVG** — Örtliche Zuständigkeit: VN kann am Wohnsitz / gewöhnlichen Aufenthalt klagen; auch Sitz des VR wählbar.
- **§ 23 Nr. 1 GVG** — Sachliche Zuständigkeit AG: bis EUR 10000 (ab 01.01.2026 Justizreform).
- **§ 71 Abs. 1 GVG** — Sachliche Zuständigkeit LG: ab EUR 10000.
- **§ 9 ZPO** — Streitwert wiederkehrender Leistungen: 3,5-facher Jahreswert; gedeckelter Wert bei kürzerer Restlaufzeit.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **§ 114 ZPO** — PKH bei wirtschaftlicher Bedürftigkeit und hinreichenden Erfolgsaussichten; Beiordnung eines RA.
- **§ 379 ZPO** — Sachverständigenvorschuss; bei PKH Übernahme durch Staatskasse.
- **§ 72 ZPO** — Streitverkündung; Makler, Vermittler bei Beratungspflichtverletzung einbeziehen.
- **§§ 195, 199, 204 BGB** — Verjährung 3 Jahre; Hemmung durch Ombudsstelle und Verhandlungen.

### Leitentscheidungen

| Gericht | Aktenzeichen | Datum | Kernaussage |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema in Tabellenform


**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.

| Nr. | Prüfschritt | Norm | Konsequenz |
|---|---|---|---|
| 1 | Außergerichtlich endgültige Ablehnung? | § 14 VVG | Klage erst nach endgültiger Ablehnung sinnvoll |
| 2 | Klageart — Leistung oder Feststellung? | §§ 253, 256 ZPO | BU-Rente: Feststellungsantrag; Sachschaden: Leistungsantrag |
| 3 | Sachliche Zuständigkeit (Streitwert)? | §§ 23, 71 GVG; § 9 ZPO | BU 3,5-facher Jahreswert; Sachschaden = Hauptforderung |
| 4 | Örtliche Zuständigkeit nach § 215 VVG? | § 215 VVG | Wohnsitz VN bevorzugt; auch Sitz VR möglich |
| 5 | Verjährung geprüft? | §§ 195, 199, 203, 204 BGB | Hemmung dokumentieren |
| 6 | Vollständige Vertragsunterlagen vorhanden? | AVB; Police; Antrag | Ohne AVB-Fassung zum Vertragsschluss: schwer zu klagen |
| 7 | Beweise zum Versicherungsfall vollständig? | ZPO §§ 371, 373, 402 | SV-Gutachten, Zeugen, Urkunden benennen |
| 8 | PKH-Antrag vorbereitet? | § 114 ZPO | Einkommensverhältnisse, hinreichende Erfolgsaussicht |
| 9 | Rechtsschutz-Deckungszusage eingeholt? | Rechtsschutz-AVB | Deckungszusage vor Klageerhebung erforderlich |
| 10 | Sachverständigenvorschuss eingeplant? | § 379 ZPO | Ca. EUR 2000–5000 für Medizin-SV |
| 11 | Streitverkündung Makler/Vermittler? | § 72 ZPO | Verjährungswirkung; Bindungswirkung für Folgeprozess |
| 12 | Vorläufige Vollstreckbarkeit beantragt? | § 708 Nr. 11 ZPO | Standardantrag in Klage |
| 13 | Zinsen berechnet? | §§ 280, 286, 288 BGB | Ab Verzugseinritt; 5 % über Basiszinssatz |
| 14 | Außergerichtliche Anwaltskosten berechnet? | § 249 BGB; RVG | 1,3 Geschäftsgebühr aus Gegenstandswert |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Deckungsklage gegen Versicherer | Klageschrift nach Pruefschema; Template unten |
| Variante A — Versicherer hat nur teilweise abgelehnt | Klage auf Differenzbetrag; Vergleich zu voller Deckung anstreben |
| Variante B — Verjaehrung droht innerhalb 3 Monaten | Klage sofort; Verhandlung parallel |
| Variante C — Mandant will keine Eskalation Folgegeschaeft | Mediation oder Ombudsmann-Verfahren zuerst; Klage danach |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Schriftsatzbausteine

### Baustein 1 — Vollständige Klageschrift BU-Versicherung

```
An das Landgericht [Ort]
— Zivilkammer —

KLAGESCHRIFT

[Vorname Nachname], geb. [Datum], [Adresse]
                                        — Kläger —
Prozessbevollmächtigte:
Rechtsanwältinnen/Rechtsanwälte [Kanzlei, Adresse]

gegen

[Versicherungs-AG], vertreten durch den Vorstand,
[Adresse]
                                        — Beklagte —

wegen Berufsunfähigkeitsleistung
Streitwert: vorläufig EUR ____ (3,5 × [Jahresrente])

I. ANTRÄGE

1. Es wird festgestellt, dass die Beklagte verpflichtet ist,
   dem Kläger aus dem Berufsunfähigkeitsversicherungsvertrag,
   Police Nr. [Nr.], Anlage K1, ab dem [Datum] eine monatliche
   Berufsunfähigkeitsrente von EUR [Betrag] sowie Befreiung von
   der Beitragszahlungspflicht zu leisten, solange und soweit
   beim Kläger Berufsunfähigkeit von mindestens 50 % in seiner
   zuletzt ausgeübten Tätigkeit als [Beruf] besteht.

2. Die Beklagte wird verurteilt, an den Kläger für den Zeitraum
   [Beginn] bis [aktuell] rückständige Renten in Höhe von
   EUR [Summe] nebst Zinsen in Höhe von 5 Prozentpunkten über
   dem Basiszinssatz seit [Datum] zu zahlen.

3. Die Beklagte wird verurteilt, an den Kläger vorgerichtliche
   Anwaltskosten in Höhe von EUR [Berechnung nach RVG] zu zahlen.

4. Die Kosten des Rechtsstreits trägt die Beklagte.

5. Das Urteil ist gegen Sicherheitsleistung in Höhe von 110 %
   vorläufig vollstreckbar.

II. SACHVERHALT

Der Kläger unterhält bei der Beklagten eine
Berufsunfähigkeitszusatzversicherung (Police Nr. [Nr.]),
abgeschlossen am [Datum], monatliche Rente EUR [Betrag],
Beitragsbefreiung bei BU (Anlage K1 Police; Anlage K2 AVB).

Seit [Datum] ist der Kläger infolge [Erkrankung/Diagnose,
ICD-Code: [X]] nicht mehr in der Lage, seinen zuletzt als
[Beruf] ausgeübten Beruf zu mindestens 50 % auszuüben.

Sein Berufsbild umfasste im Einzelnen folgende Tätigkeiten:
1. [Tätigkeit, Zeitanteil %]
2. [Tätigkeit, Zeitanteil %]
3. [Tätigkeit, Zeitanteil %]
[Detailbeschreibung der körperlichen/kognitiven Anforderungen]

Der Kläger meldete die Berufsunfähigkeit am [Datum] bei der
Beklagten an (Anlage K3). Die Beklagte lehnte die Leistung
mit Schreiben vom [Datum] ab (Anlage K4).

III. FESTSTELLUNGSINTERESSE

Die Beklagte bestreitet die Leistungspflicht dem Grunde nach.
Das Feststellungsinteresse gemäß § 256 ZPO ist gegeben —
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

IV. RECHTLICHE WÜRDIGUNG

1. Versicherungsfall — Berufsunfähigkeit liegt vor
   Der Kläger ist nach ärztlichen Attesten (Anlagen K5–K8)
   und nach dem SV-Gutachten [Name] vom [Datum] (Anlage K9)
   seit [Datum] zu mindestens 50 % berufsunfähig bezogen
   Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

2. Keine Obliegenheitsverletzung
   [Ablehnungsgrund Versicherer + Widerlegung]

3. Kein Risikoausschluss einschlägig
   [AVB-Ausschluss-Klausel prüfen + ggf. Transparenzrüge]

V. BEWEISANGEBOTE

- Anlage K1: Police
- Anlage K2: AVB (Fassung [Datum/Version])
- Anlage K3: Schadensmeldung
- Anlage K4: Ablehnungsschreiben
- Anlage K5–K8: Ärztliche Atteste/Befundberichte
- Anlage K9: SV-Gutachten (ggf. gerichtliche Bestellung
  beantragt: Medizinischer SV des Fachgebiets [X])
- Zeuge: Behandelnder Arzt [Name, Adresse] zum Beweis der
  Diagnose und des Verlaufs
- Parteivernehmung Kläger § 448 ZPO zur Berufstätigkeit
  (hilfsweise)

[Kanzlei]
```

### Baustein 2 — PKH-Erklärung und Antrag (Kurzschema)

```
ANTRAG AUF PROZESSKOSTENHILFE
gemäß § 114 ZPO

mit der Bitte um Beiordnung:
Rechtsanwalt/Rechtsanwältin [Name, Kanzlei]

I. Wirtschaftliche Bedürftigkeit
Monatliches Nettoeinkommen: EUR [Betrag]
Abzüge: [Kosten Unterkunft, Unterhalt etc.]
Verfügbares Einkommen: EUR [unter Freibetrag]
Erklärung mit Belegen: Anlage PKH 1-4

II. Hinreichende Erfolgsaussichten
Die Klage ist hinreichend aussichtsreich, da
[Zusammenfassung Ablehnungsgründe + Widerlegung].

III. Bitte um Ratenzahlung
Monatlich EUR [Betrag] ab [Datum].

[Kanzlei]
```

### Baustein 3 — Streitverkündung an Versicherungsmakler

```
STREITVERKÜNDUNG § 72 ZPO

In dem Rechtsstreit [Az] verkünden wir dem

[Makler/Vermittler GmbH], [Adresse]

den Streit.

Für den Fall, dass die Klage gegen die Beklagte Versicherungs-AG
abgewiesen werden sollte, werden wir Ersatzansprüche gegen den
Streitverkündungsempfänger geltend machen, da er bei Abschluss
des Versicherungsvertrags nicht korrekt über die Anforderungen
an die Anzeigepflicht § 19 VVG / die AVB-Klauseln [X] belehrt hat.

Die Streitverkündung erfolgt zur Bindungswirkung für einen
etwaigen Folgeprozess (§ 74 ZPO).

[Kanzlei]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.


## Beweislast und Darlegungslast

| Frage | Beweislast |
|---|---|
| Eintritt des Versicherungsfalls | Kläger (VN) |
| Grad der Berufsunfähigkeit | Kläger; SV-Gutachten |
| Schadenshöhe (Rückstände, künftige Rente) | Kläger (Police-Wert) |
| Obliegenheitsverletzung | Beklagte (Versicherer) |
| Kausalität Obliegenheit → Schaden fehlt | Kläger (§ 28 Abs. 3 VVG Exkulpation) |
| AVB-Klausel wirksam | Beklagte / Gericht (Transparenzprüfung) |
| Verjährungshemmung | Kläger |

## Fristen und Verjährung

| Frist | Dauer | Anker | Norm |
|---|---|---|---|
| Verjährung | 3 Jahre | Jahresende der Kenntnis | §§ 195, 199 BGB |
| Hemmung Ombudsstelle | Dauer + 6 Monate | Einleitung | § 204 Abs. 1 Nr. 4 BGB |
| Hemmung Verhandlungen | Dauer | Verhandlungsbeginn | § 203 BGB |
| Fälligkeit Versicherungsleistung | nach Abschluss Ermittlungen | Abschluss | § 14 Abs. 1 VVG |
| Streitverkündungsfrist für Regress | abhängig von Anspruch (typisch 3 Jahre) | Kenntnis Mangel | §§ 195, 199 BGB |

## Typische Gegenargumente und Reaktion

| Einwand Versicherer | Reaktion |
|---|---|
| BU-Grad unter 50 % | Eigenes SV-Gutachten vorlegen; gerichtlicher SV im Prozess; Berufsbildanalyse detailliert |
| Verweisung auf Vergleichsberuf | AVB auf abstrakte Verweisung prüfen; neuere AVB schließen häufig aus |
| Vorvertragliche Anzeigepflicht verletzt | Antragsfragebogen prüfen; Kausalität zwischen Nichtanzeige und Berufsunfähigkeit |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| PKH-Antrag abzuweisen wegen mangelnder Erfolgsaussichten | Konkrete Ablehnungsbegründung ist schwach; Erfolgsaussicht darlegen |
| Sachverständigenkosten zu hoch | § 379 ZPO-Vorschuss; bei PKH übernimmt Staatskasse; SV-Beauftragung notwendig |

## Streitwert und Kosten

- BU-Versicherung: 3,5-facher Jahreswert der Rente (§ 9 ZPO); bei 10 Jahren Restlaufzeit und EUR 1500/Monat = EUR 63000 Streitwert.
- Gerichtskostenvorschuss LG bei Streitwert EUR 63000: ca. EUR 1638 (GKG).
- Medizinischer SV-Vorschuss: EUR 2500–6000.
- Bei PKH-Bewilligung: Staatskasse trägt GKG-Vorschuss und SV-Kosten.
- Rechtsschutzversicherung: Deckungszusage vorab zwingend; ohne Zusage Eigenanteil des Mandanten.

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| BU — klarer medizinischer Befund | SV-Gutachten vorab einholen; Klageschrift mit Gutachten einreichen |
| BU — streitiger Grad | Feststellungsklage; gerichtlicher SV-Beweis; Berufsbild detailliert beschreiben |
| Sachschaden — Ablehnung ohne Substanz | Direktklage nach 2-Wochen-Fristsetzung |
| Streitwert unter EUR 10000 | AG-Verfahren; Ombudsstelle prüfen (bindend bis EUR 10000) |
| Verjährung naht | Klageeinreichung hemmt Verjährung ab Zustellung § 204 Abs. 1 Nr. 1 BGB |

## Anschluss-Skills

- `deckungsanfrage-pruefen` — Vorprüfung vor Klage
- `klage-versicherer-strategie` — Klagestrategie-Details
- `fachanwalt-versicherungsrecht-regress-abwehr` — Regress des Versicherers

## Quellen

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Vertiefung — Aktuelle Rechtsprechung und Normen

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Paragrafenkette

§ 256 ZPO (Feststellungsklage bei laufender BU-Rente) → § 215 VVG (örtliche Zuständigkeit Klage VN gegen Versicherer) → §§ 23, 71 GVG (sachliche Zuständigkeit AG/LG nach Streitwert) → § 1 VVG (Hauptleistungspflicht) → § 286 ZPO (Beweislast und freie Beweiswürdigung) → § 402 ZPO (gerichtlicher Sachverständiger) → § 114 ZPO (PKH bei Bedürftigkeit) → § 286 ZPO (Beweiswürdigung Privatgutachten)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage — Sofortprüfung Deckungsklage

1. **Zuständigkeit prüfen:** Streitwert ≤ 10.000 EUR → AG; > 10.000 EUR → LG. Örtlich: Wohnsitz VN (§ 215 VVG) oder Sitz Versicherer (§ 17 ZPO) — Wahlrecht beim Kläger.
2. **Klageantrag formulieren:** Laufende Rente → Feststellungsantrag § 256 ZPO; rückständige Beträge → Zahlungsantrag beziffert.
3. **Sachverständigenbeweis vorbereiten:** Privatgutachten als Anlage + Antrag auf gerichtliches Gutachten; Kosten-PKH prüfen.
4. **PKH-Berechtigung prüfen:** § 114 ZPO — ausreichende Erfolgsaussichten (Gutachtenlage) + Bedürftigkeit.
5. **Verjährung hemmen:** Bei Verhandlungen § 203 BGB; sonst Klageschrift einreichen vor Ablauf der 3-Jahres-Frist.

---

<!-- AUDIT 27.05.2026 — Bundle 027 Halluzinations-Reparatur
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
-->

---

## Skill: `deckungsklage`

_Wenn es um Deckungsklage in Fachanwalt Versicherungsrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. Auswahlstichwort: Deckungsklage; Arbeitsfeld: Fachanwalt Versicherungsrecht._

# Deckungsklage gegen Versicherer auf Versicherungsleistung nach erfolgloser außergerichtlicher Phase


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: SGB V §§ 27, 39, 92, 109, 137, 295, 301, RisikoStruktAusglV, SGB IV, SGB X, SGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Deckungsklage gegen Versicherer auf Versicherungsleistung nach erfolgloser außergerichtlicher Phase. Anwendungsfall Versicherer verweigert Leistung endgueltig und Klage soll erhoben werden. Normen § 1 VVG Versicherungsanspruch § 215 VVG örtliche Zuständigkeit Wohnsitz § 256 ZPO Feststellungsantrag § 114 ZPO PKH. Prüfraster Streitwert Zuständigkeit AG oder LG Klageantrag Beweislast Sachverständigennachweis. Output Deckungsklage-Entwurf mit Antrag Sachverhalt AVB-Auslegung Sachverständigenantrag und PKH-Antrag. Abgrenzung zu klage-versicherer-strategie und fachanwalt-versicherungsrecht-leistungsablehnung-prüfen.

### Deckungsklage

## Kaltstart-Rückfragen

1. Wurde außergerichtlich vollständig die Leistung gefordert und ist die Ablehnung endgültig? Liegt ein ausdrückliches Ablehnungsschreiben vor?
2. Bei BU-Versicherung: Liegt ein Berufsunfähigkeitsgutachten und liegen ärztliche Atteste vor? Ist der Grad der BU von mindestens 50 % ärztlich belegt?
3. Welche Klageart ist erforderlich — Leistungsklage auf bezifferten Betrag oder Feststellungsklage auf künftige Rentenpflicht (§ 256 ZPO)?
4. Welcher Streitwert ergibt sich — bei wiederkehrenden Leistungen 3,5-facher Jahreswert (§ 9 ZPO); gedeckelt wenn Restlaufzeit kürzer?
5. Besteht Rechtsschutzversicherung — Deckungszusage eingeholt? Oder ist PKH (§ 114 ZPO) zu beantragen?
6. Sind alle Vertragsunterlagen (Police, AVB-Fassung zum Vertragsschluss, Antragsformular, sämtliche Schriftwechsel) vorhanden?
7. Droht Verjährung (3 Jahre ab Jahresende der Kenntnis §§ 195, 199 BGB)? Hemmung durch Ombudsstelle § 204 BGB aktiv?
8. Ist eine Streitverkündung an den Versicherungsmakler/Vermittler erforderlich (bei Beratungsfehlern)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

### Normtexte (Kernauszug)

- **§ 1 VVG** — Materielle Anspruchsgrundlage; Versicherungspflicht des VR.
- **§ 14 VVG** — Fälligkeit nach Abschluss der zur Feststellung nötigen Erhebungen; Verzug ab Mahnung oder Fristablauf.
- **§ 215 VVG** — Örtliche Zuständigkeit: VN kann am Wohnsitz / gewöhnlichen Aufenthalt klagen; auch Sitz des VR wählbar.
- **§ 23 Nr. 1 GVG** — Sachliche Zuständigkeit AG: bis EUR 10000 (ab 01.01.2026 Justizreform).
- **§ 71 Abs. 1 GVG** — Sachliche Zuständigkeit LG: ab EUR 10000.
- **§ 9 ZPO** — Streitwert wiederkehrender Leistungen: 3,5-facher Jahreswert; gedeckelter Wert bei kürzerer Restlaufzeit.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **§ 114 ZPO** — PKH bei wirtschaftlicher Bedürftigkeit und hinreichenden Erfolgsaussichten; Beiordnung eines RA.
- **§ 379 ZPO** — Sachverständigenvorschuss; bei PKH Übernahme durch Staatskasse.
- **§ 72 ZPO** — Streitverkündung; Makler, Vermittler bei Beratungspflichtverletzung einbeziehen.
- **§§ 195, 199, 204 BGB** — Verjährung 3 Jahre; Hemmung durch Ombudsstelle und Verhandlungen.

### Leitentscheidungen

| Gericht | Aktenzeichen | Datum | Kernaussage |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema in Tabellenform

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Nr. | Prüfschritt | Norm | Konsequenz |
|---|---|---|---|
| 1 | Außergerichtlich endgültige Ablehnung? | § 14 VVG | Klage erst nach endgültiger Ablehnung sinnvoll |
| 2 | Klageart — Leistung oder Feststellung? | §§ 253, 256 ZPO | BU-Rente: Feststellungsantrag; Sachschaden: Leistungsantrag |
| 3 | Sachliche Zuständigkeit (Streitwert)? | §§ 23, 71 GVG; § 9 ZPO | BU 3,5-facher Jahreswert; Sachschaden = Hauptforderung |
| 4 | Örtliche Zuständigkeit nach § 215 VVG? | § 215 VVG | Wohnsitz VN bevorzugt; auch Sitz VR möglich |
| 5 | Verjährung geprüft? | §§ 195, 199, 203, 204 BGB | Hemmung dokumentieren |
| 6 | Vollständige Vertragsunterlagen vorhanden? | AVB; Police; Antrag | Ohne AVB-Fassung zum Vertragsschluss: schwer zu klagen |
| 7 | Beweise zum Versicherungsfall vollständig? | ZPO §§ 371, 373, 402 | SV-Gutachten, Zeugen, Urkunden benennen |
| 8 | PKH-Antrag vorbereitet? | § 114 ZPO | Einkommensverhältnisse, hinreichende Erfolgsaussicht |
| 9 | Rechtsschutz-Deckungszusage eingeholt? | Rechtsschutz-AVB | Deckungszusage vor Klageerhebung erforderlich |
| 10 | Sachverständigenvorschuss eingeplant? | § 379 ZPO | Ca. EUR 2000–5000 für Medizin-SV |
| 11 | Streitverkündung Makler/Vermittler? | § 72 ZPO | Verjährungswirkung; Bindungswirkung für Folgeprozess |
| 12 | Vorläufige Vollstreckbarkeit beantragt? | § 708 Nr. 11 ZPO | Standardantrag in Klage |
| 13 | Zinsen berechnet? | §§ 280, 286, 288 BGB | Ab Verzugseinritt; 5 % über Basiszinssatz |
| 14 | Außergerichtliche Anwaltskosten berechnet? | § 249 BGB; RVG | 1,3 Geschäftsgebühr aus Gegenstandswert |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu prüfen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Deckungsklage gegen Versicherer | Klageschrift nach Prüfschema; Template unten |
| Variante A — Versicherer hat nur teilweise abgelehnt | Klage auf Differenzbetrag; Vergleich zu voller Deckung anstreben |
| Variante B — Verjährung droht innerhalb 3 Monaten | Klage sofort; Verhandlung parallel |
| Variante C — Mandant will keine Eskalation Folgegeschaeft | Mediation oder Ombudsmann-Verfahren zuerst; Klage danach |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Baustein 1 — Vollständige Klageschrift BU-Versicherung

```
An das Landgericht [Ort]
— Zivilkammer —

KLAGESCHRIFT

[Vorname Nachname], geb. [Datum], [Adresse]
 — Kläger —
Prozessbevollmächtigte:
Rechtsanwältinnen/Rechtsanwälte [Kanzlei, Adresse]

gegen

[Versicherungs-AG], vertreten durch den Vorstand,
[Adresse]
 — Beklagte —

wegen Berufsunfähigkeitsleistung
Streitwert: vorläufig EUR ____ (3,5 × [Jahresrente])

I. ANTRÄGE

1. Es wird festgestellt, dass die Beklagte verpflichtet ist,
 dem Kläger aus dem Berufsunfähigkeitsversicherungsvertrag,
 Police Nr. [Nr.], Anlage K1, ab dem [Datum] eine monatliche
 Berufsunfähigkeitsrente von EUR [Betrag] sowie Befreiung von
 der Beitragszahlungspflicht zu leisten, solange und soweit
 beim Kläger Berufsunfähigkeit von mindestens 50 % in seiner
 zuletzt ausgeübten Tätigkeit als [Beruf] besteht.

2. Die Beklagte wird verurteilt, an den Kläger für den Zeitraum
 [Beginn] bis [aktuell] rückständige Renten in Höhe von
 EUR [Summe] nebst Zinsen in Höhe von 5 Prozentpunkten über
 dem Basiszinssatz seit [Datum] zu zahlen.

3. Die Beklagte wird verurteilt, an den Kläger vorgerichtliche
 Anwaltskosten in Höhe von EUR [Berechnung nach RVG] zu zahlen.

4. Die Kosten des Rechtsstreits trägt die Beklagte.

5. Das Urteil ist gegen Sicherheitsleistung in Höhe von 110 %
 vorläufig vollstreckbar.

II. SACHVERHALT

Der Kläger unterhält bei der Beklagten eine
Berufsunfähigkeitszusatzversicherung (Police Nr. [Nr.]),
abgeschlossen am [Datum], monatliche Rente EUR [Betrag],
Beitragsbefreiung bei BU (Anlage K1 Police; Anlage K2 AVB).

Seit [Datum] ist der Kläger infolge [Erkrankung/Diagnose,
ICD-Code: [X]] nicht mehr in der Lage, seinen zuletzt als
[Beruf] ausgeübten Beruf zu mindestens 50 % auszuüben.

Sein Berufsbild umfasste im Einzelnen folgende Tätigkeiten:
1. [Tätigkeit, Zeitanteil %]
2. [Tätigkeit, Zeitanteil %]
3. [Tätigkeit, Zeitanteil %]
[Detailbeschreibung der körperlichen/kognitiven Anforderungen]

Der Kläger meldete die Berufsunfähigkeit am [Datum] bei der
Beklagten an (Anlage K3). Die Beklagte lehnte die Leistung
mit Schreiben vom [Datum] ab (Anlage K4).

III. FESTSTELLUNGSINTERESSE

Die Beklagte bestreitet die Leistungspflicht dem Grunde nach.
Das Feststellungsinteresse gemäß § 256 ZPO ist gegeben —
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

IV. RECHTLICHE WÜRDIGUNG

1. Versicherungsfall — Berufsunfähigkeit liegt vor
 Der Kläger ist nach ärztlichen Attesten (Anlagen K5–K8)
 und nach dem SV-Gutachten [Name] vom [Datum] (Anlage K9)
 seit [Datum] zu mindestens 50 % berufsunfähig bezogen
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

2. Keine Obliegenheitsverletzung
 [Ablehnungsgrund Versicherer + Widerlegung]

3. Kein Risikoausschluss einschlägig
 [AVB-Ausschluss-Klausel prüfen + ggf. Transparenzrüge]

V. BEWEISANGEBOTE

- Anlage K1: Police
- Anlage K2: AVB (Fassung [Datum/Version])
- Anlage K3: Schadensmeldung
- Anlage K4: Ablehnungsschreiben
- Anlage K5–K8: Ärztliche Atteste/Befundberichte
- Anlage K9: SV-Gutachten (ggf. gerichtliche Bestellung
 beantragt: Medizinischer SV des Fachgebiets [X])
- Zeuge: Behandelnder Arzt [Name, Adresse] zum Beweis der
 Diagnose und des Verlaufs
- Parteivernehmung Kläger § 448 ZPO zur Berufstätigkeit
 (hilfsweise)

[Kanzlei]
```

### Baustein 2 — PKH-Erklärung und Antrag (Kurzschema)

```
ANTRAG AUF PROZESSKOSTENHILFE
gemäß § 114 ZPO

mit der Bitte um Beiordnung:
Rechtsanwalt/Rechtsanwältin [Name, Kanzlei]

I. Wirtschaftliche Bedürftigkeit
Monatliches Nettoeinkommen: EUR [Betrag]
Abzüge: [Kosten Unterkunft, Unterhalt etc.]
Verfügbares Einkommen: EUR [unter Freibetrag]
Erklärung mit Belegen: Anlage PKH 1-4

II. Hinreichende Erfolgsaussichten
Die Klage ist hinreichend aussichtsreich, da
[Zusammenfassung Ablehnungsgründe + Widerlegung].

III. Bitte um Ratenzahlung
Monatlich EUR [Betrag] ab [Datum].

[Kanzlei]
```

### Baustein 3 — Streitverkündung an Versicherungsmakler

```
STREITVERKÜNDUNG § 72 ZPO

In dem Rechtsstreit [Az] verkünden wir dem

[Makler/Vermittler GmbH], [Adresse]

den Streit.

Für den Fall, dass die Klage gegen die Beklagte Versicherungs-AG
abgewiesen werden sollte, werden wir Ersatzansprüche gegen den
Streitverkündungsempfänger geltend machen, da er bei Abschluss
des Versicherungsvertrags nicht korrekt über die Anforderungen
an die Anzeigepflicht § 19 VVG / die AVB-Klauseln [X] belehrt hat.

Die Streitverkündung erfolgt zur Bindungswirkung für einen
etwaigen Folgeprozess (§ 74 ZPO).

[Kanzlei]
```

--- vor Versand klären ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen für ein klärenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## Beweislast und Darlegungslast

| Frage | Beweislast |
|---|---|
| Eintritt des Versicherungsfalls | Kläger (VN) |
| Grad der Berufsunfähigkeit | Kläger; SV-Gutachten |
| Schadenshöhe (Rückstände, künftige Rente) | Kläger (Police-Wert) |
| Obliegenheitsverletzung | Beklagte (Versicherer) |
| Kausalität Obliegenheit → Schaden fehlt | Kläger (§ 28 Abs. 3 VVG Exkulpation) |
| AVB-Klausel wirksam | Beklagte / Gericht (Transparenzprüfung) |
| Verjährungshemmung | Kläger |

## Fristen und Verjährung

| Frist | Dauer | Anker | Norm |
|---|---|---|---|
| Verjährung | 3 Jahre | Jahresende der Kenntnis | §§ 195, 199 BGB |
| Hemmung Ombudsstelle | Dauer + 6 Monate | Einleitung | § 204 Abs. 1 Nr. 4 BGB |
| Hemmung Verhandlungen | Dauer | Verhandlungsbeginn | § 203 BGB |
| Fälligkeit Versicherungsleistung | nach Abschluss Ermittlungen | Abschluss | § 14 Abs. 1 VVG |
| Streitverkündungsfrist für Regress | abhängig von Anspruch (typisch 3 Jahre) | Kenntnis Mangel | §§ 195, 199 BGB |

## Typische Gegenargumente und Reaktion

| Einwand Versicherer | Reaktion |
|---|---|
| BU-Grad unter 50 % | Eigenes SV-Gutachten vorlegen; gerichtlicher SV im Prozess; Berufsbildanalyse detailliert |
| Verweisung auf Vergleichsberuf | AVB auf abstrakte Verweisung prüfen; neuere AVB schließen häufig aus |
| Vorvertragliche Anzeigepflicht verletzt | Antragsfragebogen prüfen; Kausalität zwischen Nichtanzeige und Berufsunfähigkeit |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| PKH-Antrag abzuweisen wegen mangelnder Erfolgsaussichten | Konkrete Ablehnungsbegründung ist schwach; Erfolgsaussicht darlegen |
| Sachverständigenkosten zu hoch | § 379 ZPO-Vorschuss; bei PKH übernimmt Staatskasse; SV-Beauftragung notwendig |

## Streitwert und Kosten

- BU-Versicherung: 3,5-facher Jahreswert der Rente (§ 9 ZPO); bei 10 Jahren Restlaufzeit und EUR 1500/Monat = EUR 63000 Streitwert.
- Gerichtskostenvorschuss LG bei Streitwert EUR 63000: ca. EUR 1638 (GKG).
- Medizinischer SV-Vorschuss: EUR 2500–6000.
- Bei PKH-Bewilligung: Staatskasse trägt GKG-Vorschuss und SV-Kosten.
- Rechtsschutzversicherung: Deckungszusage vorab zwingend; ohne Zusage Eigenanteil des Mandanten.

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| BU — klarer medizinischer Befund | SV-Gutachten vorab einholen; Klageschrift mit Gutachten einreichen |
| BU — streitiger Grad | Feststellungsklage; gerichtlicher SV-Beweis; Berufsbild detailliert beschreiben |
| Sachschaden — Ablehnung ohne Substanz | Direktklage nach 2-Wochen-Fristsetzung |
| Streitwert unter EUR 10000 | AG-Verfahren; Ombudsstelle prüfen (bindend bis EUR 10000) |
| Verjährung naht | Klageeinreichung hemmt Verjährung ab Zustellung § 204 Abs. 1 Nr. 1 BGB |

## Anschluss-Skills

- `deckungsanfrage-pruefen` — Vorprüfung vor Klage
- `klage-versicherer-strategie` — Klagestrategie-Details
- `fachanwalt-versicherungsrecht-regress-abwehr` — Regress des Versicherers

## Quellen

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Vertiefung — Aktuelle Rechtsprechung und Normen

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Paragrafenkette

§ 256 ZPO (Feststellungsklage bei laufender BU-Rente) → § 215 VVG (örtliche Zuständigkeit Klage VN gegen Versicherer) → §§ 23, 71 GVG (sachliche Zuständigkeit AG/LG nach Streitwert) → § 1 VVG (Hauptleistungspflicht) → § 286 ZPO (Beweislast und freie Beweiswürdigung) → § 402 ZPO (gerichtlicher Sachverständiger) → § 114 ZPO (PKH bei Bedürftigkeit) → § 286 ZPO (Beweiswürdigung Privatgutachten)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Triage — Sofortprüfung Deckungsklage

1. **Zuständigkeit prüfen:** Streitwert ≤ 10.000 EUR → AG; > 10.000 EUR → LG. Örtlich: Wohnsitz VN (§ 215 VVG) oder Sitz Versicherer (§ 17 ZPO) — Wahlrecht beim Kläger.
2. **Klageantrag formulieren:** Laufende Rente → Feststellungsantrag § 256 ZPO; rückständige Beträge → Zahlungsantrag beziffert.
3. **Sachverständigenbeweis vorbereiten:** Privatgutachten als Anlage + Antrag auf gerichtliches Gutachten; Kosten-PKH prüfen.
4. **PKH-Berechtigung prüfen:** § 114 ZPO — ausreichende Erfolgsaussichten (Gutachtenlage) + Bedürftigkeit.
5. **Verjährung hemmen:** Bei Verhandlungen § 203 BGB; sonst Klageschrift einreichen vor Ablauf der 3-Jahres-Frist.

---

<!-- AUDIT 27.05.2026 — Bundle 027 Halluzinations-Reparatur
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
-->

---

## Skill: `versr-bafin-ombudsmann-aufsichtsbeschwerde`

_Wenn es um BaFin-Beschwerde, Versicherungsombudsmann, PKV-Ombudsmann und Klage taktisch wählen. in Fachanwalt Versicherungsrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik._

# BaFin-Beschwerde, Versicherungsombudsmann, PKV-Ombudsmann und Klage taktisch wählen.


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: SGB V §§ 27, 39, 92, 109, 137, 295, 301, RisikoStruktAusglV, SGB IV, SGB X, SGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** BaFin-Beschwerde, Versicherungsombudsmann, PKV-Ombudsmann und Klage taktisch wählen.

### FA Versicherungsrecht: BaFin und Ombudsmann

## Norm- und Quellenanker

- VVG §§ 214 ff. für außergerichtliche Streitbeilegung; VAG/BaFin-Aufsicht für Aufsichtsbeschwerde.
- Ombudsmann-Verfahrensordnungen live prüfen: Zuständigkeit, Streitwertgrenzen, Bindungswirkung, Verjährungshemmung, Ausschlüsse.
- ZPO/SGG/VwGO je nach Hauptrechtsweg nicht durch Beschwerdeverfahren ersetzen.
- BaFin prüft Aufsicht und Missstand, entscheidet aber typischerweise nicht den individuellen Zahlungsanspruch wie ein Gericht.

## Red Flags

- BaFin als Leistungsgericht
- Hemmung überschätzt
- falscher Ombudsmann
- Beschwerde ohne klares Ziel: Zahlung, erneute Prüfung, Aufsichtshinweis oder Vergleich
- Parallelfrist im Deckungsprozess läuft weiter

## Arbeitsstil

Konkrete Normen, konkrete Unterlagen, konkrete nächste Handlung. Keine pauschalen Empfehlungen; Rechtsprechung nur verifiziert mit Gericht, Datum, Aktenzeichen und frei zugänglicher Quelle.

---

## Skill: `klage-versicherer-strategie`

_Wenn es um Klagestrategie gegen Versicherer nach erfolgloser außergerichtlicher Korrespondenz in Fachanwalt Versicherungsrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik._

# Klagestrategie gegen Versicherer nach erfolgloser außergerichtlicher Korrespondenz


## Direktstart: lesen, entscheiden, liefern

Beginne nicht mit einem Fragenkatalog. Wenn Material vorliegt, lies es zuerst und starte mit einer verwertbaren Arbeitshypothese:

- Frist oder Sofortrisiko.
- erkannte Rolle, Zielrichtung und Verfahrensstand.
- tragende Tatsachen aus dem Material.
- bester nächster Arbeitsschritt mit direkt nutzbarem Output.

Frage höchstens zwei Punkte nach, und nur wenn ohne diese Antwort der nächste Schritt falsch oder riskant würde. Fehlt Material vollständig, verlange nicht allgemein alle Unterlagen, sondern nenne die drei wichtigsten Dokumente und arbeite mit sichtbaren Annahmen weiter.

Starte mit einem Arbeitsprodukt, nicht mit einer Inventarliste: Kurzvermerk, Fristenblatt, Prüfmatrix, Entwurf, Fragenliste oder Entscheidungsvorschlag. Routing ist nur Mittel zum Zweck. Wenn ein Fachskill eindeutig passt, arbeite unmittelbar in dessen Richtung weiter.

Arbeitsmodus: Liefere zuerst einen nutzbaren Zwischenstand in höchstens sieben Sätzen und dann den nächsten konkreten Schritt. Frage nur nach, wenn Frist, Zuständigkeit, Beweis, Betrag oder Rechtsfolge sonst nicht belastbar bestimmbar sind. Tabellen nur für Fristen, Belege, Beträge, Varianten oder Streitstoff.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: SGB V §§ 27, 39, 92, 109, 137, 295, 301, RisikoStruktAusglV, SGB IV, SGB X, SGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Klagestrategie gegen Versicherer nach erfolgloser außergerichtlicher Korrespondenz. Anwendungsfall alle außergerichtlichen Einigungsversuche sind gescheitert und Klage muss strategisch vorbereitet werden. Normen § 14 VVG Fälligkeit Verzug § 215 VVG örtliche Zuständigkeit § 204 BGB Hemmung § 256 ZPO Feststellungsantrag GVG Streitwert. Prüfraster Streitwert Zuständigkeit Klageantrag Substantiierung Beweisangebote Sachverständiger Zeugen Urkundenbeweis Mahnverfahren Zinsen Anwaltskosten. Output Klage-Strategie-Memo mit Antragsformulierung Beweiskonzept Kostenrisikobewertung. Abgrenzung zu fachanwalt-versicherungsrecht-deckungsklage und schriftsatzkern-substantiierung.

### Klage gegen Versicherer — Strategie

## Kaltstart-Rückfragen

1. Wurde das vollständige außergerichtliche Verfahren durchlaufen — Schadensanzeige, Stellungnahme, endgültige Ablehnung?
2. Welche Sparte — Sachversicherung (Hausrat/Gebäude), BU, Leben, Haftpflicht, Rechtsschutz, Cyber, D&O?
3. Ist die Hauptforderung bezifferbar (Leistungsklage) oder handelt es sich um künftige Rentenleistungen (Feststellungsklage § 256 ZPO)?
4. Streitwert: unter EUR 10000 (AG) oder darüber (LG)? Bei BU-Rente: 3,5-facher Jahreswert § 9 ZPO.
5. Besteht Rechtsschutzversicherung oder ist PKH (§ 114 ZPO) zu beantragen?
6. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
7. Wurde die Ombudsstelle eingeschaltet — Hemmungswirkung § 204 BGB dokumentiert?
8. Droht Verjährung (3 Jahre §§ 195, 199 BGB)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

### Normtexte (Kernauszug)

- **§ 1 VVG** — Versicherungspflicht; Grundlage der Leistungsklage.
- **§ 14 VVG** — Fälligkeit nach Abschluss nötiger Erhebungen; Abschlagszahlung § 14 Abs. 2 VVG.
- **§ 28 VVG** — Obliegenheitsverletzung; Leistungsfreiheit bei Vorsatz; quotal bei grober Fahrlässigkeit; Kausalität § 28 Abs. 3 VVG.
- **§ 81 VVG** — Herbeiführung Versicherungsfall grob fahrlässig; quotale Kürzung.
- **§ 215 VVG** — Gerichtsstand Wohnsitz des VN; Verbraucherschutz; alternativ allgemeiner Gerichtsstand Versicherer § 17 ZPO.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **§ 9 ZPO** — Streitwert bei wiederkehrenden Leistungen: 3,5-facher Jahreswert (deckelnder Wert bei kürzerer Restlaufzeit).
- **§§ 280, 286, 288 BGB** — Verzug; Zinsen 5 Prozentpunkte über Basiszinssatz; Ersatz Verzugsschadens (Anwaltskosten).
- **§§ 195, 199, 203, 204 BGB** — Verjährung 3 Jahre; Hemmung durch Verhandlungen, Ombudsstelle.
- **§ 114 ZPO** — Prozesskostenhilfe bei wirtschaftlicher Bedürftigkeit und hinreichenden Erfolgsaussichten.
- **§§ 305–310 BGB** — AGB-Kontrolle; § 305c Abs. 2 BGB Unklarheitenregel gegen Versicherer.

### Leitentscheidungen

| Gericht | Aktenzeichen | Datum | Kernaussage |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema in Tabellenform

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Nr. | Prüfschritt | Norm | Konsequenz |
|---|---|---|---|
| 1 | Klageart: Leistungsklage oder Feststellungsklage? | §§ 253, 256 ZPO | BU-Dauerleistung → Feststellungsantrag |
| 2 | Sachliche Zuständigkeit (Streitwert)? | §§ 23, 71 GVG; § 9 ZPO | AG bis EUR 10000; LG ab EUR 10000 |
| 3 | Örtliche Zuständigkeit? | § 215 VVG | Wohnsitz VN (Verbraucherschutz) |
| 4 | Verjährung noch nicht abgelaufen? | §§ 195, 199, 203, 204 BGB | Hemmung durch Ombudsstelle dokumentieren |
| 5 | Vollständige außergerichtliche Phase? | § 14 VVG | Pflicht zur Abmahnung vor Klage bei noch laufender Prüfung |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| 7 | Beweisführung Versicherungsfall? | Urkundenbeweis, SV, Zeugen | Alle Beweismittel benennen |
| 8 | Obliegenheitsverletzung des VN? | § 28 VVG | Kausalitätsdefense § 28 Abs. 3 VVG |
| 9 | Grob fahrlässige Herbeiführung? | § 81 VVG | Quotale Kürzung; Verschuldensgrad |
| 10 | Risikoausschluss-Klausel wirksam? | §§ 305c, 307 BGB | Unwirksam wenn intransparent |
| 11 | Verzug und Zinsen berechnet? | §§ 280, 286, 288 BGB | Ab Fälligkeit § 14 VVG oder Mahnung |
| 12 | Anwaltskosten außergerichtlich einklagbar? | § 249 BGB | Ab Verzugseinritt erstattungsfähig |
| 13 | Sachverständige bestellt / vorgesehen? | § 411 ZPO; § 379 ZPO | Bei BU: medizinischer SV; bei Sachschaden: technischer SV |
| 14 | PKH-Antrag oder Rechtsschutz-Deckung? | § 114 ZPO | Deckungszusage RS-Versicherung vorab |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu prüfen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Klage gegen Versicherer strategisch planen | Klagestrategie nach Prüfschema; Template unten |
| Variante A — Aussichten gut aber Vergleich schneller | Vergleichsverhandlung vor Klageerhebung einleiten |
| Variante B — Beweislage unsicher Sachverstaendiger noetig | Selbständiges Beweisverfahren zuerst; Klage nach Gutachten |
| Variante C — Mehrere Versicherer beteiligt Abstimmung noetig | Federführungs-Versicherer bestimmen; Klagen koordiniert stellen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Baustein 1 — Klageschrift Sachversicherung (Leistungsklage)

```
An das [Amtsgericht / Landgericht] [Ort]

KLAGESCHRIFT

[Vorname Nachname], [Adresse]
 — Kläger —
Prozessbevollmächtigte: Rechtsanwältinnen/Rechtsanwälte [Kanzlei]

gegen

[Versicherungs-AG], vertreten durch den Vorstand
 — Beklagte —

wegen Versicherungsleistung (Hausrat/Gebäude/[Sparte])
Streitwert: EUR ____

I. ANTRÄGE

1. Die Beklagte wird verurteilt, an den Kläger EUR [Hauptforderung]
 nebst Zinsen in Höhe von 5 Prozentpunkten über dem Basiszinssatz
 seit [Datum Verzugseinritt] zu zahlen.

2. Die Beklagte wird verurteilt, an den Kläger vorgerichtliche
 Anwaltskosten in Höhe von EUR [Betrag] (1,3 Geschäftsgebühr
 Nr. 2300 VV RVG aus EUR [Gegenstandswert] + USt + Auslagen)
 zu zahlen.

3. Die Kosten des Rechtsstreits trägt die Beklagte.

4. Das Urteil ist gegen Sicherheitsleistung in Höhe von 110 %
 des zu vollstreckenden Betrags vorläufig vollstreckbar.

II. SACHVERHALT

Am [Datum] ereignete sich [Versicherungsfall] an dem vom Kläger
bei der Beklagten versicherten Objekt / in dem versicherten
Haushalt / bei dem versicherten Unternehmen. Einzelheiten [Anlage K1
Polizeibericht / Schadensprotokoll].

Der Kläger unterhält bei der Beklagten eine [Hausrat-/Gebäude-/
Kfz-]Versicherung, Police Nr. [Nr.], Anlage K2.

Die Beklagte lehnte die Leistung mit Schreiben vom [Datum],
Anlage K3, ab.

III. RECHTLICHE WÜRDIGUNG

1. Versicherungsfall liegt vor (vgl. § [X AVB])
 [Subsumtion]

2. Ablehnungsgrund trägt nicht
 [Obliegenheitsverletzung fehlt / Risikoausschluss unwirksam /
 Kausalität fehlt § 28 Abs. 3 VVG]
 BGH-Rechtsprechung zu Transparenzgebot (§ 307 Abs. 1 S. 2 BGB).

3. Fälligkeit und Verzug
 Der Anspruch ist gemäß § 14 VVG fällig. Verzug trat am
 [Datum] ein (Ablauf der Frist aus Anwaltsschreiben Anlage K4).

IV. BEWEISANGEBOTE

- Anlage K1: [Schadensnachweis]
- Anlage K2: Versicherungsschein mit AVB
- Anlage K3: Ablehnungsschreiben
- Sachverständigengutachten zum Nachweis des Schadens:
 Sachverständiger [Name] oder gerichtlich zu bestellen
- Zeuge: [Name, Anschrift, Beweisthema]

[Rechtsanwälte]
```

### Baustein 2 — Klageschrift Berufsunfähigkeitsversicherung (Feststellungsklage)

```
II. ANTRÄGE BU-VERSICHERUNG

1. Es wird festgestellt, dass die Beklagte verpflichtet ist, dem
 Kläger ab dem [Datum] aus dem Versicherungsvertrag (Police Nr.
 [Nr.]) eine monatliche Berufsunfähigkeitsrente in Höhe von
 EUR [X] sowie Beitragsbefreiung zu gewähren, solange Berufs-
 unfähigkeit von mindestens 50 % im Beruf des Klägers als
 [Berufsbezeichnung] besteht.

2. Die Beklagte wird verurteilt, die aufgelaufenen Rückstände
 für den Zeitraum [Beginn] bis [aktuell] in Höhe von EUR [X]
 nebst Zinsen von 5 % über Basiszinssatz ab [Datum] zu zahlen.

III. VERSICHERUNGSFALL BERUFSUNFÄHIGKEIT

Der Kläger ist seit [Datum] infolge [Diagnose, ICD-Code] zu
mindestens 50 % außerstande, seinen Beruf als [Bezeichnung]
auszuüben. Sein konkretes Berufsbild umfasste folgende Tätigkeiten:
[Detailbeschreibung der Haupttätigkeiten mit Zeitanteilen].

Beweis: Sachverständigengutachten bezogen auf die konkrete
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Eine Verweisung auf Vergleichsberufe ist nach § [X] AVB
ausgeschlossen / nach aktuellen AVB nicht vorgesehen.

IV. FESTSTELLUNGSINTERESSE

Feststellungsinteresse besteht, da die Beklagte die Leistungspflicht
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
```

### Baustein 3 — Antrag auf Prozesskostenhilfe

```
ANTRAG AUF PROZESSKOSTENHILFE
gemäß § 114 ZPO

[Kläger] beantragt Prozesskostenhilfe unter Beiordnung der
unterzeichneten Rechtsanwältinnen / Rechtsanwälte.

I. Wirtschaftliche Bedürftigkeit
[Kläger] ist nicht in der Lage, die Prozesskosten aufzubringen.
PKH-Erklärung mit Belegen liegt bei (Anlage PKH 1).

II. Hinreichende Erfolgsaussichten
[Zusammenfassung der Klagebegründung]

Die Klage hat hinreichende Erfolgsaussichten, da [...]
und der Beklagte keine tragfähige Ablehnung begründet hat.

III. Ratenzahlung
Ratenzahlung in Höhe von EUR [Betrag] monatlich wird angeboten.

[Rechtsanwälte]
```

--- vor Versand klären ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen für ein klärenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## Beweislast und Darlegungslast

| Frage | Beweislast |
|---|---|
| Versicherungsfall — Eintritt | Kläger (VN) |
| Schadenshöhe, Leistungsumfang | Kläger |
| Obliegenheitsverletzung | Beklagte (Versicherer) |
| Kausalität Obliegenheit → Schaden fehlt | Kläger (Exkulpation § 28 Abs. 3 VVG) |
| Grob fahrlässige Herbeiführung | Versicherer |
| AVB-Klausel unwirksam (Transparenz) | Gericht von Amts wegen; Kläger regt an |
| Verjährung / Hemmung | Kläger für Hemmung; Beklagte für Ablauf |

## Fristen und Verjährung

| Frist | Dauer | Anker | Norm |
|---|---|---|---|
| Verjährung Versicherungsanspruch | 3 Jahre | Jahresende der Kenntnis | §§ 195, 199 BGB |
| Hemmung Ombudsstelle | Dauer des Verfahrens + 6 Monate | Einleitung | § 204 Abs. 1 Nr. 4 BGB |
| Hemmung Verhandlungen | Dauer | Verhandlungsbeginn | § 203 BGB |
| Antwortfrist Versicherer | keine gesetzliche Frist | ggf. setzen: 4 Wochen | § 14 VVG analog |
| Zustellung der Klageschrift | alsbald nach Einreichung § 167 ZPO | Klageeinreichung hemmt Verjährung | § 204 Abs. 1 Nr. 1 BGB |

## Typische Gegenargumente und Reaktion

| Einwand Versicherer | Reaktion |
|---|---|
| Versicherungsfall nicht eingetreten | AVB-Definition schmal auslegen versuchen; § 305c Abs. 2 BGB gegen Versicherer |
| Obliegenheitsverletzung — Verspätete Anzeige | § 28 Abs. 3 VVG: Kausalität; fehlende Kausalität beseitigt Leistungsfreiheit |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Forderung verjährt | Hemmungszeiträume (Ombudsstelle, Verhandlungen) in Rechnung stellen |
| AVB-Ausschluss eindeutig | Transparenztest § 307 Abs. 1 S. 2 BGB; Auslegung § 305c Abs. 2 BGB |
| Mahnverfahren zumutbar | Bei BU oder Feststellungsklage: Mahnverfahren ungeeignet; direkte Klage |

## Streitwert und Kosten

- Sachversicherung: Streitwert = Hauptforderung; RVG-Gebühren danach.
- BU-Versicherung: 3,5-facher Jahreswert der Rente (§ 9 ZPO); bei kurzer Restlaufzeit weniger.
- Gerichtskostenvorschuss: bei LG-Verfahren oft EUR 500–3000; bei PKH von Staatskasse.
- Sachverständigenkostenvorschuss § 379 ZPO: medizinischer SV ca. EUR 2000–5000; bei PKH Staatskasse.
- Anwaltsgebühren außergerichtlich erstattungsfähig ab Verzug.

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Klarer Versicherungsfall, endgültige Ablehnung | Direkt Klage; kein weiteres Schreiben |
| BU — streitig über Grad | SV-Gutachten vor Klage einholen; Feststellungsantrag kombiniert mit Rückstandsantrag |
| Vergleich möglich | Schriftliches Vergleichsangebot vor Klagezustellung; Verhandlung hemmt Verjährung |
| Streitwert unter EUR 5000 | Ombudsstelle-Empfehlung bindend bis EUR 10000; weniger kostspielig |
| AVB-Klausel zweifelhaft | Transparenzargument schon im Klageschriftsatz ausführlich begründen |

## Anschluss-Skills

- `deckungsanfrage-pruefen` — Vorprüfung Deckungsablehnung
- `fachanwalt-versicherungsrecht-deckungsklage` — formale Klageschrift-Details
- `fachanwalt-versicherungsrecht-regress-abwehr` — Abwehr von Regress-Ansprüchen

## Quellen

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Vertiefung — Aktuelle Rechtsprechung und Normen

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§ 286 Abs. 2 Nr. 3 BGB (Verzug durch Ablehnungsschreiben ohne Mahnung) → § 288 BGB (Verzugszinsen) → § 204 BGB (Hemmung durch Klage, Mahnbescheid, Schlichtungsantrag) → § 215 VVG (örtliche Zuständigkeit Klage VN) → § 281 ZPO (Mahnverfahren, Widerspruch, Abgabe) → § 256 ZPO (Feststellungsklage BU/laufende Leistung)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

---

## Anwendungshinweise

1. Diesen Vollprüfung als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.
