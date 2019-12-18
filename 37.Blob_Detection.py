import cv2

#img = cv2.imread("Images/week3/blob_detection.jpg", cv2.IMREAD_COLOR)
#img = cv2.imread("Images/week3/shapes.jpg", cv2.IMREAD_COLOR)
img = cv2.imread("Images/week3/test.png", cv2.IMREAD_COLOR)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

params.filterByColor = 1
params.blobColor = 255   # 0 for dark blobs 255 for bright blobs


# Change thresholds
params.minThreshold = 0    #The darkest
params.maxThreshold = 255  # The brightest

# Filter by Area.
params.filterByArea = True
params.minArea = 500
params.maxArea = 400000

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.8
params.maxCircularity = 1

# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.1
params.maxConvexity = 1

# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.01
params.maxInertiaRatio = 1

# Create a detector with the parameters
detector = cv2.SimpleBlobDetector_create(params)

# Create a detctor object with default Param
#detector = cv2.SimpleBlobDetector_create()

# Use the detect function with the object created
keyPoints = detector.detect(imgGray)

for k in keyPoints:
    x,y = k.pt
    radius = k.size/2
    #Mark the Center
    cv2.circle(img, (int(x),int(y)), 3, (255,0,0), -1)
    #Mark the Blob
    cv2.circle(img, (int(x),int(y)), int(radius), (0,0,255), 2)

cv2.imshow("Original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
