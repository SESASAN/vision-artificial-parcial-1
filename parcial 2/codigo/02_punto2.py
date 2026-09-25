import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

import sys
sys.path.append("..")

ref = np.array(Image.open("../images/Referencia.tif").convert("L"))
plt.imshow(ref, cmap="gray")
plt.axis("off")

# TODO: calcular y graficar el histograma de ref

# TODO: cargar gray (imagen original en escala de grises, ver Punto 1)
# TODO: aplicar especificación de histograma usando ref como objetivo
gray_spec = None

# TODO: calcular y graficar el histograma de gray_spec
