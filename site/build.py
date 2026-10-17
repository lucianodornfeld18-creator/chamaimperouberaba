"""Gera o site estático da Chácara Império em site/dist.

Uso (na pasta do projeto):  python site/build.py
Pré-requisito: python images/process_photos.py (gera site/static/img, og e _imgmeta.json)
Vídeo (opcional): python video/make_tour.py (gera site/static/video)

Sem dependências além da biblioteca padrão (Pillow só para os ícones).
"""
import hashlib
import importlib.util
import json
import os
import re
import shutil
import sys
from xml.sax.saxutils import escape as xesc

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import _data as D  # noqa: E402
import _layout as L  # noqa: E402
from _components import img_url, meta, og_url  # noqa: E402
from _photos import PHOTOS  # noqa: E402

DIST = os.path.join(HERE, "dist")
STATIC = os.path.join(HERE, "static")
PAGES_DIR = os.path.join(HERE, "pages")
INDEXNOW_KEY = "fdea639fc0c676b18e646e034a12bd60"

AI_BOTS = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User",
           "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot", "Applebot-Extended",
           "Bingbot", "DuckAssistBot", "Meta-ExternalAgent", "MistralAI-User", "CCBot", "YouBot"]


def minify_css(css):
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\s+", " ", css)
    css = re.sub(r"\s*([{};,>])\s*", r"\1", css)
    css = css.replace(";}", "}")
    return css.strip()


def short_hash(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()[:8]


def load_pages():
    pages = []
    for name in sorted(os.listdir(PAGES_DIR)):
        if not name.endswith(".py") or name.startswith("_"):
            continue
        spec = importlib.util.spec_from_file_location(f"pages.{name[:-3]}", os.path.join(PAGES_DIR, name))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        found = getattr(mod, "PAGES", None) or [getattr(mod, "PAGE")]
        for p in found:
            req = p.get("requires")
            if req and not all(getattr(D, r, None) for r in req):
                print(f"  (pulada até ter dados: {p['path']} precisa de {req})")
                continue
            p.setdefault("module", name)
            pages.append(p)
    return pages


def write(path, content, mode="w"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, mode, encoding=None if "b" in mode else "utf-8", newline=None if "b" in mode else "\n") as f:
        f.write(content)


def out_path(page_path):
    if page_path.endswith(".html"):
        return os.path.join(DIST, page_path.lstrip("/"))
    return os.path.join(DIST, page_path.strip("/"), "index.html") if page_path != "/" else os.path.join(DIST, "index.html")


def copy_static():
    for sub, dest in (("fonts", "assets/fonts"), ("img", "img"), ("og", "og"), ("video", "video")):
        src = os.path.join(STATIC, sub)
        if os.path.isdir(src):
            shutil.copytree(src, os.path.join(DIST, dest), dirs_exist_ok=True,
                            ignore=shutil.ignore_patterns("src", "*.css", "*.duration"))
    brand_src = os.path.join(os.path.dirname(HERE), "brand")  # logo vetorial (brand/make_logo.py)
    os.makedirs(os.path.join(DIST, "brand"), exist_ok=True)
    for name in ("logo-chacara-imperio.svg", "logo-mark.svg", "logo-horizontal-claro.svg", "logo-horizontal-escuro.svg"):
        shutil.copy(os.path.join(brand_src, name), os.path.join(DIST, "brand", name))
    for name in ("logo-chacara-imperio-512.png", "logo-chacara-imperio-1024.png"):
        shutil.copy(os.path.join(brand_src, "png", name), os.path.join(DIST, "brand", name))
    js_src = os.path.join(STATIC, "js", "site.js")
    os.makedirs(os.path.join(DIST, "assets"), exist_ok=True)
    shutil.copy(js_src, os.path.join(DIST, "assets", "site.js"))
    L.JS_URL = f"/assets/site.js?v={short_hash(js_src)}"
    with open(os.path.join(STATIC, "css", "site.css"), encoding="utf-8") as f:
        L.CSS = minify_css(f.read())


def make_icons():
    """Ícones a partir do monograma da logo (brand/png/logo-mark-*.png)."""
    from PIL import Image
    png = os.path.join(os.path.dirname(HERE), "brand", "png")
    shutil.copy(os.path.join(os.path.dirname(HERE), "brand", "logo-mark.svg"), os.path.join(DIST, "favicon.svg"))
    mark = Image.open(os.path.join(png, "logo-mark-1024.png")).convert("RGBA")

    def on_bg(size, pad):
        bg = Image.new("RGBA", (size, size), (18, 42, 30, 255))
        m = mark.resize((size - 2 * pad, size - 2 * pad), Image.LANCZOS)
        bg.alpha_composite(m, (pad, pad))
        return bg

    on_bg(180, 10).convert("RGB").save(os.path.join(DIST, "apple-touch-icon.png"))
    mark.resize((192, 192), Image.LANCZOS).save(os.path.join(DIST, "icon-192.png"))
    mark.resize((512, 512), Image.LANCZOS).save(os.path.join(DIST, "icon-512.png"))
    mark.resize((64, 64), Image.LANCZOS).save(os.path.join(DIST, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])
    manifest = {"name": D.NAME, "short_name": "Império", "start_url": "/", "display": "browser",
                "background_color": "#fbf7f0", "theme_color": "#163627", "lang": "pt-BR",
                "icons": [{"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"},
                          {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"}]}
    write(os.path.join(DIST, "site.webmanifest"), json.dumps(manifest, ensure_ascii=False, indent=1))


def sitemap(pages):
    rows = []
    for p in sorted(pages, key=lambda x: (x["path"] != "/", x["path"])):
        if p.get("noindex") or p["path"].endswith(".html"):
            continue
        imgs = []
        for pid in [p.get("hero")] + list(p.get("sitemap_images", [])):
            if pid and pid in PHOTOS:
                w = max(int(k) for k in meta()[pid]["variants"])
                loc = D.SITE_URL + img_url(pid, w).split("?")[0]
                imgs.append(f"<image:image><image:loc>{xesc(loc)}</image:loc></image:image>")
        rows.append(f"<url><loc>{xesc(D.SITE_URL + p['path'])}</loc><lastmod>{p.get('updated', D.UPDATED)}</lastmod>"
                    + "".join(imgs) + "</url>")
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
           'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n' + "\n".join(rows) + "\n</urlset>\n")
    write(os.path.join(DIST, "sitemap.xml"), xml)
    return len(rows)


def robots():
    lines = ["# Chácara Império — buscadores e assistentes de IA são bem-vindos", "User-agent: *", "Allow: /", ""]
    for bot in AI_BOTS:
        lines += [f"User-agent: {bot}", "Allow: /", ""]
    lines += [f"Sitemap: {D.SITE_URL}/sitemap.xml", ""]
    write(os.path.join(DIST, "robots.txt"), "\n".join(lines))


def llms(pages):
    f = D.FACTS
    summary = L.ENTITY_DESCRIPTION
    key_facts = [
        f"Nome: {D.NAME} (Uberaba – MG, Brasil)",
        f"Tipo: chácara para eventos e hospedagem (locação da chácara inteira)",
        f"Eventos: até {f['event_capacity']} convidados — casamentos, aniversários e 15 anos, confraternizações de empresa, reuniões de família, Natal e Réveillon, ensaios fotográficos",
        f"Hospedagem: até {f['lodging_capacity']} pessoas, {f['suites']} suítes, {f['beds']} camas, {f['bathrooms']} banheiros, ar-condicionado nas suítes",
        f"Área: {f['area_m2']:,} m²; estacionamento para {f['parking']} carros".replace(",", "."),
        "Lazer: piscina adulto e piscina infantil, campo de futebol, parquinho, jardins com pérgolas",
        "Área gourmet: churrasqueira, fogão a lenha, salão coberto, varandas, cozinha equipada",
        "Localização: dentro do perímetro urbano de Uberaba, acesso asfaltado, portão eletrônico, câmeras externas",
        f"Check-in a partir das {f['checkin']}; check-out até as {f['checkout']}",
        "Aceita animais de estimação; fotografia comercial permitida; aceita contrato de locação temporária para empresas",
        f"Anfitriões: {D.HOSTS_PHRASE}",
        f"Reservas: somente por telefone ou WhatsApp {D.PHONE_DISPLAY} (+55 34 99169-0139)",
        f"Instagram: {D.INSTAGRAM}",
        f"Airbnb: {D.AIRBNB}",
        f"Site oficial: {D.SITE_URL}/",
    ]
    main_paths = ["/", "/eventos/", "/eventos/casamento/", "/eventos/aniversario/", "/eventos/confraternizacao-de-empresa/",
                  "/eventos/reuniao-de-familia/", "/eventos/natal-e-reveillon/", "/eventos/ensaio-fotografico/",
                  "/hospedagem/", "/hospedagem/expozebu/", "/estrutura/", "/galeria/", "/tour-em-video/", "/sobre/",
                  "/como-chegar/", "/perguntas-frequentes/", "/reservas/"]
    by_path = {p["path"]: p for p in pages}
    main = [by_path[x] for x in main_paths if x in by_path]
    others = [p for p in pages if p["path"] not in main_paths and not p.get("noindex") and not p["path"].endswith(".html")]
    out = [f"# {D.NAME}", "", f"> {summary}", "", "## Fatos principais", ""]
    out += [f"- {k}" for k in key_facts]
    out += ["", "## Páginas principais", ""]
    out += [f"- [{p['title']}]({D.SITE_URL}{p['path']}): {p['description']}" for p in main]
    out += ["", "## Guias e outras páginas", ""]
    out += [f"- [{p['title']}]({D.SITE_URL}{p['path']}): {p['description']}" for p in others]
    out += ["", f"Atualizado em {D.UPDATED_HUMAN}. Valores e disponibilidade: consultar pelo WhatsApp {D.PHONE_DISPLAY}.", ""]
    write(os.path.join(DIST, "llms.txt"), "\n".join(out))

    full = [f"# {D.NAME} — informações completas", "", summary, "", "## Fatos", ""]
    full += [f"- {k}" for k in key_facts]
    full += ["", "## Distâncias rodoviárias até Uberaba (aproximadas)", ""]
    full += [f"- {c}: cerca de {km} km" for c, km in D.DISTANCES]
    for p in pages:
        if p.get("faq") and not p.get("noindex"):
            full += ["", f"## Perguntas e respostas — {p['title']}", f"Fonte: {D.SITE_URL}{p['path']}", ""]
            for q, a in p["faq"]:
                full += [f"P: {q}", f"R: {L.strip_tags(a)}", ""]
    write(os.path.join(DIST, "llms-full.txt"), "\n".join(full))


def headers_and_redirects():
    csp = ("default-src 'self'; img-src 'self' data:; media-src 'self'; style-src 'self' 'unsafe-inline'; "
           "script-src 'self' https://static.cloudflareinsights.com; connect-src 'self' https://cloudflareinsights.com; "
           "font-src 'self'; frame-src https://www.google.com https://maps.google.com; base-uri 'self'; "
           "form-action 'self'; frame-ancestors 'self'; object-src 'none'")
    h = f"""/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=()
  X-Frame-Options: SAMEORIGIN
  Strict-Transport-Security: max-age=31536000
  Content-Security-Policy: {csp}

/assets/*
  Cache-Control: public, max-age=31536000, immutable

/img/*
  Cache-Control: public, max-age=31536000, immutable

/brand/*
  Cache-Control: public, max-age=86400

/og/*
  Cache-Control: public, max-age=86400

/video/*
  Cache-Control: public, max-age=604800
"""
    write(os.path.join(DIST, "_headers"), h)
    wa = D.wa_url("geral")
    r = f"""/index.html / 301
/contato /reservas/ 301
/contato/ /reservas/ 301
/reserva /reservas/ 301
/reservar /reservas/ 301
/fotos /galeria/ 301
/fotos/ /galeria/ 301
/faq /perguntas-frequentes/ 301
/duvidas /perguntas-frequentes/ 301
/localizacao /como-chegar/ 301
/casamento /eventos/casamento/ 301
/casamentos /eventos/casamento/ 301
/aniversario /eventos/aniversario/ 301
/15-anos /eventos/aniversario/ 301
/empresas /eventos/confraternizacao-de-empresa/ 301
/reveillon /eventos/natal-e-reveillon/ 301
/expozebu /hospedagem/expozebu/ 301
/video /tour-em-video/ 301
/tour /tour-em-video/ 301
/sobre-nos /sobre/ 301
/quem-somos /sobre/ 301
/whatsapp {wa} 302
"""
    write(os.path.join(DIST, "_redirects"), r)
    routes = {"version": 1, "include": ["/*"], "exclude": ["/assets/*", "/img/*", "/og/*", "/video/*"]}
    write(os.path.join(DIST, "_routes.json"), json.dumps(routes))
    write(os.path.join(DIST, f"{INDEXNOW_KEY}.txt"), INDEXNOW_KEY)


def main():
    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)
    copy_static()
    pages = load_pages()
    for p in pages:  # páginas que dependem das outras (ex.: índice do guia)
        if callable(p.get("render_body")):
            p["body"] = p["render_body"](pages)
    seen_paths, seen_titles = set(), {}
    for p in pages:
        assert p["path"] not in seen_paths, f"caminho repetido: {p['path']}"
        seen_paths.add(p["path"])
        if p["title"] in seen_titles:
            raise SystemExit(f"título repetido: {p['title']} ({p['path']} e {seen_titles[p['title']]})")
        seen_titles[p["title"]] = p["path"]
        write(out_path(p["path"]), L.render(p))
    make_icons()
    n = sitemap(pages)
    robots()
    llms(pages)
    headers_and_redirects()
    total = sum(os.path.getsize(os.path.join(dp, f)) for dp, _, fs in os.walk(DIST) for f in fs)
    print(f"{len(pages)} páginas ({n} no sitemap) → {DIST}  [{total/1024/1024:.1f} MB]")


if __name__ == "__main__":
    main()
