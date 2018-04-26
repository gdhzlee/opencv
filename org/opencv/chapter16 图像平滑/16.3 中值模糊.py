"""
16.3 中值模糊
顾名思义就是用与卷积框对应像素的中值来替代中心像素的值。这个滤波器经常用来去除椒盐噪声。
前面的滤波器都是用计算得到的一个新值来取代中心像素的值，而中值滤波是用中心像素周围（也可以使他本身）的值来取代他。
他能有效的去除噪声。卷积核的大小也应该是一个奇数。
"""
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("../../../resource/img/1.jpg");
"""
cv2.medianBlur(src, ksize[, dst]) → dst
Blurs an image using the median filter.
    src – input 1-, 3-, or 4-channel image; when ksize is 3 or 5, the image depth should be CV_8U, CV_16U, or CV_32F, for larger aperture sizes, it can only be CV_8U.
    ksize – aperture linear size; it must be odd and greater than 1, for example: 3, 5, 7 ...
"""
blur = cv2.medianBlur(img,9);
plt.subplot(1,2,1),plt.imshow(img),plt.title("src");
plt.xticks([])
plt.yticks([])
plt.subplot(1,2,2),plt.imshow(blur),plt.title("medianblur");
plt.xticks([])
plt.yticks([])
plt.show();