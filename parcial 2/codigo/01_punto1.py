import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

import sys
sys.path.append("..")

# TODO: cargar tu imagen (ver 00_preparacion.ipynb) y convertir a escala de grises
img = None  # np.array(Image.open("../images/mi_imagen.png").convert("RGB"))
gray = None  # np.array(Image.fromarray(img).convert("L"))

# TODO: calcular y graficar el histograma de gray
hist = None

# TODO: ecualizar gray
gray_eq = None

# TODO: calcular y graficar el histograma de gray_eq
hist_eq = None

# TODO: encontrar el nivel con mayor frecuencia en hist y su probabilidad

# TODO: encontrar el nivel con mayor frecuencia en hist_eq y su probabilidad

# TODO: calcular la probabilidad del nivel 176 en hist_eq
