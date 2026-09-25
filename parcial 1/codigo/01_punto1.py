import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = np.array(Image.open("../images/cinnamorroll_1024.png").convert("RGB"))
print("original:", img.shape)
cropped = img[300:660, 200:840, :]
print("recortada:", cropped.shape)

plt.imshow(cropped)
plt.axis("off")
plt.savefig("../results/punto1_recorte.png", bbox_inches="tight", pad_inches=0)

def relacion_aspecto(im):
    h, w = im.shape[:2]
    return w / h

print(f"Original: {img.shape[1]}x{img.shape[0]} -> {relacion_aspecto(img):.4f}")
print(f"Recortada: {cropped.shape[1]}x{cropped.shape[0]} -> {relacion_aspecto(cropped):.4f}")
