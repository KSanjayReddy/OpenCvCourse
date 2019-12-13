import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Images/week3/erosion_example.jpg",cv2.IMREAD_COLOR)

# Either take one big kernel and do once
# or take one small kernal and iterate twice
ksize = (7,7)  # size is generally 3,5,7,9
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, ksize)
#kernel = kernel * 255
dst  = cv2.erode(img, kernel, iterations = 1)

cv2.imshow("Original",img)
cv2.imshow("Kernel",kernel)
cv2.imshow("Output",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
