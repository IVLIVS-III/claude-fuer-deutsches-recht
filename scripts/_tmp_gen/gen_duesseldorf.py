#!/usr/bin/env python3
"""Erzeugt Aktenstuecke 16-25 fuer starug-aufhebung-holding-duesseldorf-ix-zb-18-25."""
import sys
sys.path.insert(0, "/home/user/workspace/legal-work/target/scripts/_tmp_gen")
from aktenbau import make_docx, TESTAKTEN

D = TESTAKTEN / "starug-aufhebung-holding-duesseldorf-ix-zb-18-25"
KOPF = "Quirrenbach & Partner mbB | Rechtsanwaelte | Duesseldorf"

# 16 - Kostenentscheidung BGH nachtrag
make_docx(
    D / "16_kostenfestsetzungsbeschluss_bgh_2026-05-19.docx",
    KOPF,
    "Kostenfestsetzungsbeschluss — BGH, IX ZB 18/25",
    [
        "Bundesgerichtshof, IX. Zivilsenat, Geschaeftszeichen IX ZB 18/25",
        "Rechtspflegerin am Bundesgerichtshof — Kostenfestsetzungsbeschluss vom 19.05.2026",
        "## Tenor",
        "Die von der Schuldnerin, Silberweiher Beteiligungs GmbH, an die Rheinboden Kreditbank AG "
        "zu erstattenden Kosten des Rechtsbeschwerdeverfahrens IX ZB 18/25 werden auf 8.940,17 EUR "
        "nebst Zinsen in Hoehe von 5 Prozentpunkten ueber dem Basiszinssatz seit dem 24.04.2026 festgesetzt.",
        "## Gruende",
        "Die Kostengrundentscheidung ergibt sich aus Ziffer 2 des Beschlusses vom 23.04.2026 (IX ZB 18/25). "
        "Die Rheinboden Kreditbank AG hat mit Schriftsatz vom 12.05.2026 eine Kostenrechnung ueber "
        "1,3 Verfahrensgebuehr nach Nr. 3206 VV RVG aus einem Gegenstandswert von 610.054,00 EUR "
        "zuzueglich Auslagenpauschale und Umsatzsteuer vorgelegt. Die Berechnung ist nicht zu beanstanden.",
        "## Kostenaufstellung",
        "- 1,3 Verfahrensgebuehr Nr. 3206 VV RVG (Gegenstandswert 610.054,00 EUR): 7.234,30 EUR",
        "- Auslagenpauschale Nr. 7002 VV RVG: 20,00 EUR",
        "- Zwischensumme: 7.254,30 EUR",
        "- 19 Prozent Umsatzsteuer: 1.378,32 EUR",
        "- Gesamtbetrag: 8.632,62 EUR (rechnerisch korrigiert auf 8.940,17 EUR wegen Nebenintervention Fedder & Sohst)",
    ],
    "Die Rechtspflegerin",
)

# 17 - Insolvenzantrag der Holding nach Aufhebung
make_docx(
    D / "17_eigenantrag_insolvenz_silberweiher_2026-05-28.docx",
    KOPF,
    "Eigenantrag auf Eroeffnung des Insolvenzverfahrens — Silberweiher Beteiligungs GmbH",
    [
        "Amtsgericht Duesseldorf — Insolvenzgericht",
        "Antragstellerin: Silberweiher Beteiligungs GmbH, Grafenberger Allee 214, 40237 Duesseldorf",
        "vertreten durch den Geschaeftsfuehrer Dr. Cornelius Wefing",
        "## Antrag",
        "Namens und im Auftrag der Schuldnerin wird beantragt, ueber das Vermoegen der Silberweiher "
        "Beteiligungs GmbH das Insolvenzverfahren zu eroeffnen.",
        "## Begruendung",
        "Nachdem der Bundesgerichtshof mit Beschluss vom 23.04.2026 (IX ZB 18/25) die Rechtsbeschwerde "
        "gegen die Aufhebung der Restrukturierungssache 603 RES 6/24 zurueckgewiesen hat, ist die "
        "bereits am 06.12.2024 angezeigte Zahlungsunfaehigkeit nicht mehr abwendbar. Die Rheinboden "
        "Kreditbank AG hat die Zwangsvollstreckung aus der faelliggestellten Buergschaftsforderung "
        "ueber 610.054,00 EUR wiederaufgenommen; liquide Mittel zur Befriedigung stehen nicht zur Verfuegung.",
        "## Vermoegensuebersicht",
        "- Aktiva: Beteiligungen an zwei insolventen Tochtergesellschaften (Buchwert 0,00 EUR), Kassenbestand 4.180,00 EUR",
        "- Passiva: Rheinboden Kreditbank AG 610.054,00 EUR, Fedder & Sohst 1.897,00 EUR, "
        "Verfahrenskosten BGH 8.940,17 EUR, sonstige Verbindlichkeiten rund 12.300,00 EUR",
        "Es wird angeregt, Rechtsanwalt Dr. Markus Ovelgoenne, Duesseldorf, zum vorlaeufigen "
        "Insolvenzverwalter zu bestellen.",
    ],
    "Dr. Cornelius Wefing, Geschaeftsfuehrer",
)

# 18 - Eroeffnungsbeschluss
make_docx(
    D / "18_eroeffnungsbeschluss_2026-08-03.docx",
    KOPF,
    "Beschluss ueber die Eroeffnung des Insolvenzverfahrens",
    [
        "Amtsgericht Duesseldorf, Az. 512 IN 88/26",
        "Beschluss vom 03.08.2026",
        "## Tenor",
        "1. Ueber das Vermoegen der Silberweiher Beteiligungs GmbH, Grafenberger Allee 214, "
        "40237 Duesseldorf, wird heute um 09:15 Uhr das Insolvenzverfahren eroeffnet.",
        "2. Zum Insolvenzverwalter wird bestellt: Rechtsanwalt Dr. Markus Ovelgoenne, Duesseldorf.",
        "3. Die Glaeubiger der Schuldnerin werden aufgefordert, ihre Forderungen bis zum 15.09.2026 "
        "beim Insolvenzverwalter schriftlich anzumelden.",
        "4. Termin zur Pruefung der angemeldeten Forderungen sowie zum Berichtstermin wird bestimmt "
        "auf den 20.10.2026, 10:00 Uhr, Saal 233.",
        "## Gruende",
        "Die Schuldnerin ist zahlungsunfaehig im Sinne des Paragraf 17 InsO. Dies ergibt sich aus dem "
        "eigenen Vorbringen sowie aus dem Gutachten des Sachverstaendigen vom 15.07.2026.",
    ],
    "Der Richter am Amtsgericht",
)

# 19 - Forderungsanmeldung Rheinboden
make_docx(
    D / "19_forderungsanmeldung_rheinboden_2026-08-25.docx",
    "Rheinboden Kreditbank AG | Recovery Management",
    "Forderungsanmeldung zur Insolvenztabelle",
    [
        "An den Insolvenzverwalter Dr. Markus Ovelgoenne, Duesseldorf",
        "Insolvenzverfahren Silberweiher Beteiligungs GmbH, Az. 512 IN 88/26",
        "## Anmeldung",
        "Die Rheinboden Kreditbank AG meldet zur Insolvenztabelle folgende Forderung an:",
        "- Hauptforderung aus Hoechstbetragsbuergschaft (Faelligstellung vom 02.12.2024): 610.054,00 EUR",
        "- Zinsen seit Faelligstellung bis Verfahrenseroeffnung (03.08.2026): 47.612,30 EUR",
        "- Kostenerstattung aus BGH-Verfahren IX ZB 18/25 (Kostenfestsetzungsbeschluss vom 19.05.2026): 8.940,17 EUR",
        "- Gesamtforderung: 666.606,47 EUR",
        "Rang: einfache Insolvenzforderung nach Paragraf 38 InsO. Eine abgesonderte Befriedigung wird "
        "nicht geltend gemacht, da die Buergschaft ungesichert war.",
    ],
    "i.A. Recovery Management, Rheinboden Kreditbank AG",
)

# 20 - Forderungspruefungsprotokoll
make_docx(
    D / "20_forderungspruefungsprotokoll_2026-10-20.docx",
    KOPF,
    "Protokoll des Pruefungstermins",
    [
        "Amtsgericht Duesseldorf, Az. 512 IN 88/26, Termin vom 20.10.2026",
        "## Ergebnis der Forderungspruefung",
        "- Rheinboden Kreditbank AG, 666.606,47 EUR: festgestellt in voller Hoehe, kein Widerspruch",
        "- Fedder & Sohst, 1.897,00 EUR: festgestellt in voller Hoehe",
        "- Finanzamt Duesseldorf-Nord (Gewerbesteuer 2025), 3.240,00 EUR: festgestellt",
        "- Sonstige Kleinglaeubiger (IT-Dienstleister, Buerobedarf): 2.114,90 EUR: festgestellt",
        "- Gesamtsumme der festgestellten Insolvenzforderungen: 673.858,37 EUR",
        "## Berichtstermin",
        "Der Insolvenzverwalter berichtet, dass eine Fortfuehrung der Schuldnerin mangels operativen "
        "Geschaeftsbetriebs nicht in Betracht kommt. Die Beteiligungen an den beiden Tochtergesellschaften "
        "sind wertlos, da diese sich bereits im eigenen Insolvenzverfahren befinden. Es wird die "
        "masselose Abwicklung angestrebt.",
    ],
    "Protokollfuehrerin der Geschaeftsstelle",
)

# 21 - Gutachten Zahlungsunfaehigkeit Nachtrag (fuer Insolvenzverfahren, nicht StaRUG)
make_docx(
    D / "21_gutachten_masseunzulaenglichkeit_2026-09-01.docx",
    "Dr. Ovelgoenne Rechtsanwaltsgesellschaft | Vorlaeufiger Insolvenzverwalter",
    "Gutachten zur Insolvenzfaehigkeit und Massekostendeckung",
    [
        "Amtsgericht Duesseldorf, Az. 512 IN 88/26",
        "Gutachten vom 01.09.2026",
        "## Feststellungen",
        "1. Die Schuldnerin ist zahlungsunfaehig gemaess Paragraf 17 InsO seit dem 06.12.2024 "
        "(Anzeige nach Paragraf 32 Abs. 3 StaRUG).",
        "2. Ueberschuldung liegt ebenfalls vor: Aktiva 4.180,00 EUR Kassenbestand gegen Passiva von "
        "voraussichtlich 673.858,37 EUR.",
        "3. Die Kosten des Verfahrens (voraussichtlich 9.500,00 EUR) sind durch den vorhandenen "
        "Kassenbestand sowie einen Kostenvorschuss der Geschaeftsfuehrung in Hoehe von 6.000,00 EUR gedeckt.",
        "## Empfehlung",
        "Eroeffnung des Insolvenzverfahrens wird empfohlen. Eine Sanierung scheidet aus, da die "
        "Schuldnerin ueber keinen eigenen Geschaeftsbetrieb verfuegt und reine Holdingfunktion hatte.",
    ],
    "Dr. Markus Ovelgoenne, vorlaeufiger Insolvenzverwalter",
)

# 22 - Schlussbericht
make_docx(
    D / "22_schlussbericht_verwalter_2027-02-10.docx",
    "Dr. Ovelgoenne Rechtsanwaltsgesellschaft | Insolvenzverwalter",
    "Schlussbericht des Insolvenzverwalters",
    [
        "Amtsgericht Duesseldorf, Az. 512 IN 88/26",
        "Schlussbericht vom 10.02.2027",
        "## Verfahrensverlauf",
        "Nach Eroeffnung am 03.08.2026 wurden Forderungen in Hoehe von 673.858,37 EUR festgestellt. "
        "Eine Verwertung nennenswerter Aktiva war mangels operativen Geschaeftsbetriebs nicht moeglich. "
        "Die Beteiligungen an den Tochtergesellschaften Rheinaue Logistik GmbH und Bergischer Anlagenbau "
        "GmbH blieben wertlos, da beide Gesellschaften zwischenzeitlich mangels Masse eingestellt wurden.",
        "## Masseverzeichnis",
        "- Kassenbestand bei Eroeffnung: 4.180,00 EUR",
        "- Kostenvorschuss der Geschaeftsfuehrung: 6.000,00 EUR",
        "- Verwertungserloes Bueroausstattung: 890,00 EUR",
        "- Gesamtmasse: 11.070,00 EUR",
        "- Verfahrenskosten (Gerichtskosten, Verwaltervergueting): 9.480,00 EUR",
        "- Verteilungsmasse an Insolvenzglaeubiger: 1.590,00 EUR (Quote rund 0,24 Prozent)",
        "## Antrag",
        "Es wird beantragt, das Insolvenzverfahren nach Vollzug der Schlussverteilung gemaess "
        "Paragraf 200 InsO aufzuheben.",
    ],
    "Dr. Markus Ovelgoenne, Insolvenzverwalter",
)

# 23 - Verteilungsverzeichnis
make_docx(
    D / "23_schlussverteilungsverzeichnis_2027-03-15.docx",
    KOPF,
    "Schlussverteilungsverzeichnis",
    [
        "Amtsgericht Duesseldorf, Az. 512 IN 88/26",
        "Verzeichnis vom 15.03.2027",
        "## Verteilung auf festgestellte Forderungen (Quote 0,236 Prozent)",
        "- Rheinboden Kreditbank AG (666.606,47 EUR): Quotenzahlung 1.573,20 EUR",
        "- Fedder & Sohst (1.897,00 EUR): Quotenzahlung 4,48 EUR",
        "- Finanzamt Duesseldorf-Nord (3.240,00 EUR): Quotenzahlung 7,65 EUR",
        "- Sonstige Kleinglaeubiger (2.114,90 EUR): Quotenzahlung 4,99 EUR",
        "- Summe Verteilungsmasse: 1.590,32 EUR",
        "Die Verteilung erfolgt nach Rechtskraft des Schlusstermins gemaess Paragraf 196 InsO.",
    ],
    "Der Insolvenzverwalter",
)

# 24 - Aufhebungsbeschluss Insolvenzverfahren
make_docx(
    D / "24_aufhebungsbeschluss_insolvenzverfahren_2027-04-30.docx",
    KOPF,
    "Beschluss ueber die Aufhebung des Insolvenzverfahrens",
    [
        "Amtsgericht Duesseldorf, Az. 512 IN 88/26",
        "Beschluss vom 30.04.2027",
        "## Tenor",
        "Das Insolvenzverfahren ueber das Vermoegen der Silberweiher Beteiligungs GmbH wird nach "
        "Vollzug der Schlussverteilung gemaess Paragraf 200 Abs. 1 InsO aufgehoben.",
        "## Gruende",
        "Der Schlusstermin hat am 20.04.2027 stattgefunden. Einwendungen gegen die Schlussrechnung "
        "wurden nicht erhoben. Die Verteilungsmasse von 1.590,32 EUR wurde quotal an die festgestellten "
        "Insolvenzglaeubiger ausgekehrt. Da die Schuldnerin eine GmbH ist, fuehrt die Aufhebung des "
        "Insolvenzverfahrens mangels Restvermoegen zur Aufloesung gemaess Paragraf 60 Abs. 1 Nr. 4 GmbHG.",
    ],
    "Der Richter am Amtsgericht",
)

# 25 - Schlussvermerk der Kanzlei
make_docx(
    D / "25_schlussvermerk_kanzlei_2027-05-12.docx",
    KOPF,
    "Schlussvermerk zur Handakte",
    [
        "Mandat: Silberweiher Beteiligungs GmbH ./. StaRUG-Aufhebung und Folgeinsolvenz",
        "Verfasst am 12.05.2027 von Rechtsanwalt Dr. Alexander Quirrenbach",
        "## Zusammenfassung",
        "Die Restrukturierungssache 603 RES 6/24 wurde am 15.01.2025 aufgehoben; die hiergegen "
        "gerichteten Rechtsmittel blieben in allen drei Instanzen ohne Erfolg (zuletzt BGH, Beschluss "
        "vom 23.04.2026, IX ZB 18/25). Die Schuldnerin zeigte bereits waehrend des Beschwerdeverfahrens "
        "die Zahlungsunfaehigkeit an; nach rechtskraeftigem Abschluss des Rechtsbeschwerdeverfahrens "
        "wurde am 28.05.2026 Eigenantrag gestellt. Das Insolvenzverfahren (512 IN 88/26) wurde am "
        "03.08.2026 eroeffnet und nach Schlussverteilung mit einer Quote von 0,236 Prozent am "
        "30.04.2027 aufgehoben. Die Schuldnerin ist damit gemaess Paragraf 60 Abs. 1 Nr. 4 GmbHG "
        "aufgeloest.",
        "## Bewertung",
        "Der Fall bestaetigt die vom BGH aufgestellten Massstaebe zu Paragraf 33 Abs. 2 Satz 1 Nr. 1 "
        "StaRUG: Ein nicht rechtsverbindlich zugesagter Drittbeitrag genuegt nicht, um von der "
        "Aufhebung abzusehen. Das Mandat wird als abgeschlossen zu den Akten genommen.",
    ],
    "Dr. Alexander Quirrenbach, Rechtsanwalt",
)

print("Duesseldorf 16-25 erzeugt.")
