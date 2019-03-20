import cv2
import numpy as np
#from matplotlib import pyplot as plt



img = cv2.imread('blueEyes.jpeg')
print('original image shape:', img.shape)
cv2.imshow("Image", img)
width, height = 480, 640
resized_img = cv2.resize(img, (width, height))
print('resized to 128x256 image shape:', resized_img.shape)



cv2.imshow("Image", resized_img)
# cv2.imshow("Mask", mask)
# cv2.imshow("res", res)



#mask
# hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
blur = cv2.blur(resized_img,(50,50))

cv2.imshow("blured", blur)
cv2.waitKey(0)
# lower_red = np.array([30,150,50])
# upper_red = np.array([255,255,180])
#
# plt.subplot(221),plt.imshow(img),plt.title('Original')
# plt.xticks([]), plt.yticks([])
 #plt.subplot(222),plt.imshow(blur),plt.title('Blurred')
#plt.xticks([]), plt.yticks([])
# plt.subplot(223),plt.imshow(hsv),plt.title('hsv')
# plt.xticks([]), plt.yticks([])
#plt.show()

#
# if img is not None:
#     cv2.imshow("Image", img)
#     cv2.waitKey(500)
#
# else:
#     print("Empty image!")
