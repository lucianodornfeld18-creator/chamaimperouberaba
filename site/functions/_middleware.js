// Cloudflare Pages: www → domínio sem www, e noindex no endereço de teste *.pages.dev
const APEX = "chacaraimperiouberaba.com.br";

export async function onRequest(context) {
  const url = new URL(context.request.url);
  if (url.hostname === "www." + APEX) {
    url.hostname = APEX;
    return Response.redirect(url.toString(), 301);
  }
  const response = await context.next();
  if (url.hostname.endsWith(".pages.dev")) {
    const r = new Response(response.body, response);
    r.headers.set("X-Robots-Tag", "noindex, nofollow");
    return r;
  }
  return response;
}
