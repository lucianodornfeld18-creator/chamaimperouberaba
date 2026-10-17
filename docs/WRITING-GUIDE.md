# Guia de redação — site da Chácara Império

Vale para qualquer página nova em `site/pages/`. Leia antes de escrever.

## 1. Quem fala e com quem

- Idioma: português do Brasil, tratamento "você". Tom acolhedor, direto e mineiro sem caricatura.
- O site é da Chácara Império, em Uberaba (MG). Anfitriões: **Maria Inês e Luciano**.
- Leitor típico: quem está escolhendo onde fazer uma festa ou passar um fim de semana em Uberaba
  (noivos, mães organizando aniversário, RH de empresa, famílias, grupos que vêm para a Expozebu).

## 2. Regra de ouro: nada inventado

Só pode ser afirmado sobre a chácara o que está em `site/_data.py`:

- 2.500 m²; eventos até 250 convidados; hospedagem até 40 pessoas; 6 suítes; 40 camas; 8 banheiros;
  estacionamento para 40 carros; check-in a partir das 15h, check-out até as 11h.
- Piscina adulto e piscina infantil; área gourmet com churrasqueira e fogão a lenha; salão coberto;
  varandas; campo de futebol gramado; parquinho; jardins com pérgolas e carro de boi decorativo;
  sala de estar e jantar; cozinha equipada; ar-condicionado nas suítes; Wi-Fi; espaço de trabalho;
  chuveiro externo; portão eletrônico; câmeras externas (varandas, estacionamento, portão).
- Dentro do perímetro urbano de Uberaba, acesso asfaltado.
- Aceita animais de estimação; fotografia comercial permitida; aceita contrato de locação temporária
  para empresas; os hóspedes podem usar todo o espaço.
- Reservas **somente por telefone ou WhatsApp** (34) 99169-0139.

**Não sabemos (não afirmar, nem por dedução):** preços, endereço/bairro, horário limite de som,
se o buffet é livre ou indicado, se roupa de cama e toalhas estão incluídas, se a piscina é
aquecida, quantidade de mesas e cadeiras, gerador, acessibilidade, distância exata até pontos de
Uberaba, quantos eventos já foram feitos, desde quando a chácara funciona. Para esses pontos,
escreva algo como "confirme pelo WhatsApp" ou "pergunte aos anfitriões".

Proibido: "a melhor/maior chácara de Uberaba", depoimentos inventados, números de clientes,
prêmios, notas de avaliação, "mais de X anos", promessas de preço.

## 3. Fatos de fora (Uberaba, Expozebu, turismo)

- Só com fonte verificada na web. Anote cada fonte (URL + o que ela confirma) em `research/fontes.md`.
- Prefira fontes oficiais (prefeitura, UFTM, ABCZ, governo de MG) e veículos conhecidos.
- Datas, horários e preços de atrações mudam: não publique horário/ingresso; diga "confira no site oficial".
- Se duas fontes divergem, use a formulação mais segura ou omita.

## 4. Formato da página (módulo Python em `site/pages/`)

Modelo pronto: `site/pages/guia_o_que_levar.py`. Helpers em `site/_components.py`:
`answer()`, `toc()`, `checks()`, `figure()`, `faq_html()`, `related()`, `cta_band()`,
`article_schema()`, `btn_wa()`, `features()`, `tiles()`. Fotos: ids de `site/_photos.py`.
Chaves de WhatsApp: `WA_MESSAGES` em `site/_data.py` (toda mensagem já diz "Cheguei pelo site").

Cada guia precisa de:

1. `title` ≤ 60 caracteres, único; `description` 140–160 caracteres, única.
2. `answer()` logo no topo: resposta direta de 40–70 palavras para a pergunta principal (é o trecho
   que Google e assistentes de IA citam).
3. `toc()` com os H2. Todo H2 com `id`.
4. Parágrafos curtos (2–4 frases), listas quando couber, 1–3 fotos com `figure()`.
5. Uma seção que liga o tema à Chácara Império com fatos da seção 2 — sem forçar venda.
6. 4–6 perguntas frequentes (`FAQ` usado em `faq_html()` E em `PAGE["faq"]`), respostas que se
   sustentam sozinhas (citáveis fora de contexto, com o nome "Chácara Império" quando falar dela).
7. `related()` com 3 links internos e `cta_band(..., key=...)` no fim.
8. `PAGE` com `crumbs`, `hero`, `eyebrow="Guia"`, `schema=[article_schema(...)]`,
   `guide=dict(summary=..., minutes=..., pid=...)` (aparece no índice /guia/).
9. 1.000 a 1.600 palavras de texto útil. Nada de enchimento nem repetição entre páginas.

## 5. Antes de entregar

- `python site/build.py` sem erro (rodar na pasta do projeto).
- Abrir `site/dist/<caminho>/index.html` e conferir que não sobrou `{`, `}` ou chamada de helper como texto.
- Grep proibido no HTML gerado: `TODO`, `XXX`, `lorem`, `a melhor chácara`, `R$`.
