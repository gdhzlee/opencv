"""
14.4 仿射变换
在仿射变换中，原图中所有的平行线在结果图像中同样平行。为了创建这个矩阵我们需要从原图像中找到三个点以及他们在输出图像中的位置。
然后cv2.getAffineTransform 会创建一个2x3 的矩阵，最后这个矩阵会被传给函数cv2.warpAffine。
Calculates an affine transform from three pairs of the corresponding平行 points.
cv2.getAffineTransform(src, dst) → retval
    src – Coordinates of triangle vertices in the source image.
    dst – Coordinates of the corresponding triangle vertices in the destination image.
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("C:\\Users\\lee\\Desktop\\1.jpg");
rows, cols = img.shape[:2];

pts1 = np.float32([[10,10],[10,200],[200,10]]);
pts2 = np.float32([[2,20],[20,250],[200,10]]);

M = cv2.getAffineTransform(pts1,pts2);
dst = cv2.warpAffine(img,M,(cols,rows));

plt.subplot(121),plt.imshow(img),plt.title("src");
plt.subplot(122),plt.imshow(dst),plt.title("dst");
plt.show();