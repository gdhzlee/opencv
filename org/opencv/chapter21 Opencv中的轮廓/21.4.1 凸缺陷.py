"""
21.4.1 凸缺陷
前面我们已经学习了轮廓的凸包，对象上的任何凹陷都被成为凸缺陷。OpenCV 中有一个函数cv.convexityDefect() 可以帮助我们找到凸缺陷。
"""
import cv2
import numpy as np

img = cv2.imread("../../../resource/img/4.jpg");
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY);
imgae, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE);

cnt = contours[0];
area_max = cv2.contourArea(cnt);
for cont in contours:
    area = cv2.contourArea(cont);
    if area_max < area:
        cnt = cont;
        area_max = area;
#获取凸包
#如果要查找凸缺陷，在使用函数cv2.convexHull 找凸包时，参数returnPoints 一定要是False。
hull = cv2.convexHull(cnt, returnPoints=False);

"""
cv2.convexityDefects(contour, convexhull[, convexityDefects]) → convexityDefects
Finds the convexity defects of a contour.
    contour – Input contour.
    convexhull – Convex hull obtained using convexHull() that should contain indices of the contour points that make the hull.
    convexityDefects – The output vector of convexity defects. In C++ and the new Python/Java interface each convexity defect is represented as 4-element integer vector (a.k.a. cv::Vec4i): (start_index, end_index, farthest_pt_index, fixpt_depth), where indices are 0-based indices in the original contour of the convexity defect beginning, end and the farthest point, and fixpt_depth is fixed-point approximation (with 8 fractional bits) of the distance between the farthest contour point and the hull. That is, to get the floating-point value of the depth will be fixpt_depth/256.0. In C interface convexity defect is represented by CvConvexityDefect structure - see below.
    storage – Container for the output sequence of convexity defects. If it is NULL, the contour or hull (in that order) storage is used.
它会返回一个数组，其中每一行包含的值是[起点，终点，最远的点，到最远点的近似距离]。
"""
defects = cv2.convexityDefects(cnt, hull);
for i in range(defects.shape[0]):
    s, e, f, d = defects[i,0];  #起点，终点，最远的点，到最远点的近似距离
    #todo cnt[s][0]什么意思啊
    start = tuple(cnt[s][0]);
    end = tuple(cnt[e][0]);
    far = tuple(cnt[f][0]);
    print(str(cnt[s][0])+" "+str(start));
    cv2.line(img, start, end, [0,255,0], 2);
    cv2.circle(img, far, 5, [0,0,255], -1);

cv2.imshow("img",img);
cv2.waitKey(3000);