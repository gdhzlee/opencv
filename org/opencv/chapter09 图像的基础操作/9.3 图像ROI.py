"""
9.3 图像ROI
ROI（region of interest），感兴趣区域。机器视觉、图像处理中，从被处理的图像以方框、圆、椭圆、不规则多边形等方式勾勒出需要处理的区域，称为感兴趣区域.
ROI 也是使用Numpy 索引来获得的。现在我们选择球的部分并把他拷贝到图像的其他区域。
"""
import cv2
import numpy as np

img = cv2.imread("../../../resource/img/1.jpg")
#获取图像部分
imgPart = img[0:100,0:100]
cv2.imshow("imgPart",imgPart);
cv2.waitKey(2000)

