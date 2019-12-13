import cv2
import matplotlib.pyplot as plt
plt.rc('image', cmap='gray')


colorPath = "Images/week1/boy.jpg"
img = cv2.imread(colorPath, cv2.IMREAD_COLOR)

#cv2.imshow("Hello world", img)
#cv2.waitKey(0)


#img = img[:,:,::-1]
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.colorbar()
plt.show()
