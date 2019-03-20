
import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument('--path', default='Lena.jpg', help='Image path.')
parser.add_argument('--out_png', default='Lena_compressed.png',
                    help='Output image path for lossy result.')
parser.add_argument('--out_jpg', default='Lena_compressed.jpg',
                   help='Output image path for lossless result.')
params = parser.parse_args()
img = cv2.imread(params.path)

# save image with lower compression—bigger file size but faster decoding
cv2.imwrite(params.out_jpg, img, [cv2.IMWRITE_JPEG_QUALITY, 0])


# check that image saved and loaded again image is the same as original one
saved_img = cv2.imread(params.out_jpg)
assert saved_img.all() == img.all()

# save image with lower compression - bigger file size but faster decoding
cv2.imwrite(params.out_png, img, [cv2.IMWRITE_PNG_COMPRESSION, 0])
saved_img = cv2.imread(params.out_png)
assert saved_img.all() == img.all()