from _components import card_link, cta_band, section_head

PATH = "/guia/"


def render_body(pages):
    guides = sorted((p for p in pages if p.get("guide")), key=lambda p: p["title"])
    cards = "".join(
        card_link(p["path"], p["guide"]["pid"], p["h1"], p["guide"]["summary"],
                  f'{p["guide"]["minutes"]} min de leitura') for p in guides)
    return f'''
<section class="section">
<div class="wrap">
{section_head("Guia e dicas", "Para planejar a festa ou o fim de semana", "Guias práticos para quem vai fazer um evento ou se hospedar numa chácara em Uberaba — escritos por quem recebe festas e hóspedes na chácara.")}
<div class="grid grid-3">{cards}</div>
</div>
</section>
<section class="section section--tight">
<div class="wrap">{cta_band()}</div>
</section>
'''


PAGE = dict(
    path=PATH,
    title="Guia e Dicas para Festa e Hospedagem em Chácara",
    description="Guias da Chácara Império: o que levar para a chácara, como organizar festa e casamento em chácara, como escolher o espaço e o que fazer em Uberaba (MG).",
    h1="Guia e dicas",
    lead="Checklists e guias práticos para planejar festas, casamentos e fins de semana em chácara.",
    eyebrow="Guia",
    hero="pergola-jardim",
    crumbs=[("Início", "/"), ("Guia", PATH)],
    page_type="CollectionPage",
    hero_ctas="",
    wa_key="geral",
    body="",
    render_body=render_body,
)
