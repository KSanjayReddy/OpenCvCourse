import cv2
import numpy as np

colorPath = "Images/week1/boy.jpg"

img = cv2.imread(colorPath, cv2.IMREAD_COLOR)
new_img = img.copy()

#creating an empty matrix of desired dimensions
empty_mat1 = np.zeros((100,200,3), dtype = 'uint8')
empty_mat2 = 255 * np.ones((100,200,3), dtype = 'uint8')

#creating an empty matrix similar to a existing image
mat1 = np.zeros_like(img)
mat2 = 255 * np.ones_like(img)

print(mat1.shape)
cv2.imshow("hello", mat2)
cv2.waitKey(0)
cv2.destroyAllWindows()
