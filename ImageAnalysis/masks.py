"""
Testing various 2D convolution methods
Important: Remember to use the correct RGB BGR ordering!
"""
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def main():
    """ main function """
    # e1 and e2 test for performance
    e1 = cv.getTickCount()

    # read in two images
    img = cv.imread('flubba1.jpg')
    mask_source = cv.imread('ap-logo.jpg')

    cv.namedWindow('Original')
    cv.imshow('Original', img)
    
    rows, cols, _channels = map(int, mask_source.shape)
    roi = img[0:rows, 0:cols]

    mask_gray = cv.cvtColor( mask_source, cv.COLOR_BGR2GRAY)
    _ret, mask = cv.threshold( mask_gray, 200, 255, cv.THRESH_BINARY )
    mask_inv = cv.bitwise_not(mask)

    img_bg = cv.bitwise_and( roi, roi, mask=mask)

    img_fg = cv.bitwise_and( mask_source, mask_source, mask=mask_inv )

    destination = cv.add(img_bg, img_fg)

    img[0:rows, 0:cols] = destination

    cv.imwrite('flubba.mask1.jpg', img)
    
    # end performance check
    e2 = cv.getTickCount()
    t = (e2-e1)/cv.getTickFrequency()

    print "Time taken: %f seconds" % t

    cv.namedWindow('Modified')
    cv.imshow('Modified', img)

    cv.waitKey(0)
    # cvReleaseImage(&img);
    return 0
    
main()
