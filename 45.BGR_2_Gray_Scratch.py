import cv2
import numpy as np

colorPath = "Images/week1/boy.jpg"
img = cv2.imread(colorPath, cv2.IMREAD_COLOR)
graycv = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def convertBGRtoGray(img):
    img = np.float32(img) / 255.0
    b,g,r = cv2.split(img)
    new = np.zeros_like(b)
    new = 0.299 * r + 0.587 * g + 0.114*b
    new = np.uint8(np.round(new * 255.0))
    return new

gray = convertBGRtoGray(img)

#cv2.imshow("Color", img)
cv2.imshow("graycv", graycv)
cv2.imshow("gray", gray)
cv2.imshow("diff", np.abs(gray-graycv))



cv2.waitKey(0)
cv2.destroyAllWindows()
