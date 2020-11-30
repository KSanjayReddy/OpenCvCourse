import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "Images/week2/threshold.png"

img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img,None, fx = 0.7, fy = 0.7, interpolation = cv2.INTER_AREA)
dst = img.copy()

def applyThreshold(thresh, max):
    print("Apply Thresh with thresh {} and max {}".format(thresh, max))
    ret, dst = cv2.threshold(img,thresh,max, cv2.THRESH_BINARY)
    return dst

def nothing(value):
    pass


cv2.namedWindow("img")
cv2.createTrackbar("Thresh", "img", 127, 255, nothing)
cv2.createTrackbar("MaxVal", "img", 255, 255, nothing)

while True:
    cv2.imshow("img", img)
    t = cv2.getTrackbarPos("Thresh", "img")
    m = cv2.getTrackbarPos("MaxVal", "img")
    dst = applyThreshold(t,m)
    cv2.imshow("Result", dst)
    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()
