import cv2
import numpy as np
import matplotlib.pyplot as plt

elonPath = "../Images/week1/musk.jpg"
glassPath = "../Images/week1/sunglass.png"

elon = cv2.imread(elonPath, cv2.IMREAD_COLOR)
glass = cv2.imread(glassPath, cv2.IMREAD_UNCHANGED)
glass = cv2.resize(glass,None, fx=0.5, fy =0.5, interpolation = cv2.INTER_AREA)
print(glass.shape)
#convert both to float before arithmaric operations
elon = np.float32(elon) * (1/255.0)
glass = np.float32(glass) * (1/255.0)

height,width = glass.shape[0:2]
startRow,startCol = 145,130

glassBGR = glass[:,:,0:3]
glassMask = glass[:,:,3]
glassMask = cv2.merge((glassMask,glassMask,glassMask)) # single channel to 2 chn
maskFg = glassMask
maskBg = 1 - maskFg

roi = elon[startRow:startRow+height, startCol:startCol+width]

tmp1 = cv2.multiply(roi,maskBg)
tmp2 = cv2.multiply(glassBGR,maskFg)
tmp3 = cv2.multiply(roi,maskFg)
tmp4 = cv2.addWeighted(tmp2, 0.75, tmp3, 0.25, 0)

elon[startRow:startRow+height, startCol:startCol+width] = cv2.add(tmp1,tmp4)

cv2.imshow("Elon",elon)

cv2.waitKey(0)
cv2.destroyAllWindows()
