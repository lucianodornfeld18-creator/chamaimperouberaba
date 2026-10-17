"""Fatia uma captura de página inteira em pedaços para revisão: python qa/slice.py arquivo.png [altura]"""
import os, sys
from PIL import Image
src = sys.argv[1]; h = int(sys.argv[2]) if len(sys.argv) > 2 else 1600
im = Image.open(src); base = os.path.splitext(src)[0]
for i, y in enumerate(range(0, im.height, h)):
    im.crop((0, y, im.width, min(y + h, im.height))).save(f"{base}-part{i+1}.png")
    print(f"{base}-part{i+1}.png")
