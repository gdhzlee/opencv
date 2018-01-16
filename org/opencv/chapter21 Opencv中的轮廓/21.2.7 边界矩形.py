"""
21.2.7 边界矩形
1、直边界矩形一个直矩形（就是没有旋转的矩形）。它不会考虑对象是否旋转。所以边界矩形的面积不是最小的。
（x，y）为矩形左上角的坐标，（w，h）是矩形的宽和高。

"""
import cv2
import numpy as np

img = cv2.imread("../../../resource/img/4.jpg");
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY);
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
"""
cv2.boundingRect(points) → retval
Calculates the up-right bounding rectangle of a point set.
    points – Input 2D point set, stored in std::vector or Mat.
"""
img1 = img.copy();
for cont in contours:
    x, y, height, width = cv2.boundingRect(cont);
    img1 = cv2.rectangle(img1, (x, y), (x+width, y+height), (0, 255, 0), 1);
img1 = cv2.drawContours(img1, contours, -1, (0, 0, 255), 1);
cv2.imshow("img1",cv2.pyrDown(img1));

img2 = img.copy();
#找出面积最大的轮廓
cnt = contours[0];
area_max = cv2.contourArea(cnt);
for cont in contours:
    area = cv2.contourArea(cont)
    if area_max < area:
        cnt = cont;
        area_max = area;
img2 = cv2.drawContours(img2, cnt, -1, (0, 0, 255), 1);
x, y, height, width = cv2.boundingRect(cnt);
img2 = cv2.rectangle(img2, (x, y), (x+width, y+height), (0, 255, 0), 1);
cv2.imshow("img2", cv2.pyrDown(img2));

"""
旋转的边界矩形这个边界矩形是面积最小的，因为它考虑了对象的旋转。用到的函数为cv2.minAreaRect()。
返回的是一个Box2D 结构，其中包含矩形左上角角点的坐标（x，y），矩形的宽和高（w，h），以及旋转角度。
但是要绘制这个矩形需要矩形的4 个角点，可以通过函数cv2.boxPoints() 获得。
"""
img3 = img.copy();
"""
cv2.minAreaRect(points) → retval
Finds a rotated rectangle of the minimum area enclosing the input 2D point set.
    points – Input vector of 2D points:
"""
rect = cv2.minAreaRect(cnt);
"""
cv2.boxPoints(box[, points]) → points
Finds the four vertices顶点 of a rotated旋转后 rect. Useful to draw the rotated rectangle.
    box – The input rotated rectangle. It may be the output of .. ocv:function:: minAreaRect.
"""
box = cv2.boxPoints(rect);
print(box);
"""
bool_ Boolean (True or False) stored as a byte 
int_ Default integer type (same as C long; normally either int64 or int32) 
intc Identical to C int (normally int32 or int64) 
intp Integer used for indexing (same as C ssize_t; normally either int32 or int64) 
int8 Byte (-128 to 127) 
int16 Integer (-32768 to 32767) 
int32 Integer (-2147483648 to 2147483647) 
int64 Integer (-9223372036854775808 to 9223372036854775807) 
uint8 Unsigned integer (0 to 255) 
uint16 Unsigned integer (0 to 65535) 
uint32 Unsigned integer (0 to 4294967295) 
uint64 Unsigned integer (0 to 18446744073709551615) 
float_ Shorthand for float64. 
float16 Half precision float: sign bit, 5 bits exponent, 10 bits mantissa 
float32 Single precision float: sign bit, 8 bits exponent, 23 bits mantissa 
float64 Double precision float: sign bit, 11 bits exponent, 52 bits mantissa 
complex_ Shorthand for complex128. 
complex64 Complex number, represented by two 32-bit floats (real and imaginary components) 
complex128 Complex number, represented by two 64-bit floats (real and imaginary components)
"""
box = np.int0(box);
print(box);
img3 = cv2.drawContours(img3, [box], 0, (0, 255, 0), 1);
cv2.imshow("img3", cv2.pyrDown(img3));cv2.waitKey(3000);