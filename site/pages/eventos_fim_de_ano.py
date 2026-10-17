from _components import (answer, checks, composer, cta_band, faq_html, figure, img, section_head, tiles)

PATH = "/eventos/natal-e-reveillon/"

FAQ = [
    ("A Chácara Império aluga para o Réveillon?",
     "Sim. A chácara pode ser reservada para a virada do ano, com festa para até 250 convidados e hospedagem para até 40 pessoas em 6 suítes. As datas de fim de ano são as primeiras a fechar — consulte cedo pelo WhatsApp."),
    ("Dá para passar o Natal com a família na chácara?",
     "Dá. A ceia pode ser na área gourmet ou no salão coberto, com churrasqueira, fogão a lenha e cozinha equipada, e a família dorme nas suítes com ar-condicionado."),
    ("Quantas pessoas podem dormir na chácara no fim de ano?",
     "Até 40 pessoas, em 6 suítes com 40 camas e 8 banheiros."),
    ("A piscina fica iluminada à noite?",
     "Sim. A área da piscina tem luminárias, e os jardins e a pérgola também ficam iluminados à noite."),
    ("Como funciona a reserva para o fim de ano?",
     "Pelo telefone ou WhatsApp (34) 99169-0139: informe as datas de chegada e saída e o número de pessoas para receber disponibilidade e as condições do período."),
]

BODY = f'''
<section class="section section--tight">
<div class="wrap">
{answer("Para passar o Natal ou o Réveillon numa chácara em Uberaba, a <strong>Chácara Império</strong> reúne festa e pernoite: ceia na área gourmet ou no salão coberto, piscina iluminada à noite e <strong>6 suítes com ar-condicionado para até 40 pessoas</strong>. Recebe até 250 convidados. As datas de fim de ano costumam ser as primeiras a fechar — consulte com antecedência pelo WhatsApp (34) 99169-0139.")}
</div>
</section>

<section class="section section--paper">
<div class="wrap">
{section_head("Fim de ano", "Natal com a família, Réveillon com quem você ama", None)}
{tiles([
    ("star", "Ceia de Natal", "Mesa posta na área gourmet ou no salão coberto, fogão a lenha aceso e as crianças correndo no gramado."),
    ("sparkle", "Virada do ano", "Jardins, pérgola e piscinas iluminados para receber o ano novo do lado de fora."),
    ("bed", "Ninguém dirige depois", "Até 40 pessoas dormindo na chácara: a festa termina e todos já estão em casa."),
    ("sun", "Dia 1º na piscina", "Piscina adulto e infantil para o primeiro dia do ano, sem pressa."),
    ("users", "Família e amigos", "Espaço para até 250 convidados se a festa for maior que a família."),
    ("paw", "Pet incluído", "O cachorro da família passa a virada junto — a chácara aceita animais."),
])}
</div>
</section>

<section class="section">
<div class="wrap">
<div class="grid grid-2">
{figure("piscinas-noite", "Piscinas iluminadas à noite", "(min-width: 640px) 50vw, 100vw")}
{figure("gourmet-noite", "Área gourmet à noite, de frente para a piscina", "(min-width: 640px) 50vw, 100vw")}
{figure("pergola-noite", "Pérgola iluminada no jardim", "(min-width: 640px) 50vw, 100vw")}
{figure("varanda-noite", "Varanda coberta e jardim à noite", "(min-width: 640px) 50vw, 100vw")}
</div>
</div>
</section>

<section class="section section--sand">
<div class="wrap split">
<div>
{section_head("Planejando o fim de ano", "O que definir primeiro", "Fim de ano tem mais procura e mais gente envolvida. Quanto antes estas respostas estiverem prontas, mais fácil fica garantir a data.")}
{checks(["Datas de chegada e de saída (Natal, Réveillon ou os dois)", "Quantas pessoas vão dormir e quantas vêm só para a festa", "Quem cuida da ceia ou se haverá buffet", "Bebidas, gelo e caixas térmicas para vários dias", "Regras de som e de fogos — combine com os anfitriões", "Divisão das suítes entre as famílias"])}
</div>
<div>{composer("Natal ou Réveillon")}</div>
</div>
</section>

<section class="section section--paper">
<div class="wrap narrow">
{faq_html(FAQ, "Perguntas frequentes sobre Natal e Réveillon")}
</div>
</section>

<section class="section section--tight">
<div class="wrap">{cta_band("Garanta o seu fim de ano na chácara", "Mande as datas e o número de pessoas pelo WhatsApp. Respondemos com disponibilidade e as condições para Natal e Réveillon.", key="fimdeano", wa_label="Consultar Natal ou Réveillon")}</div>
</section>
'''

PAGE = dict(
    path=PATH,
    title="Chácara para Natal e Réveillon em Uberaba",
    description="Natal e Réveillon em chácara em Uberaba (MG): ceia na área gourmet, piscina iluminada e pernoite para até 40 pessoas em 6 suítes. Reserve cedo pelo WhatsApp.",
    h1="Chácara para Natal e Réveillon em Uberaba",
    lead="A ceia com a família, a virada do ano ao ar livre e todo mundo dormindo na chácara — com piscinas iluminadas, área gourmet e 6 suítes.",
    eyebrow="Fim de ano",
    hero="piscinas-noite",
    og="gourmet-noite",
    crumbs=[("Início", "/"), ("Eventos", "/eventos/"), ("Natal e Réveillon", PATH)],
    wa_key="fimdeano",
    wa_label="Consultar Natal ou Réveillon",
    faq=FAQ,
    body=BODY,
    sitemap_images=["gourmet-noite", "pergola-noite", "varanda-noite"],
)
