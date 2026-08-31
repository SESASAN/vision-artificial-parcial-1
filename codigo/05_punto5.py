# Punto 5 (0.5) — Fraccionamiento de gris (gray-level slicing)
#
# Transformación que realza los píxeles en el rango [A,B] llevándolos a 255, y los demás a 0. Usa como entrada la imagen original en escala de grises. Asegúrate que las imágenes resultantes están en uint8 (rango 0-255).

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

# Imagen Original en Escala de Grises

img = np.array(Image.open("../images/cinnamorroll_1024.png").convert("RGB"))
gray = np.array(Image.fromarray(img).convert("L"))

plt.imshow(gray, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto5_gris.png", bbox_inches="tight", pad_inches=0)

# T. Fraccionamiento de Gris — A=30 B=75

# cv2.inRange(imagen, limite_inferior, limite_superior) revisa cada
# pixel: si está dentro del rango [A,B] devuelve 255 (blanco), si no
# devuelve 0 (negro). Es una función genérica de OpenCV (no pensada
# solo para esto), pero hace exactamente el fraccionamiento de gris.
# A=30,B=75: aísla las sombras más oscuras.
slicing_1 = cv2.inRange(gray, 30, 75)

plt.imshow(slicing_1, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto5_slicing_1.png", bbox_inches="tight", pad_inches=0)

# T. Fraccionamiento de Gris — A=130 B=160

# A=130,B=160: tonos medios, aísla el contorno y sombreado del peluche.
slicing_2 = cv2.inRange(gray, 130, 160)

plt.imshow(slicing_2, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto5_slicing_2.png", bbox_inches="tight", pad_inches=0)

# T. Fraccionamiento de Gris — A=200 B=230

# A=200,B=230: tonos claros, aísla el pelaje blanco y la luz de ventana.
slicing_3 = cv2.inRange(gray, 200, 230)

plt.imshow(slicing_3, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto5_slicing_3.png", bbox_inches="tight", pad_inches=0)
