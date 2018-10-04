"""
Testing various 2D convolution methods
Important: Remember to use the correct RGB BGR ordering!
"""
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def main():
    """ main function """
    # read in two images
    img1 = cv.imread('flubba1.jpg')
    img2 = cv.imread('flubba2.jpg')
    # img_color = cv.imread('flubba1.jpg')

    cols1, rows1, _channels1 = map( int, img1.shape )
    cols2, rows2, _channels2 = map( int, img2.shape )

    # get first gaussian pyramid
    img1_g1 = cv.pyrDown(img1, dstsize=(cols1 // 2, rows1 // 2))
    img2_g1 = cv.pyrDown(img2, dstsize=(cols2 // 2, rows2 // 2))

    # upsample g1
    img1_g0 = cv.pyrUp( img1_g1, dstsize=(cols1, rows1))
    img2_g0 = cv.pyrUp( img2_g1, dstsize=(cols2, rows2))

    # compute different between original and upsamples g1 to get laplacian

    img1_laplacian = img1 - img1_g0
    img2_laplacian = img2 - img2_g0

    cv.imwrite('flubba.laplacian1.jpg', img1_laplacian)
    cv.imwrite('flubba.laplacian2.jpg', img2_laplacian)

main()
