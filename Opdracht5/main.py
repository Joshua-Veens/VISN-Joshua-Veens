import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn import svm
import random

digits = datasets.load_digits()
trainingData = []
trainingTarget = []

testImages = []
testData = []
testTarget = []

def sortData():
    for digit in range(len(digits.data)):
        randNr = random.randint(1,3)
        if randNr > 2:
            testData.append(digits.data[digit])
            testTarget.append(digits.target[digit])
            testImages.append(digits.images[digit])
        if randNr <= 2:
            trainingData.append(digits.data[digit])
            trainingTarget.append(digits.target[digit])

sortData()

print(len(trainingData))
print(len(testData))

clf = svm.SVC(gamma=0.001, C=100)
X,y = trainingData, trainingTarget
clf.fit(X,y)

print(clf.predict(testData[-4:-3]))
plt.imshow(testImages[-4], cmap=plt.cm.gray_r, interpolation='nearest')
ConfusionMatrixDisplay.from_predictions(testTarget, clf.predict(testData))

plt.show()
