import cv2
import numpy as np

colorPath = "Images/week1/boy.jpg"
img = cv2.imread(colorPath, cv2.IMREAD_COLOR)
graycv = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def convertBGRtoGray(image):
    row,col, _ = image.shape
    gray = np.zeros((row,col,1), dtype = 'float64')
    b,g,r = cv2.split(image)
    grayf = image[:,:,0]*0.1147 + image[:,:,1]*0.587  + image[:,:,2]* 0.299
    gray = np.round(grayf)
    gray = np.uint8(gray)
    return gray

gray = convertBGRtoGray(img)

#cv2.imshow("Color", img)
cv2.imshow("graycv", graycv)
cv2.imshow("gray", gray)
cv2.imshow("diff", np.abs(gray-graycv))



cv2.waitKey(0)
cv2.destroyAllWindows()
