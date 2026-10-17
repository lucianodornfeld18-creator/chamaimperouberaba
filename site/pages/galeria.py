import _data as D
from _components import (biggest, cta_band, esc, img, img_url, og_url)
from _icons import icon
from _photos import GALLERY_CATS, PHOTOS

PATH = "/galeria/"

ORDER = ["piscina-banco", "piscinas-vista", "piscinas-casa", "piscina-luminarias", "piscina-deque",
         "piscina-casa-principal", "varanda-piscina", "churrasqueira", "gourmet-bar", "area-coberta-mesas",
         "varanda-mesa", "salao", "pergola-jardim", "pergola-varanda", "carro-de-boi", "jardim-banco",
         "jardim-coqueiro", "jardim-lateral", "casa-gramado", "alameda", "estacionamento", "parquinho",
         "sala", "sala-2", "cozinha", "suite-1", "suite-2", "suite-3", "suite-4", "suite-5", "suite-6",
         "jardim-noite", "pergola-noite", "carro-de-boi-noite", "coqueiro-noite", "piscinas-noite",
         "piscina-noite-2", "gourmet-noite", "varanda-noite", "portao-noite"]

items = []
for pid in ORDER:
    p = PHOTOS[pid]
    w, _ = biggest(pid)
    items.append(
        f'<a id="foto-{pid}" href="{img_url(pid, w)}" data-full="{img_url(pid, w)}" data-cat="{p["cat"]}" '
        f'data-caption="{esc(p["caption"])}">{img(pid, "(min-width: 1100px) 25vw, (min-width: 760px) 33vw, 50vw")}</a>')

filters = "".join(
    f'<button type="button" data-filter="{c}" aria-pressed="{"true" if c == "todas" else "false"}">{esc(n)}</button>'
    for c, n in GALLERY_CATS)

BODY = f'''
<section class="section">
<div class="wrap">
<p class="muted">{len(ORDER)} fotos da Chácara Império, de dia e de noite. Toque numa foto para ampliar.</p>
<div class="filters" role="group" aria-label="Filtrar fotos">{filters}</div>
<div class="gallery" data-gallery>{"".join(items)}</div>
<p class="mt-2"><a class="link-arrow" href="/tour-em-video/">Prefere vídeo? Assista ao tour pela chácara {icon("arrow")}</a></p>
</div>
</section>

<dialog class="lightbox" data-lightbox aria-label="Foto ampliada">
<figure><img src="" alt=""><figcaption></figcaption></figure>
<button class="lb-btn lb-prev" type="button" data-prev aria-label="Foto anterior">{icon("left")}</button>
<button class="lb-btn lb-next" type="button" data-next aria-label="Próxima foto">{icon("right")}</button>
<button class="lb-btn lb-close" type="button" data-close aria-label="Fechar">{icon("x")}</button>
</dialog>

<section class="section section--tight">
<div class="wrap">{cta_band("Imaginou o seu evento aqui?")}</div>
</section>
'''

GALLERY_SCHEMA = {
    "@type": "ImageGallery",
    "@id": D.SITE_URL + PATH + "#galeria",
    "name": "Fotos da Chácara Império",
    "about": {"@id": D.SITE_URL + "/#negocio"},
    "associatedMedia": [
        {"@type": "ImageObject", "contentUrl": D.SITE_URL + img_url(pid, biggest(pid)[0]).split("?")[0],
         "caption": PHOTOS[pid]["alt"], "name": PHOTOS[pid]["caption"]} for pid in ORDER],
}

PAGE = dict(
    path=PATH,
    title="Fotos da Chácara Império em Uberaba – Galeria",
    description="Fotos da Chácara Império em Uberaba (MG): piscinas, área gourmet, salão coberto, jardins com pérgolas, parquinho, suítes e a chácara iluminada à noite.",
    h1="Fotos da Chácara Império",
    lead="Piscinas, área gourmet, jardins, suítes e a chácara iluminada à noite.",
    eyebrow="Galeria",
    hero="piscinas-noite",
    og="piscinas-vista",
    crumbs=[("Início", "/"), ("Galeria", PATH)],
    page_type="CollectionPage",
    hero_ctas="",
    wa_key="geral",
    schema=[GALLERY_SCHEMA],
    body=BODY,
    sitemap_images=ORDER[:30],
)
