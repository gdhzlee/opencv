"""
17.4 结构化元素
在前面的例子中我们使用Numpy 构建了结构化元素，它是正方形的。但有时我们需要构建一个椭圆形/圆形的核。
为了实现这种要求，提供了OpenCV函数cv2.getStructuringElement()。你只需要告诉他你需要的核的形状和大小。
cv2.getStructuringElement(shape, ksize[, anchor]) → retval
Returns a structuring element of the specified size and shape for morphological operations.
    shape –Element shape that could be one of the following:
        MORPH_RECT - a rectangular structuring element: E_{ij}=1
        MORPH_ELLIPSE - an elliptic structuring element, that is, a filled ellipse inscribed into the rectangle Rect(0, 0, esize.width, 0.esize.height)
        MORPH_CROSS - a cross-shaped structuring element: E_{ij} =  \fork{1}{if i=\texttt{anchor.y} or j=\texttt{anchor.x}}{0}{otherwise}
        CV_SHAPE_CUSTOM - custom structuring element (OpenCV 1.x API)
    ksize – Size of the structuring element.
    cols – Width of the structuring element
    rows – Height of the structuring element
"""
import cv2
import numpy as np

#矩形内核
rect = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5));
print(rect);
#椭圆内核
ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5));
print(ellipse);
#十字形内核
cross = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5));
print(cross);
