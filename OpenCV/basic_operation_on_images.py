import cv2 as cv
import numpy as np

img = cv.imread('OpenCV\images\messi.jpg')
img2 = cv.imread('OpenCV\images\lena.jpg')

# print(img.shape)
# print(img.size)
# print(img.dtype)

b,g,r = cv.split(img)
img = cv.merge((b,g,r))

# ball = img[380:440, 430:490]
# img[273:433, 100:160] = ball
img = cv.resize(img, (512, 512))
img2 = cv.resize(img2, (512, 512))

destination = cv.addWeighted(img, 0.9, img2, 0.4, 0)

cv.imshow('Image', destination)
cv.waitKey(0)
cv.destroyAllWindows()