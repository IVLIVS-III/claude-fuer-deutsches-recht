#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut einen Screenshot-artigen JPG-Ausdruck des Handelsregisterportals."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

ROOT = Path("/home/user/workspace/legal-work/target/testakten/statusfeststellung-gmbh-geschaeftsfuehrer-minderheit-erlangen")
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

W, H = 1200, 900
BG = (255, 255, 255)
HEADER = (24, 60, 110)


def build():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    f_header = ImageFont.truetype(FONT_BOLD, 30)
    f_reg = ImageFont.truetype(FONT_REG, 22)
    f_bold = ImageFont.truetype(FONT_BOLD, 22)
    f_mono = ImageFont.truetype(FONT_MONO, 20)

    draw.rectangle([0, 0, W, 80], fill=HEADER)
    draw.text((30, 22), "Gemeinsames Registerportal der Laender - Unternehmensregister", font=f_header, fill=(255, 255, 255))

    y = 110
    draw.text((30, y), "Registergericht: Amtsgericht Fuerth", font=f_reg, fill=(20, 20, 20)); y += 34
    draw.text((30, y), "Registerart / Registernummer: HRB 18442", font=f_bold, fill=(20, 20, 20)); y += 34
    draw.text((30, y), "Firma: Neuralis MedTech GmbH", font=f_reg, fill=(20, 20, 20)); y += 34
    draw.text((30, y), "Sitz: Erlangen", font=f_reg, fill=(20, 20, 20)); y += 50

    draw.line([30, y, W - 30, y], fill=(200, 200, 200), width=2); y += 20
    draw.text((30, y), "Chronologische Eintragungen (Auszug)", font=f_bold, fill=(20, 20, 20)); y += 40

    rows = [
        "AD  14.11.2019  Ersteintragung. GF: Dr. Henrik Vogt, einzelvertretungsberecht.",
        "AD  22.05.2021  Kapitalerhoehung auf 100.000,00 EUR",
        "AD  06.03.2023  Neufassung Gesellschaftsvertrag (Urk. Nr. 214/2023)",
        "AD  19.09.2025  Nachtrag Paragraf 6 und Paragraf 9 (Urk. Nr. 501/2025)",
    ]
    for r in rows:
        draw.text((40, y), r, font=f_mono, fill=(30, 30, 30))
        y += 34

    y += 30
    draw.line([30, y, W - 30, y], fill=(200, 200, 200), width=2); y += 20
    draw.text((30, y), "Abrufhinweis: Abruf vom 03.02.2026, gebuehrenpflichtiger Ausdruck,", font=f_reg, fill=(90, 90, 90)); y += 30
    draw.text((30, y), "elektronisch signiert.", font=f_reg, fill=(90, 90, 90))

    out_path = ROOT / "jpg" / "hr-portal-auszug-screenshot.jpg"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(out_path, "JPEG", quality=88)
    print("geschrieben:", out_path)


if __name__ == "__main__":
    build()
