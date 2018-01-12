"""
21.1 初识轮廓
轮廓可以简单认为成将连续的点（连着边界）连在一起的曲线，具有相同的颜色或者灰度。轮廓在形状分析和物体的检测和识别中很有用。

• 为了更加准确，要使用二值化图像。在寻找轮廓之前，要进行阈值化处理或者Canny 边界检测。
    cv2.threshold(img, 127, 255, cv2.THRESH_BINARY )
    cv2.Canny(img, minVal, maxVal , )
• 查找轮廓的函数会修改原始图像。如果你在找到轮廓之后还想使用原始图像的话，你应该将原始图像存储到其他变量中。
• 在OpenCV 中，查找轮廓就像在黑色背景中找白色物体。你应该记住，要找的物体应该是白色而背景应该是黑色。


"""

import cv2
import numpy as np

img = cv2.imread("C:\\Users\\lee\\Desktop\\1.jpg");
imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
ret, thresh = cv2.threshold(imggray, 127, 255, 0);  #cv2.THRESH_BINARY=0
cv2.imshow("thresh", thresh);
"""
cv2.findContours(image, mode, method[, contours[, hierarchy[, offset]]]) → image, contours轮廓（是个python列表，存储图像所有的轮廓，每个轮廓都是一个numpy数组，包含对象边界点（x，y）的坐标）, hierarchy轮廓的层析结构
    image – Source, an 8-bit single-channel image. Non-zero pixels are treated as 1’s. Zero pixels remain 0’s, so the image is treated as binary . You can use compare() , inRange() , threshold() , adaptiveThreshold() , Canny() , and others to create a binary image out of a grayscale or color one. The function modifies the image while extracting the contours. If mode equals to CV_RETR_CCOMP or CV_RETR_FLOODFILL, the input can also be a 32-bit integer image of labels (CV_32SC1).
        接受的是二值图，不是灰度图。因此需要先将图像转换成灰度图，再进行二值化处理。
    mode –Contour retrieval mode (if you use Python see also a note below).轮廓的检索模式
        CV_RETR_EXTERNAL retrieves only the extreme outer contours. It sets hierarchy[i][2]=hierarchy[i][3]=-1 for all the contours.
        CV_RETR_LIST retrieves all of the contours without establishing any hierarchical relationships.
        CV_RETR_CCOMP retrieves all of the contours and organizes them into a two-level hierarchy. At the top level, there are external boundaries of the components. At the second level, there are boundaries of the holes. If there is another contour inside a hole of a connected component, it is still put at the top level.
        CV_RETR_TREE retrieves all of the contours and reconstructs a full hierarchy of nested contours. This full hierarchy is built and shown in the OpenCV contours.c demo.
    method –Contour approximation method (if you use Python see also a note below). 轮廓的检测方法
        CV_CHAIN_APPROX_NONE stores absolutely all the contour points. That is, any 2 subsequent points (x1,y1) and (x2,y2) of the contour will be either horizontal, vertical or diagonal neighbors, that is, max(abs(x1-x2),abs(y2-y1))==1.
        CV_CHAIN_APPROX_SIMPLE compresses horizontal, vertical, and diagonal segments and leaves only their end points. For example, an up-right rectangular contour is encoded with 4 points.
        CV_CHAIN_APPROX_TC89_L1,CV_CHAIN_APPROX_TC89_KCOS applies one of the flavors of the Teh-Chin chain approximation algorithm. See [TehChin89] for details.
    offset – Optional offset by which every contour point is shifted. This is useful if the contours are extracted from the image ROI and then they should be analyzed in the whole image context.
"""
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE); #会直接修改传入的图像
"""
cv2.drawContours(image, contours, contourIdx, color[, thickness[, lineType[, hierarchy[, maxLevel[, offset]]]]]) → image
    image – Destination image.
    contours – All the input contours轮廓. Each contour is stored as a point vector. 轮廓
    contourIdx – Parameter indicating a contour to draw. If it is negative, all the contours are drawn. 轮廓的索引
    color – Color of the contours.
    thickness – Thickness of lines the contours are drawn with. If it is negative (for example, thickness=CV_FILLED ), the contour interiors 内部 are drawn.
"""
#最后这两种方法结果是一样的，但是后边的知识会告诉你最后一种方法更有用。
#img = cv2.drawContour(img, contours, -1, (0,255,0), 3); 绘制独立轮廓
cv2.drawContours(img, contours, -1, (0,255,0), 1);

cv2.imshow("img", img);
cv2.waitKey(3000);