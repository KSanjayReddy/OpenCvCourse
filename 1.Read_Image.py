import cv2

grayPath = "Images/week1/boy_gray.jpg"
colorPath = "Images/week1/boy.jpg"
pngPath = "Images/week1/panther.png"

if True:
    imgGray = cv2.imread(grayPath,cv2.IMREAD_GRAYSCALE)
    imgColor = cv2.imread(grayPath,cv2.IMREAD_COLOR)
    imgUnchan = cv2.imread(grayPath,cv2.IMREAD_UNCHANGED)

if False:
    imgGray = cv2.imread(colorPath,cv2.IMREAD_GRAYSCALE)
    imgColor = cv2.imread(colorPath,cv2.IMREAD_COLOR)
    imgUnchan = cv2.imread(colorPath,cv2.IMREAD_UNCHANGED)

if 0:
    imgGray = cv2.imread(pngPath,cv2.IMREAD_GRAYSCALE)
    imgColor = cv2.imread(pngPath,cv2.IMREAD_COLOR)
    imgUnchan = cv2.imread(pngPath,cv2.IMREAD_UNCHANGED)

print("Read as a gray image, number of channels ",imgGray.shape,imgGray.dtype)
print("Read as a color image, number of channels ",imgColor.shape,imgColor.dtype)
print("Read as a unchanged image, number of channels ",imgUnchan.shape,imgUnchan.dtype)

print(imgColor[359,479])
