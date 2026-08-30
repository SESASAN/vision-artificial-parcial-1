# Punto 3 (0.9) — Transformaciones de intensidad: gamma y logarítmica
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
plt.savefig("../results/punto3_gris.png", bbox_inches="tight", pad_inches=0)

# Transformación Gamma (γ=0.3)

gamma_03 = gamma_transform(gray, 0.3)

plt.imshow(gamma_03, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto3_gamma_0.3.png", bbox_inches="tight", pad_inches=0)

# Transformación Gamma (γ=2.3)

gamma_23 = gamma_transform(gray, 2.3)

plt.imshow(gamma_23, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto3_gamma_2.3.png", bbox_inches="tight", pad_inches=0)

# Transformación Logarítmica

log_img = log_transform(gray)

plt.imshow(log_img, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto3_log.png", bbox_inches="tight", pad_inches=0)
