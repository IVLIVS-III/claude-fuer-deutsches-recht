#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Erzeugt Aktenstuecke 18-25 fuer die Fuerth-Akte (Klageverfahren)."""
import sys
sys.path.insert(0, "/home/user/workspace/legal-work/target/scripts/_tmp_gen")
from aktenbau import make_docx, TESTAKTEN

BASE = TESTAKTEN / "insolvenzanfechtung-inkongruente-deckung-zwangsvollstreckung-fuerth"

KOPF_VERWALTER = "Dr. Cornelius Wehrfritz, Rechtsanwalt und Insolvenzverwalter | Ludwig-Erhard-Anlage 4, 90761 Nuernberg"
KOPF_GEGNER = "Rechtsanwaeltin Dr. Sabine Ottmann | Koenigstrasse 21, 90402 Nuernberg"
KOPF_GERICHT = "Landgericht Nuernberg-Fuerth, 4. Zivilkammer"

# 18 Klageschrift
make_docx(
    BASE / "18_klageschrift_lg_nuernberg-fuerth_2026-09-14.docx",
    KOPF_VERWALTER,
    "Klageschrift",
    [
        "An das Landgericht Nuernberg-Fuerth, 4. Zivilkammer",
        "",
        "In dem Rechtsstreit",
        "Dr. Cornelius Wehrfritz als Insolvenzverwalter ueber das Vermoegen der Frankenletter Druck- und Medien GmbH, Waldstrasse 41, 90763 Fuerth",
        "- Klaeger -",
        "gegen",
        "Karow Verpackungswerk GmbH, vertreten durch den Geschaeftsfuehrer Herbert Karow, Industriestrasse 12, 91126 Schwabach",
        "- Beklagte -",
        "",
        "wegen Insolvenzanfechtung (Streitwert: 41.750,00 EUR)",
        "",
        "erhebe ich namens und in Vollmacht des Klaegers Klage und werde beantragen:",
        "1. Die Beklagte wird verurteilt, an den Klaeger 41.750,00 EUR nebst Zinsen in Hoehe von fuenf Prozentpunkten ueber dem Basiszinssatz seit Rechtshaengigkeit zu zahlen.",
        "2. Die Beklagte traegt die Kosten des Rechtsstreits.",
        "## Sachverhalt",
        "Die Schuldnerin hat der Beklagten im letzten Monat vor dem am 12.03.2026 gestellten Eigenantrag insgesamt 41.750,00 EUR zukommen lassen: eine Barzahlung von 9.750,00 EUR an der Warenrampe am 18.02.2026, den Erloes einer Kassenpfaendung von 12.000,00 EUR am 25.02.2026 sowie eine Ueberweisung von 20.000,00 EUR am 04.03.2026, die ausweislich des Verwendungszwecks zur Abwendung angekuendigter weiterer Vollstreckungsmassnahmen geleistet wurde.",
        "Der Klaeger stuetzt die Anfechtung in erster Linie auf § 131 Abs. 1 Nr. 1 InsO. Alle drei Rechtshandlungen liegen innerhalb des letzten Monats vor dem Eroeffnungsantrag. Auf eine Kenntnis der Beklagten von einer Zahlungsunfaehigkeit oder Glaeubigerbenachteiligungsabsicht kommt es fuer diesen Tatbestand nicht an.",
        "## Rechtliche Wuerdigung",
        "Die durch Zwangsvollstreckung erlangte Befriedigung (Barzahlung an der Rampe und Kassenpfaendung) ist eine inkongruente Deckung im Sinne des § 131 Abs. 1 Nr. 1 InsO, da die Beklagte sie nicht in dieser Art zu beanspruchen hatte. Auch die Ueberweisung vom 04.03.2026 ist inkongruent, da sie unter dem unmittelbaren Druck einer angekuendigten weiteren Vollstreckung erfolgte und damit keine freiwillige Erfuellungshandlung darstellt.",
        "Hilfsweise wird die Anfechtung auf § 130 Abs. 1 Nr. 1 InsO sowie § 131 Abs. 1 Nr. 2 und 3 InsO gestuetzt, da die Beklagte aufgrund der Mahnstufen, der Ruecklastschrift und des internen Kreditvermerks vom 17.11.2025 Kenntnis von der drohenden Zahlungsunfaehigkeit der Schuldnerin hatte.",
        "Es wird Klageerhebung beantragt.",
    ],
    unterschrift="Dr. Cornelius Wehrfritz, Rechtsanwalt und Insolvenzverwalter",
)

# 19 Klageerwiderung
make_docx(
    BASE / "19_klageerwiderung_ottmann_2026-10-26.docx",
    KOPF_GEGNER,
    "Klageerwiderung",
    [
        "In dem Rechtsstreit Dr. Cornelius Wehrfritz ./. Karow Verpackungswerk GmbH",
        "4 O 812/26 - Landgericht Nuernberg-Fuerth",
        "",
        "beantrage ich fuer die Beklagte, die Klage abzuweisen.",
        "## Begruendung",
        "Die Beklagte bestreitet nicht den Zahlungseingang der drei Betraege in der geltend gemachten Hoehe. Sie bestreitet jedoch, dass es sich bei der Ueberweisung vom 04.03.2026 um eine inkongruente Deckung handelt. Die Zahlung sei freiwillig und in Erfuellung der bereits titulierten Forderung aus dem Vollstreckungsbescheid des Amtsgerichts Coburg erfolgt.",
        "Ferner wird bestritten, dass die Beklagte von einer Krise der Schuldnerin gewusst habe. Die Mahnstufen seien branchenueblich und liessen keinen Rueckschluss auf eine Zahlungsunfaehigkeit zu. Der interne Kreditvermerk vom 17.11.2025 sei eine routinemaessige Bonitaetseinschaetzung ohne Aussagekraft fuer eine tatsaechliche Kenntnis der gesetzlichen Vermutungstatbestaende.",
        "Die Beklagte weist zudem darauf hin, dass der Eigenantrag der Schuldnerin den Eintritt der Zahlungsunfaehigkeit selbst erst auf Anfang Maerz 2026 datiert. Es sei widerspruechlich, wenn der Klaeger nunmehr einen frueheren Zeitpunkt behaupte.",
        "## Zu den einzelnen Zahlungen",
        "Die Barzahlung an der Warenrampe und der Erloes aus der Kassenpfaendung werden als Ergebnisse rechtmaessiger Zwangsvollstreckungsmassnahmen bezeichnet, denen sich die Beklagte nicht habe entziehen koennen und muessen. Die Beklagte habe im Zeitpunkt der Vollstreckung keinerlei besondere Kenntnis gehabt, die ueber das hinausgehe, was jeder Glaeubiger bei ausstehenden Forderungen wisse.",
        "Aus diesen Gruenden wird beantragt, die Klage vollumfaenglich abzuweisen.",
    ],
    unterschrift="Dr. Sabine Ottmann, Rechtsanwaeltin",
)

# 20 Replik
make_docx(
    BASE / "20_replik_wehrfritz_2026-11-16.docx",
    KOPF_VERWALTER,
    "Replik",
    [
        "In dem Rechtsstreit Dr. Cornelius Wehrfritz ./. Karow Verpackungswerk GmbH",
        "4 O 812/26 - Landgericht Nuernberg-Fuerth",
        "",
        "erwidere ich auf die Klageerwiderung vom 26.10.2026 wie folgt:",
        "## Zum Tatbestand des § 131 Abs. 1 Nr. 1 InsO",
        "Fuer die Barzahlung an der Warenrampe sowie die Kassenpfaendung kommt es entgegen der Auffassung der Beklagten nicht auf deren Kenntnis an. § 131 Abs. 1 Nr. 1 InsO erfasst jede im letzten Monat vor dem Eroeffnungsantrag durch oder wegen einer Zwangsvollstreckung erlangte Deckung unabhaengig von einer Kenntnis oder gar Zahlungsunfaehigkeit. Der Vortrag der Beklagten zur fehlenden Kenntnis geht insoweit ins Leere.",
        "## Zur Ueberweisung vom 04.03.2026",
        "Die von der Beklagten behauptete Freiwilligkeit der Ueberweisung wird durch die als Anlage K7 vorgelegte Zahlungsaufforderung des Gerichtsvollziehers Heckel vom 02.03.2026 sowie die interne E-Mail des Geschaeftsfuehrers Pflugbeil vom 03.03.2026 widerlegt, in der es woertlich heisst: 'sonst stehen die am 11.03. wieder auf dem Hof'. Die Zahlung erfolgte damit erkennbar zur Abwendung einer unmittelbar bevorstehenden weiteren Vollstreckungsmassnahme und ist mithin ebenfalls inkongruent.",
        "## Zur Insolvenzreife",
        "Die vom Klaeger vorgelegte Bankspiegel- und BWA-Reihe belegt eine seit dem 01.02.2025 durchgehende Liquiditaetsluecke von deutlich ueber zehn Prozent der faelligen Verbindlichkeiten ueber einen Zeitraum von weit mehr als drei Wochen. Der im Eigenantrag genannte Zeitpunkt Anfang Maerz 2026 ist mit den eigenen Unterlagen der Schuldnerin nicht in Einklang zu bringen und beruht ersichtlich auf einer zu spaeten Selbsteinschaetzung der Geschaeftsfuehrung, nicht auf der tatsaechlichen Vermoegenslage.",
        "Fuer die Hilfstatbestaende der §§ 130, 131 Abs. 1 Nr. 2 und 3 InsO wird an der bereits vorgetragenen Kenntnis der Beklagten festgehalten und ergaenzend auf den internen Kreditvermerk vom 17.11.2025 verwiesen, in dem die Debitorenbuchhaltung der Beklagten die Bonitaet der Schuldnerin ausdruecklich als 'kritisch, Zahlungsverhalten deutlich verschlechtert' einstuft.",
    ],
    unterschrift="Dr. Cornelius Wehrfritz, Rechtsanwalt und Insolvenzverwalter",
)

# 21 Duplik
make_docx(
    BASE / "21_duplik_ottmann_2026-12-07.docx",
    KOPF_GEGNER,
    "Duplik",
    [
        "In dem Rechtsstreit Dr. Cornelius Wehrfritz ./. Karow Verpackungswerk GmbH",
        "4 O 812/26 - Landgericht Nuernberg-Fuerth",
        "",
        "nehme ich zur Replik vom 16.11.2026 wie folgt Stellung:",
        "Die Beklagte raeumt nunmehr ein, dass es fuer die Barzahlung und die Kassenpfaendung tatbestandlich nicht auf ihre Kenntnis ankommt, halt jedoch daran fest, dass diese beiden Vorgaenge unabhaengig von der rechtlichen Einordnung wirtschaftlich notwendig gewesen seien, um die eigene Forderung durchzusetzen, und dass eine Rueckgewaehr die Beklagte unbillig treffe.",
        "Zur Ueberweisung vom 04.03.2026 wird bestritten, dass die zitierte interne E-Mail des Geschaeftsfuehrers Pflugbeil der Beklagten in irgendeiner Form bekannt gewesen sei oder ihr zugerechnet werden koenne. Die Beklagte habe die Zahlung als regulaeren Zahlungseingang gebucht.",
        "Der interne Kreditvermerk vom 17.11.2025 wird als unternehmensinterne Risikoeinschaetzung bezeichnet, die keine Aussage ueber eine drohende oder eingetretene Zahlungsunfaehigkeit im Rechtssinne treffe, sondern lediglich das allgemein vorsichtige Kreditmanagement der Beklagten dokumentiere.",
        "An dem Klageabweisungsantrag wird festgehalten.",
    ],
    unterschrift="Dr. Sabine Ottmann, Rechtsanwaeltin",
)

# 22 Beweisbeschluss
make_docx(
    BASE / "22_beweisbeschluss_lg_nuernberg-fuerth_2026-12-21.docx",
    KOPF_GERICHT,
    "Beweisbeschluss",
    [
        "4 O 812/26",
        "",
        "In dem Rechtsstreit Dr. Cornelius Wehrfritz ./. Karow Verpackungswerk GmbH",
        "",
        "beschliesst das Gericht:",
        "1. Es wird Beweis erhoben durch Vernehmung des Zeugen Herbert Karow, Geschaeftsfuehrer der Beklagten, zu der Behauptung, die Ueberweisung vom 04.03.2026 sei ohne Kenntnis der internen E-Mail vom 03.03.2026 als freiwillige Zahlung veranlasst worden.",
        "2. Es wird ferner Beweis erhoben durch Einholung eines schriftlichen Sachverstaendigengutachtens zu der Behauptung des Klaegers, die Frankenletter Druck- und Medien GmbH sei bereits seit Februar 2025 zahlungsunfaehig gewesen.",
        "3. Zum Sachverstaendigen wird bestellt: Dipl.-Kfm. Rainer Fessenmayer, Nuernberg.",
        "4. Termin zur Zeugenvernehmung wird bestimmt auf den 18.02.2027, 10:00 Uhr.",
    ],
)

# 23 Sachverstaendigengutachten
make_docx(
    BASE / "23_sachverstaendigengutachten_fessenmayer_2027-04-30.docx",
    "Dipl.-Kfm. Rainer Fessenmayer, oeffentlich bestellter und vereidigter Sachverstaendiger | Fuerther Strasse 244, 90429 Nuernberg",
    "Sachverstaendigengutachten zur Zahlungsunfaehigkeit der Frankenletter Druck- und Medien GmbH",
    [
        "Gutachten im Auftrag des Landgerichts Nuernberg-Fuerth, Az. 4 O 812/26",
        "## Auftrag",
        "Zu begutachten war, ob die Frankenletter Druck- und Medien GmbH bereits im Februar 2025 zahlungsunfaehig im Sinne des § 17 InsO war.",
        "## Grundlagen",
        "Ausgewertet wurden die monatliche BWA-Reihe Januar 2025 bis Februar 2026 (Anlage K3), der Bankspiegel mit taeglicher Liquiditaetslage fuer denselben Zeitraum (Anlage K4) sowie die Faelligkeitsuebersichten der Kreditoren.",
        "## Feststellungen",
        "Die Liquiditaetsluecke der Schuldnerin betrug zum Stichtag 01.02.2025 rund 17 Prozent der faelligen Verbindlichkeiten und stieg bis zum 01.03.2026 kontinuierlich auf ueber 38 Prozent an. Die Unterdeckung bestand ohne Unterbrechung ueber den gesamten Betrachtungszeitraum von mehr als 13 Monaten, mithin weit ueber die vom Bundesgerichtshof geforderte Drei-Wochen-Frist hinaus.",
        "## Ergebnis",
        "Die Frankenletter Druck- und Medien GmbH war nach den vorgelegten Unterlagen bereits am 01.02.2025 zahlungsunfaehig im Sinne des § 17 Abs. 2 InsO. Der im Eigenantrag genannte Zeitpunkt Anfang Maerz 2026 ist mit den betriebswirtschaftlichen Unterlagen nicht vereinbar.",
    ],
    unterschrift="Dipl.-Kfm. Rainer Fessenmayer",
)

# 24 Urteil
make_docx(
    BASE / "24_urteil_lg_nuernberg-fuerth_2027-07-09.docx",
    KOPF_GERICHT,
    "Urteil",
    [
        "4 O 812/26",
        "",
        "IM NAMEN DES VOLKES",
        "",
        "In dem Rechtsstreit Dr. Cornelius Wehrfritz als Insolvenzverwalter ./. Karow Verpackungswerk GmbH",
        "",
        "hat das Landgericht Nuernberg-Fuerth, 4. Zivilkammer, fuer Recht erkannt:",
        "1. Die Beklagte wird verurteilt, an den Klaeger 41.750,00 EUR nebst Zinsen in Hoehe von fuenf Prozentpunkten ueber dem Basiszinssatz seit dem 15.09.2026 zu zahlen.",
        "2. Die Beklagte traegt die Kosten des Rechtsstreits.",
        "3. Das Urteil ist vorlaeufig vollstreckbar.",
        "## Tatbestand",
        "Der Klaeger macht als Insolvenzverwalter Rueckgewaehranspruche wegen dreier im letzten Monat vor dem Eigenantrag erlangter Zahlungen in Hoehe von insgesamt 41.750,00 EUR geltend.",
        "## Entscheidungsgruende",
        "Die Klage ist begruendet. Die Barzahlung an der Warenrampe vom 18.02.2026 und der Erloes der Kassenpfaendung vom 25.02.2026 sind inkongruente Deckungen im Sinne des § 131 Abs. 1 Nr. 1 InsO, da sie durch Zwangsvollstreckung erlangt wurden. Auf eine Kenntnis der Beklagten kommt es fuer diesen Tatbestand nicht an; der entsprechende Einwand der Beklagten geht ins Leere.",
        "Auch die Ueberweisung vom 04.03.2026 ist inkongruent. Die Vernehmung des Zeugen Karow hat nicht zur Ueberzeugung des Gerichts ergeben, dass die Zahlung ohne Kenntnis der Drucksituation erfolgte; die als Anlage K7 vorgelegte Zahlungsaufforderung des Gerichtsvollziehers mit Terminbestimmung auf den 11.03.2026 sowie der Verwendungszweck 'zur Abwendung der Vollstreckung' sprechen eine eindeutige Sprache. Die Kammer wertet die Zahlung als unter dem Druck unmittelbar bevorstehender Zwangsvollstreckung geleistet und damit als inkongruent im Sinne des § 131 Abs. 1 Nr. 1 InsO.",
        "Das eingeholte Sachverstaendigengutachten des Sachverstaendigen Fessenmayer hat zur vollen Ueberzeugung der Kammer ergeben, dass die Schuldnerin bereits seit dem 01.02.2025 zahlungsunfaehig war. Die Kammer folgt den nachvollziehbaren und in sich schluessigen Feststellungen des Gutachtens vollumfaenglich.",
        "Der Rueckgewaehranspruch folgt aus § 143 Abs. 1 InsO. Die zurueckgewaehrte Forderung lebt gemaess § 144 Abs. 1 InsO wieder auf. Fuer die Kassenpfaendung greift ergaenzend die Rueckschlagsperre des § 88 InsO.",
        "Die Kostenentscheidung beruht auf § 91 ZPO, die Entscheidung zur vorlaeufigen Vollstreckbarkeit auf § 709 ZPO.",
    ],
)

# 25 Schlussvermerk
make_docx(
    BASE / "25_schlussvermerk_wehrfritz_2027-09-20.docx",
    KOPF_VERWALTER,
    "Schlussvermerk zum Anfechtungsprozess Karow Verpackungswerk GmbH",
    [
        "Az. 4 O 812/26 (LG Nuernberg-Fuerth); IN 145/26 (AG Fuerth)",
        "## Verfahrensstand",
        "Das Urteil vom 09.07.2027 ist seit dem 12.08.2027 rechtskraeftig. Die Beklagte hat auf Zahlungsaufforderung vom 16.08.2027 den titulierten Betrag von 41.750,00 EUR nebst Zinsen in Hoehe von 3.180,45 EUR, insgesamt 44.930,45 EUR, am 15.09.2027 vollstaendig auf das Massekonto ueberwiesen.",
        "## Zusammenfassung",
        "Die Anfechtung nach § 131 Abs. 1 Nr. 1 InsO wurde in vollem Umfang bestaetigt. Massgeblich war insbesondere, dass der Tatbestand keine Kenntnis der Beklagten voraussetzt und dass die Ueberweisung vom 04.03.2026 durch die interne E-Mail des Geschaeftsfuehrers Pflugbeil sowie die Zahlungsaufforderung des Gerichtsvollziehers zweifelsfrei als Druckzahlung belegt werden konnte. Das Sachverstaendigengutachten hat die Insolvenzreife bereits ab Februar 2025 zusaetzlich abgesichert.",
        "Die vereinnahmten 44.930,45 EUR werden der Masse zugefuehrt. Der Vorgang gilt als abgeschlossen.",
    ],
    unterschrift="Dr. Cornelius Wehrfritz, Rechtsanwalt und Insolvenzverwalter",
)

print("Fuerth 18-25 erzeugt")
