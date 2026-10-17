import _data as D
from _components import (answer, article_schema, checks, cta_band, faq_html, figure, related, toc)

PATH = "/guia/como-escolher-chacara-para-festa/"
TITLE = "Como Escolher Chácara para Festa: 12 Pontos e Golpes"
DESC = ("Como escolher uma chácara para festa ou fim de semana: 12 pontos para comparar, perguntas "
        "para fazer ao dono e como evitar golpes no aluguel de chácara.")
H1 = "Como escolher uma chácara para festa (e não cair em golpe)"

FAQ = [
    ("O que perguntar antes de alugar uma chácara para festa?",
     "Pergunte a capacidade de convidados e de pernoite, o horário de entrada e saída, o que está incluído (mesas, cadeiras, utensílios, roupa de cama), as regras de som, se o buffet é livre, se há espaço coberto para chuva, o estacionamento, a forma de pagamento e a política de cancelamento."),
    ("Como saber se o anúncio de chácara é golpe?",
     "Desconfie de preço muito abaixo do mercado, pressa para pagar, pedido de PIX para conta de terceiros e recusa em mostrar o espaço ou fazer contrato. Confira o histórico no Instagram e no Google, fale com o dono por telefone e pague só com contrato e recibo."),
    ("Com quanto tempo de antecedência devo alugar uma chácara?",
     "Para sábados, feriados e fim de ano, quanto antes melhor — essas datas fecham primeiro. Para datas de semana, a disponibilidade costuma ser maior."),
    ("Chácara com hospedagem vale a pena para festa?",
     "Para festas que vão até tarde ou com convidados de fora, sim: anfitriões e família dormem no local e ninguém precisa dirigir depois. A Chácara Império, por exemplo, hospeda até 40 pessoas em 6 suítes."),
    ("Como reservar a Chácara Império?",
     "Somente por telefone ou WhatsApp (34) 99169-0139, direto com os anfitriões Maria Inês e Luciano."),
]

BODY = f'''
<section class="section">
<div class="wrap">
<div class="prose">
<p class="updated">Atualizado em {D.UPDATED_HUMAN} · leitura de 7 minutos</p>
{answer("Para escolher uma chácara para festa, compare capacidade de convidados e de pernoite, espaço coberto para chuva, estacionamento, acesso (asfalto ou terra), banheiros, área gourmet, lazer para crianças, regras de som e de fornecedores, o que está incluído no preço e a segurança do local. Antes de pagar, confirme que está falando com o dono, peça contrato e recibo e desconfie de preços muito baixos.")}
{toc([("pontos", "12 pontos para comparar chácaras"), ("perguntas", "Perguntas para fazer ao dono"), ("golpes", "Como evitar golpes"), ("visita", "Na visita ou na chamada de vídeo"), ("imperio", "Como a Chácara Império se encaixa"), ("perguntas-frequentes", "Perguntas frequentes")])}

<h2 id="pontos">12 pontos para comparar chácaras</h2>
<ol>
<li><strong>Capacidade real de convidados.</strong> Pergunte quantas pessoas cabem sentadas e não só "em pé". Some crianças, fornecedores e equipe.</li>
<li><strong>Pernoite.</strong> Quantas pessoas podem dormir e em quantos quartos. Festa que vai até tarde fica muito mais tranquila quando a família dorme no local.</li>
<li><strong>Espaço coberto.</strong> Chuva acontece. Verifique se há salão ou área coberta para todos os convidados — não só para a mesa do bolo.</li>
<li><strong>Acesso.</strong> Estrada de terra vira lama na chuva e afasta convidados de carro baixo. Acesso asfaltado e localização dentro da cidade facilitam a vida de todo mundo.</li>
<li><strong>Estacionamento.</strong> Conte um carro para cada 3 ou 4 convidados, em média, e confira quantas vagas há dentro do terreno.</li>
<li><strong>Banheiros.</strong> Poucos banheiros viram fila. Pergunte quantos há e quais ficam liberados para os convidados.</li>
<li><strong>Área gourmet e cozinha.</strong> Churrasqueira, fogão, pia, bancada e geladeira mudam o tipo de cardápio possível — e o custo do buffet.</li>
<li><strong>Lazer.</strong> Piscina, campo, parquinho e gramado seguram as crianças e animam os adultos. Veja se a piscina infantil é separada da adulta.</li>
<li><strong>Regras.</strong> Horário de som, buffet livre ou indicado, decoração (o que pode ser fixado), fogos, uso da piscina durante a festa e animais de estimação.</li>
<li><strong>O que está incluído.</strong> Mesas, cadeiras, utensílios, roupa de cama, limpeza, gás, lenha e gelo podem ou não entrar no preço.</li>
<li><strong>Segurança.</strong> Portão, iluminação noturna, muros, câmeras e alguém responsável pelo local durante o evento.</li>
<li><strong>Quem atende.</strong> Falar direto com o dono costuma deixar os combinados mais claros do que passar por vários intermediários.</li>
</ol>
{figure("salao", "Espaço coberto para todos os convidados é o plano B que salva a festa em dia de chuva")}

<h2 id="perguntas">Perguntas para fazer ao dono antes de fechar</h2>
{checks(["Minha data está livre? Até quando vocês seguram a data?", "Quantas pessoas cabem na festa e quantas podem dormir?", "Que horas posso entrar para montar e até que horas a festa pode ir?", "Posso escolher o buffet, o DJ e a decoração?", "O que está incluído no valor: mesas, cadeiras, utensílios, roupa de cama, limpeza?", "Qual o valor do sinal, como é o pagamento e qual a política de cancelamento?", "Tem contrato? Em nome de quem?", "Há alguém responsável no local durante o evento?"])}

<h2 id="golpes">Como evitar golpes no aluguel de chácara</h2>
<p>Golpes com anúncios falsos de imóveis para temporada são um problema conhecido em todo o país: fotos copiadas de outros lugares, preço tentador e pressa para receber um sinal. Alguns cuidados resolvem a maior parte do risco:</p>
{checks(["Desconfie de preço muito abaixo dos outros da região e de “promoção que acaba hoje”", "Confira o histórico: perfil no Instagram com posts antigos, avaliações no Google e anúncios em plataformas conhecidas", "Ligue para o número do anúncio e converse — golpistas evitam ligação", "Peça para conhecer o espaço ou faça uma chamada de vídeo andando pela chácara", "Nunca pague para conta em nome de terceiros sem explicação; prefira contrato e recibo", "Guarde todas as conversas, comprovantes e o contrato assinado"])}

<h2 id="visita">Na visita ou na chamada de vídeo</h2>
<p>Vá no horário parecido com o da sua festa. Se o evento for à noite, veja a iluminação; se for de dia, a sombra. Ande pelo caminho que os convidados vão fazer: do estacionamento até o salão, do salão até os banheiros. Abra torneiras, olhe a piscina, pergunte onde fica o quadro de energia e onde os fornecedores descarregam.</p>

<h2 id="imperio">Como a Chácara Império se encaixa</h2>
<p>Se você está procurando em Uberaba, compare com o que a <a href="/estrutura/">Chácara Império</a> oferece:</p>
{checks(["Eventos de até 250 convidados e pernoite para até 40 pessoas em 6 suítes, com 8 banheiros", "Salão coberto, área gourmet e varandas cobertas para dias de chuva", "Dentro do perímetro urbano de Uberaba, com acesso asfaltado", "Estacionamento para 40 carros dentro da chácara", "Piscina adulto e infantil, campo de futebol, parquinho e jardins", "Portão eletrônico e câmeras externas", "Atendimento direto com os anfitriões, por telefone ou WhatsApp"])}
<p>Regras de som, fornecedores e o que está incluído são combinados direto com os anfitriões — pergunte tudo antes de fechar, como você faria em qualquer lugar.</p>

{faq_html(FAQ, "Perguntas frequentes", "perguntas-frequentes")}
</div>
</div>
</section>

<section class="section section--sand">
<div class="wrap">
<h2>Leia também</h2>
{related([
    ("/eventos/", "jardim-noite", "Eventos na Chácara Império", "Casamentos, aniversários, empresas e reuniões de família."),
    ("/guia/o-que-levar-para-a-chacara/", "piscinas-casa", "O que levar para a chácara", "Checklist completo para o fim de semana."),
    ("/perguntas-frequentes/", "varanda-piscina", "Perguntas frequentes", "Capacidade, reservas, hospedagem e estrutura."),
])}
</div>
</section>

<section class="section section--tight">
<div class="wrap">{cta_band("Quer comparar? Consulte a Chácara Império.", key="evento")}</div>
</section>
'''

PAGE = dict(
    path=PATH,
    title=TITLE,
    description=DESC,
    h1=H1,
    lead="Os pontos que fazem diferença no dia da festa, as perguntas certas para o dono e os cuidados para não cair em golpe.",
    eyebrow="Guia",
    hero="salao",
    crumbs=[("Início", "/"), ("Guia", "/guia/"), ("Como escolher uma chácara", PATH)],
    wa_key="evento",
    faq=FAQ,
    schema=[article_schema(PATH, H1, DESC, "salao", "2026-10-16")],
    body=BODY,
    guide=dict(summary="12 pontos para comparar, perguntas ao dono e como evitar golpes.", minutes=7, pid="salao"),
)
