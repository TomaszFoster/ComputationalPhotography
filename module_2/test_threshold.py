"""
Testing various threshold plotting functions on images
"""
# import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
# import matplotlib.image as mpimg

def main():
    """ main function """
    # read in an image
    img_color = cv.imread('flubba1.jpg')
    img_grayscale = cv.imread('flubba1.jpg', 0)

    figure = plt.figure(figsize=(8, 8))
    # img = cv.medianBlur(img,5)

    ths = 120
    ret, th1 = cv.threshold(img_grayscale, ths, 255, cv.THRESH_BINARY)
    th2 = cv.adaptiveThreshold(img_grayscale, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
    th3 = cv.adaptiveThreshold(img_grayscale, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
    titles = ['Original Image', 'Global Thresholding (v = %d)' % ths,
              'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
    images = [img_color, th1, th2, th3]
    for i in xrange(4):
        plt.subplot(2, 2, i+1)
        if i==0:
            plt.imshow( cv.cvtColor( images[i], cv.COLOR_BGR2RGB) )
        else:
            plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    # plt.show()

    figure.savefig('flubba.thresholds.jpg')

main()
