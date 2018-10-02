"""
Testing edge detection
Important: Remember to use the correct RGB BGR ordering!
"""
# import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def main():
    """ main function """

    # read in an image in grayscale
    img = cv.imread('flubba1.jpg', 0)

    img = cv.GaussianBlur( img, (9, 9), 0)

    # read in a color version of the image
    # img_color = cv.imread('flubba1.jpg')

    # create a figure so we can save it to a file later; size is in inches
    figure = plt.figure(figsize=(10,10))

    # # threshold
    # threshold = 25
    img_edge = cv.Canny(img, 50, 50)

    titles = ['Original Image', 'Edge Image']
    images = [img, img_edge]
    for i in xrange(2):
        plt.subplot(2, 2, i+1)
        plt.imshow( images[i],'gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    # plt.show()

    figure.savefig('flubba.edges.jpg')

main()
