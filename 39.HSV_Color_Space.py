import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Images/week4/capsicum.jpg", cv2.IMREAD_COLOR)

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

plt.imshow(img_hsv)    # This printing has no significance
plt.title("HSV Orig")

plt.figure(figsize=(20,15))
plt.subplot(131)
plt.imshow(img_hsv[:,:,0],cmap='gray')
plt.title("Hue");
plt.subplot(132)
plt.imshow(img_hsv[:,:,1],cmap='gray')
plt.title("Saturation");
plt.subplot(133)
plt.imshow(img_hsv[:,:,2],cmap='gray')
plt.title("Value");

plt.show()
