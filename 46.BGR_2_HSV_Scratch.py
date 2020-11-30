import cv2
import numpy as np

colorPath = "Images/week4/sample.jpg"
img = cv2.imread(colorPath, cv2.IMREAD_COLOR)
hsvcv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def convertBGRtoHSV(image):
    image = image/255.0
    row,col, _ = image.shape
    hsv = np.zeros((row,col,3), dtype = 'float64')
    b,g,r = cv2.split(image)
    v = np.maximum.reduce([b,g,r])   # v is calculated

    min_rgb = np.minimum.reduce([b,g,r])
    nonzero_mask = v!=0
    zero_mask = v==0
    s = np.where(v!=0,((v-min_rgb)/v),0)

    h = np.zeros_like(s)
    h = np.where(v==r, 60*(g-b)/(v-min_rgb), h)
    h = np.where(v==g, 120 + 60*(b-r)/(v-min_rgb), h)
    h = np.where(v==b, 240 + 60*(r-g)/(v-min_rgb), h)

    h = np.where(h<0, h+360, h)
    h = h/2
    s,v = s*255, v*255
    hsv = cv2.merge([h,s,v])
    hsv = np.round(hsv)
    #hsv = np.uint8(hsv)

    return s

myhsv = convertBGRtoHSV(img)
h,s,v = cv2.split(hsvcv)

cv2.imshow("Color", img)
cv2.imshow("actual", s)
cv2.imshow("my", myhsv)

#cv2.imshow("diff", np.abs(h-myhsv))



cv2.waitKey(0)
cv2.destroyAllWindows()
