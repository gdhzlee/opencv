"""
19.2 OpenCV 中的Canny 边界检测

"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("C:\\Users\\lee\\Desktop\\1.jpg",0);
"""
cv2.Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient]]]) → edges
    image – 8-bit input image.
    edges – output edge map; single channels 8-bit image, which has the same size as image .
    threshold1 – first threshold for the hysteresis procedure.  - minVal
    threshold2 – second threshold for the hysteresis procedure.  - maxVal
    apertureSize – aperture size for the Sobel() operator.
    L2gradient – a flag, indicating whether a more accurate  L_2 norm  =\sqrt{(dI/dx)^2 + (dI/dy)^2} should be used to calculate the image gradient magnitude ( L2gradient=true ), or whether the default  L_1 norm  =|dI/dx|+|dI/dy| is enough ( L2gradient=false ).

    现在要确定那些边界才是真正的边界。这时我们需要设置两个阈值：
minVal 和maxVal。当图像的灰度梯度高于maxVal 时被认为是真的边界，
那些低于minVal 的边界会被抛弃。如果介于两者之间的话，就要看这个点是
否与某个被确定为真正的边界点相连，如果是就认为它也是边界点，如果不是
就抛弃
这个函数的第一个参数是输入图像。第二和第三
个分别是minVal 和maxVal。第三个参数设置用来计算图像梯度的Sobel
卷积核的大小，默认值为3。最后一个参数是L2gradient，它可以用来设定
求梯度大小的方程。如果设为True，就会使用我们上面提到过的方程，否则
使用方程：Edge_Gradient (G) = |Gx^2| + |Gy^2|代替，默认值为False。
"""
edges = cv2.Canny(img, 100, 200);
cv2.namedWindow("image");

def nothing(x):
    pass;

cv2.createTrackbar('minVal','image',0,255,nothing);
cv2.createTrackbar("maxVal","image",0,255,nothing);

edges1 = img;
while(1):

    cv2.imshow("image",edges1);
    k = cv2.waitKey(2)&0xFF
    if k==27:
        break;

    minVal = cv2.getTrackbarPos("minVal","image");
    maxVal = cv2.getTrackbarPos("maxVal","image");

    edges1 = cv2.Canny(img,minVal,maxVal);

cv2.destroyAllWindows();