import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

import sys
sys.path.append("..")

sobel_h = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
sobel_v = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
laplaciano_8 = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])

# TODO: cargar gray (imagen original en escala de grises, ver Punto 1)
gray = None

# TODO: aplicar sobel_h y sobel_v por convolución sobre gray
# TODO: magnitud del gradiente = |Gx| + |Gy|
sobel_magnitud = None

# TODO: aplicar laplaciano_8 por convolución sobre gray
laplaciano_resultado = None
