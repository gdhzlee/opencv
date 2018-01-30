"""
14.3 旋转
对一个图像旋转角度, 需要使用到下面形式的旋转矩阵。
    M = [ cosΘ -sinΘ ]
        [ sinΘ cosΘ ]
但是OpenCV 允许你在任意地方进行旋转，但是旋转矩阵的形式应该修改为
    M = [ α β (1-α)*center.x - β*center.y ]
        [ -β α β*center.x + (1-α)*center.y ]
            α = scale * cosΘ
            β= scale * sinΘ
为了构建这个旋转矩阵，OpenCV 提供了一个函数：cv2.getRotationMatrix2D。下面的例子是在不缩放的情况下将图像旋转90 度。
cv2.getRotationMatrix2D(center, angle, scale) → retval
Calculates an affine matrix of 2D rotation.
    center – Center of the rotation in the source image.
    angle – Rotation angle in degrees. Positive values mean counter-clockwise rotation (the coordinate origin is assumed to be the top-left corner).
    scale – Isotropic scale factor. 缩放因子
    map_matrix – The output affine transformation, 2x3 floating-point matrix.
"""
import cv2
import numpy as np

img = cv2.imread("../../../resource/img/1.jpg");
rows, cols = img.shape[:2];

M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)

dst = cv2.warpAffine(img,M,(cols,rows));
cv2.imshow("dst",dst);
cv2.waitKey(3000)