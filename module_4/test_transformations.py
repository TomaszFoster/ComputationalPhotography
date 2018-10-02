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
    # mask_source = cv.imread('ap-logo.jpg')

    # cv.namedWindow('Original')
    # cv.imshow('Original', img)

    cols, rows, _channels = map(int, img.shape)
    
    # Translations:
    #     | 1 0 x | where x = 100
    # M = | 0 1 y | where y =  50

    # M = np.float32([[1, 0, 100], [0, 1, 50]])
    # dst = cv.warpAffine(img, M, (cols, rows))

    # Rotations:
    #     | cos(theta) -sin(theta) | 
    # M = | sintheta  costheta | 
    # 
    # alternatively OpenCV provides scaled rotation with adjustable center of rotation
    #
    # |  alpha   beta  (1-alpha)*center.x - beta*center.y  |
    # | -beta   alpha  beta*center.x + (1-alpha)*center.y  |
    #
    # where:
    # alpha = scale*costheta
    # beta = scale*sintheta

    # M = cv.getRotationMatrix2D(((cols-1)/2.0, (rows-1)/2.0), 45, 1)
    # dst = cv.warpAffine(img, M, (cols, rows))

    # Perspective transformation

    pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
    pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

    M = cv.getPerspectiveTransform(pts1, pts2)

    dst = cv.warpPerspective(img, M, (300, 300))

    plt.subplot(121), plt.imshow(img), plt.title('Input')
    plt.subplot(122), plt.imshow(dst), plt.title('Output')
    plt.show()

    # cv.namedWindow('Modified')
    # cv.imshow('Modified', dst)

    cv.waitKey(0)
    # cvReleaseImage(&img);
    return 0
    
main()
