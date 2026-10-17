import _data as D
from _components import (answer, checks, composer, cta_band, faq_html, features, figure, img,
                         section_head, tiles)

PATH = "/hospedagem/"

FAQ = [
    ("Quantas pessoas podem se hospedar na Chácara Império?",
     "Até 40 pessoas, em 6 suítes com 40 camas (camas de casal e beliches) e 8 banheiros. As suítes têm ar-condicionado."),
    ("Qual é o horário de check-in e de check-out?",
     "O check-in é a partir das 15h e o check-out até as 11h."),
    ("A Chácara Império aceita animais de estimação?",
     "Sim, a chácara aceita animais de estimação. Leve ração, potes, guia e caminha do seu pet."),
    ("Roupa de cama e toalhas estão incluídas?",
     "Confirme pelo WhatsApp (34) 99169-0139 o que está incluído na sua reserva antes de arrumar a mala — assim você leva só o que precisa."),
    ("A chácara tem Wi-Fi?",
     "Tem Wi-Fi e um espaço de trabalho, para quem precisa resolver alguma coisa durante a estadia."),
    ("Dá para alugar a chácara para uma equipe de trabalho?",
     "Dá. A Chácara Império aceita contrato de locação temporária para empresas, com hospedagem para até 40 pessoas, estacionamento para 40 carros e acesso asfaltado dentro do perímetro urbano de Uberaba."),
]

BODY = f'''
<section class="section section--tight">
<div class="wrap">
{answer("A <strong>Chácara Império</strong> aluga a chácara inteira em Uberaba (MG) para fins de semana, feriados e temporadas: <strong>até 40 pessoas em 6 suítes</strong> com ar-condicionado, 40 camas e 8 banheiros, piscina adulto e infantil, área gourmet com churrasqueira e fogão a lenha, campo de futebol, parquinho, Wi-Fi e estacionamento para 40 carros. Aceita pets. Check-in às 15h e check-out às 11h.")}
</div>
</section>

<section class="section section--paper">
<div class="wrap split">
<div>
{section_head("A chácara inteira para o seu grupo", "Tudo é seu durante a estadia", "Na hospedagem, os hóspedes podem usar todo o espaço da chácara — da piscina ao campo, da cozinha ao fogão a lenha.")}
{features([("bed", "6 suítes · 40 camas"), ("bath", "8 banheiros"), ("snow", "Ar-condicionado nas suítes"), ("home", "Sala de estar e jantar"), ("utensils", "Cozinha equipada"), ("flame", "Churrasqueira e fogão a lenha"), ("waves", "Piscina adulto e infantil"), ("shower", "Chuveiro externo"), ("ball", "Campo de futebol"), ("smile", "Parquinho"), ("wifi", "Wi-Fi e espaço de trabalho"), ("car", "Estacionamento para 40 carros"), ("shield", "Portão eletrônico e câmeras externas"), ("paw", "Aceita animais de estimação")])}
</div>
<div class="split-media">{img("piscina-casa-principal", "(min-width: 900px) 560px, 100vw")}{img("sala", "220px", cls="stack")}</div>
</div>
</section>

<section class="section">
<div class="wrap">
{section_head("As suítes", "Camas para a família inteira", "As 6 suítes misturam camas de casal e beliches de madeira, todas com ar-condicionado. Algumas têm também ventilador de teto e forro de madeira.")}
<div class="grid grid-3">
{figure("suite-1", None, "(min-width: 960px) 33vw, (min-width: 640px) 50vw, 100vw")}
{figure("suite-2", None, "(min-width: 960px) 33vw, (min-width: 640px) 50vw, 100vw")}
{figure("suite-4", None, "(min-width: 960px) 33vw, (min-width: 640px) 50vw, 100vw")}
{figure("suite-5", None, "(min-width: 960px) 33vw, (min-width: 640px) 50vw, 100vw")}
{figure("suite-6", None, "(min-width: 960px) 33vw, (min-width: 640px) 50vw, 100vw")}
{figure("cozinha", None, "(min-width: 960px) 33vw, (min-width: 640px) 50vw, 100vw")}
</div>
</div>
</section>

<section class="section section--sand">
<div class="wrap">
{section_head("Para quem é", "Quem costuma se hospedar numa chácara em Uberaba", None)}
{tiles([
    ("users", "Famílias grandes", "Avós, filhos, netos e o cachorro, cada núcleo na sua suíte."),
    ("calendar", "Feriados prolongados", "Três ou quatro dias com a turma toda num espaço completo."),
    ("heart", "Convidados de casamento", "Família e padrinhos hospedados juntos, no mesmo lugar da festa."),
    ("star", "Grupos da Expozebu", "Comitivas e equipes que vêm para a feira no Parque Fernando Costa."),
    ("briefcase", "Equipes de trabalho", "Hospedagem por contrato temporário para empresas."),
    ("sun", "Amigos de fim de semana", "Piscina, churrasco e futebol sem hora para acabar."),
])}
<p class="mt-2">Vem para a Expozebu? Veja a página de <a href="/hospedagem/expozebu/">hospedagem para a Expozebu</a>.</p>
</div>
</section>

<section class="section" id="empresas">
<div class="wrap split reverse">
<div>
{section_head("Hospedagem para empresas", "Equipes hospedadas por contrato", "A Chácara Império aceita contrato de locação temporária para empresas. Para equipes que vêm trabalhar em Uberaba, ela reúne tudo num endereço só.")}
{checks(["Até 40 pessoas em 6 suítes, com 8 banheiros", "Wi-Fi e espaço de trabalho", "Cozinha equipada para as refeições da equipe", "Estacionamento para 40 veículos dentro da chácara", "Portão eletrônico e câmeras externas", "Dentro do perímetro urbano, com acesso asfaltado"])}
<p>Prazos, dados do contrato e pagamento são combinados direto com os anfitriões.</p>
</div>
<div class="split-media">{img("estacionamento", "(min-width: 900px) 560px, 100vw")}</div>
</div>
</section>

<section class="section section--paper">
<div class="wrap split">
<div>
{section_head("Regras da casa", "Combinados para uma estadia tranquila", None)}
{checks([f"Check-in a partir das {D.FACTS['checkin'].replace(':00', 'h')} e check-out até as {D.FACTS['checkout'].replace(':00', 'h')}", "Animais de estimação são bem-vindos", "Câmeras de segurança externas nas varandas, no estacionamento e no portão de entrada", "Antes de sair: recolher o lixo, desligar tudo, devolver as chaves e trancar a casa", "Confira seus pertences ao sair — a chácara não se responsabiliza por objetos esquecidos"])}
<p>Para a mala, use o <a href="/guia/o-que-levar-para-a-chacara/">checklist do que levar para a chácara</a>.</p>
</div>
<div>{composer("Hospedagem (fim de semana / feriado)")}</div>
</div>
</section>

<section class="section">
<div class="wrap narrow">
{faq_html(FAQ, "Perguntas frequentes sobre hospedagem")}
</div>
</section>

<section class="section section--tight">
<div class="wrap">{cta_band("Quais são as datas da sua estadia?", "Mande as datas de chegada e saída e quantas pessoas vão se hospedar. Respondemos com disponibilidade e valores.", key="hospedagem", wa_label="Consultar hospedagem")}</div>
</section>
'''

PAGE = dict(
    path=PATH,
    title="Chácara para Alugar no Fim de Semana em Uberaba",
    description="Alugue a chácara inteira em Uberaba (MG) para fins de semana, feriados e temporadas: 6 suítes, 40 camas, piscinas, churrasqueira e pet friendly.",
    h1="Hospedagem em chácara em Uberaba para até 40 pessoas",
    lead="A chácara inteira para a sua família ou o seu grupo: 6 suítes com ar-condicionado, piscinas, área gourmet, campo de futebol — e o pet também vem.",
    eyebrow="Hospedagem",
    hero="piscinas-casa",
    crumbs=[("Início", "/"), ("Hospedagem", PATH)],
    wa_key="hospedagem",
    wa_label="Consultar hospedagem",
    faq=FAQ,
    body=BODY,
    sitemap_images=["suite-1", "suite-2", "cozinha", "sala"],
)
