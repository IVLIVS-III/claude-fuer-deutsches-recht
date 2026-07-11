#!/usr/bin/env python3
"""Verhindert das Wiederauftauchen konkret berichtigter Rechtsstandsfehler."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class Sentinel:
    label: str
    pattern: re.Pattern[str]


SENTINELS = (
    Sentinel(
        "alte Kleinunternehmergrenzen 22.000/50.000 Euro",
        re.compile(
            r"(?:UStG|Kleinunternehmer(?:regelung)?).{0,180}"
            r"22[.]000.{0,180}50[.]000",
            re.IGNORECASE | re.DOTALL,
        ),
    ),
    Sentinel(
        "falsche Zehnjahresfrist bei vorsätzlich vorenthaltenen Beiträgen",
        re.compile(
            r"(?:SGB\s*IV|Paragraf\s*28p|§\s*28p).{0,180}"
            r"(?:10|zehn)\s+Jahre\s+bei\s+Vorsatz",
            re.IGNORECASE | re.DOTALL,
        ),
    ),
    Sentinel(
        "rechtsformabhängiger Ausschluss der Kleinunternehmerregelung",
        re.compile(
            r"(?:GmbH|UG|AG).{0,120}"
            r"(?:immer\s+Regelbesteuerung|kein\s+Kleinunternehmer|"
            r"Kleinunternehmer.{0,30}(?:unzulässig|nicht\s+möglich))",
            re.IGNORECASE | re.DOTALL,
        ),
    ),
    Sentinel(
        "nicht amtlich verifizierter Entscheidungsanker 10 O 306/25",
        re.compile(r"\b10\s+O\s+306/25\b"),
    ),
    Sentinel(
        "Gesetze nicht zugeordnete Arbeitsrechts-Normenformel",
        re.compile(
            r"Paragrafen\s+611a,\s*Paragrafen\s+1,\s*"
            r"Paragrafen\s+14"
        ),
    ),
    Sentinel(
        "fachfremder Universal-Normenradar im Arbeitsrecht",
        re.compile(
            r"Normenradar:\*\*\s+BGB\s+Paragrafen\s+611a,\s*613a,\s*"
            r"615,\s*623;\s*KSchG\s+Paragrafen\s+1,\s*4,\s*7;\s*"
            r"TzBfG\s+Paragrafen\s+14,\s*15,\s*16"
        ),
    ),
    Sentinel(
        "falsches Datum zum BFH-Anker IX R 28/14",
        re.compile(
            r"(?:16[.]05[.]2015.{0,100}IX\s+R\s+28/14|"
            r"IX\s+R\s+28/14.{0,100}16[.]05[.]2015)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "falsches Datum zum EuGH-Anker C-307/22",
        re.compile(
            r"(?:07[.]11[.]2023.{0,100}C-307/22|"
            r"C-307/22.{0,100}07[.]11[.]2023)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "veralteter und fachfremder AGB-Sammelanker",
        re.compile(
            r"AGBG\s*\(alt\).{0,120}C-26/13.{0,80}C-186/16",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "fachfremder Statusrecht-Sammelanker",
        re.compile(
            r"B\s+12\s+BA\s+3/23\s+R.{0,220}"
            r"B\s+12\s+BA\s+9/22\s+R.{0,220}"
            r"B\s+12\s+KR\s+37/19\s+R",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "fachfremder Insolvenzrecht-Sammelanker",
        re.compile(
            r"IX\s+ZR\s+211/02.{0,260}"
            r"(?:Paragraf|§)\s*343\s+InsO.{0,100}Chapter-15",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "fachfremder Gesellschaftsrecht-Sammelanker",
        re.compile(
            r"II\s+ZR\s+91/21.{0,260}II\s+ZB\s+11/24.{0,260}"
            r"II\s+ZR\s+166/05",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "fachfremder Mietrecht-Sammelanker",
        re.compile(
            r"VIII\s+ZR\s+93/15.{0,260}VIII\s+ZR\s+66/20.{0,260}"
            r"V\s+ZR\s+128/23",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "fachfremder Steuerrecht-Sammelanker",
        re.compile(
            r"BMF-Schreiben\s+vom\s+15[.]10[.]2025.{0,260}"
            r"Forschungszulage.{0,260}Mindeststeuer",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "materielle Überdehnung der VARTA-Nichtannahmeentscheidung",
        re.compile(
            r"1\s+BvR\s+418/25.{0,260}"
            r"(?:bestätigt|grundsätzliche\s+Verfassungsmäßigkeit|"
            r"verfassungsrechtlich\s+(?:grundsätzlich\s+)?zulässig|"
            r"Tragfähigkeit\s+des\s+StaRUG)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "falsch bezeichnete Schneidmesser-Entscheidung",
        re.compile(
            r"X\s+ZR\s+95/05.{0,80}Schneidmesser|"
            r"Schneidmesser.{0,80}X\s+ZR\s+95/05",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "falsch zugeordneter Rechtsbestandsanker X ZR 173/02",
        re.compile(
            r"X\s+ZR\s+173/02.{0,180}"
            r"Rechtsbestand.{0,100}glaubhaft",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "nicht existentes HOAI-Leistungsbild Flachbau",
        re.compile(r"HOAI.{0,160}Flachbau", re.IGNORECASE),
    ),
    Sentinel(
        "falsche Gesetzesabkürzung für Beitragsbemessungsgrenze",
        re.compile(r"BBG\s*\(Beitragsbemessung\)", re.IGNORECASE),
    ),
    Sentinel(
        "vertauschte SGG-Normen für Klage und Eilrechtsschutz",
        re.compile(
            r"(?:Klagefrist.{0,60}(?:§|Paragraf)?\s*84\s+SGG|"
            r"Eil(?:antrag|rechtsschutz).{0,60}(?:§|Paragraf)?\s*87\s+SGG)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "vertauschter Gläubigerantrag und Antragspflicht in der InsO",
        re.compile(
            r"(?:Paragraf|§)\s*14\s+InsO.{0,100}Antragspflicht"
            r".{0,160}(?:Paragraf|§)\s*15a.{0,80}Gläubigerantrag",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "falsche Schutzdauer-Norm im Gebrauchsmusterrecht",
        re.compile(
            r"(?:Paragraf|§)\s*(?:11|13)(?:\s+GebrMG)?.{0,80}"
            r"Schutzdauer",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "pauschale Patentgesetz-Analogie für Gebrauchsmusteransprüche",
        re.compile(
            r"(?:PatG\s+(?:Paragrafen|§§)\s*14,\s*21,\s*24,\s*139,\s*"
            r"140a,\s*140b\s+analog|(?:Paragrafen|§§)\s*139\s*ff[.]?\s*"
            r"PatG.{0,80}(?:analog|Gebrauchsmuster))",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "Werkstattrisiko-Entscheidung fälschlich der fiktiven Abrechnung zugeordnet",
        re.compile(
            r"(?:VI\s+ZR\s+239/22.{0,120}fiktiv|"
            r"fiktiv.{0,120}VI\s+ZR\s+239/22)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "XII ZB 415/25 auf einen pauschalen Vertretungshinweis verkürzt",
        re.compile(
            r"XII\s+ZB\s+415/25.{0,220}"
            r"Vertretung\s+und\s+Verfahrensbefugnis.{0,120}"
            r"vor\s+jedem\s+Antrag",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "scheinpräzises Musteraktenzeichen X ZR 123/45",
        re.compile(r"\bX\s+ZR\s+123/45\b"),
    ),
    Sentinel(
        "fehlerhafte Dollar-Schreibweise für Paragraf 22 AGG",
        re.compile(r"\$\s*22\s+AGG"),
    ),
    Sentinel(
        "falsche Lüth-Fundstelle und fachfremder Universalanker",
        re.compile(r"BVerfGE\s+Band\s+6\s+Rn\s+32", re.IGNORECASE),
    ),
    Sentinel(
        "falsch bezeichnete BHO-Norm zur Wirtschaftlichkeit",
        re.compile(
            r"(?:Paragraf|§)\s*6\s+BHO.{0,80}"
            r"Wirtschaftlichkeit(?:,\s*Sparsamkeit)?",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "falsch bezeichnete BHO-Norm zur BRH-Prüfung",
        re.compile(
            r"(?:Paragraf|§)\s*109\s+BHO.{0,80}"
            r"Prüfung\s+durch\s+(?:den\s+)?BRH",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "falsch bezeichnete Vorleistungen als Vorbehaltsklauseln",
        re.compile(
            r"(?:Paragrafen|§§)\s*55,?\s*56\s+BHO.{0,100}"
            r"Vorbehaltsklauseln",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "II ZR 296/05 fälschlich als Drei-Wochen-Liquiditätsanker",
        re.compile(
            r"II\s+ZR\s+296/05.{0,180}(?:Drei-Wochen|Liquiditätsstockung|"
            r"Zahlungsunfähigkeit)|(?:Drei-Wochen|Liquiditätsstockung).{0,180}"
            r"II\s+ZR\s+296/05",
            re.IGNORECASE | re.DOTALL,
        ),
    ),
    Sentinel(
        "nicht verifizierter Patentanwaltsanker 4 Ni 18/26",
        re.compile(r"4\s+Ni\s+18/26\s*\(Patent-Nichtigkeit\s+Standard\)", re.IGNORECASE),
    ),
    Sentinel(
        "nicht verifizierter Patentanwaltsanker 1 BvR 2616/17",
        re.compile(r"\b1\s+BvR\s+2616/17\b"),
    ),
    Sentinel(
        "VII ZR 46/06 fälschlich als HOAI-Mindestsatzanker",
        re.compile(
            r"VII\s+ZR\s+46/06.{0,120}Mindestsatz|"
            r"Mindestsatz.{0,120}VII\s+ZR\s+46/06",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "VII ZR 63/14 fälschlich als Architekten-Abschlagsanker",
        re.compile(
            r"VII\s+ZR\s+63/14.{0,140}(?:Abschlagszahlung|Tunnel)|"
            r"(?:Abschlagszahlung|Tunnel).{0,140}VII\s+ZR\s+63/14",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "VII ZR 58/11 fälschlich als Akquise- oder Mischgutanker",
        re.compile(
            r"VII\s+ZR\s+58/11.{0,140}(?:Akquise|Mischgut)|"
            r"(?:Akquise|Mischgut).{0,140}VII\s+ZR\s+58/11",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "nicht verifizierter Berufsgerichtsanker StbSt R 2/21",
        re.compile(r"\bStbSt\s+R\s+2/21\b", re.IGNORECASE),
    ),
    Sentinel(
        "BFH II R 33/19 fälschlich der Vertretungsbefugnis zugeordnet",
        re.compile(
            r"II\s+R\s+33/19.{0,100}Vertretungsbefugnis|"
            r"Vertretungsbefugnis.{0,100}II\s+R\s+33/19",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "EuGH C-606/19 fälschlich dem Abschlussprüferrecht zugeordnet",
        re.compile(
            r"C-606/19.{0,120}(?:Abschlussprüfer|Wirtschaftsprüfer|Unabhängigkeit)|"
            r"(?:Abschlussprüfer|Wirtschaftsprüfer).{0,120}C-606/19",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "BGH II ZR 217/03 fälschlich dem Bestätigungsvermerk zugeordnet",
        re.compile(
            r"II\s+ZR\s+217/03.{0,120}(?:Bestätigungsvermerk|Abschlussprüfer)|"
            r"(?:Bestätigungsvermerk|Abschlussprüfer).{0,120}II\s+ZR\s+217/03",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "KZR 12/15 fälschlich als AGB-Indizanker",
        re.compile(
            r"KZR\s+12/15.{0,140}(?:AGB|Indizwirkung|Paragraf\s+307)|"
            r"(?:AGB|Indizwirkung).{0,140}KZR\s+12/15",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "I ZB 75/16 fälschlich als ordre-public-Anker",
        re.compile(
            r"I\s+ZB\s+75/16.{0,100}ordre\s+public|"
            r"ordre\s+public.{0,100}I\s+ZB\s+75/16",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "IX ZR 119/14 fälschlich der geltungserhaltenden Reduktion zugeordnet",
        re.compile(
            r"IX\s+ZR\s+119/14.{0,180}(?:geltungserhaltend|Fremdrecht)|"
            r"(?:geltungserhaltend|Fremdrecht).{0,180}IX\s+ZR\s+119/14",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "II ZR 234/09 fälschlich als Beschlussmängel- oder Untersuchungsanker",
        re.compile(
            r"II\s+ZR\s+234/09.{0,220}(?:Beschlussmängel|Siemens|Neubürger)|"
            r"(?:Beschlussmängel|Siemens|Neubürger).{0,220}II\s+ZR\s+234/09",
            re.IGNORECASE | re.DOTALL,
        ),
    ),
    Sentinel(
        "XI ZR 121/21 fälschlich als Verwahrentgeltanker",
        re.compile(
            r"XI\s+ZR\s+121/21.{0,120}Verwahrentgelt|"
            r"Verwahrentgelt.{0,120}XI\s+ZR\s+121/21",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "VIII ZR 96/13 fälschlich der AGB-Kollision zugeordnet",
        re.compile(
            r"VIII\s+ZR\s+96/13.{0,120}(?:AGB-Kollision|battle\s+of\s+forms)|"
            r"(?:AGB-Kollision|battle\s+of\s+forms).{0,120}VIII\s+ZR\s+96/13",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "nicht verifizierter Arbeitsrechtsanker 9 AZR 134/16",
        re.compile(r"\b9\s+AZR\s+134/16\b", re.IGNORECASE),
    ),
    Sentinel(
        "nicht verifizierter Patentrechtsanker X ZR 89/18",
        re.compile(r"\bX\s+ZR\s+89/18\b", re.IGNORECASE),
    ),
    Sentinel(
        "VIII ZR 13/19 fälschlich als Cookie-Anker",
        re.compile(
            r"VIII\s+ZR\s+13/19.{0,100}Cookie|"
            r"Cookie.{0,100}VIII\s+ZR\s+13/19",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "EuGH C-92/11 fälschlich als Schulz/Egbringhoff bezeichnet",
        re.compile(r"C-92/11\s*\([^)]*Schulz", re.IGNORECASE),
    ),
    Sentinel(
        "veralteter HGB-Anker Paragraf 319a ohne Altstandskennzeichnung",
        re.compile(r"(?:§|Paragraf)\s*319a\s+HGB(?!\s*(?:a[.]?F[.]?|alt))", re.IGNORECASE),
    ),
    Sentinel(
        "WPO Paragraf 51 fälschlich als Verschwiegenheitsnorm",
        re.compile(
            r"(?:§|Paragraf)\s*51\s+WPO.{0,100}Verschwiegenheit|"
            r"Verschwiegenheit.{0,100}(?:§|Paragraf)\s*51\s+WPO",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "VVG Paragraf 43 fälschlich als Wissenszurechnungsnorm",
        re.compile(
            r"(?:§|Paragraf)\s*43\s+VVG.{0,120}(?:Wissenszurechnung|Vertreterwissen)|"
            r"(?:Wissenszurechnung|Vertreterwissen).{0,120}(?:§|Paragraf)\s*43\s+VVG",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "UmwG Paragraf 16 fälschlich als Norm der Registerwirkung",
        re.compile(
            r"(?:§|Paragraf)\s*16\s+UmwG.{0,100}(?:Registerwirkung|Wirkung\s+der\s+Eintragung)|"
            r"(?:Registerwirkung|Wirkung\s+der\s+Eintragung).{0,100}(?:§|Paragraf)\s*16\s+UmwG",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "BSIG Paragraf 8a fälschlich als ausdrückliche Space-Weather-Pflicht",
        re.compile(
            r"(?:§|Paragraf)\s*8a\s+BSIG.{0,180}"
            r"(?:verlangt|fordert|schreibt).{0,80}Space\s+Weather",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "Zahlungsunfähigkeit fälschlich allein aus Insolvenzantrag vermutet",
        re.compile(
            r"Zahlungsunfähigkeit.{0,100}(?:wird\s+)?vermutet\s+ab.{0,80}"
            r"(?:Insolvenzantrag|Antragstellung)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "erfundene Dreiwochen-Amtsfrist des vorläufigen Insolvenzverwalters",
        re.compile(
            r"(?:3|drei)\s+Wochen\s+ab\s+Bestellung.{0,120}"
            r"vorläufig(?:e|er|en)\s+Insolvenzverwalter",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "pauschale Sechswochenfrist für Forderungsanmeldung",
        re.compile(
            r"(?:6|sechs)\s+Wochen\s+ab\s+Eröffnung.{0,120}"
            r"Forderungsanmeldung",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "veraltete Zehnjahresfrist für besonders schwere Steuerhinterziehung",
        re.compile(
            r"(?:10|zehn)\s+Jahre.{0,160}(?:schwere|besonders\s+schwere)\s+"
            r"Steuerhinterziehung",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "verkürzter Verjährungsbeginn nach Paragraf 146 InsO",
        re.compile(
            r"(?:§|Paragraf)\s*146\s+InsO.{0,100}"
            r"(?:ab\s+(?:Verwalter-?)?Kenntnis|drei\s+Jahre\s+häufig\s+vergessen)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "Paragraf 138 InsO fälschlich als pauschale Kenntnisvermutung im AnfG",
        re.compile(
            r"(?:§|Paragraf)\s*138\s+InsO.{0,80}analog.{0,80}"
            r"(?:Kenntnisvermutung|Vermutungsregel)|"
            r"(?:Kenntnisvermutung|Vermutungsregel).{0,80}analog.{0,80}"
            r"(?:§|Paragraf)\s*138\s+InsO",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "widersprüchliche Rangrücktrittsfolge bei sonstigem freien Vermögen",
        re.compile(
            r"sonstig(?:es|em)\s+frei(?:es|en)\s+Vermögen.{0,240}"
            r"Passivierungsverbot\s+nach\s+(?:§|Paragraf)\s*5\s+Absatz\s+2a",
            re.IGNORECASE | re.DOTALL,
        ),
    ),
    Sentinel(
        "Passivierungsverbot fälschlich ohne möglichen Wegfallgewinn",
        re.compile(
            r"Passivierungsverbot.{0,160}(?:kein|ohne)\s+(?:sofortigen\s+)?"
            r"Sanierungsertrag",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "verschobene GebrMG-Normenkette oder abgesenkte Erfindungshöhe",
        re.compile(
            r"(?:(?:§|Paragraf)\s*4\s+GebrMG.{0,80}erfinderischer\s+Schritt|"
            r"(?:§|Paragraf)\s*17\s+GebrMG.{0,80}(?:Umwandlung|Abzweigung)|"
            r"(?:§|Paragraf)\s*24\s+GebrMG.{0,80}Löschungsgr|"
            r"erfinderischer\s+Schritt.{0,80}(?:niedriger|geringer)\s+"
            r"(?:als|gegenüber).{0,40}Patent)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "4 StR 247/16 fälschlich als allgemeiner Beweiswürdigungsanker",
        re.compile(
            r"4\s+StR\s+247/16.{0,160}(?:Beweisw.rdig|L.cken|Widerspr.che)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "5 StR 566/18 fälschlich der Strafzumessung zugeordnet",
        re.compile(
            r"5\s+StR\s+566/18.{0,160}(?:Strafzumessung|schuldangemessen)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "2 BvR 669/04 fälschlich als abstrakter Verhältnismäßigkeitsanker",
        re.compile(
            r"2\s+BvR\s+669/04.{0,220}(?:legitimen?\s+Zweck|Geeignetheit|Erforderlichkeit)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "X ZB 4/10 fälschlich als allgemeiner Primärrechtsschutzanker",
        re.compile(
            r"X\s+ZB\s+4/10.{0,180}(?:effektiv(?:en|er)\s+Prim.rrechtsschutz|vor\s+Zuschlag)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "VII ZR 37/12 fälschlich als IT-Projektanker",
        re.compile(
            r"VII\s+ZR\s+37/12.{0,180}(?:IT-Projekt|Leistungsbeschreibung|Abnahmepr.fung)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "VII ZR 262/11 fälschlich als Abnahmefähigkeitsanker",
        re.compile(
            r"VII\s+ZR\s+262/11.{0,180}(?:Abnahmef.hig|Werklohn.{0,50}Abnahme)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "VII ZR 19/12 fälschlich als allgemeiner Abnahmeanker",
        re.compile(
            r"VII\s+ZR\s+19/12.{0,180}(?:Abnahmereife|F.lligkeit\s+und\s+M.ngelrechte)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "VII ZR 220/14 fälschlich als Nachtragsanker",
        re.compile(
            r"VII\s+ZR\s+220/14.{0,180}(?:Nachtr.ge|Abgrenzung\s+vom\s+Vertragssoll)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "heutiger BauGB Paragraf 124 fälschlich als Erschließungsvertrag bezeichnet",
        re.compile(
            r"BauGB\s+Paragraf\s+124\s*:\s*Erschlie.ungsvertrag|"
            r"Erschlie.ungsvertrag\s+nach\s+BauGB\s+Paragraf\s+124",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "II ZR 331/00 fälschlich als ARAG/Garmenbeck bezeichnet",
        re.compile(
            r"II\s+ZR\s+331/00.{0,140}ARAG|ARAG.{0,140}II\s+ZR\s+331/00",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "II ZR 354/03 fälschlich als Trihotel bezeichnet",
        re.compile(
            r"II\s+ZR\s+354/03.{0,140}Trihotel|Trihotel.{0,140}II\s+ZR\s+354/03",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "II ZR 342/14 fälschlich der Gesellschafterliste zugeordnet",
        re.compile(
            r"II\s+ZR\s+342/14.{0,160}(?:Gesellschafterliste|Legitimationswirkung)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "VIII ZR 17/16 fälschlich als Substantiierungsanker",
        re.compile(
            r"VIII\s+ZR\s+17/16.{0,180}(?:Substanti|anspruchsbegr.ndend)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "VIII ZR 185/14 fälschlich als Quotenabgeltungsanker",
        re.compile(
            r"VIII\s+ZR\s+185/14.{0,160}Quotenabgeltung",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "VIII ZR 242/13 fälschlich als Überwälzungsanker bei unrenovierter Wohnung",
        re.compile(
            r"VIII\s+ZR\s+242/13.{0,180}(?:unrenoviert|renovierungsbed.rftig)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "VIII ZR 103/06 fälschlich als Abrechnungsanker",
        re.compile(
            r"VIII\s+ZR\s+103/06.{0,180}(?:Betriebskostenabrechnung|geordnet\s+und\s+nachvollziehbar)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "VIII ZR 195/10 fälschlich als Eigenbedarfsanker",
        re.compile(
            r"VIII\s+ZR\s+195/10.{0,180}Eigenbedarf",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "XII ZB 201/16 fälschlich dem Wechselmodell zugeordnet",
        re.compile(
            r"XII\s+ZB\s+201/16.{0,180}Wechselmodell",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "XII ZB 512/18 fälschlich als allgemeiner Kindesunterhaltsanker",
        re.compile(
            r"XII\s+ZB\s+512/18.{0,180}(?:Kindesunterhalt|Unterhaltsberechnung)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "XII ZB 118/16 fälschlich als allgemeiner Auskunftsanker",
        re.compile(
            r"XII\s+ZB\s+118/16.{0,180}(?:Auskunft\s+und\s+Belegvorlage|Belegvorlage.{0,40}Unterhalt)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "XII ZB 164/20 fälschlich selbständigem Unterhalt zugeordnet",
        re.compile(
            r"XII\s+ZB\s+164/20.{0,180}(?:selbst.ndig|mehrerer\s+Jahre)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "XII ZB 499/19 fälschlich dem Versorgungsausgleich zugeordnet",
        re.compile(
            r"XII\s+ZB\s+499/19.{0,180}(?:Versorgungsausgleich|Ehezeit|Anrechtsbewertung)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "IX ZR 148/19 fälschlich als Sanierungsversuchsanker",
        re.compile(
            r"IX\s+ZR\s+148/19.{0,180}(?:Sanierungsversuch|Sanierungsbem.hung|Sanierungskonzept)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "IX ZR 219/10 fälschlich als Bargeschäftsanker",
        re.compile(
            r"IX\s+ZR\s+219/10.{0,180}(?:Bargesch.ft|Bargesch.ftsn.he)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "IX ZR 285/14 fälschlich als Liquiditätsanker",
        re.compile(
            r"IX\s+ZR\s+285/14.{0,220}(?:Liquidit.tsstatus|Zahlungsstockung|Mittelzufl.sse)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "B 4 AS 48/07 R fälschlich als Unterkunftskostenanker",
        re.compile(
            r"B\s+4\s+AS\s+48/07\s+R.{0,180}(?:Unterkunft|schl.ssiges\s+Konzept)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "B 6 KA 34/08 R fälschlich als sozialmedizinischer Aufklärungsanker",
        re.compile(
            r"B\s+6\s+KA\s+34/08\s+R.{0,220}(?:Sachverhaltsaufkl.rung|medizinische.{0,60}Grundlage)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "IV ZR 225/10 fälschlich als Beratungsanker",
        re.compile(
            r"IV\s+ZR\s+225/10.{0,180}(?:Beratungspflicht|Bedarfsermittlung)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "IV ZR 205/15 fälschlich als Anzeigepflichtanker",
        re.compile(
            r"IV\s+ZR\s+205/15.{0,180}(?:Anzeigepflicht|Risikofragen|R.cktritt)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "IV ZR 68/17 fälschlich als Obliegenheitsanker",
        re.compile(
            r"IV\s+ZR\s+68/17.{0,180}(?:Obliegenheit|Rechtsfolgenbelehrung)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "falsches Datum zum Rentenanker B 13 R 19/14 R",
        re.compile(
            r"09[.]12[.]2016.{0,100}B\s+13\s+R\s+19/14\s+R|"
            r"B\s+13\s+R\s+19/14\s+R.{0,100}09[.]12[.]2016",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "nicht verifizierter Rentenanker B 13 R 6/18 R",
        re.compile(r"\bB\s+13\s+R\s+6/18\s+R\b", re.IGNORECASE),
    ),
    Sentinel(
        "nicht verifizierter Rentenanker B 5 R 5/20 R",
        re.compile(r"\bB\s+5\s+R\s+5/20\s+R\b", re.IGNORECASE),
    ),
    Sentinel(
        "B 12 R 6/18 R fälschlich berufsständischer Befreiung zugeordnet",
        re.compile(
            r"B\s+12\s+R\s+6/18\s+R.{0,180}(?:berufsst.ndisch|Befreiung|Pflichtversicherung)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "nicht verifizierter Verwaltungsrechtsanker 7 C 79.76",
        re.compile(r"\b7\s+C\s+79[.]76\b", re.IGNORECASE),
    ),
    Sentinel(
        "7 C 87.87 fälschlich der Verwaltungsvollstreckung zugeordnet",
        re.compile(
            r"7\s+C\s+87[.]87.{0,180}Verwaltungsvollstreckung",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "8 C 127.84 fälschlich als Rücknahme- oder Widerrufsanker",
        re.compile(
            r"8\s+C\s+127[.]84.{0,180}(?:R.cknahme|Widerruf)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "SGB I Paragraf 39 fälschlich als gebundener Anspruch bezeichnet",
        re.compile(
            r"SGB\s+I\s+(?:Paragraf|§)\s*39.{0,180}(?:Anspruch\s+bei\s+Vorliegen|gesetzlichen\s+Voraussetzungen)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "IX ZB 219/10 fälschlich der Verwalterauswahl zugeordnet",
        re.compile(
            r"IX\s+ZB\s+219/10.{0,220}(?:Auswahl|Kontrolle).{0,80}Insolvenzverwalter",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "Direktanspruch fälschlich PflVG Paragraf 115 zugeordnet",
        re.compile(
            r"PflVG\s+(?:Paragraf|§)\s*115.{0,160}Direktanspruch|"
            r"Direktanspruch.{0,160}PflVG\s+(?:Paragraf|§)\s*115",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "fehlerhafte Abkürzung GeschG statt GeschGehG",
        re.compile(r"\bGeschG\s+(?:Paragraf|§)", re.IGNORECASE),
    ),
    Sentinel(
        "veraltete Bezeichnung Gemeinschaftsgeschmacksmusterverordnung",
        re.compile(r"\bGemeinschaftsgeschmacksmusterverordnung\b", re.IGNORECASE),
    ),
    Sentinel(
        "GPSR Artikel 9 und 14 fälschlich als Hersteller- und Händlerpflichten gebündelt",
        re.compile(
            r"GPSR\s+Artikel\s+9\s+und\s+Artikel\s+14.{0,120}Hersteller-.{0,20}H.ndlerpflichten",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "nicht existentes Aktenzeichen XII ZR 181/22",
        re.compile(r"\bXII\s+ZR\s+181/22\b", re.IGNORECASE),
    ),
    Sentinel(
        "nicht existentes Aktenzeichen XII ZB 504/20",
        re.compile(r"\bXII\s+ZB\s+504/20\b", re.IGNORECASE),
    ),
    Sentinel(
        "nicht existentes Aktenzeichen XII ZB 304/18",
        re.compile(r"\bXII\s+ZB\s+304/18\b", re.IGNORECASE),
    ),
    Sentinel(
        "nicht existentes Aktenzeichen XII ZB 72/19",
        re.compile(r"\bXII\s+ZB\s+72/19\b", re.IGNORECASE),
    ),
    Sentinel(
        "XII ZB 55/17 fälschlich dem Ehegattenunterhalt zugeordnet",
        re.compile(
            r"XII\s+ZB\s+55/17.{0,180}(?:Trennungsunterhalt|Ehegattenunterhalt|fiktive\s+Eink.nfte)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "XII ZB 25/19 fälschlich dem Versorgungsausgleich zugeordnet",
        re.compile(
            r"XII\s+ZB\s+25/19.{0,180}(?:Versorgungsausgleich|Versorgungstr.gerauskunft)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "XII ZB 109/16 fälschlich dem Kindesunterhalt zugeordnet",
        re.compile(
            r"XII\s+ZB\s+109/16.{0,180}(?:Kindesunterhalt|barunterhaltspflichtig|Pauschalabz.ge)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "XII ZB 340/11 fälschlich als allgemeiner Härte- oder Teilhabeanker",
        re.compile(
            r"XII\s+ZB\s+340/11.{0,180}(?:grobe\s+Unbilligkeit|H.rtekorrektur|gleichm..ige\s+Teilhabe)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "nicht existentes Domainrechtsaktenzeichen I ZR 138/19",
        re.compile(r"\bI\s+ZR\s+138/19\b", re.IGNORECASE),
    ),
    Sentinel(
        "T-612/17 fälschlich als Entscheidung des EuGH bezeichnet",
        re.compile(
            r"(?:EuGH.{0,100}T-612/17|T-612/17.{0,100}EuGH)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "Artikel 14 DSA fälschlich als Notice-and-Takedown-Verfahren",
        re.compile(
            r"(?:Art(?:ikel|[.])?\s*14.{0,140}(?:Notice-and-Takedown|Meldeverfahren)|"
            r"(?:Notice-and-Takedown|Meldeverfahren).{0,140}Art(?:ikel|[.])?\s*14)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "Paragraf 18b AufenthG fälschlich als Blue-Card-Gehaltsnorm",
        re.compile(
            r"(?:Paragraf|§)\s*18b\s+AufenthG.{0,220}"
            r"(?:Blue\s*Card|Blaue\s+Karte).{0,120}"
            r"(?:45[.]?300|2/3|zwei\s+Drittel|Gehalts(?:grenze|schwelle))|"
            r"(?:Blue\s*Card|Blaue\s+Karte).{0,160}"
            r"(?:45[.]?300|2/3|zwei\s+Drittel).{0,160}"
            r"(?:Paragraf|§)\s*18b\s+AufenthG",
            re.IGNORECASE | re.DOTALL,
        ),
    ),
    Sentinel(
        "nicht verifiziertes Schiedsaktenzeichen CAS 2018/A/22",
        re.compile(r"\bCAS\s+2018(?:/A/|\s+A\s+)22\b", re.IGNORECASE),
    ),
    Sentinel(
        "falsches Datum zum BGH-Anker IX ZB 219/10",
        re.compile(
            r"(?:19[.]09[.]2013.{0,100}IX\s+ZB\s+219/10|"
            r"IX\s+ZB\s+219/10.{0,100}19[.]09[.]2013)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "falsches Datum zum BGH-Anker VIII ZR 304/00",
        re.compile(
            r"(?:25[.]11[.]2002.{0,100}VIII\s+ZR\s+304/00|"
            r"VIII\s+ZR\s+304/00.{0,100}25[.]11[.]2002)",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "2 BvR 882/09 fälschlich Kanzleidurchsuchungen zugeordnet",
        re.compile(
            r"(?:2\s+BvR\s+882/09.{0,180}"
            r"(?:Anwaltsdurchsuch|Kanzleidurchsuch|Internal.?Investigat|Beschlagnahme)|"
            r"(?:Anwaltsdurchsuch|Kanzleidurchsuch|Internal.?Investigat|Beschlagnahme)"
            r".{0,180}2\s+BvR\s+882/09)",
            re.IGNORECASE | re.DOTALL,
        ),
    ),
    Sentinel(
        "seit 1. Juli 2026 überholte SGB-II-Abstufung 10/20/30 Prozent",
        re.compile(
            r"(?:Regelminderung|Sanktionsabstufung).{0,160}"
            r"(?:erste|1[.])\s*Pflichtverletzung.{0,60}10\s*(?:Prozent|%|v[.]\s*H[.])"
            r".{0,140}(?:zweite|2[.]|weitere).{0,60}20\s*(?:Prozent|%|v[.]\s*H[.])",
            re.IGNORECASE | re.DOTALL,
        ),
    ),
    Sentinel(
        "BGH 1 StR 618/98 fälschlich als Beschluss bezeichnet",
        re.compile(
            r"Beschluss\s+vom\s+30[.]07[.]1999.{0,80}1\s+StR\s+618/98",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "BGH VI ZR 599/16 fälschlich als Urteil bezeichnet",
        re.compile(
            r"Urteil\s+vom\s+24[.]07[.]2018.{0,80}VI\s+ZR\s+599/16",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "BVerfG 1 BvL 7/16 fälschlich als Beschluss bezeichnet",
        re.compile(
            r"Beschluss\s+vom\s+05[.]11[.]2019.{0,80}1\s+BvL\s+7/16",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "Lüth 1 BvR 400/51 fälschlich als Beschluss bezeichnet",
        re.compile(
            r"Beschluss\s+vom\s+15[.]01[.]1958.{0,80}1\s+BvR\s+400/51",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "Apothekenurteil 1 BvR 596/56 fälschlich als Beschluss bezeichnet",
        re.compile(
            r"Beschluss\s+vom\s+11[.]06[.]1958.{0,80}1\s+BvR\s+596/56",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "Lebach 1 BvR 536/72 fälschlich als Beschluss bezeichnet",
        re.compile(
            r"Beschluss\s+vom\s+05[.]06[.]1973.{0,80}1\s+BvR\s+536/72",
            re.IGNORECASE,
        ),
    ),
    Sentinel(
        "Verständigungsurteil 2 BvR 2628/10 fälschlich als Beschluss bezeichnet",
        re.compile(
            r"Beschluss\s+vom\s+19[.]03[.]2013.{0,120}"
            r"2\s+BvR\s+(?:2628|2883)/10",
            re.IGNORECASE,
        ),
    ),
)

# Ein kurzer Textanker verhindert unnötige Volltext-RegEx-Läufe pro Datei. Die
# Reihenfolge entspricht SENTINELS; Alternativen werden kleingeschrieben.
SENTINEL_HINTS = (
    ("22.000",),
    ("jahre bei vorsatz",),
    ("kleinunternehmer",),
    ("10 o 306/25",),
    ("paragrafen 611a",),
    ("normenradar:",),
    ("ix r 28/14",),
    ("c-307/22",),
    ("agbg",),
    ("b 12 ba 3/23",),
    ("ix zr 211/02",),
    ("ii zr 91/21",),
    ("viii zr 93/15",),
    ("bmf-schreiben vom 15.10.2025",),
    ("1 bvr 418/25",),
    ("x zr 95/05",),
    ("x zr 173/02",),
    ("flachbau",),
    ("bbg",),
    ("84 sgg",),
    ("gläubigerantrag",),
    ("schutzdauer",),
    ("140a", "139 ff"),
    ("vi zr 239/22",),
    ("xii zb 415/25",),
    ("x zr 123/45",),
    ("$ 22 agg", "$22 agg"),
    ("bverfge band 6",),
    ("wirtschaftlichkeit",),
    ("109 bho",),
    ("vorbehaltsklauseln",),
    ("ii zr 296/05",),
    ("patent-nichtigkeit standard",),
    ("1 bvr 2616/17",),
    ("vii zr 46/06",),
    ("vii zr 63/14",),
    ("vii zr 58/11",),
    ("stbst r 2/21",),
    ("ii r 33/19",),
    ("c-606/19",),
    ("ii zr 217/03",),
    ("kzr 12/15",),
    ("i zb 75/16",),
    ("ix zr 119/14",),
    ("ii zr 234/09",),
    ("xi zr 121/21",),
    ("viii zr 96/13",),
    ("9 azr 134/16",),
    ("x zr 89/18",),
    ("viii zr 13/19",),
    ("c-92/11",),
    ("319a",),
    ("51 wpo",),
    ("43 vvg",),
    ("16 umwg",),
    ("space weather",),
    ("zahlungsunfähigkeit",),
    ("wochen ab bestellung",),
    ("wochen ab eröffnung",),
    ("steuerhinterziehung",),
    ("146 inso",),
    ("138 inso",),
    ("freies vermögen", "freien vermögen"),
    ("passivierungsverbot",),
    ("gebrmg", "erfinderischer schritt"),
    ("4 str 247/16",),
    ("5 str 566/18",),
    ("2 bvr 669/04",),
    ("x zb 4/10",),
    ("vii zr 37/12",),
    ("vii zr 262/11",),
    ("vii zr 19/12",),
    ("vii zr 220/14",),
    ("paragraf 124",),
    ("ii zr 331/00",),
    ("ii zr 354/03",),
    ("ii zr 342/14",),
    ("viii zr 17/16",),
    ("viii zr 185/14",),
    ("viii zr 242/13",),
    ("viii zr 103/06",),
    ("viii zr 195/10",),
    ("xii zb 201/16",),
    ("xii zb 512/18",),
    ("xii zb 118/16",),
    ("xii zb 164/20",),
    ("xii zb 499/19",),
    ("ix zr 148/19",),
    ("ix zr 219/10",),
    ("ix zr 285/14",),
    ("b 4 as 48/07 r",),
    ("b 6 ka 34/08 r",),
    ("iv zr 225/10",),
    ("iv zr 205/15",),
    ("iv zr 68/17",),
    ("b 13 r 19/14 r",),
    ("b 13 r 6/18 r",),
    ("b 5 r 5/20 r",),
    ("b 12 r 6/18 r",),
    ("7 c 79.76",),
    ("7 c 87.87",),
    ("8 c 127.84",),
    ("sgb i paragraf 39", "sgb i § 39"),
    ("ix zb 219/10",),
    ("pflvg paragraf 115", "pflvg § 115"),
    ("geschg paragraf", "geschg §"),
    ("gemeinschaftsgeschmacksmusterverordnung",),
    ("gpsr artikel 9",),
    ("xii zr 181/22",),
    ("xii zb 504/20",),
    ("xii zb 304/18",),
    ("xii zb 72/19",),
    ("xii zb 55/17",),
    ("xii zb 25/19",),
    ("xii zb 109/16",),
    ("xii zb 340/11",),
    ("i zr 138/19",),
    ("t-612/17",),
    ("14",),
    ("18b",),
    ("cas 2018",),
    ("ix zb 219/10",),
    ("viii zr 304/00",),
    ("2 bvr 882/09",),
    ("regelminderung", "sanktionsabstufung"),
    ("1 str 618/98",),
    ("vi zr 599/16",),
    ("1 bvl 7/16",),
    ("1 bvr 400/51",),
    ("1 bvr 596/56",),
    ("1 bvr 536/72",),
    ("2 bvr 2628/10", "2 bvr 2883/10"),
)

if len(SENTINEL_HINTS) != len(SENTINELS):
    raise RuntimeError("SENTINEL_HINTS und SENTINELS sind nicht synchron")


def markdown_files() -> list[Path]:
    return sorted(
        path
        for path in REPO.rglob("*.md")
        if ".git" not in path.parts and "node_modules" not in path.parts
    )


def main() -> int:
    findings: list[str] = []
    files = markdown_files()
    for path in files:
        relative = path.relative_to(REPO)
        text = path.read_text(encoding="utf-8", errors="replace")
        if path.name == "SKILL.md":
            if relative.as_posix().endswith(
                "fachanwalt-sportrecht/skills/"
                "fussballtransfer-vertragsbruch-und-rstp/SKILL.md"
            ):
                match = re.search(r"\b(?:NADA-Code|BImSchG)\b", text, re.IGNORECASE)
                if match:
                    line = text.count("\n", 0, match.start()) + 1
                    findings.append(
                        f"{relative}:{line}: "
                        "fachfremde Doping- oder Immissionsnorm im Fußballtransfer"
                    )
            match = re.search(
                r"^###\s+Kuratierte\s+Normen-Bibliothek\s*$",
                text,
                re.IGNORECASE | re.MULTILINE,
            )
            if match:
                line = text.count("\n", 0, match.start()) + 1
                findings.append(
                    f"{relative}:{line}: "
                    "fachgebietsweiter Normenanhang im Einzelskill"
                )
            match = re.search(
                r"^\|[^\n]*Rechtsprechung\s+(?:live\s+prüfen|"
                r"keine\s+Entscheidung\s+aus\s+Modellwissen)[^\n]*\|\s*$",
                text,
                re.IGNORECASE | re.MULTILINE,
            )
            if match:
                line = text.count("\n", 0, match.start()) + 1
                findings.append(
                    f"{relative}:{line}: "
                    "Platzhalterzeile statt fachlicher Tabelleninformation"
                )
            match = re.search(
                r"nur verwenden, wenn die Fundstelle über ein amtliches "
                r"oder frei zugängliches Portal gegengeprüft ist",
                text,
                re.IGNORECASE,
            )
            if match:
                line = text.count("\n", 0, match.start()) + 1
                findings.append(
                    f"{relative}:{line}: "
                    "ungeprüfter Entscheidungsanker im produktiven Skill"
                )
            match = re.search(
                r"\b(?:WRONG_TOPIC|NOT_FOUND|UNVERIFIABLE)\b",
                text,
                re.IGNORECASE,
            )
            if match:
                line = text.count("\n", 0, match.start()) + 1
                findings.append(
                    f"{relative}:{line}: "
                    "interner Auditstatus im produktiven Skill"
                )
        if relative.parts and relative.parts[0] == "haushaltsrecht-bho-bund-laender":
            match = re.search(
                r"\b(?:BVerwG\s+8\s+C\s+8[.]14|"
                r"BVerwG\s+6\s+C\s+3[.]21|"
                r"BVerfG\s+2\s+BvR\s+2628/10)\b",
                text,
                re.IGNORECASE,
            )
            if match:
                line = text.count("\n", 0, match.start()) + 1
                findings.append(
                    f"{relative}:{line}: "
                    "fachfremde Entscheidung im Haushaltsrecht"
                )
        if (
            len(relative.parts) == 2
            and relative.parts[0] in {"fahrgastrechte", "fluggastrechte"}
            and relative.name.endswith(("-werkstatt.md", "-schnellstart.md"))
        ):
            match = re.search(
                r"\b(?:StVG|Straßenverkehrsgesetz|VVG\s+Paragraf\s+115)\b",
                text,
                re.IGNORECASE,
            )
            if match:
                line = text.count("\n", 0, match.start()) + 1
                findings.append(
                    f"{relative}:{line}: "
                    "straßenverkehrsrechtlicher Fremdanker im Flug- oder Fahrgastprompt"
                )
        folded = text.casefold()
        for sentinel, hints in zip(SENTINELS, SENTINEL_HINTS, strict=True):
            if not any(hint in folded for hint in hints):
                continue
            match = sentinel.pattern.search(text)
            if not match:
                continue
            line = text.count("\n", 0, match.start()) + 1
            findings.append(
                f"{relative}:{line}: {sentinel.label}"
            )

    if findings:
        print(f"validate-current-law-sentinels: {len(findings)} Fehler")
        for finding in findings[:100]:
            print(f"- {finding}")
        if len(findings) > 100:
            print(f"- ... {len(findings) - 100} weitere Treffer")
        return 1

    print(
        "validate-current-law-sentinels OK "
        f"({len(files)} Markdown-Dateien, {len(SENTINELS)} Sperrmuster)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
