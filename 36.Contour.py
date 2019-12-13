import cv2
import numpy as np

img = cv2.imread("Images/week3/Contour.png",cv2.IMREAD_COLOR)
img = cv2.resize( img, None, fx = 0.8, fy=0.8, interpolation = cv2.INTER_CUBIC)

#Threshold to get a binary Image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, imgBinary = cv2.threshold(imgGray,127, 255, cv2.THRESH_BINARY)

#Find Contours
# cv2.RETR_EXTERNAL , cv2.RETR_LIST , cv2.RETR_CCOMP , cv2.RETR_TREE
# cv2.CHAIN_APPROX_NONE , cv2.CHAIN_APPROX_SIMPLE , cv2.CHAIN_APPROX_TC89_KCOS
contours, hierarchy = cv2.findContours(imgBinary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#print("Contours Data : {}".format(contours))
print("Hierarchy Data : {}".format(hierarchy))
print("Number of Contours : {}".format(len(contours)))

#Draw Contours
cv2.drawContours(img, contours, -1, (0,255,0), 2)

#Center of Mass or Centroid using momemts
for cnt in contours:
    M = cv2.moments(cnt)
    #Formula
    x = int(round(M["m10"]/M["m00"]))
    y = int(round(M["m01"]/M["m00"]))

    cv2.circle(img, (x,y), 5, (0,0,255), -1)

# Area and Parameter
for index,cnt in enumerate(contours):
    area = cv2.contourArea(cnt)
    perimeter = cv2.arcLength(cnt,True)
    print("For contour no.: {}, Area : {}, Perimeter : {}".format(index, area, perimeter))

# Finding Vertical Bounding Boxes
for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,255),2)

# Minimum Area Rectangles
for cnt in contours:
    box = cv2.minAreaRect(cnt)  #box has rect data along with some other data
    boxPts = cv2.boxPoints(box)    #extracting only the rect points data
    boxPts = np.int0(boxPts)
    cv2.drawContours(img,[boxPts], -1, (0,255,255), 2)

# Fit a Circle
for cnt in contours:
    ((x,y), radius) = cv2.minEnclosingCircle(cnt)        # x, y and radius will be in float
    cv2.circle(img, (int(x),int(y)), int(radius), (180,180,180), 2)

# Fit an Ellipse
for cnt in contours:
    # To fit an ellipse we need atleast 5 points in our contour
    if len(cnt) < 5:
        continue
    ellipseData = cv2.fitEllipse(cnt)
    cv2.ellipse(img, ellipseData, (200,50,100), 2)

cv2.imshow("Original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
