from _components import (answer, checks, composer, cta_band, faq_html, figure, img, section_head, tiles)

PATH = "/eventos/reuniao-de-familia/"

FAQ = [
    ("A Chácara Império é boa para reunir a família toda?",
     "É feita para isso: recebe eventos de até 250 pessoas e hospeda até 40 em 6 suítes, com piscinas, parquinho, campo de futebol e área gourmet para o almoço de domingo."),
    ("Dá para fazer bodas, batizado ou chá revelação na chácara?",
     "Sim. A Chácara Império recebe bodas, almoços de batizado, chá revelação, chá de bebê e aniversários de avós, com salão coberto, varandas e jardins."),
    ("A família pode passar o fim de semana inteiro na chácara?",
     "Pode. A hospedagem é da chácara inteira, para até 40 pessoas, com check-in a partir das 15h e check-out até as 11h."),
    ("Posso levar o cachorro para a reunião de família?",
     "Pode. A Chácara Império aceita animais de estimação."),
    ("Tem lugar para os avós descansarem durante a festa?",
     "Tem. Além das varandas cobertas com mesas, a casa tem sala de estar com sofás e suítes com ar-condicionado para um descanso no meio do dia."),
]

BODY = f'''
<section class="section section--tight">
<div class="wrap">
{answer("Para uma reunião de família em Uberaba, a <strong>Chácara Império</strong> junta festa e hospedagem num lugar só: até 250 convidados no dia do encontro e <strong>até 40 pessoas dormindo em 6 suítes</strong>. Há piscina adulto e infantil, parquinho, campo de futebol, área gourmet com churrasqueira e fogão a lenha — e o pet da família também pode ir.")}
</div>
</section>

<section class="section section--paper">
<div class="wrap">
{section_head("Ocasiões em família", "Quando todo mundo merece estar junto", None)}
{tiles([
    ("heart", "Bodas", "Bodas de prata, de ouro ou só porque sim: almoço no salão coberto e fotos no jardim."),
    ("sparkle", "Chá revelação e chá de bebê", "Jardins e pérgolas para o grande momento — e espaço para toda a família."),
    ("home", "Batizado e primeira comunhão", "O almoço depois da cerimônia, com as crianças no parquinho e na piscina infantil."),
    ("cake", "Aniversário dos avós", "Uma festa que reúne netos, filhos e bisnetos sem ninguém ter que ir embora cedo."),
    ("users", "Encontro de primos", "Fim de semana inteiro para colocar a conversa em dia, com futebol e piscina."),
    ("calendar", "Feriados prolongados", "Três dias com a família reunida, cada núcleo na sua suíte."),
])}
</div>
</section>

<section class="section">
<div class="wrap split">
<div>
{section_head("Como fica o fim de semana", "Espaço para cada geração", "Uma reunião de família funciona quando cada idade tem o seu canto — e todos se encontram na hora do almoço.")}
{checks(["As crianças no parquinho, na piscina infantil e no gramado", "Os jovens no campo de futebol e na piscina", "Os adultos na área gourmet, entre a churrasqueira e o fogão a lenha", "Os avós nas varandas cobertas, de olho em tudo", "À noite, todos à mesa — e depois cada família na sua suíte"])}
</div>
<div class="split-media">{img("area-coberta-mesas", "(min-width: 900px) 560px, 100vw")}{img("parquinho", "220px", cls="stack")}</div>
</div>
</section>

<section class="section section--sand">
<div class="wrap">
<div class="grid grid-3">
{figure("varanda-mesa", "Varanda com mesa de madeira e vista para o jardim", "(min-width: 960px) 33vw, (min-width: 640px) 50vw, 100vw")}
{figure("sala", "Sala de estar e jantar da casa", "(min-width: 960px) 33vw, (min-width: 640px) 50vw, 100vw")}
{figure("suite-2", "Suíte com cama de casal e beliches", "(min-width: 960px) 33vw, (min-width: 640px) 50vw, 100vw")}
</div>
</div>
</section>

<section class="section">
<div class="wrap split">
<div>
{section_head("Para organizar", "Dicas para a reunião dar certo", None)}
{checks(["Faça uma lista de quem dorme e divida as suítes por núcleo familiar", "Monte um cardápio por refeição e divida as compras entre as famílias", "Combine um rodízio de adultos olhando as crianças na piscina", "Leve jogos, baralho e o álbum de fotos antigas — a noite rende", "Confirme pelo WhatsApp o que a casa oferece (roupa de cama, utensílios)"])}
<p>Veja a lista completa do <a href="/guia/o-que-levar-para-a-chacara/">que levar para a chácara</a>.</p>
</div>
<div>{composer("Reunião de família")}</div>
</div>
</section>

<section class="section section--paper">
<div class="wrap narrow">
{faq_html(FAQ, "Perguntas frequentes sobre reuniões de família")}
</div>
</section>

<section class="section section--tight">
<div class="wrap">{cta_band("Vamos reunir a família?", key="familia", wa_label="Consultar data para a família")}</div>
</section>
'''

PAGE = dict(
    path=PATH,
    title="Chácara para Reunião de Família em Uberaba",
    description="Reunião de família em chácara em Uberaba (MG): bodas, batizados, chá revelação e feriados com até 250 convidados e pernoite para 40 pessoas em 6 suítes.",
    h1="Chácara para reunião de família em Uberaba",
    lead="Bodas, batizados, chá revelação, aniversário dos avós ou um feriado inteiro juntos — com piscinas, parquinho, churrasco e suítes para todo mundo.",
    eyebrow="Família",
    hero="piscinas-vista",
    crumbs=[("Início", "/"), ("Eventos", "/eventos/"), ("Reunião de família", PATH)],
    wa_key="familia",
    wa_label="Consultar data para a família",
    faq=FAQ,
    body=BODY,
    sitemap_images=["area-coberta-mesas", "varanda-mesa", "sala"],
)
