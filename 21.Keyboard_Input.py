import cv2

cap = cv2.VideoCapture(0)

# width = 640, height = 480
#print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
k=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        if(k == ord('e')):
            cv2.putText(frame,"E is pressed", (100,400), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,0,255), 3 )
        elif(k == ord('z')):
            cv2.putText (frame,"Z is presses", (100,400), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,255), 3 )
        elif(k==27):
            break
        cv2.imshow("Window",frame)
        k = cv2.waitKey(5000)
    else:
        break
cap.release()
