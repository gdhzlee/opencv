"""
13.4 简单阈值化
Here, the matter is straight forward. If pixel value 像素值is greater than a threshold value, it is assigned one value (may be
white), else it is assigned another value (may be black).
cv2.threshold(src, thresh, maxval, type[, dst]) → retval, dst
    First argument is thesource image, which should be a grayscale image.
    Second argument is the threshold value which is used to classify the pixel values.
    Third argument is the maxVal which represents the value to be given if pixel value is more than(sometimes less than) the threshold value.
    OpenCV provides different styles of thresholding and it is decided by thefourth parameter of the function. Different types are:
        • cv2.THRESH_BINARY
        • cv2.THRESH_BINARY_INV
        • cv2.THRESH_TRUNC
        • cv2.THRESH_TOZERO
        • cv2.THRESH_TOZERO_INV
    Two outputs are obtained. First one is a retval which will be explained later. Second output is our thresholded image.
"""
import cv2
import numpy as np

img = cv2.imread("C:\\Users\\lee\\Desktop\\1.jpg");
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, threshold = cv2.threshold(img, 127,255,cv2.THRESH_BINARY);

cv2.imshow("threshold",threshold);
cv2.waitKey(1000);

