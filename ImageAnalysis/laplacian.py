"""
Testing various 2D blending using Gaussian and Laplace pyramids
"""
import numpy as np, sys
import cv2 as cv
import matplotlib.pyplot as plt

def main():
    """ main function """

    img1 = cv.imread('flubba1.jpg')
    img2 = cv.imread('flubba2.jpg')

    # generate Gaussian pyramid for img1
    gaussian = img1.copy()
    gaussian_pyramid1 = [gaussian]
    for i in xrange(6):
        gaussian = cv.pyrDown(gaussian)
        gaussian_pyramid1.append(gaussian)

    # generate Gaussian pyramid for img2
    gaussian = img2.copy()
    gaussian_pyramid2 = [gaussian]
    for i in xrange(6):
        gaussian = cv.pyrDown(gaussian)
        gaussian_pyramid2.append(gaussian)

    # generate Laplacian Pyramid for img1
    laplacian_pyramid1 = [gaussian_pyramid1[5]]
    for i in xrange(5, 0, -1):
        gaussian_expanded = cv.pyrUp(gaussian_pyramid1[i])
        laplacian_level = cv.subtract( gaussian_pyramid1[i-1], gaussian_expanded )
        laplacian_pyramid1.append(laplacian_level)

    # generate Laplacian Pyramid for img2
    laplacian_pyramid2 = [gaussian_pyramid2[5]]
    for i in xrange(5, 0, -1):
        gaussian_expanded = cv.pyrUp(gaussian_pyramid2[i])
        laplacian_level = cv.subtract(gaussian_pyramid2[i-1], gaussian_expanded)
        laplacian_pyramid2.append(laplacian_level)

    # Now add left and right halves of images in each level
    levels = []
    for laplacian_a, laplacian_b in zip(laplacian_pyramid1, laplacian_pyramid2):
        _rows, cols, _dpt = laplacian_a.shape
        level = np.hstack((laplacian_a[:, 0:cols/2], laplacian_b[:, cols/2:]))
        levels.append(level)
    # now reconstruct
    ls_ = levels[0]
    for i in xrange(1, 6):
        ls_ = cv.pyrUp(ls_)
        ls_ = cv.add(ls_, levels[i])
    # image with direct connecting each half
    real = np.hstack((img1[:, :cols/2], img2[:, cols/2:]))
    cv.imwrite('Pyramid_blending2.jpg', ls_)
    cv.imwrite('Direct_blending.jpg', real)
    
main()
