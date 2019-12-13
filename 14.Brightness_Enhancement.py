import cv2
import numpy as np

colorPath = "Images/week1/boy.jpg"

img = cv2.imread(colorPath, cv2.IMREAD_COLOR)
brightness = 50
print(img.shape)

#use either of the below, both should be of same size
img1 = np.ones((360,480,3), dtype='uint8') * brightness
#img1 = np.ones_like(img) * brightness

output  = cv2.add(img, img1)  # It will just add and clip the values which are out of range

cv2.imshow("orig", img)
cv2.imshow("output", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
