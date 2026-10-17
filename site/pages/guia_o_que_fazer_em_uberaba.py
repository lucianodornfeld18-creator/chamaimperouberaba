import _data as D
from _components import (answer, article_schema, checks, cta_band, faq_html, figure, related, toc)

PATH = "/guia/o-que-fazer-em-uberaba/"
TITLE = "O que fazer em Uberaba (MG): roteiro de 1 a 3 dias"
DESC = ("Turismo em Uberaba (MG): roteiro de 1, 2 ou 3 dias com dinossauros em Peirópolis, Geoparque da "
        "UNESCO, Chico Xavier, Expozebu e passeios com crianças.")
H1 = "O que fazer em Uberaba (MG): roteiros de 1, 2 e 3 dias"
HERO = "casa-gramado"

KM = dict(D.DISTANCES)  # distâncias de rodovia a partir do centro de Uberaba (fonte: _data.py)


def ext(url, text):
    return f'<a href="{url}" target="_blank" rel="noopener">{text}</a>'


UFTM = ext("https://dti.uftm.edu.br/museudosdinossauros", "página do museu na UFTM")
UNESCO = ext("https://www.unesco.org/en/iggp/uberaba-unesco-global-geopark", "página do geoparque na UNESCO")
EXPOZEBU = ext("https://www.expozebu.com.br", "expozebu.com.br")

ANSWER = ("Em um dia, veja o Museu dos Dinossauros, em Peirópolis, de manhã e o centro à tarde — Mercado Municipal "
          "e Igreja Santa Rita — ou troque a tarde pelo roteiro de Chico Xavier. Com dois ou três dias, some o "
          "Museu do Zebu, os museus do Geoparque Uberaba (reconhecido pela UNESCO em 2024) e passeios nos arredores. "
          "Confirme horários e agendamentos.")

FAQ = [
    ("Quantos dias são suficientes para conhecer Uberaba?",
     "Um dia dá para o Museu dos Dinossauros, em Peirópolis, e o centro. Com dois, entram o roteiro de Chico Xavier e o Museu do Zebu. Com três, a Rota dos Museus Orgânicos e um passeio a uma cidade vizinha."),
    ("O que fazer em Uberaba com crianças?",
     "O Museu dos Dinossauros, em Peirópolis, é o programa que mais combina com crianças: segundo a UFTM, tem réplicas de esqueletos, reconstruções em vida, dioramas e mediadores treinados. Depois, a piscina infantil e o parquinho da Chácara Império ajudam a gastar a energia que sobrou."),
    ("Quais lugares de Chico Xavier visitar em Uberaba?",
     "Reportagens de turismo de 2026 citam o Memorial Chico Xavier, a Casa de Memórias e Lembranças (visita com agendamento), o Grupo Espírita da Prece, o túmulo no Cemitério São João Batista e a estátua de bronze no centro. Confirme horários e regras na Prefeitura de Uberaba."),
    ("O que fazer em Uberaba durante a Expozebu?",
     "A Expozebu, organizada pela ABCZ, acontece no Parque de Exposições Fernando Costa, em Uberaba; a 91ª edição foi de 25 de abril a 3 de maio de 2026. Entre os dias de feira, vale reservar um para a manhã em Peirópolis, no Museu dos Dinossauros, ou para o Museu do Zebu, instalado no próprio parque (visita com agendamento)."),
    ("A Chácara Império serve de base para quem vem passear em Uberaba?",
     'Serve para grupos de até 40 pessoas: 6 suítes, 40 camas e 8 banheiros, com check-in a partir das 15h e check-out até as 11h. Fica dentro do perímetro urbano de Uberaba, com acesso asfaltado. Reservas e trajeto até as atrações: telefone ou WhatsApp (34) 99169-0139. Veja a <a href="/hospedagem/">hospedagem para grupos</a>.'),
]

DIA1 = [
    "<strong>Manhã:</strong> Museu dos Dinossauros, no Complexo Cultural e Científico de Peirópolis, ligado à UFTM. Reserve a manhã inteira.",
    "<strong>Tarde:</strong> segundo reportagens de turismo de 2026, o Mercado Municipal (de 1924) reúne queijos, doces e produtos regionais, e a Igreja Santa Rita (de 1854) abriga o Museu de Arte Sacra.",
]

DIA2 = [
    "<strong>Segundo dia, manhã:</strong> Memorial Chico Xavier e Casa de Memórias e Lembranças.",
    "<strong>Segundo dia, tarde:</strong> Museu do Zebu – Edilson Lamartine Mendes, instalado no Parque Fernando Costa e mantido pela ABCZ.",
]

CHICO = [
    "<strong>Memorial Chico Xavier:</strong> reaberto em 2024 após revitalização, com exposição imersiva, objetos pessoais e quatro galerias, segundo o Correio Braziliense.",
    "<strong>Casa de Memórias e Lembranças:</strong> preserva a casa onde o médium morou, com objetos pessoais, fotografias e manuscritos. Integra a Rota dos Museus Orgânicos, com visita por agendamento.",
    "<strong>Grupo Espírita da Prece (Casa da Prece):</strong> centro espírita onde ele atendeu por décadas e foi velado em 2002. Informe-se antes sobre as regras de visita.",
    "<strong>Túmulo:</strong> no Cemitério São João Batista.",
    "<strong>Estátua:</strong> uma estátua de bronze do médium fica no centro da cidade.",
]

PERTO = [
    f"<strong>Uberlândia (cerca de {KM['Uberlândia (MG)']} km):</strong> o Parque do Sabiá tem zoológico, aquário e lago, segundo o Correio Braziliense (julho de 2026).",
    f"<strong>Araxá (cerca de {KM['Araxá (MG)']} km):</strong> o Complexo do Barreiro reúne o Grande Hotel, as Termas e jardins de Burle Marx e é tombado pelo estado, segundo o IEPHA-MG.",
]

BODY = f'''
<section class="section">
<div class="wrap">
<div class="prose">
<p class="updated">Atualizado em {D.UPDATED_HUMAN} · leitura de 7 minutos</p>
{answer(ANSWER)}
{toc([("um-dia", "Roteiro de 1 dia"), ("dois-dias", "Roteiro de 2 dias"), ("tres-dias", "Roteiro de 3 dias"), ("criancas", "Com crianças"), ("chico-xavier", "Chico Xavier"), ("dinossauros", "Dinossauros e Geoparque"), ("expozebu", "Expozebu"), ("perto", "Perto de Uberaba"), ("onde-ficar", "Onde ficar com o grupo"), ("perguntas", "Perguntas frequentes")])}

<h2 id="um-dia">O que fazer em Uberaba em 1 dia</h2>
<p>Com um dia só, divida a cidade em duas frentes: Peirópolis, distrito rural onde fica o Museu dos Dinossauros (entre 20 e 25 km do centro, segundo as fontes consultadas), e o centro. Comece pelo mais distante.</p>
{checks(DIA1)}
<p>Museus costumam fechar um dia por semana, e alguns exigem agendamento. Este guia não traz horários nem ingressos, que mudam: confirme nos canais oficiais.</p>

<h2 id="dois-dias">O que fazer em Uberaba em 2 dias (fim de semana)</h2>
<p>Com dois dias, faça o roteiro de um dia e deixe o segundo para Chico Xavier e para a história do zebu. A Casa de Memórias e Lembranças e o Museu do Zebu pedem agendamento, segundo reportagens de julho de 2026: marque antes de viajar.</p>
{checks(DIA2)}

<h2 id="tres-dias">O que fazer em Uberaba em 3 dias</h2>
<p>A Rota dos Museus Orgânicos, lançada em junho de 2026 e ligada ao Geoparque, reúne nove espaços — ateliês, oficinas, uma doceria e a Casa de Memórias de Chico Xavier —, segundo o Diário do Turismo. As visitas são mediante agendamento.</p>
<p>Para variar: um passeio a uma cidade vizinha (veja abaixo) ou um dia de piscina e churrasco.</p>

<h2 id="criancas">O que fazer em Uberaba com crianças</h2>
<p>O programa que mais combina com os pequenos é o Museu dos Dinossauros. Segundo a UFTM, são três espaços musealizados — um a céu aberto e outro na antiga estação ferroviária de Peirópolis —, com réplicas de esqueletos, reconstruções em vida, dioramas e mediadores treinados para tirar dúvidas. O UAI (dezembro de 2025) descreve a visita como educativa e adequada a crianças e adultos.</p>
<p>Como parte é ao ar livre, leve protetor solar, boné e água. Uma reportagem de julho de 2026 cita reforma na antiga estação: confirme quais espaços estão abertos e, para grupos, use o link de agendamento da {UFTM}.</p>

<h2 id="chico-xavier">O que fazer em Uberaba: roteiro de Chico Xavier</h2>
<p>Chico Xavier viveu em Uberaba por décadas e morreu na cidade em 30 de junho de 2002. Os lugares ligados a ele estão entre os principais motivos de visita:</p>
{checks(CHICO)}
<p>É um roteiro de contemplação, não de pressa. Horários, ingressos e regras mudam: confirme na Prefeitura de Uberaba ou na Fundação Cultural antes de ir.</p>

<h2 id="dinossauros">Dinossauros e Geoparque: a Terra de Gigantes</h2>
<p>Uberaba abriga o Geoparque Uberaba Terra de Gigantes, reconhecido pela UNESCO em 27 de março de 2024. Segundo a Agência Minas, foi o primeiro patrimônio geológico de Minas Gerais reconhecido pela UNESCO, e o território, de cerca de 4,5 mil km², engloba todo o município.</p>
<p>A UNESCO destaca mais de 10 mil fósseis do Cretáceo Superior, entre eles o Uberabatitan ribeiroi, dinossauro de cerca de 27 metros de comprimento (veja a {UNESCO}). De acordo com a UFTM, centenas de fósseis dele foram encontradas em 2004, na Serra da Galga, durante obras na BR-050.</p>
<p>Ao anunciar o título, a Agência Minas listou seis geossítios — Ponte Alta, Caieira, Univerdecidade, Serra da Galga, Santa Rita e Vale Encantado — e dois sítios não geológicos, o Museu dos Dinossauros e o Museu da Cal. Antes de ir a um geossítio por conta própria, confirme com a Prefeitura se ele recebe visitantes.</p>

<h2 id="expozebu">Expozebu: como encaixar a feira no roteiro</h2>
<p>Uberaba, que se apresenta como a Capital Mundial do Zebu, recebe todos os anos a Expozebu, feira organizada pela ABCZ (Associação Brasileira dos Criadores de Zebu) no Parque de Exposições Fernando Costa. A 91ª edição foi de 25 de abril a 3 de maio de 2026, com mais de 400 mil visitantes esperados, segundo a Rádio Itatiaia.</p>
<p>A feira costuma ocupar o fim de abril e o começo de maio: a abertura de 2025 foi em 26 de abril, e a edição de 2024, de 27 de abril a 5 de maio. Há julgamentos, leilões e shows. As datas da próxima saem pela ABCZ; acompanhe em {EXPOZEBU}.</p>
<p>Entre os dias de feira, reserve um para este roteiro: a manhã em Peirópolis ou o Museu do Zebu, no próprio parque. Para o grupo ficar junto, veja a <a href="/hospedagem/expozebu/">hospedagem na Expozebu</a>.</p>

<h2 id="perto">O que fazer perto de Uberaba</h2>
<p>Distâncias por rodovia, a partir do centro de Uberaba:</p>
{checks(PERTO)}

<h2 id="onde-ficar">Onde ficar com o grupo: Chácara Império</h2>
<p>Roteiro com crianças, avós e amigos pede um lugar onde todos fiquem juntos. A Chácara Império hospeda até 40 pessoas em 6 suítes, com 40 camas, 8 banheiros, ar-condicionado nas suítes, Wi-Fi e cozinha equipada. Os hóspedes podem usar todo o espaço: piscina adulto e infantil, área gourmet com churrasqueira e fogão a lenha, campo de futebol gramado e parquinho.</p>
{figure("piscinas-vista", "Piscina adulto e piscina infantil da Chácara Império, vistas do alto")}
<p>O check-in é a partir das 15h e o check-out, até as 11h. A chácara fica dentro do perímetro urbano de Uberaba, com acesso asfaltado, e aceita animais de estimação. Peça o endereço e o trajeto até as atrações pelo WhatsApp (34) 99169-0139; as reservas são somente por telefone ou WhatsApp.</p>
{figure("suite-1", "Suíte da Chácara Império com cama de casal e beliches")}
<p>Antes de arrumar a mala, veja <a href="/guia/o-que-levar-para-a-chacara/">o que levar para a chácara</a>.</p>

{faq_html(FAQ, "Perguntas frequentes")}
<p class="updated mt-2">Fontes consultadas em outubro de 2026: UNESCO, UFTM, Agência Minas, ABCZ, Rádio Itatiaia, Canal Rural, CNA, Diário do Turismo, Catraca Livre, UAI, Correio Braziliense, Diário do Grande ABC e IEPHA-MG.</p>
</div>
</div>
</section>

<section class="section section--sand">
<div class="wrap">
<h2>Leia também</h2>
{related([
    ("/hospedagem/", "suite-1", "Hospedagem para grupos", "A chácara inteira para até 40 pessoas, em 6 suítes."),
    ("/hospedagem/expozebu/", "piscina-luminarias", "Hospedagem na Expozebu", "Para comitivas, equipes e famílias que vêm à feira."),
    ("/como-chegar/", "alameda", "Como chegar", "Distâncias de rodovia até Uberaba e orientações para chegar."),
])}
</div>
</section>

<section class="section section--tight">
<div class="wrap">{cta_band("Vai passar uns dias em Uberaba com o grupo?", key="hospedagem")}</div>
</section>
'''

PAGE = dict(
    path=PATH,
    title=TITLE,
    description=DESC,
    h1=H1,
    lead="Dinossauros, Chico Xavier, Expozebu e passeios para a família: como montar de 1 a 3 dias na cidade.",
    eyebrow="Guia",
    hero=HERO,
    crumbs=[("Início", "/"), ("Guia", "/guia/"), ("O que fazer em Uberaba", PATH)],
    page_type="WebPage",
    wa_key="hospedagem",
    faq=FAQ,
    schema=[article_schema(PATH, H1, DESC, HERO, "2026-10-16")],
    body=BODY,
    guide=dict(summary="Roteiros de 1, 2 e 3 dias: dinossauros, Geoparque, Chico Xavier, Expozebu e crianças.",
               minutes=7, pid=HERO),
)
