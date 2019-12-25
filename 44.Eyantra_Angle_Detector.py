import cv2
import numpy as np
import math

img = cv2.imread("Images/extra/eyantra.jpg", cv2.IMREAD_COLOR)
img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

def getPointForColorMarket(hsv_min,hsv_max, flag):    # flag True -> red,green  flag False -> white
    global img
    mask = cv2.inRange(img_hsv, hsv_min, hsv_max)
    #some small noise is present in mask
    ksize = (3,3)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, ksize)
    img_eroded  = cv2.erode(mask, kernel, iterations = 1)
    img_dilated  = cv2.dilate(img_eroded, kernel, iterations = 2)
    mask_all = img_dilated.copy()

    contours, hierarchy = cv2.findContours(mask_all, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if flag:
        #Find the contour with the smallest are
        area_min = 10000000
        index_min = -1
        for index,cnt in enumerate(contours):
            area = cv2.contourArea(cnt)
            if area < area_min:
                area_min = area; index_min = index

        #cv2.d rawContours(img, contours, index_min, (255,255,255), 2)
        M = cv2.moments(contours[index_min])
        x = int(round(M["m10"]/M["m00"]))
        y = int(round(M["m01"]/M["m00"]))
        cv2.circle(img, (x,y), 8, (255,255,255), 2)
        final_point = (x,y)
        return final_point

    else:
        #Find the contour with the largest area
        area_max = 0
        index_max = -1
        for index,cnt in enumerate(contours):
            area = cv2.contourArea(cnt)
            if area > area_max:
                area_max = area; index_max = index

        #cv2.drawContours(img, contours, index_max, (255,255,255), 2)
        M = cv2.moments(contours[index_max])
        x = int(round(M["m10"]/M["m00"]))
        y = int(round(M["m01"]/M["m00"]))
        #cv2.circle(img, (x,y), 3, (255,0,0), -1)
        final_point = (x,y)
        return final_point


(cx0, cy0) = getPointForColorMarket( (35,60,60), (65,255,255) , True)
(cx1, cy1) = getPointForColorMarket( (168,30,50), (180,255,255) , True)
(cx2, cy2) = getPointForColorMarket( (168,30,50), (180,255,255), False )
print(cx0, cy0)
print(cx1, cy1)
print(cx2, cy2)

angle0 = math.atan2(-cy0 + cy2, cx0 - cx2) * 180.0 / 3.14
angle1 = math.atan2(-cy1 + cy2, cx1 - cx2) * 180.0 / 3.14
#to check if the angle is greater than 180 deg then to get the smallest angle subtract it from 360 deg
if abs(angle0-angle1)>180 :
    angle=round((360-abs(angle0-angle1)),2)
else:
    angle=round(abs(angle0-angle1),2)

print("The final angle is : ",angle)
text = "Angle:" + str(angle)
cv2.putText(img, text, (30,20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)
cv2.imshow("Original",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
