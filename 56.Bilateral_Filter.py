import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rc('image', cmap = 'gray')

path = "Images/week4/gaussian-noise.png"
img = cv2.imread(path, cv2.IMREAD_COLOR)

#Parameters of bilateral filtering
# diameter of pixel neighbourhood used for filtering
d = 15
# larger the value more distant color will also have impact
sigmaColor = 80
# larger the value the more farther pixels will also have impact
sigmaSpace = 80

# Perfect for gaussian noise
new = cv2.bilateralFilter(img, d, sigmaColor, sigmaSpace)

out = np.hstack((img,new))

cv2.imshow("Bilateral Filtering", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
