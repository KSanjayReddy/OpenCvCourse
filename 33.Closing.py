import cv2
# Opening means Dilation then Erosion => To remove small black blobs

img = cv2.imread("Images/week3/closing.png",cv2.IMREAD_GRAYSCALE)

'''
#Method 1 using erosion and Dilation functions
#Either take small kernel and iterate multiple times else take a big kernel
ksize = (21,21)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, ksize)
img_dilated = cv2.dilate(img,kernel, iterations = 1)
img_closed = cv2.erode(img_dilated,kernel,iterations = 1)

'''
#Method 2
ksize = (21,21)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,ksize)
img_closed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations = 1)


cv2.imshow("Original",img)
#cv2.imshow("Dilated",img_dilated)
cv2.imshow("Closed",img_closed)
cv2.waitKey(0)
cv2.destroyAllWindows()
