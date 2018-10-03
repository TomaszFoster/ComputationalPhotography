"""
Testing finding countours and drawing them on the original image
"""
import numpy as np
import cv2 as cv

def main():
    """ main function """

    img = cv.imread('flubba1.jpg', 0)
    # get grayscale of image
    # img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # find thresholds of image
    _ret, thresh = cv.threshold(img, 127, 255, 0)

    # find the contours themselves
    _img, contours, _hierarchy = cv.findContours(thresh, 1, 2)
    # print contours
    cnt = contours[0]
    M = cv.moments(cnt)
    print M
    # cx = int(M['m10']/M['m00'])
    # cy = int(M['m01']/M['m00'])

    # draw the actual contours on the original image
    cv.drawContours(img, contours, -1, (0, 255, 0), 3)

    cv.imwrite('flubba.contour.jpg', img)

main()
