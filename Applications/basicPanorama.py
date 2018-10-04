"""
Testing a basic panorama
"""
import numpy as np
import cv2 as cv

def main():
    """ main function """
    
    # read images
    img1 = cv.imread('flubba.left.jpg' )
    img2 = cv.imread('flubba.right.jpg' )

    # convert to grayscale
    img1_gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
    img2_gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

    # init our Orb detector
    orb = cv.ORB_create()

    # find keypoints, compute descriptors, 
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    img1_kp1 = cv.drawKeypoints(img1, kp1, outImage=None, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    img2_kp2 = cv.drawKeypoints(img2, kp2, outImage=None, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # match keypoints using BF matcher
    bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)

    print "{} matches found".format(len(matches))

    # create two sequences of corresponding matched points
    pts1 = []
    pts2 = []

    # get the matching keypoints for each of the images
    for mat in matches:
        pts1.append(kp1[mat.queryIdx].pt)
        pts2.append(kp2[mat.trainIdx].pt)

    pts1 = np.asarray(pts1, dtype=np.float32)
    pts2 = np.asarray(pts2, dtype=np.float32)

    # compute homography using RANSAC to reject outliers
    M_homograph, inliers = cv.findHomography( pts2, pts1, cv.RANSAC )

    print M_homograph

    # create panorama
    pano_size = ( int(M_homograph[0, 2] + img2.shape[1]), max( img1.shape[0], img2.shape[0] ) )
    # apply transforms
    print img1.shape
    print img2.shape
    print pano_size
    img_pano = cv.warpPerspective( img2, M_homograph, pano_size )
    # copy pixels from img1 to img2 (with visible seams)
    img_pano[0:img1.shape[0], 0:img1.shape[1], :] = img1
    cv.imwrite("flubba.pano.jpg", img_pano)
    
main()
