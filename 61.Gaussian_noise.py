import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rc('image', cmap = 'gray')

path = "Images/week4/sample.jpg"
img = cv2.imread(path, cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gauss = np.zeros_like(img)
gauss = cv2.randn(gauss,50,20) # (array, mean, standard deviation)

new = cv2.add(img, np.uint8(gauss*0.5))

new1 = cv2.GaussianBlur(new,(11,11), 0)

cv2.imshow("img", img)
cv2.imshow("gauss noise", gauss)
cv2.imshow("image with noise", new)
cv2.imshow("Gaussian blur", new1)
cv2.waitKey(0)
cv2.destroyAllWindows()
