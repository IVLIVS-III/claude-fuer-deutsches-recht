#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Erzeugt eml-Dateien fuer emails/ und eml/ Ordner der Erlangen-Akte."""
from pathlib import Path

ROOT = Path("/home/user/workspace/legal-work/target/testakten/statusfeststellung-gmbh-geschaeftsfuehrer-minderheit-erlangen")

def write_eml(path, frm, to, date, subject, body):
    content = f"""From: {frm}
To: {to}
Date: {date}
Subject: {subject}
Content-Type: text/plain; charset=utf-8

{body}
"""
    path.write_text(content, encoding="utf-8")
    print("geschrieben:", path)


write_eml(
    ROOT / "emails" / "2025-09-03_seidl_an_vogt_satzung.eml",
    "miriam.seidl@example.invalid",
    "henrik.vogt@neuralis.example.invalid",
    "Wed, 03 Sep 2025 07:55:00 +0200",
    "Re: Satzungsaenderung gestern",
    (
        "Hallo Henrik,\n\n"
        "ich habe gestern zugestimmt, aber ich bin nicht sicher, ob die enge Fassung "
        "uns im DRV-Verfahren wirklich hilft. Wenn die Sperrminoritaet nur das Ressort "
        "Entwicklung betrifft, sieht das fuer Aussenstehende schnell nach einer "
        "Feigenblattregelung aus. Bitte sprich das nochmal mit Fabian Rehbogen durch, "
        "bevor die Kanzlei das im Widerspruch verwendet.\n\n"
        "Viele Gruesse\nMiriam"
    ),
)

write_eml(
    ROOT / "emails" / "2025-09-03_vogt_an_seidl_antwort.eml",
    "henrik.vogt@neuralis.example.invalid",
    "miriam.seidl@example.invalid",
    "Wed, 03 Sep 2025 08:40:00 +0200",
    "Re: Re: Satzungsaenderung gestern",
    (
        "Hallo Miriam,\n\n"
        "ich sehe das Risiko auch, aber mehr war bei Torben gestern nicht drin. "
        "Er hat klar gesagt, der Fonds gibt keine Kontrolle ueber Finanzierungsrunden "
        "oder Abberufung ab. Ich nehme lieber die enge Fassung als gar nichts. "
        "Fabian sagt, wir koennen naechstes Jahr nachverhandeln, wenn die Studie "
        "gut laeuft.\n\n"
        "Gruss\nHenrik"
    ),
)

write_eml(
    ROOT / "emails" / "2026-05-13_aldenhoven_an_beirat_abberufung.eml",
    "t.aldenhoven@frankenhealth-ventures.example.invalid",
    "beirat@neuralis.example.invalid",
    "Wed, 13 May 2026 16:02:00 +0200",
    "Abberufungsbeschluss zugestellt",
    (
        "Liebe Beiratskollegen,\n\n"
        "der Beschluss vom 12.05. ist Henrik heute zugegangen. Ich rechne mit "
        "Widerstand, insbesondere weil der Werkvertrag mit dem externen Entwickler "
        "aus meiner Sicht klar unter die Beiratszustimmung nach Ziffer 7.3.2 faellt "
        "und nicht unter seine 50000-Euro-Grenze aus dem Anstellungsvertrag. Bitte "
        "haltet die Blackout-Kommunikation ein, bis die Anwaelte sich abgestimmt "
        "haben.\n\n"
        "Torben"
    ),
)

write_eml(
    ROOT / "eml" / "2026-03-11_rehbogen_an_drv_eingangsbestaetigung.eml",
    "rehbogen@kanzlei-rehbogen.example.invalid",
    "clearingstelle@drv-bund.example.invalid",
    "Wed, 11 Mar 2026 11:20:00 +0100",
    "Eingangsbestaetigung erbeten, Az. SV-2023-771402-VOGT",
    (
        "Sehr geehrte Damen und Herren,\n\n"
        "anbei die Nachbesserung unseres Widerspruchs vom 10.03.2026. Wir bitten "
        "um kurze Eingangsbestaetigung sowie um Mitteilung, ob ein Erlaeuterungstermin "
        "zur Sperrminoritaet moeglich ist, bevor ueber den Widerspruch entschieden wird.\n\n"
        "Mit freundlichen Gruessen\nDr. Fabian Rehbogen"
    ),
)

write_eml(
    ROOT / "eml" / "2026-09-16_holzapfel_an_rehbogen_vergleich.eml",
    "b.holzapfel@drv-bund.example.invalid",
    "rehbogen@kanzlei-rehbogen.example.invalid",
    "Wed, 16 Sep 2026 09:44:00 +0200",
    "Re: Vergleichsvorschlag Az. S 5 R 214/26",
    (
        "Sehr geehrter Herr Dr. Rehbogen,\n\n"
        "wir koennen der zeitlichen Aufteilung grundsaetzlich naehertreten, halten "
        "den Stichtag 19.09.2025 fuer sachgerecht, da an diesem Tag die Sperrminoritaet "
        "notariell wirksam wurde. Zur Frage der Saeumniszuschlaege muessten wir "
        "aber auf dem Zugang der Anhoerung als Stichtag bestehen, nicht auf einem "
        "frueheren Zeitpunkt.\n\n"
        "Mit freundlichen Gruessen\nBettina Holzapfel"
    ),
)

print("fertig")
