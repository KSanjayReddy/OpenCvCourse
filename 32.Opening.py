import cv2
# Opening means Erosion then Dilation => To remove small white spots
img = cv2.imread("Images/week3/opening.png",cv2.IMREAD_GRAYSCALE)

'''
#Method 1 using erosion and Dilation functions
#Either take small kernel and iterate multiple times else take a big kernel
ksize = (17,17)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, ksize)
img_eroded = cv2.erode(img,kernel,iterations = 1)
img_open = cv2.dilate(img_eroded,kernel, iterations = 1)
'''
#Method 2
ksize = (17,17)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,ksize)
img_open = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations = 1)

cv2.imshow("Original",img)
#cv2.imshow("Eroded",img_eroded)
cv2.imshow("Opened",img_open)
cv2.waitKey(0)
cv2.destroyAllWindows()
