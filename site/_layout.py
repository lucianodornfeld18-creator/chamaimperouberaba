"""Casca HTML de todas as páginas: <head>, schema.org, cabeçalho, hero, rodapé."""
import json

import _data as D
from _components import (btn_tel, btn_wa, crumbs_html, esc, img, img_url, meta, og_url)
from _icons import icon
from _photos import PHOTOS

ENTITY_DESCRIPTION = (
    "A Chácara Império é uma chácara para eventos e hospedagem em Uberaba (MG), dentro do "
    "perímetro urbano e com acesso asfaltado. São 2.500 m² com piscina adulto e infantil, "
    "área gourmet com churrasqueira e fogão a lenha, salão coberto, campo de futebol, parquinho "
    "e estacionamento para 40 carros. Recebe eventos de até 250 convidados e hospeda até 40 "
    "pessoas em 6 suítes. Reservas por telefone ou WhatsApp: (34) 99169-0139."
)

CSS = ""        # preenchido pelo build (CSS minificado)
JS_URL = ""     # preenchido pelo build (/assets/site.js?v=hash)


def abs_url(path):
    return D.SITE_URL + path


# ── schema.org ──────────────────────────────────────────────────────────

def business_node():
    amen = [
        "Piscina adulto", "Piscina infantil", "Área gourmet", "Churrasqueira", "Fogão a lenha",
        "Salão coberto para festas", "Campo de futebol", "Parquinho infantil", "Ar-condicionado nas suítes",
        "Wi-Fi", "Cozinha equipada", "Chuveiro externo", "Estacionamento gratuito no local (40 vagas)",
        "Portão eletrônico", "Câmeras de segurança externas", "Aceita animais de estimação",
    ]
    node = {
        "@type": ["LodgingBusiness", "EventVenue"],
        "@id": abs_url("/#negocio"),
        "name": D.NAME,
        "alternateName": D.ALT_NAMES,
        "description": ENTITY_DESCRIPTION,
        "slogan": "Um espaço exclusivo para eventos memoráveis",
        "url": abs_url("/"),
        "telephone": "+55 34 99169-0139",
        "image": [og_url("piscina-banco"), og_url("piscinas-vista"), og_url("salao"),
                  og_url("gourmet-noite"), og_url("suite-1")],
        "logo": abs_url("/brand/logo-chacara-imperio-512.png"),
        "address": {"@type": "PostalAddress", "addressLocality": D.CITY,
                    "addressRegion": D.STATE, "addressCountry": D.COUNTRY},
        "areaServed": [
            {"@type": "City", "name": "Uberaba"},
            {"@type": "AdministrativeArea", "name": "Triângulo Mineiro"},
        ],
        "sameAs": [D.INSTAGRAM, D.AIRBNB],
        "maximumAttendeeCapacity": D.FACTS["event_capacity"],
        "numberOfRooms": D.FACTS["suites"],
        "petsAllowed": True,
        "checkinTime": D.FACTS["checkin"],
        "checkoutTime": D.FACTS["checkout"],
        "amenityFeature": [{"@type": "LocationFeatureSpecification", "name": a, "value": True} for a in amen],
        "additionalProperty": [
            {"@type": "PropertyValue", "name": "Área total", "value": D.FACTS["area_m2"], "unitCode": "MTK"},
            {"@type": "PropertyValue", "name": "Hóspedes (pernoite)", "value": D.FACTS["lodging_capacity"]},
            {"@type": "PropertyValue", "name": "Camas", "value": D.FACTS["beds"]},
            {"@type": "PropertyValue", "name": "Banheiros", "value": D.FACTS["bathrooms"]},
            {"@type": "PropertyValue", "name": "Vagas de estacionamento", "value": D.FACTS["parking"]},
        ],
        "contactPoint": {"@type": "ContactPoint", "telephone": "+55 34 99169-0139",
                         "contactType": "reservations", "availableLanguage": ["Portuguese"],
                         "areaServed": "BR"},
        "knowsLanguage": "pt-BR",
        "makesOffer": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Locação da chácara para eventos",
                                               "description": "Casamentos, aniversários, 15 anos, confraternizações de empresa e reuniões de família para até 250 convidados."}},
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Hospedagem para grupos",
                                               "description": "Chácara inteira para até 40 hóspedes em 6 suítes, para fins de semana, feriados e temporadas."}},
        ],
    }
    if D.ADDRESS:
        node["address"].update({"streetAddress": D.ADDRESS["street"], "postalCode": D.ADDRESS["postal_code"]})
    if D.GEO:
        node["geo"] = {"@type": "GeoCoordinates", "latitude": D.GEO[0], "longitude": D.GEO[1]}
    if D.MAPS_URL:
        node["hasMap"] = D.MAPS_URL
    if D.GOOGLE_BUSINESS:
        node["sameAs"].append(D.GOOGLE_BUSINESS)
    return node


def graph(page):
    url = abs_url(page["path"])
    nodes = [
        {"@type": "WebSite", "@id": abs_url("/#site"), "url": abs_url("/"), "name": D.NAME,
         "inLanguage": "pt-BR", "publisher": {"@id": abs_url("/#negocio")}},
        business_node(),
    ]
    wp = {
        "@type": page.get("page_type", "WebPage"),
        "@id": url + "#pagina",
        "url": url,
        "name": page["title"],
        "description": page["description"],
        "inLanguage": page.get("lang", "pt-BR"),
        "isPartOf": {"@id": abs_url("/#site")},
        "about": {"@id": abs_url("/#negocio")},
        "dateModified": page.get("updated", D.UPDATED),
    }
    if page.get("hero"):
        wp["primaryImageOfPage"] = {"@type": "ImageObject", "url": og_url(page["hero"]),
                                    "width": 1200, "height": 630}
    trail = page.get("crumbs")
    if trail and len(trail) > 1:
        wp["breadcrumb"] = {"@id": url + "#trilha"}
        nodes.append({"@type": "BreadcrumbList", "@id": url + "#trilha", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": abs_url(u)}
            for i, (n, u) in enumerate(trail)]})
    if page.get("faq"):
        faq = {"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in page["faq"]]}
        if wp["@type"] == "FAQPage":
            wp["mainEntity"] = faq["mainEntity"]
        else:
            nodes.append(faq)
    nodes.insert(0, wp)
    nodes.extend(page.get("schema", []))
    return {"@context": "https://schema.org", "@graph": nodes}


def strip_tags(s):
    import re
    s = re.sub(r"<[^>]+>", "", s)
    return " ".join(s.split())


# ── Partes visuais ──────────────────────────────────────────────────────

def header(page):
    overlay = page.get("hero_kind") == "home"
    links = []
    for name, href in D.NAV:
        cur = ' aria-current="page"' if page["path"].startswith(href) else ""
        links.append(f'<a href="{href}"{cur}>{esc(name)}</a>')
    nav = "".join(links)
    cls = "site-header is-overlay" if overlay else "site-header"
    return f'''<header class="{cls}" data-header>
<div class="wrap header-inner">
<a class="brand" href="/"><img class="brand-logo" src="/brand/logo-horizontal-{"claro" if overlay else "escuro"}.svg" alt="Chácara Império — Eventos &amp; Experiências, Uberaba (MG)" width="288" height="50"></a>
<nav class="nav" aria-label="Menu principal">{nav}</nav>
{btn_wa("Reservar", page.get("wa_key", "geral"), cls="btn-sm header-cta")}
<button class="nav-toggle" type="button" aria-expanded="false" aria-controls="menu-celular" aria-label="Abrir menu" data-nav-toggle>{icon("menu")}</button>
</div>
<div class="nav-panel" id="menu-celular"><nav aria-label="Menu">{nav}<a href="/reservas/">Como reservar</a><a href="/guia/">Guia e dicas</a></nav>{btn_wa("Consultar data no WhatsApp", page.get("wa_key", "geral"))}</div>
</header>'''


def page_hero(page):
    pid = page.get("hero")
    trail = page.get("crumbs") or []
    crumbs = crumbs_html(trail) if len(trail) > 1 else ""
    lead = f'<p class="lead">{page["lead"]}</p>' if page.get("lead") else ""
    eyebrow = f'<p class="eyebrow">{esc(page["eyebrow"])}</p>' if page.get("eyebrow") else ""
    ctas = page.get("hero_ctas")
    if ctas is None:
        ctas = (f'<div class="btn-row">{btn_wa(page.get("wa_label", "Consultar data no WhatsApp"), page.get("wa_key", "geral"))}'
                f'{btn_tel(cls="btn-light")}</div>')
    media = (f'<div class="hero-media">{img(pid, "100vw", eager=True, priority=True, alt="")}</div>'
             if pid else "")
    return f'''<section class="hero hero--page">{media}<div class="hero-shade"></div>
<div class="wrap hero-content">{crumbs}{eyebrow}<h1>{page["h1"]}</h1>{lead}{ctas}</div></section>'''


def footer(page):
    a_chacara = [("Eventos", "/eventos/"), ("Hospedagem", "/hospedagem/"), ("Estrutura", "/estrutura/"),
                 ("Galeria de fotos", "/galeria/"), ("Tour em vídeo", "/tour-em-video/"),
                 ("Quem somos", "/sobre/"), ("Como chegar", "/como-chegar/"),
                 ("Perguntas frequentes", "/perguntas-frequentes/")]
    col1 = "".join(f'<li><a href="{u}">{esc(n)}</a></li>' for n, u in a_chacara)
    col2 = "".join(f'<li><a href="{u}">{esc(n)}</a></li>' for n, u in D.FOOTER_LINKS)
    return f'''<footer class="site-footer">
<div class="wrap">
<div class="footer-grid">
<div class="footer-brand">
<a class="footer-logo" href="/"><img src="/brand/logo-chacara-imperio.svg" alt="Logo da Chácara Império — Eventos &amp; Experiências" width="150" height="150" loading="lazy"></a>
<p class="mt-2">Chácara para eventos de até 250 convidados e hospedagem para até 40 pessoas em 6 suítes, dentro do perímetro urbano de Uberaba. Anfitriões: {esc(D.HOSTS_PHRASE)}.</p>
<p><strong>Reservas somente por telefone ou WhatsApp.</strong></p>
<p class="contact-line">{icon("whatsapp")}<a href="{esc(D.wa_url(page.get("wa_key", "geral")))}" target="_blank" rel="noopener">WhatsApp {D.PHONE_DISPLAY}</a></p>
<p class="contact-line">{icon("phone")}<a href="{D.TEL_URL}">Telefone {D.PHONE_DISPLAY}</a></p>
<p class="contact-line">{icon("instagram")}<a href="{D.INSTAGRAM}" target="_blank" rel="noopener">{D.INSTAGRAM_HANDLE}</a></p>
<p class="contact-line">{icon("pin")}<span>{esc(D.CITY)} – {esc(D.STATE_NAME)}</span></p>
</div>
<div><h2>A chácara</h2><ul class="footer-list">{col1}</ul></div>
<div><h2>Para o seu evento</h2><ul class="footer-list">{col2}</ul></div>
</div>
<div class="footer-bottom"><span>© 2026 {esc(D.NAME)} · {esc(D.CITY)} – {D.STATE}</span><span>Conteúdo revisado em {D.UPDATED_HUMAN} · <a href="/politica-de-privacidade/">Privacidade</a></span></div>
</div>
</footer>'''


def render(page):
    lang = page.get("lang", "pt-BR")
    url = abs_url(page["path"])
    og_pid = page.get("og") or page.get("hero") or "piscina-banco"
    og_alt = PHOTOS[og_pid]["alt"]
    robots = "noindex, follow" if page.get("noindex") else \
        "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"
    preload_img = ""
    if page.get("hero"):
        m = meta()[page["hero"]]
        widths = sorted(int(k) for k in m["variants"])
        srcset = ", ".join(f"{img_url(page['hero'], w)} {w}w" for w in widths)
        preload_img = (f'<link rel="preload" as="image" href="{img_url(page["hero"], 800)}" '
                       f'imagesrcset="{srcset}" imagesizes="100vw" fetchpriority="high">')
    alternates = "".join(f'<link rel="alternate" hreflang="{hl}" href="{abs_url(p)}">'
                         for hl, p in page.get("alternates", []))
    ld = json.dumps(graph(page), ensure_ascii=False, separators=(",", ":"))
    hero = page.get("hero_html") if page.get("hero_kind") == "home" else (
        page_hero(page) if page.get("hero_kind", "page") == "page" else "")
    wa_key = page.get("wa_key", "geral")
    og_type = "article" if page.get("page_type") in ("Article", "BlogPosting") else "website"
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(page["title"])}</title>
<meta name="description" content="{esc(page["description"])}">
<link rel="canonical" href="{url}">
<meta name="robots" content="{robots}">
{alternates}
<meta name="theme-color" content="#163627">
<meta name="format-detection" content="telephone=no">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{esc(D.NAME)}">
<meta property="og:locale" content="{"pt_BR" if lang == "pt-BR" else "en_US"}">
<meta property="og:title" content="{esc(page.get("og_title", page["title"]))}">
<meta property="og:description" content="{esc(page["description"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og_url(og_pid)}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{esc(og_alt)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="geo.region" content="BR-MG">
<meta name="geo.placename" content="Uberaba">
<link rel="preload" href="/assets/fonts/Fraunces-normal-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/NunitoSans-normal-latin.woff2" as="font" type="font/woff2" crossorigin>
{preload_img}
<style>{CSS}</style>
<script type="application/ld+json">{ld}</script>
</head>
<body>
<a class="skip" href="#conteudo">Pular para o conteúdo</a>
{header(page)}
<main id="conteudo">
{hero}
{page["body"]}
</main>
{footer(page)}
<div class="mobile-bar">{btn_wa("WhatsApp", wa_key)}{btn_tel("Ligar", cls="btn-ghost")}</div>
<a class="wa-float" href="{esc(D.wa_url(wa_key))}" target="_blank" rel="noopener" aria-label="Falar no WhatsApp">{icon("whatsapp")}</a>
<script src="{JS_URL}" defer></script>
</body>
</html>
'''
