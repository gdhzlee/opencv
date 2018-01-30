"""
21.5.2 OpenCV 中层次结构
不管层次结构是什么样的，每一个轮廓都包含自己的信息：谁是父，谁是子等。
OpenCV 使用一个含有四个元素的数组表示。[Next，Previous，First_Child，Parent]。
    Next 表示同一级组织结构中的下一个轮廓。
    Previous 表示同一级结构中的前一个轮廓。
    First_Child 表示它的第一个子轮廓。
    Parent 表示它的父轮廓。
当四个元素所代表的轮廓的不存在时，则值为 -1
轮廓的顺序：从左到右，从外到里

21.5.3 轮廓检索模式

"""
import cv2
import numpy as np

img = cv2.imread("../../../resource/img/8.jpg");
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY);

image = np.zeros((600,600), dtype=np.uint8);
image[0:600,0:600] = 255;
"""
1、RETR_LIST 从解释的角度来看，这中应是最简单的。它只是提取所有的轮廓，而不去创建任何父子关系。
可以从输出结果，看到该模式下，First_Child 和 Parent 的值都是-1。
"""
image1 = thresh.copy();
image1, contours1, hierarchy1 = cv2.findContours(image1, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE);
print(hierarchy1);
image1 = cv2.drawContours(image.copy(), contours1, -1, ( 0, 0, 255), 10 );
cv2.imshow("image1",image1);
print("---------------------");

"""
2、RETR_EXTERNAL 如果你选择这种模式的话，只会返回最外边的的轮廓，所有的子轮廓都会被忽略掉。
从输出结果，看到该模式下，只有返回了最外边的轮廓
"""
image2 = thresh.copy();
image2, contours2, hierarchy2 = cv2.findContours(image2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE);
image2 = cv2.drawContours(image.copy(), contours2, -1, (0, 0, 0), 1);
cv2.imshow("image2", image2);
print(hierarchy2);
print("---------------------");

"""
3、RETR_CCOMP 在这种模式下会返回所有的轮廓并将轮廓分为两级组织结构。
例如，一个对象的外轮廓为第1 级组织结构。而对象内部中空洞的轮廓为第2 级组织结构，空洞中的任何对象的轮廓又是第1 级组织结构。
空洞的组织结构为第2 级。
"""
image3 = thresh.copy();
image3, contours3, hierarchy3 = cv2.findContours(image3, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE);
image3 = cv2.drawContours(image.copy(), contours3, -1, (0, 255, 0), 1);
cv2.imshow("image3", image3); cv2.waitKey(3000);
print(hierarchy3);
print("----------------------");

"""
RETR_TREE 终于到最后一个了，也是最完美的一个。
这种模式下会返回所有轮廓，并且创建一个完整的组织结构列表。
"""
image4, contours4, hierarchy4 = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE);
image4 = cv2.drawContours(image.copy(), -1, (0, 255, 0), 1);
cv2.imshow("image4",image4);cv2.waitKey(3000);
print(hierarchy4);

