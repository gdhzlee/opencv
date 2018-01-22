"""
21.2.5 凸包
凸包与轮廓近似相似，但不同，虽然有些情况下它们给出的结果是一样的。函数cv2.convexHull() 可以用来检测一个曲线是否具有凸性缺陷，并能纠正缺陷。
一般来说，凸性曲线总是凸出来的，至少是平的。如果有地方凹进去了就被叫做凸性缺陷。

cv2.convexHull(points[, hull[, clockwise[, returnPoints]]]) → hull
    points – Input 2D point set, stored in std::vector or Mat. 需要传入的轮廓
    clockwise – Orientation flag. If it is true, the output convex hull is oriented clockwise. Otherwise, it is oriented counter-clockwise. The assumed coordinate system has its X axis pointing to the right, and its Y axis pointing upwards.
        方向标志，如果设置为true，输出的凸包是顺时针方向的。否则为输出逆时针方向
    returnPoints – Operation flag. In case of a matrix, when the flag is true, the function returns convex hull points. Otherwise, it returns indices of the convex hull points. When the output array is std::vector, the flag is ignored, and the output depends on the type of the vector: std::vector<int> implies returnPoints=true, std::vector<Point> implies returnPoints=false.
        默认为True，返回凸包上点的坐标，如果设置为false，就会返回凸包对应轮廓上的点。
"""
import cv2
import numpy as np

img  = cv2.imread("../../../resource/img/4.jpg");
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
ret, thresh = cv2.threshold(hsv, 127, 255, cv2.THRESH_BINARY);

image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE);
#point is not numpy array, nerther a scalar. point既不是numpy的数组，也不是一个标量

cnt = contours[0];
area_max = cv2.contourArea(cnt);
for cont in contours:
    area = cv2.contourArea(cont);
    if(area_max < area):
        area_max = area;
        cnt = cont;
hull = cv2.convexHull(cnt);

image = img.copy();
image = cv2.drawContours(image, hull, -1, (0, 255, 0), 10);
cv2.imshow("image",cv2.pyrDown(image));cv2.waitKey(3000);

"""
cv2.isContourConvex(contour) → retval
    contour –Input vector of 2D points
    可以可以用来检测一个曲线是不是凸的。返回 True 或 False。
"""
print(cv2.isContourConvex(contours[0]));