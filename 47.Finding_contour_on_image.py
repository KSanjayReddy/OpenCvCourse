import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rc('image', cmap='gray')

path = "Images/week2/blob.jpg"
img = cv2.imread(path, cv2.IMREAD_COLOR)
orig = img.copy()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, img = cv2.threshold(img,150, 255, cv2.THRESH_BINARY_INV)

ksize  = (11,11)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, ksize)
img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations = 1)

ret, imgLabels = cv2.connectedComponents(img)

#print(imgLabels.dtype)

min,max, _,_ = cv2.minMaxLoc(imgLabels)

imgLabels = 255 * (imgLabels - min)/(max - min)
imgLabels = np.uint8(imgLabels)

imgLabels = cv2.applyColorMap(imgLabels, cv2.COLORMAP_JET)

cnts, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("The no. of blobs is : ", len(cnts))
for cnt in cnts:
    M = cv2.moments(cnt)
    x = int(M["m10"]/M["m00"])
    y = int(M["m01"]/M["m00"])

    cv2.circle(orig, (x,y), 2, (0,255,255), thickness=2)
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(orig, (x,y), (x+w,y+h), (0,255,0), thickness = 2)

cv2.imshow("final final",orig)
cv2.waitKey(0)
cv2.destroyAllWindows()
