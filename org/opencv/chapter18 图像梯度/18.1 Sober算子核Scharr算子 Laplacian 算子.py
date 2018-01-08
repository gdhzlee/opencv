"""
OpenCV 提供了三种不同的梯度滤波器，或者说高通滤波器：Sobel，Scharr 和Laplacian。Sobel，Scharr 其实就是求一阶或二阶导数。
Scharr 是对Sobel（使用小的卷积核求解求解梯度角度时）的优化。Laplacian 是求二阶导数。
"""
"""
18.1 Sobel 算子和Scharr 算子 Laplacian 算子
Sobel 算子是高斯平滑与微分操作的结合体，所以它的抗噪声能力很好。可以设定求导的方向（xorder 或yorder）。
还可以设定使用的卷积核的大小（ksize）。如果ksize=-1，会使用3x3 的Scharr 滤波器，它的的效果要比3x3 的Sobel 滤波器好
（而且速度相同，所以在使用3x3 滤波器时应该尽量使用Scharr 滤波器）。3x3 的Scharr 滤波器卷积核如下：

Laplacian 算子
拉普拉斯算子可以使用二阶导数的形式定义，可假设其离散实现类似于二
阶Sobel 导数，事实上，OpenCV 在计算拉普拉斯算子时直接调用Sobel 算
子。拉普拉斯滤波器使用的卷积核：
kernel = [ 0  1  0 ]
         [ 1 -4  1 ]
         [ 1  1  0 ]
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt;

img = cv2.imread("C:\\Users\\lee\\Desktop\\1.jpg",0);
"""
cv2.Laplacian(src, ddepth[, dst[, ksize[, scale[, delta[, borderType]]]]]) → dst
Calculates the Laplacian of an image.
    src – Source image.
    ddepth – Desired depth of the destination image.
    ksize – Aperture size used to compute the second-derivative filters. See getDerivKernels() for details. The size must be positive and odd.
    scale – Optional scale factor for the computed Laplacian values. By default, no scaling is applied. See getDerivKernels() for details.
    delta – Optional delta value that is added to the results prior to storing them in dst .
    borderType – Pixel extrapolation method. See borderInterpolate for details.
"""
laplacian = cv2.Laplacian(img,cv2.CV_64F);

"""
cv2.Sobel(src, ddepth, dx, dy[, dst[, ksize[, scale[, delta[, borderType]]]]]) → dst
Calculates the first, second, third, or mixed image derivatives using an extended Sobel operator.
    src – input image.
    dst – output image of the same size and the same number of channels as src .
    ddepth –output image depth; the following combinations of src.depth() and ddepth are supported:
        src.depth() = CV_8U, ddepth = -1/CV_16S/CV_32F/CV_64F
        src.depth() = CV_16U/CV_16S, ddepth = -1/CV_32F/CV_64F
        src.depth() = CV_32F, ddepth = -1/CV_32F/CV_64F
        src.depth() = CV_64F, ddepth = -1/CV_64F
        when ddepth=-1, the destination image will have the same depth as the source; in the case of 8-bit input images it will result in truncated derivatives 截断面.
    xorder – order of the derivative x.
    yorder – order of the derivative y.
    ksize – size of the extended Sobel kernel; it must be 1, 3, 5, or 7.
"""
#参数为 1,0 只在x方法求一阶导数，最大可以求二阶导数
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5);
#参数为 0,1 只在y方法求一阶导数，最大可以求二阶导数
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5);

plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show();