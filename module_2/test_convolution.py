"""
Testing various 2D convolution methods
Important: Remember to use the correct RGB BGR ordering!
"""
# import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def main():
    """ main function """
    # read in an image
    img = cv.imread('flubba1.jpg', 0)
    img_color = cv.imread('flubba1.jpg')

    figure = plt.figure(figsize=(10, 10))

    # threshold
    threshold = 25

    # regular blur
    blur1 = cv.blur(img_color, (threshold, threshold))

    # bilateral filter
    # bf_threshold = 300
    # blur1 = cv.bilateralFilter( img_color, 9, bf_threshold, bf_threshold)

    # gaussian blur
    blur2 = cv.GaussianBlur(img_color, (threshold, threshold), 0)

    # median blur
    blur3 = cv.medianBlur( img_color, threshold)

    titles = ['Original Image', 'Blur',
              'Gaussian Blur (v = %d)' % threshold, 'Median Blur (v = %d)' % threshold,]
    images = [img_color, blur1, blur2, blur3]
    for i in xrange(4):
        plt.subplot(2, 2, i+1),plt.imshow( cv.cvtColor(images[i], cv.COLOR_BGR2RGB ) )
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    # plt.show()

    figure.savefig('flubba.blurs.jpg')

main()
