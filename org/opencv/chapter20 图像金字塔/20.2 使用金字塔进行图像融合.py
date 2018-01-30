"""
20.2 使用金字塔进行图像融合
图像金字塔的一个应用是图像融合。例如，在图像缝合中，你需要将两幅图叠在一起，但是由于连接区域图像像素的不连续性，
整幅图的效果看起来会很差。这时图像金字塔就可以排上用场了，他可以帮你实现无缝连接。
"""
import cv2
import numpy as np,sys

A = cv2.imread("../../../resource/img/5.png");
B = cv2.imread("../../../resource/img/6.png");

G = A.copy();
gpA = [G];
for i in range(6):
    G = cv2.pyrDown(G)
    gpA.append(G);

G = B.copy();
gpB = [G];
for i in range(6):
    G = cv2.pyrDown(G);
    gpB.append(G);


"""
cv2.subtract(src1, src2[, dst[, mask[, dtype]]]) → dst
Calculates the per-element difference between two arrays or array and a scalar.
    src1 – first input array or a scalar.
    src2 – second input array or a scalar.
    dst – output array of the same size and the same number of channels as the input array.
    mask – optional operation mask; this is an 8-bit single channel array that specifies elements of the output array to be changed.
    dtype – optional depth of the output array (see the details below).
"""

#range(start, end , scan)
lpA = [gpA[5]];
for i in range(5, 0, -1):
    GE = cv2.pyrUp(gpA[i]);
    L = cv2.subtract(gpA[i-1], GE);
    lpA.append(L);

lpB = [gpB[5]];
for i in range(5, 0, -1):
    GE = cv2.pyrUp(gpB[i]);
    L = cv2.subtract(gpB[i-1], GE);
    lpB.append(L);
    print(i-1);

#TODO The operation is neither 'array op array' (where arrays have the same size and the same number of channels), nor 'array op scalar', nor 'scalar op array' in function cv::arithm_op

