# Vollprüfung: fachanwalt-verkehrsrecht

## Zusammensetzung

Dieser Vollprüfung enthaelt top-10 von 77 Skills des Plugins `fachanwalt-verkehrsrecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Wenn es um Anwalts-Dashboard Fachanwalt Verkehrsrecht in Fachanwalt Verkehrsrecht geht: klärt Rolle, Ziel, Frist, Unterl…
2. **mandat-triage-verkehrsrecht** — Wenn es um Neues Verkehrsrechtsmandat kommt rein und Anwalt muss Sachgebiet klären und Fristen prüfen in Fachanwalt Verk…
3. **fachanwalt-verkehrsrecht-orientierung** — Wenn es um Fachanwalt für Verkehrsrecht — Orientierung in Fachanwalt Verkehrsrecht geht: prüft Frist, Form, Zuständigkei…
4. **erstgespraech-mandatsannahme** — Wenn es um Erstgespraech Mandatsannahme in Fachanwalt Verkehrsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg un…
5. **erstpruefung-und-mandatsziel** — Wenn es um Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel in Fachanwalt Verkehrsrecht geht: klärt Rolle, Ziel, F…
6. **fachanwalt-verkehrsrecht-regulierungsanforderung** — Wenn es um Regulierungsanforderung in Fachanwalt Verkehrsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sof…
7. **regulierungsanforderung** — Wenn es um Regulierungsanforderung in Fachanwalt Verkehrsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sof…
8. **versicherer-quotenverhandlung-vergleich** — Wenn es um Versicherer hat Regulierung angeboten und Anwalt verhandelt Quotenerhöhung oder Vergleich in Fachanwalt Verke…
9. **verk-fahrerlaubnisrecht-leitfaden** — Wenn es um Leitfaden Fahrerlaubnisrecht: Entziehung, MPU, Sperrfrist, vorzeitige Wiedererteilung in Fachanwalt Verkehrsr…
10. **bussgeldbescheid-pruefen** — Wenn es um Mandant hat OWi-Bußgeldbescheid erhalten und Anwalt prüft ob Einspruch sinnvoll ist in Fachanwalt Verkehrsrec…

---

## Skill: `einstieg-routing`

_Wenn es um Anwalts-Dashboard Fachanwalt Verkehrsrecht in Fachanwalt Verkehrsrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Anwalts-Dashboard Fachanwalt Verkehrsrecht

> Bußgeld, Fahrerlaubnis, Unfallregulierung, Trunkenheitsfahrt — drei Aktenbündel, oft parallel: OWi/Straf, FE-Behörde, Versicherer.
>
> Sie sehen unten die Sofort-Triage. Keine Rückfragen, bis die Tabelle steht. Wenn die Akte 80 % trägt, gehen wir direkt zum Anschluss-Skill — Sie entscheiden, ob.

## Sofort-Triage

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
| --- | --- | --- |
| Rolle | Wen vertrete ich? (Mandant · Gegenseite · Mehrere) | Mandantenmail, Vertretungsbestellung |
| Verfahrensstand | Vorprozessual · außergerichtlich · Klage · Rechtsmittel · Vollstreckung | Vorhandene Schriftsätze, Eingangsstempel |
| Eilfrist | **§ 67 OWiG: 2 Wochen** Einspruch Bußgeldbescheid ab Zustellung. § 80 III VwGO: Widerspruch gegen FE-Entzug 1 Monat. § 41 RL 2009/103/EG / § 115 VVG: Direktanspruch Versicherer (keine Verjährungsfalle, aber Verzug nach 6 Wochen). | Frist aus Zugangs-/Kenntnisdatum berechnen |
| Hauptanspruch | OWi-Verteidigung (§§ 66, 67 OWiG), Straffahrlässigkeit/Vorsatz (§§ 315c, 316 StGB, § 21 StVG, § 24a StVG), Schadensersatz aus Unfall §§ 7 StVG, 18 StVG, 17 StVG (Quote), §§ 823, 249 BGB, 253 II BGB (Schmerzensgeld), Direktanspruch § 115 VVG. | Sachverhaltsabgleich mit Tatbestandsmerkmalen |
| Zuständigkeit | OWi: AG am Tatort (§ 68 OWiG). Strafsachen: AG/LG nach §§ 24 ff. GVG. FE-Sache: Verwaltungsbehörde + VG. Zivilrechtlich: Wahlrecht §§ 17, 32 ZPO, AG/LG je Streitwert. | Gesetz, Vertrag, Gerichtsstandsklausel |

## Risiko-Ampel

- **Frist:** 🔴 Bußgeld-Einspruch (2 Wochen) tickt ab Zustellung; Datum aus Akte verifizieren. 🟠 Verjährung OWi: 3 Monate bis Anhörung, 6 Monate gesamt (§ 26 III StVG für StVO-Verstöße).
- **Beweislage:** 🟠 Messverfahren: Eichschein, Bauartzulassung, Toleranzabzug. 🔴 Trunkenheit: BAK-Analyse, Blutprobenrichter (§ 81a StPO!).
- **Wirtschaftlich:** 🟠 1-Monats-Fahrverbot: Schonfrist § 25 IIa StVG (Beruf!). 🔴 FE-Entzug: MPU-Risiko und 6-Monats-Wiedererteilungssperre § 69a StGB.

## Anschluss-Skills (Router)

| Wenn der Fall trägt … | dann Skill | Erwartung |
| --- | --- | --- |
| **Bußgeldbescheid eingegangen** | `bussgeld-einspruch-pruefen` | Einspruch fristgerecht, Akteneinsicht, Messverfahren-Check |
| Fahrerlaubnis-Entzug droht | `fahrerlaubnis-entzug` | MPU-Anordnung prüfen, vorläufige Entziehung § 111a StPO |
| MPU steht an | `mpu-vorbereitung` | Begutachtungsanlass, Abstinenzbelege, Vorbereitungsphase |
| Unfallregulierung Versicherer | `verk-unfallregulierung-workflow` | Haftungsquote, Schadensersatzpositionen, Anlagensatz § 287 ZPO |
| Trunkenheits-/Drogenfahrt | `verk-trunkenheit-drogenfahrt-spezial` | BAK/AAK-Bewertung, § 316 StGB vs. § 24a StVG, FE-Folgen |

## Norm-Radar (live verifizieren)

- **§ 67 OWiG** — Einspruchsfrist 2 Wochen Bußgeld
- **§ 25 StVG** — Fahrverbot; Schonfrist Abs. 2a
- **§ 69 StGB** — Entziehung Fahrerlaubnis; Wiedererteilungssperre § 69a
- **§ 316 StGB** — Trunkenheit im Verkehr
- **§ 7 StVG** — Halterhaftung Unfall
- **§ 115 VVG** — Direktanspruch gegen KH-Versicherer

## Genau eine Rückfrage (nur wenn nötig)

> Welche **Schiene** dominiert (OWi/Straf · FE-Behörde · Versicherer-Regulierung) — und welche Frist tickt zuerst?

Wenn die Akte die Frage selbst beantwortet, **diese überspringen** und direkt den passenden Anschluss-Skill arbeiten.

## Leitentscheidungs-Anker (Such-Wegweiser, keine fertigen Zitate)

- **Standardisiertes Messverfahren** — BGH 4. Strafsenat (Linie seit 1997) — *live verifizieren auf* `bundesgerichtshof.de`
- **Akteneinsicht in Rohmessdaten (OWi)** — BVerfG 2. Senat (Beschluss v. 12.11.2020) — *live verifizieren auf* `bundesverfassungsgericht.de`
- **Halterhaftung § 7 StVG; Höhere Gewalt** — BGH VI. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Direktanspruch § 115 VVG gegen KH-Versicherer** — BGH IV. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`

> Diese Anker sind Sucheinstieg. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle prüfen und Datum, Aktenzeichen, Randnummer abklären. Kuratierte Anker-Sammlung in `references/leitentscheidungen-anker.md`.

## Hinweis

Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Die Konvention dieses Einstiegs-Dashboards steht in `references/anwalts-dashboard-konvention.md`.

---

## Skill: `mandat-triage-verkehrsrecht`

_Wenn es um Neues Verkehrsrechtsmandat kommt rein und Anwalt muss Sachgebiet klären und Fristen prüfen in Fachanwalt Verkehrsrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Neues Verkehrsrechtsmandat kommt rein und Anwalt muss Sachgebiet klären und Fristen prüfen


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
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StVG; PflVG; §§ 315c 316 StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Neues Verkehrsrechtsmandat kommt rein und Anwalt muss Sachgebiet klären und Fristen prüfen. Eingangs-Triage Verkehrsrecht. Prüfraster: Verfahrensart (Zivilrecht Schadensregulierung OWi Strafrecht Fahrerlaubnis) Unfallart Fristen (Einspruch OWi 2 Wochen § 67 OWiG Verjährung 3 Jahre § 195 BGB) Versicherungslage Eilbedürftigkeit vorläufige Entziehung § 111a StPO. Output: Routing-Entscheidung mit Folge-Skill. Abgrenzung zu fachanwalt-verkehrsrecht-orientierung (Orientierung) und bußgeld-einspruch-prüfen.

### Mandat-Triage Verkehrsrecht

## Ablauf — sieben Fragen

### Frage 1 — Wer ruft und für wen?

- Selbst Unfallbeteiligter
- Angehöriger
- Versicherer (Verteidigungsmandat)
- Anderer Anwalt (Vertretung)

### Frage 2 — Verfahrensart?

- **Zivilrechtlich** Schadensregulierung
- **Owi** Bußgeldbescheid wegen Geschwindigkeit Rotlicht Abstand Handy am Steuer Trunkenheit
- **Strafrechtlich** Verkehrsstraftat (§ 315c StGB Gefährdung § 315d Raserfälle § 142 Unfallflucht § 316 § 315a Trunkenheit § 229 fahrlässige Körperverletzung § 222 fahrlässige Tötung)
- **Fahrerlaubnisrecht** vorläufige Entziehung Wiedererteilung MPU
- **Versicherungsrecht** Deckungsablehnung Kasko Haftpflicht
- **Fahrerlaubnisrecht-Punkte** Fahreignungsregister (FAER) Tilgung

### Frage 3 — Akute Eilbedürftigkeit?

- Vorläufige Entziehung Fahrerlaubnis § 111a StPO — sofort Beschwerde § 304 StPO
- Berufstätigkeit auf Führerschein angewiesen — Härtefall-Argumentation
- Fahrtenbuch-Auflage drohend
- Hauptverhandlung Strafrecht binnen Tagen

### Frage 4 — Unfall: Personen- oder Sachschaden?

- Sachschaden — Standard-Regulierung
- Personenschaden — zusätzliche Quoten Schmerzensgeld Vorhaltekosten Heilbehandlungskosten Renten-Anspruch
- Bei Personenschaden sofort SV-Träger informieren (Krankenkasse BG)

### Frage 5 — Versicherungslage?

- Eigene Haftpflicht (Vollkasko)
- Verkehrsrechtsschutz (Deckungszusage einholen)
- Insassenunfallversicherung
- Gegnerische Versicherung bekannt?

### Frage 6 — Frist?

- **Einspruch Bußgeldbescheid** zwei Wochen § 67 OWiG
- **Anhörung im Bußgeldverfahren** keine zwingende Frist aber Bedeutung der Aussage
- **Verjährung zivilrechtlicher Anspruch** drei Jahre § 195 BGB
- **Verjährung Personenschaden** dreißig Jahre § 199 Abs. 2 BGB
- **Punkte-Tilgung** Fahreignungsregister
- **Wiedererteilung Fahrerlaubnis** Sperrfrist § 69a StGB

### Frage 7 — Hauptaktenstand?

- Polizeiprotokoll vorhanden?
- Schadensgutachten vorhanden?
- Anhörungsbogen StA / Bußgeldstelle?
- Bisheriger Schriftwechsel mit Versicherung?

## Routing-Matrix

| Verfahrensart | Folge-Skill | Frist-Sofort-Check |
|---|---|---|
| Schadensregulierung Sachschaden | `unfall-haftungsquote-berechnen` | Verjährung drei Jahre |
| Schadensregulierung Personenschaden | `unfall-haftungsquote-berechnen` plus medizinische Begutachtung | drei oder dreißig Jahre |
| Bußgeldbescheid | (Skill bußgeld-prüfen — perspektivisch) | zwei Wochen § 67 OWiG |
| Vorläufige Entziehung FE | sofort Beschwerde § 304 StPO | binnen Stunden |
| Verkehrsstraftaten | Skill aus `fachanwalt-strafrecht` `mandat-triage-strafrecht` | je nach Verfahrensstadium |
| MPU | (Skill mpu-vorbereitung — perspektivisch) | sechs Monate vor Frist Beginn |
| Punkte | (Skill faer-prüfen — perspektivisch) | Tilgungsfristen |
| Versicherungs-Deckungsstreit | Skill aus `fachanwalt-versicherungsrecht` | nach VVG |

## Eilmodus vorläufige Entziehung

Bei Fahrerlaubnis-vorläufig-entzogen § 111a StPO:

- **Beschwerde § 304 StPO** statthaft
- Hilfsweise Antrag auf Aufhebung beim selben Gericht
- Eilbedürftigkeit Beruf häufig führt zu Beschluss in der Sache
- Bei Hauptverhandlung Plädoyer auf Aussetzung § 69a StGB Sperrfrist nicht erforderlich

## Mandatsannahme

- **Konflikt-Check** — kein anderer Mandant in derselben Sache (Unfallgegner Versicherer Mitfahrer)
- **Streitwert** ab EUR 10000 LG; darunter AG (Streitwertgrenze zehntausend Euro seit 01.01.2026 Justizreform)
- **Komplexität** Personenschaden Eigentums-Streit über Halterstellung Auslandsbezug Lkw-Frachtrecht

## Eskalation

- **Telefon-Sofort** vorläufige FE-Entziehung
- **Binnen einer Stunde** Verkehrsunfallflucht-Anhörung
- **Heute** Versicherungs-Reaktion auf Deckungsablehnung Akteneinsicht Bußgeld
- **Diese Woche** Klageeinreichung Schadensregulierung Einspruch Bußgeld

## Ausgabe

- `triage-protokoll-verkehrsrecht.md`
- Aktenanlage Az-Vorschlag
- Frist im Fristenbuch
- Rechtsschutz-Deckungsanfrage als Entwurf
- Mandatsvereinbarung Vorlage
- Empfehlung Folge-Skill

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Quellen

- StVG StVO StPO §§ 111a 304
- StGB §§ 142 222 229 315a 315c 315d 316 69 69a
- OWiG § 67 (Einspruch)
- VVG §§ 28 86 115
- BGH VI. Zivilsenat 4. Strafsenat

## Aktuelle Rechtsprechung Triage (Stand Mai 2026)

Verifizierte Aktenzeichen mit offener Quelle (vor Versand jeweils Volltext in der angegebenen Quelle aufrufen):

- BGH VI ZR 253/22, Urt. v. 16.1.2024 — Werkstattrisiko (juris.bundesgerichtshof.de)
- BGH VI ZR 239/22, Urt. v. 16.1.2024 — Werkstattrisiko bei fiktiver Abrechnung (juris.bundesgerichtshof.de)
- BGH VI ZR 280/22, Urt. v. 12.3.2024 — Sachverstaendigenrisiko (juris.bundesgerichtshof.de)
- BGH VI ZR 12/24, Urt. v. 5.11.2024 — Haushaltsfuehrungsschaden / Mindestlohn (juris.bundesgerichtshof.de)
- BGH VI ZR 24/25, Urt. v. 14.10.2025 — Substantiierungsanforderungen Art. 103 Abs. 1 GG (juris.bundesgerichtshof.de)
- BVerwG 3 B 2.24, Beschl. v. 8.1.2025 — Cannabis und KCanG (bverwg.de)
- BVerfG 2 BvR 1167/20, Beschl. v. 20.6.2023 — Rohmessdaten Geschwindigkeitsmessung (bundesverfassungsgericht.de)
- BVerfG 2 BvR 1616/18, Beschl. v. 12.11.2020 — Akteneinsicht / Informationszugang OWi (bundesverfassungsgericht.de)

<!-- AUDIT 27.05.2026: BGH VI ZR 1/21 (NOT_FOUND auf dejure.org) entfernt und ersetzt durch BGH VI ZR 37/99, NJW 2000, 861 (verifiziert auf dejure.org). -->

---

## Skill: `fachanwalt-verkehrsrecht-orientierung`

_Wenn es um Fachanwalt für Verkehrsrecht — Orientierung in Fachanwalt Verkehrsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Fachanwalt für Verkehrsrecht — Orientierung

## FAO-Voraussetzungen

- Lehrgang 120 Stunden + drei Klausuren.
- 80 Fälle in den letzten drei Jahren, davon mindestens 60 streitige.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| Haftung | §§ 7 ff. StVG (Halterhaftung) § 18 StVG (Führer) § 823 BGB (Verschuldenshaftung) |
| Versicherung | PflVG VVG §§ 100 ff. VVG (Haftpflicht) §§ 86 ff. VVG (Kasko) |
| Straßenverkehrsrecht | StVO StVZO FeV |
| Bußgeld | OWiG StPO §§ 67 ff. OWiG |
| Verkehrsstrafrecht | §§ 315b 315c 315d 316 StGB (Trunkenheit Straßenverkehrsgefährdung) § 142 StGB (Unfallflucht) |
| Schadensrecht | §§ 249 ff. BGB Naturalrestitution Differenzhypothese Wertminderung Nutzungsausfall |

## Typische Mandate

- Unfallregulierung Schadensersatz
- Personenschaden (Schmerzensgeld Erwerbsschaden)
- Schmerzensgeld nach BGH-Tabellen
- Bußgeldverfahren OWi
- Fahrerlaubnisrecht (Entziehung Wiedererteilung MPU)
- Verkehrsstrafrecht
- Versicherungsstreit (Haftpflicht Vollkasko)

## Fristen

- **Bußgeldverfahren** Einspruch zwei Wochen (§ 67 OWiG).
- **Klagefrist Verwaltungsgericht** ein Monat (§ 74 VwGO) z. B. Fahrerlaubnisentzug.
- **Verjährung** Schadensersatz nach Unfall regelmäßig drei Jahre (§ 195 BGB).
- **Direktanspruch** gegen Versicherer drei Jahre.

## Hauptgerichte

- Amtsgericht Buss- und Strafsachen erstinstanzlich.
- Landgericht Zivilrechtliche Klagen über 10.000 EUR.
- OLG / BGH Revisionsinstanz.
- Verwaltungsgericht bei Fahrerlaubnis.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Berufsverband

- ADAC ARGE Verkehrsrecht DAV.

## Schnittstellen

- **kanzlei-allgemein** Fristenbuch Timesheet.
- **fachanwalt-versicherungsrecht** bei Versicherungsstreit.
- **fachanwalt-strafrecht** bei Verkehrsstrafrecht.

## Aktuelle Rechtsprechung Verkehrsrecht

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

---

## Skill: `erstgespraech-mandatsannahme`

_Wenn es um Erstgespraech Mandatsannahme in Fachanwalt Verkehrsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Strukturierter Erstgespraechsleitfaden für Verkehrsrecht (Unfall-, OWi- und Verkehrsstrafrecht): Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen.


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StVG; PflVG; §§ 315c 316 StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Strukturierter Erstgespraechsleitfaden für Verkehrsrecht (Unfall-, OWi- und Verkehrsstrafrecht): Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen.

### Erstgespraech und Mandatsannahme im Verkehrsrecht (Unfall-, OWi- und Verkehrsstrafrecht)

## Wann dieser Arbeitsgang greift

- Neue Anfrage aus dem Bereich Verkehrsrecht (Unfall-, OWi- und Verkehrsstrafrecht) (Telefon, Mail, Empfehlung, Walk-in).
- Mandantin oder Mandant beschreibt Sachverhalt unstrukturiert; viele Anlagen ohne System.
- Vor jeder weiteren fachlichen Bearbeitung: erst Annahme klären, Konflikt- und GwG-Prüfung, Vollmacht, Streitwert/Vereinbarung, Fristen.

## Phasen des Erstgespraechs

### 1. Aufnahme der Konstellation (10-15 Min.)

Standard-Fragenraster für Verkehrsrecht (Unfall-, OWi- und Verkehrsstrafrecht):

- Beteiligte (Vor-/Nachname, Geburtsdatum, Anschrift, Rolle: Klägerin/Beklagter, Antragsteller, Beschuldigter)
- Konflikt-Kern in einem Satz ("Was ist Ihr Ziel?")
- Konkrete fachliche Stossrichtung: Unfallregulierung, OWi, Punktekonto, MPU, Fahrerlaubnis, KFZ-Versicherung
- Bisherige Korrespondenz (Bescheide, Schreiben der Gegenseite, anwaltliche Vertretung der Gegenseite?)
- **Fristenscreening sofort:** anstehende Klage-/Widerspruchs-/Einspruchsfristen aus den vorgelegten Schreiben (z.B. Klage Verkehrsunfall, Einspruch OWi-Bussgeldbescheid, Klage KFZ-Versicherung). Frist-Alarm an die Vorbereitung weitergeben.

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

Standard-Streitwerte im Bereich Verkehrsrecht (Unfall-, OWi- und Verkehrsstrafrecht):

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

- BORA, BRAO, FAO für Fachanwaltschaft Verkehrsrecht (Unfall-, OWi- und Verkehrsstrafrecht).
- GwG, GwGMeldV, Identifizierungsleitfaden BRAK.
- StVG, StVO, StVZO, FeV, PflVG, BKatV, OWiG (für fachliche Erstpruefung).
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

Mandantin kommt am Donnerstag, Frist laeuft am Montag (Klage- oder Widerspruchsfrist im Bereich Verkehrsrecht (Unfall-, OWi- und Verkehrsstrafrecht)). Handlungs-Sequenz:

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
- Verfahrensdauer im Bereich Verkehrsrecht (Unfall-, OWi- und Verkehrsstrafrecht): Erfahrungswerte nach Instanz.
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

## Aktuelle Rechtsprechung Erstgespraech Verkehrsrecht

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Normen Erstgespraech Verkehrsrecht

- § 67 OWiG — Einspruchsfrist Bussgeldbescheid (2 Wochen)
- § 195 BGB — allgemeine Verjährungsfrist 3 Jahre (Unfall-Schadensersatz)
- § 199 Abs. 2 BGB — Hoechstfrist 30 Jahre bei Personenschaden
- §§ 10-17 GwG — Identifizierungs- und Sorgfaltspflichten
- § 9 RVG — Vorschussanforderung
- §§ 3a, 4a RVG — schriftliche Honorarvereinbarung, Erfolgshonorar-Schranken

<!-- AUDIT 27.05.2026
Geprüfte AZ (task_270.json, 3 Probleme):
1. BGH VI ZR 168/15 (NOT_FOUND): dejure.org meldet "Keine Entscheidung gefunden". Zeile ersatzlos geloescht.
2. BGH VI ZR 261/16 (WRONG_TOPIC): Echtes Thema laut dejure.org = Vererblichkeit des Anspruchs auf Geldentzuendigung (Persoenlichkeitsrecht), BGHZ 215, 117, NJW 2017, 3004 — nicht "Fristversaeumnis durch Kanzlei, NJW 2017, 2601". Zeile ersatzlos geloescht.
3. BGH VI ZR 4/22 (NOT_FOUND): dejure.org meldet "Keine Entscheidung gefunden". Zeile ersatzlos geloescht.
Frontmatter unveraendert. Kein Commit. Bearbeiter: KI-Audit-Agent.
-->

---

## Skill: `erstpruefung-und-mandatsziel`

_Wenn es um Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel in Fachanwalt Verkehrsrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StVG; PflVG; §§ 315c 316 StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel.

## Spezialwissen: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** StVG, StVO, PflVG, VVG.

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

## Fachanwalt-Verkehr Erstpruefung Mandatsziel Bausteine
- **Saeule-Identifikation in der Triage:**
 - (a) Verkehrszivilrecht (Unfall, Schadenersatz, Versicherer-Streit).
 - (b) Verkehrs-OWi (Bussgeldbescheid, Punkte, Fahrverbot).
 - (c) Verkehrsstrafrecht (§§ 142, 222, 229, 315 ff., 316 StGB).
 - (d) Verkehrsverwaltungsrecht (FeV-Entziehung, MPU, Wiedererteilung).
 - (e) Versicherungsrecht (Kasko-Ablehnung, Insassenversicherung).
- **Rolle-Klärung:** Geschaedigter, Schaediger, Halter, Fahrer, Versicherungsnehmer, Beschuldigter, Antragsteller FE-Wiedererteilung; ggf. mehrere Rollen parallel.
- **Mandatsziel-Hierarchie nach Saeule:**
 - **Zivil:** Schaden vollumfaenglich; Mietwagen / Nutzungsausfall; Wertminderung; Personenschaden Schmerzensgeld § 253 BGB.
 - **OWi:** Fahrverbot abwenden, Punkte vermeiden, Geldbusse reduzieren.
 - **Strafrecht:** Schuldspruch vermeiden, Strafmilderung, Fahrerlaubnis erhalten / wiedererlangen.
 - **Verwaltungsrecht:** MPU-Vorbereitung, Sperrenkürzung, Wiedererteilung.
 - **Versicherung:** Kostenerstattung, Leistungserschwerden, Schadenfreiheitsrabatt.
- **Sofort-Maßnahmen:**
 - Unfallregulierung: Schadenanzeige, SV-Gutachten beauftragen (eigener SV bei klarer Haftung), Werkstatt einleiten.
 - OWi: Akteneinsicht § 49 OWiG; Schweigerecht § 55 OWiG.
 - Strafrecht: Verteidigerbestellung § 137 StPO; Schweigerecht § 136 StPO; bei vorläufiger Entziehung Fuehrerschein § 111a StPO Beschwerde.
 - FeV: Anhörungstermin wahrnehmen; ggf. Stellungnahme einreichen.
- **Frist-Re-Check:** § 195 BGB / § 199 BGB Schaden; § 67 OWiG 2 Wochen; § 410 StPO 2 Wochen; § 314 StPO 1 Woche; § 30 VVG unverzueglich; § 25 IIa StVG 4-Monatsfrist Fahrverbot.
- **Rechtsschutzversicherungs-Deckungsanfrage** sofort (RS-Versicherer informieren; Wartezeit prüfen).
- **Mandatsmatrix erstellen:** mit Mandantenfreigabe schriftlich für alle weiteren Schritte (Strategie, Vergleich, Klage, Einspruch, Verzicht).

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 67 OWiG
- § 69a StGB
- § 7 StVG
- § 18 StVG
- § 115 VVG
- § 69 StGB
- § 4 StVG
- § 33 OWiG
- § 24a StVG
- § 17 StVG
- § 55 OWiG
- § 26 StVG

### Leitentscheidungen

- BGH VI ZR 12/24
- BGH VI ZR 280/22
- BGH VI ZR 253/22
- BGH VI ZR 239/22
- BGH VI ZR 24/25

---

## Skill: `fachanwalt-verkehrsrecht-regulierungsanforderung`

_Wenn es um Regulierungsanforderung in Fachanwalt Verkehrsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Fachanwalt Verkehrsrecht Regulierungsanforderung; Arbeitsfeld: Fachanwalt Verkehrsrecht._

# Regulierungsanforderung

## Kaltstart-Rückfragen

1. Wann, wo und wie geschah der Unfall — Schilderung beider Beteiligter, Polizeibericht, Zeugen?
2. Welches Fahrzeug, Erstzulassung, Laufleistung, Schadenshöhe gemäß Sachverständigengutachten oder Werkstattrechnung?
3. Soll fiktiv (Sachverständigengutachten ohne Reparatur) oder konkret (mit Reparaturrechnung) abgerechnet werden? Liegt Totalschaden vor (Reparaturkosten > 130 % Wiederbeschaffungswert)?
4. Wer ist die gegnerische Haftpflichtversicherung und ist bereits eine Schadensnummer vergeben? Erfolgte erste Regulierung oder Ablehnung?
5. Bestehen weitere Schadensposten — Mietwagen, Nutzungsausfall, Wertminderung, Schmerzensgeld, Heilbehandlungskosten, Verdienstausfall?
6. Hat der Mandant eigene Mithaftung — Tempoverstoß, Sicherheitsabstand, Anschnallpflicht?
7. Liegt SGB X-Regressi durch Kranken- oder Rentenversicherung, Berufsgenossenschaft vor?
8. Droht Verjährung (3 Jahre ab Schluss des Jahres der Kenntnis, §§ 195, 199 BGB)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

### Normtexte (Kernauszug)

- **§ 7 Abs. 1 StVG** — Gefährdungshaftung Halter; beim Betrieb eines Kraftfahrzeugs entstehende Schäden ohne Verschulden ersatzpflichtig.
- **§ 17 Abs. 1 StVG** — Ausgleich bei mehreren Beteiligten; Quotelung nach Verursachungsbeiträgen.
- **§ 18 StVG** — Fahrerhaftung; Verschuldensvermutung; Entlastungsbeweis möglich.
- **§ 115 Abs. 1 Nr. 1 VVG** — Direktanspruch des Geschädigten gegen Haftpflichtversicherer; eigene Pflicht des Versicherers, den Schaden zu regulieren.
- **§ 249 Abs. 2 Satz 1 BGB** — Schadensersatz in Geld; Herstellungskosten oder Wiederbeschaffungswert.
- **§ 249 Abs. 2 Satz 2 BGB** — Umsatzsteuer nur bei tatsächlicher Zahlung.
- **§ 251 BGB** — Wertausgleich (Nutzungsausfall, merkantiler Minderwert).
- **§ 252 BGB** — Entgangener Gewinn (Verdienstausfall).
- **§ 253 Abs. 2 BGB** — Schmerzensgeld.
- **§ 254 BGB** — Mitverschulden; Schadensminderungspflicht.
- **§ 116 SGB X** — Legalzession auf Sozialversicherungsträger; sachliche und zeitliche Kongruenz; Quotenvorrecht Geschädigter § 116 Abs. 3 SGB X.

### Leitentscheidungen (Stand Mai 2026; jeweils Volltext in offener Quelle vor Verwendung prüfen)

| Gericht | Aktenzeichen | Datum | Kernaussage | Offene Quelle |
|---|---|---|---|---|
| BGH VI. ZS | VI ZR 253/22 | 16.1.2024 | Werkstattrisiko: Geschädigter trägt im Regelfall nicht das Risiko überhöhter Reparaturkosten der Werkstatt | juris.bundesgerichtshof.de |
| BGH VI. ZS | VI ZR 239/22 | 16.1.2024 | Werkstattrisiko parallel (fiktive Abrechnung) | juris.bundesgerichtshof.de |
| BGH VI. ZS | VI ZR 280/22 | 12.3.2024 | Werkstattrisiko-Grundsätze gelten auch für überhöhte Sachverstaendigenkosten | juris.bundesgerichtshof.de |
| BGH VI. ZS | VI ZR 12/24 | 5.11.2024 | Fiktiver Haushaltsfuehrungsschaden: Mindestlohn ist Untergrenze, jedoch nachvollziehbare Begründung des Stundensatzes erforderlich (§ 287 ZPO) | juris.bundesgerichtshof.de |
| BGH VI. ZS | VI ZR 24/25 | 14.10.2025 | Überspannte Substantiierungsanforderungen an Geschädigten zu Haushaltsfuehrungs-/Mehrbedarfsschaden verletzen Art. 103 Abs. 1 GG | juris.bundesgerichtshof.de |

Hinweis: Reihenfolge Rspr. vor Lit.; neueste zuerst. Keine Aufsatz- oder Kommentar-Fundstellen aus Modellwissen. Verifikation in der BGH-eigenen Datenbank, dejure.org oder openjur.de Pflicht.

## Prüfschema in Tabellenform


**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.

| Nr. | Prüfschritt | Norm | Ergebnis |
|---|---|---|---|
| 1 | Haftungsgrundlage (Gefährdung § 7 oder Verschulden § 18/§ 823)? | §§ 7, 18 StVG; § 823 BGB | Gefährdungshaftung kein Verschuldensnachweis nötig |
| 2 | Direktanspruch § 115 VVG — Versicherungsschutz bestehend? | § 115 VVG | Versicherungsschein / Deckungszusage beschaffen |
| 3 | Haftungsquote bestimmt? | § 17 StVG; § 254 BGB | Anscheinsbeweis bei Auffahrunfall etc. |
| 4 | Werkstattrisiko / Sachverstaendigenrisiko bei Kostenkürzung? | § 249 BGB i.V.m. BGH VI ZR 253/22, VI ZR 239/22, VI ZR 280/22 | Geschädigter trägt im Regelfall nicht das Risiko überhöhter Werkstatt-/Gutachterkosten; Kürzung des Versicherers regelmäßig unbegründet |
| 5 | Schadensaufstellung vollständig (Reparatur netto / WBW abzüglich Restwert)? | § 249 BGB | Bei fiktiver Abrechnung Umsatzsteuer nur bei tatsächlicher Zahlung (§ 249 Abs. 2 S. 2 BGB) |
| 6 | Wertminderung beziffert (SV-Gutachten)? | § 251 BGB | Eigenständige Position neben Reparaturkosten |
| 7 | Schmerzensgeld nach § 253 Abs. 2 BGB? | § 253 BGB | Bei Personenschaden; Genugtuung als Bemessungsgesichtspunkt (st. Rspr. BGH VI. ZS) |
| 8 | Mietwagenkosten oder Nutzungsausfall? | §§ 249, 251 BGB | Wahlrecht; Schadensminderungspflicht; Schätzgrundlage Schwacke und/oder Fraunhofer (§ 287 ZPO) |
| 9 | Haushaltsfuehrungsschaden nachvollziehbar begründet? | § 251 BGB i.V.m. BGH VI ZR 12/24 | Mindestlohn ist Untergrenze, aber konkrete Begründung des Stundensatzes erforderlich |
| 10 | Verdienstausfall beziffert? | § 252 BGB | Bruttolohn minus erhaltenes Krankengeld |
| 11 | SGB X-Übergang berücksichtigt? | § 116 SGB X | Quotenvorrecht sichern; SV-Träger informieren |
| 12 | Anwaltskosten angesetzt? | § 249 BGB | Außergerichtlich 1.3 Geschäftsgebühr Nr. 2300 VV RVG |
| 13 | Verjährung geprüft? | §§ 195, 199 BGB | 3 Jahre ab Jahresende der Kenntnis |
| 14 | Fristsetzung an Versicherer mit Verzugsankündigung? | §§ 280, 286, 288 BGB | 4-Wochen-Frist üblich |
| 15 | Klageroute bei Ablehnung vorbereitet? | §§ 23, 71 GVG | AG bis EUR 10000; LG ab EUR 10000 |

Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen. Rspr.-Angaben in der BGH-eigenen Datenbank, auf dejure.org oder openjur.de verifizieren.

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Regulierungsanforderung nach Unfall stellen | Regulierungsschreiben an Versicherer nach Checkliste; Template unten |
| Variante A — Haftungsquote streitig Gegner bestreitet | Haftungsquote-Pruefung zuerst; Schriftsatz erst nach Quotenfixierung |
| Variante B — Totalschaden Restwert streitig | Gutachten abwarten; Regulierung auf Basis Sachverstaendiger |
| Variante C — Personenschaden Schmerzensgeld ungeklaert | Erst Heilbehandlung abschliessen dann Schmerzensgeldanspruch beziffern |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Schriftsatzbausteine

### Baustein 1 — Regulierungsanforderung an Haftpflichtversicherer

```
[Kanzlei]
[Adresse]
[Datum]

[Name Haftpflichtversicherung]
[Adresse]
Schadensnummer: [falls bekannt]

Betreff: Verkehrsunfall vom [Datum], [Uhrzeit], [Unfallort]
         Ihr Versicherungsnehmer: [Name], Kfz-Kennzeichen: [Kz]

Sehr geehrte Damen und Herren,

wir vertreten die rechtlichen Interessen von [Name des Mandanten],
[Anschrift], und zeigen unsere Bevollmächtigung an.

I. Sachverhalt

Am [Datum] gegen [Uhrzeit] ereignete sich auf der [Straße/Kreuzung]
in [Ort] ein Verkehrsunfall. Ihr Versicherungsnehmer [Name] befuhr
mit dem Kfz, Kennzeichen [Kz], [Fahrtrichtung]. Unser Mandant
befuhr mit dem Kfz [Kennzeichen] ebenfalls die [Straße/Kreuzung] in
[Fahrtrichtung].

Ihr Versicherungsnehmer [Unfallhergang konkret, z.B.: fuhr auf das
ordnungsgemäß haltende / fahrende / abbiegende Fahrzeug unseres
Mandanten auf, ohne den nach § 4 Abs. 1 StVO erforderlichen
Sicherheitsabstand einzuhalten].

II. Haftung

Die Haftung trifft allein Ihren Versicherungsnehmer aus §§ 7, 17,
18 StVG i.V.m. § 115 VVG. [Bei Anscheinsbeweis ergänzen: Für den
vorliegenden Auffahrunfall spricht der Anscheinsbeweis des
Auffahrenden gemäß § 4 Abs. 1 StVO; ein atypischer Geschehensverlauf
ist nicht dargetan.]

[Verifikationspflicht vor Versand: konkrete Leitentscheidung zum
Anscheinsbeweis (BGH-Datenbank / dejure.org / openjur.de) mit
Aktenzeichen und Randnummer einsetzen; nicht aus Modellwissen zitieren.]

Ein Mitverschulden unseres Mandanten nach § 254 BGB ist nicht
gegeben, da [Begründung].

III. Schadensaufstellung

Position                                            EUR
-------------------------------------------------  --------
1. Reparaturkosten netto lt. SV-Gutachten          ______
   (oder: WBW EUR ___ - Restwert EUR ___ = _____)
2. Merkantile Wertminderung lt. SV-Gutachten       ______
3. Sachverständigenkosten lt. Rechnung             ______
4. Abschleppkosten lt. Rechnung                    ______
5. Mietwagenkosten lt. Rechnung / Nutzungsausfall
   [X] Tage × EUR [Y] (Sanden/Danner/Klass)       ______
6. Schmerzensgeld § 253 Abs. 2 BGB                 ______
   [Verletzungen benennen; Arztatteste beigefügt]
7. Unkostenpauschale                                  30,00
-------------------------------------------------  --------
Gesamt                                             ______

Anwaltskosten: 1,3 Geschäftsgebühr Nr. 2300 VV RVG
aus EUR [Gesamtschaden] = EUR [Berechnung]
+ Auslagenpauschale Nr. 7002 VV EUR 20,00
+ USt 19 % = EUR [Betrag]                           ______
-------------------------------------------------  --------
Gesamtforderung                                    ______

IV. Frist

Wir fordern Sie auf, den vorstehenden Betrag bis zum [Datum + 4
Wochen] auf das Konto unseres Mandanten IBAN [xxx] zu überweisen.

Nach fruchtlosem Ablauf der Frist tritt Verzug gemäß § 286 BGB ein
und es werden Verzugszinsen in Höhe von 5 Prozentpunkten über dem
Basiszinssatz (§ 288 Abs. 1 BGB) sowie die durch etwaige
Rechtsverfolgungskosten entstehenden Schäden geltend gemacht.

Anlagen
- Polizeibericht / Unfallaufnahme vom [Datum]
- Sachverständigengutachten vom [Datum]
- Lichtbilder Unfallort und Fahrzeugschaden
- Werkstattrechnung / Mietwagenrechnung
- Ärztliche Atteste (bei Personenschaden)
- Vollmacht

Mit freundlichen Grüßen
[Rechtsanwälte]
```

### Baustein 2 — Reaktion auf Teilregulierung / Ablehnung

```
[Kanzlei]
[Datum]

An [Versicherung]
Schadensnummer: [...]

Betreff: Ihre Teilregulierung vom [Datum] — nicht ausreichend

Sehr geehrte Damen und Herren,

Ihre Zahlung vom [Datum] in Höhe von EUR [X] nehmen wir zur Kenntnis.
Die Regulierung ist aus folgenden Gründen unvollständig:

1. Reparaturkosten: Sie haben EUR [X] gekürzt mit der Begründung
   [Begründung Versicherer]. Diese Kürzung ist nicht berechtigt, weil
   das Werkstattrisiko grundsätzlich beim Schädiger liegt
   (BGH, Urt. v. 16.1.2024, VI ZR 253/22; BGH, Urt. v. 16.1.2024,
   VI ZR 239/22 — Quelle vor Versand in juris.bundesgerichtshof.de
   bzw. dejure.org verifizieren und Randnummer einfügen).

2. Nutzungsausfall: Sie haben [X] Tage anerkannt; tatsächlich waren
   [Y] Tage Ausfallzeit erforderlich (SV-Gutachten, Seite [X]).
   Schätzgrundlage Schwacke- und/oder Fraunhofer-Tabelle in
   tatrichterlicher Würdigung (§ 287 ZPO).

3. Sachverständigenkosten: Sie haben EUR [X] gekürzt. Der
   Sachverständige [Name] hat marktübliche Sätze berechnet. Auch
   überhöhte Sachverstaendigenkosten sind dem Geschädigten zu
   ersetzen; das Sachverstaendigenrisiko liegt im Regelfall beim
   Schädiger (BGH, Urt. v. 12.3.2024, VI ZR 280/22 — vor Versand
   Volltext in juris.bundesgerichtshof.de aufrufen und Randnummer
   einsetzen).

Wir halten unsere Restforderung in Höhe von EUR [Differenz] aufrecht
und setzen Ihnen letzte Frist bis [Datum]. Danach erheben wir Klage.

[Rechtsanwälte]
```

### Baustein 3 — Argumentation Merkantile Wertminderung

```
Merkantiler Minderwert (§ 251 BGB)

Das Fahrzeug unseres Mandanten war zum Unfallzeitpunkt
[X Monate] alt und hatte [Y] km gelaufen. Es handelt sich
um ein hochwertiges Fahrzeug der Klasse [Z]. Ein
unfallbedingter Wertverlust am Markt ist unweigerlich
eingetreten — potenzielle Käufer zahlen für Unfallfahrzeuge
weniger als für unvergleichbare schadensfreie Fahrzeuge.

Die Höhe des merkantilen Minderwerts beträgt laut
Sachverständigengutachten EUR [X]. Dieser Betrag ist als
eigenständige Position neben den Reparaturkosten zu ersetzen
(st. Rspr. des BGH zum merkantilen Minderwert nach § 251 BGB —
konkrete Entscheidung vor Versand in juris.bundesgerichtshof.de
oder dejure.org verifizieren und mit Aktenzeichen sowie Randnummer
einsetzen).
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
| Unfallereignis, Kausalität | Mandant |
| Haftungsquote (Anscheinsbeweis widerlegen) | Schädiger / Versicherer |
| Schadenshöhe (Reparatur, WBW) | Mandant (SV-Gutachten) |
| Schadensminderungspflichtverletzung | Versicherer |
| Mitverschulden des Mandanten | Versicherer |
| Tatsächlich gelebte Nutzung (Nutzungsausfall) | Mandant |
| SGB X-Übergang (Kongruenz) | Sozialversicherungsträger |

## Fristen und Verjährung

| Frist | Dauer | Anker | Norm |
|---|---|---|---|
| Verjährung Sachschadenersatz | 3 Jahre | 31.12. des Kenntnisjahres | §§ 195, 199 BGB |
| Verjährung bei Tötung / Körperverletzung | 30 Jahre | Begehungsdatum | § 199 Abs. 2 BGB |
| Hemmung durch außergerichtliche Verhandlungen | Dauer der Verhandlungen | Beginn Verhandlungen | § 203 BGB |
| Regulierungsfrist Versicherer | 4 Wochen (Praxis) | Eingang vollständiger Unterlagen | kein Gesetzsanspruch |
| Verzugszinsen | ab Verzugseintritt | Fristablauf / Mahnung | § 288 Abs. 1 BGB |

## Typische Gegenargumente und Reaktion

| Einwand Versicherer | Reaktion |
|---|---|
| Werkstattkosten überhöht (Stundensaetze, UPE-Zuschläge) | Werkstattrisiko liegt beim Schädiger; BGH VI ZR 253/22, VI ZR 239/22 (16.1.2024) — Volltext und Randnummer vor Versand verifizieren |
| Verbringungskosten abgelehnt | Regionale Werkstattpraxis belegen; bei tatsächlich angefallenen Kosten keine Diskussion |
| Sachverstaendigenkosten ueberhoeht | Sachverstaendigenrisiko liegt beim Schädiger; BGH VI ZR 280/22 (12.3.2024) — Quelle in juris.bundesgerichtshof.de prüfen |
| Mietwagen-Tagessatz überhöht | Schätzgrundlage Schwacke und/oder Fraunhofer in tatrichterlicher Würdigung (§ 287 ZPO); BGH-Linie offen für beide Modelle |
| Haushaltsfuehrungsschaden zu niedrig angesetzt | Mindestlohn ist Untergrenze, aber konkrete Begründung des Stundensatzes erforderlich; BGH VI ZR 12/24 (5.11.2024) |

## Streitwert und Kosten

- Gegenstandswert = Gesamtschadensbetrag; außergerichtliche RA-Gebühren nach RVG 1,3 (Nr. 2300 VV) erstattungsfähig.
- Gericht: AG bis EUR 10000 (§ 23 GVG); LG ab EUR 10000 (§ 71 GVG); bei Personenschaden oft LG-zuständig.
- Bei streitigem Sachverständigengutachten: Kosten trägt unterlegene Partei § 91 ZPO.
- SGB X-Regress: kein eigener Klageanteil, aber Koordination mit SV-Träger schützt Quotenvorrecht § 116 Abs. 3 SGB X.

## Strategische Empfehlung

- Bei eindeutigem Anscheinsbeweis: Fristsetzung 4 Wochen, danach Klage ohne weiteres Zögern.
- Bei streitiger Quote (50:50 möglich): Vergleich mit 75:25 anstreben, wenn Sachverständigenbeweis teuer wäre.
- Bei Personenschäden: klinische Stabilisierung abwarten, keine vorschnelle Einigung — Folgeschäden absichern durch Feststellungsklage zusätzlich zur Leistungsklage.
- Immer SGB X-Koordination: Krankenkasse frühzeitig informieren; Quotenvorrecht § 116 Abs. 3 SGB X dem Versicherer gegenüber benennen.

## Anschluss-Skills

- `unfall-haftungsquote-berechnen` — detaillierte Quotelung
- `fachanwalt-versicherungsrecht-regress-abwehr` — SGB X-Abwehr
- `fachanwalt-versicherungsrecht-deckungsanfrage-pruefen` — eigene Kaskoversicherung

## Quellen

Verbindlich `references/zitierweise.md`. Erlaubte offene Quellen für Verifikation: dejure.org, openjur.de, BGH-eigene Datenbank (juris.bundesgerichtshof.de), BGBl., BVerfG. Beck-RS und juris-Fundstellen ohne offene Quelle sind nicht zu zitieren. Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; literarische Quellen nur bei Nutzervorlage oder lizenziertem Live-Zugriff.

Aktueller Stand Mai 2026 (verifizierte Aktenzeichen mit offener Quelle):
- BGH VI ZR 253/22 v. 16.1.2024 (Werkstattrisiko)
- BGH VI ZR 239/22 v. 16.1.2024 (Werkstattrisiko fiktive Abrechnung)
- BGH VI ZR 280/22 v. 12.3.2024 (Sachverstaendigenrisiko)
- BGH VI ZR 12/24 v. 5.11.2024 (Haushaltsfuehrungsschaden, Mindestlohn als Untergrenze)
- BGH VI ZR 24/25 v. 14.10.2025 (Art. 103 Abs. 1 GG — Substantiierungsanforderungen Schaden)

---

## Skill: `regulierungsanforderung`

_Wenn es um Regulierungsanforderung in Fachanwalt Verkehrsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Regulierungsanforderung; Arbeitsfeld: Fachanwalt Verkehrsrecht._

# Mandant hat Verkehrsunfall und fordert Schadensersatz vom Haftpflichtversicherer des Unfallverursachers


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StVG; PflVG; §§ 315c 316 StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Mandant hat Verkehrsunfall und fordert Schadensersatz vom Haftpflichtversicherer des Unfallverursachers. § 115 VVG Direktanspruch §§ 7 17 StVG § 823 BGB. Prüfraster: Direktanspruch Reparatur vs. fiktive Abrechnung Wiederbeschaffungswert Mitverschulden § 17 StVG Anscheinsbeweis § 4 StVO. Mietwagen Nutzungsausfall Wertminderung Sachverständigenkosten. Output: Regulierungsanforderung an Versicherer fertig. Abgrenzung zu fachanwalt-verkehrsrecht-versicherer-quotenverhandlung-vergleich (Verhandlung) und unfall-haftungsquote-berechnen.

### Regulierungsanforderung

## Kaltstart-Rückfragen

1. Wann, wo und wie geschah der Unfall — Schilderung beider Beteiligter, Polizeibericht, Zeugen?
2. Welches Fahrzeug, Erstzulassung, Laufleistung, Schadenshöhe gemäß Sachverständigengutachten oder Werkstattrechnung?
3. Soll fiktiv (Sachverständigengutachten ohne Reparatur) oder konkret (mit Reparaturrechnung) abgerechnet werden? Liegt Totalschaden vor (Reparaturkosten > 130 % Wiederbeschaffungswert)?
4. Wer ist die gegnerische Haftpflichtversicherung und ist bereits eine Schadensnummer vergeben? Erfolgte erste Regulierung oder Ablehnung?
5. Bestehen weitere Schadensposten — Mietwagen, Nutzungsausfall, Wertminderung, Schmerzensgeld, Heilbehandlungskosten, Verdienstausfall?
6. Hat der Mandant eigene Mithaftung — Tempoverstoß, Sicherheitsabstand, Anschnallpflicht?
7. Liegt SGB X-Regressi durch Kranken- oder Rentenversicherung, Berufsgenossenschaft vor?
8. Droht Verjährung (3 Jahre ab Schluss des Jahres der Kenntnis, §§ 195, 199 BGB)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

### Normtexte (Kernauszug)

- **§ 7 Abs. 1 StVG** — Gefährdungshaftung Halter; beim Betrieb eines Kraftfahrzeugs entstehende Schäden ohne Verschulden ersatzpflichtig.
- **§ 17 Abs. 1 StVG** — Ausgleich bei mehreren Beteiligten; Quotelung nach Verursachungsbeiträgen.
- **§ 18 StVG** — Fahrerhaftung; Verschuldensvermutung; Entlastungsbeweis möglich.
- **§ 115 Abs. 1 Nr. 1 VVG** — Direktanspruch des Geschädigten gegen Haftpflichtversicherer; eigene Pflicht des Versicherers, den Schaden zu regulieren.
- **§ 249 Abs. 2 Satz 1 BGB** — Schadensersatz in Geld; Herstellungskosten oder Wiederbeschaffungswert.
- **§ 249 Abs. 2 Satz 2 BGB** — Umsatzsteuer nur bei tatsächlicher Zahlung.
- **§ 251 BGB** — Wertausgleich (Nutzungsausfall, merkantiler Minderwert).
- **§ 252 BGB** — Entgangener Gewinn (Verdienstausfall).
- **§ 253 Abs. 2 BGB** — Schmerzensgeld.
- **§ 254 BGB** — Mitverschulden; Schadensminderungspflicht.
- **§ 116 SGB X** — Legalzession auf Sozialversicherungsträger; sachliche und zeitliche Kongruenz; Quotenvorrecht Geschädigter § 116 Abs. 3 SGB X.

### Leitentscheidungen (Stand Mai 2026; jeweils Volltext in offener Quelle vor Verwendung prüfen)

| Gericht | Aktenzeichen | Datum | Kernaussage | Offene Quelle |
|---|---|---|---|---|
| BGH VI. ZS | VI ZR 253/22 | 16.1.2024 | Werkstattrisiko: Geschädigter trägt im Regelfall nicht das Risiko überhöhter Reparaturkosten der Werkstatt | juris.bundesgerichtshof.de |
| BGH VI. ZS | VI ZR 239/22 | 16.1.2024 | Werkstattrisiko parallel (fiktive Abrechnung) | juris.bundesgerichtshof.de |
| BGH VI. ZS | VI ZR 280/22 | 12.3.2024 | Werkstattrisiko-Grundsätze gelten auch für überhöhte Sachverstaendigenkosten | juris.bundesgerichtshof.de |
| BGH VI. ZS | VI ZR 12/24 | 5.11.2024 | Fiktiver Haushaltsfuehrungsschaden: Mindestlohn ist Untergrenze, jedoch nachvollziehbare Begründung des Stundensatzes erforderlich (§ 287 ZPO) | juris.bundesgerichtshof.de |
| BGH VI. ZS | VI ZR 24/25 | 14.10.2025 | Überspannte Substantiierungsanforderungen an Geschädigten zu Haushaltsfuehrungs-/Mehrbedarfsschaden verletzen Art. 103 Abs. 1 GG | juris.bundesgerichtshof.de |

Hinweis: Reihenfolge Rspr. vor Lit.; neueste zuerst. Keine Aufsatz- oder Kommentar-Fundstellen aus Modellwissen. Verifikation in der BGH-eigenen Datenbank, dejure.org oder openjur.de Pflicht.

## Prüfschema in Tabellenform

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Nr. | Prüfschritt | Norm | Ergebnis |
|---|---|---|---|
| 1 | Haftungsgrundlage (Gefährdung § 7 oder Verschulden § 18/§ 823)? | §§ 7, 18 StVG; § 823 BGB | Gefährdungshaftung kein Verschuldensnachweis nötig |
| 2 | Direktanspruch § 115 VVG — Versicherungsschutz bestehend? | § 115 VVG | Versicherungsschein / Deckungszusage beschaffen |
| 3 | Haftungsquote bestimmt? | § 17 StVG; § 254 BGB | Anscheinsbeweis bei Auffahrunfall etc. |
| 4 | Werkstattrisiko / Sachverstaendigenrisiko bei Kostenkürzung? | § 249 BGB i.V.m. BGH VI ZR 253/22, VI ZR 239/22, VI ZR 280/22 | Geschädigter trägt im Regelfall nicht das Risiko überhöhter Werkstatt-/Gutachterkosten; Kürzung des Versicherers regelmäßig unbegründet |
| 5 | Schadensaufstellung vollständig (Reparatur netto / WBW abzüglich Restwert)? | § 249 BGB | Bei fiktiver Abrechnung Umsatzsteuer nur bei tatsächlicher Zahlung (§ 249 Abs. 2 S. 2 BGB) |
| 6 | Wertminderung beziffert (SV-Gutachten)? | § 251 BGB | Eigenständige Position neben Reparaturkosten |
| 7 | Schmerzensgeld nach § 253 Abs. 2 BGB? | § 253 BGB | Bei Personenschaden; Genugtuung als Bemessungsgesichtspunkt (st. Rspr. BGH VI. ZS) |
| 8 | Mietwagenkosten oder Nutzungsausfall? | §§ 249, 251 BGB | Wahlrecht; Schadensminderungspflicht; Schätzgrundlage Schwacke und/oder Fraunhofer (§ 287 ZPO) |
| 9 | Haushaltsfuehrungsschaden nachvollziehbar begründet? | § 251 BGB i.V.m. BGH VI ZR 12/24 | Mindestlohn ist Untergrenze, aber konkrete Begründung des Stundensatzes erforderlich |
| 10 | Verdienstausfall beziffert? | § 252 BGB | Bruttolohn minus erhaltenes Krankengeld |
| 11 | SGB X-Übergang berücksichtigt? | § 116 SGB X | Quotenvorrecht sichern; SV-Träger informieren |
| 12 | Anwaltskosten angesetzt? | § 249 BGB | Außergerichtlich 1.3 Geschäftsgebühr Nr. 2300 VV RVG |
| 13 | Verjährung geprüft? | §§ 195, 199 BGB | 3 Jahre ab Jahresende der Kenntnis |
| 14 | Fristsetzung an Versicherer mit Verzugsankündigung? | §§ 280, 286, 288 BGB | 4-Wochen-Frist üblich |
| 15 | Klageroute bei Ablehnung vorbereitet? | §§ 23, 71 GVG | AG bis EUR 10000; LG ab EUR 10000 |

Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen. Rspr.-Angaben in der BGH-eigenen Datenbank, auf dejure.org oder openjur.de verifizieren.

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu prüfen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Regulierungsanforderung nach Unfall stellen | Regulierungsschreiben an Versicherer nach Checkliste; Template unten |
| Variante A — Haftungsquote streitig Gegner bestreitet | Haftungsquote-Prüfung zuerst; Schriftsatz erst nach Quotenfixierung |
| Variante B — Totalschaden Restwert streitig | Gutachten abwarten; Regulierung auf Basis Sachverstaendiger |
| Variante C — Personenschaden Schmerzensgeld ungeklaert | Erst Heilbehandlung abschliessen dann Schmerzensgeldanspruch beziffern |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Baustein 1 — Regulierungsanforderung an Haftpflichtversicherer

```
[Kanzlei]
[Adresse]
[Datum]

[Name Haftpflichtversicherung]
[Adresse]
Schadensnummer: [falls bekannt]

Betreff: Verkehrsunfall vom [Datum], [Uhrzeit], [Unfallort]
 Ihr Versicherungsnehmer: [Name], Kfz-Kennzeichen: [Kz]

Sehr geehrte Damen und Herren,

wir vertreten die rechtlichen Interessen von [Name des Mandanten],
[Anschrift], und zeigen unsere Bevollmächtigung an.

I. Sachverhalt

Am [Datum] gegen [Uhrzeit] ereignete sich auf der [Straße/Kreuzung]
in [Ort] ein Verkehrsunfall. Ihr Versicherungsnehmer [Name] befuhr
mit dem Kfz, Kennzeichen [Kz], [Fahrtrichtung]. Unser Mandant
befuhr mit dem Kfz [Kennzeichen] ebenfalls die [Straße/Kreuzung] in
[Fahrtrichtung].

Ihr Versicherungsnehmer [Unfallhergang konkret, z.B.: fuhr auf das
ordnungsgemäß haltende / fahrende / abbiegende Fahrzeug unseres
Mandanten auf, ohne den nach § 4 Abs. 1 StVO erforderlichen
Sicherheitsabstand einzuhalten].

II. Haftung

Die Haftung trifft allein Ihren Versicherungsnehmer aus §§ 7, 17,
18 StVG i.V.m. § 115 VVG. [Bei Anscheinsbeweis ergänzen: Für den
vorliegenden Auffahrunfall spricht der Anscheinsbeweis des
Auffahrenden gemäß § 4 Abs. 1 StVO; ein atypischer Geschehensverlauf
ist nicht dargetan.]

[Verifikationspflicht vor Versand: konkrete Leitentscheidung zum
Anscheinsbeweis (BGH-Datenbank / dejure.org / openjur.de) mit
Aktenzeichen und Randnummer einsetzen; nicht aus Modellwissen zitieren.]

Ein Mitverschulden unseres Mandanten nach § 254 BGB ist nicht
gegeben, da [Begründung].

III. Schadensaufstellung

Position EUR
------------------------------------------------- --------
1. Reparaturkosten netto lt. SV-Gutachten ______
 (oder: WBW EUR ___ - Restwert EUR ___ = _____)
2. Merkantile Wertminderung lt. SV-Gutachten ______
3. Sachverständigenkosten lt. Rechnung ______
4. Abschleppkosten lt. Rechnung ______
5. Mietwagenkosten lt. Rechnung / Nutzungsausfall
 [X] Tage × EUR [Y] (Sanden/Danner/Klass) ______
6. Schmerzensgeld § 253 Abs. 2 BGB ______
 [Verletzungen benennen; Arztatteste beigefügt]
7. Unkostenpauschale 30,00
------------------------------------------------- --------
Gesamt ______

Anwaltskosten: 1,3 Geschäftsgebühr Nr. 2300 VV RVG
aus EUR [Gesamtschaden] = EUR [Berechnung]
+ Auslagenpauschale Nr. 7002 VV EUR 20,00
+ USt 19 % = EUR [Betrag] ______
------------------------------------------------- --------
Gesamtforderung ______

IV. Frist

Wir fordern Sie auf, den vorstehenden Betrag bis zum [Datum + 4
Wochen] auf das Konto unseres Mandanten IBAN [xxx] zu überweisen.

Nach fruchtlosem Ablauf der Frist tritt Verzug gemäß § 286 BGB ein
und es werden Verzugszinsen in Höhe von 5 Prozentpunkten über dem
Basiszinssatz (§ 288 Abs. 1 BGB) sowie die durch etwaige
Rechtsverfolgungskosten entstehenden Schäden geltend gemacht.

Anlagen
- Polizeibericht / Unfallaufnahme vom [Datum]
- Sachverständigengutachten vom [Datum]
- Lichtbilder Unfallort und Fahrzeugschaden
- Werkstattrechnung / Mietwagenrechnung
- Ärztliche Atteste (bei Personenschaden)
- Vollmacht

Mit freundlichen Grüßen
[Rechtsanwälte]
```

### Baustein 2 — Reaktion auf Teilregulierung / Ablehnung

```
[Kanzlei]
[Datum]

An [Versicherung]
Schadensnummer: [...]

Betreff: Ihre Teilregulierung vom [Datum] — nicht ausreichend

Sehr geehrte Damen und Herren,

Ihre Zahlung vom [Datum] in Höhe von EUR [X] nehmen wir zur Kenntnis.
Die Regulierung ist aus folgenden Gründen unvollständig:

1. Reparaturkosten: Sie haben EUR [X] gekürzt mit der Begründung
 [Begründung Versicherer]. Diese Kürzung ist nicht berechtigt, weil
 das Werkstattrisiko grundsätzlich beim Schädiger liegt
 (BGH, Urt. v. 16.1.2024, VI ZR 253/22; BGH, Urt. v. 16.1.2024,
 VI ZR 239/22 — Quelle vor Versand in juris.bundesgerichtshof.de
 bzw. dejure.org verifizieren und Randnummer einfügen).

2. Nutzungsausfall: Sie haben [X] Tage anerkannt; tatsächlich waren
 [Y] Tage Ausfallzeit erforderlich (SV-Gutachten, Seite [X]).
 Schätzgrundlage Schwacke- und/oder Fraunhofer-Tabelle in
 tatrichterlicher Würdigung (§ 287 ZPO).

3. Sachverständigenkosten: Sie haben EUR [X] gekürzt. Der
 Sachverständige [Name] hat marktübliche Sätze berechnet. Auch
 überhöhte Sachverstaendigenkosten sind dem Geschädigten zu
 ersetzen; das Sachverstaendigenrisiko liegt im Regelfall beim
 Schädiger (BGH, Urt. v. 12.3.2024, VI ZR 280/22 — vor Versand
 Volltext in juris.bundesgerichtshof.de aufrufen und Randnummer
 einsetzen).

Wir halten unsere Restforderung in Höhe von EUR [Differenz] aufrecht
und setzen Ihnen letzte Frist bis [Datum]. Danach erheben wir Klage.

[Rechtsanwälte]
```

### Baustein 3 — Argumentation Merkantile Wertminderung

```
Merkantiler Minderwert (§ 251 BGB)

Das Fahrzeug unseres Mandanten war zum Unfallzeitpunkt
[X Monate] alt und hatte [Y] km gelaufen. Es handelt sich
um ein hochwertiges Fahrzeug der Klasse [Z]. Ein
unfallbedingter Wertverlust am Markt ist unweigerlich
eingetreten — potenzielle Käufer zahlen für Unfallfahrzeuge
weniger als für unvergleichbare schadensfreie Fahrzeuge.

Die Höhe des merkantilen Minderwerts beträgt laut
Sachverständigengutachten EUR [X]. Dieser Betrag ist als
eigenständige Position neben den Reparaturkosten zu ersetzen
(st. Rspr. des BGH zum merkantilen Minderwert nach § 251 BGB —
konkrete Entscheidung vor Versand in juris.bundesgerichtshof.de
oder dejure.org verifizieren und mit Aktenzeichen sowie Randnummer
einsetzen).
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
| Unfallereignis, Kausalität | Mandant |
| Haftungsquote (Anscheinsbeweis widerlegen) | Schädiger / Versicherer |
| Schadenshöhe (Reparatur, WBW) | Mandant (SV-Gutachten) |
| Schadensminderungspflichtverletzung | Versicherer |
| Mitverschulden des Mandanten | Versicherer |
| Tatsächlich gelebte Nutzung (Nutzungsausfall) | Mandant |
| SGB X-Übergang (Kongruenz) | Sozialversicherungsträger |

## Fristen und Verjährung

| Frist | Dauer | Anker | Norm |
|---|---|---|---|
| Verjährung Sachschadenersatz | 3 Jahre | 31.12. des Kenntnisjahres | §§ 195, 199 BGB |
| Verjährung bei Tötung / Körperverletzung | 30 Jahre | Begehungsdatum | § 199 Abs. 2 BGB |
| Hemmung durch außergerichtliche Verhandlungen | Dauer der Verhandlungen | Beginn Verhandlungen | § 203 BGB |
| Regulierungsfrist Versicherer | 4 Wochen (Praxis) | Eingang vollständiger Unterlagen | kein Gesetzsanspruch |
| Verzugszinsen | ab Verzugseintritt | Fristablauf / Mahnung | § 288 Abs. 1 BGB |

## Typische Gegenargumente und Reaktion

| Einwand Versicherer | Reaktion |
|---|---|
| Werkstattkosten überhöht (Stundensaetze, UPE-Zuschläge) | Werkstattrisiko liegt beim Schädiger; BGH VI ZR 253/22, VI ZR 239/22 (16.1.2024) — Volltext und Randnummer vor Versand verifizieren |
| Verbringungskosten abgelehnt | Regionale Werkstattpraxis belegen; bei tatsächlich angefallenen Kosten keine Diskussion |
| Sachverstaendigenkosten ueberhoeht | Sachverstaendigenrisiko liegt beim Schädiger; BGH VI ZR 280/22 (12.3.2024) — Quelle in juris.bundesgerichtshof.de prüfen |
| Mietwagen-Tagessatz überhöht | Schätzgrundlage Schwacke und/oder Fraunhofer in tatrichterlicher Würdigung (§ 287 ZPO); BGH-Linie offen für beide Modelle |
| Haushaltsfuehrungsschaden zu niedrig angesetzt | Mindestlohn ist Untergrenze, aber konkrete Begründung des Stundensatzes erforderlich; BGH VI ZR 12/24 (5.11.2024) |

## Streitwert und Kosten

- Gegenstandswert = Gesamtschadensbetrag; außergerichtliche RA-Gebühren nach RVG 1,3 (Nr. 2300 VV) erstattungsfähig.
- Gericht: AG bis EUR 10000 (§ 23 GVG); LG ab EUR 10000 (§ 71 GVG); bei Personenschaden oft LG-zuständig.
- Bei streitigem Sachverständigengutachten: Kosten trägt unterlegene Partei § 91 ZPO.
- SGB X-Regress: kein eigener Klageanteil, aber Koordination mit SV-Träger schützt Quotenvorrecht § 116 Abs. 3 SGB X.

## Strategische Empfehlung

- Bei eindeutigem Anscheinsbeweis: Fristsetzung 4 Wochen, danach Klage ohne weiteres Zögern.
- Bei streitiger Quote (50:50 möglich): Vergleich mit 75:25 anstreben, wenn Sachverständigenbeweis teuer wäre.
- Bei Personenschäden: klinische Stabilisierung abwarten, keine vorschnelle Einigung — Folgeschäden absichern durch Feststellungsklage zusätzlich zur Leistungsklage.
- Immer SGB X-Koordination: Krankenkasse frühzeitig informieren; Quotenvorrecht § 116 Abs. 3 SGB X dem Versicherer gegenüber benennen.

## Anschluss-Skills

- `unfall-haftungsquote-berechnen` — detaillierte Quotelung
- `fachanwalt-versicherungsrecht-regress-abwehr` — SGB X-Abwehr
- `fachanwalt-versicherungsrecht-deckungsanfrage-pruefen` — eigene Kaskoversicherung

## Quellen

Verbindlich `references/zitierweise.md`. Erlaubte offene Quellen für Verifikation: dejure.org, openjur.de, BGH-eigene Datenbank (juris.bundesgerichtshof.de), BGBl., BVerfG. Beck-RS und juris-Fundstellen ohne offene Quelle sind nicht zu zitieren. Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; literarische Quellen nur bei Nutzervorlage oder lizenziertem Live-Zugriff.

Aktueller Stand Mai 2026 (verifizierte Aktenzeichen mit offener Quelle):
- BGH VI ZR 253/22 v. 16.1.2024 (Werkstattrisiko)
- BGH VI ZR 239/22 v. 16.1.2024 (Werkstattrisiko fiktive Abrechnung)
- BGH VI ZR 280/22 v. 12.3.2024 (Sachverstaendigenrisiko)
- BGH VI ZR 12/24 v. 5.11.2024 (Haushaltsfuehrungsschaden, Mindestlohn als Untergrenze)
- BGH VI ZR 24/25 v. 14.10.2025 (Art. 103 Abs. 1 GG — Substantiierungsanforderungen Schaden)

---

## Skill: `versicherer-quotenverhandlung-vergleich`

_Wenn es um Versicherer hat Regulierung angeboten und Anwalt verhandelt Quotenerhöhung oder Vergleich in Fachanwalt Verkehrsrecht geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen._

# Versicherer hat Regulierung angeboten und Anwalt verhandelt Quotenerhöhung oder Vergleich


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StVG; PflVG; §§ 315c 316 StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Versicherer hat Regulierung angeboten und Anwalt verhandelt Quotenerhöhung oder Vergleich. Versicherer-Verhandlung Unfallregulierung. Prüfraster: Mitverschuldensquote § 254 BGB vorgerichtliche Korrespondenz Schmerzensgeld-Tabellen gerichtlicher Vergleich § 278 Abs. 6 ZPO Mediation Personenschaden. Output: Verhandlungspaket und Vergleichsentwurf. Abgrenzung zu fachanwalt-verkehrsrecht-unfallregulierung-quoten (Berechnung) und vergleichsverhandlung-strategie (Strategie).

### Versicherer-Verhandlung / Quotenstreit im Verkehrsrecht

## Eingaben

- Unfallhergang (Polizei, Foto, Zeugen)
- Mandant (geschädigter Insasse / Fahrer / Halter)
- Versicherer-Reaktion (Anerkenntnis %, Ablehnung)
- Schadensart (Sachschaden, Personenschaden, Unterhaltsausfall)
- Streitwert

## Rechtlicher Rahmen

- **§ 7 StVG** — Halter-Gefährdungshaftung
- **§ 18 StVG** — Fahrer-Verschulden
- **§ 254 BGB** — Mitverschulden
- **§ 11 StVG** — Schmerzensgeld
- **§ 843 BGB** — Renten-Ersatz vermehrte Bedürfnisse
- **PflVG** — Pflicht-Versicherung
- **§ 17 StVG** — Quotelung Halter

## ADR-Pfade

### Pfad 1 — Versicherer-Verhandlung

- Schadensanzeige binnen 7 Tagen
- Quotenangebot Versicherer
- Verhandlung mit Sachbearbeiter
- Vergleichs-Quote 70-90 %

### Pfad 2 — Schiedsgutachten Mitverschuldensquote

- Bei unstreitiger Quote-Frage
- Sachverständigen-Gutachten DEKRA / TÜV
- Bindend für Versicherer

### Pfad 3 — Gerichtlicher Vergleich § 278 ZPO

- Güteverhandlung § 278 Abs. 2 ZPO als Pflicht-Termin vor Beweisaufnahme
- Vergleichsabschluss zu Protokoll § 160 Abs. 3 Nr. 1 ZPO oder per Beschluss § 278 Abs. 6 ZPO (schriftlicher Vergleich)
- Vor Amts-/Landgericht; bei mittlerem Streitwert besonders effizient
- Erörterungstermin mit Quotenvorschlag Gericht

### Pfad 4 — Mediation bei Schwerstverletzung

- DGFM-Mediator
- Bei Querschnitt, Hirnschaden, lebenslange Pflege
- Lebenslange Renten-Vereinbarung

### Pfad 5 — Versicherungs-Ombudsmann

- Bei Verbraucher mit Versicherer
- VVR e.V.

## Workflow

### Phase 1 — Unfall-Aufnahme

- Polizei (zwingend bei Personenschaden)
- Foto-/Zeugen-Dokumentation
- Krankenhaus-/Werkstatt-Belege

### Phase 2 — Schadensanzeige Versicherer

- Schriftliche Schadensmeldung
- Schadenshöhe-Beziferung
- Fragenkatalog Versicherer beantworten

### Phase 3 — Verhandlung

- Versicherer-Quotenvorschlag
- Gegenangebot
- Schriftliche Niederlegung

### Phase 4 — Vergleich

- Erledigungs-Klausel
- Abfindungsbetrag
- Bei Personenschaden: Renten-Vereinbarung

### Phase 5 — Bei Scheitern Klage

- AG/LG je Streitwert
- Sachverständigen-Beweis
- Vergleichstermin vor Gericht

## Strategie und Taktik

- **Mitverschuldensquote nie vor Akteneinsicht akzeptieren**
- **Schmerzensgeld-Tabelle Hacks / Beck** als Orientierungsmaßstab
- **130 %-Grenze bei Fahrzeugschaden**: Reparatur kann teurer als Marktwert sein
- **Vermehrte Bedürfnisse** § 843 BGB lebenslang-Rente bei Schwerstverletzung
- **Versicherer-Vergleichsdruck**: Klage-Drohung oft Quotenerhöher

## Quellen und Updates

Stand: 05/2026. StVG, § 254 BGB. BGH-Linie zu Schmerzensgeld stabil.

## Aktuelle Rechtsprechung Quotenverhandlung (Stand Mai 2026)

Verifizierte Aktenzeichen mit offener Quelle (vor Versand jeweils Volltext aufrufen):

- BGH VI ZR 253/22, Urt. v. 16.1.2024 — Werkstattrisiko liegt im Regelfall beim Schädiger. Quelle: juris.bundesgerichtshof.de
- BGH VI ZR 239/22, Urt. v. 16.1.2024 — Werkstattrisiko bei fiktiver Abrechnung. Quelle: juris.bundesgerichtshof.de
- BGH VI ZR 280/22, Urt. v. 12.3.2024 — Sachverstaendigenrisiko (Übertragung Werkstattrisiko auf Gutachterkosten). Quelle: juris.bundesgerichtshof.de
- BGH VI ZR 12/24, Urt. v. 5.11.2024 — Fiktiver Haushaltsfuehrungsschaden; Mindestlohn als Untergrenze, konkrete Stundensatzbegründung erforderlich. Quelle: juris.bundesgerichtshof.de
- BGH VI ZR 24/25, Urt. v. 14.10.2025 — Substantiierungsanforderungen Schaden; Art. 103 Abs. 1 GG. Quelle: juris.bundesgerichtshof.de

Keine Modellwissen-Zitate. Vor Versand offene Quelle prüfen (juris.bundesgerichtshof.de, dejure.org, openjur.de).

<!-- audit: 27.05.2026 — VI ZR 73/22 (NOT_FOUND auf dejure.org) geloescht; VI ZR 233/19 (NOT_FOUND auf dejure.org) geloescht; VI ZR 286/19 WRONG_TOPIC korrigiert: Thema Anhaenger-Gefaehrdungshaftung § 7 StVG, NJW-Zitat 2020 2116 (nicht 1876), Quelle dejure.org/2020,9266. -->

---

## Skill: `verk-fahrerlaubnisrecht-leitfaden`

_Wenn es um Leitfaden Fahrerlaubnisrecht: Entziehung, MPU, Sperrfrist, vorzeitige Wiedererteilung in Fachanwalt Verkehrsrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Leitfaden Fahrerlaubnisrecht: Entziehung, MPU, Sperrfrist, vorzeitige Wiedererteilung


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StVG; PflVG; §§ 315c 316 StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Leitfaden Fahrerlaubnisrecht: Entziehung, MPU, Sperrfrist, vorzeitige Wiedererteilung. Prüfraster FeV-Begutachtung und Klage gegen Fahrerlaubnisbehoerde.

### Verk: Fahrerlaubnisrecht

## Spezialwissen: Verk: Fahrerlaubnisrecht
- **Normen-/Quellenanker:** MPU, FeV, BGH, BVerfG.

## Fallweichen
Frage zu Beginn nur ab, was für den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Verträge, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, für wen, in welcher Tonalitaet?

## Prüfraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Prüfung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Prüfvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei prüfbarem Link.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

---

## Skill: `bussgeldbescheid-pruefen`

_Wenn es um Mandant hat OWi-Bußgeldbescheid erhalten und Anwalt prüft ob Einspruch sinnvoll ist in Fachanwalt Verkehrsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Mandant hat OWi-Bußgeldbescheid erhalten und Anwalt prüft ob Einspruch sinnvoll ist


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StVG; PflVG; §§ 315c 316 StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Mandant hat OWi-Bußgeldbescheid erhalten und Anwalt prüft ob Einspruch sinnvoll ist. OWiG §§ 65 ff. StVG § 26 Abs. 3 Verjährung. Prüfraster: Form- und Verfahrensfehler Verjährung 3 Monate ab Tat unterbrochen § 33 OWiG Messverfahren standardisiert/nicht-standardisiert Toleranzabzug Anhörung § 55 OWiG Akteneinsicht Fahrverbot § 25 StVG Ausnahmen. Output: Bescheid-Prüfprotokoll und Einspruchsempfehlung. Abgrenzung zu bußgeld-einspruch-prüfen (Schnell-Triage) und fachanwalt-verkehrsrecht-fahrerlaubnis-entzug.

### Bußgeldbescheid prüfen

## Kaltstart-Rückfragen

1. Welche Tat liegt zugrunde — Geschwindigkeitsüberschreitung, Rotlichtverstoß, Abstandsverstoß, Handyverstoß, Alkohol § 24a StVG, Drogen?
2. Wann war die Tatzeit und wann wurde der Bußgeldbescheid zugestellt? Einspruchsfrist § 67 Abs. 1 OWiG zwei Wochen; Verjährungsprüfung § 26 Abs. 3 StVG drei Monate ab Tatzeit.
3. Welches Messverfahren wurde eingesetzt — Lasergerät, Radar, ProViDa, Section Control, ESO, PoliScan, TraffiStar? Liegt Eichschein und Schulungsnachweis des Bedieners vor?
4. Wurde der Mandant als Fahrer anhand des Lichtbilds identifiziert oder nur als Halter angeschrieben?
5. Ist ein Fahrverbot festgesetzt und besteht berufliche Härte (Existenzgefährdung)? Gibt es Voreintragungen im FAER?
6. Wurde eine Anhörung gemäß § 55 OWiG vor Bescheiderlass durchgeführt? Anhörungsbogen ausgefüllt?
7. Bestehen formelle Fehler im Bescheid — fehlerhafte Tatzeit, Tatort, Geschwindigkeit, Rechtsbehelfsbelehrung?
8. Liegt die Tat bereits nahe der Verjährungsgrenze (3 Monate Basis + Unterbrechungen nach § 33 OWiG)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

### Normtexte (Kernauszug)

- **§ 26 Abs. 3 StVG** — Verjährungsfrist drei Monate ab Tatzeit bei Ordnungswidrigkeiten im Straßenverkehr; nach Erlass des Bußgeldbescheids verlängerte Frist.
- **§ 33 OWiG** — Unterbrechungsgründe: Bekanntgabe Verfahrenseinleitung an Betroffenen; schriftliche Aufnahme Sachverhalt für Protokoll; Anordnung Auskunft über Betroffenen; Erlass Bußgeldbescheid; Einlegung Einspruch. Nach jeder Unterbrechung beginnt neue volle Frist.
- Volltext-Verifikation: Rspr. zu § 33 OWiG (Unterbrechungswirkung) und zu standardisierten Messverfahren in BGH-eigener Datenbank, dejure.org oder openjur.de aufrufen; nicht aus Modellwissen zitieren.
- **§ 55 OWiG** — Anhörungsrecht Betroffener; Verletzung kann zur Rechtswidrigkeit des Bußgeldbescheids führen; Heilung möglich wenn Betroffener im Einspruchsverfahren gehört wird.
- **§ 65 OWiG** — Bußgeldbescheid; Mindestinhalt: Personalien, Tatbeschreibung, Tatzeit, Tatort, angewandte Vorschriften, Bußgeldhöhe, Fahrverbot.
- **§ 67 Abs. 1 OWiG** — Einspruch innerhalb zwei Wochen nach Bekanntgabe; schriftlich oder zur Niederschrift bei erlassender Behörde.
- **§ 24a StVG** — Alkohol- und Drogenfahrt als OWi; 0,5 bis 1,09 Promille EUR 500, 2 Punkte, 1 Monat Fahrverbot; Drogen-Grenzwert nach Verordnung.
- **§ 25 StVG** — Fahrverbot; Regelfahrverbot nach BKatV; Wegfall bei atypischem Fall und erhöhter Geldbuße.
- **§ 25 Abs. 2a StVG** — Fahrverbotsbeginn frei wählbar bis 4 Monate nach Rechtskraft.
- **§ 4 Abs. 4 BKatV** — Absehen vom Fahrverbot bei Verhängung höherer Geldbuße.

### BGH und BVerfG-Leitentscheidungen (Stand Mai 2026; offene Quellen)

| Gericht | Aktenzeichen | Datum | Kernaussage | Offene Quelle |
|---|---|---|---|---|
| BVerfG | 2 BvR 1167/20 | 20.6.2023 | Standardisierte Geschwindigkeitsmessung; keine Pflicht zur Speicherung von Rohmessdaten; Recht auf erweiterten Informationszugang im Einzelfall | bundesverfassungsgericht.de |
| BVerfG | 2 BvR 1616/18 | 12.11.2020 | Informationszugang OWi-Verfahren; Akteneinsicht in Messunterlagen | bundesverfassungsgericht.de |
| BVerwG | 3 B 2.24 | 8.1.2025 | KCanG ab 1.4.2024: Cannabis ist kein BtM mehr; § 14 FeV neu zu lesen | bverwg.de |

Hinweis: BGH (4. Strafsenat) zu Geschwindigkeitsmessverfahren ist standardisiert anerkannt; konkrete Mess-Fehler im Einzelfall müssen substantiiert vorgetragen werden. Aktenzeichen vor Versand in BGH-eigener Datenbank, dejure.org oder openjur.de verifizieren.

## Prüfschema in Tabellenform

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Nr. | Prüfschritt | Norm | Konsequenz |
|---|---|---|---|
| 1 | Verjährung geprüft? (3 Monate ab Tatzeit) | § 26 Abs. 3 StVG | Abgelaufen und keine Unterbrechung: Einstellung § 46 OWiG |
| 2 | Unterbrechungshandlungen belegt? | § 33 OWiG | Lücke in Unterbrechungskette → Verjährung |
| 3 | Einspruchsfrist gewahrt? (2 Wochen + 4-Tage-Fiktion) | § 67 OWiG; PostModG | Versäumt: Wiedereinsetzung § 52 OWiG prüfen |
| 4 | Anhörung ordnungsgemäß? | § 55 OWiG | Heilung im Einspruchsverfahren möglich |
| 5 | Mindestinhalt Bescheid vollständig § 65 OWiG? | § 65 OWiG | Fehlt wesentlicher Inhalt: Aufhebung rügbar |
| 6 | Fahreridentifizierung belegt? | Darlegungslast Behörde | Zweifelhaftes Lichtbild: Sachverständigen-Beweisangebot |
| 7 | Messverfahren standardisiert? | BGHSt 39, 291 | Nicht standardisiert: volle Beweislast Behörde |
| 8 | Eichschein gültig zur Tatzeit? | § 31 MessEG | Abgelaufen: Verwertungsverbot prüfen |
| 9 | Recht auf Akteneinsicht in Rohmessdaten geltend gemacht? | Art. 103 GG; BVerfG 2 BvR 1616/18 (12.11.2020), BVerfG 2 BvR 1167/20 (20.6.2023) | Antrag schriftlich; keine pauschale Speicherungspflicht, aber Anspruch auf vorhandene Daten |
| 10 | Cannabis-Beteiligung? | § 24a StVG, KCanG (seit 1.4.2024); BVerwG 3 B 2.24 (8.1.2025) | THC-Grenzwert 3.5 ng/ml im Serum (§ 24a Abs. 1a StVG seit 22.8.2024) |
| 11 | Toleranzabzug korrekt vorgenommen? | BGHSt 39, 291; BKatV | Zu gering: Neuberechnung; ggf. anderes Tatbild |
| 12 | Bußgeld korrekt nach BKatV? | BKatV Anlage 1, 2 | Fehler: unmittelbare Rüge |
| 13 | Fahrverbot: Regelfall oder Atypik? | § 25 StVG; § 4 Abs. 4 BKatV | Härtefall: erhöhte Geldbuße statt Fahrverbot |
| 14 | § 25 Abs. 2a StVG-Aufschub genutzt? | § 25 Abs. 2a StVG | Bis 4 Monate nach Rechtskraft; Ferienzeit wählen |
| 15 | FAER-Punkte korrekt? Tilgungsfristen? | § 29 StVG | 2,5 Jahre Tilgung bei 1-2 Punkten |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu prüfen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Mandant will Bussgeldbescheid prüfen lassen | Formelle und materielle Prüfung; Schriftsatz unten |
| Variante A — Bescheid ohne Messfehler Akzeptanz guenstiger | Keine weiteren Maßnahmen; Zahlung empfehlen |
| Variante B — Fahrverbot mit Haertefall Elternzeit Fernpendler | Einspruch nur wegen Fahrverbot; Geldbusse akzeptieren |
| Variante C — Standardisiertes Messverfahren fehlerhafte Geeichung | Einspruch mit technischer Ruege; Akte anfordern |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Baustein 1 — Einspruch mit Akteneinsicht und Rohmessdaten-Antrag

```
An die [Bußgeldstelle]
[Adresse]
Aktenzeichen: [Az]

EINSPRUCH § 67 OWiG

In der Bußgeldsache gegen
[Name, Adresse, geb. Datum]

namens und in Vollmacht des Betroffenen lege ich gegen den
Bußgeldbescheid vom [Datum], zugestellt am [Datum],

 EINSPRUCH

ein. Eine Begründung bleibt nach Akteneinsicht vorbehalten.

ANTRÄGE

1. Akteneinsicht § 49 OWiG

Ich beantrage vollständige Akteneinsicht einschließlich:
a) Sämtlicher Rohmessdaten des Falldatensatzes und der
 Falldatensätze der Messreihe (konkret: alle Einzelmessungen,
 sofern vom Gerät gespeichert; vgl. BVerfG, Beschl. v. 12.11.2020,
 2 BvR 1616/18; BVerfG, Beschl. v. 20.6.2023, 2 BvR 1167/20 — kein
 Anspruch auf nicht gespeicherte Daten, aber Anspruch auf alle
 vorhandenen Daten);
b) Eichschein des Messgeräts mit Gültigkeitsdauer zur Tatzeit;
c) Schulungsnachweis des messenden Beamten (Name, Gerätekurs);
d) Messprotokoll mit Aufstellungsort, -bedingungen und -dauer;
e) Betriebsanleitung des eingesetzten Geräts [Bezeichnung].

2. Aussetzung der Vollziehung des Fahrverbots
 bis zur rechtskräftigen Entscheidung, da berufliche Härte
 droht (Begründung nach Akteneinsicht).

Mit freundlichen Grüßen
[Rechtsanwalt]
```

### Baustein 2 — Begründung nach Akteneinsicht: Verjährung

```
Begründung des Einspruchs

I. Verjährung

Die Ordnungswidrigkeit vom [Tatdatum] ist verjährt.

Gemäß § 26 Abs. 3 StVG beträgt die Verjährungsfrist drei Monate
ab Tatzeit ([Tatdatum]).

Die Akte enthält folgende Unterbrechungshandlungen:
- Anhörungsbogen versandt am [Datum]
- Eingang Anhörungsbogen am [Datum] (Unterschrift des Mandanten)
- Bußgeldbescheid erlassen am [Datum]

Nach der Unterbrechung durch Absendung des Anhörungsbogens am
[Datum] begann die neue 3-Monats-Frist. Diese lief ab am [Datum +
3 Monate]. Der Bußgeldbescheid wurde am [Datum] erlassen, also
NACH Ablauf der Verjährungsfrist.

Die Ordnungswidrigkeit ist verjährt. Der Einspruch ist begründet.
Das Verfahren ist einzustellen.
```

### Baustein 3 — Begründung Messfehler / Rohmessdaten

```
II. Messung nicht verwertbar

Das eingesetzte Messgerät [Bezeichnung, Gerätenummer] misst nach
dem standardisierten Verfahren (BGHSt 39, 291). Allerdings sind
folgende Fehler zu verzeichnen:

1. Eichschein abgelaufen:
 Laut beigebrachtem Eichschein war das Gerät zuletzt am
 [Datum] geeicht. Die Eichgültigkeitsdauer beträgt nach
 § 32 MessEV 12 Monate. Die Tatzeit [Datum] liegt nach
 Ablauf der Eichgültigkeit. Das Messergebnis ist nicht
 verwertbar.

2. Rohmessdaten verweigert:
 Trotz konkretem Antrag vom [Datum] (Anlage K1) wurden die
 Rohmessdaten des Falldatensatzes nicht vorgelegt. Nach der
 Rechtsprechung des BVerfG (Beschl. v. 12.11.2020, 2 BvR 1616/18;
 Beschl. v. 20.6.2023, 2 BvR 1167/20) hat der Betroffene einen
 Anspruch auf Zugang zu den vorhandenen Messdaten und
 Begleitunterlagen; jedenfalls bei konkret dargelegtem
 Aufklärungsbedarf greift ein Verwertungsverbot, wenn die
 Verteidigung nachvollziehbar darlegt, dass sie ohne diese
 Daten die Messung nicht überprüfen kann.
 (Volltext der Beschlüsse vor Versand in
 bundesverfassungsgericht.de aufrufen und Randnummern
 ergänzen.)

3. Sachverständigengutachten wird beantragt:
 Zum Nachweis der Unverwertbarkeit der Messung beantragen
 wir die Einholung eines Sachverständigengutachtens zur
 Frage, ob das eingesetzte Gerät am Tattag zuverlässige
 Messergebnisse liefern konnte.
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
| Tatbestand, Schuld | Bußgeldstelle / Gericht |
| Fahreridentität | Bußgeldstelle; Halterschaft allein genügt nicht |
| Standardisiertes Messverfahren korrekt angewendet | Grundsatzvermutung BGHSt 39, 291; Verteidigung muss konkrete Fehler benennen |
| Verjährungsunterbrechung | Bußgeldstelle (Zugangsnachweise für Anhörung etc.) |
| Härtefall Fahrverbot | Betroffener (konkrete Existenzgefährdung) |
| Ordnungsgemäße Anhörung | Bußgeldstelle |

## Fristen und Verjährung

| Frist | Dauer | Anker | Norm |
|---|---|---|---|
| Verjährung OWi Straßenverkehr | 3 Monate ab Tatzeit | Tatzeit | § 26 Abs. 3 StVG |
| Verlängerte Verjährung nach Bußgeldbescheid | 6 Monate nach Rechtskraft | VerfH § 26 Abs. 3 StVG | |
| Einspruchsfrist | 2 Wochen (+ 4 Tage Zustellungsfiktion) | Zustellung | § 67 OWiG; PostModG |
| Wiedereinsetzung | 2 Wochen | Hindernis entfallen | § 52 OWiG |
| Fahrverbotsbeginn (Wahlrecht) | bis 4 Monate nach Rechtskraft | Rechtskraft | § 25 Abs. 2a StVG |
| Tilgung FAER | 2,5 / 5 / 10 Jahre | Rechtskraft | § 29 StVG |

## Typische Gegenargumente und Reaktion

| Einwand | Reaktion |
|---|---|
| Standardisiertes Verfahren — kein Fehler möglich | Konkrete Benennung: Eichablauf, fehlender Schulungsnachweis, Rohmessdaten-Verweigerung |
| Fahrerbild eindeutig | Sachverständigen-Lichtbildvergleich beantragen; Beweiswürdigung dem Gericht überlassen |
| Verjährung durch Anhörungsversand unterbrochen | Beweislast Bußgeldstelle für Zugangszeitpunkt; Versandtag ist nicht Zugangstag |
| Keine Anhörungspflichtverletzung — heilbar | Im Hauptverfahren Gelegenheit gegeben; aber: formelle Pflicht des Bescheids unberührt |
| Härtefall nicht beweisbar | Arbeitgeberbestätigung + Gehaltsnachweis + Routenplan + Bescheinigung ÖPNV-Unzumutbarkeit |

## Streitwert und Kosten

- Kein Kostenrisiko für Betroffenen bei Einspruch; Kosten bei Verurteilung nach OWiG-Gebührentabelle.
- Anwaltsgebühren: Nr. 5100 ff. VV RVG; Grundgebühr + Verfahrensgebühr + ggf. Terminsgebühr; gesamt ca. EUR 400–1500 nach Bußgeldhöhe.
- Sachverständigengutachten Messung: EUR 800–2500; bei Freispruch: Staatskasse trägt Kosten § 467 StPO i.V.m. § 46 OWiG.

## Strategische Empfehlung

- Bei klarer Messung ohne Fehler: Einspruch nur bezüglich Fahrverbot (§ 4 Abs. 4 BKatV); Geldbuße akzeptieren.
- Bei Identitätszweifel: Vollenspruch; Sachverständigen-Beweisangebot im Einspruch benennen.
- Bei Verjährungs-Verdacht: Fristberechnung exakt; Unterbrechungskette der Bußgeldstelle anfordern.
- Bei Messfehler-Verdacht: BVerfG-Antrag auf Rohmessdaten konkret formulieren; nach Verweigerung sofort Verwertungsverbot geltend machen.
- Bei Fahrverbot + Beruf: Immer § 4 Abs. 4 BKatV Antrag; Arbeitgeberbestätigung sofort einholen; § 25 Abs. 2a StVG-Aufschub erklären.

## Anschluss-Skills

- `bussgeld-einspruch-pruefen` — detailliertes Messverfahrens-Prüfschema
- `fachanwalt-verkehrsrecht-fahrerlaubnis-entzug` — bei Fahrerlaubnisfolgen
- `fachanwalt-strafrecht-hauptverhandlung-vorbereiten` — Vorbereitung AG-Verhandlung

## Quellen

Verbindlich `references/zitierweise.md`. Erlaubte offene Quellen: bundesverfassungsgericht.de, bundesgerichtshof.de (juris.bundesgerichtshof.de), bverwg.de, dejure.org, openjur.de, BGBl. Beck-RS und juris-Fundstellen ohne offene Quelle sind nicht zu zitieren.

Aktueller Stand Mai 2026 (verifizierte Aktenzeichen):
- BVerfG, Beschl. v. 12.11.2020, 2 BvR 1616/18 — Akteneinsicht / Informationszugang OWi
- BVerfG, Beschl. v. 20.6.2023, 2 BvR 1167/20 — Keine Rohmessdaten-Speicherungspflicht; aber Anspruch auf vorhandene Daten
- BVerwG, Beschl. v. 8.1.2025, 3 B 2.24 — Cannabis und KCanG ab 1.4.2024
- KCanG vom 27.3.2024, BGBl. I 2024 Nr. 109; § 24a Abs. 1a StVG i. d. F. vom 21.8.2024, BGBl. I 2024 Nr. 274 (3.5 ng/ml THC-Grenzwert)

---

## Anwendungshinweise

1. Diesen Vollprüfung als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

