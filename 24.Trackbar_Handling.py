import cv2

imagePath = "Images/week1/boy.jpg"
img = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
orig = img.copy()

def mujeBulao(value):
    global img
    img = orig.copy()
    #print("Koi kuch kar raha he : ", value)
    if value ==0:
        value =1
    tmp = 1 + value/100
    img = cv2.resize(img, None, fx = tmp, fy = tmp,interpolation= cv2.INTER_LINEAR)
    print(img.shape)
    cv2.imshow("Sanjay", img)
    #cv2.putText(img,str(value),(200,200), cv2.FONT_HERSHEY_SIMPLEX, 1.5,(255,255,255), 2 )

value = 5
max = 100
cv2.namedWindow("Sanjay",cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar("Mera Trackbar","Sanjay", value, max, mujeBulao)

cv2.imshow("Sanjay", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
