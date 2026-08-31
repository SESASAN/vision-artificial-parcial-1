# Punto 1 (0.5) — Recorte por indexación
#
# Usa indexación de matrices para recortar tu imagen para los rangos:
# - Filas: 300-659
# - Columnas: 200-839
# - Todos los componentes RGB

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

# Recorte
#
# Realiza el recorte y muestra/guarda la imagen resultante (sin títulos de figura).

img = np.array(Image.open("../images/cinnamorroll_1024.png").convert("RGB"))
print("original:", img.shape)

# Recorte por indexación de matrices
cropped = img[300:660, 200:840, :]
print("recortada:", cropped.shape)

plt.imshow(cropped)
plt.axis("off")
plt.savefig("../results/punto1_recorte.png", bbox_inches="tight", pad_inches=0)

# Relación de aspecto
#
# ¿Cuál es la relación de aspecto de la imagen original?
#
# *Responda aquí.*
#
# ¿Cuál es la relación de aspecto de la imagen recortada?
#
# *Responda aquí.*

def relacion_aspecto(im):
    h, w = im.shape[:2]
    return w / h

print(f"Original: {img.shape[1]}x{img.shape[0]} -> {relacion_aspecto(img):.4f}")
print(f"Recortada: {cropped.shape[1]}x{cropped.shape[0]} -> {relacion_aspecto(cropped):.4f}")
