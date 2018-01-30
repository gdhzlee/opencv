"""
16.1 平均
这是由一个归一化卷积框完成的。他只是用卷积框覆盖区域所有像素的平均值来代替中心元素。
可以使用函数cv2.blur() 和cv2.boxFilter() 来完这个任务。
可以同看查看文档了解更多卷积框的细节。我们需要设定卷积框的宽和高。
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("../../../resource/img/1.jpg");

"""
cv2.blur(src, ksize[, dst[, anchor[, borderType]]]) → dst
Blurs an image using the normalized box filter 归一化滤波器.
    src – input image; it can have any number of channels, which are processed independently, but the depth should be CV_8U, CV_16U, CV_16S, CV_32F or CV_64F.
    ksize – blurring kernel size.
"""
blur = cv2.blur(img,(5,5));

plt.subplot(1,2,1),plt.imshow(img),plt.title("src");
plt.subplot(1,2,2),plt.imshow(blur),plt.title("blur");
plt.show();
