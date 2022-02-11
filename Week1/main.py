import skimage.color
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image = plt.imread("image.jpg")

imageArray = np.array(image)
color = [90,120,90]

def changeColor(imageArray, color):
    for x in range(imageArray.shape[0]):
        for y in range(imageArray.shape[1]):
            if imageArray[x, y][0] > color[0] and imageArray[x, y][1] < color[1] and imageArray[x, y][2] < color[2]:
                continue
            else:
                imageArray[x, y] = [imageArray[x, y][0] / 3, imageArray[x, y][0] / 3, imageArray[x, y][0] / 3]

changeColor(imageArray, color)

imgplot = plt.imshow(imageArray)
plt.show()