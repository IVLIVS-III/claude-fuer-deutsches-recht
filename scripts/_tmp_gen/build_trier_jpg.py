#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut ein Standbild-artiges JPG als Beschreibung der Kamerabeweislage Rampe 4."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

ROOT = Path("/home/user/workspace/legal-work/target/testakten/unfallversicherung-arbeitsunfall-lagerleiter-sturz-trier")
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

W, H = 1200, 800
BG = (18, 18, 18)
HEADER = (40, 40, 40)


def build():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    f_header = ImageFont.truetype(FONT_BOLD, 26)
    f_reg = ImageFont.truetype(FONT_REG, 20)
    f_mono = ImageFont.truetype(FONT_MONO, 18)

    draw.rectangle([0, 0, W, 60], fill=HEADER)
    draw.text((20, 16), "Kamera Rampe 4 - Systemprotokoll (Standbild-Beschreibung, kein Originalbild)", font=f_header, fill=(255, 255, 255))

    y = 90
    draw.text((20, y), "Kamerakanal: RAMPE4_CAM_02", font=f_mono, fill=(0, 220, 0)); y += 30
    draw.text((20, y), "Status 06:28 - 06:31 Uhr: Verbindung aktiv, letztes Bild vorhanden", font=f_reg, fill=(220, 220, 220)); y += 30
    draw.text((20, y), "Status 06:31 - 07:13 Uhr: Verbindungsabbruch zum Switch, kein Bildmaterial", font=f_reg, fill=(255, 120, 120)); y += 30
    draw.text((20, y), "Status ab 07:13 Uhr: Verbindung wiederhergestellt", font=f_reg, fill=(220, 220, 220)); y += 50

    draw.line([20, y, W - 20, y], fill=(90, 90, 90), width=2); y += 30
    draw.text((20, y), "Angrenzende Kamera RAMPE3_CAM_01 (Randbereich, Rampe 4 nur teilweise sichtbar)", font=f_mono, fill=(0, 220, 0)); y += 30
    draw.text((20, y), "06:38 Uhr: Person mit Werkzeug auf dem Weg Richtung Rampe 4 erkennbar", font=f_reg, fill=(220, 220, 220)); y += 30
    draw.text((20, y), "07:02 Uhr: Rettungsdienstpersonal im Bildausschnitt erkennbar", font=f_reg, fill=(220, 220, 220)); y += 50

    draw.line([20, y, W - 20, y], fill=(90, 90, 90), width=2); y += 30
    draw.text((20, y), "Hinweis: Der eigentliche Sturzvorgang 06:38 bis 06:45 Uhr ist auf keiner", font=f_reg, fill=(255, 200, 80)); y += 26
    draw.text((20, y), "verfuegbaren Kameraaufzeichnung erfasst. Beschreibung erstellt durch IT-Abteilung", font=f_reg, fill=(255, 200, 80)); y += 26
    draw.text((20, y), "MoselLogistik GmbH am 09.04.2026 zur Vorlage bei der Berufsgenossenschaft.", font=f_reg, fill=(255, 200, 80)); y += 40

    img.save(ROOT / "jpg" / "kamera_standbildbeschreibung_rampe4.jpg", quality=90)
    print("geschrieben: kamera_standbildbeschreibung_rampe4.jpg")


if __name__ == "__main__":
    build()
