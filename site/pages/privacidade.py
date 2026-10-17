import _data as D

PATH = "/politica-de-privacidade/"

BODY = f'''
<section class="section">
<div class="wrap">
<div class="prose">
<p class="updated">Atualizada em {D.UPDATED_HUMAN}</p>
<h2>Resumo</h2>
<p>Este site da {D.NAME} é informativo. Ele não tem cadastro, login nem formulário que envie dados para os nossos servidores. As reservas são feitas somente por telefone ou WhatsApp.</p>
<h2>Botões de WhatsApp e telefone</h2>
<p>Ao tocar num botão de WhatsApp, o site abre o aplicativo (ou o WhatsApp Web) com uma mensagem pronta. O formulário "Monte sua consulta" só monta esse texto no seu próprio navegador — nada é gravado ou enviado ao site. A conversa acontece no WhatsApp, que tem a sua própria política de privacidade. As informações que você nos enviar por lá (nome, data, número de pessoas) são usadas apenas para responder à sua consulta e organizar a reserva.</p>
<h2>Cookies e estatísticas</h2>
<p>O site não usa cookies de publicidade nem de rastreamento. Podemos usar estatísticas de acesso agregadas e anônimas da hospedagem do site (por exemplo, quantas pessoas visitaram cada página), sem identificar ninguém.</p>
<h2>Fotos e vídeos</h2>
<p>As fotos e vídeos publicados mostram a chácara e os anfitriões. Se você aparece em alguma imagem e quer que ela seja retirada, fale com a gente.</p>
<h2>Seus direitos (LGPD)</h2>
<p>Você pode pedir a qualquer momento a confirmação, a correção ou a exclusão dos dados que nos enviou, nos termos da Lei Geral de Proteção de Dados (Lei nº 13.709/2018).</p>
<h2>Contato</h2>
<p>Telefone e WhatsApp: <a href="{D.TEL_URL}">{D.PHONE_DISPLAY}</a> · Instagram: <a href="{D.INSTAGRAM}" target="_blank" rel="noopener">{D.INSTAGRAM_HANDLE}</a></p>
</div>
</div>
</section>
'''

PAGE = dict(
    path=PATH,
    title="Política de Privacidade – Chácara Império",
    description="Como o site da Chácara Império trata seus dados: sem cadastro nem cookies de rastreamento; reservas e conversas somente por telefone ou WhatsApp.",
    h1="Política de privacidade",
    eyebrow="Privacidade",
    hero_kind="none",
    crumbs=[("Início", "/"), ("Privacidade", PATH)],
    wa_key="geral",
    body='<section class="section section--tight"><div class="wrap"><h1>Política de privacidade</h1></div></section>' + BODY,
)
