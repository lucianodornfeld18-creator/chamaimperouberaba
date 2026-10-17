"""Gera as versões web das fotos registradas em site/_photos.py.

Uso:  python images/process_photos.py
Saída: site/static/img/<slug>-<largura>.webp, site/static/og/<slug>.jpg
       site/_imgmeta.json (largura x altura de cada versão, lido pelo build)

- Sem metadados EXIF nas saídas.
- Retoques: cada caixa (x0, y0, x1, y1) é pintada com a cor mediana do entorno
  e suavizada (usado para apagar o letreiro antigo da caixa d'água).
- A foto dos anfitriões vem do post do Instagram e é recortada em 4:5.
"""
import json
import os
import statistics
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "site"))
from _photos import PHOTOS, HERO  # noqa: E402

SRC = os.path.join(ROOT, "images", "source")
SR2X = os.path.join(ROOT, "images", "sr2x")  # ampliadas por IA (images/upscale_ai.py)
BRAND = os.path.join(ROOT, "brand")
OUT = os.path.join(ROOT, "site", "static", "img")
OG = os.path.join(ROOT, "site", "static", "og")
META = os.path.join(ROOT, "site", "_imgmeta.json")
HOSTS_ORIGINAL = os.path.join(ROOT, "images", "incoming", "instagram", "post-anfitrioes-DZck6FcHF52.jpg")

WIDTHS = [480, 800, 1200, 1600]
HERO_EXTRA = 2000
PORTRAIT_WIDTHS = [400, 640, 960]
QUALITY = 72


def retouch(im, boxes):
    im = im.copy()
    px = im.load()
    for x0, y0, x1, y1 in boxes:
        # amostra um anel de 2 px em volta da caixa (cor da própria superfície)
        ring = []
        for x in range(x0 - 2, x1 + 3):
            for y in (y0 - 2, y1 + 2):
                ring.append(px[x, y])
        for y in range(y0 - 2, y1 + 3):
            for x in (x0 - 2, x1 + 2):
                ring.append(px[x, y])
        color = tuple(int(statistics.median(c[i] for c in ring)) for i in range(3))
        ImageDraw.Draw(im).rectangle((x0, y0, x1, y1), fill=color)
        region = im.crop((x0 - 2, y0 - 2, x1 + 3, y1 + 3)).filter(ImageFilter.GaussianBlur(1))
        im.paste(region, (x0 - 2, y0 - 2))
    return im


def hosts_source():
    """Recorta a foto do post (3072x4096) em 4:5 com os dois anfitriões."""
    dest = os.path.join(SRC, "anfitrioes.jpg")
    if os.path.exists(dest):
        return dest
    im = ImageOps.exif_transpose(Image.open(HOSTS_ORIGINAL)).convert("RGB")
    w, h = im.size
    cw = w
    ch = int(cw * 5 / 4)
    top = max(0, int(h * 0.04))
    if top + ch > h:
        top = h - ch
    im.crop((0, top, cw, top + ch)).save(dest, quality=92)
    return dest


def save_webp(im, path):
    im.save(path, "WEBP", quality=QUALITY, method=6)


def og_image(im, slug, focal):
    """1200x630 com faixa discreta do nome. Recorte pelo ponto focal."""
    tw, th = 1200, 630
    scale = max(tw / im.width, th / im.height)
    big = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
    fx = big.width * focal[0] / 100
    fy = big.height * focal[1] / 100
    left = int(min(max(fx - tw / 2, 0), big.width - tw))
    top = int(min(max(fy - th / 2, 0), big.height - th))
    card = big.crop((left, top, left + tw, top + th)).filter(ImageFilter.UnsharpMask(1.2, 40, 2))
    shade = Image.new("L", (tw, th), 0)
    d = ImageDraw.Draw(shade)
    for y in range(th):
        v = max(0, (y - th * 0.42) / (th * 0.58)) ** 0.85
        d.line((0, y, tw, y), fill=int(225 * v))
    dark = Image.new("RGB", (tw, th), (12, 26, 19))
    card = Image.composite(dark, card, shade)
    logo = Image.open(os.path.join(BRAND, "png", "logo-chacara-imperio-512.png")).convert("RGBA").resize((210, 210), Image.LANCZOS)
    card = card.convert("RGBA")
    card.alpha_composite(logo, (44, th - 254))
    d = ImageDraw.Draw(card)
    try:
        f1 = ImageFont.truetype(os.path.join(BRAND, "fonts", "Cinzel[wght].ttf"), 54)
        f1.set_variation_by_axes([650])
        f2 = ImageFont.truetype(os.path.join(BRAND, "fonts", "Montserrat[wght].ttf"), 25)
        f2.set_variation_by_axes([500])
    except OSError:
        f1 = f2 = ImageFont.load_default()
    d.text((278, th - 168), "CHÁCARA IMPÉRIO", font=f1, fill=(250, 245, 232))
    d.text((281, th - 94), "EVENTOS E HOSPEDAGEM EM UBERABA – MG", font=f2, fill=(232, 212, 160))
    card = card.convert("RGB")
    os.makedirs(OG, exist_ok=True)
    card.save(os.path.join(OG, f"{slug}.jpg"), quality=84, optimize=True, progressive=True)


def main():
    os.makedirs(OUT, exist_ok=True)
    meta = {}
    for pid, p in PHOTOS.items():
        scale = 1
        if p["src"] == "anfitrioes.jpg":
            src = hosts_source()
        elif os.path.exists(os.path.join(SR2X, p["src"])):
            src, scale = os.path.join(SR2X, p["src"]), 2
        else:
            src = os.path.join(SRC, p["src"])
        im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
        if p.get("retouch"):
            im = retouch(im, [tuple(v * scale for v in box) for box in p["retouch"]])
        widths = PORTRAIT_WIDTHS if p.get("portrait") else list(WIDTHS)
        if pid == HERO:
            widths = widths + [HERO_EXTRA]
        variants = {}
        for w in widths:
            if w > im.width:
                continue
            h = round(im.height * w / im.width)
            v = im.resize((w, h), Image.LANCZOS)
            name = f"{p['slug']}-{w}.webp"
            save_webp(v, os.path.join(OUT, name))
            variants[w] = [w, h]
        if not p.get("portrait"):
            og_image(im, p["slug"], p.get("focal", (50, 50)))
        meta[pid] = {"slug": p["slug"], "variants": variants, "ratio": round(im.width / im.height, 4)}
        print(f"{pid:22s} {im.width}x{im.height} -> {sorted(variants)}")
    with open(META, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=1)
    total = sum(os.path.getsize(os.path.join(OUT, n)) for n in os.listdir(OUT) if n.endswith(".webp"))
    print(f"{len(meta)} fotos, {total/1024:.0f} KB em webp")


if __name__ == "__main__":
    main()
