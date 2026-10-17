"""Verificação completa do site gerado (site/dist).

Uso: python qa/qa_all.py      → imprime FAIL/WARN por página e um resumo; sai com código 1 se houver FAIL.
"""
import html
import json
import os
import re
import sys
from urllib.parse import unquote, urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, "site", "dist")
SITE = "https://chacaraimperiouberaba.com.br"
WA = "https://wa.me/5534991690139?text="
CASE_SENSITIVE = [r"\bTODO\b", r"\bXXX\b", r"\bFIXME\b"]
FORBIDDEN = [r"lorem", r"a melhor chácara", r"melhor chácara de Uberaba", r"R\$\s?\d",
             r"Alaska", r"n[ºo°]\s?1\b", r"\bnúmero 1\b"]

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def pages():
    for dp, _, fs in os.walk(DIST):
        for f in fs:
            if f.endswith(".html"):
                full = os.path.join(dp, f)
                rel = "/" + os.path.relpath(full, DIST).replace(os.sep, "/")
                path = rel[:-len("index.html")] if rel.endswith("/index.html") else rel
                yield path, full


def visible_text(doc):
    doc = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", doc, flags=re.S)
    doc = re.sub(r"<[^>]+>", " ", doc)
    return html.unescape(" ".join(doc.split()))


def exists(url_path):
    p = unquote(url_path.split("?")[0].split("#")[0])
    if p.endswith("/"):
        return os.path.exists(os.path.join(DIST, p.strip("/"), "index.html")) or p == "/"
    return os.path.exists(os.path.join(DIST, p.lstrip("/")))


def main():
    fails, warns = [], []
    titles, descs = {}, {}
    total_words = 0
    built = dict(pages())
    redirects = set()
    rpath = os.path.join(DIST, "_redirects")
    if os.path.exists(rpath):
        redirects = {line.split()[0] for line in open(rpath, encoding="utf-8") if line.strip()}
    for path, full in sorted(built.items()):
        doc = open(full, encoding="utf-8").read()
        F = lambda m: fails.append(f"{path}: {m}")  # noqa: E731
        Wn = lambda m: warns.append(f"{path}: {m}")  # noqa: E731
        t = re.search(r"<title>(.*?)</title>", doc, re.S)
        title = html.unescape(t.group(1)) if t else ""
        d = re.search(r'<meta name="description" content="([^"]*)"', doc)
        desc = html.unescape(d.group(1)) if d else ""
        if not title:
            F("sem <title>")
        elif len(title) > 65:
            F(f"título com {len(title)} caracteres")
        elif len(title) > 60:
            Wn(f"título com {len(title)} caracteres (Google corta ~60)")
        if not (110 <= len(desc) <= 165):
            (F if not desc else Wn)(f"description com {len(desc)} caracteres")
        if title in titles:
            F(f"título repetido com {titles[title]}")
        titles[title] = path
        if desc in descs:
            F(f"description repetida com {descs[desc]}")
        descs[desc] = path
        h1 = len(re.findall(r"<h1[\s>]", doc))
        if h1 != 1:
            F(f"{h1} tags h1")
        noindex = 'content="noindex' in doc
        canon = re.search(r'<link rel="canonical" href="([^"]+)"', doc)
        if not canon:
            F("sem canonical")
        elif not noindex and canon.group(1) != SITE + path:
            F(f"canonical {canon.group(1)} difere do caminho")
        for blob in re.findall(r'<script type="application/ld\+json">(.*?)</script>', doc, re.S):
            try:
                data = json.loads(blob)
                assert "@graph" in data
            except Exception as e:  # noqa: BLE001
                F(f"JSON-LD inválido: {e}")
        text = visible_text(doc)
        words = len(re.findall(r"\w+", text))
        total_words += words
        if re.search(r"\{[a-zA-Z_]|\}", text):
            F("sobra de template ({ ou }) no texto visível")
        for pat in FORBIDDEN:
            if re.search(pat, text, re.I):
                F(f"termo proibido: {pat}")
        for pat in CASE_SENSITIVE:
            if re.search(pat, text):
                F(f"marcador pendente: {pat}")
        for m in re.finditer(r'<img\b([^>]*)>', doc):
            attrs = m.group(1)
            if "alt=" not in attrs:
                F("imagem sem alt")
            if 'width="' not in attrs and 'src=""' not in attrs:
                Wn("imagem sem width/height")
            src = re.search(r'src="([^"]*)"', attrs)
            if src and src.group(1) and src.group(1).startswith("/") and not exists(src.group(1)):
                F(f"imagem inexistente {src.group(1)}")
        for href in re.findall(r'href="([^"]+)"', doc):
            h = html.unescape(href)
            if h.startswith("https://wa.me/"):
                if not h.startswith(WA):
                    F(f"link de WhatsApp com número errado: {h[:60]}")
                msg = unquote(h[len(WA):])
                if "pelo site" not in msg and "your website" not in msg:
                    F(f"mensagem de WhatsApp sem 'pelo site': {msg[:60]}")
            elif h.startswith("tel:") and h != "tel:+5534991690139":
                F(f"telefone errado: {h}")
            elif h.startswith("/") and not h.startswith("//"):
                base = h.split("#")[0]
                if base and not exists(base) and base.split("?")[0].rstrip("/") not in redirects:
                    F(f"link interno quebrado: {h}")
            elif h.startswith(SITE):
                pass
        for src in re.findall(r'(?:data-mp4|data-av1|data-mmp4|data-mav1|src)="(/video/[^"]+)"', doc):
            if not exists(src):
                F(f"vídeo inexistente {src}")
        if words < 250 and not noindex and path not in ("/politica-de-privacidade/",):
            Wn(f"pouco texto ({words} palavras)")
        print(f"{path:48s} {words:5d} palavras  título {len(title):2d}  desc {len(desc):3d}")
    sm = open(os.path.join(DIST, "sitemap.xml"), encoding="utf-8").read()
    for path, full in built.items():
        doc = open(full, encoding="utf-8").read()
        if 'content="noindex' not in doc and not path.endswith(".html"):
            if f"<loc>{SITE}{path}</loc>" not in sm:
                fails.append(f"{path}: fora do sitemap")
    for f in ("robots.txt", "llms.txt", "llms-full.txt", "_headers", "_redirects", "favicon.ico", "site.webmanifest"):
        if not os.path.exists(os.path.join(DIST, f)):
            fails.append(f"arquivo ausente: {f}")
    print(f"\n{len(built)} páginas · {total_words} palavras no total")
    for w in warns:
        print("WARN", w)
    for f in fails:
        print("FAIL", f)
    print(f"\n{len(fails)} FAIL · {len(warns)} WARN")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
