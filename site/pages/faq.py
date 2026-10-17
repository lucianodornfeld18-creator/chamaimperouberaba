import _data as D
from _components import (answer, cta_band, faq_html, toc)

PATH = "/perguntas-frequentes/"

GROUPS = [
    ("reservas", "Reservas e valores", [
        ("Como reservar a Chácara Império?",
         "As reservas são feitas somente por telefone ou WhatsApp, no (34) 99169-0139, direto com os anfitriões Maria Inês e Luciano. Informe a data, o tipo de evento ou estadia e o número de pessoas."),
        ("Quanto custa alugar a Chácara Império?",
         "O valor depende da data, do tipo de evento, do número de convidados, da duração e de haver pernoite. Feriados, fim de ano e o período da Expozebu são os mais procurados. Peça um orçamento pelo WhatsApp (34) 99169-0139."),
        ("Dá para reservar pelo site?",
         "O site não faz reservas: ele abre o WhatsApp com a sua mensagem pronta. A confirmação é sempre feita com os anfitriões, por telefone ou WhatsApp."),
        ("Posso conhecer a chácara antes de fechar?",
         "Peça pelo WhatsApp (34) 99169-0139 para combinar com os anfitriões a melhor forma de conhecer o espaço."),
        ("A Chácara Império faz contrato para empresas?",
         "Sim. A chácara aceita contrato de locação temporária para empresas, para eventos e para hospedar equipes."),
        ("Com quanta antecedência devo reservar?",
         "Quanto antes, melhor — principalmente para sábados, feriados prolongados, novembro e dezembro e o período da Expozebu, que costumam ser os primeiros a fechar."),
    ]),
    ("eventos", "Eventos", [
        ("Quantos convidados cabem num evento na Chácara Império?",
         "Até 250 convidados, com estacionamento para 40 carros dentro da chácara."),
        ("Que tipos de evento a chácara recebe?",
         "Casamentos, aniversários e festas de 15 anos, festas infantis, confraternizações de empresa, reuniões de família (bodas, batizados, chá revelação), Natal, Réveillon e ensaios fotográficos."),
        ("A chácara tem espaço coberto para o caso de chuva?",
         "Tem salão coberto com forro de madeira, área gourmet coberta e varandas — o plano B natural para dias de chuva."),
        ("Posso trazer meu próprio buffet, decoração e som?",
         "Fornecedores, montagem e regras de som são combinados com os anfitriões antes da reserva. Conte pelo WhatsApp o que você pretende contratar."),
        ("Os convidados podem dormir na chácara depois da festa?",
         "Até 40 pessoas podem dormir na chácara, em 6 suítes com 40 camas e 8 banheiros."),
        ("A chácara pode ser usada para fotos e gravações?",
         "Sim, a fotografia comercial é permitida. Há pérgolas, carro de boi decorativo, coqueiros, piscinas e jardins iluminados à noite como cenário."),
    ]),
    ("hospedagem", "Hospedagem", [
        ("Quantas pessoas podem se hospedar?",
         "Até 40 pessoas, em 6 suítes com ar-condicionado, 40 camas (camas de casal e beliches) e 8 banheiros."),
        ("Qual é o horário de check-in e check-out?",
         "Check-in a partir das 15h e check-out até as 11h."),
        ("A hospedagem é da chácara inteira?",
         "Sim. Na hospedagem, o grupo pode usar todo o espaço da chácara: piscinas, área gourmet, campo, parquinho, casa e suítes."),
        ("Roupa de cama e toalhas estão incluídas?",
         "Confirme pelo WhatsApp (34) 99169-0139 o que está incluído na sua reserva antes de arrumar a mala."),
        ("A chácara aceita animais de estimação?",
         "Sim, a Chácara Império aceita animais de estimação."),
        ("Tem Wi-Fi?",
         "Tem Wi-Fi e um espaço de trabalho."),
    ]),
    ("estrutura", "Estrutura", [
        ("A Chácara Império tem piscina?",
         "Tem piscina adulto e piscina infantil, com deque de pedra, espreguiçadeiras, luminárias e chuveiro externo."),
        ("Tem churrasqueira?",
         "Tem churrasqueira de tijolinho e fogão a lenha na área gourmet coberta, com bancada de granito, pia e balcão de bar."),
        ("Tem campo de futebol?",
         "Tem campo de futebol gramado, cercado por alambrado."),
        ("Tem espaço para crianças?",
         "Tem parquinho com balanços e escorregador, piscina infantil e bastante gramado."),
        ("As suítes têm ar-condicionado?",
         "Sim, as 6 suítes têm ar-condicionado."),
        ("Qual é o tamanho da chácara?",
         "A Chácara Império tem 2.500 m²."),
    ]),
    ("localizacao", "Localização e chegada", [
        ("Onde fica a Chácara Império?",
         "Em Uberaba, no Triângulo Mineiro (MG), dentro do perímetro urbano, com acesso asfaltado e portão eletrônico. A localização exata é enviada pelo WhatsApp."),
        ("O acesso é asfaltado?",
         "Sim, o acesso à chácara é asfaltado."),
        ("Tem estacionamento?",
         "Sim, estacionamento dentro da chácara para 40 carros."),
        ("A chácara é segura?",
         "A entrada tem portão eletrônico e há câmeras de segurança externas nas varandas, no estacionamento e no portão."),
    ]),
]

ALL = [qa for _, _, items in GROUPS for qa in items]

blocks = "".join(f'<div class="faq-group">{faq_html(items, title, hid)}</div>' for hid, title, items in GROUPS)

BODY = f'''
<section class="section">
<div class="wrap narrow">
{answer("A <strong>Chácara Império</strong>, em Uberaba (MG), recebe eventos de até 250 convidados e hospeda até 40 pessoas em 6 suítes. Tem piscina adulto e infantil, área gourmet com churrasqueira e fogão a lenha, salão coberto, campo de futebol, parquinho e estacionamento para 40 carros. Aceita pets. Check-in às 15h, check-out às 11h. Reservas somente por telefone ou WhatsApp: (34) 99169-0139.", "Resumo")}
{toc([(hid, title) for hid, title, _ in GROUPS])}
{blocks}
<p class="updated mt-3">Respostas revisadas em {D.UPDATED_HUMAN}. Não encontrou sua dúvida? <a href="{D.wa_url("geral")}" target="_blank" rel="noopener">Pergunte no WhatsApp</a>.</p>
</div>
</section>

<section class="section section--tight">
<div class="wrap">{cta_band("Ainda ficou alguma dúvida?", "Fale direto com os anfitriões pelo WhatsApp ou telefone. A gente responde com carinho — e com a disponibilidade da sua data.")}</div>
</section>
'''

PAGE = dict(
    path=PATH,
    title="Perguntas Frequentes – Chácara Império em Uberaba",
    description="Respostas sobre a Chácara Império em Uberaba: capacidade, valores, reservas, hospedagem, check-in, pets, piscinas, churrasqueira, estacionamento e localização.",
    h1="Perguntas frequentes",
    lead="Tudo o que costumam perguntar antes de reservar — eventos, hospedagem, estrutura, localização e como reservar.",
    eyebrow="Dúvidas",
    hero="varanda-piscina",
    crumbs=[("Início", "/"), ("Perguntas frequentes", PATH)],
    page_type="FAQPage",
    hero_ctas="",
    wa_key="geral",
    faq=ALL,
    body=BODY,
)
