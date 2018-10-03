"""
Testing finding countours and drawing them on the original image
"""
# import numpy as np
import cv2 as cv
# import matplotlib.pyplot as plt

def main():
    """ main function """

    img = cv.imread('flubba1.jpg')
    # get grayscale of image
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # find thresholds of image
    _ret, thresh = cv.threshold(img_gray, 127, 255, 0)

    # find the contours themselves
    _img2, contours, _hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # draw the actual contours on the original image
    cv.drawContours(img, contours, -1, (0, 255, 0), 3)

    cv.imwrite('flubba.contour.jpg', img)

main()
