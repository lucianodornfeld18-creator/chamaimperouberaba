"""Blocos reutilizáveis das páginas."""
import hashlib
import html
import json
import os

import _data as D
from _icons import icon
from _photos import PHOTOS

HERE = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(HERE, "static", "img")
_META = None
_HASH = {}


def esc(s):
    return html.escape(s, quote=True)


def meta():
    global _META
    if _META is None:
        with open(os.path.join(HERE, "_imgmeta.json"), encoding="utf-8") as f:
            _META = json.load(f)
    return _META


def ver(path_in_static):
    """Hash curto do arquivo (cache-busting de imagens com cache longo)."""
    if path_in_static not in _HASH:
        full = os.path.join(HERE, "static", path_in_static.replace("/", os.sep))
        with open(full, "rb") as f:
            _HASH[path_in_static] = hashlib.md5(f.read()).hexdigest()[:8]
    return _HASH[path_in_static]


def img_url(pid, width):
    slug = meta()[pid]["slug"]
    name = f"{slug}-{width}.webp"
    return f"/img/{name}?v={ver('img/' + name)}"


def og_url(pid):
    slug = meta()[pid]["slug"]
    return f"{D.SITE_URL}/og/{slug}.jpg"


def biggest(pid):
    v = meta()[pid]["variants"]
    w = max(int(k) for k in v)
    return w, v[str(w)][1]


def img(pid, sizes="100vw", cls="", eager=False, alt=None, priority=False):
    m = meta()[pid]
    p = PHOTOS[pid]
    widths = sorted(int(k) for k in m["variants"])
    srcset = ", ".join(f"{img_url(pid, w)} {w}w" for w in widths)
    default_w = 800 if 800 in widths else widths[len(widths) // 2]
    w, h = m["variants"][str(default_w)]
    fx, fy = p.get("focal", (50, 50))
    attrs = [
        f'src="{img_url(pid, default_w)}"', f'srcset="{srcset}"', f'sizes="{sizes}"',
        f'width="{w}" height="{h}"', f'alt="{esc(alt if alt is not None else p["alt"])}"',
        'loading="eager"' if eager else 'loading="lazy"', 'decoding="async"',
    ]
    if priority:
        attrs.append('fetchpriority="high"')
    if (fx, fy) != (50, 50):
        attrs.append(f'style="object-position:{fx}% {fy}%"')
    if cls:
        attrs.append(f'class="{cls}"')
    return "<img " + " ".join(attrs) + ">"


def figure(pid, caption=None, sizes="(min-width: 900px) 720px, 100vw", cls=""):
    cap = caption if caption is not None else PHOTOS[pid]["caption"]
    c = f' class="{cls}"' if cls else ""
    return f"<figure{c}>{img(pid, sizes)}<figcaption>{esc(cap)}</figcaption></figure>"


# ── Botões e links de contato ───────────────────────────────────────────

def btn_wa(label="Consultar data no WhatsApp", key="geral", cls="", text=None):
    href = esc(D.wa_url(key, text))
    c = f"btn btn-wa {cls}".strip()
    return (f'<a class="{c}" href="{href}" target="_blank" rel="noopener" '
            f'data-wa="{key}">{icon("whatsapp")}<span>{esc(label)}</span></a>')


def btn_tel(label=None, cls="btn-ghost"):
    label = label or f"Ligar: {D.PHONE_DISPLAY}"
    return f'<a class="btn {cls}" href="{D.TEL_URL}">{icon("phone")}<span>{esc(label)}</span></a>'


def wa_link(text_html, key="geral"):
    return f'<a href="{esc(D.wa_url(key))}" target="_blank" rel="noopener">{text_html}</a>'


def tel_link():
    return f'<a href="{D.TEL_URL}">{D.PHONE_DISPLAY}</a>'


def cta_row(key="geral", wa_label="Consultar data no WhatsApp", light=False):
    tel_cls = "btn-light" if light else "btn-ghost"
    return f'<div class="btn-row">{btn_wa(wa_label, key)}{btn_tel(cls=tel_cls)}</div>'


# ── Blocos de conteúdo ──────────────────────────────────────────────────

def section_head(eyebrow, title, text=None, center=False, tag="h2", hid=None):
    c = " center" if center else ""
    p = f"<p>{text}</p>" if text else ""
    idattr = f' id="{hid}"' if hid else ""
    return (f'<div class="section-head{c}"><p class="eyebrow">{esc(eyebrow)}</p>'
            f"<{tag}{idattr}>{title}</{tag}>{p}</div>")


def ornament():
    return f'<div class="ornament" aria-hidden="true">{icon("crown")}</div>'


def answer(text_html, label="Resposta rápida"):
    """Bloco de resposta direta no topo (AEO): 40–70 palavras, factual."""
    return f'<div class="answer"><span class="answer-label">{esc(label)}</span><p>{text_html}</p></div>'


FACT_ITEMS = [
    ("event_capacity", "convidados em eventos"),
    ("lodging_capacity", "hóspedes para dormir"),
    ("suites", "suítes"),
    ("bathrooms", "banheiros"),
    ("area_m2", "m² de área"),
    ("parking", "vagas de estacionamento"),
]


def fmt_num(n):
    return f"{n:,}".replace(",", ".")


def facts_grid():
    items = "".join(
        f'<div class="fact" role="listitem"><span class="fact-num">{fmt_num(D.FACTS[k])}</span>'
        f'<span class="fact-label">{label}</span></div>' for k, label in FACT_ITEMS)
    return f'<div class="facts" role="list" aria-label="A chácara em números">{items}</div>'


def checks(items):
    lis = "".join(f"<li>{icon('check')}<span>{it}</span></li>" for it in items)
    return f'<ul class="checks">{lis}</ul>'


def features(items, cols3=False):
    c = " cols-3" if cols3 else ""
    lis = "".join(f"<li>{icon(ic)}<span>{txt}</span></li>" for ic, txt in items)
    return f'<ul class="features{c}">{lis}</ul>'


def tiles(items, cols="grid-3"):
    out = []
    for ic, title, text in items:
        out.append(f'<div class="tile"><span class="tile-icon">{icon(ic)}</span>'
                   f"<h3>{title}</h3><p>{text}</p></div>")
    return f'<div class="grid {cols}">{"".join(out)}</div>'


def card_link(href, pid, title, text, tag=None, sizes="(min-width: 960px) 360px, (min-width: 640px) 50vw, 100vw"):
    t = f'<span class="card-tag">{esc(tag)}</span>' if tag else ""
    return (f'<a class="card" href="{href}"><div class="card-media">{img(pid, sizes)}</div>'
            f'<div class="card-body">{t}<h3>{title}</h3><p>{text}</p>'
            f'<span class="link-arrow">Ver detalhes {icon("arrow")}</span></div></a>')


def steps(items, vertical=False):
    lis = "".join(f"<li><h3>{t}</h3><p>{d}</p></li>" for t, d in items)
    c = "steps vertical" if vertical else "steps"
    return f'<ol class="{c}">{lis}</ol>'


def faq_html(items, heading=None, hid="perguntas"):
    """items: lista de (pergunta, resposta_html). O schema FAQPage sai do layout."""
    h = f'<h2 id="{hid}">{heading}</h2>' if heading else ""
    det = "".join(
        f'<details><summary>{esc(q)}</summary><div class="faq-a"><p>{a}</p></div></details>'
        for q, a in items)
    return f'{h}<div class="faq">{det}</div>'


def cta_band(title="Vamos conversar sobre a sua data?", text=None, key="geral",
             wa_label="Chamar no WhatsApp"):
    text = text or ("As reservas são feitas direto com a gente, por telefone ou WhatsApp. "
                    "Conte a data, o tipo de evento ou estadia e quantas pessoas — "
                    "respondemos com disponibilidade e valores.")
    return (f'<div class="cta-band">{ornament_left()}<h2>{title}</h2><p>{text}</p>'
            f'<div class="btn-row">{btn_wa(wa_label, key)}{btn_tel(cls="btn-ghost")}</div>'
            f'<p class="cta-meta">WhatsApp e telefone: {D.PHONE_DISPLAY} · {esc(D.CITY)} – {D.STATE}</p></div>')


def ornament_left():
    return f'<p class="eyebrow">{esc(D.NAME)} · {esc(D.CITY)}</p>'


def crumbs_html(trail):
    """trail: [(nome, url), ...] incluindo a página atual por último (sem link)."""
    lis = []
    for i, (name, url) in enumerate(trail):
        if i == len(trail) - 1:
            lis.append(f'<li aria-current="page">{esc(name)}</li>')
        else:
            lis.append(f'<li><a href="{url}">{esc(name)}</a></li>')
    return f'<nav class="crumbs" aria-label="Você está em"><ol>{"".join(lis)}</ol></nav>'


def mosaic(pids, sizes_first="(min-width: 860px) 50vw, 50vw"):
    out = []
    for i, pid in enumerate(pids):
        sizes = sizes_first if i == 0 else "(min-width: 860px) 25vw, 50vw"
        out.append(f'<a href="/galeria/#foto-{pid}" aria-label="{esc(PHOTOS[pid]["caption"])} — abrir na galeria">'
                   f"{img(pid, sizes)}</a>")
    return f'<div class="mosaic">{"".join(out)}</div>'


def distances_table(limit=None):
    rows = D.DISTANCES if limit is None else D.DISTANCES[:limit]
    trs = "".join(f"<tr><td>{esc(c)}</td><td>cerca de {km} km</td></tr>" for c, km in rows)
    return ('<table class="table"><caption class="visually-hidden">Distâncias rodoviárias até Uberaba</caption>'
            '<thead><tr><th scope="col">Saindo de</th><th scope="col">Até Uberaba</th></tr></thead>'
            f"<tbody>{trs}</tbody></table>")


def composer(default_type=None):
    """Formulário que só monta a mensagem e abre o WhatsApp (nada é enviado ao site)."""
    opts = ["Casamento", "Aniversário / 15 anos", "Confraternização de empresa", "Reunião de família",
            "Natal ou Réveillon", "Ensaio fotográfico", "Hospedagem (fim de semana / feriado)",
            "Hospedagem na Expozebu", "Outro evento"]
    matched = default_type in opts
    options = "" if matched else '<option value="" selected>Escolha uma opção</option>'
    options += "".join(
        f'<option{" selected" if o == default_type else ""}>{esc(o)}</option>' for o in opts)
    return f'''<form class="composer" id="consulta" data-composer data-wa="{D.WHATSAPP}" novalidate>
<h3>Monte sua consulta</h3>
<p class="hint">Preencha o que já souber. O botão abre o WhatsApp com a mensagem pronta — é só enviar.</p>
<div class="field"><label for="c-tipo">O que você está planejando?</label><select id="c-tipo" name="tipo">{options}</select></div>
<div class="field-row">
<div class="field"><label for="c-data">Data desejada</label><input id="c-data" name="data" type="date"></div>
<div class="field"><label for="c-pessoas">Número de pessoas</label><input id="c-pessoas" name="pessoas" type="number" min="1" max="400" inputmode="numeric" placeholder="ex.: 80"></div>
</div>
<div class="field"><label for="c-nome">Seu nome</label><input id="c-nome" name="nome" type="text" autocomplete="given-name" placeholder="Como podemos te chamar?"></div>
<button class="btn btn-wa" type="submit">{icon("whatsapp")}<span>Enviar consulta pelo WhatsApp</span></button>
<p class="hint mt-1">Prefere ligar? {tel_link()}</p>
</form>'''


def article_schema(path, headline, description, hero, published, modified=None):
    """BlogPosting publicado pela própria chácara (sem autor inventado)."""
    url = D.SITE_URL + path
    return {
        "@type": "BlogPosting", "@id": url + "#artigo", "headline": headline, "description": description,
        "url": url, "mainEntityOfPage": {"@id": url + "#pagina"}, "inLanguage": "pt-BR",
        "image": og_url(hero), "datePublished": published, "dateModified": modified or published,
        "author": {"@id": D.SITE_URL + "/#negocio"}, "publisher": {"@id": D.SITE_URL + "/#negocio"},
    }


def toc(items):
    """items: [(id, título)] — sumário no topo de artigos longos."""
    lis = "".join(f'<li><a href="#{i}">{esc(t)}</a></li>' for i, t in items)
    return f'<nav class="toc" aria-label="Neste guia"><strong>Neste guia</strong><ol>{lis}</ol></nav>'


def related(links):
    """links: [(href, pid, título, texto)] — 3 cartões de leitura relacionada."""
    cards = "".join(card_link(h, pid, t, x) for h, pid, t, x in links)
    return f'<div class="grid grid-3">{cards}</div>'
