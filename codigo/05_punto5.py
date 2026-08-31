# Punto 5 (0.5) — Fraccionamiento de gris (gray-level slicing)
#
# Transformación que realza los píxeles en el rango [A,B] llevándolos a 255, y los demás a 0. Usa como entrada la imagen original en escala de grises. Asegúrate que las imágenes resultantes están en uint8 (rango 0-255).

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

import sys
sys.path.append("..")
from utils import to_uint8, gamma_transform, log_transform, piecewise_linear, gray_level_slicing

# Imagen Original en Escala de Grises

img = np.array(Image.open("../images/cinnamorroll_1024.png").convert("RGB"))
gray = np.array(Image.fromarray(img).convert("L"))

plt.imshow(gray, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto5_gris.png", bbox_inches="tight", pad_inches=0)

# T. Fraccionamiento de Gris — A=30 B=75

slicing_1 = gray_level_slicing(gray, A=30, B=75)

plt.imshow(slicing_1, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto5_slicing_1.png", bbox_inches="tight", pad_inches=0)

# T. Fraccionamiento de Gris — A=130 B=160

slicing_2 = gray_level_slicing(gray, A=130, B=160)

plt.imshow(slicing_2, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto5_slicing_2.png", bbox_inches="tight", pad_inches=0)

# T. Fraccionamiento de Gris — A=200 B=230

slicing_3 = gray_level_slicing(gray, A=200, B=230)

plt.imshow(slicing_3, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto5_slicing_3.png", bbox_inches="tight", pad_inches=0)
