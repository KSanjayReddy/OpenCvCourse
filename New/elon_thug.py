import cv2
import numpy as np
import matplotlib.pyplot as plt

elonPath = "../Images/week1/musk.jpg"
glassPath = "../Images/week1/thug1.png"
cigarPath = "../Images/week1/cigar.png"
writePath = "../Images/week1/Thug_Elon.jpg"

elon = cv2.imread(elonPath, cv2.IMREAD_COLOR)
glass = cv2.imread(glassPath, cv2.IMREAD_UNCHANGED)
cigar = cv2.imread(cigarPath, cv2.IMREAD_UNCHANGED)

glass = cv2.resize(glass,(314,170), interpolation = cv2.INTER_AREA)
cigar = cv2.resize(cigar,None, fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)

#convert both to float before arithmaric operations

elon = np.float32(elon) * (1/255.0)
glass = np.float32(glass) * (1/255.0)
cigar = np.float32(cigar) * (1/255.0)

height,width = glass.shape[0:2]
startRow,startCol = 105,130

glassBGR = glass[:,:,0:3]
glassMask = glass[:,:,3]

cigarBGR = cigar[:,:,0:3]
cigarBGR = cv2.add(cigarBGR, np.ones_like(cigarBGR)* (40/255)) # add some brightness
cigarBGR = cigarBGR * 1.2 # add some contrast
cigarMask = cigar[:,:,3]

glassMask = cv2.merge((glassMask,glassMask,glassMask)) # single channel to 2 chn
maskFg = glassMask
maskBg = 1 - maskFg

cigarMask = cv2.merge((cigarMask,cigarMask,cigarMask)) # single channel to 2 chn
cmaskFg = cigarMask
cmaskBg = 1 - cmaskFg

roi = elon[startRow:startRow+height, startCol:startCol+width]
cStartRow, cStartCol = 310,330
h,w = cigar.shape[0:2]
croi = elon[cStartRow:cStartRow+h, cStartCol:cStartCol+w]

tmp1 = cv2.multiply(roi,maskBg)
tmp2 = cv2.multiply(glassBGR,maskFg)

tmp3 = cv2.multiply(croi,cmaskBg)
tmp4 = cv2.multiply(cigarBGR,cmaskFg)

elon[startRow:startRow+height, startCol:startCol+width] = cv2.add(tmp1,tmp2)
elon[cStartRow:cStartRow+h, cStartCol:cStartCol+w] = cv2.add(tmp3,tmp4)
cv2.imshow("Elon",elon)

elon = np.uint8(elon*255)
cv2.imwrite(writePath, elon)

cv2.waitKey(0)
cv2.destroyAllWindows()
