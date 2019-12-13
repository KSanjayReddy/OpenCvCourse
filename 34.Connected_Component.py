import cv2
import numpy as np
# First Computer Vision Program, CCA - Connected Comp Analysis

img = cv2.imread("Images/week3/truth.png",cv2.IMREAD_GRAYSCALE)
#Threshold to get a binary image
ret, imgThresh = cv2.threshold(img,150,255,cv2.THRESH_BINARY)

#Find Connected Components
ret, imgLabels = cv2.connectedComponents(imgThresh)   #imgLabels will have blobs labelled starting from 1
imgLabels = np.uint8(imgLabels)  # Required if we need to display the image

#Display each Label
no_of_comp = imgLabels.max()
print(no_of_comp)

for i in range(no_of_comp+1):
    tmp = imgLabels==i
    tmp = np.float32(tmp)
    print(tmp.dtype)
    cv2.imshow("Each Label", tmp)
    cv2.waitKey(0)



cv2.imshow("Original",img)
imgLabels = imgLabels * 50      # Not needed if we use matplotlib, as it will take min max value automatically
cv2.imshow("Labelled",imgLabels)
cv2.waitKey(0)
cv2.destroyAllWindows()
