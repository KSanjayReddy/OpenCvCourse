import cv2
import numpy as np

colorPath = "Images/week4/sample.jpg"
img = cv2.imread(colorPath, cv2.IMREAD_COLOR)
hsvcv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def convertBGRtoHSV(img):
    img = np.float32(img) / 255.0
    b,g,r = cv2.split(img)

    v = np.maximum.reduce([b,g,r])

    min_bgr = np.minimum.reduce([b,g,r])
    s = np.where(v==0,0, (v- min_bgr)/v)

    h = np.zeros_like(v)
    h = np.where(v==r , 60*(g-b)/(v - min_bgr), h)
    h = np.where(v==g, 120 + 60*(b-r)/(v - min_bgr), h)
    h = np.where(v==b, 240 + 60*(r-g)/(v - min_bgr), h)
    h = np.where(h<0, h+360, h)

    # current ranges h : 0-360, s,v : 0-1
    # convert to uint 8, i.e s,v : 0:255, h:1-180
    s = np.uint8(np.round(s*255))
    v = np.uint8(np.round(v*255))
    h = np.uint8(np.round(h/2))

    new = cv2.merge((h,s,v))
    return new

myhsv = convertBGRtoHSV(img)
h,s,v = cv2.split(hsvcv)

cv2.imshow("Color", img)
cv2.imshow("actual", hsvcv)
cv2.imshow("my", myhsv)
cv2.imshow("Diff", hsvcv - myhsv)
#cv2.imshow("diff", np.abs(h-myhsv))



cv2.waitKey(0)
cv2.destroyAllWindows()
