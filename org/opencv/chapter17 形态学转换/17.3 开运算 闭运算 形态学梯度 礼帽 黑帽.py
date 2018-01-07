"""
17.3 开运算 闭运算 形态学梯度 礼帽 黑帽

cv2.morphologyEx(src, op, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]]) → dst
Performs advanced morphological transformations.
    src – Source image. The number of channels can be arbitrary. The depth should be one of CV_8U, CV_16U, CV_16S, CV_32F` or ``CV_64F.
    kernel – Structuring element. It can be created using getStructuringElement().
    op –Type of a morphological operation that can be one of the following:
        MORPH_OPEN - an opening operation
        MORPH_CLOSE - a closing operation
        MORPH_GRADIENT - a morphological gradient
        MORPH_TOPHAT - “top hat”
        MORPH_BLACKHAT - “black hat”
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("C:\\Users\\lee\\Desktop\\4.jpg");

kernel = np.ones((5,5),np.uint8);
#先进性腐蚀再进行膨胀就叫做开运算。就像我们上面介绍的那样，它被用来去除噪声。
opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel);
#先膨胀再腐蚀。它经常被用来填充前景物体中的小洞，或者前景物体上的小黑点。
closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel);
#其实就是一幅图像膨胀与腐蚀的差。结果看上去就像前景物体的轮廓。
gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel);
#原始图像与进行开运算之后得到的图像的差。
tophat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel);
#进行闭运算之后得到的图像与原始图像的差。
blackhat = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel);

plt.subplot(2,3,1),plt.imshow(img),plt.title("src");
plt.subplot(2,3,2),plt.imshow(opening),plt.title("opening");
plt.subplot(2,3,3),plt.imshow(closing),plt.title("closing");
plt.subplot(2,3,4),plt.imshow(gradient),plt.title("gradient");
plt.subplot(2,3,5),plt.imshow(tophat),plt.title("tophat");
plt.subplot(2,3,6),plt.imshow(blackhat),plt.title("blackhat");
plt.show();

"""
Opening: dst = open(src,element)=dilate(erode(src,element),element);
Closing: dst = close(src,element)=erode(dilate(src,element),element);
Morphological: dst = morph_grad(src,element) = dilate(src,element) - erode(src,element);
top hat: dst = tophat(src,element) = src - open(src,element)
black hat: dst = blackhat(src,element) = close(src,element) - src
"""