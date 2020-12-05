import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rc("image", cmap = "gray")

path = "Images/week4/night-sky.jpg"
img = cv2.imread(path, cv2.IMREAD_COLOR)

imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

new1 = imghsv.copy()
new2 = imghsv.copy()

new1[:,:,2] = cv2.equalizeHist(imghsv[:,:,2])

#CLAHE USAGE
clahe = cv2.createCLAHE(clipLimit = 2.0, tileGridSize = (8,8))
new2[:,:,2] = clahe.apply(imghsv[:,:,2])

# Store the v channels to plot histogram
v = imghsv[:,:,2]
v1 = new1[:,:,2]
v2 = new2[:,:,2]

new1 = cv2.cvtColor(new1, cv2.COLOR_HSV2BGR)
new2 = cv2.cvtColor(new2, cv2.COLOR_HSV2BGR)

plt.subplot(2,3,1);plt.imshow(img[:,:,::-1]);plt.title("Original")
plt.subplot(2,3,2);plt.imshow(new1[:,:,::-1]);plt.title("Hist Equa")
plt.subplot(2,3,3);plt.imshow(new2[:,:,::-1]);plt.title("CLAHE")

plt.subplot(2,3,4);plt.hist(v.flatten(), bins=256);plt.title("Original")
plt.subplot(2,3,5);plt.hist(v1.flatten(), bins=256);plt.title("Hist Equa")
plt.subplot(2,3,6);plt.hist(v2.flatten(), bins = 256);plt.title("CLAHE")

plt.show()

'''
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
