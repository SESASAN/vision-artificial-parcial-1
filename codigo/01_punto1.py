# Punto 1 (0.5) — Recorte por indexación
#
# Usa indexación de matrices para recortar tu imagen para los rangos:
# - Filas: 300-659
# - Columnas: 200-839
# - Todos los componentes RGB

# numpy: manejo de la imagen como matriz (recortes, reflexiones,
#        reordenar canales) y funciones auxiliares como np.zeros_like.
# matplotlib.pyplot: mostrar y guardar (savefig) las imágenes resultantes.
# PIL.Image: leer archivos de imagen (.png/.tif) y convertir entre modos
#            de color (RGB, L = escala de grises).
# cv2 (OpenCV): trae las funciones de transformación de intensidad ya
#      implementadas (gammaCorrection, logTransform, contrastStretching,
#      bitwise_not, inRange), en vez de escribir la fórmula a mano.
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

# Recorte
#
# Realiza el recorte y muestra/guarda la imagen resultante (sin títulos de figura).

# Usa la versión ya redimensionada a 1024x1024 (ver 00_preparacion.ipynb)
img = np.array(Image.open("../images/cinnamorroll_1024.png").convert("RGB"))
print("original:", img.shape)

# Recorte por indexación de matrices (numpy puro, sin cv2): img[filas, columnas, canales].
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

# La relación de aspecto es la proporción ancho/alto. im.shape es
# (alto, ancho, canales), por eso se usa shape[1] (ancho) / shape[0] (alto).
def relacion_aspecto(im):
    h, w = im.shape[:2]
    return w / h

print(f"Original: {img.shape[1]}x{img.shape[0]} -> {relacion_aspecto(img):.4f}")
print(f"Recortada: {cropped.shape[1]}x{cropped.shape[0]} -> {relacion_aspecto(cropped):.4f}")
