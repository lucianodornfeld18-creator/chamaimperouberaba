import _data as D
from _components import (answer, btn_tel, btn_wa, checks, composer, faq_html, section_head, steps)
from _icons import icon

PATH = "/reservas/"

FAQ = [
    ("A reserva pode ser feita pelo site?",
     "Não. O site só monta a mensagem e abre o WhatsApp. A reserva da Chácara Império é feita somente por telefone ou WhatsApp, direto com os anfitriões."),
    ("Qual é o telefone da Chácara Império?",
     "Telefone e WhatsApp: (34) 99169-0139."),
    ("O que preciso informar para receber o orçamento?",
     "A data (ou as datas), o tipo de evento ou estadia, o número de pessoas e se alguém vai dormir na chácara."),
]

BODY = f'''
<section class="section">
<div class="wrap split">
<div>
{answer("Para reservar a <strong>Chácara Império</strong>, chame no <strong>WhatsApp ou ligue para (34) 99169-0139</strong>. As reservas são feitas somente por telefone ou WhatsApp, direto com os anfitriões Maria Inês e Luciano. Informe a data, o tipo de evento ou estadia e o número de pessoas para receber a disponibilidade e os valores.", "Como reservar")}
<div class="btn-row">{btn_wa("Chamar no WhatsApp", "geral")}{btn_tel()}</div>
{section_head("Passo a passo", "Como funciona", None, tag="h2")}
{steps([
    ("Você manda a consulta", "Pelo WhatsApp ou por telefone, com a data, o tipo de evento ou estadia e quantas pessoas."),
    ("A gente responde", "Com a disponibilidade da data, o valor para o seu caso e o que está incluído."),
    ("Reserva confirmada", "Combinamos os detalhes da reserva e deixamos tudo pronto para você."),
], vertical=True)}
</div>
<div>
{composer()}
<div class="tile mt-2">
<h3 class="mt-0">O que ajuda na resposta</h3>
{checks(["Data ou datas desejadas", "Tipo de evento ou estadia", "Número de convidados e de pessoas para dormir", "Horário de início e término (para eventos)", "Fornecedores que você pretende contratar"])}
</div>
</div>
</div>
</section>

<section class="section section--sand">
<div class="wrap split">
<div>
{section_head("Contato", "Fale com a Chácara Império", None)}
<p class="contact-line">{icon("whatsapp")}<a href="{D.wa_url("geral")}" target="_blank" rel="noopener">WhatsApp {D.PHONE_DISPLAY}</a></p>
<p class="contact-line">{icon("phone")}<a href="{D.TEL_URL}">Telefone {D.PHONE_DISPLAY}</a></p>
<p class="contact-line">{icon("instagram")}<a href="{D.INSTAGRAM}" target="_blank" rel="noopener">{D.INSTAGRAM_HANDLE}</a></p>
<p class="contact-line">{icon("pin")}<span>{D.CITY} – {D.STATE_NAME}, dentro do perímetro urbano</span></p>
<p class="mt-2"><a class="btn btn-ghost" href="{D.wa_url("visita")}" target="_blank" rel="noopener">{icon("calendar")}<span>Quero conhecer a chácara</span></a></p>
</div>
<div>
{faq_html(FAQ, "Dúvidas sobre a reserva")}
</div>
</div>
</section>
'''

PAGE = dict(
    path=PATH,
    title="Como Reservar a Chácara Império – WhatsApp e Telefone",
    description="Reserve a Chácara Império em Uberaba (MG) pelo WhatsApp ou telefone (34) 99169-0139. Veja o passo a passo e o que informar para receber datas e valores.",
    h1="Como reservar",
    lead="As reservas são feitas somente por telefone ou WhatsApp, direto com os anfitriões.",
    eyebrow="Reservas",
    hero="varanda-mesa",
    crumbs=[("Início", "/"), ("Como reservar", PATH)],
    page_type="ContactPage",
    wa_key="geral",
    faq=FAQ,
    body=BODY,
)
