import cv2
import matplotlib.pyplot as plt

# Let us find the dominant color in an image using histograms

img = cv2.imread("Images/week4/jersey.jpg", cv2.IMREAD_COLOR)

#Convert the image to hsv so that we can use the hue values for color detection
img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(img_hsv)

print(h)
print(h.shape)

#The background pixels are white and we are not interested in them
# So lets remove them by chosing only pixels whose saturation is greater then 10.
h_new = h[s>10]
h_new = h_new.flatten()
print(h_new)

plt.figure(figsize=[20,10])
plt.subplot(121);plt.imshow(img[...,::-1]);plt.title("Image");plt.axis('off')
plt.subplot(122);plt.hist(h_new, bins=10, color='b');plt.title("Histogram")


plt.show()
