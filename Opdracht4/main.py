import numpy as np
import matplotlib.pyplot as plt
from skimage import data, transform

image = data.astronaut()

rotate = transform.AffineTransform(rotation=69)
translate = transform.AffineTransform(translation=100)
stretched = transform.AffineTransform(shear=13)

rotate = transform.warp(image, rotate)
translate = transform.warp(image, translate)
stretched = transform.warp(image, stretched)

fig, ax = plt.subplots(nrows=1, ncols=4, figsize=(15, 3))

ax[0].imshow(image, cmap='gray')
ax[0].set_title('Original', fontsize=20)

ax[1].imshow(rotate, cmap='gray')
ax[1].set_title('Rotated', fontsize=20)

ax[2].imshow(translate, cmap='gray')
ax[2].set_title('Translation', fontsize=20)

ax[3].imshow(stretched, cmap='gray')
ax[3].set_title('Stretched', fontsize=20)

for a in ax:
    a.axis('off')

fig.tight_layout()
plt.show()