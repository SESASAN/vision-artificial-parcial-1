# Preparación: imagen generada con IA
#
# Genera una imagen con un generador de IA gratuito (ej. Bing Image Creator).
# **Requisito:** dimensiones 1024x1024x3, no usar imágenes predefinidas de la plataforma.

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

# Prompt e imagen usada
#
# "genera una imagen con el personaje que te pasé pero que esté jugando voleibol con otras personas, la imagen tiene que tener dimensiones 1024x1024x3"
#
# ![Cinnamoroll IA](../images/cinnamorroll.png)

# Image.open + convert("RGB"): abre el archivo y fuerza 3 canales de color.
# np.array(...): convierte la imagen de PIL a un arreglo numpy (alto, ancho, canales).
img_path = "../images/cinnamorroll.png"
img_original = np.array(Image.open(img_path).convert("RGB"))
print("imagen usada:", img_original.shape, img_original.dtype)

plt.imshow(img_original)
plt.axis("off")

# Redimensionar a 1024x1024x3
#
# La imagen ya es cuadrada, así que el resize no la distorsiona.

# El enunciado pide 1024x1024x3. Como la imagen ya es cuadrada (1254x1254),
# un resize no la deforma. Image.fromarray().resize() usa PIL (no cv2) para
# el remuestreo de la imagen.
img = np.array(Image.fromarray(img_original).resize((1024, 1024)))
print("final:", img.shape, img.dtype)

# Se guarda en disco para que el resto de notebooks del taller la carguen
# ya lista, sin repetir el resize.
Image.fromarray(img).save("../images/cinnamorroll_1024.png")

plt.imshow(img)
plt.axis("off")
