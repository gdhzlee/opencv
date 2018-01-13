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

