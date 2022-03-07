import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from skimage.util import random_noise
from skimage import data, feature, filters

image = data.camera()
image2 = data.camera()
image3 = data.camera()

mask1=[[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]]

image = ndi.gaussian_filter(image, 4)
image = random_noise(image, mode='speckle', mean=0.1)
image2 = filters.sato(image2)
image3 = filters.prewitt(image3)

edges1 = feature.canny(image)
edges2 = feature.canny(image, sigma=3)

fig, ax = plt.subplots(nrows=1, ncols=5, figsize=(15, 3))

ax[0].imshow(image, cmap='gray')
ax[0].set_title('noisy image', fontsize=20)

ax[1].imshow(image2, cmap='gray')
ax[1].set_title('Sato', fontsize=20)

ax[2].imshow(image3, cmap='gray')
ax[2].set_title('Prewitt', fontsize=20)

ax[3].imshow(edges1, cmap='gray')
ax[3].set_title(r'Canny filter, $\sigma=1$', fontsize=20)

ax[4].imshow(edges2, cmap='gray')
ax[4].set_title(r'Canny filter, $\sigma=3$', fontsize=20)

for a in ax:
    a.axis('off')

fig.tight_layout()
plt.show()
