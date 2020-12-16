import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rc('image', cmap = 'gray')

#path = "Images/week4/truth.png"
path = "Images/week4/sample.jpg"

img = cv2.imread(path, cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# All the derivate operations are very much sensitive to noise
# small noise in input is largely scaled in the output so smooth it first
new = cv2.GaussianBlur(img,(5,5), 0, 0)

#Laplacian
new = cv2.Laplacian(new, cv2.CV_32F)


new = cv2.normalize(new, new, 0, 1, cv2.NORM_MINMAX)


cv2.imshow("img", img)
cv2.imshow("new", new)
cv2.waitKey(0)
cv2.destroyAllWindows()
