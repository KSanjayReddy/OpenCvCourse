import cv2

colorPath = "Images/week1/boy.jpg"
img = cv2.imread(colorPath, cv2.IMREAD_COLOR)

cv2.imwrite("delete.jpg",img)

#Addtional flags can be used which will determine
#the compression quality for jpg and other stuff, but these are rarely used.
