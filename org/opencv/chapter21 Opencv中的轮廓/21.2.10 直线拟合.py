"""
21.2.10 直线拟合
我们可以根据一组点拟合出一条直线，同样我们也可以为图像中的白色点拟合出一条直线。
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

#行，列
rows, cols = img.shape[:2];
"""
cv2.fitLine(points, distType, param, reps, aeps[, line]) → line
Fits a line to a 2D or 3D point set.
    points – Input vector of 2D or 3D points, stored in std::vector<> or Mat.
    line – 
        Output line parameters. In case of 2D fitting, it should be a vector of 4 elements (like Vec4f) - (vx, vy, x0, y0), 
        where (vx, vy) is a normalized归一化 vector向量 collinear 共线 to the line and (x0, y0) is a point on the line. 
        In case of 3D fitting, it should be a vector of 6 elements (like Vec6f) - (vx, vy, vz, x0, y0, z0), 
        where (vx, vy, vz) is a normalized vector collinear to the line and (x0, y0, z0) is a point on the line.
    distType – Distance used by the M-estimator (see the discussion below).
    param – Numerical parameter ( C ) for some types of distances. If it is 0, an optimal value is chosen.
    reps – Sufficient accuracy for the radius (distance between the coordinate origin and the line).
    aeps – Sufficient accuracy for the angle. 0.01 would be a good default value for reps and aeps.
"""
[vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01);
lefty = int((-x*vy/vx)+y);
righty = int(((cols-x)*vy/vx)+y);
img = cv2.line(img, (cols-1, righty),(0,lefty),(0,0,255),1);
cv2.imshow("img",cv2.pyrDown(img));cv2.waitKey(3000);
