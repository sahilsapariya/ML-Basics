import cv2
import numpy as np

# img = cv2.imread('lena.jpg', 1)
img = np.zeros([512, 512, 3], np.uint8)

# img = cv2.line(img, (0,0), (255, 255), (255, 0, 0), 5)

# 2nd and 3rd arguments are coordinates, 4th arg is color, 5th arg is width
img = cv2.rectangle(img, (204, 210), (410, 428), (0, 0, 255), 5)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCv', (10, 263), font, 4, (255,0,0), cv2.LINE_AA)
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()