import cv2

videoPath = "Videos/chaplin.mp4"
#cap = cv2.VideoCapture(0)  #to get webcam feed
cap = cv2.VideoCapture(videoPath)

fwidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
fheight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(fwidth)
out = cv2.VideoWriter("test.mp4",cv2.VideoWriter_fourcc('M','J','P','G'), 10, (fwidth, fheight))

while(cap.isOpened()):
    ret, img = cap.read()
    if ret:
        out.write(img)
        cv2.imshow("Hello",img)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
out.release()
