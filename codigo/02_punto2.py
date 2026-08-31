# Punto 2 (0.5) — Indexado de matrices
#
# Haz uso de indexado de matrices para realizar las siguientes operaciones y llena la tabla con las imágenes resultantes:
# - Modifica la imagen RGB para que quede en orden BGR.
# - Reflexión sobre las columnas (espejo horizontal).
# - Reflexión sobre las filas (inversión vertical).

# numpy: manejo de la imagen como matriz (arreglo N-dimensional) y toda la
#        indexación (recortes, reflexiones, reordenar canales).
# matplotlib.pyplot: mostrar y guardar (savefig) las imágenes resultantes.
# PIL.Image: leer archivos de imagen (.png/.tif) y convertir entre modos
#            de color (RGB, L = escala de grises).
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# sys.path.append("..") permite importar utils.py, que está un nivel arriba
# (en la raíz del proyecto), desde dentro de la carpeta notebooks/.
import sys
sys.path.append("..")
from utils import to_uint8, gamma_transform, log_transform, piecewise_linear, gray_level_slicing

# Imagen Original RGB

img = np.array(Image.open("../images/cinnamorroll_1024.png").convert("RGB"))
print(img.shape)

plt.imshow(img)
plt.axis("off")

# Imagen Reordenada - BGR

# Indexación de matrices con paso negativo (::-1) sobre el último eje,
# que en un arreglo (alto, ancho, canales) corresponde a los canales de
# color. Como PIL/numpy cargan la imagen en orden RGB, invertir ese eje
# la deja en orden BGR (canal azul y rojo intercambiados).
bgr = img[:, :, ::-1]

plt.imshow(bgr)
plt.axis("off")
plt.savefig("../results/punto2_bgr.png", bbox_inches="tight", pad_inches=0)

# Imagen Efecto Espejo

# Índice con paso negativo (::-1) sobre el eje de las columnas (eje 1).
# Recorre las columnas de derecha a izquierda, produciendo un espejo
# horizontal (reflexión sobre un eje vertical imaginario).
espejo = img[:, ::-1, :]

plt.imshow(espejo)
plt.axis("off")
plt.savefig("../results/punto2_espejo.png", bbox_inches="tight", pad_inches=0)

# Imagen Inversión Vertical

# Índice con paso negativo (::-1) sobre el eje de las filas (eje 0).
# Recorre las filas de abajo hacia arriba, invirtiendo la imagen
# verticalmente (reflexión sobre un eje horizontal imaginario).
invertida = img[::-1, :, :]

plt.imshow(invertida)
plt.axis("off")
plt.savefig("../results/punto2_inversion_vertical.png", bbox_inches="tight", pad_inches=0)
