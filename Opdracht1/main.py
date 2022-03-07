import skimage.color
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.colors as cl

image = plt.imread("image.jpg")

imageArray = np.array(image)

def toHSV(arrayToSet):
    return cl.rgb_to_hsv(arrayToSet)

def changeColor(array, color, colorRangeLower, colorRangeUpper):
    for y in range(array.shape[0]):
        for x in range(array.shape[1]):
            for i in range(array.shape[2]):
                if array[y, x, i] < color[i] - colorRangeLower or array[y, x, i] > color[i] + colorRangeUpper:
                    array[y, x] = [(int(array[y, x][0]) + int(array[y, x][0]) + int(array[y, x][0])) / 3, (int(array[y, x][0]) + int(array[y, x][0]) + int(array[y, x][0])) / 3, (int(array[y, x][0]) + int(array[y, x][0]) + int(array[y, x][0])) / 3]
                    break
    return array

brick = (220,55,45)
grass = (9,95,8)
colors = []

def getHUE(array, colors):
    for y in range(array.shape[0]):
        for x in range(array.shape[1]):
            colors.append(array[y, x, 0]*360)
    return colors


plt.figure(1)
plt.plot(imgplot = plt.imshow(changeColor(imageArray.copy(), brick, 170, 25)))
plt.figure(2)
plt.plot(imgplot = plt.imshow(changeColor(imageArray.copy(), grass, 80, 25)))
plt.figure(3)
plt.hist((getHUE(toHSV(imageArray.copy()),colors)), 64)
plt.figure(4)
plt.hist(getHUE(toHSV(changeColor(imageArray.copy(), brick, 170, 25)),colors), 64)
plt.show()
