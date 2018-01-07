"""
16.2 高斯模糊
现在把卷积核换成高斯核（简单来说，方框不变，将原来每个方框的值是相等的，
现在里面的值是符合高斯分布的，方框中心的值最大，其余方框根据距离中心元素的距离递减，构成一个高斯小山包。
原来的求平均数现在变成求加权平均数，全就是方框里的值）

实现的函数是cv2.GaussianBlur()。我们需要指定高斯核的宽和高（必须是奇数）。以及高斯函数沿X，Y 方向的标准差。
如果我们只指定了X 方向的的标准差，Y 方向也会取相同值。如果两个标准差都是0，那么函数会根据核函数的大小自己计算。高斯滤波可以有效的从图像中去除高斯噪音。


如果你愿意的话，你也可以使用函数cv2.getGaussianKernel() 自己构建一个高斯核。
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("C:\\Users\\lee\\Desktop\\1.jpg");

"""
cv2.GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]]) → dst
    src – input image; the image can have any number of channels, 
            which are processed independently, but the depth should be CV_8U, CV_16U, CV_16S, CV_32F or CV_64F.
    ksize – Gaussian kernel size. ksize.width and ksize.height can differ but they both must be positive and odd. Or, they can be zero’s and then they are computed from sigma* .
    sigmaX – Gaussian kernel standard deviation in X direction.
    sigmaY – Gaussian kernel standard deviation in Y direction; if sigmaY is zero, it is set to be equal to sigmaX, if both sigmas are zeros, they are computed from ksize.width and ksize.height , respectively (see getGaussianKernel() for details); to fully control the result regardless of possible future modifications of all this semantics, it is recommended to specify all of ksize, sigmaX, and sigmaY.
"""
blur = cv2.GaussianBlur(img,(5,5),0);

plt.subplot(1,2,1),plt.imshow(img),plt.title("src");
plt.subplot(1,2,2),plt.imshow(blur),plt.title("Gaussianblur");
plt.show();