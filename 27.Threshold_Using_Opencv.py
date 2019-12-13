import cv2, time

img = cv2.imread("Images/week3/threshold.png", cv2.IMREAD_GRAYSCALE)
img = cv2.resize( img, None, fx = 0.7, fy=0.7, interpolation = cv2.INTER_CUBIC)

t = time.time()
ret, dst = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
# cv2.THRESH_BINARY
# cv2.THRESH_BINARY_INV
# cv2.THRESH_TRUNC
# cv2.THRESH_TOZERO
# cv2.THRESH_TOZERO_INV

print(time.time() - t)

cv2.imshow("Original Image",img)
cv2.imshow("Thresholed Image",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
