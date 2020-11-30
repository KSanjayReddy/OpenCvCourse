import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rc('image', cmap = 'gray')

path = "Images/week2/CoinsA.png"
img = cv2.imread(path, cv2.IMREAD_COLOR)
img = cv2.resize(img, None, fx = 0.8, fy = 0.8, interpolation = cv2.INTER_AREA)
new = img.copy()
g1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
b,g,r = cv2.split(img)

'''
plt.subplot(2,2,1)
plt.imshow(g1)
plt.subplot(2,2,2)
plt.imshow(b)
plt.subplot(2,2,3)
plt.imshow(g)
plt.subplot(2,2,4)
plt.imshow(r)
plt.show()
'''
gray = g

'''
tmp = g.copy()
def threshold(value):
    global gray
    ret, gray = cv2.threshold(tmp,int(value), 255, cv2.THRESH_BINARY)
    cv2.imshow("img", gray)

cv2.namedWindow("img", cv2.WINDOW_NORMAL)
cv2.createTrackbar("thresh", "img", 127, 255, threshold)
'''

thresh = 68
ret, gray = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)

k3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
k5 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
k7 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))
k9 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9,9))
k11 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11,11))

#The below is obtained only from experimentation
gray = cv2.dilate(gray,k3, iterations = 2)
gray = cv2.morphologyEx(gray, cv2.MORPH_OPEN, k3, iterations = 3)
gray = cv2.erode(gray,k3, iterations = 1)


params = cv2.SimpleBlobDetector_Params()

params.blobColor = 255

#params.minDistBetweenBlobs = 2

# Filter by Area.
params.filterByArea = False

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.8

# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.8

# Filter by Inertia
params.filterByInertia =True
params.minInertiaRatio = 0.8

obj = cv2.SimpleBlobDetector_create(params)
keyPts = obj.detect(gray)

for k in keyPts:
    x,y = k.pt
    x = int(x)
    y = int(y)
    r = int(k.size/2)
    cv2.circle(img, (x,y), r, (0,255,0), thickness = 2, lineType= cv2.LINE_AA)

print("No. of blobs using simpleBlobDetector is : ", len(keyPts))

#Use CCA
ret, imgLabels = cv2.connectedComponents(gray)

min,max, _,__ = cv2.minMaxLoc(imgLabels)
tmp = gray.copy()
tmp = 255 * (imgLabels - min)/ (max - min)
tmp = np.uint8(tmp)
tmp = cv2.applyColorMap(tmp, cv2.COLORMAP_JET)

print("No. of blobs using connectedComponents is : ", int(max-min))

cnts, hierarchy = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

count = 0
for i,cnt in enumerate(cnts):
    area = cv2.contourArea(cnt)
    print(area)
    if int(area)>100:
        cv2.drawContours(new, cnts, i, (0,255,255), 2)
        M = cv2.moments(cnt)
        x = M["m10"]/M["m00"]
        y = M["m01"]/M["m00"]
        x,y = int(x), int(y)
        cv2.circle(new,(x,y),4, (0,0,255), -1)
        count = count +1

print("No. of blobs using findContours is : ", count)

cv2.imshow("img",new)
cv2.waitKey(0)
cv2.destroyAllWindows()
