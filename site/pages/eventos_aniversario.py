from _components import (answer, checks, composer, cta_band, faq_html, figure, img, section_head, tiles)

PATH = "/eventos/aniversario/"

FAQ = [
    ("A Chácara Império faz festa infantil?",
     "Faz. Para as crianças há parquinho com balanços e escorregador, piscina infantil e muito gramado; os adultos ficam nas varandas e na área gourmet, perto de tudo."),
    ("Dá para fazer festa de 15 anos à noite na chácara?",
     "Sim. À noite os jardins, a pérgola e as piscinas ficam iluminados, e o salão coberto recebe a pista e as mesas. A festa pode ter até 250 convidados."),
    ("A piscina pode ser usada durante a festa?",
     "A chácara tem piscina adulto e piscina infantil. O uso durante o evento é combinado com os anfitriões — em festas com crianças, defina sempre um adulto responsável olhando a piscina."),
    ("Quantos convidados cabem numa festa de aniversário?",
     "Até 250 convidados, com estacionamento para 40 carros dentro da Chácara Império."),
    ("O aniversariante e a família podem dormir na chácara depois da festa?",
     "Podem. A chácara hospeda até 40 pessoas em 6 suítes, com 40 camas e 8 banheiros."),
]

BODY = f'''
<section class="section section--tight">
<div class="wrap">
{answer("A <strong>Chácara Império</strong>, em Uberaba (MG), recebe festas de aniversário de <strong>até 250 convidados</strong>: festa infantil com parquinho e piscina infantil, festa de 15 anos que vai até a noite com jardins e piscinas iluminados, e aniversário de adulto com churrasco, fogão a lenha e campo de futebol. Depois da festa, até 40 pessoas podem dormir nas 6 suítes.")}
</div>
</section>

<section class="section section--paper">
<div class="wrap">
{section_head("Três jeitos de comemorar", "Para cada idade, um jeito de usar a chácara", None)}
{tiles([
    ("smile", "Festa infantil", "Parquinho com balanços e escorregador, piscina infantil e gramado para correr. Os adultos acompanham das varandas e da área gourmet."),
    ("sparkle", "Festa de 15 anos", "Jardins, pérgola e piscinas iluminados para as fotos, salão coberto para a pista e suítes para as amigas dormirem depois da festa."),
    ("flame", "Aniversário de adulto", "Churrasqueira, fogão a lenha, balcão de bar, futebol no campo gramado e piscina para o dia todo."),
])}
</div>
</section>

<section class="section">
<div class="wrap">
<div class="grid grid-2">
{figure("parquinho", "Parquinho com balanços e escorregador", "(min-width: 640px) 50vw, 100vw")}
{figure("piscinas-vista", "Piscina adulto e piscina infantil", "(min-width: 640px) 50vw, 100vw")}
{figure("salao", "Salão coberto para as mesas e a pista", "(min-width: 640px) 50vw, 100vw")}
{figure("gourmet-bar", "Área gourmet com churrasqueira e balcão", "(min-width: 640px) 50vw, 100vw")}
</div>
</div>
</section>

<section class="section section--sand">
<div class="wrap split">
<div>
{section_head("Festa com criança", "Combinados que deixam todo mundo tranquilo", "Festa em chácara é liberdade para as crianças — e alguns cuidados para os adultos.")}
{checks(["Escale adultos para olhar a piscina em turnos, mesmo que as crianças saibam nadar", "Leve boias, colete e protetor solar infantil", "Monte a mesa do bolo à sombra, no salão coberto ou na varanda", "Separe uma troca de roupa por criança (piscina + gramado = roupa molhada)", "Avise no convite que é festa em chácara: roupa leve e calçado confortável", "Combine com os anfitriões o horário de início e de término"])}
</div>
<div class="split-media">{img("parquinho", "(min-width: 900px) 560px, 100vw")}</div>
</div>
</section>

<section class="section">
<div class="wrap split">
<div>
{section_head("Planejando a festa", "O que mandar na sua consulta", None)}
{checks(["Data e horário da festa", "Idade do aniversariante e tipo de festa", "Número de convidados (adultos e crianças)", "Se a família vai dormir na chácara", "Buffet, bolo, decoração e som que você pretende contratar"])}
<p>Para organizar tudo — do cardápio à decoração —, veja o guia <a href="/guia/festa-em-chacara-como-organizar/">festa em chácara: como organizar</a> e a lista do <a href="/guia/o-que-levar-para-a-chacara/">que levar para a chácara</a>.</p>
</div>
<div>{composer("Aniversário / 15 anos")}</div>
</div>
</section>

<section class="section section--paper">
<div class="wrap narrow">
{faq_html(FAQ, "Perguntas frequentes sobre festas de aniversário")}
</div>
</section>

<section class="section section--tight">
<div class="wrap">{cta_band("Qual é a data do aniversário?", key="aniversario", wa_label="Consultar data da festa")}</div>
</section>
'''

PAGE = dict(
    path=PATH,
    title="Chácara para Festa de Aniversário e 15 Anos em Uberaba",
    description="Chácara para festa em Uberaba (MG): aniversário infantil com parquinho e piscina, festa de 15 anos à noite e aniversário de adulto para até 250 convidados.",
    h1="Chácara para festa de aniversário e 15 anos em Uberaba",
    lead="Parquinho e piscina infantil para as crianças, jardins iluminados para os 15 anos, churrasco e futebol para os adultos — e suítes para dormir depois da festa.",
    eyebrow="Aniversário e 15 anos",
    hero="piscinas-noite",
    crumbs=[("Início", "/"), ("Eventos", "/eventos/"), ("Aniversário e 15 anos", PATH)],
    wa_key="aniversario",
    wa_label="Consultar data da festa",
    faq=FAQ,
    body=BODY,
    sitemap_images=["parquinho", "salao", "gourmet-bar"],
)
