"""
17.2 膨胀
与腐蚀相反，与卷积核对应的原图像的像素值中只要有一个是1，中心元素的像素值就是1。
所以这个操作会增加图像中的白色区域（前景）。一般在去噪声时先用腐蚀再用膨胀。
因为腐蚀在去掉白噪声的同时，也会使前景对象变小。
所以我们再对他进行膨胀。这时噪声已经被去除了，不会再回来了，但是前景还在并会增加。膨胀也可以用来连接两个分开的物体。
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("../../../resource/img/4.jpg");

kernal = np.ones((5,5),np.uint8);
erosion = cv2.erode(img,kernal,1);
"""
cv2.dilate(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]]) → dst
Dilates an image by using a specific structuring element.
    src – input image; the number of channels can be arbitrary, but the depth should be one of CV_8U, CV_16U, CV_16S, CV_32F` or ``CV_64F.
    kernel – structuring element used for dilation; if elemenat=Mat() , a 3 x 3 rectangular structuring element is used. Kernel can be created using getStructuringElement()
    iterations – number of times dilatiionon is applied.
"""
dilation = cv2.dilate(erosion,kernal,1);

plt.subplot(1,3,1),plt.imshow(img),plt.title("src");
plt.subplot(1,3,2),plt.imshow(erosion),plt.title("erosion");
plt.subplot(1,3,3),plt.imshow(dilation),plt.title("dilat");
plt.show();