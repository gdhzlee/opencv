"""
13.2 物体跟踪
现在我们知道怎样将一幅图像从BGR 转换到HSV 了，我们可以利用这一点来提取带有某个特定颜色的物体。在HSV 颜色空间中要比在BGR 空间
中更容易表示一个特定颜色。在我们的程序中，我们要提取的是一个蓝色的物体。下面就是就是我们要做的几步：
    • 从视频中获取每一帧图像
    • 将图像转换到HSV 空间
    • 设置HSV 阈值到蓝色范围。
    • 获取蓝色物体，当然我们还可以做其他任何我们想做的事，比如：在蓝色物体周围画一个圈。

"""
#TODO
import cv2
import numpy as np
cap = cv2.VideoCapture("../../../resource/video/1.mp4")

while(cap.isOpened()):
    ret,frame = cap.read();
    try:
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    except exec:
        break
    lower_green = np.array([59,0,0])
    upper_green = np.array([61,255,255])

    """
    cv2.inRange(src, lowerb, upperb[, dst]) → dst
    Checks if array elements lie between the elements of two other arrays.
    Parameters:	
        src – first input array.
        lowerb – inclusive lower boundary array or a scalar.
        upperb – inclusive upper boundary array or a scalar.
        dst – output array of the same size as src and CV_8U type.
    就是将低于lower_red和高于upper_red的部分分别变成0，lower_red～upper_red之间的值变成255
    """
    #根据阈值进行构建掩模
    mask = cv2.inRange(hsv,lower_green,upper_green)

    res = cv2.bitwise_and(frame,frame,mask=mask)

    #cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)
    key = cv2.waitKey(5)&0xFF
    if key==27:
        break

cv2.destroyAllWindows()

#图像中仍然有一些噪音，我们会在后面的章节中介绍如何消减噪音。
"""
这是物体跟踪中最简单的方法。当你学习了轮廓之后，你就会学到更多
相关知识，那是你就可以找到物体的重心，并根据重心来跟踪物体，仅仅在摄
像头前挥挥手就可以画出同的图形，或者其他更有趣的事。
"""