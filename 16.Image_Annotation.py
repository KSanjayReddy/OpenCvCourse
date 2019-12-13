import cv2
import numpy as np

#Annnotate means to add text, or labels for the sake of explanation

muskPath = "Images/week1/musk.jpg"
img = cv2.imread(muskPath,cv2.IMREAD_COLOR)
# 500, 600, 3
#print("Shape of original image is {}".format(img.shape))
cv2.line(img, (100,100), (300,450), (255,0,100), thickness= 10, lineType=cv2.LINE_AA)

cv2.circle(img, (280,150), 30, (0,0,255), thickness = -1, lineType= cv2.LINE_AA)

cv2.ellipse(img, (300,300), (100,40), 0, 0, 300, (100,100,255), thickness=3)
cv2.ellipse(img, (300,300), (100,40), 80, 0, 300, (100,255,0), thickness=3)

cv2.rectangle(img, (100,150), (300,400), (200,200,200), thickness=3)

#For Text
text = "Hello Im Musk"
#fontSize = 1.5
fontStyle = cv2.FONT_HERSHEY_SIMPLEX
fontColor = (0,255,0)
fontThickness = 2

fontSize= cv2.getFontScaleFromHeight(fontStyle, 30, 2)

cv2.putText(img, text, (100,450), fontStyle, fontSize, fontColor, fontThickness)
testSize, baseLine = cv2.getTextSize(text, fontStyle, fontSize, fontThickness)

print(testSize, baseLine) 

cv2.imshow("Hello", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
