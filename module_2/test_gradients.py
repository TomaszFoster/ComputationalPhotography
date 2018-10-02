"""
Testing various gradient methods
Important: Remember to use the correct RGB BGR ordering!
"""
# import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def main():
    """ main function """

    # read in an image in grayscale
    img = cv.imread('flubba1.jpg', 0)

    # read in a color version of the image
    img_color = cv.imread('flubba1.jpg')

    # create a figure so we can save it to a file later; size is in inches
    figure = plt.figure(figsize=(10, 10))

    # threshold
    threshold = 31

    # laplacian
    laplacian = cv.Laplacian( img, cv.CV_64F, ksize=threshold) 

    # sobel x and y
    sobelx = cv.Sobel( img, cv.CV_64F, 1, 0, ksize=threshold)
    sobely = cv.Sobel( img, cv.CV_64F, 0, 1, ksize=threshold)

    titles = ['Original Image', 'Laplacian Gradient',
              'Sobel X Gradient', 'Sobel Y Gradient']
    images = [img, laplacian, sobelx, sobely]
    for i in xrange(4):
        plt.subplot(2, 2, i+1)
        plt.imshow( images[i], cmap='gray' )
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    # plt.show()

    figure.savefig('flubba.gradients.jpg')

main()
