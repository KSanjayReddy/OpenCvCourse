import cv2

imgGray = cv2.imread("Images/week1/number_zero.jpg",cv2.IMREAD_GRAYSCALE)

print(imgGray) # will print the image matrix
print("Shape ",imgGray.shape)  # shape of image = roows, cols, channels
print("dtype ", imgGray.dtype)
print("Type ", type(imgGray))

# number of channels if valid only for COLOR and transparent images
