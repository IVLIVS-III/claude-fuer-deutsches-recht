#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut einen WhatsApp-artigen Chat-Screenshot als JPG fuer die Erlangen-Akte."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

ROOT = Path("/home/user/workspace/legal-work/target/testakten/statusfeststellung-gmbh-geschaeftsfuehrer-minderheit-erlangen")

FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

W, H = 1080, 1500
BG = (229, 221, 213)
HEADER_BG = (0, 122, 92)
BUBBLE_IN = (255, 255, 255)
BUBBLE_OUT = (220, 248, 198)
TEXT = (30, 30, 30)
META = (110, 110, 110)


def wrap_text(text, font, max_width, draw):
    words = text.split()
    lines = []
    cur = ""
    for w in words:
        test = (cur + " " + w).strip()
        bbox = draw.textbbox((0, 0), test, font=font)
        if bbox[2] - bbox[0] > max_width and cur:
            lines.append(cur)
            cur = w
        else:
            cur = test
    if cur:
        lines.append(cur)
    return lines


def draw_bubble(draw, y, text, sender, time_str, out=False, font=None, font_bold=None):
    max_bubble_w = 760
    pad = 22
    lines = wrap_text(text, font, max_bubble_w - 2 * pad, draw)
    line_h = 34
    bubble_h = pad * 2 + len(lines) * line_h + 30
    bubble_w = max_bubble_w
    x = W - 60 - bubble_w if out else 60
    color = BUBBLE_OUT if out else BUBBLE_IN
    draw.rounded_rectangle([x, y, x + bubble_w, y + bubble_h], radius=18, fill=color)
    ty = y + pad
    if not out:
        draw.text((x + pad, ty), sender, font=font_bold, fill=(0, 100, 80))
        ty += 30
    for line in lines:
        draw.text((x + pad, ty), line, font=font, fill=TEXT)
        ty += line_h
    draw.text((x + bubble_w - pad - 70, y + bubble_h - 26), time_str, font=font, fill=META)
    return y + bubble_h + 22


def build():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT_REG, 26)
    font_bold = ImageFont.truetype(FONT_BOLD, 26)
    font_header = ImageFont.truetype(FONT_BOLD, 32)

    draw.rectangle([0, 0, W, 110], fill=HEADER_BG)
    draw.ellipse([20, 25, 80, 85], fill=(255, 255, 255))
    draw.text((100, 30), "Gesellschafter Neuralis (Gruppe)", font=font_header, fill=(255, 255, 255))
    draw.text((100, 68), "Torben Aldenhoven, Henrik Vogt, Miriam Seidl", font=font, fill=(220, 240, 235))

    y = 140
    msgs = [
        ("Torben Aldenhoven", "Kurzer Reminder: die Sperrminoritaet soll strikt auf Entwicklung begrenzt bleiben, sonst trage ich das intern nicht mit.", "14:02", False),
        ("Henrik Vogt", "Verstanden. Ich brauche aber wenigstens fuer das Ressort volle Zustimmungspflicht, sonst bringt mir das nichts.", "14:06", True),
        ("Miriam Seidl", "Koennt ihr das bitte auch mit Blick auf das DRV-Verfahren abstimmen? Nicht dass wir am Ende eine Regelung haben, die uns dort schadet.", "14:11", False),
        ("Torben Aldenhoven", "Das ist Sache der Anwaelte. Uns geht es um die operative Kontrolle, nicht um das DRV-Verfahren.", "14:13", False),
        ("Henrik Vogt", "Fabian sagt, eng gefasst ist besser als nichts. Ich nehme das erstmal so an und verhandle naechstes Jahr nach.", "14:20", True),
    ]
    for sender, text, time_str, out in msgs:
        y = draw_bubble(draw, y, text, sender, time_str, out=out, font=font, font_bold=font_bold)

    out_path = ROOT / "jpg" / "whatsapp-gesellschafter-sperrminoritaet.jpg"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(out_path, "JPEG", quality=88)
    print("geschrieben:", out_path)


if __name__ == "__main__":
    build()
