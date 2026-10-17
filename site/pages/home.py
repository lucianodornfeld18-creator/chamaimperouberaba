import os

import _data as D
from _components import (answer, btn_tel, btn_wa, card_link, composer, cta_band, esc, facts_grid,
                         faq_html, features, img, mosaic, section_head, steps, tiles, ornament, img_url, ver)
from _icons import icon

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VIDEO_DIR = os.path.join(HERE, "static", "video")


def _video_attrs():
    out = []
    for kind, name in (("av1", "tour-hero-av1.mp4"), ("mp4", "tour-hero.mp4"),
                       ("mav1", "tour-hero-mobile-av1.mp4"), ("mmp4", "tour-hero-mobile.mp4")):
        if os.path.exists(os.path.join(VIDEO_DIR, name)):
            out.append(f'data-{kind}="/video/{name}?v={ver("video/" + name)}"')
    return " ".join(out)


_v = _video_attrs()
VIDEO = (f'<video class="hero-video" data-hero-video muted loop playsinline preload="none" '
         f'aria-hidden="true" tabindex="-1" {_v}></video>') if _v else ""

HERO = f'''<section class="hero hero--home">
<div class="hero-media">{img("piscina-banco", "100vw", eager=True, priority=True)}{VIDEO}</div>
<div class="hero-shade"></div>
<div class="wrap hero-content">
<p class="eyebrow">Chácara Império · Uberaba – MG</p>
<h1>Chácara para eventos e hospedagem em Uberaba</h1>
<p class="lead">Casamentos, aniversários e confraternizações para até 250 convidados — e a chácara inteira para hospedar até 40 pessoas em 6 suítes, com piscinas, área gourmet e muito verde, dentro do perímetro urbano.</p>
<div class="btn-row">{btn_wa("Consultar data no WhatsApp", "geral")}{btn_tel("Ligar agora", cls="btn-light")}<a class="tour-link" href="/tour-em-video/"><span class="play">{icon("play")}</span>Ver o tour em vídeo</a></div>
<ul class="hero-facts" aria-label="Destaques">
<li>{icon("users")}Até 250 convidados</li><li>{icon("bed")}40 hóspedes · 6 suítes</li><li>{icon("waves")}Piscina adulto e infantil</li><li>{icon("road")}Acesso asfaltado</li>
</ul>
</div>
</section>'''

FAQ = [
    ("Quantas pessoas cabem na Chácara Império?",
     "Até 250 convidados em eventos. Para dormir, a chácara acomoda até 40 pessoas em 6 suítes, com 40 camas e 8 banheiros."),
    ("A chácara aluga só para eventos ou também para hospedagem?",
     "Para os dois. Você pode alugar a chácara inteira para um fim de semana, feriado ou temporada, para um evento, ou para um evento com a família e os convidados mais próximos hospedados no local."),
    ("Onde fica a Chácara Império?",
     "Em Uberaba, no Triângulo Mineiro, dentro do perímetro urbano da cidade, com acesso asfaltado e portão eletrônico. Peça a localização pelo WhatsApp (34) 99169-0139."),
    ("Como faço uma reserva?",
     "As reservas são feitas somente por telefone ou WhatsApp, no (34) 99169-0139. Informe a data, o tipo de evento ou estadia e o número de pessoas para receber disponibilidade e valores."),
    ("Qual é o horário de check-in e check-out?",
     "Na hospedagem, o check-in é a partir das 15h e o check-out até as 11h."),
    ("Posso levar meu cachorro?",
     "Sim. A Chácara Império aceita animais de estimação."),
    ("A chácara tem piscina?",
     "Tem duas: uma piscina adulto e uma piscina infantil, com deque de pedra, luminárias para a noite e chuveiro externo."),
    ("Quanto custa alugar a Chácara Império?",
     "O valor depende da data, do tipo de evento, do número de convidados e se haverá pernoite. Feriados, fim de ano e o período da Expozebu costumam ser os mais procurados. Peça um orçamento pelo WhatsApp (34) 99169-0139."),
]

BODY = f'''
<section class="section section--tight">
<div class="wrap">
{answer("A <strong>Chácara Império</strong> é uma chácara para alugar em Uberaba (MG) que recebe <strong>eventos de até 250 convidados</strong> e hospeda <strong>até 40 pessoas em 6 suítes</strong>. São 2.500 m² com piscina adulto e infantil, área gourmet com churrasqueira e fogão a lenha, salão coberto, campo de futebol, parquinho e estacionamento para 40 carros, dentro do perímetro urbano e com acesso asfaltado. Reservas por telefone ou WhatsApp: " + f'<a href="{D.TEL_URL}">{D.PHONE_DISPLAY}</a>.', "Em poucas palavras")}
{facts_grid()}
</div>
</section>

<section class="section section--paper">
<div class="wrap">
{section_head("Dois jeitos de aproveitar", "Festa, descanso — ou os dois no mesmo fim de semana", "Aqui o evento e o pernoite acontecem no mesmo lugar: depois da festa, a família e os amigos mais próximos podem dormir na chácara.")}
<div class="grid grid-2">
{card_link("/eventos/", "jardim-noite", "Eventos para até 250 convidados", "Casamentos, aniversários, 15 anos, confraternizações de empresa e reuniões de família, com salão coberto, área gourmet, jardins iluminados e estacionamento próprio.", "Eventos", "(min-width: 640px) 50vw, 100vw")}
{card_link("/hospedagem/", "piscinas-casa", "Hospedagem para até 40 pessoas", "A chácara inteira para o seu grupo: 6 suítes com ar-condicionado, 40 camas, piscinas, churrasqueira e campo de futebol. Ideal para fins de semana, feriados e temporadas.", "Hospedagem", "(min-width: 640px) 50vw, 100vw")}
</div>
</div>
</section>

<section class="section">
<div class="wrap">
{section_head("Para cada celebração", "Que tipo de evento você está planejando?", "Cada ocasião pede um jeito de usar o espaço. Veja o que a chácara oferece para a sua.")}
<div class="grid grid-3">
{card_link("/eventos/casamento/", "pergola-jardim", "Casamento", "Cerimônia no jardim, festa no salão coberto e pernoite para os noivos e a família.", "Até 250 convidados")}
{card_link("/eventos/aniversario/", "salao", "Aniversário e 15 anos", "Do aniversário infantil com parquinho e piscina à festa de 15 anos que vai até a noite.", "Festas")}
{card_link("/eventos/confraternizacao-de-empresa/", "gourmet-bar", "Confraternização de empresa", "Churrasco, futebol e piscina para a equipe, com contrato de locação para empresas.", "Empresas")}
{card_link("/eventos/reuniao-de-familia/", "area-coberta-mesas", "Reunião de família", "Bodas, batizados, chá revelação e aquele encontro que junta todo mundo no mesmo lugar.", "Família")}
{card_link("/eventos/natal-e-reveillon/", "piscinas-noite", "Natal e Réveillon", "A virada do ano com a família reunida, piscina iluminada e quartos para todos dormirem.", "Fim de ano")}
{card_link("/eventos/ensaio-fotografico/", "carro-de-boi", "Ensaio fotográfico", "Pérgolas, carro de boi, coqueirais e piscinas como cenário. Fotografia comercial permitida.", "Cenário para fotos")}
</div>
</div>
</section>

<section class="section section--sand">
<div class="wrap split">
<div>
{section_head("A estrutura", "Tudo o que o seu evento e a sua estadia precisam", "São 2.500 m² pensados para receber bem: lazer para as crianças, área gourmet para o churrasco e quartos para todo mundo descansar.")}
{features([("waves", "Piscina adulto e infantil"), ("flame", "Churrasqueira e fogão a lenha"), ("home", "Salão coberto para festas"), ("ball", "Campo de futebol gramado"), ("smile", "Parquinho para as crianças"), ("bed", "6 suítes com ar-condicionado"), ("utensils", "Cozinha e sala de jantar"), ("car", "Estacionamento para 40 carros"), ("shield", "Portão eletrônico e câmeras"), ("paw", "Aceita animais de estimação")])}
<p class="mt-2"><a class="link-arrow" href="/estrutura/">Conhecer a estrutura completa {icon("arrow")}</a></p>
</div>
<div class="split-media">{img("piscinas-vista", "(min-width: 900px) 560px, 100vw")}{img("churrasqueira", "220px", cls="stack")}</div>
</div>
</section>

<section class="section">
<div class="wrap">
{section_head("Passeie pela chácara", "Veja cada cantinho antes de decidir", "Fotos de dia e de noite: as piscinas iluminadas, os jardins com pérgolas, a área gourmet e as suítes.", center=True)}
{mosaic(["piscinas-vista", "gourmet-noite", "suite-1", "pergola-noite", "sala"])}
<div class="btn-row mt-2" style="justify-content:center"><a class="btn btn-ghost" href="/galeria/">{icon("camera")}<span>Ver todas as fotos</span></a><a class="btn btn-ghost" href="/tour-em-video/">{icon("play")}<span>Assistir ao tour em vídeo</span></a></div>
</div>
</section>

<section class="section section--paper" id="anfitrioes">
<div class="wrap hosts">
<figure class="hosts-photo">{img("anfitrioes", "(min-width: 880px) 420px, 90vw")}<figcaption>Maria Inês e Luciano</figcaption></figure>
<div class="letter">
<p class="eyebrow">Quem recebe você</p>
<p class="hello">Olá! Que alegria ter você por aqui!</p>
<p>Nós somos a <strong>Maria Inês</strong> e o <strong>Luciano</strong>, anfitriões da Chácara Império. Cuidamos de cada cantinho deste lugar com muito carinho para receber pessoas especiais — e o que mais nos deixa felizes é ver a chácara cheia de vida: crianças brincando, amigos celebrando e famílias criando memórias.</p>
<p>Aqui você conversa direto com a gente, do primeiro contato até o dia da sua festa ou da sua estadia. Fique à vontade para conhecer o espaço e tirar todas as suas dúvidas. Será um prazer receber você!</p>
<p class="signature">— Maria Inês e Luciano</p>
<div class="btn-row mt-2">{btn_wa("Falar com a gente", "geral")}<a class="link-arrow" href="/sobre/">Nossa história {icon("arrow")}</a></div>
</div>
</div>
</section>

<section class="section">
<div class="wrap">
{section_head("Por que a Chácara Império", "Pensada para quem quer receber bem", None)}
{tiles([
    ("bed", "Festa e pernoite no mesmo lugar", "40 camas em 6 suítes: noivos, aniversariantes e família não precisam pegar a estrada depois da festa."),
    ("road", "Fácil de chegar", "Fica dentro do perímetro urbano de Uberaba, com acesso asfaltado — convidados chegam sem estrada de terra."),
    ("smile", "Espaço para as crianças", "Piscina infantil, parquinho com balanços e escorregador e muito gramado para correr."),
    ("shield", "Tranquilidade", "Portão eletrônico e câmeras externas nas varandas, no estacionamento e na entrada."),
    ("paw", "O pet também vem", "A chácara aceita animais de estimação, então ninguém da família fica de fora."),
    ("heart", "Atendimento dos donos", "Você fala direto com a Maria Inês e o Luciano, por telefone ou WhatsApp."),
])}
</div>
</section>

<section class="section section--sand" id="reservar">
<div class="wrap split">
<div>
{section_head("Como reservar", "Reserva simples, direto com os anfitriões", "As reservas são feitas somente por telefone ou WhatsApp — sem formulários longos nem intermediários.")}
{steps([
    ("Chame no WhatsApp ou ligue", f"Conte a data, o tipo de evento ou estadia e quantas pessoas. Telefone e WhatsApp: {D.PHONE_DISPLAY}."),
    ("Receba disponibilidade e valores", "Respondemos com as datas livres, o valor para o seu caso e tudo o que está incluído."),
    ("Confirme e comemore", "Combinamos os detalhes da reserva e deixamos a chácara pronta para você."),
], vertical=True)}
</div>
<div>{composer()}</div>
</div>
</section>

<section class="section">
<div class="wrap narrow">
{section_head("Perguntas frequentes", "Antes de reservar, as dúvidas mais comuns", None)}
{faq_html(FAQ)}
<p class="mt-2"><a class="link-arrow" href="/perguntas-frequentes/">Ver todas as perguntas {icon("arrow")}</a></p>
</div>
</section>

<section class="section section--paper">
<div class="wrap split reverse">
<div>
{section_head("Localização", "Em Uberaba, no coração do Triângulo Mineiro", "A chácara fica dentro do perímetro urbano de Uberaba, com acesso asfaltado. Para quem vem de fora, a cidade está a cerca de 107 km de Uberlândia, 119 km de Araxá, 121 km de Franca e 171 km de Ribeirão Preto.")}
<div class="btn-row"><a class="btn btn-ghost" href="/como-chegar/">{icon("pin")}<span>Como chegar</span></a>{btn_wa("Pedir a localização", "geral", text=D.WA_MESSAGES["geral"].replace("gostaria de consultar uma data.", "gostaria de receber a localização da chácara."))}</div>
</div>
<div class="split-media">{img("alameda", "(min-width: 900px) 560px, 100vw")}</div>
</div>
</section>

<section class="section section--tight">
<div class="wrap">{cta_band()}</div>
</section>
'''

PAGE = dict(
    path="/",
    title="Chácara para Alugar em Uberaba: Eventos e Hospedagem",
    og_title="Chácara Império — chácara para eventos e hospedagem em Uberaba (MG)",
    description="Chácara Império, em Uberaba (MG): eventos para até 250 convidados e hospedagem para 40 pessoas em 6 suítes, com piscinas e área gourmet. Reserve pelo WhatsApp.",
    hero="piscina-banco",
    hero_kind="home",
    hero_html=HERO,
    body=BODY,
    faq=FAQ,
    wa_key="geral",
    crumbs=[("Início", "/")],
    alternates=[("pt-BR", "/"), ("en", "/en/"), ("x-default", "/")],
    sitemap_images=["piscinas-vista", "salao", "gourmet-noite", "suite-1", "anfitrioes"],
)
