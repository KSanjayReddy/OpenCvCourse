import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rc('image', cmap = 'gray')

path = "Images/week4/truth.png"
#path = "Images/week4/sample.jpg"
img = cv2.imread(path, cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gauss = np.array([1,2,1,2,4,2,1,2,1])
gauss = gauss.reshape(3,3)
print("Gauss : ")
print(gauss)

print("Perwitt :")
perwitt = np.array([-1,0,1,-1,0,1,-1,0,1])
perwitt = perwitt.reshape(3,3)
print(perwitt)

sobel = gauss * perwitt
print("Sobel")
print(sobel)

# Sobel opencv starts here
sobelx = cv2.Sobel(img, cv2.CV_32F, 1, 0)
sobely = cv2.Sobel(img, cv2.CV_32F, 0, 1)

#The sobel X and Y have both positive and negative values,normalize them to 0-1
sobelx = cv2.normalize(sobelx, sobelx, 0, 1, cv2.NORM_MINMAX)
sobely = cv2.normalize(sobely, sobely, 0, 1, cv2.NORM_MINMAX)


cv2.imshow("img", img)
cv2.imshow("sobelX", sobelx)
cv2.imshow("sobelY", sobely)

cv2.waitKey(0)
cv2.destroyAllWindows()
