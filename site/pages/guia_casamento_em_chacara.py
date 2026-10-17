import _data as D
from _components import (answer, article_schema, checks, cta_band, faq_html, figure, related, toc)

PATH = "/guia/casamento-em-chacara/"
TITLE = "Casamento em Chácara: Guia para Planejar e o que Vestir"
DESC = ("Guia para planejar casamento em chácara: horário (dia ou noite), plano B para a chuva, "
        "decoração simples e rústica, o que vestir, hospedagem e cronograma.")
H1 = "Casamento em chácara: como planejar, decorar e o que vestir"
PHONE = f'<span style="white-space:nowrap">{D.PHONE_DISPLAY}</span>'

FAQ = [
    ("Qual o melhor horário para casamento em chácara?",
     "Depende do estilo. De dia há luz natural e menos gasto com iluminação; o fim de tarde une luz bonita e calor ameno; à noite o clima é mais intimista. Em qualquer horário, tenha um plano B coberto para a chuva."),
    ("O que vestir num casamento em chácara?",
     "Roupa elegante, leve e confortável: vestido midi ou longo com salto bloco ou rasteira, para elas; terno leve ou alfaiataria, para eles. Evite branco e off-white e leve casaco ou xale se a festa for à noite."),
    ("Dá para fazer casamento simples e barato em chácara?",
     "Dá, com poucas prioridades: menos convidados, cerimônia de dia, cardápio enxuto, decoração que aproveita o jardim e uma data fora do sábado à noite. Peça orçamentos com a mesma lista de itens para comparar."),
    ("Quantos convidados cabem na Chácara Império para um casamento?",
     f"A Chácara Império, em Uberaba (MG), recebe eventos de até 250 convidados e hospeda até 40 pessoas em 6 suítes. Para consultar datas e valores, chame no WhatsApp {PHONE}."),
    ("Casamento em chácara precisa de plano B para chuva?",
     "Precisa: mesmo fora da época das chuvas, um temporal pode aparecer. Escolha uma chácara com salão ou varanda coberta. A Chácara Império tem salão coberto com forro de madeira; pergunte aos anfitriões a capacidade."),
]

BODY = f'''
<section class="section">
<div class="wrap">
<div class="prose">
<p class="updated">Atualizado em {D.UPDATED_HUMAN} · leitura de 6 minutos</p>
{answer("Para casar em chácara, defina cedo três coisas: o horário (o fim de tarde costuma dar a luz mais bonita), o plano B coberto para a chuva e se cerimônia e festa serão no mesmo lugar. Depois, aposte em decoração simples e rústica e peça aos convidados traje leve e sapato confortável para o gramado.")}
{toc([("vantagens", "Vantagens de casar em chácara"), ("horario", "De dia, à tarde ou à noite"), ("ar-livre", "Cerimônia ao ar livre e entrada dos noivos"), ("chuva", "Plano B para a chuva"), ("mesmo-lugar", "Cerimônia e recepção no mesmo lugar"), ("decoracao", "Decoração simples e rústica"), ("economia", "Casamento simples, barato ou intimista"), ("vestir", "O que vestir num casamento em chácara"), ("hospedagem", "Hospedagem dos noivos e da família"), ("cronograma", "Cronograma de 12 meses até o casamento"), ("chacara-imperio", "Casamento na Chácara Império"), ("perguntas", "Perguntas frequentes")])}

<h2 id="vantagens">Vantagens de casar em chácara</h2>
<p>Quem escolhe uma chácara busca espaço, natureza e clima de festa em família: o cenário já faz boa parte da decoração, e o formato é mais livre que o de um salão.</p>
{checks(["Gramado, árvores e jardim como cenário para a cerimônia e as fotos", "Espaço para cerimônia, jantar e pista de dança sem aperto", "Área verde para as crianças brincarem", "Possibilidade de hospedar noivos e família no mesmo lugar, quando há quartos"])}
<p>Em troca, exige mais planejamento: clima, luz, som e logística dependem de você e dos fornecedores.</p>

<h2 id="horario">De dia, à tarde ou à noite</h2>
<p>O horário muda a luz das fotos, o calor, a iluminação necessária e até o cardápio.</p>
{checks(["<strong>De dia:</strong> luz natural e pouca despesa com iluminação. O cuidado é o sol forte do meio-dia: ofereça sombra, água e leques.", "<strong>À tarde, com cerimônia no fim do dia:</strong> luz dourada, calor mais ameno e festa que segue noite adentro. Veja com o fotógrafo o horário do pôr do sol.", "<strong>À noite:</strong> clima intimista, com o jardim iluminado. Planeje a luz, leve repelente e, no inverno, agasalho."])}
{figure("jardim-noite", "O jardim da Chácara Império iluminado à noite")}

<h2 id="ar-livre">Cerimônia ao ar livre e entrada dos noivos</h2>
<p>Posicione as cadeiras para ninguém ficar de frente para o sol e prefira um ponto com sombra. Vale ainda:</p>
{checks(["Marcar o corredor com tapete ou passarela, para o salto não afundar no gramado", "Usar microfone: o vento e o espaço aberto engolem a voz do celebrante", "Manter a cerimônia curta, em torno de 20 a 30 minutos, e oferecer água"])}
<p>Na hora da entrada, aproveite o cenário (um caminho no jardim, uma pérgola como “portal” do altar, um arco simples de folhagens) e combine a música com quem vai tocar. Ensaie o trajeto, porque o gramado pode ter desníveis.</p>

<h2 id="chuva">Plano B para a chuva</h2>
<p>Mesmo fora da época das chuvas, um temporal de fim de tarde pode aparecer. O plano B é o que garante a festa.</p>
{checks(["Escolha uma chácara com salão ou varanda coberta onde caibam os convidados sentados", "Defina até que horas você decide mover a cerimônia para o espaço coberto", "Combine com decoração, som e fotógrafo a montagem das duas versões", "Deixe guarda-chuvas à mão e um trajeto coberto até a recepção"])}

<h2 id="mesmo-lugar">Cerimônia e recepção no mesmo lugar</h2>
<p>Fazer tudo na chácara poupa deslocamento, um segundo aluguel e atrasos. Os convidados ficam, as fotos ganham continuidade e a decoração se reaproveita: as flores do altar, por exemplo, vão para as mesas.</p>
<p>Atenção à “virada”: entre a cerimônia e a festa, a equipe precisa de algo como 30 a 60 minutos para ajustar o espaço. Preencha o intervalo com coquetel e fotos em família.</p>

<h2 id="decoracao">Decoração simples e rústica</h2>
<p>Num casamento rústico, o lugar faz o trabalho pesado. Observe o que a chácara já tem (pérgolas, árvores, madeira, gramado) e decore para destacar, não para cobrir.</p>
{checks(["Madeira, linho e algodão cru em mesas e cadeiras", "Flores do campo e folhagens em vasos, garrafas e potes de vidro", "Cordões de luz e lanternas de LED, mais seguras que velas ao ar livre", "Placas de madeira ou papel kraft para boas-vindas e mapa de mesas"])}
{figure("carro-de-boi", "Carro de boi decorativo e pérgola no jardim")}
<p>Pergunte aos anfitriões o que pode ser fixado ou aceso no espaço antes de encomendar qualquer peça.</p>

<h2 id="economia">Casamento simples, barato ou intimista</h2>
<p>Simples não precisa ser sem graça. Escolha poucas prioridades, em geral comida, fotos e música, e economize no resto.</p>
{checks(["Reduza a lista: cada convidado a menos economiza comida, bebida e cadeira", "Pergunte por datas fora do sábado à noite, que em muitos espaços ficam mais em conta", "Prefira o horário de dia, com menos iluminação, e um cardápio enxuto: churrasco, comida de panela ou brunch", "Peça orçamentos com a mesma lista de itens, para comparar de verdade"])}
<p>No casamento intimista, com poucos convidados, sobra orçamento por pessoa para comida, bebida e fotos melhores.</p>

<h2 id="vestir">O que vestir num casamento em chácara</h2>
<p>Para os convidados, a regra é elegância com conforto: pense em gramado, calor e vento. Siga o traje do convite e, na dúvida, pergunte aos noivos; o “esporte fino” costuma funcionar.</p>
<h3>Roupa feminina</h3>
{checks(["Vestido midi ou longo em tecido leve e fluido, ou conjunto de alfaiataria", "Evite branco, off-white e tons próximos, e confirme se as madrinhas têm cor definida", "Salto fino afunda no gramado: prefira salto bloco, plataforma ou rasteira elegante"])}
<h3>Roupa masculina</h3>
{checks(["Terno leve de linho ou algodão, ou calça de alfaiataria com camisa social e blazer", "De dia, azul, bege, verde-oliva e cinza-claro; à noite, tons mais escuros", "Gravata é opcional de dia; use sapato social ou mocassim, não tênis esportivo"])}
<h3>De dia ou à noite</h3>
<p>De dia, óculos de sol e protetor solar. À noite, leve xale ou casaco, porque o campo esfria, principalmente no inverno. Repelente serve nos dois horários.</p>

<h2 id="hospedagem">Hospedagem dos noivos e da família</h2>
<p>Quando a chácara tem quartos, os noivos podem se arrumar no local, a família de fora fica por perto e ninguém dirige de madrugada. Sem hospedagem, combine a volta com antecedência: motorista da rodada, vans ou aplicativos.</p>

<h2 id="cronograma">Cronograma de 12 meses até o casamento</h2>
{checks(["<strong>12 meses antes:</strong> definir orçamento e número de convidados, visitar chácaras e reservar a data", "<strong>6 meses antes:</strong> contratar fotógrafo, buffet, música e cerimonial", "<strong>3 meses antes:</strong> fechar decoração e plano B, enviar convites com horário e traje, fazer degustação e prova de roupas", "<strong>1 mês antes:</strong> confirmar presenças, montar o mapa de mesas e fazer visita técnica com os fornecedores (luz, som, energia)", "<strong>Na semana:</strong> ver a previsão do tempo, decidir pelo plano B, definir quem recebe cada fornecedor e montar o kit de emergência (costura, repelente, curativos, sapatilha)"])}

<h2 id="chacara-imperio">Casamento na Chácara Império</h2>
<p>Quem busca chácara para casamento em Uberaba encontra na Chácara Império espaço para até 250 convidados. Os jardins com pérgolas e o carro de boi decorativo servem de cenário, o salão coberto tem forro de madeira e as piscinas ficam iluminadas à noite. A fotografia comercial é permitida.</p>
<p>Para dormir, são 6 suítes e 40 camas, para até 40 pessoas. Há estacionamento para 40 carros e acesso asfaltado, dentro do perímetro urbano.</p>
<p>Montagem, fornecedores, som e o que está incluído: pergunte a {D.HOSTS_PHRASE} pelo <a href="{D.wa_url("casamento")}" target="_blank" rel="noopener">WhatsApp</a>. Veja também a <a href="/galeria/">galeria</a>, a página de <a href="/eventos/casamento/">casamento</a> e a <a href="/hospedagem/">hospedagem</a>.</p>

{faq_html(FAQ, "Perguntas frequentes")}
</div>
</div>
</section>

<section class="section section--sand">
<div class="wrap">
<h2>Leia também</h2>
{related([
    ("/eventos/casamento/", "pergola-noite", "Casamento na Chácara Império", "Espaços, capacidade e como consultar a sua data."),
    ("/hospedagem/", "suite-1", "Hospedagem para a família", "6 suítes e 40 camas para até 40 pessoas."),
    ("/galeria/", "piscinas-vista", "Galeria de fotos", "Jardins, salão, piscinas e suítes, de dia e de noite."),
])}
</div>
</section>

<section class="section section--tight">
<div class="wrap">{cta_band("Quer conversar sobre o seu casamento na Chácara Império?", key="casamento")}</div>
</section>
'''

PAGE = dict(
    path=PATH,
    title=TITLE,
    description=DESC,
    h1=H1,
    lead="Dia ou noite, plano B para a chuva, decoração simples, roupa dos convidados e um cronograma para não esquecer nada.",
    eyebrow="Guia",
    hero="pergola-varanda",
    crumbs=[("Início", "/"), ("Guia", "/guia/"), ("Casamento em chácara", PATH)],
    page_type="WebPage",
    wa_key="casamento",
    faq=FAQ,
    schema=[article_schema(PATH, H1, DESC, "pergola-varanda", "2026-10-16")],
    body=BODY,
    guide=dict(summary="Horário, plano B para a chuva, decoração simples, o que vestir e cronograma de 12 meses.", minutes=6, pid="pergola-varanda"),
)
