"""
16.0 2D卷积
与以为信号一样，我们也可以对2D 图像实施低通滤波（LPF），高通滤波（HPF）等。LPF 帮助我们去除噪音，模糊图像。HPF 帮助我们找到图像的边缘
OpenCV 提供的函数cv.filter2D() 可以让我们对一幅图像进行卷积操作。
图像中的卷积：图像f（x），模板g（x），然后将模板g（x）在图像中移动，每到一个位置，就把f（x）与g（x）的定义域香蕉的袁术进行乘积并且求和，
得出新的图像一点，就是被卷积后的图像，模板就又被称为卷积核。卷积核做一个矩阵的的形状。
cv2.filter2D(src, ddepth, kernel[, dst[, anchor[, delta[, borderType]]]]) → dst
    src – input image.
    dst – output image of the same size and the same number of channels as src.
    ddepth –desired depth of the destination image; if it is negative, it will be the same as src.depth();
            the following combinations of src.depth() and ddepth are supported:
                src.depth() = CV_8U, ddepth = -1/CV_16S/CV_32F/CV_64F
                src.depth() = CV_16U/CV_16S, ddepth = -1/CV_32F/CV_64F
                src.depth() = CV_32F, ddepth = -1/CV_32F/CV_64F
                src.depth() = CV_64F, ddepth = -1/CV_64F
            when ddepth=-1, the output image will have the same depth as the source.
    kernel – convolution kernel卷积内核 (or rather a correlation kernel), a single-channel floating point matrix; if you want to apply different kernels to different channels, split the image into separate color planes using split() and process them individually.

其实核是一组权重，它决定如何通过邻近像素点来计算新的像素点。核也称为卷积矩阵，它对一个区域的像素做调和或核卷积运算。
opencv预定义了许多滤波器（滤波函数）都会只用核，通常基于核的滤波器（滤波函数）被称为卷积滤波器（滤波函数）。
卷积矩阵是一个二维数组，有奇数行，奇数列，中心的元素对应于感兴趣的像素，其他像素对应于这个像素周围的邻近像素，
每个元素都有一个整数或浮点数的值，这些值就是应用在像素值上的权重。例如：
kernal = numpy.array([[-1,-1,-1],
                      [-1, 9,-1],
                      [-1,-1,-1]])
上面实例中感兴趣的像素权重为9，期邻近像素权重为-1。对于感兴趣的像素来说，新像素值是用当前像素乘以9，然后减去8个邻近像素值。
这样会让图像锐化，因为该像素的值于邻近的像素的值之间的差距拉大了。
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("C:\\Users\\lee\\Desktop\\1.jpg");

"""
平均滤波器
创建一个5 x 5 的平均滤波器
kernal = np.ones((5,5),np.float32)/25
"""
"""
numpy.ones(shape, dtype=None, order='C')
Return a new array of given shape and type, filled with ones.
    shape : int or sequence of ints. Shape of the new array, e.g., (2, 3) or 2.
    dtype : data-type, optional. The desired data-type for the array, e.g., numpy.int8. Default is numpy.float64.
    order : {‘C’, ‘F’}, optional. Whether to store multidimensional data in C- or Fortran-contiguous (row- or column-wise) order in memory.
"""
kernal = np.ones((5,5),np.float32)/25
"""
将核放在图像的一个像素A 上，求与核对应的图像上25（5x5）个像素的和，在取平均数，用这个平均数替代像素A 的值。
重复以上操作直到将图像的每一个像素值都更新一边。
"""
dst = cv2.filter2D(img,-1,kernal)

plt.subplot(1,2,1),plt.imshow(img),plt.title("src");
plt.subplot(1,2,2),plt.imshow(dst),plt.title("dst");
plt.show();