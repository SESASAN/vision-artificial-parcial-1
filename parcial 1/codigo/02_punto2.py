import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = np.array(Image.open("../images/cinnamorroll_1024.png").convert("RGB"))
print(img.shape)

plt.imshow(img)
plt.axis("off")

bgr = img[:, :, ::-1]

plt.imshow(bgr)
plt.axis("off")
plt.savefig("../results/punto2_bgr.png", bbox_inches="tight", pad_inches=0)

espejo = img[:, ::-1, :]

plt.imshow(espejo)
plt.axis("off")
plt.savefig("../results/punto2_espejo.png", bbox_inches="tight", pad_inches=0)

invertida = img[::-1, :, :]

plt.imshow(invertida)
plt.axis("off")
plt.savefig("../results/punto2_inversion_vertical.png", bbox_inches="tight", pad_inches=0)
