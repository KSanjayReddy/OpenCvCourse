import cv2
import numpy as np

colorPath = "Images/week1/boy.jpg"

img = cv2.imread(colorPath, cv2.IMREAD_COLOR)
org = img.copy()
# Lets try to increase the contrast by 30%
img = np.float32(img)
img = img / 255.0

img = img * 1.3

img = np.clip(img,0,1)

cv2.imshow("original", org)
cv2.imshow("output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
