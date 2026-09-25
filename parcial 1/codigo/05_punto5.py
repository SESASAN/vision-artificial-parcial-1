import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

img = np.array(Image.open("../images/cinnamorroll_1024.png").convert("RGB"))
gray = np.array(Image.fromarray(img).convert("L"))

plt.imshow(gray, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto5_gris.png", bbox_inches="tight", pad_inches=0)

slicing_1 = cv2.inRange(gray, 30, 75)

plt.imshow(slicing_1, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto5_slicing_1.png", bbox_inches="tight", pad_inches=0)

slicing_2 = cv2.inRange(gray, 130, 160)

plt.imshow(slicing_2, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto5_slicing_2.png", bbox_inches="tight", pad_inches=0)

slicing_3 = cv2.inRange(gray, 200, 230)

plt.imshow(slicing_3, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto5_slicing_3.png", bbox_inches="tight", pad_inches=0)
