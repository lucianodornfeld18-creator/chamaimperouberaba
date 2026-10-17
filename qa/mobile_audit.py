"""Auditoria do site no celular (Chrome, telas de 360, 390 e 414 px).

Uso: python qa/mobile_audit.py [url_base]   (padrão: servidor local em site/dist)
Para cada página: rolagem lateral, elementos que passam da borda, texto < 12 px, alvos de toque
< 40 px, imagens quebradas e erros de console. Também testa menu, galeria e montador de mensagem.
Gera capturas de página inteira em qa/shots/mobile/ (360 px).
"""
import functools
import http.server
import os
import socketserver
import sys
import threading

from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, "site", "dist")
OUT = os.path.join(ROOT, "qa", "shots", "mobile")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

CHECK_JS = """() => {
  const vw = document.documentElement.clientWidth, out = {overflow: [], small: [], tap: [], broken: []};
  const seen = new Set();
  for (const el of document.querySelectorAll('main *, header *, footer *')) {
    const r = el.getBoundingClientRect(), cs = getComputedStyle(el);
    if (r.width === 0 || cs.visibility === 'hidden' || cs.display === 'none') continue;
    if (el.closest('.nav-panel, dialog, .visually-hidden, .skip')) continue;
    if (r.right > vw + 1 || r.left < -1) {
      const k = el.tagName + '.' + el.className;
      if (!seen.has(k) && !el.closest('.hero-media')) { seen.add(k); out.overflow.push(k + ' →' + Math.round(r.right)); }
    }
    const txt = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim().length > 1);
    if (txt && parseFloat(cs.fontSize) < 12) out.small.push(el.tagName + ' ' + cs.fontSize + ' "' + el.textContent.trim().slice(0, 30) + '"');
    if ((el.tagName === 'A' || el.tagName === 'BUTTON') && !el.closest('p, li, .crumbs, figcaption, td') && (r.height < 40 && r.width < 40)) out.tap.push(el.tagName + ' ' + Math.round(r.width) + 'x' + Math.round(r.height) + ' "' + el.textContent.trim().slice(0, 25) + '"');
  }
  for (const im of document.images) if (im.complete && im.naturalWidth === 0 && im.getAttribute('src')) out.broken.push(im.getAttribute('src'));
  out.sw = document.documentElement.scrollWidth; out.vw = vw;
  return out;
}"""


def serve():
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a, **k):
            pass
    handler = functools.partial(Quiet, directory=DIST)
    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.ThreadingTCPServer(("127.0.0.1", 8793), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


def pages():
    paths = []
    for dp, _, fs in os.walk(DIST):
        for f in fs:
            if f == "index.html":
                rel = "/" + os.path.relpath(dp, DIST).replace(os.sep, "/") + "/"
                paths.append("/" if rel == "/./" else rel)
    return sorted(paths)


def main():
    base = sys.argv[1] if len(sys.argv) > 1 else None
    httpd = None if base else serve()
    base = base or "http://127.0.0.1:8793"
    os.makedirs(OUT, exist_ok=True)
    problems = 0
    with sync_playwright() as p:
        b = p.chromium.launch(channel="chrome")
        for width in (360, 390, 414):
            ctx = b.new_context(viewport={"width": width, "height": 800}, device_scale_factor=2, is_mobile=True,
                                has_touch=True, locale="pt-BR")
            pg = ctx.new_page()
            errs = []
            pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
            pg.on("pageerror", lambda e: errs.append(str(e)))
            for path in pages():
                pg.goto(base + path, wait_until="load")
                pg.add_style_tag(content="main>section{content-visibility:visible!important}")
                pg.evaluate("async () => { for (let y = 0; y < document.body.scrollHeight; y += 600) { scrollTo(0, y); await new Promise(r => setTimeout(r, 40)); } scrollTo(0, 0); }")
                pg.wait_for_timeout(250)
                r = pg.evaluate(CHECK_JS)
                issues = []
                if r["sw"] > r["vw"]:
                    issues.append(f"rolagem lateral {r['sw']}>{r['vw']}")
                for k in ("overflow", "small", "tap", "broken"):
                    if r[k]:
                        issues.append(f"{k}: " + " | ".join(dict.fromkeys(r[k]))[:300])
                if errs:
                    issues.append("console: " + " | ".join(errs)[:200])
                    errs.clear()
                if issues:
                    problems += 1
                    print(f"[{width}] {path}\n    " + "\n    ".join(issues))
                if width == 360:
                    slug = path.strip("/").replace("/", "_") or "home"
                    pg.screenshot(path=os.path.join(OUT, f"{slug}.png"), full_page=True)
            if width == 390:  # interações
                pg.goto(base + "/", wait_until="load")
                pg.click("[data-nav-toggle]")
                print("menu abre:", pg.is_visible("#menu-celular"), "| aria-expanded:", pg.get_attribute("[data-nav-toggle]", "aria-expanded"))
                pg.screenshot(path=os.path.join(OUT, "_menu-aberto.png"))
                pg.goto(base + "/galeria/", wait_until="load")
                pg.click("[data-filter='suites']")
                vis = pg.evaluate("() => [...document.querySelectorAll('[data-gallery] a')].filter(a => !a.hidden).length")
                pg.click("[data-gallery] a:not([hidden])")
                pg.wait_for_timeout(400)
                print("galeria: filtro suítes mostra", vis, "fotos | visualizador aberto:", pg.evaluate("() => document.querySelector('[data-lightbox]').open"))
                pg.screenshot(path=os.path.join(OUT, "_galeria-aberta.png"))
                pg.goto(base + "/", wait_until="load")
                pg.select_option("#c-tipo", "Casamento")
                pg.fill("#c-pessoas", "120")
                pg.fill("#c-nome", "Teste")
                with pg.expect_popup() as pop:
                    pg.click("#consulta button[type=submit]")
                url = pop.value.url
                from urllib.parse import unquote
                print("montador do WhatsApp →", unquote(url)[:160])
            ctx.close()
        b.close()
    if httpd:
        httpd.shutdown()
    print(f"\n{problems} página(s)/tela(s) com apontamentos")


if __name__ == "__main__":
    main()
