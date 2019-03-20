import argparse
import cv2
# parser = argparse.ArgumentParser()
# parser.add_argument('--path', default = 'Lena.jpg', help= 'Image path.')
# params = parser.parse_args()
# img = cv2.imread(params.path)


img = cv2.imread('blueEyes.jpeg')
print('original image shape:', img.shape)

width, height = 128, 256
resized_img = cv2.resize(img, (width, height))
print('resized to 128x256 image shape:', resized_img.shape)
cv2.imshow("Image", resized_img)

cv2.waitKey(500)