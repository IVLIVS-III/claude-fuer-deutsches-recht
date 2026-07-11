---
name: einstieg-routing
description: "Wenn es um Anwalts-Dashboard Fachanwalt Insolvenz- und Sanierungsrecht in Fachanwalt Insolvenz- und Sanierungsrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

# Anwalts-Dashboard Fachanwalt Insolvenz- und Sanierungsrecht

> Antragspflicht, Eigenverwaltung, Anfechtung, Restrukturierung: Der Antrag ist ohne schuldhaftes Zögern zu stellen; drei Wochen bei Zahlungsunfähigkeit und sechs Wochen bei Überschuldung sind nur Höchstfristen.
>
> Sie sehen unten die Sofort-Triage. Keine Rückfragen, bis die Tabelle steht. Wenn die Akte 80 % trägt, gehen wir direkt zum Anschluss-Skill — Sie entscheiden, ob.

## Sofort-Triage

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
| --- | --- | --- |
| Rolle | Wen vertrete ich? (Mandant · Gegenseite · Mehrere) | Mandantenmail, Vertretungsbestellung |
| Verfahrensstand | Vorprozessual · außergerichtlich · Klage · Rechtsmittel · Vollstreckung | Vorhandene Schriftsätze, Eingangsstempel |
| Eilfrist | **Paragraf 15a Absatz 1 InsO:** Antrag ohne schuldhaftes Zögern, höchstens drei Wochen bei Zahlungsunfähigkeit und sechs Wochen bei Überschuldung. **Paragraf 270d InsO:** Schutzschirm nur bei drohender Zahlungsunfähigkeit oder Überschuldung und fehlender Zahlungsunfähigkeit. | Objektiven Eintritt des Insolvenzgrunds und gerichtliche Bekanntmachungen dokumentieren |
| Hauptanspruch | Antragspflicht §§ 15a, 17 ff. InsO · Anfechtung §§ 129 ff. InsO · GF-Haftung § 64 GmbHG a. F. / § 15b InsO n. F. · Gläubigeranfechtung AnfG außerhalb Insolvenz · Schutzschirm § 270d InsO · Eigenverwaltung § 270 InsO · StaRUG (Stabilisierungs- und Restrukturierungsrahmen). | Sachverhaltsabgleich mit Tatbestandsmerkmalen |
| Zuständigkeit | Insolvenzgericht (AG am Sitz, § 3 InsO). Restrukturierungsgericht nach StaRUG = LG (§§ 30 ff. StaRUG). Anfechtungsklage gegen Gläubiger: LG/AG nach Streitwert. | Gesetz, Vertrag, Gerichtsstandsklausel |

## Risiko-Ampel

- **Frist:** 🔴 Paragraf 15a InsO: ohne schuldhaftes Zögern, höchstens drei Wochen ab Zahlungsunfähigkeit und sechs Wochen ab Überschuldung. Keine Höchstfrist als Sanierungsaufschub behandeln. 🟠 Eigenverwaltung nach Paragraf 270a ff. InsO und Schutzschirm nach Paragraf 270d InsO nur bei erfüllten Voraussetzungen vorbereiten.
- **Beweislage:** 🔴 Zahlungsunfähigkeit § 17 II InsO: 3-Wochen-Liquiditätsstatus. Buchhaltungs- und Bankkontodaten sichern. 🟠 Überschuldung § 19 II InsO: Fortbestehensprognose dokumentieren.
- **Wirtschaftlich:** 🔴 Zahlungen nach Insolvenzreife unter Paragraf 15b InsO einzeln erfassen und nur nach dessen Maßstab fortführen. 🟠 Bei Paragraf 133 InsO den Grundzeitraum von zehn Jahren, den Vierjahreszeitraum für Sicherung oder Befriedigung und die Sonderregeln der Absätze 3 und 4 auseinanderhalten.

## Anschluss-Skills (Router)

| Wenn der Fall trägt … | dann Skill | Erwartung |
| --- | --- | --- |
| Fortbestehensprognose anwerfen | `insanw-fortbestehensprognose-workflow` | Liquiditätsplan 12 Monate, IDW S 11, Beweisdokument |
| Eigenverwaltung / Schutzschirm Paragraf 270d InsO | `insanw-eigenverwaltung-schutzschirm-spezial` | Eigenverwaltungsplanung, Bescheinigung, Planvorlagefrist, Sachwalter |
| **Antragspflicht Paragraf 15a InsO** | `inso-p015a-antragspflicht-bei-juristischen-personen-und-rechtsfa` | unverzüglicher Antrag, Drei-/Sechswochen-Höchstfrist, Organhaftung, Strafrecht |
| Anfechtungsmandat (Gläubiger / Verwalter) | `insanw-anfechtungsmandat-leitfaden` | Tatbestände §§ 129 ff. InsO, Verteidigungsstrategie |
| Konzerninsolvenz / Gruppenkoordination | `insanw-konzerninsolvenz-koordination-spezial` | Gruppen-Gerichtsstand § 3a InsO, Koordinationsverfahren |

## Norm-Radar (live verifizieren)

- **Paragraf 15a InsO** — Insolvenzantragspflicht ohne schuldhaftes Zögern; höchstens drei Wochen bei Zahlungsunfähigkeit und sechs Wochen bei Überschuldung
- **§ 17 InsO** — Zahlungsunfähigkeit
- **§ 19 InsO** — Überschuldung
- **§ 270 InsO** — Eigenverwaltung; § 270d Schutzschirm
- **Paragraf 133 InsO** — zehnjähriger Grundzeitraum; vier Jahre, wenn die Handlung Sicherung oder Befriedigung gewährt oder ermöglicht; Absatz 3 und 4 gesondert prüfen
- **§ 15b InsO** — Zahlungsverbot nach Insolvenzreife

## Genau eine Rückfrage (nur wenn nötig)

> Stehen wir **vor** der Antragstellung (Beratung GF / Sanierung) oder **nach** Verfahrenseröffnung (Verwalter, Gläubiger, Anfechtung)?

Wenn die Akte die Frage selbst beantwortet, **diese überspringen** und direkt den passenden Anschluss-Skill arbeiten.

## Leitentscheidungs-Anker (Such-Wegweiser, keine fertigen Zitate)

- **Verwerterpflichten; höchstmögliche Erlöserzielung** — BGH IX. Zivilsenat (Linie IX ZR 169/04 v. 13.04.2006, fortgeführt) — *live verifizieren auf* `bundesgerichtshof.de`
- **Vorsatzanfechtung § 133 InsO; Bargeschäfts-Ausnahme** — BGH IX. Zivilsenat (Linienwandel ab 2021) — *live verifizieren auf* `bundesgerichtshof.de`
- **Insolvenzantragspflicht § 15a InsO; § 15b InsO Zahlungsverbot** — BGH II./IX. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Geschäftsveräußerung im Ganzen § 1 Ia UStG** — EuGH C-497/01 (Zita Modes); EuGH C-444/10 (Schriever); BFH — *live verifizieren auf* `curia.europa.eu + bfh.bund.de`

> Diese Anker sind Sucheinstieg. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle prüfen und Datum, Aktenzeichen, Randnummer abklären. Kuratierte Anker-Sammlung in `references/leitentscheidungen-anker.md`.

## Hinweis

Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Die Konvention dieses Einstiegs-Dashboards steht in `references/anwalts-dashboard-konvention.md`.
