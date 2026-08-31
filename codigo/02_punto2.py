# Punto 2 (0.5) — Indexado de matrices
#
# Haz uso de indexado de matrices para realizar las siguientes operaciones y llena la tabla con las imágenes resultantes:
# - Modifica la imagen RGB para que quede en orden BGR.
# - Reflexión sobre las columnas (espejo horizontal).
# - Reflexión sobre las filas (inversión vertical).

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

# Imagen Original RGB

img = np.array(Image.open("../images/cinnamorroll_1024.png").convert("RGB"))
print(img.shape)

plt.imshow(img)
plt.axis("off")

# Imagen Reordenada - BGR

# Indexación de matrices (numpy puro): paso negativo (::-1) sobre el
# último eje, que corresponde a los canales de color. Invierte el orden
# RGB -> BGR, intercambiando el canal rojo con el azul.
bgr = img[:, :, ::-1]

plt.imshow(bgr)
plt.axis("off")
plt.savefig("../results/punto2_bgr.png", bbox_inches="tight", pad_inches=0)

# Imagen Efecto Espejo

# Índice con paso negativo (::-1) sobre el eje de las columnas (eje 1):
# recorre las columnas de derecha a izquierda -> espejo horizontal.
espejo = img[:, ::-1, :]

plt.imshow(espejo)
plt.axis("off")
plt.savefig("../results/punto2_espejo.png", bbox_inches="tight", pad_inches=0)

# Imagen Inversión Vertical

# Índice con paso negativo (::-1) sobre el eje de las filas (eje 0):
# recorre las filas de abajo hacia arriba -> inversión vertical.
invertida = img[::-1, :, :]

plt.imshow(invertida)
plt.axis("off")
plt.savefig("../results/punto2_inversion_vertical.png", bbox_inches="tight", pad_inches=0)
