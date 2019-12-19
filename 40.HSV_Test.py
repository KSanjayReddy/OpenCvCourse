import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rc('image', cmap='gray')

VALUE_TEST = False
SATURATION_TEST = False
HUE_TEST = True

# Value test.
plt.figure(figsize=(50,50))

if VALUE_TEST:
    for i in range(0,7):
        # Create 50x50 HSV image with all zeros
        imhsv = np.zeros((50, 50, 3), dtype=np.uint8)

        # Set Hue = 0, Saturation = 0, Value = i x 40
        v = i * 40
        imhsv[:,:,:] = (0, 0, v)

        # Convert HSV to RGB
        imrgb = cv2.cvtColor(imhsv, cv2.COLOR_HSV2RGB)

        # Display image
        ax = plt.subplot(1, 7, i+1)
        plt.imshow(imrgb)
        plt.axis('off')
        ax.set_title('V='+ str(v))

if SATURATION_TEST:
    # Set brightness to 128, hue to 0, and change saturation
    for i in range(0,7):
        # Create 50x50 HSV image with all zeros
        imhsv = np.zeros((50, 50, 3), dtype=np.uint8)

        # Set Hue = 0, Saturation = s, Value = 128
        s = i * 40
        imhsv[:,:,:] = (0, s, 128)

        # Convert HSV to RGB
        imrgb = cv2.cvtColor(imhsv, cv2.COLOR_HSV2RGB)

        # Display image
        ax = plt.subplot(1, 7, i+1)
        plt.imshow(imrgb)
        plt.axis('off')
        ax.set_title('S='+ str(s))

if HUE_TEST:
    # Set brightness to 255,  saturation to 255
    for i in range(0,7):
        # Create 50x50 HSV image with all zeros
        imhsv = np.zeros((50, 50, 3), dtype=np.uint8)

        # Set Hue = h, Saturation = 255, Value = 255
        h = i * 30     # Since range is 0 to 180
        imhsv[:,:,:] = (h, 250, 250)

        # Convert HSV to RGB
        imrgb = cv2.cvtColor(imhsv, cv2.COLOR_HSV2RGB)

        # Display image
        ax = plt.subplot(1, 7, i+1)
        plt.imshow(imrgb)
        plt.axis('off')
        ax.set_title('H='+ str(h))
plt.show()
