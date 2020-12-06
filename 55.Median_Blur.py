import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rc('image', cmap = 'gray')

path = "Images/week4/salt-and-pepper.png"
img = cv2.imread(path, cv2.IMREAD_COLOR)
img = cv2.resize(img, None, fx = 0.8, fy = 0.8, interpolation = cv2.INTER_AREA)

new1 = cv2.GaussianBlur(img, (5,7), 0,0)

#Median Blur img and a single int for ksize
# Perfect for salt and pepper noise
new2 = cv2.medianBlur(img,5)

out = np.hstack((img,new1, new2))

cv2.imshow("orig", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
