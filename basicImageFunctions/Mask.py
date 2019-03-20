import cv2
import numpy as np

# Load the original image
img = cv2.imread("blueEyes.jpeg")
org_size = img.shape[0:3]
print('Orignal size', org_size )
# Create the basic black image
#mask = np.zeros(img.shape, dtype = "uint8")

# Draw a white, filled rectangle on the mask image
#rect = cv2.rectangle(img, (1000, 500), (1800, 720), (255, 255, 255), -1)
#blur = cv2.blur(rect, (10,10))# Apply the mask and display the results
#maskedImg = cv2.bitwise_and(img, blur)
#cv2.namedWindow("Masked Image", cv2.WINDOW_NORMAL)
cv2.imshow("Masked Image", img)
cv2.waitKey(0)

