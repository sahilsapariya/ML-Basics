import cv2

# second arg of imread method has 3 values
# 1 == loads colored image
# 0 == loads gray image
# -1 == loads image as it is 
img = cv2.imread('OpenCV\images\lena.jpg', 0)
cv2.imshow('image', img)

# we have to give time in miliseconds in waitKey() arguments
# after that window will disappear
# give 0 so that it will stay as it is
k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
# ord() function converts characters to it's ASCII values
elif k == ord('s'):
    cv2.imwrite('OpenCV\images\lena_copy.png', img)
    cv2.destroyAllWindows()