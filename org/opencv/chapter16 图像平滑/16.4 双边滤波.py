"""
16.4 双边滤波
函数cv2.bilateralFilter() 能在保持边界清晰的情况下有效的去除噪音。但是这种操作与其他滤波器相比会比较慢。
我们已经知道高斯滤波器是求中心点邻近区域像素的高斯加权平均值。这种高斯滤波器只考虑像素之间的空间关系，而不会考虑像素值之间的关系（像素的相似度）。
所以这种方法不会考虑一个像素是否位于边界。因此边界也会别模糊掉，而这正不是我们想要。

双边滤波是一种非线性的滤波方法，是结合图像的空间邻近度和像素值相似度的一种折衷处理，同时考虑空间与信息和灰度相似性，达到保边去噪的目的，具有简单、非迭代、局部处理的特点。

双边滤波在同时使用空间高斯权重和灰度值相似性高斯权重。
空间高斯函数确保只有邻近区域的像素对中心点有影响，灰度值相似性高斯函数确保只有与中心像素灰度值相近的才会被用来做模糊运算。
所以这种方法会确保边界不会被模糊掉，因为边界处的灰度值变化比较大。
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("C:\\Users\\lee\\Desktop\\1.jpg");

"""
cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace[, dst[, borderType]]) → dst
Applies the bilateral filter to an image.
    src – Source 8-bit or floating-point, 1-channel or 3-channel image.
    d – Diameter of each pixel neighborhood that is used during filtering. If it is non-positive, it is computed from sigmaSpace .
    sigmaColor – Filter sigma in the color space. A larger value of the parameter means that farther colors within the pixel neighborhood (see sigmaSpace ) will be mixed together, resulting in larger areas of semi-equal color.
    sigmaSpace – Filter sigma in the coordinate space 坐标空间. A larger value of the parameter means that farther pixels will influence each other as long as their colors are close enough (see sigmaColor ). When d>0 , it specifies the neighborhood size regardless of 与...无关 sigmaSpace . Otherwise, d is proportional 正比 to sigmaSpace .
"""
blur = cv2.bilateralFilter(img,9,75,75);

plt.subplot(1,2,1),plt.imshow(img),plt.title("src");
plt.subplot(1,2,2),plt.imshow(blur),plt.title("bilateraFilter");
plt.show();