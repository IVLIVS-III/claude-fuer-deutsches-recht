#!/usr/bin/env python3
"""Ausbau der Akte luftrecht-airline-insolvenz-flugzeugpfand-flughafen."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from aktenbau import make_docx, make_eml, make_csv, make_xlsx, make_jpg, TESTAKTEN

SLUG = "luftrecht-airline-insolvenz-flugzeugpfand-flughafen"
D = TESTAKTEN / SLUG
KOPF = "Airbus Financial Services (Dublin) Designated Activity Company ./. Flughafen Dortmund GmbH u.a. - Az. 3-08 O 66/26 LG Frankfurt am Main"

# 11 Insolvenzeroeffnungsbeschluss der Airline
make_docx(
    D / "11-insolvenzeroeffnungsbeschluss-airline.docx",
    "Amtsgericht Dortmund - Insolvenzgericht", "Beschluss ueber die Eroeffnung des Insolvenzverfahrens",
    [
        "Az. 257 IN 44/26",
        "In dem Insolvenzverfahren ueber das Vermoegen der WestAir Regional GmbH, Flughafenring 3, 44319 Dortmund "
        "(Fluggesellschaft, AOC Nr. DE-1042, IATA-Code WR), wird am 14.01.2026, 09:00 Uhr, das Insolvenzverfahren eroeffnet.",
        "Zum Insolvenzverwalter wird bestellt: Rechtsanwalt Dr. Henning Kaltenborn, Kaltenborn Rechtsanwaelte "
        "Partnerschaft mbB, Duesseldorf.",
        "Der Schuldnerin wird ein allgemeines Verfuegungsverbot auferlegt.",
        "Pruefungstermin: 18.03.2026, 10:00 Uhr, Saal 214, Amtsgericht Dortmund.",
        "Dortmund, den 14.01.2026",
    ],
    "Rechtspflegerin am Amtsgericht Dortmund",
)

# 12 Vorlaeufige Sicherungsanordnung
make_docx(
    D / "12-vorlaeufige-sicherungsanordnung.docx",
    "Amtsgericht Dortmund - Insolvenzgericht", "Beschluss - Vorlaeufige Sicherungsmassnahmen (§ 21 InsO)",
    [
        "Az. 257 IN 44/26",
        "Im Insolvenzeroeffnungsverfahren ueber das Vermoegen der WestAir Regional GmbH wird bereits am 20.11.2025 "
        "auf Eigenantrag vom 18.11.2025 Rechtsanwalt Dr. Henning Kaltenborn zum vorlaeufigen Insolvenzverwalter "
        "mit Zustimmungsvorbehalt bestellt.",
        "Der Schuldnerin wird aufgegeben, keine Verfuegungen ueber das Anlagevermoegen, insbesondere die im "
        "Halterregister eingetragenen Luftfahrzeuge, ohne Zustimmung des vorlaeufigen Insolvenzverwalters "
        "vorzunehmen.",
        "Dortmund, den 20.11.2025",
    ],
)

# 13 Luftfahrzeug-Registerauszug LBA
make_docx(
    D / "13-luftfahrzeug-registerauszug-lba.docx",
    "Luftfahrt-Bundesamt (LBA), Referat Luftfahrzeugrolle", "Registerauszug Luftfahrzeugrolle - D-AWRB",
    [
        "Auszug aus der Luftfahrzeugrolle gemaess § 14 LuftVZO, Stand 05.02.2026.",
        "## Luftfahrzeug",
        "Muster: Airbus A320-214, Werknummer (MSN) 6217, Kennzeichen D-AWRB, Baujahr 2016.",
        "## Halterin",
        "WestAir Regional GmbH, Flughafenring 3, 44319 Dortmund.",
        "## Eigentumsverhaeltnisse (Anmerkung)",
        "Eigentuemerin ist ausweislich vorgelegter Unterlagen die Airbus Financial Services (Dublin) Designated "
        "Activity Company, Dublin, Irland, aufgrund Kaufleasingvertrags vom 02.03.2016. Eine Eintragung von "
        "Eigentumsrechten Dritter erfolgt in der deutschen Luftfahrzeugrolle nicht; insoweit wird auf das "
        "internationale Register nach dem Kapstadt-Uebereinkommen (Cape Town Convention) verwiesen.",
    ],
)

# 14 Kaufleasingvertrag Airbus Financial Services
make_docx(
    D / "14-kaufleasingvertrag-airbus-financial-services.docx",
    KOPF, "Kaufleasingvertrag (Finance Lease) ueber ein Luftfahrzeug Airbus A320-214, MSN 6217",
    [
        "Aircraft Lease Agreement vom 02.03.2016 zwischen Airbus Financial Services (Dublin) DAC (Lessor) und "
        "WestAir Regional GmbH (Lessee) ueber das Luftfahrzeug Airbus A320-214, MSN 6217, Kennzeichen D-AWRB.",
        "## Wesentliche Konditionen",
        "Laufzeit: 144 Monate ab Uebergabe (Delivery 01.04.2016). Monatliche Leasingrate: USD 285.000,00. "
        "Kaufoption zum Laufzeitende gegen Restzahlung USD 4.200.000,00 (Finance Lease/Kaufleasing).",
        "## Sicherungsrechte",
        "Zur Sicherung ihrer Anspruche laesst sich die Lessor eine International Interest gemaess dem "
        "Kapstadter Uebereinkommen ueber internationale Sicherungsrechte an beweglicher Ausruestung (Cape Town "
        "Convention) im International Registry eintragen (Registrierungsnummer siehe Anlage Registerauszug).",
        "## Kuendigung",
        "Bei Zahlungsverzug von mehr als 60 Tagen oder Insolvenzantrag ist die Lessor zur fristlosen Kuendigung "
        "und Rueckforderung des Luftfahrzeugs berechtigt (Art. 13 Cape Town Convention - Self-Help Remedies).",
        "Dublin/Dortmund, den 02.03.2016",
    ],
)

# 15 Sicherungsübereignung Aircraft Mortgage Cape Town
make_docx(
    D / "15-aircraft-mortgage-cape-town-convention.docx",
    "International Registry (Aviareto, Dublin)", "Aircraft Mortgage / International Interest - Registrierungsauszug",
    [
        "Registration Summary, International Registry established under the Convention on International "
        "Interests in Mobile Equipment (Cape Town Convention, 2001) and the Protocol on Matters Specific to "
        "Aircraft Equipment.",
        "Registration Number: CTC-2016-0304-AFS-6217",
        "Debtor: WestAir Regional GmbH. Creditor: Airbus Financial Services (Dublin) DAC.",
        "Object: Airframe MSN 6217 (Airbus A320-214).",
        "Nature of interest: International Interest (Prospective) converted to registered International "
        "Interest upon delivery, priority date 02.03.2016.",
        "Status: aktiv, keine Loeschung eingetragen (Stand Abfrage 06.02.2026).",
    ],
)

# 16 Flughafenentgeltordnung Auszug
make_docx(
    D / "16-flughafenentgeltordnung-auszug.docx",
    "Flughafen Dortmund GmbH", "Entgeltordnung fuer die Nutzung der Flughafeneinrichtungen (Auszug)",
    [
        "Auszug aus der genehmigten Entgeltordnung, gueltig ab 01.01.2025.",
        "## Landeentgelt",
        "EUR 8,40 je angefangener Tonne höchstzulässiges Startgewicht (MTOW); bei Airbus A320-214 "
        "(MTOW 78 t) je Landung EUR 655,20.",
        "## Standgebuehr",
        "Ab dem dritten Standtag EUR 145,00 je Kalendertag und Luftfahrzeug, zzgl. Sicherungsentgelt "
        "EUR 38,00 je Tag bei nicht betriebsbereiten Luftfahrzeugen.",
        "## Verzugszinsen",
        "Bei Zahlungsverzug werden Verzugszinsen in Hoehe von 9 Prozentpunkten ueber dem Basiszinssatz "
        "sowie eine Mahnpauschale von EUR 40,00 je Mahnung erhoben.",
    ],
)

# 17 Rechnung Flughafen offene Landeentgelte + Standgebühren
rows_rech = [
    ["01.08.2025-31.08.2025", "12 Landungen", "7.862,40"],
    ["01.09.2025-30.09.2025", "10 Landungen", "6.552,00"],
    ["01.10.2025-31.10.2025", "0 Landungen (Grounding ab 08.10.)", "0,00"],
    ["01.10.2025-31.01.2026 Standgebuehr D-AWRB", "116 Tage a EUR 183,00", "21.228,00"],
    ["Mahngebuehren (3 Mahnungen)", "-", "120,00"],
]
make_csv(
    D / "17-rechnung-flughafen-landeentgelte-standgebuehren.csv",
    ["Zeitraum/Position", "Menge", "Betrag (EUR)"],
    rows_rech,
)

# 18 Aktenvermerk Flughafen-Justiziar § 20 LuftVG
make_docx(
    D / "18-aktenvermerk-justiziar-20-luftvg.docx",
    "Flughafen Dortmund GmbH, Rechtsabteilung", "Aktenvermerk: Anwendung des Zuruckbehaltungs-/Pfandrechts gemaess § 20 LuftVG",
    [
        "Verfasserin: Dr. Annegret Wessels, Justiziarin Flughafen Dortmund GmbH. Datum: 10.11.2025.",
        "Gemaess § 20 LuftVG steht dem Halter eines Flugplatzes wegen der Entgelte fuer die Benutzung des "
        "Flugplatzes ein Pfandrecht an dem Luftfahrzeug zu, das dem Pfandrecht des Vermieters nach den "
        "Vorschriften des Buergerlichen Gesetzbuches gleichsteht. Das Pfandrecht entsteht kraft Gesetzes (ex lege) "
        "und bedarf keiner Eintragung.",
        "Vorliegend steht das Luftfahrzeug D-AWRB seit dem 08.10.2025 (Grounding wegen technischer Beanstandung "
        "durch das LBA sowie fehlender Betriebsmittel) auf dem Vorfeld C, Stellplatz 14, des Flughafens Dortmund.",
        "Zu klaeren ist das Verhaeltnis des gesetzlichen Pfandrechts nach § 20 LuftVG zu den Rechten der Airbus "
        "Financial Services aus dem Kaufleasingvertrag sowie zur Insolvenzeroeffnung ueber das Vermoegen der Halterin.",
    ],
)

# 19 Kollisionsprüfung § 51 InsO vs Pfandrecht ex lege
make_docx(
    D / "19-kollisionspruefung-51-inso-pfandrecht-ex-lege.docx",
    "Kanzlei Dr. Kaltenborn - interner Vermerk", "Kollisionspruefung: Aussonderungsrecht Leasinggeberin vs. Pfandrecht Flughafen gemaess § 20 LuftVG",
    [
        "Verfasser: RA Dr. Henning Kaltenborn, Insolvenzverwalter. Datum: 25.11.2025.",
        "## Ausgangslage",
        "Zwei konkurrierende dingliche Positionen am Luftfahrzeug D-AWRB: (1) Eigentum/Aussonderungsrecht der "
        "Airbus Financial Services aus dem Kaufleasingvertrag gemaess § 47 InsO, (2) gesetzliches Pfandrecht "
        "des Flughafens Dortmund gemaess § 20 LuftVG fuer offene Flughafenentgelte, das als Absonderungsrecht "
        "gemaess § 50 Abs. 1 InsO analog dem vermieterlichen Pfandrecht zu behandeln ist.",
        "## Rechtliche Einordnung",
        "Das Pfandrecht des Flughafens nach § 20 LuftVG entsteht unabhaengig von den Eigentumsverhaeltnissen "
        "am Luftfahrzeug und geht insoweit dem schuldrechtlichen Herausgabeanspruch der Leasinggeberin im "
        "Rang vor, als es sich auf die Zeit vor Rueckgabe bezieht. Es begruendet jedoch kein Recht, das "
        "Aussonderungsrecht der Eigentuemerin insgesamt zu verdraengen; vielmehr ist die Herausgabe gemaess "
        "§ 50 InsO nur gegen Befriedigung des Pfandglaeubigers oder Sicherheitsleistung zu erwarten.",
        "## Zwischenergebnis",
        "Eine Herausgabe des Luftfahrzeugs an die Airbus Financial Services kommt nur Zug um Zug gegen "
        "Ausgleich der offenen Flughafenentgelte in Betracht, sofern der Flughafen sein Pfandrecht nicht "
        "freiwillig aufgibt.",
    ],
)

# 20 Aussonderungsklage Airbus Financial Services LG Frankfurt
make_docx(
    D / "20-aussonderungsklage-lg-frankfurt.docx",
    KOPF, "Klageschrift auf Herausgabe (Aussonderung) - Airbus Financial Services ./. Flughafen Dortmund GmbH",
    [
        "An das Landgericht Frankfurt am Main, Zivilkammer. Eingereicht durch Rechtsanwaelte Merten & Cohnen, "
        "Frankfurt am Main, fuer die Airbus Financial Services (Dublin) DAC.",
        "## Klageantrag",
        "1. Die Beklagte wird verurteilt, das Luftfahrzeug Airbus A320-214, MSN 6217, Kennzeichen D-AWRB, "
        "derzeit Vorfeld C, Stellplatz 14, Flughafen Dortmund, an die Klaegerin herauszugeben.",
        "2. Hilfsweise: Herausgabe Zug um Zug gegen Zahlung von EUR 35.762,40 (offene Landeentgelte und "
        "Standgebuehren gemaess Rechnung vom 05.11.2025).",
        "## Begruendung (Auszug)",
        "Die Klaegerin ist gemaess Kaufleasingvertrag vom 02.03.2016 zivilrechtliche Eigentuemerin des "
        "Luftfahrzeugs und nach wirksamer Kuendigung des Leasingvertrags vom 20.11.2025 zur Herausgabe berechtigt. "
        "Ein etwaiges Pfandrecht der Beklagten aus § 20 LuftVG rechtfertigt allenfalls ein Zurueckbehaltungsrecht, "
        "nicht jedoch eine dauerhafte Verweigerung der Herausgabe.",
        "Frankfurt am Main, den 02.12.2025",
    ],
)

# 21 Klageerwiderung Insolvenzverwalter (als Streitgenosse/Beigeladener)
make_docx(
    D / "21-klageerwiderung-flughafen-dortmund.docx",
    "Flughafen Dortmund GmbH ./. Airbus Financial Services", "Klageerwiderung",
    [
        "Eingereicht durch Rechtsanwaeltin Dr. Annegret Wessels fuer die Flughafen Dortmund GmbH.",
        "## Antrag",
        "Die Klage wird abgewiesen, hilfsweise: Herausgabe nur Zug um Zug gegen vollstaendigen Ausgleich "
        "saemtlicher bis zur Herausgabe entstandener Flughafenentgelte einschliesslich der bis zum Zeitpunkt "
        "der tatsaechlichen Abholung weiter auflaufenden Standgebuehren.",
        "## Begruendung",
        "Der Beklagten steht ein gesetzliches Pfandrecht gemaess § 20 LuftVG an dem Luftfahrzeug zu, das "
        "unabhaengig von den vertraglichen Beziehungen zwischen Klaegerin und Insolvenzschuldnerin besteht. "
        "Die Beklagte hat ein berechtigtes Interesse, das Luftfahrzeug erst nach vollstaendiger Zahlung "
        "freizugeben, da eine Vollstreckung gegen die insolvente Halterin aussichtslos erscheint.",
        "Dortmund, den 20.12.2025",
    ],
)

# 22 Beschluss AG über Freigabe/Herausgabe
make_docx(
    D / "22-beschluss-freigabe-herausgabe.docx",
    "Landgericht Frankfurt am Main", "Beschluss (Zwischenvergleich/Freigabebeschluss)",
    [
        "Az. 3-08 O 66/26",
        "Im Termin zur muendlichen Verhandlung vom 15.01.2026 einigen sich die Parteien auf folgenden "
        "gerichtlichen Vergleich: Die Beklagte gibt das Luftfahrzeug D-AWRB Zug um Zug gegen Zahlung von "
        "EUR 29.008,00 (reduzierter Betrag nach Verrechnung mit Wartungsleistungen) durch die Klaegerin frei. "
        "Die Kosten des Rechtsstreits werden gegeneinander aufgehoben.",
        "Frankfurt am Main, den 15.01.2026",
    ],
)

# 23 Zwangsversteigerungsantrag Flughafen (Alternative, hilfsweise gestellt und wieder zurückgenommen)
make_docx(
    D / "23-zwangsversteigerungsantrag-flughafen-hilfsweise.docx",
    "Flughafen Dortmund GmbH", "Hilfsweise gestellter Antrag auf Verwertung des Pfandrechts gemaess § 1233 BGB analog",
    [
        "Vorsorglich fuer den Fall des Scheiterns der Vergleichsverhandlungen gestellter Antrag vom 08.01.2026 "
        "auf Verwertung des Pfandrechts durch oeffentliche Versteigerung des Luftfahrzeugs D-AWRB.",
        "Nach Einigung im Termin vom 15.01.2026 (siehe Vergleichsbeschluss) wird der Antrag von der "
        "Flughafen Dortmund GmbH mit Schriftsatz vom 16.01.2026 zurueckgenommen.",
    ],
)

# 24 Wertgutachten Flugzeug DEKRA-Aviation
make_docx(
    D / "24-wertgutachten-dekra-aviation.docx",
    KOPF, "Wertgutachten DEKRA Aviation GmbH - Marktwert Airbus A320-214, MSN 6217",
    [
        "Gutachten Nr. DKA-2026-0071 vom 22.01.2026, erstellt von Dipl.-Ing. Carsten Ohlendorf, DEKRA Aviation GmbH.",
        "## Zustand",
        "Das Luftfahrzeug wurde nach dreieinhalbmonatigem Grounding technisch begutachtet. Fluglaerm- und "
        "Triebwerksstunden: 34.120 FH / 21.860 Cycles. Wesentlicher technischer Mangel: Anzeige eines "
        "Bremssystemfehlers, der zum Grounding durch das LBA fuehrte; nach Voreinschaetzung binnen 2 Wochen "
        "behebbar (Austausch Bremssteuergeraet, Kosten ca. EUR 65.000,00).",
        "## Marktwert",
        "Base Value (Zeitwert ohne Beruecksichtigung des aktuellen Mangels): USD 21.500.000,00. "
        "Unter Beruecksichtigung des Bremssystemmangels und der abgelaufenen C-Check-Frist: "
        "Current Market Value USD 19.800.000,00.",
    ],
)

# 25 Kaufvertrag Zweitverwertung Rumpf und Triebwerke (alternative Verwertung, hier: kein Verkauf sondern Rückführung, aber Alternativszenario dokumentiert)
make_docx(
    D / "25-alternativpruefung-zweitverwertung-teilezerlegung.docx",
    KOPF, "Interne Alternativpruefung: Teilezerlegung (Part-Out) als Verwertungsoption",
    [
        "Vermerk der Airbus Financial Services vom 18.12.2025 zur Frage, ob im Falle einer gescheiterten "
        "Einigung mit dem Flughafen eine Teilezerlegung (Part-Out) des Luftfahrzeugs wirtschaftlicher waere "
        "als die Rueckfuehrung in den Flugbetrieb.",
        "Ergebnis: Bei einem geschaetzten Erloes aus Triebwerken (2x CFM56-5B) von je USD 4.200.000,00 und "
        "Rumpf-/Ersatzteilwert von USD 6.800.000,00 waere ein Part-Out wirtschaftlich attraktiv, wuerde jedoch "
        "die Kaufoption der Halterin endgueltig vereiteln. Da eine einvernehmliche Freigabe erzielt wurde "
        "(siehe Vergleichsbeschluss), wird die Option nicht weiterverfolgt; das Luftfahrzeug wird nach "
        "Freigabe an einen neuen Leasingnehmer (SkyBridge Airlines) vermittelt.",
    ],
)

# 26 Auskehr Erlös Rangordnung
rows_rang = [
    ["1. Rang: Flughafen Dortmund (Pfandrecht § 20 LuftVG)", "29.008,00"],
    ["2. Rang: Verfahrenskosten/Reparatur Bremssystem (vorschussweise Airbus Financial Services)", "65.000,00"],
    ["3. Rang: Restforderung Leasingraten zur Insolvenztabelle Airline", "1.847.500,00"],
]
make_csv(
    D / "26-auskehr-erloes-rangordnung.csv",
    ["Position", "Betrag (EUR/USD gemischt, siehe Vermerk)"],
    rows_rang,
)

# 27 Cape-Town-Convention-Registerauszug (Löschung nach Freigabe)
make_docx(
    D / "27-cape-town-convention-registerauszug-loeschungsvermerk.docx",
    "International Registry (Aviareto, Dublin)", "Registerauszug mit Loeschungsvermerk International Interest",
    [
        "Registration Number: CTC-2016-0304-AFS-6217",
        "Discharge Registration filed 25.01.2026 following amicable release of the aircraft and "
        "restructuring of the lease relationship with a new operator (SkyBridge Airlines).",
        "Status: International Interest geloescht am 25.01.2026, neue Registrierung zugunsten SkyBridge "
        "Airlines als neue Betreiberin (Registrierungsnummer CTC-2026-0125-AFS-6217).",
    ],
)

# 28 Beweissicherungsantrag Wartungshistorie
make_docx(
    D / "28-beweissicherungsantrag-wartungshistorie.docx",
    KOPF, "Antrag auf selbstaendiges Beweisverfahren - Sicherung der Wartungshistorie (Aircraft Records)",
    [
        "Antrag der Airbus Financial Services vom 10.11.2025 an das Landgericht Frankfurt am Main auf "
        "Sicherung der vollstaendigen Wartungsdokumentation (Aircraft Technical Records, Logbooks) des "
        "Luftfahrzeugs D-AWRB, da bei Insolvenz der Halterin die Gefahr des Verlustes oder der Vermischung "
        "der Unterlagen mit anderen Flotten-Dokumenten besteht.",
        "Begruendung: Vollstaendige und lueckenlose Wartungsdokumentation ist wesentliche Voraussetzung fuer "
        "die Wiederzulassung und den Marktwert des Luftfahrzeugs; ein Verlust wuerde den Wert erheblich mindern.",
    ],
)

# 29 Anfechtungsprüfung § 130 InsO Rückzahlung Landeentgelte
make_docx(
    D / "29-anfechtungspruefung-130-inso-landeentgelte.docx",
    "Kanzlei Dr. Kaltenborn - interner Vermerk", "Anfechtungspruefung § 130 InsO - Zahlungen an Flughafen Dortmund im Dreimonatszeitraum",
    [
        "Vermerk vom 02.02.2026. Zu pruefen ist, ob die von der WestAir Regional GmbH im Zeitraum "
        "August/September 2025 (also innerhalb der letzten drei Monate vor dem Eigenantrag vom 18.11.2025) "
        "an den Flughafen Dortmund geleisteten Zahlungen in Hoehe von insgesamt EUR 14.414,40 wegen "
        "kongruenter Deckung bei Kenntnis der (drohenden) Zahlungsunfaehigkeit gemaess § 130 InsO anfechtbar sind.",
        "## Zwischenergebnis",
        "Da die Zahlungen laufende, im engen zeitlichen und sachlichen Zusammenhang mit der Gegenleistung "
        "(Landung, Vorfeldnutzung) stehende Entgelte betreffen, spricht viel fuer eine Behandlung als "
        "Bargeschaeft gemaess § 142 InsO, sodass eine Anfechtung nach vorlaeufiger Einschaetzung nicht in "
        "Betracht kommt. Eine abschliessende Pruefung erfolgt nach Vorlage der vollstaendigen Kontoauszuege.",
    ],
)

print("Luftrecht/Airline: Kernstuecke 11-29 erzeugt.")
