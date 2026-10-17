from _components import btn_wa
from _icons import icon

BODY = f'''
<section class="section">
<div class="wrap narrow center">
<div class="ornament" aria-hidden="true">{icon("crown")}</div>
<h1>Página não encontrada</h1>
<p>O endereço pode ter mudado. Que tal seguir por um destes caminhos?</p>
<ul class="chips" style="justify-content:center">
<li><a href="/">Início</a></li><li><a href="/eventos/">Eventos</a></li><li><a href="/hospedagem/">Hospedagem</a></li>
<li><a href="/galeria/">Fotos</a></li><li><a href="/perguntas-frequentes/">Dúvidas</a></li><li><a href="/como-chegar/">Como chegar</a></li>
</ul>
<div class="btn-row mt-3" style="justify-content:center">{btn_wa("Falar no WhatsApp", "geral")}</div>
</div>
</section>
'''

PAGE = dict(
    path="/404.html",
    title="Página não encontrada – Chácara Império",
    description="A página que você procurou não existe. Veja eventos, hospedagem, fotos e como reservar a Chácara Império em Uberaba.",
    h1="Página não encontrada",
    hero_kind="none",
    noindex=True,
    wa_key="geral",
    body=BODY,
)
