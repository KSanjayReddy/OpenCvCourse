import cv2

colorPath = "Images/week1/boy.jpg"
img = cv2.imread(colorPath,cv2.IMREAD_COLOR)

print(img.shape) # 360,480,3

#The img is always stored in row, column format
# img[row,col] = value
img[100,200] = (0,200,0)
img[0:100,0:100] = img[200:300,300:400]

cv2.imshow("img",img)
cv2.waitKey(0)
