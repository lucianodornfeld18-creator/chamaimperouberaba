# O que falta dos donos — Chácara Império

O site foi montado só com fatos que têm fonte (anúncio do Airbnb, Instagram e fotos). Tudo o que
está abaixo ficou de fora ou genérico até vocês confirmarem. Cada item diz onde entra no site.

## Urgente (afeta Google e reservas)

1. **Endereço completo + CEP + link do Google Maps.** Hoje o site só diz "Uberaba – MG, dentro do
   perímetro urbano". O Airbnb aproxima a chácara da região da **Vila Real** — é isso mesmo? Vocês
   querem o endereço visível no site e no Google (recomendado para aparecer no mapa) ou só enviado
   pelo WhatsApp? → `site/_data.py` (`ADDRESS`, `GEO`, `MAPS_URL`), página Como chegar e schema.
2. **"Chácara Alaska".** A caixa d'água nas fotos do Airbnb diz "CHÁCARA ALASKA" (apagamos o letreiro
   nas fotos do site). É o nome antigo do espaço? Se for, vale escrever "antiga Chácara Alaska" no
   site: o Google ainda sugere "chacara alaska uberaba" no autocompletar, e essas buscas viriam para vocês.
3. **Direito de uso das fotos.** As fotos profissionais do Airbnb foram feitas para vocês ou vieram do
   dono anterior? Precisamos ter certeza de que podem ser usadas no site.
4. **Telefone.** O (34) 99169-0139 recebe ligação e WhatsApp e é atendido por vocês? É o único número?
5. **Perfil da Empresa no Google (Google Meu Negócio).** Já existe? Em qual conta? É o item que mais
   pesa para aparecer em "chácara para alugar em Uberaba".

6a. **Grafia na logo original.** O arquivo da logo (avatar do Instagram) está escrito **"CHÁÇARA"**,
   com cedilha. A logo foi redesenhada em vetor (`brand/`) já como **"CHÁCARA"**. Vale trocar também o
   avatar do Instagram, o WhatsApp Business e qualquer material impresso — use `brand/png/logo-chacara-imperio-1024.png`.

## Importante (deixa o site mais completo e mais citado pelas IAs)

6. **Valores**: diária/fim de semana, feriados, Réveillon, eventos por faixa de convidados, taxa de
   limpeza, caução, sinal, formas de pagamento, política de cancelamento. Com isso criamos a página
   "Quanto custa alugar a Chácara Império" (a pergunta mais feita no Google e no ChatGPT). Pode ser
   "a partir de R$ X".
7. **Regras de eventos**: horário limite do som, buffet livre ou indicado, decoração (o que pode
   fixar), fogos, uso da piscina durante a festa, horário de montagem/desmontagem.
8. **O que está incluído**: quantas mesas e cadeiras, utensílios de cozinha, roupa de cama e toalhas
   (o Airbnb marca "itens básicos" como não incluídos), lenha, gás, gelo, limpeza.
9. **Piscina**: é aquecida? Profundidade? **Salão**: quantas pessoas sentadas?
10. **Mínimo de diárias** e se fazem **day use** (só o dia, sem pernoite).
11. **Visitas**: dá para agendar visita antes de fechar? (o site já tem um botão "Quero conhecer a chácara".)
12. **História**: desde quando a chácara é de vocês, o porquê do nome "Império", quantos eventos já
    receberam — entra na página Quem somos.

## Para depois

13. **Fotos novas em alta resolução** (as do Airbnb são prints de celular, 1181 px de largura): campo de
    futebol de perto, salão montado com mesas e decoração, eventos reais, vista de drone, pôr do sol,
    fotos com pessoas (com autorização). E o **logo oficial** (hoje o site usa uma coroa provisória).
14. **Depoimentos**: os comentários do post de boas-vindas (Luciane, Luciano B., Karine, Reinaldo,
    Angélica, Lethicya) podem virar depoimentos no site — só com autorização de cada pessoa.
15. **E-mail** (opcional): dá para criar contato@chacaraimperiouberaba.com.br encaminhando para o Gmail.

## Para publicar no domínio

O domínio **chacaraimperiouberaba.com.br** foi registrado em 16/10/2026 no registro.br (titular:
Luciano Dornfeld Silva Junior), ainda com o DNS padrão do registro.br. Para o site aparecer nele:

1. Na Cloudflare (mesma conta dos outros sites): *Add a domain* → `chacaraimperiouberaba.com.br` → plano Free.
2. No registro.br: Domínio → DNS → *Alterar servidores DNS* → colar os dois servidores que a Cloudflare mostrar.
3. Depois que a zona ativar: Pages → projeto `chacaraimperiouberaba` → *Custom domains* → adicionar o
   domínio e o `www`.
4. Na zona: deixar **desligado** o bloqueio de bots de IA (*AI Crawl Control / Block AI bots*) e o
   *Managed robots.txt* — queremos que ChatGPT, Gemini, Claude e Perplexity leiam o site.
5. Google Search Console e Bing Webmaster Tools: adicionar o domínio e enviar `/sitemap.xml`.
