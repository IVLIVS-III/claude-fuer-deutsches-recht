#!/usr/bin/env python3
"""Ausbau der Akte leasingrecht-maschinenfleet-restwert-insolvenz (Rotorwerk)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from aktenbau import make_docx, make_eml, make_csv, make_xlsx, make_jpg, TESTAKTEN

SLUG = "leasingrecht-maschinenfleet-restwert-insolvenz"
D = TESTAKTEN / SLUG
KOPF = "Rotorwerk Praezisionstechnik GmbH ./. NordLease Maschinen-Leasing GmbH - Az. 4 O 218/26 LG Bielefeld"

# 10 Leasingvertrag Volltext mit AGB
make_docx(
    D / "10-leasingvertrag-volltext-mit-agb.docx",
    KOPF, "Maschinen-Leasingvertrag Nr. NL-2022-0847 (Volltext mit AGB)",
    [
        "Zwischen der NordLease Maschinen-Leasing GmbH, Herforder Str. 112, 33609 Bielefeld (Leasinggeberin) "
        "und der Rotorwerk Praezisionstechnik GmbH, Gewerbepark Sennestadt 7, 33689 Bielefeld (Leasingnehmerin) "
        "wird nachfolgender Leasingvertrag ueber zwoelf CNC-Bearbeitungszentren des Typs Haas VF-6SS geschlossen.",
        "## § 1 Leasingobjekte",
        "Zwoelf CNC-Bearbeitungszentren Haas VF-6SS, Seriennummern siehe Anlage 1 (Objektliste), Lieferant "
        "Haas Automation Europe, Anschaffungswert je Einheit EUR 187.400,00 netto, Gesamtanschaffungswert EUR 2.248.800,00 netto.",
        "## § 2 Laufzeit und Raten",
        "Grundmietzeit 60 Monate ab Uebergabe (01.03.2022 bis 28.02.2027). Monatliche Leasingrate je Objekt EUR 3.890,00 zzgl. USt., "
        "Gesamtrate EUR 46.680,00 zzgl. USt. monatlich fuer die Flotte. Zahlbar bis zum 3. Werktag eines Monats im Voraus.",
        "## § 3 Restwert und Andienungsrecht",
        "Kalkulierter Restwert nach Ablauf der Grundmietzeit je Objekt EUR 42.000,00 (insgesamt EUR 504.000,00). Der Leasingnehmerin "
        "steht kein Andienungsrecht zu; die Leasinggeberin ist berechtigt, das Objekt am Markt zu verwerten und einen etwaigen "
        "Mindererloes gegenueber dem kalkulierten Restwert nachzufordern (§ 12 dieser AGB).",
        "## § 8 AGB - Kuendigung aus wichtigem Grund",
        "Die Leasinggeberin kann den Vertrag fristlos kuendigen, wenn die Leasingnehmerin mit mindestens zwei Monatsraten "
        "vollstaendig oder mit einem Teilbetrag von mindestens einer Monatsrate laenger als sechs Wochen in Verzug ist, "
        "oder wenn ein Insolvenzantrag ueber das Vermoegen der Leasingnehmerin gestellt wird. Im Kuendigungsfall sind saemtliche "
        "Leasingobjekte unverzueglich, spaetestens binnen 5 Werktagen, an eine von der Leasinggeberin benannte Adresse "
        "auf Kosten der Leasingnehmerin zurueckzufuehren.",
        "## § 12 AGB - Verwertung und Nachforderung",
        "Nach Rueckgabe verwertet die Leasinggeberin die Objekte bestmoeglich. Der Verwertungserloes wird auf die "
        "restlichen Leasingraten sowie den kalkulierten Restwert angerechnet. Ein danach verbleibender Fehlbetrag "
        "(Mindererloes) wird der Leasingnehmerin bzw. deren Insolvenzmasse in Rechnung gestellt.",
        "## § 14 AGB - Software und Maschinensteuerung",
        "Die Steuerungssoftware der Leasingobjekte bleibt im Eigentum des Herstellers und wird der Leasingnehmerin "
        "lediglich zur Nutzung waehrend der Vertragslaufzeit ueberlassen (gesonderter Lizenzvertrag mit Haas Automation Europe).",
        "Bielefeld, den 24.02.2022",
    ],
    "NordLease Maschinen-Leasing GmbH, i.V. Sabine Krohn (Vertriebsleitung) / Rotorwerk Praezisionstechnik GmbH, i.V. Thorsten Wibbeling (Geschaeftsfuehrer)",
)

# 11 Objektliste Vollversion
make_docx(
    D / "11-objektliste-seriennummern-standorte-vollversion.docx",
    KOPF, "Objektliste mit Seriennummern und Standorten (Vollversion, Anlage 1 zum Leasingvertrag)",
    [
        "Vollstaendige Liste der zwoelf Leasingobjekte mit Seriennummern, Standort und Zustand zum Stichtag der Kuendigung (12.01.2026).",
        "## Objektuebersicht",
        "- Objekt 1, S/N HVF6-22091, Halle A Bielefeld, betriebsbereit",
        "- Objekt 2, S/N HVF6-22092, Halle A Bielefeld, betriebsbereit",
        "- Objekt 3, S/N HVF6-22093, Halle A Bielefeld, Softwarefehler seit 09/2025, Stillstand",
        "- Objekt 4, S/N HVF6-22094, Halle A Bielefeld, Mangel Spindellagerung, Stillstand seit 11/2025",
        "- Objekt 5, S/N HVF6-22095, Halle B Bielefeld, betriebsbereit",
        "- Objekt 6, S/N HVF6-22096, Halle B Bielefeld, betriebsbereit",
        "- Objekt 7, S/N HVF6-22097, Halle B Bielefeld, betriebsbereit",
        "- Objekt 8, S/N HVF6-22098, Halle B Bielefeld, Softwarefehler seit 09/2025, Stillstand",
        "- Objekt 9, S/N HVF6-22099, Zweigwerk Herford, betriebsbereit",
        "- Objekt 10, S/N HVF6-22100, Zweigwerk Herford, betriebsbereit",
        "- Objekt 11, S/N HVF6-22101, Baustelle Pilsen/Tschechien (Vorarbeiter-Aussage), Verbleib streitig",
        "- Objekt 12, S/N HVF6-22102, Baustelle Pilsen/Tschechien (Vorarbeiter-Aussage), Verbleib streitig",
        "## Anmerkung Objekte 11 und 12",
        "Die Leasingnehmerin bestreitet eine Zustimmung der Leasinggeberin zum Auslandseinsatz. Laut internem Fahrtenbuch "
        "wurden beide Maschinen am 14.08.2025 durch die Spedition Trescher Schwertransporte auf eine Baustelle der "
        "Rotorwerk-Tochter Rotorwerk CZ s.r.o. nach Pilsen verbracht. Ein schriftlicher Zustimmungsantrag vom 30.07.2025 "
        "liegt in der Akte (siehe Anlage E-Mail-Verkehr), eine ausdrueckliche Genehmigung der NordLease ist nicht dokumentiert.",
    ],
)

# 12 Bilanzansatz Leasingnehmer
make_docx(
    D / "12-bilanzansatz-leasingnehmer-rechnungsabgrenzung.docx",
    KOPF, "Bilanzansatz bei der Leasingnehmerin - Rechnungsabgrenzung zum 31.12.2025",
    [
        "Auszug aus dem Anhang zum Jahresabschluss 2025 der Rotorwerk Praezisionstechnik GmbH, erstellt durch "
        "Steuerberatung Winkelmann & Partner, Bielefeld.",
        "## Bilanzielle Behandlung",
        "Der Maschinen-Leasingvertrag mit der NordLease Maschinen-Leasing GmbH wird als Operating-Leasing behandelt "
        "(Bilanzierung beim wirtschaftlichen Eigentuemer NordLease). Die Rotorwerk Praezisionstechnik GmbH weist "
        "die laufenden Leasingraten als Aufwand aus.",
        "## Rechnungsabgrenzungsposten",
        "- Aktiver RAP zum 31.12.2025: EUR 46.680,00 (Vorauszahlung Januarrate 2026)",
        "- Ruecklage fuer drohende Nachforderungen aus Restwertabrechnung: EUR 180.000,00 (Einschaetzung Geschaeftsfuehrung, ungewiss)",
        "## Pruefungshinweis Wirtschaftspruefer",
        "Der Abschlusspruefer (Diplom-Kaufmann Achim Roeder, Roeder Treuhand GmbH) weist im Pruefungsbericht auf ein "
        "wesentliches Risiko aus der streitigen Restwertabrechnung sowie der ungeklaerten Verbringung zweier Objekte "
        "ins Ausland hin und empfiehlt eine Ruecklagenbildung von mindestens EUR 250.000,00.",
    ],
)

# 13 Wertgutachten DEKRA
make_docx(
    D / "13-wertgutachten-dekra.docx",
    KOPF, "Wertgutachten DEKRA Automobil GmbH, Niederlassung Bielefeld - Marktwertermittlung CNC-Bearbeitungszentren",
    [
        "Gutachten Nr. DEKRA-MB-2026-0334 vom 02.02.2026, erstellt von Dipl.-Ing. Frank Osterhoff, "
        "oeffentlich bestellter und vereidigter Sachverstaendiger fuer Werkzeugmaschinen.",
        "## Auftrag",
        "Ermittlung des Marktwerts (Zeitwert) der zehn am Standort Bielefeld/Herford verbliebenen Haas VF-6SS "
        "CNC-Bearbeitungszentren zum Stichtag 20.01.2026 nach Besichtigung und Funktionspruefung.",
        "## Ergebnis je Objekt (Auszug)",
        "- Objekte 1, 2, 5, 6, 7, 9, 10 (betriebsbereit, altersgemaesser Zustand): je EUR 34.500,00",
        "- Objekt 3 (Softwarefehler, behebbar): EUR 29.800,00 (Minderung wegen Ausfallzeit und Nacharbeitsbedarf)",
        "- Objekt 4 (Spindellagerschaden): EUR 21.200,00 (Reparaturkosten geschaetzt EUR 9.800,00 bereits abgezogen)",
        "- Objekt 8 (Softwarefehler, behebbar): EUR 29.800,00",
        "## Gesamtwert",
        "Gesamtmarktwert der zehn begutachteten Objekte: EUR 259.700,00 (Durchschnitt EUR 25.970,00 je Objekt, "
        "deutlich unter dem im Leasingvertrag kalkulierten Restwert von EUR 42.000,00 je Objekt).",
        "## Ursachenhinweis Softwarefehler",
        "Der Sachverstaendige stellt bei Objekten 3 und 8 identische Fehlermeldungen der Steuerungssoftware fest "
        "('Remote service status restricted'), die nach Herstellerauskunft auf eine serverseitige Lizenzsperre "
        "zurueckzufuehren sind und nicht auf einen mechanischen Mangel.",
    ],
)

# 14 Bewertungsvergleich
rows_vgl = [
    ["Objekt 1", "34.500", "42.000", "-7.500"],
    ["Objekt 2", "34.500", "42.000", "-7.500"],
    ["Objekt 3", "29.800", "42.000", "-12.200"],
    ["Objekt 4", "21.200", "42.000", "-20.800"],
    ["Objekt 5", "34.500", "42.000", "-7.500"],
    ["Objekt 6", "34.500", "42.000", "-7.500"],
    ["Objekt 7", "34.500", "42.000", "-7.500"],
    ["Objekt 8", "29.800", "42.000", "-12.200"],
    ["Objekt 9", "34.500", "42.000", "-7.500"],
    ["Objekt 10", "34.500", "42.000", "-7.500"],
]
make_xlsx(
    D / "14-bewertungsvergleich-marktpreis-buchwert.xlsx",
    "Bewertungsvergleich",
    ["Objekt", "Marktwert DEKRA (EUR)", "Kalkulierter Restwert (EUR)", "Differenz (EUR)"],
    rows_vgl,
    title="Bewertungsvergleich Marktpreis vs. kalkulierter Restwert (Objekte 1-10, ohne Objekte 11/12 Pilsen)",
)

# 15 Rueckholungsprotokoll real
make_docx(
    D / "15-rueckholungsprotokoll.docx",
    KOPF, "Rueckholungsprotokoll (Original, unterzeichnet)",
    [
        "Protokoll ueber die Rueckholung von zehn CNC-Bearbeitungszentren am Standort Bielefeld/Herford am 26./27.01.2026, "
        "erstellt durch Spedition Trescher Schwertransporte im Beisein von Sabine Krohn (NordLease) und "
        "Thorsten Wibbeling (Rotorwerk).",
        "## Ablauf",
        "26.01.2026, 07:30 bis 16:10 Uhr: Abbau und Verladung der Objekte 1, 2, 5, 6, 7 in Halle A/B Bielefeld.",
        "27.01.2026, 07:00 bis 13:45 Uhr: Abbau und Verladung der Objekte 3, 4, 8 (Bielefeld) sowie 9, 10 (Herford).",
        "Objekte 11 und 12 konnten am Standort Bielefeld/Herford nicht vorgefunden werden; laut Auskunft des Vorarbeiters "
        "Herrn Kevin Brandes befinden sich diese auf einer Baustelle in Pilsen, Tschechien.",
        "## Zustand bei Abbau (Kurzprotokoll)",
        "- Objekte 1, 2, 5, 6, 7, 9, 10: aeusserlich unauffaellig, Fotodokumentation angefertigt (siehe Anlage JPG)",
        "- Objekt 3: Fehlermeldung 'Remote service status restricted' im Display bestaetigt",
        "- Objekt 4: hoerbares Lagergeraeusch an der Spindel bei Testlauf",
        "- Objekt 8: Fehlermeldung 'Remote service status restricted' im Display bestaetigt",
        "## Unterschriften",
        "Fuer NordLease: Sabine Krohn, 27.01.2026. Fuer Rotorwerk (unter Vorbehalt der Feststellungen zu Objekt 4): "
        "Thorsten Wibbeling, 27.01.2026.",
    ],
)

# 16 Software-Lock-Bescheinigung Hersteller
make_docx(
    D / "16-software-lock-bescheinigung-hersteller.docx",
    "Haas Automation Europe N.V., Service Center Deutschland",
    "Bescheinigung ueber Softwaresperre (Remote Service Lock)",
    [
        "Bescheinigung vom 30.01.2026, ausgestellt von Haas Automation Europe N.V. auf Anfrage der NordLease "
        "Maschinen-Leasing GmbH.",
        "Hiermit bestaetigen wir, dass bei den Maschinen mit den Seriennummern HVF6-22093 und HVF6-22098 am 15.09.2025 "
        "auf Veranlassung der NordLease Maschinen-Leasing GmbH als Lizenznehmerin des zugehoerigen Softwarevertrags "
        "eine Fernsperre der erweiterten Diagnose- und Servicefunktionen ('Remote service status restricted') aktiviert wurde, "
        "nachdem Lizenzgebuehren fuer das dritte Quartal 2025 nicht beglichen worden waren.",
        "Die Grundfunktion der Maschinen (Fertigungsbetrieb) war hiervon nicht betroffen. Betroffen waren ausschliesslich "
        "Fernwartungs-, Diagnose- und Firmware-Update-Funktionen.",
        "Nach Zahlungseingang der ausstehenden Lizenzgebuehren durch die NordLease Maschinen-Leasing GmbH am 03.02.2026 "
        "wurde die Sperre am 04.02.2026 wieder aufgehoben.",
    ],
)

# 17 Kündigungsschreiben § 8 AGB
make_docx(
    D / "17-kuendigungsschreiben-leasinggeber-para-8-agb.docx",
    "NordLease Maschinen-Leasing GmbH, Herforder Str. 112, 33609 Bielefeld",
    "Fristlose Kuendigung des Leasingvertrags Nr. NL-2022-0847 gemaess § 8 AGB",
    [
        "An die Rotorwerk Praezisionstechnik GmbH, Gewerbepark Sennestadt 7, 33689 Bielefeld",
        "Bielefeld, den 12.01.2026",
        "Sehr geehrter Herr Wibbeling,",
        "hiermit kuendigen wir den Leasingvertrag Nr. NL-2022-0847 vom 24.02.2022 gemaess § 8 unserer "
        "Allgemeinen Geschaeftsbedingungen mit sofortiger Wirkung. Grund ist der Zahlungsverzug mit den "
        "Leasingraten fuer November und Dezember 2025 in Hoehe von insgesamt EUR 93.360,00 sowie der uns am "
        "09.01.2026 bekannt gewordene Insolvenzantrag Ihres Unternehmens beim Amtsgericht Bielefeld.",
        "Wir fordern Sie auf, saemtliche zwoelf Leasingobjekte binnen 5 Werktagen an unseren Standort "
        "Herforder Str. 112, 33609 Bielefeld, auf eigene Kosten zurueckzufuehren. Fuer die Objekte 11 und 12, "
        "deren Verbleib uns nicht bekannt ist, bitten wir um umgehende Standortmitteilung.",
        "Mit freundlichen Gruessen",
    ],
    "Sabine Krohn, Vertriebsleitung NordLease Maschinen-Leasing GmbH",
)

# 18 Aussonderungsantrag § 47 InsO
make_docx(
    D / "18-aussonderungsantrag-47-inso.docx",
    "Rechtsanwaelte Bohnert & Kollegen fuer NordLease Maschinen-Leasing GmbH",
    "Aussonderungsantrag gemaess § 47 InsO",
    [
        "An Herrn Rechtsanwalt Dr. Matthias Suender, vorlaeufiger Insolvenzverwalter ueber das Vermoegen der "
        "Rotorwerk Praezisionstechnik GmbH, Amtsgericht Bielefeld, Az. 43 IN 88/26",
        "Bielefeld, den 20.01.2026",
        "Sehr geehrter Herr Dr. Suender,",
        "namens und im Auftrag unserer Mandantin, der NordLease Maschinen-Leasing GmbH, machen wir hiermit "
        "das Aussonderungsrecht gemaess § 47 InsO an den zwoelf im Eigentum unserer Mandantin stehenden "
        "CNC-Bearbeitungszentren (Leasingvertrag Nr. NL-2022-0847) geltend.",
        "Der Leasingvertrag wurde bereits vor Insolvenzantragstellung wirksam gemaess § 8 AGB gekuendigt "
        "(Kuendigungsschreiben vom 12.01.2026). Wir bitten um Bestaetigung, dass die Objekte nicht der Masse "
        "zugerechnet werden, sowie um Mitteilung zum Verbleib der Objekte 11 und 12.",
        "Mit freundlichen Gruessen",
    ],
    "RA Bohnert",
)

# 19 IV-Antwort mit Verwertungsbefugnis
make_docx(
    D / "19-insolvenzverwalter-antwort-verwertungsbefugnis.docx",
    "Dr. Matthias Suender, vorlaeufiger Insolvenzverwalter",
    "Antwort auf Aussonderungsantrag - Hinweis auf Verwertungsbefugnis gemaess § 166 Abs. 1 InsO",
    [
        "An Rechtsanwaelte Bohnert & Kollegen",
        "Bielefeld, den 28.01.2026",
        "Sehr geehrte Kolleginnen und Kollegen,",
        "das Aussonderungsrecht Ihrer Mandantin an den zehn am Standort Bielefeld/Herford befindlichen Objekten "
        "wird dem Grunde nach nicht bestritten. Allerdings befinden sich diese Objekte im unmittelbaren Besitz "
        "der Schuldnerin, sodass ich als vorlaeufiger Insolvenzverwalter gemaess § 21 Abs. 2 Nr. 5 InsO i.V.m. "
        "§ 166 Abs. 1 InsO zur Verwertung beweglicher Sachen, an denen ein Absonderungs- bzw. aussonderungsaehnliches "
        "Recht besteht, berechtigt sein kann, sofern die Voraussetzungen vorliegen.",
        "Zu den Objekten 11 und 12 (Pilsen) kann ich derzeit keine Auskunft geben; die Geschaeftsfuehrung der "
        "Schuldnerin hat hierzu bislang keine Angaben gemacht.",
        "Ich bitte um kurzfristige Abstimmung des weiteren Vorgehens, insbesondere zur Kostentragung fuer "
        "Abbau und Ruecktransport.",
        "Mit freundlichen Gruessen",
    ],
    "Dr. Matthias Suender",
)

# 20 Sicherungsübereignungsklage Vorlage
make_docx(
    D / "20-sicherungsuebereignungsklage-vorlage.docx",
    "Rechtsanwaelte Bohnert & Kollegen",
    "Klageentwurf: Herausgabeklage aus Sicherungseigentum / vorsorgliche Feststellungsklage",
    [
        "Entwurf einer Klageschrift zum Landgericht Bielefeld gegen Rotorwerk CZ s.r.o. auf Herausgabe der "
        "Objekte 11 und 12, hilfsweise Feststellung, dass der NordLease Maschinen-Leasing GmbH das Eigentum "
        "an diesen Objekten zusteht.",
        "## Klageantrag (Entwurf)",
        "1. Die Beklagte wird verurteilt, die CNC-Bearbeitungszentren mit den Seriennummern HVF6-22101 und "
        "HVF6-22102 an die Klaegerin herauszugeben.",
        "2. Hilfsweise: Es wird festgestellt, dass das Eigentum an den vorgenannten Maschinen der Klaegerin zusteht.",
        "## Vorbemerkung des Sachbearbeiters",
        "Vor Klageerhebung ist zu pruefen, ob eine internationale Zustaendigkeit gegenueber der tschechischen "
        "Tochtergesellschaft gegeben ist und ob eine Vollstreckung in Tschechien ueberhaupt aussichtsreich waere. "
        "Alternative: Verhandlungsloesung ueber den Insolvenzverwalter, da Rotorwerk CZ s.r.o. wirtschaftlich mit "
        "der insolventen Muttergesellschaft verflochten ist.",
    ],
)

# 21 Verwertungsanzeige § 168 InsO
make_docx(
    D / "21-verwertungsanzeige-168-inso.docx",
    "Dr. Matthias Suender, Insolvenzverwalter",
    "Verwertungsanzeige gemaess § 168 InsO",
    [
        "An die NordLease Maschinen-Leasing GmbH, z. Hd. Sabine Krohn",
        "Bielefeld, den 10.02.2026",
        "Sehr geehrte Frau Krohn,",
        "hiermit zeige ich gemaess § 168 InsO an, dass ich beabsichtige, die zehn am Standort befindlichen "
        "CNC-Bearbeitungszentren im Wege des freihaendigen Verkaufs zu verwerten, nachdem eine einvernehmliche "
        "Rueckfuehrung an Ihre Mandantin aus betrieblichen Gruenden (laufende Auftraege der Schuldnerin) derzeit "
        "nicht moeglich erscheint. Sie erhalten Gelegenheit, binnen einer Woche eine guenstigere Verwertungsart "
        "zu benennen.",
        "Mit freundlichen Gruessen",
    ],
    "Dr. Matthias Suender",
)

# 22 Massekostenbeitrag § 170 f InsO Berechnung
rows_mk = [
    ["Feststellungspauschale (§ 171 Abs. 1 InsO)", "4 %", "10.388,00"],
    ["Verwertungskostenpauschale (§ 171 Abs. 2 InsO)", "5 %", "12.985,00"],
    ["Umsatzsteuer auf Verwertungserloes", "19 %", "49.334,30"],
    ["Verwertungserloes brutto (Zweitverkauf)", "-", "259.700,00"],
]
make_xlsx(
    D / "22-massekostenbeitrag-170f-inso-berechnung.xlsx",
    "Massekostenbeitrag",
    ["Position", "Satz", "Betrag (EUR)"],
    rows_mk,
    title="Berechnung Massekostenbeitrag gemaess §§ 170, 171 InsO",
)

# 23 Restwert-Gutachten unabhängig
make_docx(
    D / "23-restwert-gutachten-unabhaengig-zweitmeinung.docx",
    KOPF, "Unabhaengiges Zweitgutachten zum Restwert (Sachverstaendigenbuero Klawitter, Bielefeld)",
    [
        "Auf Wunsch der Rotorwerk Praezisionstechnik GmbH beauftragtes Zweitgutachten vom 12.02.2026, "
        "erstellt von Dipl.-Ing. Renate Klawitter zur Ueberpruefung des DEKRA-Gutachtens Nr. DEKRA-MB-2026-0334.",
        "## Ergebnis",
        "Die Gutachterin bestaetigt im Wesentlichen die Bandbreite des DEKRA-Gutachtens, haelt jedoch bei den "
        "Objekten 3 und 8 (Softwarefehler) einen um ca. EUR 3.000,00 je Objekt hoeheren Marktwert fuer vertretbar, "
        "da der Fehler nachweislich auf eine Lizenzsperre und nicht auf einen technischen Defekt zurueckzufuehren war "
        "und binnen Tagen reversibel ist. Korrigierter Gesamtwert: EUR 265.700,00 (Differenz EUR 6.000,00 gegenueber DEKRA).",
        "## Empfehlung",
        "Die Gutachterin empfiehlt, den Wertunterschied bei den Verwertungsverhandlungen mit einem Zweitkaeufer "
        "als Verhandlungsspielraum zu beruecksichtigen, nicht jedoch als bindende Untergrenze.",
    ],
)

# 24 Verkaufsverhandlung Zweitkäufer Angebot
make_eml(
    D / "24-angebot-zweitkaeufer-verkaufsverhandlung.eml",
    "einkauf@wester-praezisionstechnik.de",
    "m.suender@suender-insolvenzverwaltung.de",
    "Angebot Ankauf 10x Haas VF-6SS - Ihre Anfrage vom 11.02.2026",
    "Fri, 20 Feb 2026 10:05:00 +0100",
    "Sehr geehrter Herr Dr. Suender,\n\n"
    "vielen Dank fuer die Gelegenheit zur Angebotsabgabe. Nach Sichtung der Gutachten (DEKRA und Klawitter) "
    "sowie Besichtigung am 18.02.2026 bieten wir fuer das Gesamtpaket der zehn CNC-Bearbeitungszentren "
    "(Objekte 1, 2, 5, 6, 7, 9, 10 sowie 3, 4, 8 mit Abschlag) einen Kaufpreis von EUR 251.000,00 netto, "
    "Abholung und Demontage auf unsere Kosten binnen 3 Wochen nach Zuschlag.\n\n"
    "Mit freundlichen Gruessen\nDetlef Wester\nWester Praezisionstechnik GmbH, Guetersloh",
)

# 25 Kaufvertrag Verwertung
make_docx(
    D / "25-kaufvertrag-verwertung-zweitkaeufer.docx",
    "Insolvenzverwaltung Dr. Matthias Suender", "Kaufvertrag ueber zehn CNC-Bearbeitungszentren (Verwertung)",
    [
        "Kaufvertrag vom 27.02.2026 zwischen der Insolvenzmasse der Rotorwerk Praezisionstechnik GmbH, "
        "vertreten durch den Insolvenzverwalter Dr. Matthias Suender, und der Wester Praezisionstechnik GmbH, "
        "Carl-Bertelsmann-Str. 45, 33334 Guetersloh.",
        "## § 1 Kaufgegenstand",
        "Zehn CNC-Bearbeitungszentren Haas VF-6SS (Objekte 1-10 gemaess Objektliste vom 20.01.2026).",
        "## § 2 Kaufpreis",
        "EUR 258.000,00 netto (nach Nachverhandlung gegenueber dem Erstangebot von EUR 251.000,00, unter "
        "Beruecksichtigung des Zweitgutachtens Klawitter), zahlbar binnen 10 Tagen nach Uebergabe.",
        "## § 3 Uebergabe",
        "Die Uebergabe erfolgt am Lagerort der NordLease Maschinen-Leasing GmbH nach vorheriger Abstimmung "
        "des Abholtermins mit der Kaeuferin.",
        "Bielefeld, den 27.02.2026",
    ],
    "Dr. Matthias Suender, Insolvenzverwalter / Detlef Wester, Wester Praezisionstechnik GmbH",
)

# 26 Abrechnung Verwertungserlös
rows_abr = [
    ["Verwertungserloes (netto)", "258.000,00"],
    ["abzgl. Feststellungspauschale 4 %", "-10.320,00"],
    ["abzgl. Verwertungskostenpauschale 5 %", "-12.900,00"],
    ["Auszahlungsbetrag an NordLease", "234.780,00"],
]
make_csv(
    D / "26-abrechnung-verwertungserloes.csv",
    ["Position", "Betrag (EUR)"],
    rows_abr,
)

# 27 Nachforderung Leasingnehmer-Insolvenzmasse
make_docx(
    D / "27-nachforderung-leasingnehmer-insolvenzmasse.docx",
    "NordLease Maschinen-Leasing GmbH ./. Insolvenzmasse Rotorwerk Praezisionstechnik GmbH",
    "Forderungsanmeldung Nachforderung Restwertdifferenz zur Insolvenztabelle",
    [
        "Forderungsanmeldung vom 15.03.2026 zum Insolvenzverfahren Az. 43 IN 88/26 AG Bielefeld.",
        "## Berechnung der Nachforderung",
        "Kalkulierter Restwert (10 Objekte a EUR 42.000,00): EUR 420.000,00",
        "abzueglich ausgezahltem Verwertungserloes: EUR 234.780,00",
        "abzueglich offener Leasingraten Nov./Dez. 2025: bereits gesondert angemeldet (siehe Forderungstabelle)",
        "Nachforderung Restwertdifferenz zur Anmeldung: EUR 185.220,00",
        "## Zu den Objekten 11 und 12",
        "Fuer die in Pilsen verbliebenen Objekte 11 und 12 wird ein Schaden in Hoehe des vollen kalkulierten "
        "Restwerts von je EUR 42.000,00 (insgesamt EUR 84.000,00) gesondert zur Tabelle angemeldet, da eine "
        "Rueckfuehrung bislang nicht gelungen ist (siehe gesonderte Schadensersatzberechnung).",
    ],
)

# 28 Schadensersatzberechnung Restwert-Vertrag
rows_se = [
    ["Objekt 11 (HVF6-22101)", "Restwert entgangen", "42.000,00"],
    ["Objekt 12 (HVF6-22102)", "Restwert entgangen", "42.000,00"],
    ["Rueckhol-/Ermittlungskosten Tschechien", "Rechtsverfolgung", "8.450,00"],
    ["Summe Schadensersatz Objekte 11/12", "", "92.450,00"],
]
make_xlsx(
    D / "28-schadensersatzberechnung-restwert-vertrag.xlsx",
    "Schadensersatz",
    ["Position", "Art", "Betrag (EUR)"],
    rows_se,
    title="Schadensersatzberechnung Objekte 11 und 12 (Verbleib Pilsen ungeklaert)",
)

# 29 Emails Servicetechniker Vor-Ort-Zustand
make_eml(
    D / "29-email-servicetechniker-vor-ort-zustand.eml",
    "j.pahlke@haas-service.de",
    "s.krohn@nordlease-bielefeld.de",
    "Vor-Ort-Bericht Objekte 3 und 8 - Servicetermin 16.01.2026",
    "Fri, 16 Jan 2026 17:40:00 +0100",
    "Hallo Frau Krohn,\n\n"
    "wie besprochen war ich heute vor Ort bei Rotorwerk. Beide Maschinen (S/N HVF6-22093 und HVF6-22098) "
    "laufen mechanisch einwandfrei, die Fehlermeldung 'Remote service status restricted' kommt eindeutig "
    "von unserem Lizenzserver, nicht von der Maschine selbst. Sobald die offenen Lizenzgebuehren beglichen sind, "
    "ist die Sperre in wenigen Minuten aufhebbar. Bei Objekt 4 habe ich dagegen ein deutliches Lagergeraeusch "
    "an der Hauptspindel festgestellt, das ist ein echter mechanischer Befund und unabhaengig von der Softwarefrage.\n\n"
    "Viele Gruesse\nJoerg Pahlke\nHaas Automation Service",
)

print("Leasing/Rotorwerk: Kernstuecke 10-29 erzeugt.")
