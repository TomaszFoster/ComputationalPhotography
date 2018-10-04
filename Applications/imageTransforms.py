"""
Testing various 2D convolution methods
Important: Remember to use the correct RGB BGR ordering!
"""
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def main():
    """ main function """
    
    img = cv.imread('flubba.zoom.jpg' )
    height, width = img.shape[:2]

    # perspective transform
    pts1 = np.float32([ [220, 85], [ 223, 414], [602, 190], [616, 323] ])
    pts2 = np.float32([ [75, 75], [ 72, 225], [500, 75], [500, 225] ])

    m_persp = cv.getPerspectiveTransform(pts1, pts2)
    img2 = cv.warpPerspective( img, m_persp, ( height/2, width/2 ))

    cv.imwrite("flubba.perspective.jpg", img2)
    
main()
