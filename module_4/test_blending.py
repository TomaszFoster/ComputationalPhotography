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

    # figure = plt.figure(figsize=(10, 10))

    # # threshold
    # threshold = 25

    # # regular blur
    # blur1 = cv.blur(img_color, (threshold, threshold))

    # # bilateral filter
    # # bf_threshold = 300
    # # blur1 = cv.bilateralFilter( img_color, 9, bf_threshold, bf_threshold)

    # # gaussian blur
    # blur2 = cv.GaussianBlur(img_color, (threshold, threshold), 0)

    # # median blur
    # blur3 = cv.medianBlur( img_color, threshold)

    # titles = ['Original Image', 'Blur',
    #           'Gaussian Blur (v = %d)' % threshold, 'Median Blur (v = %d)' % threshold,]
    # images = [img1, img2, blur1, blur2, blur3]
    # for i in xrange(4):
    #     plt.subplot(2, 2, i+1),plt.imshow( cv.cvtColor(images[i], cv.COLOR_BGR2RGB ) )
    #     plt.title(titles[i])
    #     plt.xticks([]),plt.yticks([])
    # # plt.show()

    # figure.savefig('flubba.g0.jpg')

main()
