import os
import cvzone
from cvzone.ClassificationModule import Classifier
import cv2

# 0 : webcam, 1 : webcam/Phone, 2 : Phone
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(1)
# cap = cv2.VideoCapture(2)

classifier = Classifier('C:/TrashClassifier/Resources/Model/keras_model.h5', 'C:/TrashClassifier/Resources/Model/labels.txt')
imgArrow = cv2.imread('C:/TrashClassifier/Resources/arrow.png', cv2.IMREAD_UNCHANGED)
classBinID = 0

# Importing Waste Images
imgWasteList = []
pathFolderWaste = "C:/TrashClassifier/Resources/Waste"
pathList = os.listdir(pathFolderWaste)
print(pathList)

for path in pathList:
    imgWasteList.append(cv2.imread(os.path.join(pathFolderWaste, path), cv2.IMREAD_UNCHANGED))

# Importing Bin Images
imgBinList = []
pathFolderBin = "C:/TrashClassifier/Resources/Bins"
pathList = os.listdir(pathFolderBin)
print(pathList)

for path in pathList:
    imgBinList.append(cv2.imread(os.path.join(pathFolderBin, path), cv2.IMREAD_UNCHANGED))

# 0 - Plastic
# 1 - Metal
classDic = {0:None,
            1:0,
            2:1}



while True:
    _, img = cap.read()
    # imgResize = cv2.resize(img, (454, 340))
    imgResize = cv2.resize(img, (400, 260))

    imgBackground = cv2.imread('C:/TrashClassifier/Resources/WhiteBackground.png')

    predection = classifier.getPrediction(img)
    print(predection)
    classID = predection[1]

    if classID != 0:
        imgBackground = cvzone.overlayPNG(imgBackground, imgWasteList[classID-1], (575, 60))
        imgBackground = cvzone.overlayPNG(imgBackground, imgArrow, (640, 280))

        classBinID = classDic[classID]
        imgBackground = cvzone.overlayPNG(imgBackground, imgBinList[classBinID], (558, 340))

    imgBackground[30:30 + 260, 30:30 + 400] = imgResize

    # Displays
    # cv2.imshow("Image", img)
    cv2.imshow("Output", imgBackground)
    cv2.waitKey(1)
