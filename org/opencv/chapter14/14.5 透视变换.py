"""
14.5 透视变换
对于视角变换，我们需要一个3x3 变换矩阵。在变换前后直线还是直线。要构建这个变换矩阵，你需要在输入图像上找4 个点，以及他们在输出图像上对应的位置。
这四个点中的任意三个都不能共线。这个变换矩阵可以有函数cv2.getPerspectiveTransform() 构建。然后把这个矩阵传给函数cv2.warpPerspective。
cv2.getPerspectiveTransform(src, dst) → retval
    Parameters:
    src – Coordinates of quadrangle vertices in the source image.
    dst – Coordinates of the corresponding quadrangle vertices in the destination image.

cv2.warpPerspective(src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]]) → dst
    src – input image.
    dst – output image that has the size dsize and the same type as src .
    M – 3\times 3 transformation matrix.
    dsize – size of the output image.
"""
#TODO
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("C:\\Users\\lee\\Desktop\\1.jpg");
rows, cols = img.shape[:2];

cv2.imshow("dst",img[0:int(rows/2)+9,230:350])
cv2.waitKey(3000)
print(int(rows/2)+9);
x1 = 230;x2=350;
y1 = 0;y2=136

pts1 = np.float32([[x1,y1],[x2,y1],[x1,y2],[x2,y2]]);
pts2 = np.float32([[0,0],[0,300],[0,300],[300,300]]);

M = cv2.getPerspectiveTransform(pts1,pts2);
dst = cv2.warpPerspective(img,M,(300,300));
cv2.imshow("dst",dst);
cv2.waitKey(3000);