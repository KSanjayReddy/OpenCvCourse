import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rc('image', cmap='gray')

img = np.zeros((10,10), dtype = "uint8")
img[0,1] = 1
img[-1,0]= 1
img[-2,-1]=1
img[2,2] = 1
img[5:8,5:8] = 1

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))

ksize = kernel.shape[0]  # 3
rows,cols = img.shape[0:2]   # 10, 10

border = ksize//2    # // indicates only quotient
paddedImg = cv2.copyMakeBorder(img,border, border, border, border, cv2.BORDER_CONSTANT, value=0)
method2 = np.zeros_like(paddedImg)

print(img)

# METHOD 2
for i in range(border, rows+border):
    for j in range(border, cols+border):
        # DO bitwise and on the portions
        roi = paddedImg[i-border: i+border+1,  j-border: j+border+1]
        tmp = cv2.bitwise_and(roi, kernel)
        method2[i,j] = np.amax(tmp)
            #print(paddedImg)
            #plt.imshow(paddedImg);plt.show()

dilatedImage = method2[border:border+rows,border:border+cols]
dilatedImage = dilatedImage*255
cv2.imwrite("method2_dilation.jpg",dilatedImage)
