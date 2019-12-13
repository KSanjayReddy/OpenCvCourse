import cv2
import numpy as np
import matplotlib.pyplot as plt

muskPath = "Images/week1/musk.jpg"
glassPath = "Images/week1/sunglass.png"

img = cv2.imread(muskPath, cv2.IMREAD_COLOR)
glass = cv2.imread(glassPath, cv2.IMREAD_UNCHANGED)
glass = cv2.resize(glass,(300,100), interpolation = cv2.INTER_CUBIC)

'''
#Using Arithmatic operations
#####################################

#convert both the images to float
img = np.float32(img) / 255.0
glass = np.float32(glass) / 255.0

roi = img[150:250, 140:440]
glass_alpha = glass[:,:,3]
glass_alpha = cv2.merge((glass_alpha, glass_alpha, glass_alpha))
mask1 = glass_alpha
mask2 = 1 - glass_alpha

first = cv2.multiply(roi, mask2)
second = cv2.multiply(glass[:,:,0:3], mask1)
third =  cv2.multiply(roi, mask1)
fourth = cv2.addWeighted(second,0.7,third,0.3,0)

final = cv2.add(first, fourth)
img[150:250, 140:440] = final
cv2.imshow("First",first)
cv2.imshow("Second",second)
cv2.imshow("third",third)
cv2.imshow("fourth",fourth)
cv2.imshow("final",img)
##################################
'''

#with binary operations
#############################
roi = img[150:250, 140:440]
glass_alpha = glass[:,:,3]
glass_alpha = cv2.merge((glass_alpha, glass_alpha, glass_alpha))
mask1 = glass_alpha
mask2 = cv2.bitwise_not(glass_alpha)

first = cv2.bitwise_and(roi, mask2)
second = cv2.bitwise_and(glass[:,:,0:3], mask1)

final = cv2.bitwise_or(first,second)
cv2.imshow("first",first)
cv2.imshow("second",second)
cv2.imshow("final",final)
#############################


cv2.waitKey(0)
cv2.destroyAllWindows()
