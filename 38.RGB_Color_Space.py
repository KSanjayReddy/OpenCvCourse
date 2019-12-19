import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Images/week4/capsicum.jpg", cv2.IMREAD_COLOR)

plt.imshow(img[:,:,::-1])
plt.title("RGB Image, Stored in BGR format")

plt.figure(figsize=(20,15))
plt.subplot(131)
plt.imshow(img[:,:,0],cmap='gray')
plt.title("Blue Channel");
plt.subplot(132)
plt.imshow(img[:,:,1],cmap='gray')
plt.title("Green Channel");
plt.subplot(133)
plt.imshow(img[:,:,2],cmap='gray')
plt.title("Red Channel");

plt.show()
