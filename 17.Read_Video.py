import cv2

videoPath = "Videos/chaplin.mp4"
#cap = cv2.VideoCapture(0)  #to get webcam feed
cap = cv2.VideoCapture(videoPath)

if cap.isOpened()==False:
    print("sorry, unable to open video")

while(cap.isOpened()):
    ret, img = cap.read()

    if(ret):
        cv2.imshow("Hello",img)
        cv2.waitKey(1)
    else:
        break

cap.release()
