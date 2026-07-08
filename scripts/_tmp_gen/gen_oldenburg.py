#!/usr/bin/env python3
"""Erzeugt Aktenstuecke 17-25 fuer insolvenzanfechtung-schenkung-familie-oldenburg."""
import sys
sys.path.insert(0, "/home/user/workspace/legal-work/target/scripts/_tmp_gen")
from aktenbau import make_docx, TESTAKTEN

D = TESTAKTEN / "insolvenzanfechtung-schenkung-familie-oldenburg"
KOPF = "Feddersen & Osterloh Rechtsanwaelte | Insolvenzverwalter | Oldenburg"
KOPF_GEGEN = "Dr. Bruns & Kollegen | Rechtsanwaelte und Notare | Oldenburg"

# 17 - Klageschrift (gegen alle drei, getrennte Antraege)
make_docx(
    D / "17_klageschrift_lg_oldenburg_2026-08-18.docx",
    KOPF,
    "Klageschrift — LG Oldenburg",
    [
        "Landgericht Oldenburg",
        "Klaeger: Dr. Jasper Feddersen als Insolvenzverwalter ueber das Vermoegen der "
        "Hollmann Bau- und Sanierungs GmbH",
        "Beklagte: 1. Karin Hollmann, 2. Lena Hollmann, 3. Uwe Tietjen",
        "## Antraege",
        "1. Die Beklagte zu 1 wird verurteilt, an den Klaeger 29.300,00 EUR nebst Zinsen zu zahlen "
        "(27.900,00 EUR fuer den BMW X3 sowie 800,00 EUR Geburtstagszahlung, hilfsweise nur "
        "27.900,00 EUR, aeusserst hilfsweise nur 800,00 EUR).",
        "2. Die Beklagte zu 2 wird verurteilt, an den Klaeger 30.000,00 EUR nebst Zinsen zu zahlen "
        "(fuenf Ueberweisungen zu je 6.000,00 EUR innerhalb der Vierjahresfrist).",
        "3. Der Beklagte zu 3 wird verurteilt, an den Klaeger 19.800,00 EUR nebst Zinsen zu zahlen.",
        "## Begruendung",
        "Saemtliche Zuwendungen erfolgten unentgeltlich im Sinne des Paragraf 134 Abs. 1 InsO. "
        "Bei der Tochter Lena Hollmann liegt die erste Ueberweisung vom 08.01.2022 ausserhalb der "
        "am 10.03.2022 beginnenden Vierjahresfrist und wird daher nicht geltend gemacht; die "
        "verbleibenden fuenf Tranchen zu je 6.000,00 EUR (zusammen 30.000,00 EUR) sind fristgerecht.",
    ],
    "Dr. Jasper Feddersen, Rechtsanwalt",
)

# 18 - Klageerwiderung
make_docx(
    D / "18_klageerwiderung_bruns_2026-09-29.docx",
    KOPF_GEGEN,
    "Klageerwiderung",
    [
        "Landgericht Oldenburg, Az. 5 O 612/26",
        "in Sachen Dr. Feddersen ./. Hollmann u.a.",
        "## Antrag",
        "Die Klage wird abgewiesen.",
        "## Begruendung",
        "Die Uebertragung des BMW X3 sei durch die langjaehrige, wenn auch unentgeltliche "
        "Buchhaltungsmitarbeit der Beklagten zu 1 ausgeglichen gewesen; jedenfalls falle die "
        "Geburtstagszahlung von 800,00 EUR unter das Gelegenheitsgeschenkprivileg des Paragraf 134 "
        "Abs. 2 InsO. Die Beklagte zu 2 habe von der Krise der Schuldnerin keine Kenntnis gehabt. "
        "Der Beklagte zu 3 sei nicht passivlegitimiert, da die Zahlung unmittelbar an die "
        "Dachdeckerei geflossen sei und diese eine werthaltige Gegenleistung erbracht habe; zudem "
        "habe der Beklagte zu 3 Geruest- und Transporthilfe fuer die Schuldnerin geleistet, die als "
        "Gegenleistung zu beruecksichtigen sei.",
    ],
    "Dr. Heiner Bruns, Rechtsanwalt und Notar",
)

# 19 - Replik
make_docx(
    D / "19_replik_verwalter_2026-10-20.docx",
    KOPF,
    "Replik zur Klageerwiderung",
    [
        "Landgericht Oldenburg, Az. 5 O 612/26",
        "## Erwiderung",
        "Die Kenntnis der Empfaenger ist fuer den Anfechtungstatbestand des Paragraf 134 InsO ohne "
        "Bedeutung; die entsprechende Argumentation der Beklagten zu 2 geht ins Leere. Fuer die "
        "Uebertragung des Pkw existiert weder ein schriftlicher Arbeitsvertrag noch eine "
        "Lohnjournal-Eintragung fuer die Beklagte zu 1; eine nachtraegliche Anerkennung freiwilliger "
        "Mitarbeit stellt keine ausgleichende Gegenleistung dar. Richtiger Anfechtungsgegner fuer die "
        "Dachdeckerrechnung ist der Beklagte zu 3, da er durch die Drittzahlung von seiner "
        "Werklohnschuld befreit wurde (Paragraf 267 BGB); die behauptete Geruesthilfe ist weder "
        "belegt noch vor der Zahlung vereinbart worden.",
    ],
    "Dr. Jasper Feddersen, Rechtsanwalt",
)

# 20 - Duplik
make_docx(
    D / "20_duplik_bruns_2026-11-10.docx",
    KOPF_GEGEN,
    "Duplik",
    [
        "Landgericht Oldenburg, Az. 5 O 612/26",
        "## Erwiderung auf die Replik",
        "Die Beklagten beantragen vorsorglich, ueber den Umfang der Mitarbeit der Beklagten zu 1 "
        "sowie ueber die behauptete Geruest- und Transporthilfe des Beklagten zu 3 Beweis durch "
        "Vernehmung von Zeugen zu erheben.",
    ],
    "Dr. Heiner Bruns, Rechtsanwalt und Notar",
)

# 21 - Beweisbeschluss
make_docx(
    D / "21_beweisbeschluss_lg_oldenburg_2026-12-01.docx",
    "Landgericht Oldenburg",
    "Beweisbeschluss",
    [
        "Az. 5 O 612/26",
        "## Beschluss",
        "Es wird Beweis erhoben ueber den Umfang der Mitarbeit der Beklagten zu 1 in der "
        "Buchhaltung der Schuldnerin sowie ueber die behauptete Geruest- und Transporthilfe des "
        "Beklagten zu 3 durch Vernehmung des Zeugen Hartmut Wienken (Steuerberater der Schuldnerin).",
    ],
    "Die Vorsitzende Richterin am Landgericht",
)

# 22 - Zeugenvernehmungsprotokoll
make_docx(
    D / "22_zeugenvernehmungsprotokoll_wienken_2027-02-16.docx",
    "Landgericht Oldenburg",
    "Protokoll der Zeugenvernehmung — Hartmut Wienken",
    [
        "Az. 5 O 612/26, Termin vom 16.02.2027",
        "## Aussage des Zeugen",
        "Der Zeuge Hartmut Wienken, Steuerberater der Schuldnerin, sagt aus, dass die Beklagte zu 1 "
        "nach seiner Kenntnis allenfalls gelegentlich Ablagearbeiten im Buero der Schuldnerin "
        "erledigt habe; eine regelmaessige oder vertraglich vereinbarte Buchhaltungstaetigkeit sei "
        "ihm nicht bekannt. Zur behaupteten Geruest- und Transporthilfe des Beklagten zu 3 koenne er "
        "keine Angaben machen, da dies nicht Gegenstand der Buchhaltung gewesen sei.",
    ],
    "Die Protokollfuehrerin",
)

# 23 - Urteil
make_docx(
    D / "23_urteil_lg_oldenburg_2027-05-11.docx",
    "Landgericht Oldenburg",
    "Urteil",
    [
        "Az. 5 O 612/26",
        "verkuendet am 11.05.2027",
        "## Tenor",
        "1. Die Beklagte zu 1 wird verurteilt, an den Klaeger 27.900,00 EUR nebst Zinsen zu zahlen. "
        "Im Uebrigen (Geburtstagszahlung 800,00 EUR) wird die Klage abgewiesen.",
        "2. Die Beklagte zu 2 wird verurteilt, an den Klaeger 30.000,00 EUR nebst Zinsen zu zahlen.",
        "3. Der Beklagte zu 3 wird verurteilt, an den Klaeger 19.800,00 EUR nebst Zinsen zu zahlen.",
        "4. Die Kosten werden verhaeltnismaessig geteilt.",
        "## Entscheidungsgruende",
        "Die Uebertragung des BMW X3 erfolgte unentgeltlich, da nach dem Ergebnis der "
        "Beweisaufnahme keine vertraglich geschuldete, wertentsprechende Gegenleistung der "
        "Beklagten zu 1 feststellbar ist; gelegentliche Ablagearbeiten reichen hierfuer nicht aus. "
        "Die Geburtstagszahlung von 800,00 EUR faellt demgegenueber unter das Gelegenheitsgeschenk-"
        "privileg des Paragraf 134 Abs. 2 InsO und ist nicht anfechtbar. Die Kenntnis-Argumentation "
        "der Beklagten zu 2 ist fuer Paragraf 134 InsO unerheblich; die fuenf innerhalb der "
        "Vierjahresfrist liegenden Ueberweisungen sind in voller Hoehe zurueckzugewaehren. Der "
        "Beklagte zu 3 ist als Empfaenger der Zuwendung passivlegitimiert, da er durch die "
        "Drittzahlung von seiner Werklohnschuld befreit wurde; eine Gegenleistung ist nicht bewiesen.",
    ],
    "Die Vorsitzende Richterin am Landgericht",
)

# 24 - Kostenfestsetzungsbeschluss
make_docx(
    D / "24_kostenfestsetzungsbeschluss_2027-07-02.docx",
    "Landgericht Oldenburg",
    "Kostenfestsetzungsbeschluss",
    [
        "Az. 5 O 612/26",
        "Beschluss vom 02.07.2027",
        "## Tenor",
        "Die zu erstattenden Kosten werden entsprechend dem Obsiegen und Unterliegen wie folgt "
        "festgesetzt: Beklagte zu 1 hat 3.240,00 EUR, Beklagte zu 2 hat 4.180,00 EUR und Beklagter "
        "zu 3 hat 3.560,00 EUR an den Klaeger zu erstatten.",
    ],
    "Der Rechtspfleger",
)

# 25 - Schlussvermerk
make_docx(
    D / "25_schlussvermerk_verwalter_2027-09-08.docx",
    KOPF,
    "Schlussvermerk zur Handakte",
    [
        "Insolvenzverfahren Hollmann Bau- und Sanierungs GmbH, Az. 60 IN 87/26",
        "Vermerk vom 08.09.2027",
        "## Zusammenfassung",
        "Das Urteil des Landgerichts Oldenburg vom 11.05.2027 (Az. 5 O 612/26) ist seit dem "
        "15.06.2027 rechtskraeftig. Alle drei Beklagten haben die titulierten Betraege "
        "(27.900,00 EUR, 30.000,00 EUR und 19.800,00 EUR, zusammen 77.700,00 EUR) nebst Zinsen und "
        "Kosten bis zum 31.08.2027 vollstaendig an die Masse gezahlt.",
        "## Bewertung",
        "Der Fall bestaetigt, dass die Kenntnis des Zuwendungsempfaengers fuer Paragraf 134 InsO "
        "unerheblich ist, dass die Vierjahresfrist streng nach dem Zeitpunkt der jeweiligen "
        "Einzelzuwendung zu berechnen ist und dass eine Drittzahlung zur Befreiung von einer fremden "
        "Verbindlichkeit den Schuldner der befreiten Verbindlichkeit und nicht den Zahlungsempfaenger "
        "zum tauglichen Anfechtungsgegner macht.",
    ],
    "Dr. Jasper Feddersen, Insolvenzverwalter",
)

print("Oldenburg 17-25 erzeugt.")
