import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rc('image', cmap = 'gray')

#path = "Images/week4/truth.png"
path = "Images/week4/sample.jpg"


img = cv2.imread(path, cv2.IMREAD_COLOR)

# In unsharp mask we first blur the image which gives the low freq info
# Then we subrtract orig img with the blurred one so we are left out with high freq
# Finally we add the high freq back to the orig image to enhance the high freq component

# Sharpen kernel this kernel does the above job
sharpen = np.array((
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]), dtype="int")

new = cv2.filter2D(img, -1, sharpen)

cv2.imshow("img", img)
cv2.imshow("new", new)
cv2.waitKey(0)
cv2.destroyAllWindows()
