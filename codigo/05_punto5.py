# Punto 5 (0.5) — Fraccionamiento de gris (gray-level slicing)
#
# Transformación que realza los píxeles en el rango [A,B] llevándolos a 255, y los demás a 0. Usa como entrada la imagen original en escala de grises. Asegúrate que las imágenes resultantes están en uint8 (rango 0-255).

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

# Imagen Original en Escala de Grises

img = np.array(Image.open("../images/cinnamorroll_1024.png").convert("RGB"))
gray = np.array(Image.fromarray(img).convert("L"))

plt.imshow(gray, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto5_gris.png", bbox_inches="tight", pad_inches=0)

# T. Fraccionamiento de Gris — A=30 B=75

# gray_level_slicing (utils.py) usa una máscara booleana de numpy
# ((gray >= A) & (gray <= B)) para poner en 255 los pixeles dentro
# del rango [A,B] y en 0 el resto. A=30,B=75 aísla las sombras más
# oscuras (texto del pizarrón, hueco del rollo de canela).
slicing_1 = gray_level_slicing(gray, A=30, B=75)

plt.imshow(slicing_1, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto5_slicing_1.png", bbox_inches="tight", pad_inches=0)

# T. Fraccionamiento de Gris — A=130 B=160

# A=130,B=160: tonos medios, aísla el contorno y sombreado del
# propio peluche.
slicing_2 = gray_level_slicing(gray, A=130, B=160)

plt.imshow(slicing_2, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto5_slicing_2.png", bbox_inches="tight", pad_inches=0)

# T. Fraccionamiento de Gris — A=200 B=230

# A=200,B=230: tonos claros, aísla el pelaje blanco y la luz de la
# ventana.
slicing_3 = gray_level_slicing(gray, A=200, B=230)

plt.imshow(slicing_3, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto5_slicing_3.png", bbox_inches="tight", pad_inches=0)
