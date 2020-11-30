import cv2
import numpy as np

colorPath = "Images/week1/boy.jpg"

img = cv2.imread(colorPath,cv2.IMREAD_COLOR)         #360,480,3
mask = np.zeros_like(img)
mask[100:200, 150:250] = 255

red_mask = cv2.inRange(img, (0,0,150), (100,100,255))
#pixels in range will become 255 and others will be 0

cv2.imshow("Original", img)
cv2.imshow("red mask", red_mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
