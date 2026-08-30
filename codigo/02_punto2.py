# Punto 2 (0.5) — Indexado de matrices
#
# Haz uso de indexado de matrices para realizar las siguientes operaciones y llena la tabla con las imágenes resultantes:
# - Modifica la imagen RGB para que quede en orden BGR.
# - Reflexión sobre las columnas (espejo horizontal).
# - Reflexión sobre las filas (inversión vertical).

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

import sys
sys.path.append("..")
from utils import to_uint8, gamma_transform, log_transform, piecewise_linear, gray_level_slicing

# Imagen Original RGB

img = np.array(Image.open("../images/cinnamorroll_1024.png").convert("RGB"))
print(img.shape)

plt.imshow(img)
plt.axis("off")

# Imagen Reordenada - BGR

# Indexación de matrices: invierte el orden del último eje (canales)
bgr = img[:, :, ::-1]

plt.imshow(bgr)
plt.axis("off")
plt.savefig("../results/punto2_bgr.png", bbox_inches="tight", pad_inches=0)

# Imagen Efecto Espejo

# Reflexión sobre las columnas (invierte el eje horizontal)
espejo = img[:, ::-1, :]

plt.imshow(espejo)
plt.axis("off")
plt.savefig("../results/punto2_espejo.png", bbox_inches="tight", pad_inches=0)

# Imagen Inversión Vertical

# Reflexión sobre las filas (invierte el eje vertical)
invertida = img[::-1, :, :]

plt.imshow(invertida)
plt.axis("off")
plt.savefig("../results/punto2_inversion_vertical.png", bbox_inches="tight", pad_inches=0)
