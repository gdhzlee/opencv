"""
21.2 轮廓特征
查找轮廓的不同特征，例如面积，周长，重心，边界框等。

"""

"""
21.2.1 矩
图像的矩可以帮助我们计算图像的质心，面积等。
"""
import cv2
import numpy as np

img = cv2.imread("C:\\Users\\lee\\Desktop\\3.jpg",0);
ret, thresh = cv2.threshold(img, 127, 255, 0);
image, contours, hierarchy = cv2.findContours(thresh, 1, 2);

cnt = contours[0];
M = cv2.moments(cnt);
print("轮廓的矩："+str(M));

#根据这些矩的值，我们可以计算出对象的重心：
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print("轮廓重心：cx = "+str(cx)+", cy = "+ str(cy));
img = cv2.line(img, (cx, cy), (cx, cy), (0, 255, 0), 5);
# cv2.imshow("img", img);cv2.waitKey(3000)
"""
21.2.2 轮廓面积
轮廓的面积可以使用函数cv2.contourArea() 计算得到，也可以使用矩（0 阶矩），M['m00']。
"""
area = cv2.contourArea(cnt);
print("轮廓面积："+ str(area));

"""
21.2.3 轮廓周长
也被称为弧长。可以使用函数cv2.arcLength() 计算得到。这个函数的第二参数可以用来指定对象的形状是闭合的（True），还是打开的（一条曲线）。
"""
perimeter = cv2.arcLength(cnt, True);
print("轮廓周长："+str(perimeter));

"""
21.2.4 轮廓近似
将轮廓形状近似到另外一种由更少点组成的轮廓形状，新轮廓的点的数目由我们设定的准确度来决定。
为了帮助理解，假设我们要在一幅图像中查找一个矩形，但是由于图像的种种原因，我们不能得到一个完美的矩形，而是一个“坏形状”（如下图所示）。
现在你就可以使用这个函数来近似这个形状（）了。这个函数的第二个参数叫epsilon，它是从原始轮廓到近似轮廓的最大距离。它是一个准确度参数。
选择一个好的epsilon 对于得到满意结果非常重要。
cv2.approxPolyDP(curve, epsilon, closed[, approxCurve]) → approxCurve
    curve – Input vector of a 2D point stored in:
        std::vector or Mat (C++ interface)
        Nx2 numpy array (Python interface)
        CvSeq or `` CvMat (C interface)
    approxCurve – Result of the approximation. The type should match the type of the input curve. In case of C interface the approximated curve is stored in the memory storage and pointer to it is returned.
    epsilon – Parameter specifying the approximation accuracy. This is the maximum distance between the original curve and its approximation.
    closed – If true, the approximated curve is closed (its first and last vertices are connected). Otherwise, it is not closed.
"""
epsilon = 0.1*perimeter;
approx = cv2.approxPolyDP(cnt, epsilon, True);

image = img.copy();
for contour in contours:
    cnt = contour;
    perimeter = cv2.arcLength(cnt,True);
    epsilon = 0.1* perimeter;
    approx = cv2.approxPolyDP(cnt, epsilon, True);
    cv2.drawContours(image, approx, -1,(0, 0, 255),5 );

cv2.imshow("img", image);
cv2.waitKey(3000);