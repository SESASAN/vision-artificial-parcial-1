import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

img = np.array(Image.open("../images/cinnamorroll_1024.png").convert("RGB"))
gray = np.array(Image.fromarray(img).convert("L"))

plt.imshow(gray, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto3_gris.png", bbox_inches="tight", pad_inches=0)

gamma_03 = np.zeros_like(gray)
cv2.intensity_transform.gammaCorrection(gray, gamma_03, 0.3)

plt.imshow(gamma_03, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto3_gamma_0.3.png", bbox_inches="tight", pad_inches=0)

gamma_23 = np.zeros_like(gray)
cv2.intensity_transform.gammaCorrection(gray, gamma_23, 2.3)

plt.imshow(gamma_23, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto3_gamma_2.3.png", bbox_inches="tight", pad_inches=0)

log_img = np.zeros_like(gray)
cv2.intensity_transform.logTransform(gray, log_img)

plt.imshow(log_img, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto3_log.png", bbox_inches="tight", pad_inches=0)
