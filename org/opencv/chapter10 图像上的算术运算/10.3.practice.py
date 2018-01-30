
"""
创建一个幻灯片用来演示一幅图如何平滑的转换成另一幅
"""
import cv2
import numpy as np

img1 = cv2.imread("../../../resource/img/1.jpg")
img2 = cv2.imread("../../../resource/img/2.jpg")

i = 0;
while i<1:
    cv2.imshow("幻灯片",cv2.addWeighted(img1,i,img2,1-i,0))
    cv2.waitKey(500)
    i+=0.1

cv2.destroyAllWindows()