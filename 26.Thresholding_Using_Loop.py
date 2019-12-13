import cv2, time
import numpy as np
img = cv2.imread("Images/week3/threshold.png", cv2.IMREAD_GRAYSCALE)
img = cv2.resize( img, None, fx = 0.7, fy=0.7, interpolation = cv2.INTER_CUBIC)
# Values
thresh = 100
maxValue = 255
#using for loops8
def threshUsingLoop(src,thresh,maxValue):
    dst = src.copy()
    rows,cols = img.shape[:2]
    for i in range(rows):
        for j in range(cols):
            if src[i,j] > thresh:
                dst[i,j] = 0
            else:
                dst[i,j] = src[i,j]
    return dst

def thresholdUsingVectors(src, thresh, maxValue):
    # Create a black output image ( all zeros )
    dst = np.zeros_like(src)
    # Find pixels which have values>threshold value
    thresholdedPixels = src>thresh
    # Assign those pixels maxValue
    dst[thresholdedPixels] = maxValue
    return dst

cv2.imshow("Original",img)
t = time.time()
#new = threshUsingLoop(img,127,255)        # Takes 0.7 seconds
new = thresholdUsingVectors(img,127,255)   # Takes 0.002 seconds
print(time.time() - t)
cv2.imshow("Inverse Threshold to Zero", new)
cv2.waitKey(0)
cv2.destroyAllWindows()
