"""
19.1 Canny边缘检测原理
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("../../../resource/img/1.jpg",0);

#19.1.1 噪声去除
#由于边缘检测很容易受到噪声影响，所以第一步是使用5x5 的高斯滤波器去除噪声
img = cv2.GaussianBlur(img, (5, 5), 0);
cv2.imshow("after Gaussian",img);
cv2.waitKey(1000);

#19.1.2 计算图像梯度
"""
对平滑后的图像使用Sobel 算子计算水平方向和竖直方向的一阶导数（图
像梯度）（Gx 和Gy）。根据得到的这两幅梯度图（Gx 和Gy）找到边界的梯
度和方向.梯度的方向一般总是与边界垂直。梯度方向被归为四类：垂直，水平，和
两个对角线。

"""
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5 );
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5 );
cv2.imshow("after sobelx", sobelx)
cv2.imshow("after sobely", sobely);
cv2.waitKey(1000)


