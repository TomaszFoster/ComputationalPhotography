import cv2 as cv

# read in two images
IMG = cv.imread('flubba1.jpg')
IMG2 = cv.imread('flubba2.jpg')

# print information about image
print 'Image type:     ', IMG.dtype
print 'Image height:   ', IMG.shape[0]
print 'Image width:    ', IMG.shape[1]
print 'Channel count:  ', IMG.shape[2]

# save a reflection of the image with border size of SIZE
SIZE = 500
REFLECTION = cv.copyMakeBorder(IMG, SIZE, SIZE, SIZE, SIZE, cv.BORDER_REFLECT_101)

# draw a green rectangle in top right corner of the reflection
cv.rectangle(REFLECTION, (REFLECTION.shape[1] - 300, 0), (REFLECTION.shape[1], 300), (0, 255, 0), 3)
# output the reflection
cv.imwrite('flubba.mirror.jpg', REFLECTION)

# add, subtract, and make weighted versions of the combination of the two input files
ADDITION = IMG + IMG2
SUBTRACTION = IMG - IMG2
ALPHA = 0.65
WEIGHTED = (1 - ALPHA)*(IMG) + ALPHA*IMG2

cv.imwrite('flubba.addition.jpg', ADDITION)
cv.imwrite('flubba.subtraction.jpg', SUBTRACTION)
cv.imwrite('flubba.weighted.jpg', WEIGHTED)

# jpg channel order is Blue, Green, Red
# get the blue channel intensities as well as an image with only blues visible
BLUE_CHANNEL = IMG[:, :, 0]
cv.imwrite('flubba.blue.channel.jpg', BLUE_CHANNEL)

BLUE_IMG = IMG
BLUE_IMG[:, :, 1] = 0
BLUE_IMG[:, :, 2] = 0
cv.imwrite('flubba.blue.jpg', BLUE_IMG)

# cv.imshow('Flubba',ADDITION)
# cv.namedWindow('Flubba', cv.WINDOW_NORMAL)
# cv.imshow('Flubba', REFLECTION)

# cv.moveWindow('Flubba', 0, 0)

# k = cv.waitKey(0)
# if k == 27:
#     cv.destroyAllWindows()