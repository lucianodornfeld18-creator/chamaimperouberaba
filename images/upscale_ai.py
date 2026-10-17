"""Amplia as fotos com IA (Real-ESRGAN x4plus, GPU) e guarda a versão 2x em images/sr2x/.

As fotos do anúncio são prints de celular com 1181 px de largura; ampliadas por IA ficam nítidas
o bastante para o vídeo em Full HD e para o topo do site em telas grandes.

Uso: python images/upscale_ai.py <caminho do realesrgan-ncnn-vulkan.exe> [id_da_gpu]
O executável vem do release oficial (github.com/xinntao/Real-ESRGAN, v0.2.5.0). Já processadas são puladas.
"""
import os
import subprocess
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "site"))
from _photos import PHOTOS  # noqa: E402

SRC = os.path.join(ROOT, "images", "source")
OUT = os.path.join(ROOT, "images", "sr2x")
TMP = os.path.join(ROOT, "images", "sr_tmp")


def main():
    exe = sys.argv[1]
    gpu = sys.argv[2] if len(sys.argv) > 2 else "0"
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(TMP, exist_ok=True)
    names = sorted({p["src"] for p in PHOTOS.values() if p["src"].startswith("airbnb-")})
    for i, name in enumerate(names, 1):
        dest = os.path.join(OUT, name)
        if os.path.exists(dest):
            continue
        src = os.path.join(SRC, name)
        tmp = os.path.join(TMP, os.path.splitext(name)[0] + ".png")
        subprocess.run([exe, "-i", src, "-o", tmp, "-n", "realesrgan-x4plus", "-g", gpu],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                       cwd=os.path.dirname(exe))
        w, h = Image.open(src).size
        Image.open(tmp).convert("RGB").resize((w * 2, h * 2), Image.LANCZOS).save(dest, quality=95, subsampling=0)
        os.remove(tmp)
        print(f"[{i}/{len(names)}] {name} -> {w * 2}x{h * 2}", flush=True)
    os.rmdir(TMP)


if __name__ == "__main__":
    main()
