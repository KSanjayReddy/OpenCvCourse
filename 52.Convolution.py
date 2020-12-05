import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rc('image', cmap = 'gray')

path = "Images/week4/sample.jpg"
img = cv2.imread(path, cv2.IMREAD_COLOR)

# Create the convolution kernel
ksize = 5
kernel = np.ones((ksize,ksize), dtype= np.float32)/(ksize**2)

new = cv2.filter2D(img, -1, kernel)

cv2.imshow("img", img)
cv2.imshow("convoluted", new)
cv2.waitKey(0)
cv2.destroyAllWindows()
