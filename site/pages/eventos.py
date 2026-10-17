import _data as D
from _components import (answer, card_link, checks, composer, cta_band, faq_html, features, img,
                         section_head, tiles)
from _icons import icon

PATH = "/eventos/"

FAQ = [
    ("Quantos convidados cabem nos eventos da Chácara Império?",
     "A Chácara Império recebe eventos de até 250 convidados, com salão coberto, área gourmet, varandas, jardins e estacionamento para 40 carros dentro da chácara."),
    ("Quais tipos de evento a Chácara Império recebe?",
     "Casamentos, aniversários e festas de 15 anos, confraternizações de empresa, reuniões de família (bodas, batizados, chá revelação), Natal e Réveillon e ensaios fotográficos."),
    ("Dá para fazer o evento e dormir na chácara?",
     "Sim. Além do evento, a chácara hospeda até 40 pessoas em 6 suítes, com 40 camas e 8 banheiros — os anfitriões da festa e a família podem passar a noite no local."),
    ("O que acontece se chover no dia do evento?",
     "A Chácara Império tem salão coberto com forro de madeira, área gourmet e varandas cobertas, que funcionam como plano B para a chuva. Vale planejar a disposição das mesas com os anfitriões."),
    ("Como consultar datas e valores para um evento?",
     "Pelo telefone ou WhatsApp (34) 99169-0139. Informe a data, o tipo de evento e o número de convidados para receber disponibilidade e valores."),
]

BODY = f'''
<section class="section section--tight">
<div class="wrap">
{answer("A Chácara Império, em Uberaba (MG), recebe <strong>eventos de até 250 convidados</strong>: casamentos, aniversários e 15 anos, confraternizações de empresa, reuniões de família, Natal e Réveillon e ensaios fotográficos. Tem salão coberto, área gourmet com churrasqueira e fogão a lenha, piscinas, jardins com pérgolas e estacionamento para 40 carros — e hospeda até 40 pessoas em 6 suítes.")}
</div>
</section>

<section class="section section--paper">
<div class="wrap">
{section_head("Escolha a sua ocasião", "Eventos na Chácara Império", "Cada celebração usa o espaço de um jeito. Veja ideias, perguntas frequentes e fotos para o seu tipo de evento.")}
<div class="grid grid-3">
{card_link("/eventos/casamento/", "pergola-jardim", "Casamento em chácara", "Cerimônia no jardim, recepção no salão coberto e pernoite para os noivos e a família.", "Até 250 convidados")}
{card_link("/eventos/aniversario/", "salao", "Aniversário e festa de 15 anos", "Festas infantis com parquinho e piscina, 15 anos que vão até a noite e aniversários de adultos.", "Festas")}
{card_link("/eventos/confraternizacao-de-empresa/", "gourmet-bar", "Confraternização de empresa", "Churrasco, futebol e piscina para a equipe, com contrato de locação temporária para empresas.", "Empresas")}
{card_link("/eventos/reuniao-de-familia/", "area-coberta-mesas", "Reunião de família", "Bodas, batizados, chá revelação, aniversário dos avós — e todo mundo dormindo no mesmo lugar.", "Família")}
{card_link("/eventos/natal-e-reveillon/", "piscinas-noite", "Natal e Réveillon", "Fim de ano com a família reunida, ceia na área gourmet e piscina iluminada à noite.", "Fim de ano")}
{card_link("/eventos/ensaio-fotografico/", "carro-de-boi", "Ensaio fotográfico", "Pérgolas, carro de boi, coqueiros e piscinas como cenário. Fotografia comercial permitida.", "Cenário para fotos")}
</div>
</div>
</section>

<section class="section">
<div class="wrap split">
<div>
{section_head("Os espaços do evento", "Um lugar para cada momento da festa", "Os convidados chegam pela alameda de palmeiras, estacionam dentro da chácara e circulam entre os jardins, as varandas e a área da piscina.")}
{features([("home", "Salão coberto com forro de madeira"), ("flame", "Área gourmet com churrasqueira e fogão a lenha"), ("palm", "Jardins com pérgolas e coqueiros"), ("waves", "Piscinas iluminadas à noite"), ("ball", "Campo de futebol gramado"), ("smile", "Parquinho para as crianças"), ("car", "Estacionamento para 40 carros"), ("bed", "6 suítes para quem vai dormir")])}
</div>
<div class="split-media">{img("salao", "(min-width: 900px) 560px, 100vw")}{img("jardim-noite", "220px", cls="stack")}</div>
</div>
</section>

<section class="section section--sand">
<div class="wrap">
{section_head("Por que fazer o evento aqui", "O que costuma pesar na escolha", None)}
{tiles([
    ("users", "Até 250 convidados", "Espaço para festas grandes sem perder o clima de casa de campo."),
    ("bed", "Pernoite no local", "6 suítes e 40 camas: quem organiza a festa não precisa pegar estrada depois."),
    ("road", "Acesso asfaltado", "Dentro do perímetro urbano de Uberaba, com portão eletrônico."),
    ("car", "Estacionamento próprio", "Vagas para 40 carros dentro da chácara."),
    ("sun", "Dia ou noite", "Gramados e piscinas para o dia; jardins e piscinas iluminados para a noite."),
    ("heart", "Direto com os donos", f"Você combina tudo com {D.HOSTS_PHRASE}, por telefone ou WhatsApp."),
])}
</div>
</section>

<section class="section">
<div class="wrap split">
<div>
{section_head("Antes de fechar a data", "O que vale combinar com antecedência", None)}
{checks(["Data e horário de início e término do evento", "Número estimado de convidados (adultos e crianças)", "Se haverá pernoite e quantas pessoas vão dormir", "Buffet, bebidas, decoração, som e demais fornecedores", "Montagem e desmontagem: quando os fornecedores podem entrar", "Regras de som e de uso da piscina durante a festa"])}
<p>Esses pontos definem o valor e a logística. Mande tudo de uma vez pelo WhatsApp e a resposta vem mais completa.</p>
</div>
<div>{composer()}</div>
</div>
</section>

<section class="section section--paper">
<div class="wrap narrow">
{faq_html(FAQ, "Perguntas frequentes sobre eventos")}
</div>
</section>

<section class="section section--tight">
<div class="wrap">{cta_band("Vamos ver se a sua data está livre?", key="evento")}</div>
</section>
'''

PAGE = dict(
    path=PATH,
    title="Chácara para Eventos em Uberaba – Até 250 Convidados",
    description="Chácara para eventos em Uberaba (MG): casamentos, aniversários, 15 anos e confraternizações para até 250 convidados, com salão coberto e pernoite para 40.",
    h1="Chácara para eventos em Uberaba",
    lead="Casamentos, aniversários, 15 anos, confraternizações e reuniões de família para até 250 convidados — com salão coberto, área gourmet, piscinas e pernoite para até 40 pessoas.",
    eyebrow="Eventos",
    hero="jardim-noite",
    crumbs=[("Início", "/"), ("Eventos", PATH)],
    wa_key="evento",
    faq=FAQ,
    body=BODY,
    sitemap_images=["salao", "pergola-jardim", "gourmet-bar"],
)
