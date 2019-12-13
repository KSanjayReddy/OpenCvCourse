import cv2

colorPath = "Images/week1/boy.jpg"
img = cv2.imread(colorPath, cv2.IMREAD_COLOR)

cv2.namedWindow("WINDOW_AUTOSIZE", cv2.WINDOW_AUTOSIZE)

cv2.namedWindow("WINDOW_NORMAL", cv2.WINDOW_NORMAL)

#cv2.imshow("WINDOW_AUTOSIZE", img)
cv2.imshow("WINDOW_NORMAL", img)

cv2.destroyWindow("WINDOW_AUTOSIZE") #destroy particular window

x = cv2.waitKey(3000)  # 0 means to wait indefinite time untill some key is pressed
print(x)            # x is the ASCII value of the key pressed
#cv2.waitKey(3000)  # will wait for 3000 ms
cv2.destroyAllWindows()        # to destroy all the windows
