import cv2

videoPath = "Videos/chaplin.mp4"
#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(videoPath)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT ))
print(cap.get(cv2.CAP_PROP_FPS))
print(cap.get(cv2.CAP_PROP_FOURCC))

while(cap.isOpened()):
    ret, img = cap.read()
    if ret:
        cv2.imshow("Hello",img)
        print(cap.get(cv2.CAP_PROP_POS_MSEC))
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
