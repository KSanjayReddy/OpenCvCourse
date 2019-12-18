import cv2
import math

colorPath = "Images/week1/musk.jpg"
img = cv2.imread(colorPath, cv2.IMREAD_COLOR)
orig = img.copy()
cv2.namedWindow("SanjayCV",cv2.WINDOW_AUTOSIZE)

center = (0,0)
point = (0,0)

def someFunction(action,x,y, flags, userdata):
    print(flags)

    if action == cv2.EVENT_MOUSEWHEEL + cv2.EVENT_FLAG_CTRLKEY:
        print("Hello")
        if (cv2.getMouseWheelDelta(cv2.EVENT_MOUSEWHEEL) > 0):
            print("Hello")

    elif action == cv2.EVENT_MOUSEWHEEL + cv2.EVENT_FLAG_CTRLKEY:
        print("Hiii")
        if (cv2.getMouseWheelDelta(cv2.EVENT_MOUSEWHEEL) < 0):
            print("Hiii")
      # Resize image

cv2.setMouseCallback("SanjayCV", someFunction)

k=0
while k!= 27:
    cv2.imshow("SanjayCV",img)
    cv2.putText(img, "Draw a Circle",(100,100),cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0),2)
    k = cv2.waitKey(1)
    if k == ord('c'):
        img = orig.copy()
