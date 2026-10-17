"""Confere a prévia no ar com o Google Chrome instalado: vídeo do topo tocando e link do WhatsApp."""
import sys
from urllib.parse import unquote
from playwright.sync_api import sync_playwright

BASE = sys.argv[1] if len(sys.argv) > 1 else "https://chacaraimperiouberaba.pages.dev"
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
with sync_playwright() as p:
    try:
        b = p.chromium.launch(channel="chrome")
    except Exception:
        b = p.chromium.launch()
        print("(Chrome não encontrado; usando Chromium do Playwright — sem H.264)")
    pg = b.new_page(viewport={"width": 1440, "height": 900})
    errors = []
    pg.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
    pg.goto(BASE + "/", wait_until="load")
    pg.wait_for_timeout(4000)
    state = pg.evaluate("""() => { const v = document.querySelector('[data-hero-video]');
        return v ? {playing: v.classList.contains('is-playing'), t: v.currentTime, src: v.currentSrc, err: v.error && v.error.code} : null }""")
    print("vídeo do topo:", state)
    href = pg.get_attribute("a.btn-wa", "href")
    print("WhatsApp:", unquote(href))
    pg.goto(BASE + "/tour-em-video/", wait_until="load")
    dur = pg.evaluate("() => new Promise(r => { const v = document.querySelector('video'); if (v.readyState >= 1) r(v.duration); else v.addEventListener('loadedmetadata', () => r(v.duration)); setTimeout(() => r(-1), 8000); })")
    print("tour: duração", dur)
    print("erros de console:", errors or "nenhum")
    b.close()
