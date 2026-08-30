# Preparación: imagen generada con IA
#
# Genera una imagen con un generador de IA gratuito (ej. Bing Image Creator).
# **Requisito:** dimensiones 1024x1024x3, no usar imágenes predefinidas de la plataforma.

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

import sys
sys.path.append("..")
from utils import to_uint8, gamma_transform, log_transform, piecewise_linear, gray_level_slicing

# Prompt e imagen usada
#
# "genera una imagen con el personaje que te pasé pero que esté jugando voleibol con otras personas, la imagen tiene que tener dimensiones 1024x1024x3"
#
# ![Cinnamoroll IA](../images/cinnamorroll.png)

img_path = "../images/cinnamorroll.png"
img_original = np.array(Image.open(img_path).convert("RGB"))
print("imagen usada:", img_original.shape, img_original.dtype)

plt.imshow(img_original)
plt.axis("off")

# Redimensionar a 1024x1024x3
#
# La imagen ya es cuadrada, así que el resize no la distorsiona.

# El enunciado pide 1024x1024x3 -> como ya es cuadrada, un resize no la distorsiona
img = np.array(Image.fromarray(img_original).resize((1024, 1024)))
print("final:", img.shape, img.dtype)

# Guarda la versión final para que los demás notebooks la usen directamente
Image.fromarray(img).save("../images/cinnamorroll_1024.png")

plt.imshow(img)
plt.axis("off")
