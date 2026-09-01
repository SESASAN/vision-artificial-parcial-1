import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img_path = "../images/cinnamorroll.png"
img_original = np.array(Image.open(img_path).convert("RGB"))
print("imagen usada:", img_original.shape, img_original.dtype)

plt.imshow(img_original)
plt.axis("off")

img = np.array(Image.fromarray(img_original).resize((1024, 1024)))
print("final:", img.shape, img.dtype)

Image.fromarray(img).save("../images/cinnamorroll_1024.png")

plt.imshow(img)
plt.axis("off")
