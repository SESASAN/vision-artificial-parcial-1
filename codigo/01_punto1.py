# Punto 1 (0.5) — Recorte por indexación
#
# Usa indexación de matrices para recortar tu imagen para los rangos:
# - Filas: 300-659
# - Columnas: 200-839
# - Todos los componentes RGB

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

# Recorte
#
# Realiza el recorte y muestra/guarda la imagen resultante (sin títulos de figura).

# Usa la versión ya redimensionada a 1024x1024 (ver 00_preparacion.ipynb)
img = np.array(Image.open("../images/cinnamorroll_1024.png").convert("RGB"))
print("original:", img.shape)

# Recorte por indexación de matrices: img[filas, columnas, canales].
# El slice 300:660 toma las filas 300 a 659 (660 no incluido), y
# 200:840 toma las columnas 200 a 839. El ":" final conserva los 3
# canales RGB sin modificarlos.
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

# La relación de aspecto es la proporción ancho/alto de la imagen.
# im.shape para un arreglo numpy es (alto, ancho, canales), por eso
# se usa shape[1] (ancho) dividido entre shape[0] (alto).
def relacion_aspecto(im):
    h, w = im.shape[:2]
    return w / h

print(f"Original: {img.shape[1]}x{img.shape[0]} -> {relacion_aspecto(img):.4f}")
print(f"Recortada: {cropped.shape[1]}x{cropped.shape[0]} -> {relacion_aspecto(cropped):.4f}")
