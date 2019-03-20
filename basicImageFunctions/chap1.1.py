import cv2

# load an image and print its original size:

img = cv2.imread('Lena.jpg')
print('The image shape is:',img.shape)

width, height = 128, 256
resized_img = cv2.resize(img,(width, height ))
print('The resized img:',resized_img.shape)


w_mult, h_mult = 0.25, 0.5
resized_img = cv2.resize(img, (0, 0), resized_img, w_mult, h_mult)
print('image shape:', resized_img.shape)


w_mult, h_mult = 2, 4
resized_img = cv2.resize(img, (0, 0), resized_img, w_mult, h_mult, cv2.INTER_NEAREST)
print('half sized image shape:', resized_img.shape)


img_flip_x = cv2.flip(img,0)
# for flipping in the y direction number can be greater than 0
img_flip_y = cv2.flip(img,2)

# We can flip both x and y simultaneously by passing any negative value to the function:
img_flipped_xy = cv2.flip(img, -1)
cv2.imshow('FlipXY',img_flipped_xy)
cv2.waitKey(0)