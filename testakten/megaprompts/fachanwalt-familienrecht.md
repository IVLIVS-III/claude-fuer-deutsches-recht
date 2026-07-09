# Vollprüfung: fachanwalt-familienrecht

## Zusammensetzung

Dieser Vollprüfung enthaelt top-8 von 157 Skills (gekuerzt fuer Chat-Fenster) des Plugins `fachanwalt-familienrecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Wenn es um Anwalts-Dashboard Fachanwalt Familienrecht in Fachanwalt Familienrecht geht: klärt Rolle, Ziel, Frist, Unterl…
2. **mandat-triage-familienrecht** — Wenn es um Mandat Triage Familienrecht in Fachanwalt Familienrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den pa…
3. **fachanwalt-familienrecht-orientierung** — Wenn es um Fachanwalt für Familienrecht — Orientierung in Fachanwalt Familienrecht geht: prüft Frist, Form, Zuständigkei…
4. **orientierung-fristen-form-und-zustaendigkeit** — Wenn es um Orientierung Fristen Form Und Zuständigkeit in Fachanwalt Familienrecht geht: prüft Frist, Form, Zuständigkei…
5. **orientierung-mandat-fachanwaltschaft** — Wenn es um Orientierung Mandat Fachanwaltschaft in Fachanwalt Familienrecht geht: prüft Frist, Form, Zuständigkeit, Rech…
6. **erstgespraech-mandatsannahme** — Wenn es um Erstgespraech Mandatsannahme in Fachanwalt Familienrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg un…
7. **erstpruefung-und-mandatsziel** — Wenn es um Erstpruefung Und Mandatsziel in Fachanwalt Familienrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den p…
8. **fachanwalt-familienrecht-mediation-156-famfg-cochemer** — Wenn es um Fachanwalt Familienrecht Mediation 156 Famfg Cochemer in Fachanwalt Familienrecht geht: ordnet Sachverhalt, N…

---

## Skill: `einstieg-routing`

_Wenn es um Anwalts-Dashboard Fachanwalt Familienrecht in Fachanwalt Familienrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Anwalts-Dashboard Fachanwalt Familienrecht

> Trennung, Unterhalt, Versorgungsausgleich, Sorge- und Umgangsrecht — meist Verbundverfahren, meist im Hintergrund das Kindeswohl.
>
> Sie sehen unten die Sofort-Triage. Keine Rückfragen, bis die Tabelle steht. Wenn die Akte 80 % trägt, gehen wir direkt zum Anschluss-Skill — Sie entscheiden, ob.

## Sofort-Triage

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
| --- | --- | --- |
| Rolle | Wen vertrete ich? (Mandant · Gegenseite · Mehrere) | Mandantenmail, Vertretungsbestellung |
| Verfahrensstand | Vorprozessual · außergerichtlich · Klage · Rechtsmittel · Vollstreckung | Vorhandene Schriftsätze, Eingangsstempel |
| Eilfrist | Keine 3-Wochen-Frist wie im ArbR, aber: Paragraf 1565 II BGB (Härtefall-Scheidung vor Trennungsjahr), Paragrafen 1666, 1666a BGB i. V. m. Paragraf 49 FamFG (Kindeswohlgefährdung — sofort), Paragraf 36 GewSchG (Gewaltschutz — sofortige Wirksamkeit). | Frist aus Zugangs-/Kenntnisdatum berechnen |
| Hauptanspruch | Scheidung Paragrafen 1564 ff. BGB · Trennungsunterhalt Paragraf 1361 BGB · Nachehelicher Unterhalt Paragrafen 1569 ff. BGB · Kindesunterhalt Paragrafen 1601 ff. BGB · Zugewinn Paragrafen 1372 ff. BGB · Versorgungsausgleich Paragrafen 1, 9 VersAusglG · Sorge Paragrafen 1671, 1684 BGB · Umgang Paragraf 1684 BGB. | Sachverhaltsabgleich mit Tatbestandsmerkmalen |
| Zuständigkeit | Familiengericht (Abt. AG) am Aufenthalt des Kindes oder gemeinsamen Wohnsitzes (Paragrafen 122, 152, 232 FamFG). Anwaltszwang in Ehesachen (Paragraf 114 FamFG). | Gesetz, Vertrag, Gerichtsstandsklausel |

## Risiko-Ampel

- **Frist:** 🔴 Kindeswohlgefährdung: sofort Eilantrag (Paragraf 49 FamFG). 🔴 Häusliche Gewalt: Schutzanordnung Paragraf 1 GewSchG. 🟠 Trennungsjahr: Datum dokumentieren (Beweis!).
- **Beweislage:** 🟠 Trennungszeitpunkt — Indizien (Kontotrennung, Schlafzimmer, schriftliche Erklärung). 🔴 Sorgekonflikt: Beweismittel sorgsam (kein Aufschaukeln, Verfahrensbeistand respektieren).
- **Wirtschaftlich:** 🟠 Hohes Vermögen: Zugewinn parallel zur Scheidung (Verbund). 🔴 Drohende Verschiebung von Vermögen: Paragraf 1379 BGB Auskunft + Paragraf 1390 BGB Anfechtung.

## Anschluss-Skills (Router)

| Wenn der Fall trägt … | dann Skill | Erwartung |
| --- | --- | --- |
| **Trennung — Trennungsjahr / Folgen** | `famr-trennungsjahr-praxis` | Trennungszeitpunkt dokumentieren, Trennungsunterhalt vorbereiten |
| Kindesunterhalt zu prüfen | `kindesunterhalt-mindestsatz-paragraf-1612a-bgb` | Mindestunterhalt, Düsseldorfer Tabelle, Mangelfall-Berechnung |
| Versorgungsausgleich offen | `famr-versorgungsausgleich-spezial` | Auskunftsverfahren VAB-Fragebogen, Halbteilung, Ausschluss |
| Gewaltschutz / Umgang in Konflikt | `gewaltschutz-und-umgang-schnittstelle` | GewSchG-Anordnung, Schnittstelle Umgang Paragraf 1684 BGB |
| Kindeswohlgefährdung — Eilantrag | `famr-kindeswohlgefaehrdung-eilantrag-spezial` | Eilantrag Paragraf 1666 BGB, Verfahrensbeistand, Jugendamt |

## Norm-Radar (live verifizieren)

- **Paragraf 1565 BGB** — Scheidungsvoraussetzung, Trennungsjahr
- **Paragraf 1361 BGB** — Trennungsunterhalt
- **Paragraf 1612a BGB** — Mindestkindesunterhalt
- **Paragraf 1666 BGB** — Maßnahmen bei Kindeswohlgefährdung
- **Paragraf 1684 BGB** — Umgangsrecht / Umgangspflicht
- **Paragraf 1 VersAusglG** — Halbteilungsgrundsatz

## Genau eine Rückfrage (nur wenn nötig)

> Geht es vorrangig um **Trennungs-/Scheidungsfolgen (Unterhalt, Zugewinn, VA)** oder um eine **akute Kindes- bzw. Gewaltschutz-Sache** (dann sofortiger Eilantrag)?

Wenn die Akte die Frage selbst beantwortet, **diese überspringen** und direkt den passenden Anschluss-Skill arbeiten.

## Leitentscheidungs-Anker (Such-Wegweiser, keine fertigen Zitate)

- **Ehevertrag; Kernbereichslehre, Wirksamkeitskontrolle** — BGH XII. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Wechselmodell; Anordnungsfähigkeit durch Familiengericht** — BGH XII. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Kindeswohlgefährdung Paragraf 1666 BGB; Eingriffsschwelle** — BVerfG 1. Senat — *live verifizieren auf* `bundesverfassungsgericht.de`
- **Düsseldorfer Tabelle (Unterhalt; jährliche Aktualisierung)** — OLG Düsseldorf — *live verifizieren auf* `olg-duesseldorf.nrw.de`

> Diese Anker sind Sucheinstieg. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle prüfen und Datum, Aktenzeichen, Randnummer abklären. Kuratierte Anker-Sammlung in `references/leitentscheidungen-anker.md`.

## Hinweis

Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Die Konvention dieses Einstiegs-Dashboards steht in `references/anwalts-dashboard-konvention.md`.

---

## Skill: `mandat-triage-familienrecht`

_Wenn es um Mandat Triage Familienrecht in Fachanwalt Familienrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Eingangs-Triage für familienrechtliche Mandate: Routing zu Scheidung, Sorge, Umgang, Unterhalt, Zugewinn oder Versorgungsausgleich


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: FamFG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Eingangs-Triage für familienrechtliche Mandate: Routing zu Scheidung, Sorge, Umgang, Unterhalt, Zugewinn oder Versorgungsausgleich. Normen: Paragraf 63 FamFG (Beschwerde 1 Monat), Paragraf 1600b BGB (Vaterschaftsanfechtung 2 Jahre), Paragraf 1666 BGB (Kindeswohlgefaehrdung Eilantrag). Prüfraster: Konflikt-Check, Eilbedürftigkeit (Gewaltschutz, Sorge-Eilantrag), Streitwert, Komplexitaet. Output Triage-Protokoll, Fristen-Ampel, Folge-Skill-Empfehlung. Abgrenzung: Detailberechnung siehe Fachmodule; Schriftsatzkern siehe schriftsatzkern-substantiierung.

### Mandat-Triage Familienrecht

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mandat-Triage Familienrecht` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB Paragrafen 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG Paragrafen 49 ff., 76, 86 ff., 112 ff.; VersAusglG Paragrafen 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, Paragraf 51 VersAusglG, Paragraf 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Mandat-Triage Familienrecht
- **Normen-/Quellenanker:** BGB Familienrecht, FamFG, VersAusglG, Unterhaltsrecht, Zugewinn, Gewaltschutz, Kindschaft, internationale Verordnungen und Vollstreckung.
- **Entscheidende Weiche:** Beteiligte, Kind/Unterhalt/Vermögen/Versorgung, Frist, Auskunft, Beleg, Eilbedarf und familiengerichtliche Verfahrensart trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Aktuelle Rechtsprechung (Triage-Orientierung, Stand 05/2026)

Verifizierte Eckpfeiler — Live-Verifikation vor Verwendung in Schriftsätzen zwingend:

- BGH 22.01.2025 - XII ZB 148/24 (Elternunterhalt, Selbstbehalt; Familienselbstbehalt)
- BVerfG 07.10.2025 - 1 BvR 746/23 (Umgangsausschluss: Begründungsanforderungen bei längerer Dauer)
- BVerfG 28.08.2025 - 1 BvR 1473/25 (Sorgerecht im einstweiligen Anordnungsverfahren; PAS-Maßstäbe)
- Düsseldorfer Tabelle 2026 (in Kraft seit 01.01.2026)

Weitere Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe über bundesgerichtshof.de, bundesverfassungsgericht.de, dejure.org oder openjur.de mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ablauf — sieben Fragen in fester Reihenfolge

### Frage 1 — Wer ruft an und für wen?

- Selbst Betroffener
- Eltern eines Kindes
- Anderer Anwalt (Verweisungsmandat)
- Gericht (Verfahrensbeistand)

**Routing:** Bei Verweisungsmandat sofort an aufnehmenden Anwalt. Bei Verfahrensbeistand separater Vermerk.

### Frage 2 — Akute Eilbedürftigkeit?

- Häusliche Gewalt — Schutzanordnung gewünscht
- Kindeswohl unmittelbar gefährdet
- Kind drohend ins Ausland verbracht (HKÜ-Fall)
- Wegweisung dringend
- Sorgerecht-Eilbedürftigkeit

**Eskalation:** Bei JA — Telefon-Sofort an Anwalt; binnen ein Stunde Eilantrag-Vorbereitung. Skill `mandat-triage-familienrecht` wechselt sofort in Eilmodus.

### Frage 3 — Hauptanliegen?

- Scheidung
- Sorgerecht
- Umgangsrecht
- Kindesunterhalt
- Ehegattenunterhalt
- Zugewinnausgleich
- Versorgungsausgleich
- Vaterschaft (Anerkennung Anfechtung)
- Ehevertrag Scheidungsfolgenvereinbarung
- Adoption
- Betreuung Vorsorgevollmacht

### Frage 4 — Stand des Verfahrens?

- Außergerichtlich keine Anzeige
- Schreiben des Gegners liegt vor
- Gerichtliches Verfahren läuft (Aktenzeichen Gericht)
- Erstinstanz abgeschlossen — Beschwerde erwogen

### Frage 5 — Familienstatus?

- Verheiratet
- Getrennt lebend (Datum der Trennung)
- Geschieden
- Lebenspartnerschaft
- Nichtehelich

### Frage 6 — Wirtschaftliche Verhältnisse?

- Nettoeinkommen beide Eheleute geschätzt
- Vermögen geschätzt (Immobilie Sparvermögen Unternehmensbeteiligungen)
- Streitwert-Schätzung

**Routing PKH:** Bei knappem Einkommen Hinweis auf Prozesskostenhilfe-Antrag. Sozialrechtliche Bedürftigkeits- und Leistungsfragen bei Bedarf an `fachanwalt-sozialrecht` routen; PKH-Antrag sonst als eigener Entwurf.

### Frage 7 — Fristen?

- Letztes Anwaltsschreiben oder Beschluss empfangen am ?
- Beschwerdefrist Paragraf 63 FamFG ein Monat
- Vaterschaftsanfechtung Paragraf 1600b BGB zwei Jahre ab Kenntnis

## Routing-Matrix

| Hauptanliegen | Folge-Skill | Frist-Sofort-Check |
|---|---|---|
| Scheidung | (Skill scheidungsverbund-vorbereiten — perspektivisch) | Versorgungsausgleichs-Auskunft anfordern |
| Kindesunterhalt | `unterhalt-duesseldorfer-tabelle` | Verzug Paragraf 1613 BGB durch Auskunftsschreiben |
| Ehegattenunterhalt | `unterhalt-duesseldorfer-tabelle` | Verzug Paragraf 1613 BGB |
| Sorge / Umgang | (Skill kindeswohl-prüfung — perspektivisch) | Eilantrag prüfen |
| Zugewinn | (Skill zugewinnausgleich-berechnen — perspektivisch) | Stichtag Zustellung Scheidungsantrag |
| Versorgungsausgleich | (Skill versorgungsausgleich — perspektivisch) | Auskunft DRV / Versorgungsträger |
| Vaterschaft | (Skill vaterschafts-verfahren — perspektivisch) | Paragraf 1600b BGB Zwei-Jahres-Frist |
| Gewaltschutz | EILMODUS — Antrag GewSchG Skill `mandat-triage-familienrecht` wechselt | sofort |

## Mandatsannahme-Kriterien

- **Konflikt-Check** — keine Beratung des Gegners im selben Sachverhalt (Paragraf 43a Abs. 4 BRAO)
- **Streitwert** über EUR 30000 OLG Familiensenat erste Instanz bei Verbund
- **Komplexität** bei Auslandsbezug Selbstständigen-Einkommen Unternehmens-Beteiligungen Gesellschafter-Streit

## Sofort-Fristen-Check

- Empfangsdatum letzter Beschluss notieren
- Bei Beschluss eingegangen heute: Beschwerdefrist nach FamFG (Paragrafen 63, 64 FamFG i.V.m. ZPO) — Zugang nach Vier-Tages-Fiktion (Paragraf 270 ZPO n.F., seit 1.1.2025 PostModG; bis 31.12.2024 drei Tage), danach Lauf der Beschwerdefrist von einem Monat (Paragraf 63 FamFG)
- Eintrag in `fristenbuch.yaml` (Skill `kanzlei-allgemein`)

## Eskalationspfad

- **Telefon-Sofort** Gewaltschutz Kindeswohlgefährdung HKÜ-Verbringung
- **Binnen einer Stunde** Eilantrag-Sorgerecht Wegweisung
- **Heute** Versorgungsausgleichs-Auskunft Verzug-Schreiben
- **Diese Woche** Schriftsatz-Erstentwurf Verbund-Antrag

## Ausgabe

- `triage-protokoll-familienrecht.md` strukturiert nach den sieben Fragen
- Aktenanlage mit Az-Vorschlag
- Frist-Eintrag im Fristenbuch
- Empfehlung Folge-Skill plus zwei Sätze Begründung
- Mandantenbrief-Entwurf mit Sachstand und nächsten Schritten

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Quellen

- Paragrafen 111 ff. FamFG (Familiensachen)
- BGH XII. Zivilsenat
- Wendl/Dose
- Schwab Familienrecht

---

## Skill: `fachanwalt-familienrecht-orientierung`

_Wenn es um Fachanwalt für Familienrecht — Orientierung in Fachanwalt Familienrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Fachanwalt für Familienrecht — Orientierung

## Aktuelle Rechtsprechung (Orientierung Familienrecht, Stand 05/2026)

Verifizierte Eckpfeiler — Live-Verifikation vor Verwendung in Schriftsätzen zwingend:

- BGH, Beschluss vom 22.01.2025 - XII ZB 148/24 (Elternunterhalt; Selbstbehalt verheirateter Unterhaltspflichtiger)
- BVerfG, Beschluss vom 07.10.2025 - 1 BvR 746/23 (Begründungsanforderungen bei mehrjährigem Umgangsausschluss)
- BVerfG, Beschluss vom 28.08.2025 - 1 BvR 1473/25 (Sorgerecht im einstweiligen Anordnungsverfahren; PAS)
- BVerfG, Beschluss vom 09.04.2025 - 1 BvR 1618/24 (internationale Zuständigkeit nach KSÜ, Sorgerechtswirkungen)
- Düsseldorfer Tabelle 2026 (in Kraft seit 01.01.2026, OLG Düsseldorf, Pressemitteilung 01.12.2025; Mindestunterhalt nach 7. MUVÄndV vom 15.11.2024, BGBl. 2024 I Nr. 359)

Weitere Entscheidungen nicht aus Modellwissen zitieren; vor Ausgabe über bundesgerichtshof.de, bundesverfassungsgericht.de, dejure.org, openjur.de verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## FAO-Voraussetzungen (Paragraf 5 Abs. 1 FAO)

- **Theoretischer Lehrgang** 120 Stunden (Paragraf 4 FAO).
- **Drei Klausuren** zum Familienrecht (Paragraf 4a FAO).
- **120 Fälle** in den letzten drei Jahren vor Antrag, davon mindestens 60 streitige Fälle (Paragraf 5 FAO).
- **Anmeldung** bei der Rechtsanwaltskammer.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| BGB Familienrecht | Paragrafen 1297 ff. BGB (Ehe Scheidung) Paragrafen 1601 ff. BGB (Unterhalt) Paragrafen 1626 ff. BGB (Elterliche Sorge) Paragrafen 1684 ff. BGB (Umgangsrecht) Paragrafen 1740 ff. BGB (Adoption) Paragrafen 1773 ff. BGB (Vormundschaft) |
| Verfahrensrecht | FamFG Paragrafen 111 ff. (Familiensachen) Paragraf 137 FamFG (Scheidungsverbund) Paragrafen 151 ff. FamFG (Kindschaftssachen) |
| Versorgungsausgleich | VersAusglG |
| Lebenspartnerschaft | LPartG |
| Gerichtsverfassung | Paragraf 23a GVG (Familiengericht beim AG) Paragraf 23b GVG |
| EU- und Völkerrecht | Brüssel IIb-VO (EU) 2019/1111 |

## Typische Mandate

- Scheidung im Verbund (Scheidung + Versorgungsausgleich + Folgesachen)
- Sorgerechtsverfahren bei getrennt lebenden Eltern
- Umgangsrechtsstreit
- Kindesunterhalt nach Düsseldorfer Tabelle
- Ehegattenunterhalt (Trennungs- und nachehelicher Unterhalt)
- Zugewinnausgleich
- Ehevertrag und Scheidungsfolgenvereinbarung
- Gewaltschutz nach GewSchG

## Wichtige Fristen

- **Beschwerde** Paragraf 63 FamFG — ein Monat.
- **Sofortige Beschwerde** Paragraf 64 FamFG — zwei Wochen.
- **Wiedereinsetzung** Paragraf 17 FamFG.
- **Versorgungsausgleichs-Anträge** parallel zum Scheidungsverfahren.
- **Anfechtungsfristen** Vaterschaft Paragraf 1600b BGB — zwei Jahre ab Kenntnis.

## Hauptgericht

- **Familiengericht** beim Amtsgericht (Paragraf 23a Abs. 1 Nr. 1 GVG).
- **OLG-Familiensenat** als Beschwerdegericht (Paragraf 119 GVG).
- **BGH XII. Zivilsenat** in Familiensachen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Berufsverband

- Deutscher Anwaltverein DAV Arbeitsgemeinschaft Familienrecht.
- Deutsche Gesellschaft für Familienrecht.

## Schnittstellen zu anderen Plugins

- **kanzlei-allgemein** für Fristenbuch Timesheet Versand-Vor-Check.
- **methodenlehre-buergerliches-recht** und **zitierweise-deutsches-recht** als Hausstandards.

## Hinweis

Dieses Plugin liefert nur die Orientierung. Tiefe Mandatsbearbeitung erfordert die Expertise des Fachanwalts für Familienrecht.

---

## Skill: `orientierung-fristen-form-und-zustaendigkeit`

_Wenn es um Orientierung Fristen Form Und Zuständigkeit in Fachanwalt Familienrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/VersAusglG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: FamFG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/VersAusglG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.

### Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB Paragrafen 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG Paragrafen 49 ff., 76, 86 ff., 112 ff.; VersAusglG Paragrafen 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, Paragraf 51 VersAusglG, Paragraf 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Spezialwissen: Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg
- **Normen-/Quellenanker:** FamFG.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Orientierung** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `orientierung-mandat-fachanwaltschaft`

_Wenn es um Orientierung Mandat Fachanwaltschaft in Fachanwalt Familienrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Orientierung im Fachanwaltsrecht Familienrecht: FAO-Voraussetzungen, Kerngebiete, Verfahren nach FamFG und BGB überblicken


## Arbeitsbereich

Einstieg in den **Fachanwaltsbereich Familienrecht**. Er klärt zunächst die Verfahrensart (Scheidung, Sorge, Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz, Personenstandsfolgen nach SBGG) und routet anschließend in die tragende Prüfungslinie. Im Mittelpunkt stehen Kindeswohlgefährdung nach Paragraf 1666 BGB, Familienmediation nach Paragraf 156 FamFG und Cochemer Praxis, der Scheidungsantrag (Paragrafen 1564 ff. BGB, Paragraf 133 FamFG) sowie die personenstandsrechtlichen Folgen nach SBGG. Die Prüfungslinien bauen aufeinander auf — zuerst das in der Akte tatsächlich tragende Feld bestimmen, dann ergänzend nur die Felder heranziehen, die der Sachverhalt wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: FamFG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Orientierung im Fachanwaltsrecht Familienrecht: FAO-Voraussetzungen, Kerngebiete, Verfahren nach FamFG und BGB überblicken. Normen: FamFG (Beschluss statt Urteil, Verbund Paragraf 137 FamFG), Paragrafen 23a und 23b GVG (Familiengericht), BGB Familienrecht. Prüfraster: Sachgebiet (Scheidung, Sorge, Umgang, Unterhalt, Zugewinn, VA), Verfahrenstypen, Eilbedürftigkeit. Output Orientierungs-Memo, Routing zu Fachmodule. Abgrenzung: Mandats-Triage siehe mandat-triage-familienrecht; Detailbearbeitungen siehe Fachmodule.

### Fachanwalt für Familienrecht — Orientierung

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Fachanwalt für Familienrecht — Orientierung` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB Paragrafen 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG Paragrafen 49 ff., 76, 86 ff., 112 ff.; VersAusglG Paragrafen 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, Paragraf 51 VersAusglG, Paragraf 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Fachanwalt für Familienrecht — Orientierung
- **Normen-/Quellenanker:** BGB Familienrecht, FamFG, VersAusglG, Unterhaltsrecht, Zugewinn, Gewaltschutz, Kindschaft, internationale Verordnungen und Vollstreckung.
- **Entscheidende Weiche:** Beteiligte, Kind/Unterhalt/Vermögen/Versorgung, Frist, Auskunft, Beleg, Eilbedarf und familiengerichtliche Verfahrensart trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Aktuelle Rechtsprechung (Orientierung Familienrecht, Stand 05/2026)

Verifizierte Eckpfeiler — Live-Verifikation vor Verwendung in Schriftsätzen zwingend:

- BGH, Beschluss vom 22.01.2025 - XII ZB 148/24 (Elternunterhalt; Selbstbehalt verheirateter Unterhaltspflichtiger)
- BVerfG, Beschluss vom 07.10.2025 - 1 BvR 746/23 (Begründungsanforderungen bei mehrjährigem Umgangsausschluss)
- BVerfG, Beschluss vom 28.08.2025 - 1 BvR 1473/25 (Sorgerecht im einstweiligen Anordnungsverfahren; PAS)
- BVerfG, Beschluss vom 09.04.2025 - 1 BvR 1618/24 (internationale Zuständigkeit nach KSÜ, Sorgerechtswirkungen)
- Düsseldorfer Tabelle 2026 (in Kraft seit 01.01.2026, OLG Düsseldorf, Pressemitteilung 01.12.2025; Mindestunterhalt nach 7. MUVÄndV vom 15.11.2024, BGBl. 2024 I Nr. 359)

Weitere Entscheidungen nicht aus Modellwissen zitieren; vor Ausgabe über bundesgerichtshof.de, bundesverfassungsgericht.de, dejure.org, openjur.de verifizieren.

## FAO-Voraussetzungen (Paragraf 5 Abs. 1 FAO)

- **Theoretischer Lehrgang** 120 Stunden (Paragraf 4 FAO).
- **Drei Klausuren** zum Familienrecht (Paragraf 4a FAO).
- **120 Fälle** in den letzten drei Jahren vor Antrag, davon mindestens 60 streitige Fälle (Paragraf 5 FAO).
- **Anmeldung** bei der Rechtsanwaltskammer.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| BGB Familienrecht | Paragrafen 1297 ff. BGB (Ehe Scheidung) Paragrafen 1601 ff. BGB (Unterhalt) Paragrafen 1626 ff. BGB (Elterliche Sorge) Paragrafen 1684 ff. BGB (Umgangsrecht) Paragrafen 1740 ff. BGB (Adoption) Paragrafen 1773 ff. BGB (Vormundschaft) |
| Verfahrensrecht | FamFG Paragrafen 111 ff. (Familiensachen) Paragraf 137 FamFG (Scheidungsverbund) Paragrafen 151 ff. FamFG (Kindschaftssachen) |
| Versorgungsausgleich | VersAusglG |
| Lebenspartnerschaft | LPartG |
| Gerichtsverfassung | Paragraf 23a GVG (Familiengericht beim AG) Paragraf 23b GVG |
| EU- und Völkerrecht | Brüssel IIb-VO (EU) 2019/1111 |

## Typische Mandate

- Scheidung im Verbund (Scheidung + Versorgungsausgleich + Folgesachen)
- Sorgerechtsverfahren bei getrennt lebenden Eltern
- Umgangsrechtsstreit
- Kindesunterhalt nach Düsseldorfer Tabelle
- Ehegattenunterhalt (Trennungs- und nachehelicher Unterhalt)
- Zugewinnausgleich
- Ehevertrag und Scheidungsfolgenvereinbarung
- Gewaltschutz nach GewSchG

## Wichtige Fristen

- **Beschwerde** Paragraf 63 FamFG — ein Monat.
- **Sofortige Beschwerde** Paragraf 64 FamFG — zwei Wochen.
- **Wiedereinsetzung** Paragraf 17 FamFG.
- **Versorgungsausgleichs-Anträge** parallel zum Scheidungsverfahren.
- **Anfechtungsfristen** Vaterschaft Paragraf 1600b BGB — zwei Jahre ab Kenntnis.

## Hauptgericht

- **Familiengericht** beim Amtsgericht (Paragraf 23a Abs. 1 Nr. 1 GVG).
- **OLG-Familiensenat** als Beschwerdegericht (Paragraf 119 GVG).
- **BGH XII. Zivilsenat** in Familiensachen.

## Berufsverband

- Deutscher Anwaltverein DAV Arbeitsgemeinschaft Familienrecht.
- Deutsche Gesellschaft für Familienrecht.

## Schnittstellen zu anderen Plugins

- **kanzlei-allgemein** für Fristenbuch Timesheet Versand-Vor-Check.
- **methodenlehre-buergerliches-recht** und **zitierweise-deutsches-recht** als Hausstandards.

## Hinweis

Dieses Plugin liefert nur die Orientierung. Tiefe Mandatsbearbeitung erfordert die Expertise des Fachanwalts für Familienrecht.

---

## Skill: `erstgespraech-mandatsannahme`

_Wenn es um Erstgespraech Mandatsannahme in Fachanwalt Familienrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Strukturierter Erstgespraechsleitfaden für Familien-, Kindschafts- und Versorgungsausgleichsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen.


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: FamFG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Strukturierter Erstgespraechsleitfaden für Familien-, Kindschafts- und Versorgungsausgleichsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen.

### Erstgespraech und Mandatsannahme im Familien-, Kindschafts- und Versorgungsausgleichsrecht

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Erstgespraech und Mandatsannahme im Familien-, Kindschafts- und Versorgungsausgleichsrecht` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB Paragrafen 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG Paragrafen 49 ff., 76, 86 ff., 112 ff.; VersAusglG Paragrafen 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, Paragraf 51 VersAusglG, Paragraf 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Erstgespraech und Mandatsannahme im Familien-, Kindschafts- und Versorgungsausgleichsrecht
- **Normen-/Quellenanker:** BGB Familienrecht, FamFG, VersAusglG, Unterhaltsrecht, Zugewinn, Gewaltschutz, Kindschaft, internationale Verordnungen und Vollstreckung.
- **Entscheidende Weiche:** Beteiligte, Kind/Unterhalt/Vermögen/Versorgung, Frist, Auskunft, Beleg, Eilbedarf und familiengerichtliche Verfahrensart trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Aktuelle Rechtsprechung (Familienrecht Erstgespräch)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Wann dieser Arbeitsgang greift

- Neue Anfrage aus dem Bereich Familien-, Kindschafts- und Versorgungsausgleichsrecht (Telefon, Mail, Empfehlung, Walk-in).
- Mandantin oder Mandant beschreibt Sachverhalt unstrukturiert; viele Anlagen ohne System.
- Vor jeder weiteren fachlichen Bearbeitung: erst Annahme klären, Konflikt- und GwG-Prüfung, Vollmacht, Streitwert/Vereinbarung, Fristen.

## Phasen des Erstgespraechs

### 1. Aufnahme der Konstellation (10-15 Min.)

Standard-Fragenraster für Familien-, Kindschafts- und Versorgungsausgleichsrecht:

- Beteiligte (Vor-/Nachname, Geburtsdatum, Anschrift, Rolle: Klägerin/Beklagter, Antragsteller, Beschuldigter)
- Konflikt-Kern in einem Satz ("Was ist Ihr Ziel?")
- Konkrete fachliche Stossrichtung: Scheidung, Unterhalt, ZGW, VA, Sorge/Umgang, Gewaltschutz, EheVertrag
- Bisherige Korrespondenz (Bescheide, Schreiben der Gegenseite, anwaltliche Vertretung der Gegenseite?)
- **Fristenscreening sofort:** anstehende Klage-/Widerspruchs-/Einspruchsfristen aus den vorgelegten Schreiben (z.B. Scheidungsantrag, Unterhaltsklage, Sorgerechtsantrag, VA-Beschwerde). Frist-Alarm an die Vorbereitung weitergeben.

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

Standard-Streitwerte im Bereich Familien-, Kindschafts- und Versorgungsausgleichsrecht:

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

- BORA, BRAO, FAO für Fachanwaltschaft Familien-, Kindschafts- und Versorgungsausgleichsrecht.
- GwG, GwGMeldV, Identifizierungsleitfaden BRAK.
- Paragrafen 1297 ff. BGB, FamFG, VersAusglG, UVG, GewSchG, IntFamRVG (für fachliche Erstpruefung).
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

Mandantin kommt am Donnerstag, Frist laeuft am Montag (Klage- oder Widerspruchsfrist im Bereich Familien-, Kindschafts- und Versorgungsausgleichsrecht). Handlungs-Sequenz:

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
- Verfahrensdauer im Bereich Familien-, Kindschafts- und Versorgungsausgleichsrecht: Erfahrungswerte nach Instanz.
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

## Cross-Refs

- `vergleichsverhandlung-strategie` (im selben Plugin) für den Fall, dass aussergerichtliche Loesung angestrebt wird.
- `schriftsatzkern-substantiierung` (im selben Plugin) für den Schriftsatzaufbau, wenn Klage/Widerspruch eingereicht wird.
- Kanzlei-Allgemein-Plugin `kanzlei-allgemein` für Konflikt-, GwG- und PEP-Prüfroutinen.

---

## Skill: `erstpruefung-und-mandatsziel`

_Wenn es um Erstpruefung Und Mandatsziel in Fachanwalt Familienrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten._

# Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/VersAusglG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: FamFG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/VersAusglG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.

### Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB Paragrafen 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG Paragrafen 49 ff., 76, 86 ff., 112 ff.; VersAusglG Paragrafen 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, Paragraf 51 VersAusglG, Paragraf 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Spezialwissen: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** FamFG.

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

## Skill: `fachanwalt-familienrecht-mediation-156-famfg-cochemer`

_Wenn es um Fachanwalt Familienrecht Mediation 156 Famfg Cochemer in Fachanwalt Familienrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt._

## Mandantenfragen beim Kaltstart

1. Haben Sie bereits einen Scheidungs- oder Sorge-/Umgangsrechtsantrag beim Familiengericht eingereicht, oder steht das noch aus?
2. Verweigert der andere Elternteil den Umgang aktiv, oder scheitert die Umsetzung an Kommunikationsproblemen?
3. Gibt es Hinweise auf häusliche Gewalt, Substanzmissbrauch oder Kindeswohlgefährdung gemäß Paragraf 1666 BGB?
4. Hat das Jugendamt bereits Kontakt aufgenommen oder ein Hilfsangebot nach Paragraf 17 SGB VIII unterbreitet?
5. Haben Sie oder Ihr Gegenüber schon an einer Cochemer-Informationsveranstaltung oder einem Erstgespräch beim Beratungsstellen-Netzwerk teilgenommen?
6. Wie alt sind die betroffenen Kinder, und wurde ein Verfahrensbeistand nach Paragraf 158 FamFG bestellt?
7. Welche finanziellen Rahmenbedingungen gelten — Prozesskostenhilfe, Scheidungskosten bereits beziffert?
8. Wurden Vereinbarungen bisher mündlich getroffen, und ist die Gegenseite grundsätzlich einigungsbereit?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

| Norm | Inhalt |
|------|--------|
| Paragraf 156 FamFG | Hinwirkungspflicht des Familiengerichts auf Einvernehmen; Anordnung einer Beratung oder Mediation |
| Paragraf 165 FamFG | Vermittlungsverfahren bei Umgangsverweigerung; Gericht beauftragt Jugendamt oder geeignete Stelle |
| Paragraf 155 FamFG | Vorrang- und Beschleunigungsgebot in Kindschaftssachen; erster Termin innerhalb eines Monats |
| Paragraf 155a FamFG | Frühe Erörterung in Kindschaftssachen; Einbeziehung des Jugendamts |
| Paragraf 158 FamFG | Verfahrensbeistand für das Kind; Aufgaben und Vergütung |
| Paragraf 158a FamFG | Qualifikationsanforderungen an den Verfahrensbeistand |
| Paragraf 1684 BGB | Umgangsrecht des Kindes mit jedem Elternteil; Wohlverhaltenspflicht beider Eltern |
| Paragraf 1666 BGB | Gerichtliche Maßnahmen bei Kindeswohlgefährdung; Ausschluss oder Einschränkung des Umgangs |
| Paragraf 1671 BGB | Alleinige elterliche Sorge auf Antrag eines Elternteils nach Trennung |
| Paragraf 17 SGB VIII | Beratung in Trennungs- und Scheidungssituationen durch Jugendamt; Jugendhilfeleistungen |
| Paragraf 18 SGB VIII | Beratung und Unterstützung bei Ausübung des Umgangsrechts |
| MediationsG | Grundsätze der Mediation; Vertraulichkeit, Freiwilligkeit, Eigenverantwortung |
| Paragraf 278a ZPO | Gerichtliche Mediation / Güterichterverfahren (analog in Familiensachen) |
| Paragraf 127a BGB | Gerichtliche Protokollierung als Ersatz für notarielle Beurkundung bei Vergleichen |
| Paragraf 36 FamFG | Vergleich im familiengerichtlichen Verfahren; Protokollierung mit Vollstreckungswirkung |

## Leitentscheidungen

| Gericht | Aktenzeichen | Datum | Kernaussage |
|---------|-------------|-------|-------------|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## ADR-Pfade im Überblick

| ADR-Pfad | Rechtsgrundlage | Dauer typisch | Kosten ca. | Besonderheit |
|----------|----------------|--------------|------------|--------------|
| Außergerichtliche Familienmediation (DGFM) | MediationsG | 5–10 Sitzungen à 90 min | EUR 100–180/h pro Mediator | Vollständige Vertraulichkeit; Ergebnis als privatschriftliche Vereinbarung |
| Cochemer Modell / Cochemer Praxis | Paragraf 156 FamFG iVm Netzwerkvereinbarungen | 4–8 Wochen | Keine gesonderten Kosten (Jugendamt) | Interdisziplinär: Anwälte, Jugendamt, Gericht, Berater gemeinsam |
| Gerichtliche Mediation / Güterichter | Paragraf 36a FamFG; Paragraf 278a ZPO analog | 1–3 Sitzungen | Keine Mehrkosten (Gerichtsgebühr) | Mediator ist Richter eines anderen Spruchkörpers; Protokoll nach Paragraf 127a BGB |
| Vermittlungsverfahren | Paragraf 165 FamFG | 3 Monate max. | Keine gesonderten Kosten | Nur bei Umgangsverweigerung; Jugendamt oder geeignete Stelle beauftragt |
| Anwaltliche Vergleichsverhandlung | Paragraf 36 FamFG; Paragraf 127a BGB | Nach Absprache | Anwaltsgebühren nach RVG | Vollstreckungsfähiger Vergleich nach Protokollierung |
| Familienkonferenz (Family Group Conference) | Paragraf 17 SGB VIII | 1–2 Konferenztage | Keine (Jugendhilfe) | Erweiterter Familien- und Unterstützerkreis einbezogen |

## Ablauf Cochemer Modell

| Phase | Akteur | Inhalt | Zeitrahmen |
|-------|--------|--------|-----------|
| 1. Eingang Antrag | Familiengericht | Paragraf 155 FamFG: Termin innerhalb 1 Monat; Jugendamt benachrichtigt | Tag 1–5 |
| 2. Frühe Erörterung | Richter + Jugendamt + ggf. Verfahrensbeistand | Paragraf 155a FamFG: Gemeinsamer Termin; Cochemer-Netzwerk aktiviert | Bis Woche 4 |
| 3. Parallele Beratung | Jugendamt Paragraf 17 SGB VIII + Beratungsstelle | Getrennte Elternberatung; Kindeswohl im Mittelpunkt | Woche 4–8 |
| 4. Runder Tisch | Alle Beteiligten inkl. Anwälte | Interdisziplinäres Fallgespräch; keine Parteinahme | Woche 6–10 |
| 5. Einigungsvorschlag | Anwälte + Gericht | Vorläufige Regelung nach Paragraf 156 FamFG; ggf. einstweilige Anordnung | Woche 8–12 |
| 6. Vereinbarung / Beschluss | Familiengericht | Protokollierung Paragraf 127a BGB oder Beschluss nach Paragraf 1684 BGB | Woche 10–14 |

## Prüfschema Paragraf 156 FamFG

**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.


| Schritt | Prüfpunkt | Norm | Rechtsfolge |
|---------|-----------|------|-------------|
| 1 | Kindschaftssache anhängig? (Sorge, Umgang, Kindesherausgabe) | Paragraf 151 FamFG | Anwendungsbereich eröffnet |
| 2 | Vorrang- und Beschleunigungsgebot beachtet? | Paragraf 155 FamFG | Erster Termin binnen 1 Monat zwingend |
| 3 | Gericht hat auf Einvernehmen hingewirkt? | Paragraf 156 Abs. 1 FamFG | Pflicht des Gerichts; bei Unterlassen Beschwerde möglich |
| 4 | Beratung / Mediation angeordnet oder empfohlen? | Paragraf 156 Abs. 1 S. 4 FamFG | Aussetzung des Verfahrens bis zu 3 Monaten zulässig |
| 5 | Umgangsverweigerung konkret? | Paragraf 165 FamFG | Vermittlungsverfahren obligatorisch vor Ordnungsmittel |
| 6 | Kindeswohlgefährdung nach Paragraf 1666 BGB? | Paragrafen 1666, 1666a BGB | Schutzklausel: Mediation ungeeignet; Sofortmaßnahmen |
| 7 | Einigung erzielt? | Paragraf 36 FamFG; Paragraf 127a BGB | Protokollierung; Vollstreckungstitel nach Paragraf 86 FamFG |
| 8 | Keine Einigung erzielt? | Paragraf 1684 Abs. 3, 4 BGB | Gerichtliche Regelung; ggf. Umgangsausschluss als ultima ratio |

## Prüfschema Paragraf 165 FamFG Vermittlungsverfahren

| Schritt | Prüfpunkt | Norm | Rechtsfolge |
|---------|-----------|------|-------------|
| 1 | Vollstreckungsfähiger Umgangstitel vorhanden? | Paragrafen 86, 89 FamFG | Voraussetzung für Vermittlungsverfahren |
| 2 | Titelschuldner hat Umgang verweigert? | Paragraf 89 FamFG | Ordnungsmittel grundsätzlich möglich |
| 3 | Gericht hat Vermittlungsverfahren eingeleitet? | Paragraf 165 Abs. 1 FamFG | Jugendamt oder geeignete Stelle beauftragt |
| 4 | Anhörungstermin durchgeführt? | Paragraf 165 Abs. 3 FamFG | Beide Eltern persönlich geladen; Ordnungsgeld bei Nichterscheinen |
| 5 | Einigung im Vermittlungsverfahren? | Paragraf 165 Abs. 4 FamFG | Protokollierung als Vergleich |
| 6 | Kein Erfolg? | Paragraf 165 Abs. 5 FamFG | Rückmeldung an Gericht; Ordnungsmittelverfahren nach Paragraf 89 FamFG |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Familienrechtliche Mediation oder Cochemer Modell | Schriftsatzbausteine unten; Antraegeauswahl nach Konstellation |
| Variante A — beide Seiten kooperativ | Direktes Mediationsverfahren ohne Gerichtsantrag |
| Variante B — eine Seite blockiert | Gerichtlicher Vermittlungsantrag Paragraf 165 FamFG als Druckmittel |
| Variante C — Kindeswohl gefaehrdet | Cochemer Modell nicht ausreichend; Kinderschutzverfahren erwaegen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatz-Bausteine

### Antrag auf gerichtliche Mediation / Güterichterverfahren

```
An das Amtsgericht – Familiengericht – [Ort]

In dem Verfahren [Az.] beantragen wir namens des/der Antragstellers/in:

Das Gericht möge das Verfahren aussetzen und die Sache einem Güterichter
nach Paragraf 36a FamFG zur Durchführung eines Güterichterverfahrens überweisen
(Paragraf 278a ZPO analog).

Begründung:
Die Beteiligten sind grundsätzlich einigungsbereit. Eine einvernehmliche Regelung
zur elterlichen Sorge / zum Umgang dient dem Kindeswohl nach Paragraf 1697a BGB besser
als eine streitige Entscheidung. Die Überweisung an den Güterichter ermöglicht eine
flexible, auf die Besonderheiten der Familie abgestimmte Lösung im Rahmen des
Paragraf 156 FamFG.

[Ort, Datum]
Rechtsanwalt/Rechtsanwältin [Name]
```

### Antrag auf Einleitung Vermittlungsverfahren Paragraf 165 FamFG

```
An das Amtsgericht – Familiengericht – [Ort]

In dem Verfahren [Az.] beantragen wir namens des/der Antragstellers/in:

Das Gericht möge gemäß Paragraf 165 Abs. 1 FamFG ein Vermittlungsverfahren einleiten
und das Jugendamt [Ort] mit der Vermittlung beauftragen.

Begründung:
Der Antragsgegner/die Antragsgegnerin verweigert seit dem [Datum] die Durchführung
des titulierten Umgangs (Beschluss/Vergleich vom [Datum], Az. [X]). Vor Einleitung
des Ordnungsmittelverfahrens nach Paragraf 89 FamFG ist das Vermittlungsverfahren
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Die Antragstellerin/der Antragsteller ist zur Teilnahme bereit.

[Ort, Datum]
Rechtsanwalt/Rechtsanwältin [Name]
```

### Mediationsvereinbarung (Muster Schlussprotokoll)

```
MEDIATIONSVEREINBARUNG

Die Beteiligten [Name 1] und [Name 2] haben in dem Mediationsverfahren
(Mediator: [Name], zertifiziert nach MediationsG) vom [Datum] bis [Datum]
folgende Vereinbarung getroffen:

1. Umgang: Das Kind [Name], geb. [Datum], verbringt den Umgang mit
   [Elternteil] wie folgt: [Regelung].

2. Übergaben: Die Übergabe erfolgt [Ort/Modalitäten].

3. Kommunikation: Die Eltern kommunizieren über [App/E-Mail] ausschließlich
   zum Wohl des Kindes.

4. Überprüfung: Die Vereinbarung wird nach [6 Monaten] gemeinsam evaluiert.

Diese Vereinbarung wird nach Paragraf 127a BGB gerichtlich protokolliert und erlangt
damit Vollstreckungswirkung nach Paragraf 86 FamFG.

[Ort, Datum]
[Unterschriften beider Elternteile und Mediator]
```

### Antrag auf Bestellung Verfahrensbeistand

```
An das Amtsgericht – Familiengericht – [Ort]

In dem Verfahren [Az.] beantragen wir namens des/der Antragstellers/in:

Das Gericht möge für das Kind [Name], geb. [Datum], einen Verfahrensbeistand
gemäß Paragraf 158 FamFG bestellen.

Begründung:
Das vorliegende Verfahren betrifft das Umgangsrecht in einer hochstrittigen
Trennungssituation. Die Interessen des Kindes sind durch die Elternkonflikte
gefährdet. Ein Verfahrensbeistand gemäß Paragraf 158 Abs. 2 FamFG ist zur angemessenen
Interessenvertretung des Kindes erforderlich. Die Qualifikationsanforderungen nach
Paragraf 158a FamFG sind bei der Auswahl zu beachten.

[Ort, Datum]
Rechtsanwalt/Rechtsanwältin [Name]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]


## Beweislast

| Beweisthema | Beweislast | Beweismittel |
|------------|-----------|--------------|
| Umgangsverweigerung | Antragsteller (umgangsberechtigter Elternteil) | Kommunikationsprotokolle, Zeugen, Terminkalender |
| Kindeswohlgefährdung Paragraf 1666 BGB | Amtsermittlung (Paragraf 26 FamFG); kein Beweislastgrundsatz | Jugendamtsbericht, Sachverständigengutachten, Aussage Verfahrensbeistand |
| Bereitschaft zur Mediation | Kein formaler Nachweis erforderlich; Glaubhaftmachung | Schriftliche Einladung, E-Mail-Korrespondenz |
| Erfolg der Mediation / Einigung | Urkundlich durch Protokoll | Gerichtliches Protokoll nach Paragraf 127a BGB; Mediationsprotokoll |
| Gewalt / Schutzklausel | Derjenige, der ADR-Ausschluss beantragt | Polizeiberichte, Strafanzeigen, einstweilige Schutzanordnung nach GewSchG |

## Fristen

| Frist | Inhalt | Norm |
|-------|--------|------|
| 1 Monat | Erster Gerichtstermin nach Eingang Antrag in Kindschaftssachen | Paragraf 155 Abs. 2 FamFG |
| 3 Monate | Maximale Aussetzung für außergerichtliche Mediation | Paragraf 156 Abs. 1 S. 4 FamFG |
| 3 Monate | Gesamtdauer Vermittlungsverfahren Paragraf 165 FamFG | Paragraf 165 Abs. 4 FamFG |
| 1 Monat | Beschwerde gegen Umgangsbeschluss (Ausgangsgericht) | Paragraf 63 FamFG |
| 2 Wochen | Ordnungsmittelankündigung vor Vollstreckung | Paragraf 89 Abs. 2 FamFG |
| Sofort | Einstweilige Anordnung bei Kindeswohlgefährdung Paragraf 1666 BGB | Paragraf 49 FamFG |

## Gegenargumente und Reaktion

| Gegenargument | Herkunft | Reaktion |
|--------------|---------|----------|
| "Mediation ist freiwillig — ich verweigere die Teilnahme" | Titelschuldner | Gerichtliche Anordnung nach Paragraf 156 FamFG möglich; Kostentragung bei Verweigerung; Ordnungsmittel nach Paragraf 89 FamFG als nächste Stufe |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "Häusliche Gewalt schließt Mediation aus" | Antragsgegner/in | Prüfung nach Paragraf 1666 BGB; bei konkreter Gefährdung Ausschluss der ADR; bis zur Klärung Schutzanordnung GewSchG |
| "Cochemer Modell ist nicht gesetzlich verankert" | Gegenanwalt | Paragraf 156 FamFG iVm kommunalen Netzwerkvereinbarungen; praktizierende Gerichte in fast allen Bundesländern; keine Gesetzesbindung nötig |
| "Mediationsergebnis ist nicht vollstreckbar" | Mandant | Protokollierung nach Paragraf 127a BGB schafft Vollstreckungstitel; alternativ gerichtlicher Beschluss nach Paragraf 86 FamFG |
| "Verfahrensbeistand ist parteiisch für Mutter/Vater" | Elternteil | Paragraf 158 FamFG: Auftrag allein dem Kindeswohl; Qualifikation nach Paragraf 158a FamFG; Beschwerde bei nachgewiesener Einseitigkeit |

## Streitwert und Kosten

**Verfahrenswert Umgangssachen:** EUR 3000 (Paragraf 45 Abs. 1 Nr. 2 FamGKG, Regelwert).
Erhöhung auf EUR 5.000–8.000 bei komplexen Hochkonfliktfällen möglich (Paragraf 45 Abs. 3 FamGKG, billiges Ermessen).

**Verfahrenswert Sorgerechtssachen:** EUR 4.000 (Paragraf 45 Abs. 1 Nr. 1 FamGKG).

**Mediationskosten:**
- Außergerichtliche Familienmediation (DGFM-zertifiziert): EUR 100–180/h pro Mediator; 5–10 Sitzungen à 90 min = EUR 1.500–3.600 gesamt je nach Stundensatz und Sitzungszahl.
- Gerichtliche Mediation / Güterichter: Keine Mehrkosten zur Gerichtsgebühr; bereits in Verfahrensgebühr enthalten.
- Vermittlungsverfahren Paragraf 165 FamFG durch Jugendamt: Gebührenfrei für Beteiligte.

**Anwaltsgebühren (RVG):**
- Verfahrensgebühr 1.3 VV RVG aus EUR 3000 = ca. EUR 262.60
- Terminsgebühr 1.2 VV RVG = ca. EUR 218.00
- Einigungsgebühr 1.5 VV RVG bei Abschluss = ca. EUR 262.60
- Zzgl. Auslagen und 19 % MwSt.

**Verfahrensbeistand:** EUR 350 pauschal je Instanz (Paragraf 158 Abs. 7 FamFG) oder nach tatsächlichem Aufwand.

**PKH/VKH:** Paragraf 76 FamFG iVm Paragrafen 114 ff. ZPO; bewilligungsfähig für Mediation als Nebenkosten, wenn Verfahren anhängig.

## Strategische Empfehlung

| Situation | Empfehlung | Begründung |
|-----------|------------|-----------|
| Erste Trennung, beide Elternteile kooperationswillig | Sofortige Familienmediation außergerichtlich (DGFM); kein Gerichtsverfahren einleiten | Günstigster, schnellster Weg; Vereinbarung nach Paragraf 127a BGB protokollieren |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Hochkonfliktfamilie, kein Konsens möglich | Cochemer Modell aktivieren über Paragraf 156 FamFG; Verfahrensbeistand Paragraf 158 FamFG beantragen | Interdisziplinäre Struktur entlastet Gerichte; Kindesinteresse im Fokus |
| Häusliche Gewalt / Paragraf 1666 BGB-Verdacht | Keine ADR; sofortige einstweilige Anordnung; Paragraf 1666 BGB-Verfahren | Sicherheit vor Einigung; Schutzanordnung GewSchG parallel |
| Einigung erzielt, aber fragile Umsetzung | Gerichtliche Protokollierung Paragraf 127a BGB + Follow-up-Mediation nach 6 Monaten | Vollstreckungstitel als Sicherheitsnetz; präventive Eskalationsminderung |
| Elternteil sabotiert Mediation systematisch | Ordnungsmittelverfahren Paragraf 89 FamFG; Beantragung Sorgerechtsübertragung Paragraf 1671 BGB | Grenzen der ADR; gerichtlicher Schutz des Umgangsrechts als Kindesrecht |

## Anschluss-Skills

- `fachanwalt-familienrecht-umgangsregelung-mustervorlagen` — Konkrete Umgangsregelungen und Beschlussmuster
- `fachanwalt-familienrecht-scheidungsantrag-stellen` — Einleitung des Scheidungsverfahrens parallel zur Umgangsregelung
- `fachanwalt-familienrecht-sbgg-personenstandswechsel-folgen` — Personenstandsrelevante Folgefragen
- `fachanwalt-familienrecht-duesseldorfer-tabelle-unterhalt` — Unterhaltsberechnung im Kontext des Sorge-/Umgangsverfahrens

## Quellen

- Paragraf 156 FamFG: https://www.gesetze-im-internet.de/famfg/__156.html
- Paragraf 165 FamFG: https://www.gesetze-im-internet.de/famfg/__165.html
- Paragraf 1684 BGB: https://www.gesetze-im-internet.de/bgb/__1684.html
- MediationsG: https://www.gesetze-im-internet.de/mediationsg/
- BGH XII ZB 99/20: https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bgh&Art=en&az=XII%20ZB%2099/20
- BVerfG 1 BvR 1491/11: https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2012/02/rs20120201_1bvr149111.html
- Cochemer Modell Überblick: https://www.cochemer-modell.de/
- DGFM Familienmediation: https://www.dgfm.de/

---

## Anwendungshinweise

1. Diesen Vollprüfung als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

