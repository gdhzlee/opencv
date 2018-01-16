"""
21.2.8 最小外接圆
函数cv2.minEnclosingCircle() 可以帮我们找到一个对象的外切圆。它是所有能够包括对象的圆中面积最小的一个。
"""
import cv2
import numpy as np

img = cv2.imread("../../../resource/img/4.jpg");
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY);
thresh, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE);

cnt = contours[0];
area_max = cv2.contourArea(cnt);
for cont in contours:
    area = cv2.contourArea(cont);
    if area_max < area:
        cnt = cont;
        area_max = area;
"""
cv2.minEnclosingCircle(points) → center, radius
Finds a circle of the minimum area enclosing a 2D point set.
    points – Input vector of 2D points, stored in
        std::vector<> or Mat (C++ interface)
        CvSeq* or CvMat* (C interface)
        Nx2 numpy array (Python interface)
    center – Output center of the circle.
    radius – Output radius of the circle.
"""
(x, y), radius = cv2.minEnclosingCircle(cnt);
image = img.copy();
image = cv2.circle(image, (int(x), int(y)), int(radius), (0, 0, 255), 1);
cv2.imshow("image", cv2.pyrDown(image));


"""
使用的函数为cv2.ellipse()，返回值其实就是旋转边界矩形的内切圆。
cv2.fitEllipse(points) → retval
Fits an ellipse around a set of 2D points.
    points –Input 2D point set
"""
image2 = img.copy();
ellipse = cv2.fitEllipse(cnt);
image2 = cv2.ellipse(image2, ellipse, (0, 0, 255), 1);
cv2.imshow("image2",cv2.pyrDown(image2));cv2.waitKey(3000);