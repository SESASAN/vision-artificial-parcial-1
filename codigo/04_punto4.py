# Punto 4 (1.2) — Transformación lineal a trozos
#
# Nota: usa como entrada la imagen original en escala de grises. Asegúrate que las imágenes resultantes están en uint8 (rango 0-255).

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

# Imagen Original en Escala de Grises

img = np.array(Image.open("../images/cinnamorroll_1024.png").convert("RGB"))
gray = np.array(Image.fromarray(img).convert("L"))

plt.imshow(gray, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto4_gris.png", bbox_inches="tight", pad_inches=0)

# T. Lineal a Trozos — r1=10 r2=50 s1=95 s2=145

lineal_1 = np.zeros_like(gray)
cv2.intensity_transform.contrastStretching(gray, lineal_1, 10, 95, 50, 145)

plt.imshow(lineal_1, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto4_lineal_1.png", bbox_inches="tight", pad_inches=0)

# T. Lineal a Trozos — r1=60 r2=120 s1=95 s2=145

lineal_2 = np.zeros_like(gray)
cv2.intensity_transform.contrastStretching(gray, lineal_2, 60, 95, 120, 145)

plt.imshow(lineal_2, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto4_lineal_2.png", bbox_inches="tight", pad_inches=0)

# T. Lineal a Trozos — r1=150 r2=200 s1=95 s2=145

lineal_3 = np.zeros_like(gray)
cv2.intensity_transform.contrastStretching(gray, lineal_3, 150, 95, 200, 145)

plt.imshow(lineal_3, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto4_lineal_3.png", bbox_inches="tight", pad_inches=0)
