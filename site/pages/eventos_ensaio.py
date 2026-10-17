from _components import (answer, checks, composer, cta_band, faq_html, figure, section_head, tiles)

PATH = "/eventos/ensaio-fotografico/"

FAQ = [
    ("A Chácara Império permite fotografia comercial?",
     "Sim. A fotografia comercial é permitida na Chácara Império — ensaios, books, pré-wedding, fotos de produto e gravações, combinados com os anfitriões."),
    ("Quais cenários a chácara tem para fotos?",
     "Pérgolas de madeira, carro de boi decorativo, coqueiros e ciprestes, gramados, duas piscinas com deque de pedra, varandas com forro de madeira, salão coberto e jardins iluminados à noite."),
    ("Qual o melhor horário para fotografar na chácara?",
     "No fim da tarde a luz fica mais suave e dourada nos gramados e nas pérgolas; à noite, os jardins, a pérgola e as piscinas iluminados rendem fotos com outro clima."),
    ("Dá para fazer ensaio de gestante, 15 anos ou pré-wedding?",
     "Dá. Os jardins e as pérgolas combinam com ensaios de gestante e pré-wedding, e as piscinas e o carro de boi com books de 15 anos."),
    ("Como reservar a chácara para um ensaio?",
     "Pelo telefone ou WhatsApp (34) 99169-0139. Informe a data, o horário, o tipo de ensaio e quantas pessoas estarão na equipe."),
]

BODY = f'''
<section class="section section--tight">
<div class="wrap">
{answer("Procurando cenário para fotos em Uberaba? A <strong>Chácara Império</strong> permite <strong>fotografia comercial</strong> e tem pérgolas de madeira, carro de boi decorativo, coqueiros, gramados, duas piscinas com deque de pedra, varandas com forro de madeira e jardins iluminados à noite. Serve para ensaios de gestante, pré-wedding, 15 anos, books, fotos de produto e gravações.")}
</div>
</section>

<section class="section section--paper">
<div class="wrap">
{section_head("Cenários", "Um lugar, muitos fundos diferentes", "Em poucos passos você troca o rústico pelo azul da piscina, o dia pela noite iluminada.")}
<div class="grid grid-3">
{figure("carro-de-boi", "Carro de boi e pérgola no jardim", "(min-width: 960px) 33vw, (min-width: 640px) 50vw, 100vw")}
{figure("pergola-jardim", "Pérgola de madeira e gramado", "(min-width: 960px) 33vw, (min-width: 640px) 50vw, 100vw")}
{figure("jardim-banco", "Cantinho do jardim com banco vermelho", "(min-width: 960px) 33vw, (min-width: 640px) 50vw, 100vw")}
{figure("piscina-deque", "Deque de pedra e piscinas", "(min-width: 960px) 33vw, (min-width: 640px) 50vw, 100vw")}
{figure("varanda-piscina", "Varanda com forro de madeira", "(min-width: 960px) 33vw, (min-width: 640px) 50vw, 100vw")}
{figure("coqueiro-noite", "Coqueiro iluminado à noite", "(min-width: 960px) 33vw, (min-width: 640px) 50vw, 100vw")}
</div>
</div>
</section>

<section class="section">
<div class="wrap">
{section_head("Para que tipo de ensaio", "Ideias que combinam com o espaço", None)}
{tiles([
    ("heart", "Pré-wedding", "Pérgolas, alameda de palmeiras e o pôr do sol no gramado."),
    ("smile", "Gestante e família", "Jardins tranquilos, sombra dos coqueiros e o clima de casa de campo."),
    ("sparkle", "Book de 15 anos", "Vestido no carro de boi, piscina azul e luzes da noite."),
    ("camera", "Moda e produto", "Texturas de madeira, tijolinho, pedra e verde para catálogos e redes sociais."),
    ("play", "Vídeos e clipes", "Cenários diurnos e noturnos sem sair do lugar."),
    ("users", "Equipes e empresas", "Fotos institucionais em um ambiente acolhedor."),
])}
</div>
</section>

<section class="section section--sand">
<div class="wrap split">
<div>
{section_head("Antes da sessão", "Combine estes pontos", None)}
{checks(["Data e janela de horário (fim de tarde e noite pedem mais tempo)", "Tamanho da equipe e equipamentos", "Quais áreas serão usadas — e se haverá troca de roupa nas suítes", "Uso de objetos de cena e o que pode ser movido", "Se o ensaio for de um evento futuro, aproveite para conhecer o espaço"])}
</div>
<div>{composer("Ensaio fotográfico")}</div>
</div>
</section>

<section class="section section--paper">
<div class="wrap narrow">
{faq_html(FAQ, "Perguntas frequentes sobre ensaios")}
</div>
</section>

<section class="section section--tight">
<div class="wrap">{cta_band("Vamos agendar o seu ensaio?", key="ensaio", wa_label="Consultar data do ensaio")}</div>
</section>
'''

PAGE = dict(
    path=PATH,
    title="Cenário para Ensaio Fotográfico em Uberaba – Chácara",
    description="Chácara em Uberaba (MG) como cenário para fotos: pérgolas, carro de boi, coqueiros e piscinas. Fotografia comercial permitida para ensaios, books e gravações.",
    h1="Cenário para ensaio fotográfico em Uberaba",
    lead="Pérgolas de madeira, carro de boi, coqueiros, piscinas e jardins iluminados à noite — com fotografia comercial permitida.",
    eyebrow="Ensaios e gravações",
    hero="carro-de-boi",
    crumbs=[("Início", "/"), ("Eventos", "/eventos/"), ("Ensaio fotográfico", PATH)],
    wa_key="ensaio",
    wa_label="Consultar data do ensaio",
    faq=FAQ,
    body=BODY,
    sitemap_images=["pergola-jardim", "jardim-banco", "coqueiro-noite"],
)
