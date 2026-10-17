from _components import (answer, checks, composer, cta_band, faq_html, figure, img, section_head, tiles)

PATH = "/eventos/confraternizacao-de-empresa/"

FAQ = [
    ("A Chácara Império faz contrato com empresas?",
     "Sim. A Chácara Império aceita contrato de locação temporária para empresas, tanto para eventos quanto para hospedar equipes. Os dados do contrato e a forma de pagamento são combinados com os anfitriões."),
    ("Quantas pessoas cabem numa confraternização de empresa?",
     "Até 250 pessoas, com salão coberto, área gourmet, varandas, campo de futebol, piscinas e estacionamento para 40 carros dentro da chácara."),
    ("A chácara pode hospedar uma equipe de trabalho?",
     "Pode. São 6 suítes com 40 camas, 8 banheiros, ar-condicionado nas suítes, Wi-Fi, espaço de trabalho, cozinha equipada e estacionamento — dentro do perímetro urbano de Uberaba, com acesso asfaltado."),
    ("Que atividades dá para fazer na confraternização?",
     "Churrasco na área gourmet com churrasqueira e fogão a lenha, futebol no campo gramado, piscina, jogos no gramado e um momento de fala ou premiação no salão coberto."),
    ("Com quanta antecedência reservar a confraternização de fim de ano?",
     "As sextas e os sábados de novembro e dezembro são os mais disputados para confraternizações. Consulte sua data pelo WhatsApp (34) 99169-0139 o quanto antes."),
]

BODY = f'''
<section class="section section--tight">
<div class="wrap">
{answer("Para a confraternização da empresa em Uberaba, a <strong>Chácara Império</strong> recebe <strong>até 250 pessoas</strong> com churrasqueira e fogão a lenha, salão coberto, campo de futebol gramado, piscinas e estacionamento para 40 carros, dentro do perímetro urbano e com acesso asfaltado. A chácara aceita <strong>contrato de locação temporária para empresas</strong> e pode hospedar equipes de até 40 pessoas.")}
</div>
</section>

<section class="section section--paper">
<div class="wrap">
{section_head("Formatos", "Um dia fora do escritório que a equipe lembra", None)}
{tiles([
    ("flame", "Confraternização de fim de ano", "Churrasco, piscina e futebol para fechar o ano com a equipe e as famílias."),
    ("users", "Integração e endomarketing", "Atividades no gramado e no campo para aproximar times e receber novos colaboradores."),
    ("star", "Comemoração de metas", "Um almoço especial no salão coberto para celebrar resultados e premiar a equipe."),
    ("briefcase", "Evento para clientes", "Um ambiente acolhedor para receber parceiros fora do ambiente formal."),
    ("bed", "Equipe hospedada", "Até 40 pessoas em 6 suítes, com Wi-Fi e espaço de trabalho, por contrato temporário."),
    ("ball", "Torneio de futebol", "Campo gramado para o clássico entre os setores — com a piscina esperando depois."),
])}
</div>
</section>

<section class="section">
<div class="wrap">
<div class="grid grid-2">
{figure("gourmet-bar", "Área gourmet com churrasqueira e balcão de bar", "(min-width: 640px) 50vw, 100vw")}
{figure("alameda", "Entrada da chácara e o campo de futebol gramado", "(min-width: 640px) 50vw, 100vw")}
{figure("area-coberta-mesas", "Área coberta com mesas rústicas, de frente para a piscina", "(min-width: 640px) 50vw, 100vw")}
{figure("estacionamento", "Estacionamento amplo dentro da chácara", "(min-width: 640px) 50vw, 100vw")}
</div>
</div>
</section>

<section class="section section--sand" id="contrato">
<div class="wrap split">
<div>
{section_head("Contrato para empresas", "Locação temporária com contrato", "A Chácara Império aceita contrato de locação temporária para empresas — para um evento de um dia ou para hospedar uma equipe por um período.")}
{checks(["40 camas em 6 suítes com ar-condicionado e 8 banheiros", "Wi-Fi e espaço de trabalho", "Cozinha equipada e área gourmet", "Estacionamento para 40 carros dentro da chácara", "Portão eletrônico e câmeras externas", "Dentro do perímetro urbano de Uberaba, com acesso asfaltado"])}
<p>Detalhes do contrato, prazos e forma de pagamento são combinados direto com os anfitriões. Veja também a página de <a href="/hospedagem/#empresas">hospedagem para equipes</a>.</p>
</div>
<div class="split-media">{img("suite-5", "(min-width: 900px) 560px, 100vw")}</div>
</div>
</section>

<section class="section">
<div class="wrap split">
<div>
{section_head("Checklist do RH", "O que levantar antes de pedir o orçamento", None)}
{checks(["Data, horário e duração do evento", "Número de colaboradores, convidados e crianças", "Transporte: carros, vans ou ônibus fretado", "Cardápio: churrasco, buffet ou serviço contratado", "Bebidas e quem cuida do gelo", "Atividades: futebol, piscina, sorteios, fala da liderança", "Se alguém vai dormir na chácara", "Dados da empresa para o contrato"])}
</div>
<div>{composer("Confraternização de empresa")}</div>
</div>
</section>

<section class="section section--paper">
<div class="wrap narrow">
{faq_html(FAQ, "Perguntas frequentes de empresas")}
</div>
</section>

<section class="section section--tight">
<div class="wrap">{cta_band("Vamos planejar a confraternização da sua equipe?", "Conte a data, o número de pessoas e o formato do evento. Respondemos com disponibilidade, valores e as condições para empresas.", key="empresa", wa_label="Pedir orçamento para empresa")}</div>
</section>
'''

PAGE = dict(
    path=PATH,
    title="Chácara para Confraternização de Empresa em Uberaba",
    description="Confraternização de empresa em chácara em Uberaba (MG): churrasco, futebol e piscina para até 250 pessoas, com contrato para empresas e pernoite para 40.",
    h1="Chácara para confraternização de empresa em Uberaba",
    lead="Churrasco, futebol, piscina e salão coberto para até 250 pessoas — com contrato de locação temporária para empresas e hospedagem para equipes.",
    eyebrow="Empresas",
    hero="gourmet-noite",
    crumbs=[("Início", "/"), ("Eventos", "/eventos/"), ("Confraternização de empresa", PATH)],
    wa_key="empresa",
    wa_label="Pedir orçamento para empresa",
    faq=FAQ,
    body=BODY,
    sitemap_images=["gourmet-bar", "alameda", "area-coberta-mesas"],
)
