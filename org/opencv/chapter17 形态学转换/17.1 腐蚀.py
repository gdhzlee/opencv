"""
17.1 腐蚀
就像土壤侵蚀一样，这个操作会把前景物体的边界腐蚀掉（但是前景仍然是白色）。
这是怎么做到的呢？卷积核沿着图像滑动，如果与卷积核对应的原图像的所有像素值都是1，那么中心元素就保持原来的像素值，否则就变为零。
这回产生什么影响呢？根据卷积核的大小靠近前景的所有像素都会被腐蚀掉（变为0），所以前景物体会变小，整幅图像的白色区域会减少。
这对于去除白噪声很有用，也可以用来断开两个连在一块的物体等。
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("C:\\Users\\lee\\Desktop\\4.jpg");

kernal = np.ones((5,5),np.uint8);
"""
cv2.erode(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]]) → dst
Erodes an image by using a specific structuring element.
    src – input image; the number of channels can be arbitrary, 
        but the depth should be one of CV_8U, CV_16U, CV_16S, CV_32F` or ``CV_64F.
    kernel – structuring element used for erosion; if element=Mat() , a 3 x 3 rectangular structuring element is used. Kernel can be created using getStructuringElement().
    iterations – number of times erosion is applied.
"""
erosion = cv2.erode(img,kernal,1);

plt.subplot(1,2,1),plt.imshow(img),plt.title("src");
plt.subplot(1,2,2),plt.imshow(erosion),plt.title("erosion");
plt.show();