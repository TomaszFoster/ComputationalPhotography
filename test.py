import cv2 as cv

IMG = cv.imread('flubba1.jpg')

# do something to the image
# img[:,:,0] = 0

# save the image
SIZE = 500
REFLECTION = cv.copyMakeBorder(IMG, SIZE, SIZE, SIZE, SIZE, cv.BORDER_REFLECT_101)
cv.imwrite('flubba.out.jpg', REFLECTION)
