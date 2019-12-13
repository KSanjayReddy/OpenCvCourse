import cv2
import math

colorPath = "Images/week1/musk.jpg"
img = cv2.imread(colorPath, cv2.IMREAD_COLOR)
orig = img.copy()
cv2.namedWindow("SanjayCV",cv2.WINDOW_AUTOSIZE)

center = (0,0)
point = (0,0)

def someFunction(action,x,y, flags, userdata):
    global center, point
    if action == cv2.EVENT_LBUTTONDOWN:
        center = (x,y)
    if action == cv2.EVENT_LBUTTONUP:
        point = (x,y)
        radius = int(math.sqrt(math.pow(point[0]-center[0],2) + math.pow(point[1]-center[1],2)))
        cv2.circle(img,center, radius, (0,0,255),3)


cv2.setMouseCallback("SanjayCV", someFunction)

k=0
while k!= 27:
    cv2.imshow("SanjayCV",img)
    cv2.putText(img, "Draw a Circle",(100,100),cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0),2)
    k = cv2.waitKey(1)
    if k == ord('c'):
        img = orig.copy()
