# Como publicar o site (GitHub + Cloudflare Pages)

- Código: **github.com/lucianodornfeld18-creator/chamaimperouberaba** (branch `main`)
- Cloudflare Pages: projeto **`chacaraimperio`** → https://chacaraimperio.pages.dev (prévia, com `noindex`)
- Domínio: **chacaraimperiouberaba.com.br** (registro.br) — ainda precisa apontar para a Cloudflare (abaixo)

## Publicar uma alteração (dia a dia)

```bash
python site/build.py        # gera site/dist
python qa/qa_all.py         # tem que terminar com 0 FAIL
git add -A
git commit -m "o que mudou"
git push                    # a Cloudflare publica sozinha em ~1 minuto
```

A Cloudflare **não roda o build**: ela publica a pasta `site/dist` que vai no commit. Por isso o
`python site/build.py` precisa rodar antes do commit. Fotos novas: `python images/process_photos.py`
antes do build. Vídeos: `python video/make_tour.py all`.

## Configuração do projeto na Cloudflare (já feita)

| Campo | Valor |
|---|---|
| Repositório | lucianodornfeld18-creator/chamaimperouberaba |
| Branch de produção | main |
| Framework preset | None |
| Build command | *(vazio)* |
| Build output directory | `dist` |
| Root directory | `site` |

Com a raiz em `site`, a Cloudflare publica `site/dist` e usa `site/functions/_middleware.js`
(que põe `noindex` no endereço .pages.dev e manda `www` para o domínio sem www).

## Colocar o domínio no ar (uma vez só)

1. **Cloudflare** → *Add a domain* → `chacaraimperiouberaba.com.br` → plano **Free**. Anote os dois
   servidores de nome que ela mostrar (algo como `xxxx.ns.cloudflare.com`).
2. **registro.br** → entrar → o domínio → **DNS** → *Alterar servidores DNS* → colar os dois
   servidores da Cloudflare → salvar. Leva de alguns minutos a algumas horas.
3. Quando a Cloudflare mostrar o domínio como **Active**: *Workers & Pages* → `chacaraimperio` →
   *Custom domains* → *Set up a custom domain* → `chacaraimperiouberaba.com.br` e depois
   `www.chacaraimperiouberaba.com.br`. A Cloudflare cria os registros de DNS sozinha.
4. Na zona do domínio: deixar **desligado** *Block AI bots* / *AI Crawl Control* e o
   *Managed robots.txt* (o site quer ser lido pelo ChatGPT, Gemini, Claude e Perplexity).
5. **Google Search Console** e **Bing Webmaster Tools**: adicionar o domínio e enviar
   `https://chacaraimperiouberaba.com.br/sitemap.xml`.

## Observações

- O projeto antigo **`chacaraimperiouberaba`** (prévia por upload direto, sem Git) pode ser apagado
  depois que o domínio estiver no projeto `chacaraimperio`.
- O vídeo vertical para Reels (`video/out/`) fica fora do Git por ser grande (38 MB).
