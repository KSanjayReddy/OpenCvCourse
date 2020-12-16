import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rc('image', cmap = 'gray')

# We are going to tune the canny edges using the below 4 parameters
blur = 1  # will keep from 1 to 5 so ksize for gaussian blur will vary from 3 to 11, this is before the canny operation
lowThresh = 50     # The lower threshold for the canny double thresholding operation
highThresh = 100   # The higher threshold for the canny double thresholding operation
apertureIndex  = 0  # To decide what should be size of sobel kernel

apertureList = [3,5,7]


path = "Images/week4/sample.jpg"
img = cv2.imread(path, cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.namedWindow("img", cv2.WINDOW_FULLSCREEN)

def applyCanny():
    if blur > 0:
        blurredImg = cv2.GaussianBlur(img,(2*blur +1,2*blur +1), 0)
    else:
        blurredImg = img.copy()

    new = cv2.Canny(blurredImg,lowThresh, highThresh, apertureSize = apertureList[apertureIndex])
    cv2.imshow("Detected Canny Edges", new)


def updateBlur(value):
    global blur
    blur = value
    applyCanny()
    pass

def updateLowThresh(value):
    global lowThresh
    lowThresh = value
    applyCanny()
    pass

def updateHighThresh(value):
    global highThresh
    highThresh = value
    applyCanny()
    pass

def updateAperture(value):
    print("test")
    global apertureIndex
    apertureIndex = value
    applyCanny()
    pass

#create trackbarks for each parameter
cv2.createTrackbar("blur","img", blur,5, updateBlur)
cv2.createTrackbar("lowThresh","img",lowThresh,255, updateLowThresh)
cv2.createTrackbar("highThresh","img", highThresh,255, updateHighThresh)
cv2.createTrackbar("apertureIndex","img", apertureIndex,2, updateAperture)

applyCanny()

cv2.imshow("img",img)
k = cv2.waitKey(0)
if k== 27:
    cv2.destroyAllWindows
