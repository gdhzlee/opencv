"""
14.2 平移
平移就是将对象换一个位置。如果你要沿（x，y）方向移动，移动的距离
是（tx，ty），你可以以下面的方式构建移动矩阵：
        [ 1 0 tx ]
    M = [ 0 1 ty ]

你可以使用Numpy 数组构建这个矩阵（数据类型是np.float32），然
后把它传给函数cv2.warpAffine()
"""
import cv2
import numpy as np

img = cv2.imread("C:\\Users\\lee\\Desktop\\1.jpg");
rows, cols = img.shape[:2];

M = np.float32([[1,0,100],[0,1,100]]);
"""
cv2.warpAffine(src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]]) → dst
Applies an affine transformation仿射变换 to an image.
Parameters:	
    src – input image.
    M – 2 * 3 transformation matrix. 变换矩阵
    dsize – size of the output image.
"""
dst = cv2.warpAffine(img, M, (cols,rows));

cv2.imshow("dst",dst);
cv2.waitKey(3000);
cv2.destroyAllWindows();

#函数cv2.warpAffine() 的第三个参数的是输出图像的大小，它的格式应该是图像的（宽，高）。应该记住的是图像的宽对应的是列数，高对应的是行数。