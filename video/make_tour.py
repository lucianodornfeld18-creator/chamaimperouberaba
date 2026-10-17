"""Monta os vídeos do tour pela chácara a partir das fotos (efeito Ken Burns), em Full HD.

Uso: python video/make_tour.py [hero|hero-mobile|tour|reel|all]   (padrão: all)
Saídas em site/static/video/:
  tour-hero.mp4 (H.264) e tour-hero-av1.mp4 (AV1)  — fundo do topo da home, sem texto, loop perfeito
  tour-hero-mobile.mp4 / -av1.mp4 (720x1280)       — o mesmo passeio em pé, para o topo no celular
  tour.mp4 (H.264) e tour-av1.mp4 (AV1)            — tour completo com logo, legendas e cartão final
  tour-poster.jpg                                  — quadro de abertura (com a logo)
e em video/out/:
  tour-reels-1080x1920.mp4                         — versão vertical para Reels/Stories/Status

Qualidade: as fotos vêm de images/sr2x (ampliadas por IA, 2362 px) e a câmera nunca amplia além
do original. Cada vídeo é desenhado uma vez num master quase sem perdas e depois codificado.
"""
import math
import os
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "site"))
sys.path.insert(0, os.path.join(ROOT, "images"))
from _photos import PHOTOS  # noqa: E402
from process_photos import retouch  # noqa: E402

SRC = os.path.join(ROOT, "images", "source")
SR2X = os.path.join(ROOT, "images", "sr2x")
BRAND = os.path.join(ROOT, "brand")
OUT_SITE = os.path.join(ROOT, "site", "static", "video")
OUT_EXTRA = os.path.join(ROOT, "video", "out")
TMP = os.path.join(ROOT, "video", "tmp")
FPS = 30
W, H = 1920, 1080

CREAM = (247, 242, 230)
GOLD = (228, 208, 158)
FOREST = (16, 38, 27)


def ffmpeg_exe():
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


def brand_font(name, size, wght):
    f = ImageFont.truetype(os.path.join(BRAND, "fonts", name), size)
    try:
        f.set_variation_by_axes([wght])
    except Exception:
        pass
    return f


def cinzel(size):
    return brand_font("Cinzel[wght].ttf", size, 650)


def mont(size, wght=500):
    return brand_font("Montserrat[wght].ttf", size, wght)


def tracked(draw, xy, text, font, fill, tracking=0.0, anchor_center=False):
    """Texto com espaçamento entre letras (tracking em em)."""
    widths = [draw.textlength(ch, font=font) for ch in text]
    extra = tracking * font.size
    total = sum(widths) + extra * (len(text) - 1)
    x, y = xy
    if anchor_center:
        x -= total / 2
    for ch, w in zip(text, widths):
        draw.text((x, y), ch, font=font, fill=fill)
        x += w + extra
    return total


_LOGO = {}


def logo(px):
    if px not in _LOGO:
        im = Image.open(os.path.join(BRAND, "png", "logo-chacara-imperio-2048.png")).convert("RGBA")
        _LOGO[px] = im.resize((px, px), Image.LANCZOS)
    return _LOGO[px]


def load(pid):
    p = PHOTOS[pid]
    sr = os.path.join(SR2X, p["src"])
    scale = 2 if os.path.exists(sr) else 1
    im = ImageOps.exif_transpose(Image.open(sr if scale == 2 else os.path.join(SRC, p["src"]))).convert("RGB")
    if p.get("retouch"):  # mesmo retoque do site (letreiro antigo da caixa d'água)
        im = retouch(im, [tuple(v * scale for v in b) for b in p["retouch"]])
    return im


def ease(t):
    return 0.5 - 0.5 * math.cos(math.pi * max(0.0, min(1.0, t)))


def box_for(im, zoom, cx, cy, aspect):
    """Caixa (x0,y0,x1,y1) com a proporção de saída, zoom>=1 relativo ao maior recorte possível."""
    iw, ih = im.size
    bw = min(iw, ih * aspect)
    bh = bw / aspect
    bw, bh = bw / zoom, bh / zoom
    x0 = min(max(cx * iw - bw / 2, 0), iw - bw)
    y0 = min(max(cy * ih - bh / 2, 0), ih - bh)
    return (x0, y0, x0 + bw, y0 + bh)


MOVES = {
    "in": ((1.0, .5, .5), (1.12, .5, .52)),
    "out": ((1.13, .5, .52), (1.0, .5, .5)),
    "right": ((1.1, .41, .52), (1.1, .59, .52)),
    "left": ((1.1, .59, .52), (1.1, .41, .52)),
    "push": ((1.02, .5, .55), (1.16, .5, .5)),
}


class Shot:
    def __init__(self, pid, move, seconds, caption=None):
        self.pid, self.move, self.seconds, self.caption = pid, move, seconds, caption
        self.im = load(pid)

    def frame(self, t, size, aspect):
        (z0, x0, y0), (z1, x1, y1) = MOVES[self.move]
        e = ease(t)
        z, cx, cy = z0 + (z1 - z0) * e, x0 + (x1 - x0) * e, y0 + (y1 - y0) * e
        return self.im.transform(size, Image.EXTENT, box_for(self.im, z, cx, cy, aspect), Image.BICUBIC)


def caption_layer(frame, text, alpha):
    """Legenda no canto inferior esquerdo: fio dourado + nome do espaço em Cinzel."""
    if not text or alpha <= 0:
        return frame
    w, h = frame.size
    over = Image.new("RGBA", frame.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(over)
    pad = int(h * 0.065)
    for y in range(int(h * 0.6), h):  # véu escuro só embaixo
        a = int(165 * ((y - h * 0.6) / (h * 0.4)) ** 1.2 * alpha)
        d.line((0, y, w, y), fill=(10, 22, 16, a))
    y_line = h - pad - int(h * 0.088)
    d.line((pad, y_line, pad + int(h * 0.06), y_line), fill=GOLD + (int(255 * alpha),), width=max(2, h // 300))
    tracked(d, (pad, h - pad - int(h * 0.07)), text.upper(), cinzel(int(h * 0.046)), CREAM + (int(255 * alpha),), 0.06)
    return Image.alpha_composite(frame.convert("RGBA"), over).convert("RGB")


def logo_card(size, t, bg=None, subtitle=None, footer=None, logo_frac=0.56):
    """Cartão com a logo centralizada (abertura/encerramento). t de 0 a 1 controla o aparecimento."""
    w, h = size
    a = min(1.0, t / 0.22)
    if bg is None:
        base = Image.new("RGB", size, FOREST)
        glow = Image.new("L", size, 0)
        gd = ImageDraw.Draw(glow)
        for r in range(int(max(w, h) * 0.7), 0, -12):
            gd.ellipse((w / 2 - r, h * 0.45 - r, w / 2 + r, h * 0.45 + r), fill=int(70 * (1 - r / (max(w, h) * 0.7))))
        base = Image.composite(Image.new("RGB", size, (38, 80, 58)), base, glow.filter(ImageFilter.GaussianBlur(40)))
    else:
        base = Image.blend(bg, Image.new("RGB", size, (10, 22, 16)), 0.58)
    card = base.convert("RGBA")
    unit = min(w, h)
    lp = int(unit * logo_frac * (0.97 + 0.03 * ease(t)))
    lg = logo(lp).copy()
    if a < 1:
        lg.putalpha(lg.getchannel("A").point(lambda v: int(v * a)))
    top = int(h * 0.5 - lp * 0.62) if (subtitle or footer) else int(h / 2 - lp / 2)
    card.alpha_composite(lg, (int(w / 2 - lp / 2), top))
    d = ImageDraw.Draw(card)
    y = top + lp + unit * 0.05
    if subtitle:
        tracked(d, (w / 2, y), subtitle, mont(int(unit * 0.03)), GOLD + (int(255 * a),), 0.32, anchor_center=True)
        y += unit * 0.07
    for text, fnt, color, trk in (footer or []):
        tracked(d, (w / 2, y), text, fnt, color + (int(255 * a),), trk, anchor_center=True)
        y += fnt.size * 1.5
    return card.convert("RGB")


def shot_segment(sh, size, aspect, frame_fn=None):
    n = int(sh.seconds * FPS)

    def get(i):
        t = i / max(1, n - 1)
        return frame_fn(sh, t) if frame_fn else sh.frame(t, size, aspect)
    return n, get


def fn_segment(fn, seconds):
    n = int(seconds * FPS)
    return n, (lambda i: fn(i / n))


def caption_track(segs, texts, n_x):
    """Converte a legenda de cada segmento em intervalos de quadros de saída, juntando repetidas."""
    track, start = [], 0
    for (n, _), text in zip(segs, texts):
        if text:
            a, b = start + n_x // 2, start + n - n_x // 2
            if track and track[-1][2] == text and a - track[-1][1] <= n_x:
                track[-1][1] = b
            else:
                track.append([a, b, text])
        start += n - n_x
    return track


def render_master(segs, path, size, xfade=0.8, loop=False, texts=None, draw=None):
    """Desenha os quadros e grava um master H.264 quase sem perdas (crf 8). Devolve a duração."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    proc = subprocess.Popen([ffmpeg_exe(), "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
                             "-s", f"{size[0]}x{size[1]}", "-r", str(FPS), "-i", "-", "-c:v", "libx264",
                             "-preset", "fast", "-crf", "8", "-pix_fmt", "yuv444p", "-an", path], stdin=subprocess.PIPE)
    n_x = int(xfade * FPS)
    track = caption_track(segs, texts, n_x) if texts else []
    fade = int(0.4 * FPS)
    count = 0
    tail = None

    def out(fr):
        nonlocal count
        for a, b, text in track:
            if a <= count < b:
                alpha = min(1.0, (count - a) / fade, (b - 1 - count) / fade)
                fr = draw(fr, text, max(0.0, alpha))
        proc.stdin.write(fr.tobytes())
        count += 1
    for k, (n, get) in enumerate(segs):
        keep_tail = (k < len(segs) - 1) or loop
        new_tail = []
        for i in range(n):
            fr = get(i)
            if tail and i < len(tail):
                fr = Image.blend(tail[i], fr, (i + 1) / (len(tail) + 1))
            if keep_tail and i >= n - n_x:
                new_tail.append(fr)
                continue
            out(fr)
        tail = new_tail if keep_tail else None
    if loop and tail:
        first = segs[0][1](0)
        for i, fr in enumerate(tail):
            out(Image.blend(fr, first, (i + 1) / (len(tail) + 1)))
    proc.stdin.close()
    proc.wait()
    return count / FPS


def encode_h264(master, dest, crf, maxrate=None):
    """H.264 de reserva (navegadores sem AV1). maxrate em kbit/s segura o peso do arquivo."""
    cap = ["-maxrate", f"{maxrate}k", "-bufsize", f"{maxrate * 2}k"] if maxrate else []
    subprocess.run([ffmpeg_exe(), "-y", "-loglevel", "error", "-i", master, "-c:v", "libx264", "-preset", "slower",
                    "-crf", str(crf), *cap, "-x264-params", "aq-mode=3",
                    "-pix_fmt", "yuv420p", "-profile:v", "high", "-level", "4.1", "-movflags", "+faststart", "-an", dest],
                   check=True)
    print(f"{os.path.basename(dest)}: {os.path.getsize(dest) / 1024 / 1024:.1f} MB")


def encode_av1(master, dest, crf):
    subprocess.run([ffmpeg_exe(), "-y", "-loglevel", "error", "-i", master, "-c:v", "libaom-av1", "-crf", str(crf),
                    "-b:v", "0", "-cpu-used", "5", "-row-mt", "1", "-tiles", "2x2", "-pix_fmt", "yuv420p",
                    "-movflags", "+faststart", "-an", dest], check=True)
    print(f"{os.path.basename(dest)}: {os.path.getsize(dest) / 1024 / 1024:.1f} MB")


HERO_SEQ = [("piscina-banco", "in"), ("alameda", "push"), ("pergola-jardim", "right"), ("piscinas-vista", "out"),
            ("varanda-piscina", "left"), ("gourmet-bar", "in"), ("salao", "right"), ("suite-1", "in"),
            ("jardim-noite", "push"), ("piscinas-noite", "out"), ("carro-de-boi-noite", "left")]

TOUR_SEQ = [("alameda", "push", "A chegada"), ("casa-gramado", "right", "A casa e o gramado"),
            ("pergola-jardim", "in", "Jardins e pérgolas"), ("carro-de-boi", "left", "Jardins e pérgolas"),
            ("piscinas-casa", "out", "Piscina adulto e infantil"), ("piscinas-vista", "in", "Piscina adulto e infantil"),
            ("varanda-piscina", "right", "Varandas"), ("churrasqueira", "in", "Área gourmet"),
            ("gourmet-bar", "left", "Área gourmet"), ("salao", "push", "Salão coberto"),
            ("parquinho", "in", "Parquinho"), ("sala", "right", "Sala de estar e jantar"),
            ("cozinha", "in", "Cozinha"), ("suite-1", "left", "6 suítes · 40 camas"),
            ("suite-2", "in", "6 suítes · 40 camas"), ("jardim-noite", "push", "À noite"),
            ("pergola-noite", "out", "À noite"), ("piscinas-noite", "in", "À noite"),
            ("gourmet-noite", "right", "À noite"), ("portao-noite", "out", None)]


def make_hero():
    os.makedirs(OUT_SITE, exist_ok=True)
    segs = [shot_segment(Shot(p, m, 3.2), (W, H), W / H) for p, m in HERO_SEQ]
    master = os.path.join(TMP, "hero-master.mp4")
    dur = render_master(segs, master, (W, H), loop=True)
    print(f"hero: {dur:.1f}s")
    encode_h264(master, os.path.join(OUT_SITE, "tour-hero.mp4"), 23, 2400)
    encode_av1(master, os.path.join(OUT_SITE, "tour-hero-av1.mp4"), 34)


# Celular: quadro em pé (9:16) passeando na horizontal pelas fotos deitadas
MOVES_PORTRAIT = {
    "in": ((1.0, .5, .5), (1.10, .5, .52)),
    "out": ((1.10, .5, .52), (1.0, .5, .5)),
    "right": ((1.0, .30, .5), (1.0, .70, .5)),
    "left": ((1.0, .70, .5), (1.0, .30, .5)),
    "push": ((1.0, .5, .55), (1.14, .5, .5)),
}
HERO_MOBILE_SEQ = [("piscina-banco", "right"), ("alameda", "push"), ("pergola-jardim", "left"), ("piscinas-vista", "right"),
                   ("varanda-piscina", "left"), ("gourmet-bar", "right"), ("salao", "push"), ("suite-1", "left"),
                   ("jardim-noite", "right"), ("piscinas-noite", "left"), ("carro-de-boi-noite", "right")]


class PortraitShot(Shot):
    def frame(self, t, size, aspect):
        (z0, x0, y0), (z1, x1, y1) = MOVES_PORTRAIT[self.move]
        e = ease(t)
        z, cx, cy = z0 + (z1 - z0) * e, x0 + (x1 - x0) * e, y0 + (y1 - y0) * e
        return self.im.transform(size, Image.EXTENT, box_for(self.im, z, cx, cy, aspect), Image.BICUBIC)


def make_hero_mobile():
    os.makedirs(OUT_SITE, exist_ok=True)
    size = (720, 1280)
    segs = [shot_segment(PortraitShot(p, m, 3.2), size, size[0] / size[1]) for p, m in HERO_MOBILE_SEQ]
    master = os.path.join(TMP, "hero-mobile-master.mp4")
    dur = render_master(segs, master, size, loop=True)
    print(f"hero celular: {dur:.1f}s")
    encode_h264(master, os.path.join(OUT_SITE, "tour-hero-mobile.mp4"), 25, 1300)
    encode_av1(master, os.path.join(OUT_SITE, "tour-hero-mobile-av1.mp4"), 38)


def end_card_fn(size):
    unit = min(size)
    footer = [("RESERVAS PELO WHATSAPP", mont(int(unit * 0.03)), GOLD, 0.3),
              ("(34) 99169-0139", cinzel(int(unit * 0.07)), CREAM, 0.04),
              ("chacaraimperiouberaba.com.br", mont(int(unit * 0.032), 500), GOLD, 0.06)]
    return lambda t: logo_card(size, t, footer=footer, logo_frac=0.46)


def make_tour():
    os.makedirs(OUT_SITE, exist_ok=True)
    shots = [Shot(p, m, 2.9, c) for p, m, c in TOUR_SEQ]
    first = Shot("piscina-banco", "in", 3.5)

    def intro(t):
        return logo_card((W, H), t, bg=first.frame(t * 0.5, (W, H), W / H), subtitle="UM PASSEIO PELA CHÁCARA · UBERABA – MG")

    segs = [fn_segment(intro, 3.5)] + [shot_segment(sh, (W, H), W / H) for sh in shots] \
        + [fn_segment(end_card_fn((W, H)), 4.5)]
    texts = [None] + [sh.caption for sh in shots] + [None]
    master = os.path.join(TMP, "tour-master.mp4")
    dur = render_master(segs, master, (W, H), texts=texts, draw=caption_layer)
    print(f"tour: {dur:.1f}s")
    encode_h264(master, os.path.join(OUT_SITE, "tour.mp4"), 23, 2600)
    encode_av1(master, os.path.join(OUT_SITE, "tour-av1.mp4"), 32)
    intro(0.6).resize((1280, 720), Image.LANCZOS).save(os.path.join(OUT_SITE, "tour-poster.jpg"), quality=86,
                                                        optimize=True, progressive=True)
    with open(os.path.join(OUT_SITE, "tour.duration"), "w") as f:
        f.write(f"{dur:.1f}")


def make_reel():
    os.makedirs(OUT_EXTRA, exist_ok=True)
    size = (1080, 1920)
    shots = [Shot(p, m, 2.7, c) for p, m, c in TOUR_SEQ]
    blurred = {}
    top_logo = logo(330)

    def frame(sh, t):
        if sh.pid not in blurred:  # fundo: a própria foto ampliada e desfocada
            bg = ImageOps.fit(sh.im, size, Image.LANCZOS).filter(ImageFilter.GaussianBlur(30))
            blurred[sh.pid] = Image.blend(bg, Image.new("RGB", size, (10, 22, 16)), 0.42)
        canvas = blurred[sh.pid].copy().convert("RGBA")
        fg = sh.frame(t, (1080, 720), 1.5)
        canvas.paste(fg, (0, (1920 - 720) // 2))
        canvas.alpha_composite(top_logo, ((1080 - 330) // 2, 170))
        return canvas.convert("RGB")

    def cap(fr, text, a):
        if not text:
            return fr
        over = Image.new("RGBA", size, (0, 0, 0, 0))
        d = ImageDraw.Draw(over)
        tracked(d, (540, 1440), text.upper(), cinzel(58), CREAM + (int(255 * a),), 0.05, anchor_center=True)
        d.line((540 - 40, 1415, 540 + 40, 1415), fill=GOLD + (int(255 * a),), width=3)
        return Image.alpha_composite(fr.convert("RGBA"), over).convert("RGB")

    segs = [shot_segment(sh, size, 1.5, frame_fn=frame) for sh in shots] + [fn_segment(end_card_fn(size), 4.5)]
    texts = [sh.caption for sh in shots] + [None]
    master = os.path.join(TMP, "reel-master.mp4")
    render_master(segs, master, size, texts=texts, draw=cap)
    encode_h264(master, os.path.join(OUT_EXTRA, "tour-reels-1080x1920.mp4"), 20)


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "all"
    if what in ("hero", "all"):
        make_hero()
    if what in ("hero-mobile", "hero", "all"):
        make_hero_mobile()
    if what in ("tour", "all"):
        make_tour()
    if what in ("reel", "all"):
        make_reel()
