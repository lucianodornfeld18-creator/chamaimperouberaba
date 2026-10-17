"""Redesenho vetorial da logo da Chácara Império (a partir do avatar do Instagram, 133 px).

Uso: python brand/make_logo.py <pasta_com_as_fontes_ttf>
Saídas (brand/):
  logo-chacara-imperio.svg        logo circular completa (disco verde, monograma, nome, slogan)
  logo-mark.svg                   monograma sobre o disco verde (selo pequeno, favicon)
  logo-horizontal-claro.svg       selo + nome + slogan em creme (sobre foto/fundo escuro)
  logo-horizontal-escuro.svg      selo + nome + slogan em verde (sobre fundo claro)
  png/…                           exportações em PNG (via Chromium/Playwright)

Fontes (OFL, Google Fonts): Cinzel (nome), Montserrat (slogan), Bodoni Moda ("C"), Allura ("I").
O texto vira curva (path): o SVG não depende de fonte instalada.
Correção em relação ao arquivo original: "CHÁÇARA" (com cedilha) → "CHÁCARA".
"""
import io
import math
import os
import sys

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "fonts")

CREAM = "#f6f1e4"
GREEN_DARK = "#163626"


def load(name, axes=None):
    f = TTFont(os.path.join(FONTS, name))
    if axes:
        f = instancer.instantiateVariableFont(f, axes)
        buf = io.BytesIO()
        f.save(buf)
        buf.seek(0)
        f = TTFont(buf)
    return f


CINZEL = load("Cinzel[wght].ttf", {"wght": 650})
MONT = load("Montserrat[wght].ttf", {"wght": 500})
BODONI = load("BodoniModa[opsz,wght].ttf", {"wght": 500, "opsz": 96})
ALLURA = load("Allura-Regular.ttf")


def glyph_d(font, ch, x, y, size, sx=1.0):
    """Contorno de um caractere como 'd' de SVG, com a linha de base em y (sx = escala horizontal)."""
    gs = font.getGlyphSet()
    name = font.getBestCmap()[ord(ch)]
    upm = font["head"].unitsPerEm
    s = size / upm
    pen = SVGPathPen(gs)
    gs[name].draw(TransformPen(pen, (s * sx, 0, 0, -s, x, y)))
    return pen.getCommands(), font["hmtx"][name][0] * s * sx


def text_d(font, text, size, tracking=0.0):
    """Texto com espaçamento extra (em em) → (d, largura). Origem em (0, 0) = linha de base."""
    ds, x = [], 0.0
    for i, ch in enumerate(text):
        if ch == " ":
            x += font["hmtx"][font.getBestCmap()[32]][0] * size / font["head"].unitsPerEm + tracking * size
            continue
        d, adv = glyph_d(font, ch, x, 0, size)
        ds.append(d)
        x += adv + (tracking * size if i < len(text) - 1 else 0)
    return " ".join(ds), x


def bbox_of(font, ch, size):
    gs = font.getGlyphSet()
    from fontTools.pens.boundsPen import BoundsPen
    bp = BoundsPen(gs)
    gs[font.getBestCmap()[ord(ch)]].draw(bp)
    s = size / font["head"].unitsPerEm
    x0, y0, x1, y1 = bp.bounds
    return x0 * s, -y1 * s, x1 * s, -y0 * s  # coordenadas SVG (y para baixo)


# ── Monograma (C + anel + I + folhas douradas), desenhado num quadro de 400×400 ──
def monogram(prefix, leaves=True):
    size_c, sx = 470, 1.15                      # o C da logo é mais redondo que o da Bodoni
    x0, y0, x1, y1 = bbox_of(BODONI, "C", size_c)
    cw, ch = (x1 - x0) * sx, y1 - y0
    cx_c, cy_c = 168, 200
    c_d, _ = glyph_d(BODONI, "C", cx_c - (x0 * sx + cw / 2), cy_c - (y0 + ch / 2), size_c, sx)
    r_c = ch / 2
    ring_cx, ring_cy, ring_r = cx_c + 62, cy_c + 6, r_c * 0.97
    size_i = 345
    ix0, iy0, ix1, iy1 = bbox_of(ALLURA, "I", size_i)
    i_cx, i_cy = ring_cx - 10, ring_cy + 8
    i_d, _ = glyph_d(ALLURA, "I", i_cx - (ix0 + (ix1 - ix0) / 2), i_cy - (iy0 + (iy1 - iy0) / 2), size_i)
    gold, glow, clip = f"{prefix}gold", f"{prefix}glow", f"{prefix}clip"
    # vão interno do C (elipse) cortado antes do I
    ex, ey, erx, ery = cx_c + 4, cy_c + 2, cw * 0.39, ch * 0.41
    cut = i_cx - 22
    parts = [f'''<defs>
<linearGradient id="{gold}" x1="0" y1="1" x2="1" y2="0">
<stop offset="0" stop-color="#7a5a1e"/><stop offset=".3" stop-color="#c39a45"/>
<stop offset=".55" stop-color="#f3dc98"/><stop offset=".75" stop-color="#cfa850"/><stop offset="1" stop-color="#94702a"/>
</linearGradient>
<radialGradient id="{glow}" cx=".35" cy=".55" r=".75">
<stop offset="0" stop-color="#e9cf86" stop-opacity=".55"/><stop offset=".6" stop-color="#b48d3c" stop-opacity=".28"/><stop offset="1" stop-color="#7a5a1e" stop-opacity="0"/>
</radialGradient>
<clipPath id="{clip}"><ellipse cx="{ex:.1f}" cy="{ey:.1f}" rx="{erx:.1f}" ry="{ery:.1f}"/></clipPath>
<linearGradient id="{prefix}fade" gradientUnits="userSpaceOnUse" x1="{ex - erx:.1f}" y1="{ey + ery * .4:.1f}" x2="{cut + 30:.1f}" y2="{ey - ery * .2:.1f}"><stop offset="0" stop-color="#fff"/><stop offset=".62" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<mask id="{prefix}mask" maskUnits="userSpaceOnUse" x="0" y="0" width="400" height="400"><rect x="0" y="0" width="400" height="400" fill="url(#{prefix}fade)"/></mask>
</defs>''']
    if leaves:
        # folhagem dourada (o original tem textura de folhas douradas no vão do C)
        # uma folha de palmeira: folíolos de cada lado em <path> separado (mesmo sentido → sem "xadrez")
        bx, by = ex - erx * 0.70, ey + ery * 0.98
        tx, ty = ex + erx * 0.30, ey - ery * 0.98
        ang = math.atan2(ty - by, tx - bx)
        sides = {-1: [], 1: []}
        for k in range(12):
            t = 0.05 + k * 0.08
            px, py = bx + (tx - bx) * t, by + (ty - by) * t
            for side in (-1, 1):
                a = ang + side * (1.0 - t * 0.4)
                ln = 112 * (1 - abs(t - 0.42) * 0.85)
                qx, qy = px + math.cos(a) * ln, py + math.sin(a) * ln
                mx, my = px + math.cos(a + side * 0.30) * ln * 0.55, py + math.sin(a + side * 0.30) * ln * 0.55
                nx, ny = px + math.cos(a - side * 0.10) * ln * 0.5, py + math.sin(a - side * 0.10) * ln * 0.5
                sides[side].append(f"M{px:.1f},{py:.1f} Q{mx:.1f},{my:.1f} {qx:.1f},{qy:.1f} Q{nx:.1f},{ny:.1f} {px:.1f},{py:.1f}Z")
        rib = f"M{bx:.1f},{by:.1f} Q{(bx + tx) / 2 - 16:.1f},{(by + ty) / 2 + 6:.1f} {tx:.1f},{ty:.1f}"
        parts.append(f'<g clip-path="url(#{clip})" mask="url(#{prefix}mask)"><rect x="{ex - erx:.1f}" y="{ey - ery:.1f}" width="{erx * 2:.1f}" height="{ery * 2:.1f}" fill="url(#{glow})"/>'
                     f'<path d="{" ".join(sides[-1])}" fill="url(#{gold})" opacity=".92"/>'
                     f'<path d="{" ".join(sides[1])}" fill="url(#{gold})" opacity=".92"/>'
                     f'<path d="{rib}" fill="none" stroke="url(#{gold})" stroke-width="4" stroke-linecap="round"/></g>')
    parts.append(f'<circle cx="{ring_cx:.1f}" cy="{ring_cy:.1f}" r="{ring_r:.1f}" fill="none" stroke="{CREAM}" stroke-width="6.5"/>')
    parts.append(f'<path d="{c_d}" fill="{CREAM}"/>')
    parts.append(f'<path d="{i_d}" fill="{CREAM}"/>')
    return "\n".join(parts)


def disc_defs(prefix):
    return f'''<linearGradient id="{prefix}bg" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="#386b51"/><stop offset=".24" stop-color="#1c3f2e"/><stop offset=".5" stop-color="#10271b"/>
<stop offset=".74" stop-color="#234c38"/><stop offset="1" stop-color="#346650"/>
</linearGradient>
<radialGradient id="{prefix}vig" cx=".5" cy=".5" r=".5">
<stop offset=".72" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".28"/>
</radialGradient>
<linearGradient id="{prefix}sheen" x1="0" y1="0" x2="1" y2="1">
<stop offset=".22" stop-color="#fff" stop-opacity="0"/><stop offset=".4" stop-color="#cdeedc" stop-opacity=".13"/>
<stop offset=".5" stop-color="#cdeedc" stop-opacity=".05"/><stop offset=".64" stop-color="#fff" stop-opacity="0"/>
</linearGradient>'''


def disc(prefix, cx=500, cy=500, r=500):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#{prefix}bg)"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#{prefix}sheen)"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#{prefix}vig)"/>')


def centered(d, width, cx, baseline):
    return f'<path transform="translate({cx - width / 2:.1f} {baseline:.1f})" d="{d}"/>'


def logo_circle():
    p = "lc-"
    name1, w1 = text_d(CINZEL, "CHÁCARA", 132, 0.02)
    name2, w2 = text_d(CINZEL, "IMPÉRIO", 132, 0.02)
    tag, wt = text_d(MONT, "EVENTOS & EXPERIÊNCIAS", 30, 0.30)
    mono = monogram(p)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000" role="img" aria-labelledby="t">
<title id="t">Chácara Império — Eventos &amp; Experiências</title>
<defs>{disc_defs(p)}</defs>
{disc(p)}
<g transform="translate(286 48) scale(.86)">{mono}</g>
<g fill="{CREAM}">{centered(name1, w1, 500, 618)}{centered(name2, w2, 500, 752)}</g>
<g fill="#e2d2a2">{centered(tag, wt, 500, 842)}</g>
</svg>'''
    return svg


def logo_mark():
    p = "lm-"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" role="img" aria-label="Chácara Império">
<defs>{disc_defs(p)}</defs>
{disc(p, 200, 200, 200)}
<g transform="translate(46 44) scale(.78)">{monogram(p)}</g>
</svg>'''


def logo_horizontal(color, tag_color, prefix):
    name, wn = text_d(CINZEL, "CHÁCARA IMPÉRIO", 64, 0.04)
    tag, wt = text_d(MONT, "EVENTOS & EXPERIÊNCIAS", 20.5, 0.30)
    x = 172
    width = x + max(wn, wt) + 8
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width:.0f} 150" role="img" aria-label="Chácara Império — Eventos &amp; Experiências">
<defs>{disc_defs(prefix)}</defs>
<g>{disc(prefix, 75, 75, 75)}<g transform="translate(18 17) scale(.29)">{monogram(prefix)}</g></g>
<g fill="{color}"><path transform="translate({x} 82)" d="{name}"/></g>
<g fill="{tag_color}"><path transform="translate({x + 2} 122)" d="{tag}"/></g>
</svg>'''


def main():
    out = {
        "logo-chacara-imperio.svg": logo_circle(),
        "logo-mark.svg": logo_mark(),
        "logo-horizontal-claro.svg": logo_horizontal(CREAM, "#e3cf98", "hc-"),
        "logo-horizontal-escuro.svg": logo_horizontal(GREEN_DARK, "#8a6a2e", "he-"),
    }
    for name, svg in out.items():
        with open(os.path.join(HERE, name), "w", encoding="utf-8") as f:
            f.write(svg)
        print(f"{name}: {len(svg) / 1024:.1f} KB")


if __name__ == "__main__":
    main()
