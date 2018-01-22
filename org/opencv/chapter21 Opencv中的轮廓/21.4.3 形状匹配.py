"""
21.4.3 形状匹配
函数cv2.matchShape() 可以帮我们比较两个形状或轮廓的相似度。如果返回值越小，匹配越好。它是根据Hu 矩来计算的。文档中对不同的方法都有解释。
cv2.matchShapes(contour1, contour2, method, parameter) → retval
    object1 – First contour or grayscale image.
    object2 – Second contour or grayscale image.
    method – Comparison method: CV_CONTOURS_MATCH_I1 , CV_CONTOURS_MATCH_I2 or CV_CONTOURS_MATCH_I3 (see the details below).
    parameter – Method-specific parameter (not supported now).
"""
import cv2
import numpy as np

img1 = cv2.imread("../../../resource/img/4.jpg");
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY);
img2 = gray.copy();

ret, thresh1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY);
ret, thresh2 = cv2.threshold(img2, 127, 255, cv2.THRESH_BINARY);

ret = cv2.matchShapes(thresh1, thresh2, 1,0.0);
print(ret);

"""
Hu 矩是归一化中心矩的线性组合，之所以这样做是为了能够获取代表图像的某个特征的矩函数，
这些矩函数对某些变化如缩放，旋转，镜像映射（除了h1）具有不变形。此段摘自《学习OpenCV》中文版。
"""

