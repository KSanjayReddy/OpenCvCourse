import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rc("image", cmap = "gray")

path = "Images/week4/girl.jpg"
img = cv2.imread(path, cv2.IMREAD_COLOR)
img = cv2.resize(img, None, fx = 0.7,fy = 0.7, interpolation = cv2.INTER_AREA)
orig = img.copy()

#Pivot points on X coordinates
orig_values = np.array([0,50,100,150,200,255])
#Changes points on Y-axis for each channel
rCurve = np.array([0,80,150,190,220,255])
bCurve = np.array([0,20,40,75,150, 255])

# Create Look Up Tables
fullRange = np.arange(0,256)
rLUT = np.interp(fullRange, orig_values, rCurve)
bLUT = np.interp(fullRange, orig_values, bCurve)

#Apply Lookup table to image channels using LUT
img[:,:,0] = cv2.LUT(img[:,:,0], bLUT)  # for Blue Channel
img[:,:,2] = cv2.LUT(img[:,:,2], rLUT)  # for Red Channel

# cool thing to join images into one
combined = np.hstack([orig, img])


plt.plot(fullRange, rLUT, color = 'r')
plt.plot(fullRange, fullRange, color = 'black')
plt.plot(fullRange, bLUT, color = 'b')
plt.show()

cv2.imshow("Warming Filter", combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
