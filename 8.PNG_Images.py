import cv2
import matplotlib.pyplot as plt
plt.rc('image', cmap='gray')

pngPath = "Images/week1/panther.png"
img = cv2.imread(pngPath, cv2.IMREAD_UNCHANGED)

b,g,r,a = cv2.split(img)

plt.figure(figsize=[20,5])
tmp = cv2.cvtColor(img,cv2.COLOR_BGRA2RGBA)

plt.subplot(1,4,1);plt.imshow(tmp);plt.title("Original")
plt.subplot(1,5,2);plt.imshow(b);plt.title("Blue CHannel")
plt.subplot(1,5,3);plt.imshow(g);plt.title("Green Channel")
plt.subplot(1,5,4);plt.imshow(r);plt.title("Red Channel")
plt.subplot(1,5,5);plt.imshow(a);plt.title("Alpha Channel")

new = cv2.merge((b,g,r,a))
cv2.imshow("hello",new)

cv2.imwrite("test_mask.jpg",a)
cv2.imwrite("A.png",img)
cv2.imwrite("B.png",new)


plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
