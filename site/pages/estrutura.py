from _components import (answer, checks, cta_band, faq_html, facts_grid, figure, section_head, toc)

PATH = "/estrutura/"

FAQ = [
    ("A Chácara Império tem piscina infantil?",
     "Tem. São duas piscinas — uma adulto e uma infantil —, com deque de pedra, espreguiçadeiras, luminárias para a noite e chuveiro externo."),
    ("Como é a área gourmet da Chácara Império?",
     "Coberta, com forro de madeira, churrasqueira de tijolinho, fogão a lenha, bancada de granito com pia, balcão de bar com banquetas e mesas de madeira rústica de frente para a piscina."),
    ("A chácara tem salão para festas?",
     "Tem um salão coberto com forro de madeira e ventiladores, ao lado da área gourmet, usado para as mesas e a pista nos eventos de até 250 convidados."),
    ("Tem campo de futebol e espaço para crianças?",
     "Tem campo de futebol gramado cercado por alambrado e parquinho com balanços e escorregador na areia, além de muito gramado."),
    ("As suítes têm ar-condicionado?",
     "Sim. As 6 suítes têm ar-condicionado e somam 40 camas, entre camas de casal e beliches de madeira. A chácara tem 8 banheiros."),
    ("Qual é o tamanho da Chácara Império?",
     "A área é de 2.500 m², com estacionamento para 40 carros dentro da chácara."),
]

SIZES = "(min-width: 960px) 33vw, (min-width: 640px) 50vw, 100vw"

BODY = f'''
<section class="section section--tight">
<div class="wrap">
{answer("A <strong>Chácara Império</strong> tem 2.500 m² em Uberaba (MG) com piscina adulto e piscina infantil, área gourmet coberta com churrasqueira e fogão a lenha, salão coberto para festas, jardins com pérgolas de madeira, campo de futebol gramado, parquinho, casa com sala e cozinha equipada, <strong>6 suítes com ar-condicionado (40 camas)</strong>, 8 banheiros, Wi-Fi e estacionamento para 40 carros.")}
{facts_grid()}
</div>
</section>

<section class="section section--paper">
<div class="wrap">
{toc([("piscinas", "Piscinas"), ("gourmet", "Área gourmet e varandas"), ("salao", "Salão coberto"), ("jardins", "Jardins e pérgolas"), ("lazer", "Campo de futebol e parquinho"), ("casa", "Casa: sala e cozinha"), ("suites", "Suítes"), ("chegada", "Chegada, estacionamento e segurança"), ("comodidades", "Outras comodidades")])}

<h2 id="piscinas">Piscinas</h2>
<p>Duas piscinas lado a lado — uma adulto e uma infantil, em formato orgânico —, rodeadas por deque de pedra, gramado e coqueiros. Há espreguiçadeiras, bancos de jardim, luminárias de globo para a noite e chuveiro externo. A área da piscina tem cerca de madeira e fica de frente para as varandas.</p>
<div class="grid grid-3">
{figure("piscinas-vista", None, SIZES)}
{figure("piscina-luminarias", None, SIZES)}
{figure("piscinas-noite", None, SIZES)}
</div>

<h2 id="gourmet" class="mt-3">Área gourmet e varandas</h2>
<p>O coração da chácara nos dias de festa: churrasqueira de tijolinho, fogão a lenha, bancada de granito com pia, balcão de bar com banquetas e mesas de madeira rústica, tudo coberto e com forro de madeira. As varandas se abrem para a piscina e para o jardim.</p>
<div class="grid grid-3">
{figure("churrasqueira", None, SIZES)}
{figure("gourmet-bar", None, SIZES)}
{figure("varanda-piscina", None, SIZES)}
{figure("area-coberta-mesas", None, SIZES)}
{figure("varanda-mesa", None, SIZES)}
{figure("gourmet-noite", None, SIZES)}
</div>

<h2 id="salao" class="mt-3">Salão coberto</h2>
<p>Um salão amplo e coberto, com forro de madeira, ventiladores e TV, ao lado da área gourmet. É onde ficam as mesas, o bolo e a pista nos eventos — e o plano B quando chove.</p>
<div class="grid grid-2">
{figure("salao", None, "(min-width: 640px) 50vw, 100vw")}
{figure("area-coberta-mesas", "Área coberta integrada, de frente para a piscina", "(min-width: 640px) 50vw, 100vw")}
</div>

<h2 id="jardins" class="mt-3">Jardins e pérgolas</h2>
<p>Gramados, coqueiros, ciprestes junto ao muro, canteiros de flores, pérgolas de madeira, um carro de boi decorativo e rodas de carroça. À noite, a iluminação dos jardins muda o clima — é um dos cenários preferidos para fotos.</p>
<div class="grid grid-3">
{figure("pergola-jardim", None, SIZES)}
{figure("carro-de-boi", None, SIZES)}
{figure("jardim-banco", None, SIZES)}
{figure("jardim-coqueiro", None, SIZES)}
{figure("pergola-noite", None, SIZES)}
{figure("coqueiro-noite", None, SIZES)}
</div>

<h2 id="lazer" class="mt-3">Campo de futebol e parquinho</h2>
<p>Campo de futebol gramado, cercado por alambrado, ao lado da alameda de entrada. Para as crianças, parquinho com balanços e escorregador na areia, perto de uma área ampla de gramado.</p>
<div class="grid grid-2">
{figure("alameda", None, "(min-width: 640px) 50vw, 100vw")}
{figure("parquinho", None, "(min-width: 640px) 50vw, 100vw")}
</div>

<h2 id="casa" class="mt-3">Casa: sala e cozinha</h2>
<p>Sala de estar com sofás e TV em painel de madeira, mesa de jantar de madeira com cadeiras e cozinha com fogão, geladeira, micro-ondas e bancada de granito.</p>
<div class="grid grid-3">
{figure("sala", None, SIZES)}
{figure("sala-2", None, SIZES)}
{figure("cozinha", None, SIZES)}
</div>

<h2 id="suites" class="mt-3">Suítes</h2>
<p>São 6 suítes com ar-condicionado, que somam 40 camas entre camas de casal e beliches de madeira. Algumas têm ventilador de teto e forro de madeira. Ao todo, a chácara tem 8 banheiros.</p>
<div class="grid grid-3">
{figure("suite-1", None, SIZES)}
{figure("suite-3", None, SIZES)}
{figure("suite-6", None, SIZES)}
</div>

<h2 id="chegada" class="mt-3">Chegada, estacionamento e segurança</h2>
<p>A chácara fica dentro do perímetro urbano de Uberaba, com acesso asfaltado. A entrada tem portão eletrônico e uma alameda de palmeiras que leva ao estacionamento de brita, com espaço para 40 carros. Há câmeras de segurança externas nas varandas, no estacionamento e no portão de entrada.</p>
<div class="grid grid-2">
{figure("estacionamento", None, "(min-width: 640px) 50vw, 100vw")}
{figure("portao-noite", None, "(min-width: 640px) 50vw, 100vw")}
</div>

<h2 id="comodidades" class="mt-3">Outras comodidades</h2>
{checks(["Wi-Fi e espaço de trabalho", "Área de refeições ao ar livre", "Chuveiro externo", "Ar-condicionado nas suítes", "Aceita animais de estimação", "Fotografia comercial permitida"])}
<p>Quer saber de algo que não está aqui, como roupa de cama ou utensílios? <a href="/reservas/">Pergunte direto aos anfitriões</a>.</p>
</div>
</section>

<section class="section">
<div class="wrap narrow">
{faq_html(FAQ, "Perguntas frequentes sobre a estrutura")}
</div>
</section>

<section class="section section--tight">
<div class="wrap">{cta_band("Gostou do espaço? Consulte a sua data.")}</div>
</section>
'''

PAGE = dict(
    path=PATH,
    title="Estrutura da Chácara: Piscinas, Área Gourmet e Suítes",
    description="Conheça a estrutura da Chácara Império em Uberaba: 2.500 m², piscina adulto e infantil, área gourmet, salão coberto, campo de futebol, parquinho e 6 suítes.",
    h1="A estrutura da Chácara Império",
    lead="2.500 m² com piscinas, área gourmet, salão coberto, jardins, campo de futebol, parquinho e 6 suítes — veja cada espaço em fotos.",
    eyebrow="Estrutura",
    hero="piscina-luminarias",
    crumbs=[("Início", "/"), ("Estrutura", PATH)],
    wa_key="geral",
    faq=FAQ,
    body=BODY,
    sitemap_images=["piscinas-vista", "churrasqueira", "salao", "pergola-jardim", "parquinho", "sala", "suite-1"],
)
