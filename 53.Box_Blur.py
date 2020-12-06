import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rc('image', cmap = 'gray')

path = "Images/week4/gaussian-noise.png"

img = cv2.imread(path, cv2.IMREAD_COLOR)
new1 = cv2.blur(img, (3,3))
new2 = cv2.blur(img, (5,5))

cv2.imshow("orig", img)
cv2.imshow("blur 3x3", new1)
cv2.imshow("blur 5x5", new2)
cv2.waitKey(0)
cv2.destroyAllWindows()
