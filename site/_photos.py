"""Registro das fotos usadas no site.

Origem: fotos do anúncio da Chácara Império no Airbnb (prints de celular
recortados por images/crop_screenshots.py → images/source/airbnb-NN.jpg) e a
foto dos anfitriões do post do Instagram de 11/06/2026.

Cada foto: arquivo de origem, nome SEO do arquivo publicado, texto alternativo
(descreve só o que aparece), legenda curta, categoria da galeria, ponto focal
(object-position, em %) e retoques (caixas pintadas com a cor do entorno).
"""

PHOTOS = {
    "piscina-banco": dict(
        src="airbnb-26.jpg", slug="chacara-imperio-uberaba-piscina-com-palmeira",
        alt="Piscina da Chácara Império com banco de madeira, palmeira e a casa ao fundo, em dia de céu azul",
        caption="A piscina adulto, com a casa ao fundo", cat="piscina", focal=(50, 60)),
    "piscinas-casa": dict(
        src="airbnb-00.jpg", slug="chacara-imperio-uberaba-piscina-adulto-e-infantil",
        alt="Piscina adulto e piscina infantil em frente à casa principal, com gramado e palmeira",
        caption="Piscina adulto e piscina infantil", cat="piscina", focal=(40, 55)),
    "piscinas-vista": dict(
        src="airbnb-27.jpg", slug="chacara-imperio-uberaba-duas-piscinas",
        alt="Vista das duas piscinas, adulto e infantil, com deque de pedra e espreguiçadeiras",
        caption="As duas piscinas vistas do alto", cat="piscina", focal=(50, 60)),
    "piscina-luminarias": dict(
        src="airbnb-19.jpg", slug="chacara-imperio-uberaba-area-da-piscina",
        alt="Área da piscina com luminárias de globo, deque de pedra, palmeiras e as varandas ao fundo",
        caption="A área da piscina e as varandas", cat="piscina", focal=(55, 60)),
    "piscina-ceu": dict(
        src="airbnb-23.jpg", slug="chacara-imperio-uberaba-piscina-e-jardim",
        alt="Piscina com banco de jardim, gramado e casa com telhado de telha, sob céu com nuvens",
        caption="Piscina, gramado e casa", cat="piscina", focal=(55, 62)),
    "piscina-deque": dict(
        src="airbnb-20.jpg", slug="chacara-imperio-uberaba-deque-da-piscina",
        alt="Deque de pedra e piscinas vistos da varanda, com cerca de madeira e muro com palmeiras",
        caption="O deque visto da varanda", cat="piscina", focal=(50, 60)),
    "piscina-casa-principal": dict(
        src="airbnb-24.jpg", slug="chacara-imperio-uberaba-piscina-e-casa-principal",
        alt="Piscina cercada por deque de pedra com a casa principal ao fundo",
        caption="Deque da piscina e casa principal", cat="piscina", focal=(40, 55)),
    "piscinas-noite": dict(
        src="airbnb-22.jpg", slug="chacara-imperio-uberaba-piscinas-iluminadas-a-noite",
        alt="Piscina adulto e piscina infantil iluminadas à noite, com luminárias e palmeiras",
        caption="As piscinas iluminadas à noite", cat="noite", focal=(50, 60)),
    "piscina-noite-2": dict(
        src="airbnb-29.jpg", slug="chacara-imperio-uberaba-piscina-a-noite",
        alt="Piscina à noite com luminárias acesas e cerca de madeira",
        caption="Noite na área da piscina", cat="noite", focal=(50, 60)),
    "varanda-piscina": dict(
        src="airbnb-21.jpg", slug="chacara-imperio-uberaba-varanda-com-vista-para-a-piscina",
        alt="Varanda coberta com forro de madeira e vista para a piscina",
        caption="Varanda coberta de frente para a piscina", cat="area-gourmet", focal=(50, 55)),
    "area-coberta-mesas": dict(
        src="airbnb-28.jpg", slug="chacara-imperio-uberaba-area-coberta-com-mesas",
        alt="Área coberta com mesas de madeira rústica e vista para a piscina no fim da tarde",
        caption="Mesas rústicas na área coberta", cat="area-gourmet", focal=(50, 55)),
    "salao": dict(
        src="airbnb-31.jpg", slug="chacara-imperio-uberaba-salao-coberto-para-festas",
        alt="Salão coberto para festas com forro de madeira, ventiladores, cadeiras empilhadas e mesas ao fundo",
        caption="O salão coberto para festas", cat="salao", focal=(50, 55)),
    "churrasqueira": dict(
        src="airbnb-33.jpg", slug="chacara-imperio-uberaba-churrasqueira",
        alt="Churrasqueira de tijolinho na área gourmet, com balcão de granito e expositor de bebidas",
        caption="Churrasqueira de tijolinho", cat="area-gourmet", focal=(35, 55)),
    "gourmet-bar": dict(
        src="airbnb-34.jpg", slug="chacara-imperio-uberaba-area-gourmet-com-bar",
        alt="Área gourmet com churrasqueira, balcão de bar em granito e banquetas",
        caption="Área gourmet com balcão", cat="area-gourmet", focal=(55, 55)),
    "gourmet-noite": dict(
        src="airbnb-35.jpg", slug="chacara-imperio-uberaba-area-gourmet-a-noite",
        alt="Área gourmet à noite, com bancada de granito, mesas de madeira e a piscina iluminada ao fundo",
        caption="Área gourmet à noite", cat="noite", focal=(50, 55)),
    "varanda-mesa": dict(
        src="airbnb-30.jpg", slug="chacara-imperio-uberaba-varanda-com-mesa-de-madeira",
        alt="Varanda com mesa redonda de madeira, cadeiras e vista para o jardim",
        caption="Varanda com vista para o jardim", cat="area-gourmet", focal=(40, 60)),
    "varanda-noite": dict(
        src="airbnb-06.jpg", slug="chacara-imperio-uberaba-varanda-a-noite",
        alt="Varanda coberta com mesas de madeira e o jardim iluminado à noite",
        caption="Varanda e jardim à noite", cat="noite", focal=(45, 60)),
    "alameda": dict(
        src="airbnb-07.jpg", slug="chacara-imperio-uberaba-entrada-e-campo-de-futebol",
        alt="Alameda de entrada com palmeiras e, à esquerda, o campo de futebol gramado cercado por alambrado",
        caption="A entrada e o campo de futebol", cat="lazer", focal=(50, 55),
        retouch=[(739, 286, 757, 300)]),
    "estacionamento": dict(
        src="airbnb-08.jpg", slug="chacara-imperio-uberaba-estacionamento",
        alt="Estacionamento amplo de brita, com gramado, árvores e o parquinho ao fundo",
        caption="Estacionamento para 40 carros", cat="lazer", focal=(50, 60)),
    "parquinho": dict(
        src="airbnb-17.jpg", slug="chacara-imperio-uberaba-parquinho",
        alt="Parquinho com balanços e escorregador na areia, iluminado à noite",
        caption="Parquinho para as crianças", cat="lazer", focal=(45, 60)),
    "casa-gramado": dict(
        src="airbnb-02.jpg", slug="chacara-imperio-uberaba-casa-e-gramado",
        alt="Casa das suítes com janelas em arco, gramado e palmeiras em dia de sol",
        caption="A casa e o gramado", cat="jardim", focal=(55, 60)),
    "pergola-jardim": dict(
        src="airbnb-04.jpg", slug="chacara-imperio-uberaba-pergola-no-jardim",
        alt="Pérgola de madeira no jardim, com gramado, coqueiro e a casa ao fundo",
        caption="Pérgola de madeira no jardim", cat="jardim", focal=(40, 55)),
    "pergola-varanda": dict(
        src="airbnb-11.jpg", slug="chacara-imperio-uberaba-pergola-e-gramado",
        alt="Pérgola de madeira sobre o gramado, com a varanda da casa ao fundo",
        caption="Pérgola e gramado", cat="jardim", focal=(45, 55)),
    "jardim-coqueiro": dict(
        src="airbnb-05.jpg", slug="chacara-imperio-uberaba-jardim-com-coqueiro",
        alt="Jardim com coqueiro, caminho de pedriscos e roda de carroça decorativa ao lado da casa",
        caption="Jardim lateral", cat="jardim", focal=(55, 55)),
    "jardim-lateral": dict(
        src="airbnb-10.jpg", slug="chacara-imperio-uberaba-jardim-lateral",
        alt="Jardim lateral com coqueiro, ciprestes junto ao muro e roda de carroça decorativa",
        caption="Coqueiros e ciprestes", cat="jardim", focal=(55, 55)),
    "jardim-banco": dict(
        src="airbnb-16.jpg", slug="chacara-imperio-uberaba-jardim-com-banco",
        alt="Jardim com gramado, coqueiros, canteiro de flores e banco decorativo vermelho",
        caption="Cantinho do jardim", cat="jardim", focal=(40, 55)),
    "carro-de-boi": dict(
        src="airbnb-15.jpg", slug="chacara-imperio-uberaba-carro-de-boi-e-pergola",
        alt="Carro de boi decorativo e pérgola no jardim ao entardecer",
        caption="Carro de boi e pérgola", cat="jardim", focal=(40, 60)),
    "jardim-noite": dict(
        src="airbnb-09.jpg", slug="chacara-imperio-uberaba-jardim-iluminado-a-noite",
        alt="Jardim iluminado à noite, com palmeiras, pérgola e a casa ao fundo",
        caption="O jardim iluminado", cat="noite", focal=(50, 60)),
    "pergola-noite": dict(
        src="airbnb-12.jpg", slug="chacara-imperio-uberaba-pergola-iluminada",
        alt="Pérgola de madeira iluminada à noite, junto à varanda da casa",
        caption="Pérgola iluminada", cat="noite", focal=(45, 60)),
    "carro-de-boi-noite": dict(
        src="airbnb-13.jpg", slug="chacara-imperio-uberaba-carro-de-boi-a-noite",
        alt="Carro de boi decorativo e pérgola no jardim iluminado à noite",
        caption="Carro de boi à noite", cat="noite", focal=(40, 60)),
    "coqueiro-noite": dict(
        src="airbnb-14.jpg", slug="chacara-imperio-uberaba-coqueiro-iluminado",
        alt="Coqueiro iluminado em verde no jardim, à noite",
        caption="Coqueiro iluminado", cat="noite", focal=(50, 55)),
    "portao-noite": dict(
        src="airbnb-01.jpg", slug="chacara-imperio-uberaba-portao-de-entrada",
        alt="Portão de entrada da Chácara Império iluminado à noite, com palmeiras e muro com trepadeiras",
        caption="O portão de entrada à noite", cat="noite", focal=(50, 60)),
    "sala": dict(
        src="airbnb-36.jpg", slug="chacara-imperio-uberaba-sala-de-estar-e-jantar",
        alt="Sala de estar com sofás e TV em painel de madeira e mesa de jantar de madeira",
        caption="Sala de estar e jantar", cat="casa", focal=(50, 55)),
    "sala-2": dict(
        src="airbnb-37.jpg", slug="chacara-imperio-uberaba-sala",
        alt="Sala com sofás de couro, mesa de jantar de madeira com cadeiras e TV",
        caption="Sala com mesa de jantar", cat="casa", focal=(50, 55)),
    "cozinha": dict(
        src="airbnb-38.jpg", slug="chacara-imperio-uberaba-cozinha",
        alt="Cozinha com fogão, geladeira, micro-ondas e bancada de granito",
        caption="Cozinha equipada", cat="casa", focal=(50, 55)),
    "suite-1": dict(
        src="airbnb-39.jpg", slug="chacara-imperio-uberaba-suite-cama-de-casal-e-beliches",
        alt="Suíte com cama de casal, beliches de madeira e ar-condicionado",
        caption="Suíte com cama de casal e beliches", cat="suites", focal=(50, 55)),
    "suite-2": dict(
        src="airbnb-41.jpg", slug="chacara-imperio-uberaba-suite-com-beliches",
        alt="Suíte com cama de casal entre dois beliches de madeira e ar-condicionado",
        caption="Suíte para famílias", cat="suites", focal=(50, 55)),
    "suite-3": dict(
        src="airbnb-42.jpg", slug="chacara-imperio-uberaba-suite-iluminada",
        alt="Suíte com beliche de madeira, cama de casal e porta do banheiro",
        caption="Suíte com banheiro", cat="suites", focal=(45, 55)),
    "suite-4": dict(
        src="airbnb-43.jpg", slug="chacara-imperio-uberaba-suite-com-banheiro",
        alt="Suíte com beliches, cama de casal e banheiro com box de vidro ao fundo",
        caption="Suíte com beliches", cat="suites", focal=(50, 55)),
    "suite-5": dict(
        src="airbnb-46.jpg", slug="chacara-imperio-uberaba-suite-com-ventilador",
        alt="Suíte com camas e beliches de madeira, ar-condicionado e ventilador de teto",
        caption="Suíte com ar e ventilador", cat="suites", focal=(50, 55)),
    "suite-6": dict(
        src="airbnb-48.jpg", slug="chacara-imperio-uberaba-suite-forro-de-madeira",
        alt="Suíte com forro de madeira, beliches e cama de solteiro",
        caption="Suíte com forro de madeira", cat="suites", focal=(45, 55)),
    "anfitrioes": dict(
        src="anfitrioes.jpg", slug="maria-ines-e-luciano-anfitrioes-chacara-imperio",
        alt="Maria Inês e Luciano, anfitriões da Chácara Império, sorrindo ao lado da piscina",
        caption="Maria Inês e Luciano, os anfitriões", cat=None, focal=(50, 35), portrait=True),
}

GALLERY_CATS = [
    ("todas", "Todas"),
    ("piscina", "Piscinas"),
    ("area-gourmet", "Área gourmet e varandas"),
    ("salao", "Salão"),
    ("jardim", "Jardins"),
    ("lazer", "Lazer e chegada"),
    ("casa", "Casa"),
    ("suites", "Suítes"),
    ("noite", "À noite"),
]

HERO = "piscina-banco"
