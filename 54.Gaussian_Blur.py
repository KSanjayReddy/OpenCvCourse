import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rc('image', cmap = 'gray')

path = "Images/week4/gaussian-noise.png"

img = cv2.imread(path, cv2.IMREAD_COLOR)

# img, kszie, sigmaX, sigmaY
# should be used where there is low gaussian noise, if higher go for bilateral
new1 = cv2.GaussianBlur(img,(9,9), 0,0)
new2 = cv2.GaussianBlur(img,(25,25), 50,50)

out = np.hstack((img,new1,new2))

cv2.imshow("orig", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
