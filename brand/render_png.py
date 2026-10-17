"""Exporta os SVGs da logo em PNG (fundo transparente) com o Chromium do Playwright.

Uso: python brand/render_png.py
Saída: brand/png/*.png
"""
import os

from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "png")

JOBS = [
    ("logo-chacara-imperio.svg", [2048, 1024, 512, 256]),
    ("logo-mark.svg", [1024, 512, 192, 180, 64, 48, 32]),
    ("logo-horizontal-claro.svg", [900]),
    ("logo-horizontal-escuro.svg", [900]),
]


def main():
    os.makedirs(OUT, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        page = b.new_page()
        for name, sizes in JOBS:
            svg = open(os.path.join(HERE, name), encoding="utf-8").read()
            vb = [float(v) for v in svg.split('viewBox="')[1].split('"')[0].split()]
            ratio = vb[3] / vb[2]
            for w in sizes:
                h = round(w * ratio)
                page.set_viewport_size({"width": w, "height": h})
                page.set_content(f'<html><body style="margin:0;background:transparent">'
                                 f'<div style="width:{w}px;height:{h}px">{svg.replace("<svg ", f"<svg width=\"{w}\" height=\"{h}\" ", 1)}</div></body></html>')
                dest = os.path.join(OUT, f"{os.path.splitext(name)[0]}-{w}.png")
                page.screenshot(path=dest, omit_background=True, clip={"x": 0, "y": 0, "width": w, "height": h})
                print(dest)
        b.close()


if __name__ == "__main__":
    main()
