"""
21.4.2 Point Polygon Test
求解图像中的一个点到一个对象轮廓的最短距离。如果点在轮廓的外部，返回值为负。如果在轮廓上，返回值为0。如果在轮廓内部，返回值为正。

cv2.pointPolygonTest(contour, pt, measureDist) → retval
    contour – Input contour.
    pt – Point tested against the contour.
    measureDist – If true, the function estimates the signed distance from the point to the nearest contour edge. Otherwise, the function only checks if the point is inside a contour or not.
如果你不需要知道具体距离，建议你将第三个参数设为False，这样速度会提高2 到3 倍。
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

dist = cv2.pointPolygonTest(cnt, (50,50), True);
print(dist);