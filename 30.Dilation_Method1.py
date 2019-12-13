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
out = cv2.VideoWriter("method1_dilation.mp4",cv2.VideoWriter_fourcc('M','J','P','G'), 10, (cols, rows))

print(img)

# METHOD 1
for i in range(border, rows+border):
    for j in range(border, cols+border):
        #Search for white pixel in original Images
        if img[i-border, j-border]:
            print("White pixel fount @ {},{}".format(i,j))
            roi = paddedImg[i-border: i+border+1,  j-border: j+border+1]
            paddedImg[i-border: i+border+1,  j-border: j+border+1] = cv2.bitwise_or(roi, kernel)
            out.write(img)
            #print(paddedImg)
            #plt.imshow(paddedImg);plt.show()

dilatedImage = paddedImg[border:border+rows,border:border+cols]
dilatedImage = dilatedImage*255
cv2.imwrite("method1_dilation.jpg",dilatedImage)
new = cv2.dilate(img,kernel, iterations=1)
new = new*255
cv2.imwrite("opencv_dilation.jpg",new)
out.release()
