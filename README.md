# Chácara Império — site

Site estático da Chácara Império (Uberaba – MG): eventos para até 250 convidados e hospedagem
para até 40 pessoas. Domínio: **chacaraimperiouberaba.com.br** (registro.br, registrado em 16/10/2026).
Reservas somente por telefone/WhatsApp (34) 99169-0139 — todo botão abre o WhatsApp com
"Olá! Cheguei pelo site da Chácara Império…".

## Como gerar

```bash
python images/crop_screenshots.py   # só se entrarem novos prints do Airbnb (recorta as faixas pretas)
python images/upscale_ai.py <realesrgan-ncnn-vulkan.exe> 0   # amplia as fotos 2x com IA → images/sr2x (já feito)
python brand/make_logo.py brand/fonts && python brand/render_png.py   # logo vetorial → brand/*.svg e brand/png
python images/process_photos.py     # fotos → site/static/img (WebP, até 1600/2000 px) e site/static/og (com a logo)
python video/make_tour.py all       # vídeos Full HD 30 fps (H.264 + AV1) e Reels vertical (~20 min)
python site/build.py                # gera site/dist
python qa/qa_all.py                 # verificação (precisa dar 0 FAIL)
python qa/shot.py / /eventos/ --full   # capturas em qa/shots (Playwright)
python -m http.server 8080 --directory site/dist   # ver no navegador
```

Requisitos: Python 3.12 com Pillow; `pip install imageio-ffmpeg` (traz o ffmpeg) para os vídeos;
Playwright só para as capturas.

## Onde está cada coisa

| Caminho | O quê |
|---|---|
| `site/_data.py` | **Fonte única dos fatos** (capacidade, regras, contato, mensagens do WhatsApp, endereço quando houver). `None` = ainda não informado → o site omite. |
| `brand/` | Logo redesenhada em vetor (SVG) a partir do avatar do Instagram, PNGs, fontes da logo e `comparacao-original-x-nova.png`. Corrige a grafia "CHÁÇARA" do arquivo original. |
| `images/sr2x/` | Fotos do anúncio ampliadas 2x por IA (Real-ESRGAN x4plus) — origem das fotos do site e dos vídeos. |
| `site/_photos.py` | Registro das fotos: nome do arquivo publicado, texto alternativo, legenda, categoria, ponto focal e retoques. |
| `site/pages/*.py` | Uma página por arquivo (`PAGE = dict(...)`). |
| `site/_layout.py` | `<head>`, schema.org (negócio, página, trilha, FAQ), cabeçalho, rodapé. |
| `site/_components.py` | Blocos reutilizáveis (resposta rápida, FAQ, cartões, galeria, montador de mensagem). |
| `site/static/` | CSS (vai embutido no HTML), JS, fontes, imagens e vídeos gerados. |
| `site/functions/_middleware.js` | `noindex` no endereço *.pages.dev e `www` → domínio sem www. |
| `docs/OWNER-INPUTS.md` | O que falta dos donos (endereço, preços, regras, fotos…). |
| `docs/PALAVRAS-CHAVE-E-ESTRATEGIA.md` | Pesquisa de palavras-chave, plano de SEO/GEO/AEO e ideias. |
| `docs/WRITING-GUIDE.md` | Regras de redação (nada inventado). |
| `images/incoming/` | Originais (prints do Airbnb, foto do Instagram). |
| `video/out/` | Vídeo vertical para Reels/Status (não vai para o site). |

## Regras

- Nada inventado sobre a chácara: só o que está em `_data.py`. Preço, endereço, horário de som,
  buffet e roupa de cama só entram quando os donos informarem.
- Fotos com o letreiro antigo "Chácara Alaska" foram retocadas (`retouch` em `_photos.py`); a foto
  `airbnb-03` não é usada.
- Para publicar: `python site/build.py`, `python qa/qa_all.py`, depois `git commit` + `git push` — a
  Cloudflare Pages (projeto `chacaraimperio`) publica `site/dist` sozinha. Passo a passo e domínio em
  `docs/PUBLICAR.md`.
