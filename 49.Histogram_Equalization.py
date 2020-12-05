import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rc('image', cmap = 'gray')


path = "Images/week4/dark-flowers.jpg"
img = cv2.imread(path, cv2.IMREAD_COLOR)

# Below if for gray scale images contrast enhancement
'''
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
new = cv2.equalizeHist(gray)


plt.subplot(1,2,1);plt.imshow(gray)
plt.subplot(1,2,2);plt.hist(gray.flatten(),256, [0,256])
plt.show()

plt.subplot(1,2,1);plt.imshow(new)
plt.subplot(1,2,2);plt.hist(new.flatten(),256, [0,256])
plt.show()
'''

# Below isfor color images, only equalizeHist the intensity channel like v in hsv
hsv  = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsv[:,:,2] = cv2.equalizeHist(hsv[:,:,2])
new = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imshow("Orig",img)
cv2.imshow("Equalized",new)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.subplot(1,2,1);plt.imshow(img[:,:,2])
plt.subplot(1,2,2);plt.hist(img[:,:,2].flatten(),256, [0,256])
plt.show()

plt.subplot(1,2,1);plt.imshow(new[:,:,2])
plt.subplot(1,2,2);plt.hist(new[:,:,2].flatten(),256, [0,256])
plt.show()
