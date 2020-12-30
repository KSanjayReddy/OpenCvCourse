import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rc('image', cmap = 'gray')

path = "Images/week4/sample.jpg"
img = cv2.imread(path, cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

uniform = np.zeros_like(img)
uniform = cv2.randu(uniform,0,255) # (array, min, max)

ret, salt = cv2.threshold(uniform, 240, 255, cv2.THRESH_BINARY)
#randn => random normal distribution, randu => random uniform distribution

new = cv2.add(img, salt)
new1 = cv2.medianBlur(new,3)

cv2.imshow("img", img)
cv2.imshow("uniform noise", uniform)
cv2.imshow("salt", salt)
cv2.imshow("img with salt noise", new)
cv2.imshow("median filter", new1)
cv2.waitKey(0)
cv2.destroyAllWindows()
