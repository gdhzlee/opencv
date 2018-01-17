"""
21.3 轮廓的性质
"""
import cv2
import numpy as np

img = cv2.imread("../../../resource/img/4.jpg");
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY);
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE);

cnt = contours[0];
area_max = cv2.contourArea(cnt);
for cont in contours:
    area = cv2.contourArea(cont);
    if area_max < area:
        area_max = area;
        cnt = cont;
"""
1、长宽比
边界矩形的宽高比
"""
x, y, w, h = cv2.boundingRect(cnt);
aspect_ratio = float(w)/h;
print(aspect_ratio);

"""
2、Extent
轮廓面积与边界矩形面积的比。
"""
area = area_max;
rect_area = w*h;
extent = float(area)/rect_area;
print(extent);

"""
3、Solidity
轮廓面积与凸包面积的比。
"""
hull = cv2.convexHull(cnt);
hull_area = cv2.contourArea(hull);
solidity = float(area)/hull_area;
print(solidity);

"""
4、 Equivalent Diameter
与轮廓面积相等的圆形的直径
"""
equi_diameter = np.sqrt(4*area/np.pi);
print(equi_diameter);

"""
5、方向
对象的方向，下面的方法还会返回长轴和短轴的长度
"""
(x, y), (MA, ma), angle = cv2.fitEllipse(cnt);

#TODO 下面这个完全不懂
"""
6、掩模和像素点
有时我们需要构成对象的所有像素点，我们可以这样做：
"""
#图像掩模是用选定的图像、图形或物体、对待处理的图像(全部或局部)进行遮挡来控制图像处理的区域或处理过程。
mask = np.zeros(gray.shape, np.uint8);
# cv2.imshow("mask", cv2.pyrDown(mask));
# mask = cv2.drawContours(mask, [cnt], 0, 255, -1);
pixepoints = np.transpose(np.nonzero(mask));

cv2.imshow("mask1",cv2.pyrDown(mask));cv2.waitKey(3000);

"""
7、最大值和最小值及它们的位置
我们可以使用掩模图像得到这些参数。
"""
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(gray, mask = mask);

"""
8、平均颜色及平均灰度
我们也可以使用相同的掩模求一个对象的平均颜色或平均灰度
"""
mean_val = cv2.mean(img, mask = mask);

"""
9、极点
一个对象最上面，最下面，最左边，最右边的点。
"""
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0]);
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0]);
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0]);
print(leftmost);

