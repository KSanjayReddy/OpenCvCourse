import cv2
import matplotlib.pyplot as plt
import numpy as np

# Let us desaturate a image by changing its saturation

img = cv2.imread("Images/week4/girl.jpg", cv2.IMREAD_COLOR)

#Convert the image to hsv
img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# convert the image to float32 as we are gng to multiply with float numbers
img_hsv = np.float32(img_hsv)

h,s,v = cv2.split(img_hsv)

# saturation scale
saturation_scale  = 1.5

s = s * saturation_scale
s = np.clip(s,0,255)

img_hsv_new = np.uint8(cv2.merge((h,s,v)))
# NOTE : first convert to int then cvtColor
img_bgr = cv2.cvtColor(img_hsv_new, cv2.COLOR_HSV2BGR)


plt.figure(figsize=[20,10])
plt.subplot(121);plt.imshow(img[...,::-1]);plt.title("Image");plt.axis('off')
plt.subplot(122);plt.imshow(img_bgr[:,:,::-1]);plt.title("Desaturated")


plt.show()
