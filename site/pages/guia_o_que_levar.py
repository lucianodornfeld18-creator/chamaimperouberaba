import _data as D
from _components import (answer, article_schema, checks, cta_band, faq_html, figure, related, toc)

PATH = "/guia/o-que-levar-para-a-chacara/"
TITLE = "O Que Levar para a Chácara: Checklist Completo"
DESC = ("Checklist do que levar para um fim de semana ou festa na chácara: roupas, piscina, "
        "cozinha e churrasco, crianças, pet e os itens que todo mundo esquece.")
H1 = "O que levar para a chácara: checklist para o fim de semana"

FAQ = [
    ("Precisa levar roupa de cama e toalha para a chácara?",
     "Depende da chácara — muitas deixam roupa de cama e toalhas por conta do hóspede. Na Chácara Império, confirme pelo WhatsApp (34) 99169-0139 o que está incluído na sua reserva antes de arrumar a mala."),
    ("Posso levar meu cachorro para a Chácara Império?",
     "Pode. A Chácara Império aceita animais de estimação. Leve ração, potes, guia, a caminha dele e saquinhos para recolher a sujeira."),
    ("Que horas posso chegar e que horas preciso sair?",
     "Na hospedagem da Chácara Império, o check-in é a partir das 15h e o check-out até as 11h."),
    ("A Chácara Império tem churrasqueira e fogão a lenha?",
     "Tem os dois, na área gourmet, além de cozinha equipada. Planeje o carvão, o gelo e os temperos e pergunte pelo WhatsApp se a lenha está inclusa."),
    ("O que costuma ser esquecido numa viagem para a chácara?",
     "Os campeões de esquecimento são carregador de celular, repelente, protetor solar, remédios de uso contínuo, saco de lixo, abridor de garrafa, gelo e roupa extra para as crianças."),
]

BODY = f'''
<section class="section">
<div class="wrap">
<div class="prose">
<p class="updated">Atualizado em {D.UPDATED_HUMAN} · leitura de 6 minutos</p>
{answer("Para um fim de semana na chácara, leve roupas leves e de banho, protetor solar e repelente, toalhas e roupa de cama (se não estiverem incluídas), itens de higiene, a comida e a bebida já planejadas por refeição, carvão e gelo para o churrasco, remédios básicos e tudo o que as crianças e o pet usam no dia a dia. Antes de tudo, confirme com os anfitriões o que a casa já oferece.")}
{toc([("antes", "Antes de arrumar a mala"), ("roupas", "Roupas e itens pessoais"), ("piscina", "Piscina e sol"), ("cozinha", "Cozinha e churrasco"), ("criancas", "Para as crianças"), ("pet", "Para o pet"), ("esquecidos", "Os itens que todo mundo esquece"), ("festa", "Se for uma festa"), ("saida", "Na hora de ir embora"), ("perguntas", "Perguntas frequentes")])}

<h2 id="antes">Antes de arrumar a mala: confirme o que a chácara oferece</h2>
<p>Cada chácara funciona de um jeito. Algumas entregam a casa com roupa de cama, toalhas e utensílios; outras deixam boa parte disso por conta de quem aluga. Cinco minutos de conversa com o anfitrião evitam uma mala pesada demais — ou a falta de algo importante no sábado à noite.</p>
<p>Pergunte antes de sair de casa:</p>
{checks(["Roupa de cama e toalhas estão incluídas?", "A cozinha tem panelas, pratos, talheres e copos para todo o grupo?", "Carvão e lenha estão inclusos ou cada grupo leva o seu?", "Há geladeira ou freezer suficiente para as bebidas?", "Qual é o horário de check-in e de check-out?", "Animais de estimação são bem-vindos?", "Existe horário limite para som alto?"])}
<p>Na <a href="/hospedagem/">hospedagem da Chácara Império</a>, por exemplo, o check-in é a partir das 15h e o check-out até as 11h, a casa tem cozinha equipada, churrasqueira, fogão a lenha, Wi-Fi e ar-condicionado nas suítes, e o pet pode ir junto. O que estiver incluído na sua reserva — como roupa de cama e toalhas — vale confirmar direto pelo <a href="{D.wa_url("hospedagem")}" target="_blank" rel="noopener">WhatsApp</a>.</p>

<h2 id="roupas">Roupas e itens pessoais</h2>
<p>No Triângulo Mineiro os dias costumam ser quentes, mas a noite no campo pode esfriar — principalmente entre maio e agosto. Leve camadas.</p>
{checks(["Roupas leves para o dia e um agasalho para a noite", "Pijama e roupa de baixo para todos os dias, mais um conjunto extra", "Chinelo, tênis confortável e um calçado fechado para andar no gramado", "Boné ou chapéu", "Itens de higiene: escova e pasta de dente, sabonete, xampu, desodorante", "Roupa de cama e toalhas de banho, se não estiverem incluídas", "Remédios de uso contínuo e uma pequena farmácia: analgésico, antialérgico, curativos"])}

<h2 id="piscina">Piscina e sol</h2>
{checks(["Roupas de banho (uma para cada dia, assim sempre há uma seca)", "Toalhas de piscina, separadas das de banho", "Protetor solar e protetor labial", "Óculos de sol", "Boias e coletes para as crianças pequenas", "Saco plástico ou bolsa estanque para levar roupa molhada de volta"])}
{figure("piscinas-vista", "Piscina adulto e piscina infantil da Chácara Império")}
<p>Com piscina adulto e piscina infantil, o ideal é combinar um revezamento de adultos olhando as crianças na água — mesmo as que já nadam bem.</p>

<h2 id="cozinha">Cozinha e churrasco</h2>
<p>Comida é onde mais se gasta tempo e dinheiro. Monte um cardápio simples por refeição (café da manhã, almoço, lanche e jantar) e calcule as quantidades pelo número de pessoas. Assim você compra uma vez só e não precisa sair da chácara.</p>
{checks(["Carvão, acendedor e sal grosso", "Carnes temperadas em casa, em potes ou sacos bem fechados", "Gelo em quantidade — ele acaba antes da cerveja", "Caixas térmicas para bebidas", "Temperos, óleo, açúcar, café e filtro", "Papel-toalha, papel-alumínio e filme plástico", "Sacos de lixo grandes", "Abridor de garrafas e saca-rolhas", "Detergente e esponja, se não houver na casa", "Potes para guardar as sobras"])}
<p>Na Chácara Império, a área gourmet tem churrasqueira de tijolinho, fogão a lenha e bancada de granito — um bom lugar para reunir o grupo. Veja os detalhes na página da <a href="/estrutura/">estrutura</a>.</p>

<h2 id="criancas">Para as crianças</h2>
{checks(["Roupas extras — no mínimo uma troca a mais por dia", "Boias, colete e protetor solar infantil", "Repelente adequado para a idade", "Brinquedos para o gramado: bola, pipa, bambolê", "Lanches e mamadeiras do jeito que eles gostam", "Remédios e o cartão do plano de saúde"])}
<p>O parquinho com balanços e escorregador e a piscina infantil costumam ser o ponto alto do fim de semana para os pequenos.</p>

<h2 id="pet">Para o pet</h2>
{checks(["Ração para todos os dias e potes de água e comida", "Guia, coleira com identificação e caminha", "Saquinhos para recolher a sujeira", "Carteira de vacinação em dia", "Toalha velha para secar depois da piscina ou da chuva"])}

<h2 id="esquecidos">Os itens que todo mundo esquece</h2>
{checks(["Carregador de celular e uma extensão", "Lanterna ou lanterna de cabeça", "Repelente (de novo — ele merece aparecer duas vezes)", "Documento de identidade de todos", "Pilhas, se levar caixa de som ou brinquedos", "Um baralho ou jogos de tabuleiro para a noite"])}

<h2 id="festa">Se o fim de semana for uma festa</h2>
<p>Quando a hospedagem vem junto com um evento — um aniversário, uma reunião de família, um casamento —, a lista cresce um pouco:</p>
{checks(["Decoração, fita dupla face e abraçadeiras (combine antes o que pode ser fixado)", "Lista de convidados para organizar a entrada no portão", "Descartáveis extras e sacos de lixo grandes", "Gelo e caixas térmicas para as bebidas da festa", "Uma muda de roupa para trocar depois da festa", "Contato do buffet, do DJ e dos fornecedores à mão"])}
<p>Para planejar a festa do começo ao fim, veja também <a href="/guia/como-escolher-chacara-para-festa/">como escolher uma chácara para festa</a>.</p>

<h2 id="saida">Na hora de ir embora</h2>
<p>O check-out fica mais leve quando todos ajudam na última hora. Uma rotina simples:</p>
{checks(["Recolha todo o lixo e deixe nos locais combinados", "Desligue luzes, ar-condicionado e aparelhos", "Confira gavetas, banheiros, varal e geladeira", "Devolva as chaves e tranque tudo", "Faça uma última volta pela piscina e pelo gramado procurando brinquedos e toalhas"])}
<p>Objetos esquecidos dão trabalho para todo mundo — e nem sempre a chácara se responsabiliza por eles. Na dúvida, tire uma foto de cada quarto antes de sair.</p>

{faq_html(FAQ, "Perguntas frequentes")}
</div>
</div>
</section>

<section class="section section--sand">
<div class="wrap">
<h2>Leia também</h2>
{related([
    ("/hospedagem/", "suite-1", "Hospedagem para grupos", "A chácara inteira para até 40 pessoas, em 6 suítes."),
    ("/estrutura/", "gourmet-bar", "A estrutura da chácara", "Piscinas, área gourmet, salão coberto, campo e parquinho."),
    ("/guia/como-escolher-chacara-para-festa/", "salao", "Como escolher uma chácara para festa", "Os pontos que fazem diferença antes de fechar a data."),
])}
</div>
</section>

<section class="section section--tight">
<div class="wrap">{cta_band("Quer passar o fim de semana na Chácara Império?", key="hospedagem")}</div>
</section>
'''

PAGE = dict(
    path=PATH,
    title=TITLE,
    description=DESC,
    h1=H1,
    lead="Uma lista prática para não esquecer nada — da roupa de banho ao carvão, das crianças ao pet.",
    eyebrow="Guia",
    hero="piscinas-casa",
    crumbs=[("Início", "/"), ("Guia", "/guia/"), ("O que levar para a chácara", PATH)],
    page_type="WebPage",
    wa_key="hospedagem",
    faq=FAQ,
    schema=[article_schema(PATH, H1, DESC, "piscinas-casa", "2026-10-16")],
    body=BODY,
    guide=dict(summary="Checklist de roupas, piscina, cozinha, crianças, pet e saída.", minutes=6, pid="piscinas-casa"),
)
