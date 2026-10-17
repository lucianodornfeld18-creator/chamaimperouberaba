import _data as D
from _components import (answer, btn_wa, checks, composer, cta_band, faq_html, features, figure, img,
                         section_head, steps)
from _icons import icon

PATH = "/eventos/casamento/"

FAQ = [
    ("Quantos convidados cabem num casamento na Chácara Império?",
     "Até 250 convidados. A recepção acontece no salão coberto, na área gourmet e nas varandas, e a chácara tem estacionamento para 40 carros."),
    ("Dá para fazer a cerimônia e a festa no mesmo lugar?",
     "Sim. Os jardins com pérgolas de madeira e coqueiros servem de cenário para a cerimônia, e a festa segue no salão coberto e nas varandas, sem deslocamento dos convidados."),
    ("Os noivos e a família podem dormir na chácara?",
     "Podem. A Chácara Império hospeda até 40 pessoas em 6 suítes com ar-condicionado, 40 camas e 8 banheiros — noivos, padrinhos e família passam a noite no local."),
    ("E se chover no dia do casamento?",
     "O salão coberto com forro de madeira, a área gourmet e as varandas cobertas funcionam como plano B. Combine com os anfitriões a montagem alternativa da cerimônia."),
    ("Posso escolher meu buffet, decoração e música?",
     "Os fornecedores e as regras de som são combinados direto com os anfitriões. Envie pelo WhatsApp (34) 99169-0139 quem você pretende contratar e tire as dúvidas antes de fechar."),
    ("Com quanta antecedência devo reservar a data?",
     "Quanto antes, melhor: sábados e datas próximas a feriados costumam ser os primeiros a fechar. Consulte a disponibilidade da sua data pelo WhatsApp."),
]

BODY = f'''
<section class="section section--tight">
<div class="wrap">
{answer("Para casar em chácara em Uberaba, a <strong>Chácara Império</strong> oferece jardins com pérgolas de madeira para a cerimônia, salão coberto e área gourmet para a recepção de <strong>até 250 convidados</strong>, piscinas iluminadas para as fotos da noite, estacionamento para 40 carros e <strong>6 suítes com 40 camas</strong> para os noivos, os padrinhos e a família passarem a noite. Fica dentro do perímetro urbano, com acesso asfaltado.")}
</div>
</section>

<section class="section section--paper">
<div class="wrap split">
<div>
{section_head("Do sim à festa", "Tudo no mesmo lugar, sem pressa para ir embora", "Num casamento em chácara, o dia inteiro acontece num só endereço. Na Chácara Império, ele pode ser assim:")}
{steps([
    ("Preparação", "Noiva e noivo se arrumam com calma nas suítes, com ar-condicionado e banheiro privativo."),
    ("Cerimônia no jardim", "Pérgolas de madeira, gramado e coqueiros formam o cenário do sim — de dia ou ao entardecer."),
    ("Recepção e pernoite", "A festa segue no salão coberto e nas varandas; depois, quem é da casa dorme na chácara."),
], vertical=True)}
</div>
<div class="split-media">{img("pergola-jardim", "(min-width: 900px) 560px, 100vw")}{img("carro-de-boi-noite", "220px", cls="stack")}</div>
</div>
</section>

<section class="section">
<div class="wrap">
{section_head("O espaço", "Cenários para cada momento do casamento", "Fotos reais da chácara. As pérgolas, o carro de boi decorativo e as piscinas iluminadas rendem fotos lindas — de dia e de noite.")}
<div class="grid grid-2">
{figure("pergola-varanda", "Pérgola de madeira sobre o gramado — um cenário natural para a cerimônia", "(min-width: 640px) 50vw, 100vw")}
{figure("salao", "Salão coberto com forro de madeira para a recepção", "(min-width: 640px) 50vw, 100vw")}
{figure("piscinas-noite", "As piscinas iluminadas à noite, ótimas para fotos dos noivos", "(min-width: 640px) 50vw, 100vw")}
{figure("jardim-noite", "Jardim iluminado à noite, com pérgola e coqueiros", "(min-width: 640px) 50vw, 100vw")}
</div>
</div>
</section>

<section class="section section--sand">
<div class="wrap split reverse">
<div>
{section_head("Hospedagem dos noivos e da família", "A festa acaba, a família fica", "Depois de um dia longo, ninguém precisa pegar a estrada. A chácara acomoda até 40 pessoas.")}
{features([("bed", "6 suítes com ar-condicionado"), ("users", "40 camas — casal e beliches"), ("bath", "8 banheiros"), ("utensils", "Cozinha para o café do dia seguinte"), ("waves", "Piscina para o almoço pós-casamento"), ("paw", "O pet da família também é bem-vindo")])}
<p class="mt-2">Os horários de entrada e saída num casamento são combinados com os anfitriões. Na hospedagem comum, o check-in é a partir das 15h e o check-out até as 11h.</p>
</div>
<div class="split-media">{img("suite-1", "(min-width: 900px) 560px, 100vw")}</div>
</div>
</section>

<section class="section">
<div class="wrap split">
<div>
{section_head("Planejamento", "O que combinar antes de fechar o casamento", None)}
{checks(["Data, horário da cerimônia e horário de término da festa", "Número de convidados adultos e crianças", "Onde será a cerimônia — e o plano B no salão coberto se chover", "Buffet, bolo, bebidas e quem cuida do gelo", "Decoração: o que pode ser fixado e quando a montagem começa", "Som, DJ ou banda e o horário combinado para a música", "Quem vai dormir na chácara e em quais suítes", "Lista de convidados para a entrada pelo portão"])}
<p>Quer um passo a passo completo? Leia o <a href="/guia/casamento-em-chacara/">guia de casamento em chácara</a>, com cronograma, dicas de decoração e até o que vestir.</p>
</div>
<div>{composer("Casamento")}</div>
</div>
</section>

<section class="section section--paper">
<div class="wrap narrow">
{faq_html(FAQ, "Perguntas frequentes sobre casamento na chácara")}
</div>
</section>

<section class="section section--tight">
<div class="wrap">{cta_band("Já escolheram a data? Vamos ver se ela está livre.", "Mande a data, o horário e o número de convidados pelo WhatsApp. A gente responde com disponibilidade e valores para o casamento de vocês.", key="casamento", wa_label="Consultar data do casamento")}</div>
</section>
'''

PAGE = dict(
    path=PATH,
    title="Chácara para Casamento em Uberaba | Chácara Império",
    description="Casamento em chácara em Uberaba (MG): cerimônia no jardim com pérgolas, festa para até 250 convidados no salão coberto e pernoite para noivos e família.",
    h1="Chácara para casamento em Uberaba",
    lead="Cerimônia entre pérgolas e coqueiros, recepção para até 250 convidados e os noivos — e a família toda — dormindo na própria chácara.",
    eyebrow="Casamento",
    hero="pergola-varanda",
    crumbs=[("Início", "/"), ("Eventos", "/eventos/"), ("Casamento", PATH)],
    wa_key="casamento",
    wa_label="Consultar data do casamento",
    faq=FAQ,
    body=BODY,
    sitemap_images=["pergola-jardim", "salao", "piscinas-noite", "jardim-noite"],
)
