import cv2
import numpy as np

img = cv2.imread("Images/week3/truth.png",cv2.IMREAD_GRAYSCALE)
ret, imgThresh = cv2.threshold(img,150,255,cv2.THRESH_BINARY)

#Find Connected Components
ret, imgLabels = cv2.connectedComponents(imgThresh)   #imgLabels will have blobs labelled starting from 1

(min,max, minLoc, maxLoc) = cv2.minMaxLoc(imgLabels)
print(min,max, minLoc, maxLoc)

# Normalize the image so that the min value is 0 and max value is 255.
imgLabels = 255 * (imgLabels - min)/(max-min)
imgLabels = np.uint8(imgLabels)

result = cv2.applyColorMap(imgLabels, cv2.COLORMAP_JET)

cv2.imshow("Original",img)
cv2.imshow("Result Gray",imgLabels)
cv2.imshow("Result",result)
cv2.waitKey(0)
cv2.destroyAllWindows()
