"""Recorta as faixas pretas dos prints do Airbnb (1181x2560) e salva só a foto.

Uso: python images/crop_screenshots.py
Entrada: images/incoming/airbnb/airbnb-NN.png (prints de celular, JPEG por dentro)
Saída:   images/source/airbnb-NN.jpg  (só a área da foto, qualidade 95, sem metadados)

Duplicatas exatas (mesmo MD5) são puladas e registradas no relatório.
"""
import hashlib
import os
import sys
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "incoming", "airbnb")
OUT = os.path.join(HERE, "source")


def photo_rows(im):
    """Devolve (top, bottom) do maior bloco contínuo de linhas que não são preto puro."""
    g = im.convert("L").resize((96, im.height))
    w = g.width
    data = g.load()
    rows = []
    for y in range(im.height):
        vals = [data[x, y] for x in range(w)]
        rows.append(max(vals) > 18 and (sum(vals) / w) > 6)
    best, cur_start, best_len = (0, 0), None, 0
    for y, ok in enumerate(rows + [False]):
        if ok and cur_start is None:
            cur_start = y
        elif not ok and cur_start is not None:
            if y - cur_start > best_len:
                best_len, best = y - cur_start, (cur_start, y)
            cur_start = None
    return best


def main():
    os.makedirs(OUT, exist_ok=True)
    seen = {}
    for name in sorted(os.listdir(SRC)):
        if not name.lower().endswith((".png", ".jpg", ".jpeg")):
            continue
        path = os.path.join(SRC, name)
        digest = hashlib.md5(open(path, "rb").read()).hexdigest()
        if digest in seen:
            print(f"{name}: duplicata de {seen[digest]} - pulada")
            continue
        seen[digest] = name
        im = Image.open(path).convert("RGB")
        top, bottom = photo_rows(im)
        # Fotos noturnas: o céu escuro parece faixa preta. As fotos 3:2 do anúncio
        # terminam na linha ~1674 e têm 788 linhas; nesse caso usa o bloco inteiro.
        if bottom - top < 780 and 1668 <= bottom <= 1676:
            top = bottom - 788
        # 2 px de margem para não pegar a borda escura do print
        crop = im.crop((0, top + 2, im.width, bottom - 2))
        dest = os.path.join(OUT, os.path.splitext(name)[0] + ".jpg")
        crop.save(dest, quality=95, optimize=True)
        print(f"{name}: linhas {top}-{bottom} -> {crop.width}x{crop.height}")


if __name__ == "__main__":
    sys.exit(main())
