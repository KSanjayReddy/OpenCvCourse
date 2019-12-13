import cv2
import numpy as np

colorPath = "Images/week1/boy.jpg"

img = cv2.imread(colorPath, cv2.IMREAD_COLOR)
print("Initial dtype is {}".format(img.dtype))

new = np.float32(img)
print("new dtype is {}".format(new.dtype))
new = new / 255.0



old = new * 255
old = np.uint8(old)


cv2.imshow("image", old)
cv2.waitKey(0)
cv2.destroyAllWindows()
