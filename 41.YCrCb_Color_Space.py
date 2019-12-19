import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Images/week4/capsicum.jpg", cv2.IMREAD_COLOR)

img_ycb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

plt.imshow(img_ycb)    # This printing has no significance
plt.title("YCrCb Orig")

plt.figure(figsize=(20,15))
plt.subplot(131)
plt.imshow(img_ycb[:,:,0],cmap='gray')
plt.title("Y");
plt.subplot(132)
plt.imshow(img_ycb[:,:,1],cmap='gray')
plt.title("Cr");
plt.subplot(133)
plt.imshow(img_ycb[:,:,2],cmap='gray')
plt.title("Cb");

plt.show()
