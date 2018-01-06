"""
13.2 物体跟踪
现在我们知道怎样将一幅图像从BGR 转换到HSV 了，我们可以利用这一点来提取带有某个特定颜色的物体。在HSV 颜色空间中要比在BGR 空间
中更容易表示一个特定颜色。在我们的程序中，我们要提取的是一个蓝色的物体。下面就是就是我们要做的几步：
    • 从视频中获取每一帧图像
    • 将图像转换到HSV 空间
    • 设置HSV 阈值到蓝色范围。
    • 获取蓝色物体，当然我们还可以做其他任何我们想做的事，比如：在蓝色物体周围画一个圈。

"""
import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while(1):
    ret,frame = cap.read();
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_green = np.array([])