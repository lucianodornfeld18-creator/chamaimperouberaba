import _data as D
from _components import (answer, btn_wa, checks, cta_band, distances_table, faq_html, img, section_head)
from _icons import icon

PATH = "/como-chegar/"
LOC_MSG = D.WA_MESSAGES["geral"].replace("gostaria de consultar uma data.", "gostaria de receber a localização da chácara.")

FAQ = [
    ("Onde fica a Chácara Império?",
     "Em Uberaba, no Triângulo Mineiro (MG), dentro do perímetro urbano da cidade, com acesso asfaltado e portão eletrônico. Peça a localização pelo WhatsApp (34) 99169-0139."),
    ("Precisa de carro alto ou 4x4 para chegar?",
     "Não. O acesso à Chácara Império é asfaltado."),
    ("Tem estacionamento?",
     "Sim, dentro da chácara, com espaço para 40 carros."),
    ("Qual a distância de Uberlândia até Uberaba?",
     "Cerca de 107 km por rodovia. De Araxá são cerca de 119 km, de Franca cerca de 121 km e de Ribeirão Preto cerca de 171 km."),
    ("Uberaba tem aeroporto?",
     "Tem o Aeroporto de Uberaba – Mário de Almeida Franco, além da rodoviária. Consulte as companhias aéreas para os voos disponíveis."),
]

map_block = ""
if D.MAPS_URL:
    map_block = f'<p><a class="btn btn-ghost" href="{D.MAPS_URL}" target="_blank" rel="noopener">{icon("pin")}<span>Abrir no Google Maps</span></a></p>'

BODY = f'''
<section class="section section--tight">
<div class="wrap">
{answer("A <strong>Chácara Império</strong> fica em <strong>Uberaba (MG)</strong>, no Triângulo Mineiro, dentro do perímetro urbano da cidade e com <strong>acesso asfaltado</strong>. A entrada tem portão eletrônico e o estacionamento comporta 40 carros. A localização exata é enviada pelo WhatsApp (34) 99169-0139. Uberaba fica a cerca de 107 km de Uberlândia e 171 km de Ribeirão Preto.")}
</div>
</section>

<section class="section section--paper">
<div class="wrap split">
<div>
{section_head("Localização", "Dentro do perímetro urbano de Uberaba", "Estar dentro do perímetro urbano faz diferença no dia do evento: o acesso é asfaltado e os convidados chegam sem estrada de terra.")}
{checks(["Dentro do perímetro urbano de Uberaba", "Acesso asfaltado até o portão", "Portão eletrônico e alameda de palmeiras na entrada", "Estacionamento para 40 carros dentro da chácara", "Câmeras de segurança no portão e no estacionamento"])}
<div class="btn-row mt-2">{btn_wa("Pedir a localização no WhatsApp", "geral", text=LOC_MSG)}</div>
{map_block}
</div>
<div class="split-media">{img("alameda", "(min-width: 900px) 560px, 100vw")}{img("portao-noite", "220px", cls="stack")}</div>
</div>
</section>

<section class="section">
<div class="wrap split">
<div>
{section_head("Para quem vem de fora", "Distâncias até Uberaba", "Distâncias rodoviárias aproximadas até Uberaba. Some alguns minutos dentro da cidade até a chácara.")}
<p>Uberaba é cortada pela BR-050, que liga a cidade a Uberlândia e ao interior de São Paulo, e pela BR-262, caminho de quem vem de Araxá e de Belo Horizonte. A cidade também tem rodoviária e o Aeroporto de Uberaba – Mário de Almeida Franco.</p>
<p>Vem para um evento ou para a Expozebu? Veja a <a href="/hospedagem/">hospedagem para grupos</a> e <a href="/guia/o-que-fazer-em-uberaba/">o que fazer em Uberaba</a>.</p>
</div>
<div>{distances_table()}<p class="updated mt-1">Fonte: rotas do OpenStreetMap (OSRM), a partir do centro de Uberaba, outubro de 2026.</p></div>
</div>
</section>

<section class="section section--paper">
<div class="wrap narrow">
{faq_html(FAQ, "Perguntas frequentes sobre a localização")}
</div>
</section>

<section class="section section--tight">
<div class="wrap">{cta_band("Já sabe a data? Consulte a disponibilidade.")}</div>
</section>
'''

PAGE = dict(
    path=PATH,
    title="Como Chegar à Chácara Império em Uberaba (MG)",
    description="Localização da Chácara Império em Uberaba (MG): perímetro urbano, acesso asfaltado e estacionamento para 40 carros. Distâncias de Uberlândia, Franca e região.",
    h1="Como chegar à Chácara Império",
    lead="Dentro do perímetro urbano de Uberaba, com acesso asfaltado, portão eletrônico e estacionamento para 40 carros.",
    eyebrow="Como chegar",
    hero="alameda",
    crumbs=[("Início", "/"), ("Como chegar", PATH)],
    hero_ctas=f'<div class="btn-row">{btn_wa("Pedir a localização", "geral", text=LOC_MSG)}</div>',
    wa_key="geral",
    faq=FAQ,
    body=BODY,
)
