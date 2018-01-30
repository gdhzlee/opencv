"""
13.5 自适应阈值化
In the previous section, we used a global value as threshold value. But it may not be good in all the conditions where
image has different lighting conditions in different areas. In that case, we go for adaptive thresholding. In this, the
algorithm calculate the threshold for a small regions of the image. So we get different thresholds for different regions
of the same image and it gives us better results for images with varying illumination.
It has three ‘special’ input params and only one output argument.
cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst]) → dst
    Adaptive Method - It decides how thresholding value is calculated.
        • cv2.ADAPTIVE_THRESH_MEAN_C : threshold value is the mean of neighbourhood area.
        • cv2.ADAPTIVE_THRESH_GAUSSIAN_C : threshold value is the weighted sum of neighbourhood values
                where weights are a gaussian window.
    Block Size - It decides the size of neighbourhood area.
    C - It is just a constant which is subtracted from the mean or weighted mean calculated.
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
"""
Flags specifying the color type of a loaded image:
    CV_LOAD_IMAGE_ANYDEPTH - If set, return 16-bit/32-bit image when the input has the corresponding depth, otherwise convert it to 8-bit.
    CV_LOAD_IMAGE_COLOR - If set, always convert image to the color one
    CV_LOAD_IMAGE_GRAYSCALE - If set, always convert image to the grayscale one
    >0 Return a 3-channel color image.
    =0 Return a grayscale image.
    <0 Return the loaded image as is (with alpha channel).
"""
img = cv2.imread("../../../resource/img/1.jpg",0);
"""
使用中值滤波消除噪点
cv2.medianBlur(src, ksize[, dst]) → dst
    ksize – aperture linear size孔径线性尺寸; it must be odd奇数 and greater than 1, for example: 3, 5, 7 ...
"""
img = cv2.medianBlur(img,5)

ret, th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

titles = ['Original Image', 'Global Thresholding (v = 127)',
'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],"gray");
    plt.title(titles[i]);
    plt.xticks([]),plt.yticks([])
plt.show()