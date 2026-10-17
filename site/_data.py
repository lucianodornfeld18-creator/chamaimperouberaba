"""Fonte única dos fatos da Chácara Império.

Regra: só entra aqui o que tem fonte. Cada bloco diz de onde veio.
Campos None = ainda não informados pelos donos; o site omite o que for None
(nada é inventado). Ver docs/OWNER-INPUTS.md.
"""
from urllib.parse import quote

SITE_URL = "https://chacaraimperiouberaba.com.br"
UPDATED = "2026-10-16"          # data da última revisão do conteúdo
UPDATED_HUMAN = "outubro de 2026"

# ── Identidade e contato ────────────────────────────────────────────────
# Fonte: Instagram @chacaraimperiouberaba (bio e link do WhatsApp), anúncio Airbnb.
NAME = "Chácara Império"
ALT_NAMES = ["Chácara Império Uberaba"]
# Nome antigo provável (caixa d'água das fotos diz "Chácara Alaska"). Só vai ao ar
# se os donos confirmarem; ver OWNER-INPUTS.
FORMER_NAME = None
TAGLINE = "Eventos e hospedagem em Uberaba"
CITY = "Uberaba"
STATE = "MG"
STATE_NAME = "Minas Gerais"
REGION = "Triângulo Mineiro"
COUNTRY = "BR"

PHONE_E164 = "+5534991690139"
PHONE_DISPLAY = "(34) 99169-0139"
WHATSAPP = "5534991690139"
EMAIL = None  # sugestão: contato@chacaraimperiouberaba.com.br (Email Routing)

INSTAGRAM = "https://www.instagram.com/chacaraimperiouberaba/"
INSTAGRAM_HANDLE = "@chacaraimperiouberaba"
AIRBNB = "https://www.airbnb.com.br/rooms/1548767361678241363"
GOOGLE_BUSINESS = None  # link do Perfil da Empresa no Google, quando existir
FACEBOOK = None

# Endereço: NÃO informado. O Airbnb só mostra um ponto aproximado.
ADDRESS = None  # ex.: {"street": "Rua X, 123", "district": "Bairro", "postal_code": "38000-000"}
GEO = None      # ex.: (-19.79, -48.01) — só com o ponto exato confirmado
MAPS_URL = None

# ── Anfitriões ──────────────────────────────────────────────────────────
# Fonte: post de boas-vindas no Instagram (11/06/2026) e anúncio Airbnb
# (anfitrião Luciano, coanfitriã Maria Inês, moram em Uberaba).
HOSTS = ["Maria Inês", "Luciano"]
HOSTS_PHRASE = "Maria Inês e Luciano"

# ── Números do espaço ───────────────────────────────────────────────────
# Fonte: descrição do anúncio no Airbnb escrita pelos donos.
FACTS = {
    "area_m2": 2500,
    "event_capacity": 250,
    "lodging_capacity": 40,
    "suites": 6,
    "beds": 40,
    "bathrooms": 8,
    "parking": 40,
    "checkin": "15:00",
    "checkout": "11:00",
}

# Fonte: anúncio Airbnb (descrição, comodidades e regras) + fotos do anúncio.
FEATURES = {
    "pools": "piscina adulto e piscina infantil",
    "gourmet": "área de lazer com espaço gourmet",
    "grill": "churrasqueira",
    "wood_stove": "fogão a lenha",
    "soccer": "campo de futebol gramado",
    "green": "área verde com gramado, coqueiros e jardins",
    "pergolas": "pérgolas de madeira no jardim",
    "playground": "parquinho com balanços e escorregador",
    "covered_hall": "salão coberto com forro de madeira",
    "living": "sala de estar e jantar",
    "kitchen": "cozinha equipada",
    "ac": "ar-condicionado nas suítes",
    "wifi": "Wi-Fi",
    "workspace": "espaço de trabalho",
    "outdoor_shower": "chuveiro externo",
    "outdoor_dining": "área de refeições ao ar livre",
    "gate": "portão eletrônico",
    "cameras": "câmeras de segurança nas varandas, no estacionamento e no portão",
    "paved": "acesso asfaltado",
    "urban": "dentro do perímetro urbano de Uberaba",
}

RULES = {
    "pets": True,                 # "Permitido animais de estimação"
    "commercial_photo": True,     # "Fotografia comercial permitida"
    "company_contracts": True,    # "Aceitamos contrato de locação temporário para empresas"
    "guests_use_all": True,       # "Os hóspedes podem usar todo o espaço da chácara"
    # Pendentes (donos): horário limite de som, buffet livre ou indicado,
    # roupa de cama/toalhas, caução, sinal, política de cancelamento.
    "sound_until": None,
    "own_buffet": None,
    "linens_included": None,
    "deposit": None,
    "cancellation": None,
}

PRICES = None  # tabela de preços dos donos; páginas de preço só são geradas com isto

# ── Distâncias (rodovia, a partir do centro de Uberaba) ─────────────────
# Fonte: OSRM (OpenStreetMap), consultado em 16/10/2026. Arredondadas.
DISTANCES = [
    ("Delta (MG)", 34), ("Igarapava (SP)", 42), ("Água Comprida (MG)", 46),
    ("Veríssimo (MG)", 47), ("Conquista (MG)", 60), ("Conceição das Alagoas (MG)", 65),
    ("Sacramento (MG)", 76), ("Nova Ponte (MG)", 81), ("Uberlândia (MG)", 107),
    ("Araxá (MG)", 119), ("Franca (SP)", 121), ("Frutal (MG)", 136),
    ("Barretos (SP)", 136), ("Araguari (MG)", 139), ("Ribeirão Preto (SP)", 171),
    ("Campinas (SP)", 389), ("Goiânia (GO)", 459), ("Belo Horizonte (MG)", 476),
    ("São Paulo (SP)", 481), ("Brasília (DF)", 525),
]

# ── WhatsApp: toda mensagem diz que a pessoa chegou pelo site ───────────
_WA_BASE = "Olá! Cheguei pelo site da Chácara Império"
WA_MESSAGES = {
    "geral": f"{_WA_BASE} e gostaria de consultar uma data.",
    "evento": f"{_WA_BASE} e quero consultar uma data para um evento.",
    "casamento": f"{_WA_BASE} e quero consultar datas e valores para um casamento.",
    "aniversario": f"{_WA_BASE} e quero consultar uma data para uma festa de aniversário.",
    "empresa": f"{_WA_BASE} e quero consultar uma data para um evento da minha empresa.",
    "familia": f"{_WA_BASE} e quero consultar uma data para uma reunião de família.",
    "fimdeano": f"{_WA_BASE} e quero consultar datas para o fim de ano (Natal ou Réveillon).",
    "ensaio": f"{_WA_BASE} e quero consultar uma data para um ensaio fotográfico.",
    "hospedagem": f"{_WA_BASE} e quero consultar hospedagem.",
    "expozebu": f"{_WA_BASE} e quero consultar hospedagem para o período da Expozebu.",
    "tour": f"{_WA_BASE}, vi o tour em vídeo e gostaria de consultar uma data.",
    "visita": f"{_WA_BASE} e gostaria de combinar uma visita para conhecer o espaço.",
    "en": "Hello! I found Chácara Império through your website and would like to check availability.",
}


def wa_url(key="geral", text=None):
    msg = text if text is not None else WA_MESSAGES[key]
    return f"https://wa.me/{WHATSAPP}?text={quote(msg)}"


TEL_URL = f"tel:{PHONE_E164}"

# ── Navegação ───────────────────────────────────────────────────────────
NAV = [
    ("Eventos", "/eventos/"),
    ("Hospedagem", "/hospedagem/"),
    ("Estrutura", "/estrutura/"),
    ("Galeria", "/galeria/"),
    ("Quem somos", "/sobre/"),
    ("Dúvidas", "/perguntas-frequentes/"),
    ("Como chegar", "/como-chegar/"),
]

FOOTER_LINKS = [
    ("Casamento", "/eventos/casamento/"),
    ("Aniversário e 15 anos", "/eventos/aniversario/"),
    ("Confraternização de empresa", "/eventos/confraternizacao-de-empresa/"),
    ("Reunião de família", "/eventos/reuniao-de-familia/"),
    ("Natal e Réveillon", "/eventos/natal-e-reveillon/"),
    ("Ensaio fotográfico", "/eventos/ensaio-fotografico/"),
    ("Hospedagem para grupos", "/hospedagem/"),
    ("Hospedagem na Expozebu", "/hospedagem/expozebu/"),
    ("Tour em vídeo", "/tour-em-video/"),
    ("Guia e dicas", "/guia/"),
    ("Como reservar", "/reservas/"),
]
