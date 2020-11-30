import cv2

#Read an image and save original
#imagePath = "Images/week1/musk.jpg"
imagePath = "Images/week1/musk.jpg"
img = cv2.imread(imagePath, cv2.IMREAD_COLOR)
cv2.namedWindow("ElonMusk",cv2.WINDOW_AUTOSIZE)
orig = img.copy()

#Showing directions on how to crop
cv2.rectangle(img,(20,7),(340,26),(0,0,0),-1)
cv2.putText(img,"Click and Drag in ANY direction to Crop",(20,20), cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),1)

#Default values of points and variables
point1 = (0,0)
point2 = (0,0)
tmp = (0,0)
isCropStarted = False
k=0

# MouseCallback function body
def cropImage(action,x,y, flags, userdata):
    global img,point1,point2,tmp,isCropStarted
    #LOGIC Goes Here
    print(action)
    if(isCropStarted):
        if(tmp != (x,y)):
            img = orig.copy()
            tmp = (x,y)
            cv2.rectangle(img, point1, tmp, (0,255,0), 2)

    if action == cv2.EVENT_LBUTTONDOWN:
        point1 = (x,y)
        isCropStarted = True

    if action == cv2.EVENT_LBUTTONUP:
        point2 = (x,y)
        isCropStarted = False
        cv2.rectangle(img,(20,7),(360,22),(0,0,0),-1)
        cv2.putText(img,"Cropped Image is saved, Press 'q' to Quit",(20,20), cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),1)
        #extract roi and save to file
        (x1,y1) = point1; (x2,y2) = point2
        if(x2>x1 and y2>y1):
            roi = orig[y1:y2, x1:x2]
        elif(x2<x1 and y2<y1):
            roi = orig[y2:y1, x2:x1]
        elif(x2<x1 and y2>y1):
            roi = orig[y1:y2, x2:x1]
        elif(x2>x1 and y2<y1):
            roi = orig[y2:y1, x1:x2]
        cv2.imwrite("Cropped.jpg",roi)
        #Uncomment to see the cropped Image
        cv2.imshow("cropped",roi)

#Setting the MouseCallback function to the window
cv2.setMouseCallback("ElonMusk", cropImage)

while k!= ord('q'):
    cv2.imshow("ElonMusk",img)
    k = cv2.waitKey(1)
