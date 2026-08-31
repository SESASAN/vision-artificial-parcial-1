# Punto 3 (0.9) — Transformaciones de intensidad: gamma y logarítmica
#
# Nota: usa como entrada la imagen original en escala de grises. Asegúrate que las imágenes resultantes están en uint8 (rango 0-255).

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
# convert("L"): modo "L" de PIL = escala de grises de 8 bits (0-255).
gray = np.array(Image.fromarray(img).convert("L"))

plt.imshow(gray, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto3_gris.png", bbox_inches="tight", pad_inches=0)

# Transformación Gamma (γ=0.3)

# cv2.intensity_transform.gammaCorrection(input, output, gamma) aplica
# s = c*r^gamma. No devuelve el resultado: lo escribe dentro de "output",
# por eso primero se crea un arreglo vacío del mismo tamaño (np.zeros_like)
# para que la función lo llene.
# gamma=0.3 (<1): aclara la imagen, expande los tonos oscuros.
gamma_03 = np.zeros_like(gray)
cv2.intensity_transform.gammaCorrection(gray, gamma_03, 0.3)

plt.imshow(gamma_03, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto3_gamma_0.3.png", bbox_inches="tight", pad_inches=0)

# Transformación Gamma (γ=2.3)

# gamma=2.3 (>1): oscurece la imagen, expande los tonos claros.
gamma_23 = np.zeros_like(gray)
cv2.intensity_transform.gammaCorrection(gray, gamma_23, 2.3)

plt.imshow(gamma_23, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto3_gamma_2.3.png", bbox_inches="tight", pad_inches=0)

# Transformación Logarítmica

# cv2.intensity_transform.logTransform(input, output) aplica
# s = c*log(1+r). A diferencia de gamma no tiene parámetro ajustable:
# siempre aclara, y más fuerte en los tonos oscuros que en los claros.
log_img = np.zeros_like(gray)
cv2.intensity_transform.logTransform(gray, log_img)

plt.imshow(log_img, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto3_log.png", bbox_inches="tight", pad_inches=0)
