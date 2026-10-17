"""Reduz as fontes ao que o site usa (latim + pontuação) e corta eixos de peso não usados.

Uso: python tools/subset_fonts.py
Entrada: site/static/fonts/src/*.woff2 (arquivos originais do Google Fonts)
Saída:   site/static/fonts/<mesmo nome>.woff2
"""
import io
import os

from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "site", "static", "fonts", "src")
OUT = os.path.join(ROOT, "site", "static", "fonts")

UNICODES = (list(range(0x20, 0x7F)) + list(range(0xA0, 0x100)) +
            [0x2013, 0x2014, 0x2018, 0x2019, 0x201C, 0x201D, 0x2022, 0x2026, 0x203A, 0x2039, 0x20AC, 0x2192])

# limites de eixo por arquivo (o que o CSS realmente usa)
AXES = {
    "Fraunces-normal-latin.woff2": {"wght": (500, 700)},
    "Fraunces-italic-latin.woff2": {"wght": (400, 600)},
    "NunitoSans-normal-latin.woff2": {"wght": (400, 800)},
}


def main():
    for name in sorted(os.listdir(SRC)):
        if not name.endswith(".woff2"):
            continue
        font = TTFont(os.path.join(SRC, name))
        opts = subset.Options()
        opts.flavor = "woff2"
        opts.layout_features = ["kern", "liga", "calt", "ccmp", "locl", "mark", "mkmk", "onum", "lnum", "pnum", "tnum"]
        opts.name_IDs = ["*"]
        opts.notdef_outline = True
        sub = subset.Subsetter(opts)
        sub.populate(unicodes=UNICODES)
        sub.subset(font)
        # corta os eixos depois do subset (antes dele o fontTools falha no gvar do .notdef)
        if name in AXES and "fvar" in font:
            buf = io.BytesIO()
            font.flavor = None
            font.save(buf)
            buf.seek(0)
            font = instancer.instantiateVariableFont(TTFont(buf), AXES[name])
        dest = os.path.join(OUT, name)
        font.flavor = "woff2"
        font.save(dest)
        before = os.path.getsize(os.path.join(SRC, name)) / 1024
        after = os.path.getsize(dest) / 1024
        print(f"{name}: {before:.0f} KB -> {after:.0f} KB")


if __name__ == "__main__":
    main()
