import os

import _data as D
from _components import (answer, cta_band, faq_html, mosaic, section_head, ver)
from _icons import icon

PATH = "/tour-em-video/"
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VDIR = os.path.join(HERE, "static", "video")


def _exists(name):
    return os.path.exists(os.path.join(VDIR, name))


def _duration():
    try:
        with open(os.path.join(VDIR, "tour.duration")) as f:
            secs = round(float(f.read().strip()))
        return f"PT{secs // 60}M{secs % 60}S" if secs >= 60 else f"PT{secs}S", secs
    except (OSError, ValueError):
        return None, None


ISO, SECS = _duration()
HAS_VIDEO = _exists("tour.mp4")

if HAS_VIDEO:
    sources = ""
    if _exists("tour-av1.mp4"):
        sources += (f'<source src="/video/tour-av1.mp4?v={ver("video/tour-av1.mp4")}" '
                    'type="video/mp4; codecs=&quot;av01.0.08M.08&quot;">')
    sources += f'<source src="/video/tour.mp4?v={ver("video/tour.mp4")}" type="video/mp4">'
    PLAYER = (f'<div class="video-frame"><video controls playsinline preload="metadata" '
              f'poster="/video/tour-poster.jpg?v={ver("video/tour-poster.jpg")}" '
              f'aria-label="Tour em vídeo pela Chácara Império">{sources}'
              f'Seu navegador não reproduz vídeo. <a href="/galeria/">Veja as fotos</a>.</video></div>')
else:
    PLAYER = '<p class="note">O vídeo do tour está sendo preparado. Enquanto isso, <a href="/galeria/">veja a galeria de fotos</a>.</p>'

CHAPTERS = [("A chegada", "alameda de palmeiras e campo de futebol"), ("Jardins", "pérgolas de madeira e carro de boi"),
            ("Piscinas", "piscina adulto e infantil com deque de pedra"), ("Varandas e área gourmet", "churrasqueira, fogão a lenha e balcão"),
            ("Salão coberto", "o espaço das festas"), ("Parquinho", "balanços e escorregador"),
            ("A casa", "sala de estar e jantar e cozinha"), ("Suítes", "6 suítes com ar-condicionado, 40 camas"),
            ("À noite", "jardins, pérgola e piscinas iluminados")]
chapter_html = "".join(f"<li><strong>{a}</strong> — {b}</li>" for a, b in CHAPTERS)

FAQ = [
    ("O vídeo mostra a Chácara Império de verdade?",
     "Sim. O tour é montado com fotos reais da Chácara Império, de dia e de noite, na ordem de um passeio: chegada, jardins, piscinas, área gourmet, salão, casa, suítes e a chácara iluminada."),
    ("Posso conhecer a chácara pessoalmente antes de reservar?",
     "Peça pelo WhatsApp (34) 99169-0139 para combinar com os anfitriões a melhor forma de conhecer o espaço."),
]

BODY = f'''
<section class="section">
<div class="wrap">
{PLAYER}
<div class="btn-row mt-2">
<a class="btn btn-wa" href="{D.wa_url("tour")}" target="_blank" rel="noopener" data-wa="tour">{icon("whatsapp")}<span>Gostei! Consultar uma data</span></a>
<a class="btn btn-ghost" href="/galeria/">{icon("camera")}<span>Ver as fotos</span></a>
</div>
</div>
</section>

<section class="section section--paper">
<div class="wrap split">
<div>
{section_head("O que aparece no tour", "Um passeio do portão às suítes", None)}
<ol class="prose">{chapter_html}</ol>
</div>
<div>
{answer("A Chácara Império fica em Uberaba (MG) e tem 2.500 m² com piscina adulto e infantil, área gourmet com churrasqueira e fogão a lenha, salão coberto, campo de futebol, parquinho e 6 suítes. Recebe eventos de até 250 convidados e hospeda até 40 pessoas.", "Sobre a chácara")}
{faq_html(FAQ)}
</div>
</div>
</section>

<section class="section">
<div class="wrap">
{section_head("Mais fotos", "Veja os detalhes com calma", None)}
{mosaic(["piscina-luminarias", "churrasqueira", "suite-2", "carro-de-boi", "cozinha"])}
</div>
</section>

<section class="section section--tight">
<div class="wrap">{cta_band(key="tour")}</div>
</section>
'''

SCHEMA = []
if HAS_VIDEO:
    v = {
        "@type": "VideoObject",
        "@id": D.SITE_URL + PATH + "#video",
        "name": "Tour em vídeo pela Chácara Império, em Uberaba (MG)",
        "description": "Passeio pela Chácara Império: chegada, jardins com pérgolas, piscina adulto e infantil, área gourmet com churrasqueira e fogão a lenha, salão coberto, parquinho, casa, 6 suítes e a chácara iluminada à noite.",
        "thumbnailUrl": [D.SITE_URL + "/video/tour-poster.jpg"],
        "uploadDate": "2026-10-16",
        "contentUrl": D.SITE_URL + "/video/tour.mp4",
        "inLanguage": "pt-BR",
        "publisher": {"@id": D.SITE_URL + "/#negocio"},
        "about": {"@id": D.SITE_URL + "/#negocio"},
    }
    if ISO:
        v["duration"] = ISO
    SCHEMA.append(v)

PAGE = dict(
    path=PATH,
    title="Tour em Vídeo pela Chácara Império – Uberaba (MG)",
    description="Assista ao tour em vídeo pela Chácara Império, em Uberaba: chegada, jardins, piscinas, área gourmet, salão coberto, suítes e a chácara iluminada à noite.",
    h1="Tour em vídeo pela Chácara Império",
    lead=(f"Um passeio de {SECS} segundos, do portão às suítes, de dia e de noite." if SECS else "Um passeio do portão às suítes, de dia e de noite."),
    eyebrow="Tour",
    hero="jardim-noite",
    og="piscina-banco",
    crumbs=[("Início", "/"), ("Tour em vídeo", PATH)],
    hero_ctas="",
    wa_key="tour",
    faq=FAQ,
    schema=SCHEMA,
    body=BODY,
)
