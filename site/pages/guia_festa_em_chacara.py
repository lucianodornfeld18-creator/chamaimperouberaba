import _data as D
from _components import (answer, article_schema, checks, cta_band, faq_html, figure, related, toc)

PATH = "/guia/festa-em-chacara-como-organizar/"
TITLE = "Festa em Chácara: Como Organizar, o que Servir e Decorar"
DESC = ("Como organizar uma festa em chácara: passo a passo, o que servir, festa infantil e de 15 anos, "
        "decoração simples, música e o que pesa no custo do aluguel.")
H1 = "Festa em chácara: como organizar do começo ao fim"
PHONE = f'<span style="white-space:nowrap">{D.PHONE_DISPLAY}</span>'

FAQ = [
    ("Como organizar uma festa em chácara?",
     "Defina data, convidados e orçamento; visite a chácara e confirme o que está incluído e as regras de som; contrate comida, bolo, música e decoração; monte um roteiro do dia e deixe um plano B coberto para a chuva."),
    ("O que servir em uma festa em chácara?",
     "O churrasco é o clássico, mas buffet, comida de panela e food trucks também funcionam. Como estimativa, calcule de 300 a 500 g de carne por adulto, cerca de 2 litros de bebida e 1 kg de gelo por pessoa."),
    ("Quanto custa alugar uma chácara para festa?",
     f"O preço varia com a data, o número de convidados, a duração, o pernoite e o que está incluído, além de extras como limpeza, gelo, lenha e buffet. Na Chácara Império, os valores saem pelo WhatsApp {PHONE}."),
    ("Dá para fazer festa de 15 anos em chácara com piscina?",
     "Dá. O ideal é separar o baile do momento da piscina e manter adultos vigiando a água. A Chácara Império tem piscina adulto e infantil, salão coberto para festas e 6 suítes para dormir no local."),
    ("A Chácara Império serve para festa infantil?",
     "A Chácara Império tem piscina infantil, parquinho com balanços e escorregador, gramado e salão coberto, estrutura que ajuda numa festa infantil. Mantenha sempre um adulto vigiando a piscina e peça detalhes aos anfitriões pelo WhatsApp."),
]

BODY = f'''
<section class="section">
<div class="wrap">
<div class="prose">
<p class="updated">Atualizado em {D.UPDATED_HUMAN} · leitura de 6 minutos</p>
{answer("Para organizar uma festa em chácara, defina a data, o número de convidados e o orçamento antes de escolher o espaço. Depois visite a chácara, confirme o que está incluído e as regras de som, contrate comida, bebida e música, calcule as quantidades por pessoa e deixe um plano B coberto para a chuva.")}
{toc([("passo-a-passo", "Passo a passo para organizar"), ("servir", "O que servir em festa de chácara"), ("dia-noite", "Festa em chácara de dia ou à noite"), ("infantil", "Festa infantil em chácara"), ("quinze-anos", "Festa de 15 anos em chácara com piscina"), ("decoracao", "Decoração simples e temas"), ("vestir", "O que vestir em festa de chácara"), ("musica", "Música e vizinhança"), ("custo", "Quanto custa alugar uma chácara para festa"), ("chacara-imperio", "Festa na Chácara Império"), ("perguntas", "Perguntas frequentes")])}

<h2 id="passo-a-passo">Passo a passo para organizar</h2>
<ol>
<li><strong>Data e formato.</strong> Escolha o tipo de festa e consulte a disponibilidade cedo: feriados e fim de ano costumam esgotar primeiro.</li>
<li><strong>Convidados.</strong> Faça uma lista realista, contando as crianças. Ela define espaço, comida, bebida e, muitas vezes, o preço.</li>
<li><strong>Orçamento.</strong> Defina o total e separe uma reserva para imprevistos (muita gente separa de 10% a 15%, como estimativa).</li>
<li><strong>Chácara.</strong> Visite ou peça fotos e vídeos. Confira capacidade, área coberta, banheiros, estacionamento, regras de som e o que está incluído.</li>
<li><strong>Fornecedores.</strong> Contrate comida, bolo, música, decoração e recreação. Peça orçamentos com a mesma lista de itens e feche por escrito.</li>
<li><strong>Roteiro do dia.</strong> Monte um cronograma, da montagem ao encerramento, e passe a todos os fornecedores.</li>
</ol>

<h2 id="servir">O que servir em festa de chácara</h2>
<p>O churrasco é a escolha clássica, mas não a única.</p>
{checks(["<strong>Churrasco:</strong> agrada vários perfis. Precisa de churrasqueiro, carvão e muito gelo; inclua opções sem carne.", "<strong>Buffet contratado:</strong> alivia a organização; pergunte à chácara como funciona a entrada de buffet de fora.", "<strong>Food trucks:</strong> ótimos para muitos convidados; combine espaço, energia e acesso dos veículos com os anfitriões.", "<strong>Comida de panela e petiscos:</strong> feijoada, caldos e massas costumam ser opções mais em conta."])}
{figure("gourmet-bar", "Área gourmet da Chácara Império, com churrasqueira e balcão de granito")}
<p>Estimativas gerais por pessoa, para ajustar ao seu grupo:</p>
{checks(["Carne: de 300 a 500 g por adulto (menos com muitos acompanhamentos) e cerca da metade para crianças", "Bebidas: por volta de 2 litros em uma festa de 4 a 5 horas, somando água, refrigerante, suco e cerveja", "Gelo: cerca de 1 kg em dia quente"])}
<p>São referências de uso comum, não regras: se a festa for longa, aumente a margem.</p>

<h2 id="dia-noite">Festa em chácara de dia ou à noite</h2>
{checks(["<strong>De dia:</strong> combina com festa infantil e almoço em família e aproveita a piscina. Peça sombra, água e protetor solar.", "<strong>À noite:</strong> clima mais fresco e luz que valoriza o jardim, ótimo para festas de 15 anos e de adultos. Leve repelente e agasalho; combine a volta com motorista da vez ou aplicativo."])}
<p>Se a festa vai até mais tarde, uma chácara com quartos permite que parte dos convidados durma no local.</p>

<h2 id="infantil">Festa infantil em chácara</h2>
<p>Criança em chácara tem muito espaço para correr, e por isso a segurança precisa estar combinada antes da festa.</p>
{checks(["<strong>Piscina:</strong> um adulto olhando a água o tempo todo, sem celular, com revezamento combinado; defina se ela fica liberada a festa toda ou só em horários marcados", "Colete salva-vidas para quem não nada bem: boia não substitui vigilância", "<strong>Parquinho:</strong> adultos por perto e atenção ao horário de sol forte", "Sombra, água à vontade e lanches no horário certo"])}
{figure("parquinho", "Parquinho com balanços e escorregador, iluminado à noite")}
<p>Em grupos grandes, considere contratar um salva-vidas para o horário da piscina.</p>

<h2 id="quinze-anos">Festa de 15 anos em chácara com piscina</h2>
<p>A chácara permite misturar baile e descontração. Uma boa saída é separar os momentos: valsa, fotos e jantar primeiro; piscina e pista de dança depois.</p>
{checks(["Combine se a piscina fica liberada durante o baile ou só depois, sempre com adultos de olho na água", "Para uma festa de 15 anos simples: almoço ou brunch, poucos elementos de decoração bem escolhidos, uma boa playlist e um cantinho para fotos", "Para adolescentes, bebidas sem álcool e um cardápio que eles gostem"])}

<h2 id="decoracao">Decoração simples e temas</h2>
<p>Numa chácara, a melhor decoração valoriza o cenário: use gramado, árvores e pérgolas como base e acrescente poucos elementos de impacto.</p>
{checks(["Bandeirinhas, balões em arco desfeito e painel de tecido ou de madeira", "Mesas de madeira, toalhas de algodão cru, flores do campo e potes de vidro", "Cordões de luz e lanternas, que transformam o fim da tarde"])}
<p>Temas que combinam com o ambiente: fazendinha (festa infantil), festa junina, country ou sertanejo, boteco, luau, jardim encantado e pool party. Antes de comprar a decoração, combine com os anfitriões o que pode ser fixado.</p>

<h2 id="vestir">O que vestir em festa de chácara</h2>
<p><strong>De dia:</strong> roupa leve, de algodão ou linho; calçado confortável, como rasteira, tênis ou sandália de salto bloco; chapéu, óculos de sol e protetor. Se vai à piscina, leve roupa de banho e uma troca.</p>
<p><strong>À noite:</strong> um degrau mais arrumado, com uma camada extra para a friagem, como jaqueta leve ou xale. Prefira sapato que aguenta o gramado e leve repelente. Em festa de 15 anos ou de adultos, pergunte à família qual é o traje.</p>

<h2 id="musica">Música e vizinhança</h2>
<p>O som merece atenção, porque o barulho chega longe em área aberta. As regras variam de cidade para cidade e de chácara para chácara.</p>
{checks(["Pergunte aos anfitriões as regras de som e de horário antes de contratar DJ ou banda", "Aponte as caixas para longe das casas vizinhas e ajuste o volume", "Use música ambiente na hora da comida e deixe a pista para depois", "Avise os vizinhos mais próximos com antecedência"])}

<h2 id="custo">Quanto custa alugar uma chácara para festa</h2>
<p>Não existe preço único: o valor muda de chácara para chácara e de festa para festa. O que mais pesa:</p>
{checks(["<strong>Data e época:</strong> feriados, fim de ano e fins de semana muito procurados tendem a custar mais", "<strong>Número de convidados:</strong> mais gente pede mais espaço, banheiros e equipe", "<strong>Duração e pernoite:</strong> festa de tarde é diferente de festa até a madrugada ou com hospedagem", "<strong>O que está incluído:</strong> mesas, cadeiras, cozinha, utensílios, limpeza", "<strong>Custos extras:</strong> limpeza final, gelo, carvão e lenha, decoração, buffet, bebidas, som e salva-vidas"])}
<p>Ao pedir orçamento, informe data, tipo de festa, número de convidados e se haverá hospedagem, e peça a lista do que está incluído. Na Chácara Império, o orçamento sai pelo WhatsApp {PHONE}.</p>

<h2 id="chacara-imperio">Festa na Chácara Império</h2>
<p>A Chácara Império, em Uberaba (MG), recebe festas de até 250 convidados. Para a festa há salão coberto com forro de madeira, área gourmet com churrasqueira e fogão a lenha, piscina adulto e infantil (iluminadas à noite), parquinho, campo de futebol gramado e estacionamento para 40 carros.</p>
{figure("salao", "O salão coberto para festas")}
<p>Para esticar a festa, são 6 suítes com ar-condicionado e 40 camas, para até 40 pessoas. A chácara fica dentro do perímetro urbano, com acesso asfaltado, e aceita contrato de locação temporária para empresas.</p>
<p>Buffet, bebidas, som e decoração: confirme com {D.HOSTS_PHRASE} como funciona, pelo <a href="{D.wa_url("aniversario")}" target="_blank" rel="noopener">WhatsApp</a>. Veja as páginas de <a href="/eventos/aniversario/">aniversário e 15 anos</a> e de <a href="/eventos/confraternizacao-de-empresa/">confraternização de empresa</a>, e o <a href="/guia/o-que-levar-para-a-chacara/">checklist do que levar</a>.</p>

{faq_html(FAQ, "Perguntas frequentes")}
</div>
</div>
</section>

<section class="section section--sand">
<div class="wrap">
<h2>Leia também</h2>
{related([
    ("/eventos/aniversario/", "area-coberta-mesas", "Aniversário e 15 anos", "Do aniversário infantil à festa de 15 anos, na Chácara Império."),
    ("/eventos/confraternizacao-de-empresa/", "alameda", "Confraternização de empresa", "Churrasco, piscina e campo de futebol para a equipe."),
    ("/guia/o-que-levar-para-a-chacara/", "piscinas-casa", "O que levar para a chácara", "Checklist de roupas, cozinha, crianças, pet e itens esquecidos."),
])}
</div>
</section>

<section class="section section--tight">
<div class="wrap">{cta_band("Quer organizar a sua festa na Chácara Império?", key="aniversario")}</div>
</section>
'''

PAGE = dict(
    path=PATH,
    title=TITLE,
    description=DESC,
    h1=H1,
    lead="Passo a passo, cardápio, festa infantil e de 15 anos, decoração, música e o que pesa no custo do aluguel.",
    eyebrow="Guia",
    hero="piscinas-noite",
    crumbs=[("Início", "/"), ("Guia", "/guia/"), ("Festa em chácara", PATH)],
    page_type="WebPage",
    wa_key="aniversario",
    faq=FAQ,
    schema=[article_schema(PATH, H1, DESC, "piscinas-noite", "2026-10-16")],
    body=BODY,
    guide=dict(summary="Passo a passo, cardápio, festa infantil e de 15 anos, decoração, música e o que pesa no custo.", minutes=6, pid="piscinas-noite"),
)
