import _data as D
from _components import (btn_wa, checks, cta_band, faq_html, facts_grid, figure, img, section_head, tiles)
from _icons import icon

PATH = "/sobre/"

FAQ = [
    ("Quem são os donos da Chácara Império?",
     "A Chácara Império é cuidada pelos anfitriões Maria Inês e Luciano, que atendem pessoalmente as reservas por telefone e WhatsApp."),
    ("Com quem eu falo para reservar?",
     "Direto com os anfitriões, pelo telefone ou WhatsApp (34) 99169-0139. Não há intermediários."),
    ("A Chácara Império tem Instagram?",
     "Tem: @chacaraimperiouberaba, com fotos e vídeos dos eventos e da chácara."),
]

BODY = f'''
<section class="section section--paper">
<div class="wrap hosts">
<figure class="hosts-photo">{img("anfitrioes", "(min-width: 880px) 420px, 90vw", eager=True)}<figcaption>Maria Inês e Luciano</figcaption></figure>
<div class="letter">
<p class="hello">Olá! Que alegria ter você por aqui!</p>
<p>Nós somos a <strong>Maria Inês</strong> e o <strong>Luciano</strong>, anfitriões da Chácara Império, em Uberaba. Cuidamos de cada cantinho deste lugar com muito carinho para receber pessoas especiais.</p>
<p>O que mais nos deixa felizes é ver a chácara cheia de vida: crianças brincando no gramado e na piscina, amigos celebrando em volta da churrasqueira, famílias criando memórias que vão durar para sempre. É para isso que ela existe.</p>
<p>Aqui você conversa direto com a gente — sem intermediários —, do primeiro contato até o dia do seu evento ou da sua estadia. Fique à vontade para conhecer o espaço e tirar suas dúvidas. E se você já esteve aqui com a gente, conte para outras pessoas como foi!</p>
<p class="signature">— Maria Inês e Luciano</p>
<div class="btn-row mt-2">{btn_wa("Falar com a gente no WhatsApp", "geral")}<a class="btn btn-ghost" href="{D.INSTAGRAM}" target="_blank" rel="noopener">{icon("instagram")}<span>{D.INSTAGRAM_HANDLE}</span></a></div>
</div>
</div>
</section>

<section class="section">
<div class="wrap">
{section_head("Nosso jeito de receber", "O que você pode esperar da gente", None)}
{tiles([
    ("heart", "Atendimento dos donos", "Quem responde o WhatsApp e atende o telefone somos nós."),
    ("sparkle", "Espaço bem cuidado", "Jardins, piscinas, área gourmet e suítes preparados para cada reserva."),
    ("shield", "Tranquilidade", "Portão eletrônico e câmeras externas nas varandas, no estacionamento e na entrada."),
    ("users", "Lugar para todos", "Crianças, avós e até o pet: a chácara foi pensada para famílias inteiras."),
    ("calendar", "Combinados claros", "Horários, regras e o que está incluído conversados antes da reserva."),
    ("home", "Do jeito mineiro", "Receber bem é tradição em Minas — e a gente leva isso a sério."),
])}
</div>
</section>

<section class="section section--sand">
<div class="wrap">
{section_head("A chácara", "A Chácara Império em números", "2.500 m² dentro do perímetro urbano de Uberaba, com acesso asfaltado.")}
{facts_grid()}
<div class="grid grid-3 mt-3">
{figure("piscinas-vista", None, "(min-width: 960px) 33vw, (min-width: 640px) 50vw, 100vw")}
{figure("gourmet-noite", None, "(min-width: 960px) 33vw, (min-width: 640px) 50vw, 100vw")}
{figure("pergola-jardim", None, "(min-width: 960px) 33vw, (min-width: 640px) 50vw, 100vw")}
</div>
</div>
</section>

<section class="section">
<div class="wrap narrow">
{faq_html(FAQ, "Perguntas sobre a Chácara Império")}
</div>
</section>

<section class="section section--tight">
<div class="wrap">{cta_band("Vai ser um prazer receber você")}</div>
</section>
'''

PERSONS = [
    {"@type": "Person", "@id": D.SITE_URL + "/sobre/#maria-ines", "name": "Maria Inês", "jobTitle": "Anfitriã",
     "worksFor": {"@id": D.SITE_URL + "/#negocio"}, "homeLocation": {"@type": "City", "name": "Uberaba"}},
    {"@type": "Person", "@id": D.SITE_URL + "/sobre/#luciano", "name": "Luciano", "jobTitle": "Anfitrião",
     "worksFor": {"@id": D.SITE_URL + "/#negocio"}, "homeLocation": {"@type": "City", "name": "Uberaba"}},
]

PAGE = dict(
    path=PATH,
    title="Quem Somos: Maria Inês e Luciano, da Chácara Império",
    description="Conheça Maria Inês e Luciano, anfitriões da Chácara Império em Uberaba (MG): atendimento direto dos donos, espaço bem cuidado e lugar para a família inteira.",
    h1="Quem somos",
    lead="A Chácara Império é cuidada pelos anfitriões Maria Inês e Luciano, em Uberaba.",
    eyebrow="Quem recebe você",
    hero="pergola-varanda",
    og="piscina-banco",
    crumbs=[("Início", "/"), ("Quem somos", PATH)],
    page_type="AboutPage",
    hero_ctas="",
    wa_key="geral",
    faq=FAQ,
    schema=PERSONS,
    body=BODY,
    sitemap_images=["anfitrioes"],
)
