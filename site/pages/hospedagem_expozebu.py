from _components import (answer, checks, composer, cta_band, faq_html, figure, img, section_head, tiles)

PATH = "/hospedagem/expozebu/"

FAQ = [
    ("Quando acontece a Expozebu?",
     "A Expozebu costuma acontecer entre o fim de abril e o início de maio, no Parque Fernando Costa, em Uberaba. A 91ª edição foi de 25 de abril a 3 de maio de 2026. As datas de cada ano são divulgadas pela ABCZ."),
    ("Quantas pessoas a Chácara Império hospeda durante a Expozebu?",
     "Até 40 pessoas, em 6 suítes com 40 camas e 8 banheiros, com estacionamento para 40 carros dentro da chácara."),
    ("A chácara fica perto do Parque Fernando Costa?",
     "A Chácara Império fica dentro do perímetro urbano de Uberaba, com acesso asfaltado. Peça a localização pelo WhatsApp (34) 99169-0139 para calcular o trajeto até o Parque Fernando Costa."),
    ("Dá para trabalhar da chácara durante a feira?",
     "Dá. A chácara tem Wi-Fi e espaço de trabalho — útil para quem acompanha leilões e negócios durante a Expozebu."),
    ("Com quanta antecedência reservar para a Expozebu?",
     "O quanto antes. A organização esperava mais de 400 mil visitantes na edição de 2026, e a hospedagem em Uberaba fica disputada no período. Consulte pelo WhatsApp assim que souber as datas do seu grupo."),
]

BODY = f'''
<section class="section section--tight">
<div class="wrap">
{answer("A Expozebu, promovida pela ABCZ no Parque Fernando Costa, em Uberaba, é apontada como a maior feira de gado zebu do mundo — e a cidade fica cheia no período. Para comitivas, equipes de leilão e famílias, a <strong>Chácara Império</strong> hospeda <strong>até 40 pessoas em 6 suítes</strong>, com estacionamento para 40 carros, Wi-Fi, churrasqueira e piscina, dentro do perímetro urbano e com acesso asfaltado.")}
</div>
</section>

<section class="section section--paper">
<div class="wrap split">
<div>
{section_head("A feira", "Expozebu em poucas linhas", None)}
<ul class="checks">
<li><span><strong>O quê:</strong> exposição e feira de negócios do gado zebu, com julgamentos das raças, leilões, palestras e shows.</span></li>
<li><span><strong>Onde:</strong> Parque Fernando Costa, em Uberaba (MG).</span></li>
<li><span><strong>Quem organiza:</strong> ABCZ — Associação Brasileira dos Criadores de Zebu.</span></li>
<li><span><strong>Quando:</strong> costuma acontecer entre o fim de abril e o início de maio. A 91ª edição foi de 25 de abril a 3 de maio de 2026.</span></li>
<li><span><strong>Movimento:</strong> para 2026, a organização esperava mais de 400 mil visitantes ao longo da programação.</span></li>
</ul>
<p class="note">As datas e a programação de cada edição são divulgadas pela ABCZ. Confira sempre no site oficial antes de fechar a viagem.</p>
</div>
<div class="split-media">{img("piscina-luminarias", "(min-width: 900px) 560px, 100vw")}</div>
</div>
</section>

<section class="section">
<div class="wrap">
{section_head("Por que uma chácara", "O grupo inteiro junto durante a feira", "Em vez de dividir a comitiva em vários quartos de hotel, a chácara reúne todos num lugar só — com espaço para o churrasco depois de um dia inteiro de parque.")}
{tiles([
    ("users", "Comitiva junta", "Até 40 pessoas em 6 suítes, com 40 camas e 8 banheiros."),
    ("car", "Estacionamento próprio", "Vagas para 40 carros dentro da chácara, com portão eletrônico."),
    ("road", "Acesso fácil", "Dentro do perímetro urbano de Uberaba, por acesso asfaltado."),
    ("laptop", "Wi-Fi e espaço de trabalho", "Para acompanhar leilões, mandar propostas e fechar negócios."),
    ("flame", "Churrasco no fim do dia", "Área gourmet com churrasqueira e fogão a lenha."),
    ("waves", "Descanso de verdade", "Piscina, varandas e ar-condicionado nas suítes."),
])}
</div>
</section>

<section class="section section--sand">
<div class="wrap">
<div class="grid grid-3">
{figure("gourmet-noite", "Área gourmet à noite", "(min-width: 960px) 33vw, (min-width: 640px) 50vw, 100vw")}
{figure("suite-2", "Uma das 6 suítes", "(min-width: 960px) 33vw, (min-width: 640px) 50vw, 100vw")}
{figure("estacionamento", "Estacionamento dentro da chácara", "(min-width: 960px) 33vw, (min-width: 640px) 50vw, 100vw")}
</div>
</div>
</section>

<section class="section">
<div class="wrap split">
<div>
{section_head("Para reservar", "Mande estas informações", None)}
{checks(["Datas de chegada e de saída do grupo", "Quantas pessoas e quantos veículos", "Se o grupo é de criadores, equipe de leilão, empresa ou família", "Se precisa de contrato em nome de empresa"])}
<p>Quer aproveitar a viagem? Veja <a href="/guia/o-que-fazer-em-uberaba/">o que fazer em Uberaba</a> entre um dia e outro de feira.</p>
</div>
<div>{composer("Hospedagem na Expozebu")}</div>
</div>
</section>

<section class="section section--paper">
<div class="wrap narrow">
{faq_html(FAQ, "Perguntas frequentes sobre hospedagem na Expozebu")}
<p class="updated mt-2">Fontes sobre a Expozebu: Canal Rural e Itatiaia (edição 2026), Forbes Agro. Datas oficiais: ABCZ.</p>
</div>
</section>

<section class="section section--tight">
<div class="wrap">{cta_band("Garanta a hospedagem do seu grupo na Expozebu", "As datas da feira são as mais disputadas do ano em Uberaba. Mande as datas e o tamanho do grupo pelo WhatsApp.", key="expozebu", wa_label="Consultar hospedagem na Expozebu")}</div>
</section>
'''

PAGE = dict(
    path=PATH,
    title="Hospedagem para a Expozebu em Uberaba: Chácara para Grupos",
    description="Vai à Expozebu? Hospede seu grupo numa chácara em Uberaba (MG): até 40 pessoas em 6 suítes, estacionamento para 40 carros, Wi-Fi, piscina e churrasqueira.",
    h1="Hospedagem para a Expozebu: chácara para grupos em Uberaba",
    lead="Comitivas, equipes de leilão e famílias juntas num só lugar durante a maior feira do zebu — com 6 suítes, estacionamento e churrasqueira.",
    eyebrow="Expozebu",
    hero="alameda",
    og="piscina-banco",
    crumbs=[("Início", "/"), ("Hospedagem", "/hospedagem/"), ("Expozebu", PATH)],
    wa_key="expozebu",
    wa_label="Consultar hospedagem na Expozebu",
    faq=FAQ,
    body=BODY,
    sitemap_images=["gourmet-noite", "suite-2"],
)
