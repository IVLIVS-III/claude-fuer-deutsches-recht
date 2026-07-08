#!/usr/bin/env python3
"""Ausbau Augsburg Vorsatzanfechtung Finanzamt auf 25 Aktenstuecke."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from aktenbau import make_docx, make_csv

SLUG = "insolvenzanfechtung-vorsatzanfechtung-finanzamt-ratenzahlung-augsburg"
D = Path("/home/user/workspace/legal-work/target/testakten") / SLUG

VERWALTER_KOPF = "Rechtsanwalt Dr. Simon Brettschneider - Insolvenzverwalter\nMaximilianstrasse 41, 86150 Augsburg"
FA_KOPF = "Finanzamt Augsburg-Stadt - Vollstreckungsstelle\nSchiessstaettenstrasse 44, 86161 Augsburg"
GERICHT_KOPF = "Landgericht Augsburg - 5. Zivilkammer\nAlpenstrasse 12, 86159 Augsburg"

make_docx(
    D / "16_klageschrift_freistaat_bayern_lg_augsburg.docx",
    VERWALTER_KOPF,
    "Klageschrift",
    [
        "Landgericht Augsburg",
        "5. Zivilkammer",
        "Alpenstrasse 12, 86159 Augsburg",
        "",
        "In dem Rechtsstreit",
        "Rechtsanwalt Dr. Simon Brettschneider, als Insolvenzverwalter ueber das Vermoegen der Lechtal Spedition und Logistik GmbH",
        "- Klaeger -",
        "gegen",
        "Freistaat Bayern, vertreten durch das Finanzamt Augsburg-Stadt, Schiessstaettenstrasse 44, 86161 Augsburg",
        "- Beklagter -",
        "",
        "wird Klage erhoben mit dem Antrag, den Beklagten zu verurteilen, an den Klaeger EUR 388.000,00 nebst Zinsen seit dem 09.07.2026 zu zahlen.",
        "## Begruendung",
        "Die 30 Ratenzahlungen und die Sicherungsabtretung von Frachtforderungen vom 09.09.2024 unterliegen der Anfechtung nach Paragraf 133 Abs. 1 InsO. Der Geschaeftsfuehrer handelte mit Benachteiligungsvorsatz, wie die eigene 13-Wochen-Liquiditaetsplanung und die E-Mail vom 03.03.2023 ('wir zahlen nur noch, wer am lautesten droht') belegen. Der Beklagte kannte den Vorsatz aufgrund der Vollstreckungshistorie, der beiden fruchtlosen Pfaendungsversuche, der Ruecklastschriften und des zweimaligen Sicherheitsverlangens; die Vermutung des Paragraf 133 Abs. 3 Satz 2 InsO greift nicht, weil die Kenntnis nicht allein auf der Ratenzahlungsbitte beruht.",
    ],
    "Dr. Simon Brettschneider\nRechtsanwalt, Insolvenzverwalter",
)

make_docx(
    D / "17_klageerwiderung_finanzamt_2026-09-10.docx",
    "Bayerisches Landesamt fuer Steuern - Prozessvertretung\nOstenstrasse 13, 85072 Eichstaett",
    "Klageerwiderung",
    [
        "An das Landgericht Augsburg - Az. 5 O 611/26",
        "",
        "Namens und im Auftrag des Beklagten wird beantragt, die Klage abzuweisen.",
        "## Begruendung",
        "Die Ratenzahlungen erfolgten kongruent aufgrund der Vereinbarung vom 24.10.2022 und waren aus Sicht der Finanzverwaltung Ausdruck eines ernsthaften Sanierungsbemuehens. Das Sicherheitsverlangen sei ueblich und keine ausreichende Grundlage fuer eine Vorsatzkenntnis; die Vermutungswirkung des Paragraf 133 Abs. 3 Satz 2 InsO sei zugunsten des Beklagten anzuwenden, da die Kenntnis allenfalls aus der Ratenbitte selbst hergeleitet werden koenne.",
        "Die Vollstreckungshistorie und die Ruecklastschriften seien fuer sich genommen nicht ausreichend, um eine hinreichend sichere Kenntnis des drohenden Benachteiligungsvorsatzes zu begruenden.",
    ],
    "Bayerisches Landesamt fuer Steuern",
)

make_docx(
    D / "18_replik_verwalter_2026-10-01.docx",
    VERWALTER_KOPF,
    "Replik",
    [
        "An das Landgericht Augsburg - Az. 5 O 611/26",
        "",
        "1. Die Vermutungswirkung des Paragraf 133 Abs. 3 Satz 2 InsO betrifft nur den Fall, dass sich die Kenntnis allein aus der Ratenzahlungsbitte ergibt. Hier liegen mit zwei fruchtlosen Pfaendungsversuchen, mehreren Ruecklastschriften und zweimaligem Sicherheitsverlangen erheblich weitergehende Umstaende vor.",
        "2. Das Sicherheitsverlangen selbst indiziert, dass die Finanzverwaltung die Zahlungsfaehigkeit der Schuldnerin bereits erheblich in Zweifel zog.",
        "3. Es wird Zeugenbeweis durch den zustaendigen Sachbearbeiter Herrn Ruckdeschel zu den internen Erwaegungen bei Bewilligung des zweiten und dritten Aufschubs angeboten.",
    ],
    "Dr. Simon Brettschneider\nRechtsanwalt, Insolvenzverwalter",
)

make_docx(
    D / "19_duplik_finanzamt_2026-10-20.docx",
    "Bayerisches Landesamt fuer Steuern - Prozessvertretung\nOstenstrasse 13, 85072 Eichstaett",
    "Duplik",
    [
        "An das Landgericht Augsburg - Az. 5 O 611/26",
        "",
        "Der Beklagte haelt an seiner Rechtsauffassung fest, erklaert sich aber mit der angebotenen Zeugenvernehmung einverstanden. Ergaenzend wird die Einholung eines Sachverstaendigengutachtens zum Eintritt der Zahlungsunfaehigkeit beantragt, da die eigenen 13-Wochen-Planungen der Schuldnerin methodisch zu hinterfragen seien.",
    ],
    "Bayerisches Landesamt fuer Steuern",
)

make_docx(
    D / "20_beweisbeschluss_lg_augsburg_2026-11-05.docx",
    GERICHT_KOPF,
    "Beweisbeschluss",
    [
        "Az. 5 O 611/26",
        "",
        "In dem Rechtsstreit Dr. Brettschneider ./. Freistaat Bayern wird beschlossen:",
        "1. Es wird Beweis erhoben durch Vernehmung des Zeugen Herrn Ruckdeschel (Vollstreckungsstelle) zu den internen Erwaegungen bei Bewilligung des zweiten und dritten Vollstreckungsaufschubs.",
        "2. Es wird Beweis erhoben durch Einholung eines schriftlichen Sachverstaendigengutachtens zum Eintritt der Zahlungsunfaehigkeit anhand der BWA-Quartalsreihe und der 13-Wochen-Planungen.",
        "3. Zum Sachverstaendigen wird bestellt: Dipl.-Kfm. Reinhard Osswald, oeffentlich bestellter Sachverstaendiger fuer Unternehmensbewertung, Augsburg.",
        "Augsburg, 05.11.2026",
    ],
    "Vorsitzender Richter am Landgericht Dr. Anton Wiedemann",
)

make_docx(
    D / "21_sachverstaendigengutachten_osswald_zahlungsunfaehigkeit.docx",
    "Dipl.-Kfm. Reinhard Osswald\nOeffentlich bestellter Sachverstaendiger, Augsburg",
    "Schriftliches Sachverstaendigengutachten",
    [
        "Gutachten zum Zeitpunkt des Eintritts der Zahlungsunfaehigkeit der Lechtal Spedition und Logistik GmbH, erstattet im Auftrag des Landgerichts Augsburg, Az. 5 O 611/26.",
        "1. Grundlage: BWA-Quartalsreihe 2022 bis 2025 (Aktenstueck 08), 13-Wochen-Planungen (Aktenstuecke 09 und 10), Zahlungsliste Finanzamt (Aktenstueck 07).",
        "2. Befund: Die eigene 13-Wochen-Planung vom 19.09.2022 weist bereits eine Unterdeckung von 19 Prozent am Planungshorizont aus; die BWA-Quartalsreihe zeigt seit dem dritten Quartal 2022 durchgehend faellige, nicht bediente Verbindlichkeiten oberhalb der Bagatellgrenze.",
        "3. Ergebnis: Die Zahlungsunfaehigkeit ist methodisch nachvollziehbar spaetestens im August/September 2022 eingetreten; die Datierung im Eigenantrag auf Anfang 2026 ist nicht haltbar.",
        "Augsburg, 20.01.2027",
    ],
    "Dipl.-Kfm. Reinhard Osswald",
)

make_docx(
    D / "22_zeugenvernehmungsprotokoll_ruckdeschel.docx",
    GERICHT_KOPF,
    "Protokoll der Zeugenvernehmung",
    [
        "Termin vom 20.01.2027, Az. 5 O 611/26",
        "Zeuge: Herr Ruckdeschel, Vollstreckungsstelle Finanzamt Augsburg-Stadt",
        "",
        "Der Zeuge gibt an: 'Wir haben den dritten Aufschub nur gegen Sicherheit bewilligt, weil wir nach den Ruecklastschriften intern erhebliche Zweifel an der dauerhaften Zahlungsfaehigkeit der Schuldnerin hatten. Das war aktenkundig in unserem Vollstreckungsvermerk vermerkt.'",
        "Protokollfuehrerin: Justizangestellte K. Brummer",
    ],
    "Vorsitzender Richter am Landgericht Dr. Anton Wiedemann",
)

make_docx(
    D / "23_urteil_lg_augsburg_2027-03-10.docx",
    GERICHT_KOPF,
    "Urteil",
    [
        "Az. 5 O 611/26",
        "",
        "Im Namen des Volkes ergeht folgendes Urteil:",
        "Der Beklagte wird verurteilt, an den Klaeger EUR 338.000,00 nebst Zinsen zu zahlen. Im Uebrigen wird die Klage abgewiesen.",
        "## Entscheidungsgruende (Auszug)",
        "Das Gericht ist nach dem Ergebnis der Beweisaufnahme davon ueberzeugt, dass der Beklagte aufgrund der Vollstreckungshistorie, der Ruecklastschriften und des internen Vollstreckungsvermerks Kenntnis vom Benachteiligungsvorsatz hatte, soweit es die letzten 26 Raten und die Sicherungsabtretung betrifft. Fuer die ersten vier Raten nach Abschluss der Ratenzahlungsvereinbarung fehlt es an hinreichenden Kenntnisindizien; insoweit war die Klage abzuweisen.",
        "Die Kosten werden im Verhaeltnis 87 (Beklagter) zu 13 (Klaeger) verteilt.",
        "Augsburg, 10.03.2027",
    ],
    "Vorsitzender Richter am Landgericht Dr. Anton Wiedemann",
)

make_docx(
    D / "24_kostenfestsetzungsbeschluss_2027-04-14.docx",
    GERICHT_KOPF,
    "Kostenfestsetzungsbeschluss",
    [
        "Az. 5 O 611/26",
        "",
        "Die vom Beklagten an den Klaeger zu erstattenden Kosten werden auf EUR 18.940,20 festgesetzt.",
        "Augsburg, 14.04.2027",
    ],
    "Rechtspflegerin Birgit Hafner",
)

make_docx(
    D / "25_schlussvermerk_verwalter_vollstreckung.docx",
    VERWALTER_KOPF,
    "Schlussvermerk",
    [
        "Der Freistaat Bayern hat gegen das Urteil vom 10.03.2027 keine Berufung eingelegt; das Urteil ist seit dem 12.04.2027 rechtskraeftig.",
        "Die Urteilssumme von EUR 338.000,00 nebst Zinsen sowie die festgesetzten Kosten von EUR 18.940,20 sind am 28.04.2027 vollstaendig auf dem Massekonto eingegangen.",
        "Der Anfechtungskomplex Finanzamt Augsburg-Stadt ist damit abgeschlossen; die Akte wird zur Schlussrechnungslegung vorgemerkt.",
    ],
    "Dr. Simon Brettschneider\nRechtsanwalt, Insolvenzverwalter",
)

make_csv(
    D / "csv" / "fristenliste_verjaehrung_paragraf_146_inso.csv",
    ["Anspruch", "Kenntnis Verwalter ab", "Verjaehrung (3 Jahre)", "Status"],
    [
        ["Anfechtung Ratenzahlungen 5 bis 30", "08.06.2026", "31.12.2029", "gewahrt, Klage erhoben 09.07.2026"],
        ["Anfechtung Sicherungsabtretung", "08.06.2026", "31.12.2029", "gewahrt, im selben Verfahren geltend gemacht"],
    ],
)
make_csv(
    D / "csv" / "urteilssumme_zahlungseingang.csv",
    ["Position", "Betrag (EUR)", "Datum"],
    [
        ["Urteilssumme", "338.000,00", "28.04.2027"],
        ["Kostenerstattung", "18.940,20", "28.04.2027"],
        ["Gesamtsumme Zahlungseingang", "356.940,20", "28.04.2027"],
    ],
)

print("Augsburg Kernstuecke 16-25 sowie csv/ erzeugt.")
