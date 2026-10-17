"""Capturas de tela das páginas (Playwright, Chromium headless).

Uso: python qa/shot.py / /eventos/ ...   (padrão: /)
Gera qa/shots/<nome>-mobile.png e -desktop.png. Sobe um servidor local na porta 8791.
Opções: --full (página inteira), --only=mobile|desktop
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
OUT = os.path.join(ROOT, "qa", "shots")
PORT = 8791


def serve():
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a, **k):
            pass
    handler = functools.partial(Quiet, directory=DIST)
    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.ThreadingTCPServer(("127.0.0.1", PORT), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    full = "--full" in sys.argv
    only = next((a.split("=")[1] for a in sys.argv if a.startswith("--only=")), None)
    paths = args or ["/"]
    os.makedirs(OUT, exist_ok=True)
    httpd = serve()
    sizes = {"mobile": (390, 844), "desktop": (1440, 900)}
    with sync_playwright() as p:
        b = p.chromium.launch()
        for name, (w, h) in sizes.items():
            if only and only != name:
                continue
            ctx = b.new_context(viewport={"width": w, "height": h}, device_scale_factor=1,
                                reduced_motion="reduce", is_mobile=(name == "mobile"), has_touch=(name == "mobile"))
            page = ctx.new_page()
            errors = []
            page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
            page.on("pageerror", lambda e: errors.append(str(e)))
            for path in paths:
                page.goto(f"http://127.0.0.1:{PORT}{path}", wait_until="networkidle")
                if full:  # rola até o fim para carregar as imagens com loading=lazy
                    page.evaluate("""async () => { for (let y = 0; y < document.body.scrollHeight; y += 500) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 60)); } window.scrollTo(0, 0); }""")
                    page.wait_for_load_state("networkidle")
                page.wait_for_timeout(300)
                slug = path.strip("/").replace("/", "_") or "home"
                dest = os.path.join(OUT, f"{slug}-{name}.png")
                page.screenshot(path=dest, full_page=full)
                sw = page.evaluate("document.documentElement.scrollWidth")
                print(f"{dest}  scrollWidth={sw} (viewport {w})" + ("  ERROS: " + " | ".join(errors) if errors else ""))
                errors.clear()
            ctx.close()
        b.close()
    httpd.shutdown()


if __name__ == "__main__":
    main()
