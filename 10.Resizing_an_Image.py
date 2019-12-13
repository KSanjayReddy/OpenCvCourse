import cv2

colorPath = "Images/week1/boy.jpg"

img = cv2.imread(colorPath,cv2.IMREAD_COLOR)
print("Shape of original image is {}".format(img.shape))

# fixed dimensions
new1 = cv2.resize( img, (200,500), interpolation = cv2.INTER_CUBIC)
new2 = cv2.resize( img, (200,500), interpolation = cv2.INTER_NEAREST)

# using scaling factor
new3 = cv2.resize( img, None, fx = 0.6, fy=1.2, interpolation = cv2.INTER_CUBIC)
print("Shape of original image is {}".format(new2.shape))


cv2.imshow("cubic", new1)
cv2.imshow("nearest", new2)
cv2.imshow("scaling", new3)
cv2.waitKey(0)
cv2.destroyAllWindows()
