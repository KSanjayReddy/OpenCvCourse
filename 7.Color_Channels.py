import cv2
import matplotlib.pyplot as plt
plt.rc('image', cmap='gray')


colorPath = "Images/week1/musk.jpg"
img = cv2.imread(colorPath, cv2.IMREAD_COLOR)

b,g,r = cv2.split(img)


plt.figure(figsize=[20,5])
'''
plt.subplot(1,4,1);plt.imshow(img[:,:,::-1]);plt.title("Original")
plt.subplot(1,4,2);plt.imshow(img[:,:,0]);plt.title("Blue CHannel")
plt.subplot(1,4,3);plt.imshow(img[:,:,1]);plt.title("Green Channel")
plt.subplot(1,4,4);plt.imshow(img[:,:,2]);plt.title("Red Channel")
'''
plt.subplot(1,4,1);plt.imshow(img[:,:,::-1]);plt.title("Original")
plt.subplot(1,4,2);plt.imshow(b);plt.title("Blue CHannel")
plt.subplot(1,4,3);plt.imshow(g);plt.title("Green Channel")
plt.subplot(1,4,4);plt.imshow(r);plt.title("Red Channel")

new = cv2.merge((b,g,r))
cv2.imshow("hello",new)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
