from PIL import Image, ImageDraw, ImageFont

BASE = "/home/user/workspace/legal-work/target/testakten/sozialrecht-elektrorollstuhl-koerner-oldenburg/jpg"
import os
os.makedirs(BASE, exist_ok=True)

def font(size):
    for path in [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ]:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()

def make_placeholder(filename, title, lines, w=1000, h=750):
    img = Image.new("RGB", (w, h), (235, 235, 230))
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, w - 1, h - 1], outline=(120, 120, 120), width=3)
    d.rectangle([20, 20, w - 20, 90], fill=(60, 60, 60))
    d.text((35, 35), title, font=font(24), fill=(255, 255, 255))
    y = 130
    for line in lines:
        d.text((35, y), line, font=font(18), fill=(30, 30, 30))
        y += 34
    d.text((35, h - 45), "Foto-Platzhalter, Bildbeschreibung fuer die Akte", font=font(14), fill=(90, 90, 90))
    img.save(f"{BASE}/{filename}", quality=88)
    print("geschrieben:", filename)

make_placeholder(
    "treppenhaus_altbau_eingang.jpg",
    "Treppenhaus Eingang, Peterstrasse 18",
    [
        "Aufnahme vom 24.05.2026, Wohnumfeldbegehung RehaTechnik Albrecht.",
        "Schmales gewendeltes Treppenhaus, keine Rampe, kein Aufzug.",
        "Stufenhoehe circa 18 Zentimeter, insgesamt 16 Stufen zum ersten Obergeschoss.",
        "Handlauf einseitig vorhanden, Breite des Treppenhauses 95 Zentimeter.",
        "Ein Elektrorollstuhl kann diese Treppe nicht befahren, Nutzung nur",
        "innerhalb der Wohnung und nach Verlassen des Hauses ueber die",
        "vorhandene Rollstuhlrampe am Hinterausgang vorgesehen.",
    ],
)

make_placeholder(
    "wohnzimmer_bewegungsflaeche.jpg",
    "Wohnzimmer, Bewegungsflaeche",
    [
        "Aufnahme vom 24.05.2026.",
        "Durchgangsbreite zwischen Sofa und Wohnzimmerschrank 88 Zentimeter.",
        "Türbreite zum Flur 82 Zentimeter, ausreichend fuer Referenzmodell.",
        "Teppichboden mit Kurzflor, laut Herstellerangabe befahrbar.",
        "Kein Wendekreis von 1,50 Metern im Raum vorhanden, Rollstuhl",
        "muss rueckwaerts aus dem Raum gefahren werden koennen.",
    ],
)

make_placeholder(
    "hinterausgang_rampe.jpg",
    "Hinterausgang mit Rollstuhlrampe",
    [
        "Aufnahme vom 24.05.2026.",
        "Vom Vermieter 2019 nachtraeglich errichtete Holzrampe, Neigung etwa 9 Prozent.",
        "Rampenlaenge 4,20 Meter, Breite 100 Zentimeter, beidseitig Handlauf.",
        "Zugang zum Gehweg der Peterstrasse ueber die Rampe moeglich.",
        "Von dort naechste Bushaltestelle 180 Meter, Apotheke 340 Meter,",
        "Hausarztpraxis Dr. Stahlmann 460 Meter entfernt.",
    ],
)

make_placeholder(
    "gehweg_peterstrasse.jpg",
    "Gehweg Peterstrasse Richtung Innenstadt",
    [
        "Aufnahme vom 24.05.2026.",
        "Asphaltierter Gehweg, an zwei Stellen abgesenkte Bordsteine.",
        "Leichtes Gefaelle auf den ersten 60 Metern, danach eben.",
        "Wetterabhaengig teilweise nass und rutschig, keine Ueberdachung.",
        "Fussgaengerampel an der Kreuzung Peterstrasse/Damm mit",
        "Bordsteinabsenkung auf beiden Seiten.",
    ],
)

print("fertig jpg")
