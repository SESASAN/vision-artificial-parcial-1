# Punto 4 (1.2) — Transformación lineal a trozos
#
# Nota: usa como entrada la imagen original en escala de grises. Asegúrate que las imágenes resultantes están en uint8 (rango 0-255).

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
plt.savefig("../results/punto4_gris.png", bbox_inches="tight", pad_inches=0)

# T. Lineal a Trozos — r1=10 r2=50 s1=95 s2=145

lineal_1 = piecewise_linear(gray, r1=10, s1=95, r2=50, s2=145)

plt.imshow(lineal_1, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto4_lineal_1.png", bbox_inches="tight", pad_inches=0)

# T. Lineal a Trozos — r1=60 r2=120 s1=95 s2=145

lineal_2 = piecewise_linear(gray, r1=60, s1=95, r2=120, s2=145)

plt.imshow(lineal_2, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto4_lineal_2.png", bbox_inches="tight", pad_inches=0)

# T. Lineal a Trozos — r1=150 r2=200 s1=95 s2=145

lineal_3 = piecewise_linear(gray, r1=150, s1=95, r2=200, s2=145)

plt.imshow(lineal_3, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto4_lineal_3.png", bbox_inches="tight", pad_inches=0)
