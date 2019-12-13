import cv2

imagePath = "Images/week1/truth.jpg"
img = cv2.imread(imagePath, cv2.IMREAD_COLOR)
orig  = img.copy()

def changeScaleType(*args):
    global scaleType
    scaleType = args[0]

def ScaleImage(*args):
    global scaleFactor,scaleType,img

    if(scaleType):
        scaleFactor = 1 - args[0]/100
    else:
        scaleFactor = 1 + args[0]/100

    if scaleFactor == 0:
        scaleFactor =1
    img = cv2.resize(orig, None, fx = scaleFactor, fy = scaleFactor,interpolation= cv2.INTER_CUBIC)
    cv2.imshow("ResizeImage", img)

scaleFactor = 1
maxValue = 100
scaleType = 0
cv2.namedWindow("ResizeImage",cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar("Scale Percentage","ResizeImage", scaleFactor, maxValue, ScaleImage)
cv2.createTrackbar("Type: \n 0: Scale Up \n 1: Scale Down","ResizeImage", 0, 1, changeScaleType)


cv2.imshow("ResizeImage", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
