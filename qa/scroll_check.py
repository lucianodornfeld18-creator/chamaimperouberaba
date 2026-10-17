"""Rola a página como um usuário e fotografa a tela em alguns pontos (checa content-visibility)."""
import sys
from playwright.sync_api import sync_playwright
URL = sys.argv[1]
OUT = sys.argv[2]
with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome")
    pg = b.new_page(viewport={"width": 390, "height": 844}, is_mobile=True, has_touch=True, device_scale_factor=1)
    pg.goto(URL, wait_until="load")
    h = pg.evaluate("document.body.scrollHeight")
    shots = []
    for i, frac in enumerate((0.30, 0.55, 0.80)):
        pg.mouse.wheel(0, 0)
        pg.evaluate(f"window.scrollTo(0, {int(h * frac)})")
        pg.wait_for_timeout(700)
        path = f"{OUT}-{i}.png"
        pg.screenshot(path=path)
        shots.append(path)
    print(h, shots)
    b.close()
