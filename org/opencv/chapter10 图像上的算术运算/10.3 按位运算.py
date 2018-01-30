"""
10.3 按位运算
这里包括的按位操作有：AND，OR，NOT，XOR 等。当我们提取图像的
一部分，选择非矩形ROI 时这些操作会很有用（下一章你就会明白）。下面的
例子就是教给我们如何改变一幅图的特定区域。
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread("../../../resource/img/1.jpg")
img2 = img1[100,200,0:100]

"""
cv2.threshold(src, thresh, maxval, type[, dst]) → retval, dst
Parameters:	
    src – input array (single-channel, 8-bit or 32-bit floating point).
    dst – output array of the same size and type as src.
    thresh – threshold value.阈值
    maxval – maximum value to use with the THRESH_BINARY and THRESH_BINARY_INV thresholding types.
    type – thresholding type (see the details below).
        • cv2.THRESH_BINARY（黑白二值） 
        • cv2.THRESH_BINARY_INV（黑白二值反转） 
        • cv2.THRESH_TRUNC （得到的图像为多像素值） 
        • cv2.THRESH_TOZERO 
        • cv2.THRESH_TOZERO_INV 
像素高于阈值时，给像素赋予新值，否则，赋予另外一种颜色。作用：用于获取二元值的灰度图像 
图像的阈值处理一般使得图像的像素值更单一、图像更简单。阈值可以分为全局性质的阈值，也可以分为局部性质的阈值，可以是单阈值的也可以是多阈值的。
"""
ret,thresh1 = cv2.threshold(img1,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img1,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img1,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img1,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img1,127,255,cv2.THRESH_TOZERO_INV)
images = [img1,thresh1,thresh2,thresh3,thresh4,thresh5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],"gray")
    plt.title(i)
    #plt.xticks([]),plt.yticks([])
plt.show()
cv2.waitKey(3000)
plt.close()

"""
cv2.bitwise_not(src[, dst[, mask]]) → dst
Inverts every bit of an array.
Parameters:	
src – input array.
dst – output array that has the same size and type as the input array.
mask – optional operation mask, 8-bit single channel array, that specifies elements of the output array to be changed.
"""
cv2.imshow("bitwise_not",cv2.bitwise_not(img1))
cv2.waitKey(2000)

"""
cv2.bitwise_and(src1, src2[, dst[, mask]]) → dst
Calculates the per-element bit-wise conjunction of two arrays or an array and a scalar.
Parameters:	
    src1 – first input array or a scalar.
    src2 – second input array or a scalar.
    src – single input array.
    value – scalar value.
    dst – output array that has the same size and type as the input arrays.
    mask – optional operation mask, 8-bit single channel array, that specifies elements of the output array to be changed.
    The function calculates the per-element bit-wise logical conjunctio
"""
img1 = cv2.imread("../../../resource/img/1.jpg")
img2 = cv2.imread("../../../resource/img/2.jpg")
cv2.imshow("bitwise_and",cv2.bitwise_and(img1,img2))
cv2.waitKey(2000)

img1 = cv2.imread("../../../resource/img/1.jpg")
img2 = cv2.imread("../../../resource/img/3.jpg")
rows,cols,channels = img2.shape;
roi = img1[0:rows,0:cols]

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
cv2.imshow("img2gray",img2gray);cv2.waitKey(1000)
ret, mask = cv2.threshold(img2gray,175,255,cv2.THRESH_BINARY)
cv2.imshow("mask",mask);cv2.waitKey(1000)
mask_inv = cv2.bitwise_not(mask)
cv2.imshow("mask_inv",mask_inv);cv2.waitKey(2000)

img1_bg = cv2.bitwise_and(roi,roi,mask=mask)
cv2.imshow("img1_bg",img1_bg);cv2.waitKey(1000)
img2_fg = cv2.bitwise_and(img2,img2,mask=mask_inv)
cv2.imshow("img1_fg",img2_fg);cv2.waitKey(1000)

dst = cv2.add(img1_bg,img2_fg)
cv2.imshow("dst",dst);cv2.waitKey(1000)

img1[0:rows,0:cols] = dst;
cv2.imshow("res",img1);cv2.waitKey(10000)
