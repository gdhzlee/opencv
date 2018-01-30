"""
9.4 拆分及合并图像通道
有时我们需要对BGR 三个通道分别进行操作。这是你就需要把BGR 拆
分成单个通道。有时你需要把独立通道的图片合并成一个BGR 图像。你可以
这样做：
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("../../../resource/img/1.jpg")
#拆分通道
"""
Python: cv2.split(m[, mv]) → mv
    mv – output array or vector of arrays; 
        in the first variant of the function the number of arrays must match src.channels(); 
        the arrays themselves are reallocated, if needed.
"""
b,g,r = cv2.split(img)
cv2.imshow('blue', b)
cv2.imshow('green',g)
cv2.imshow('red',r)
#合并通道
"""
Python: cv2.merge(mv[, dst]) → dst
    mv – input array or vector of matrices to be merged; 
        all the matrices in mv must have the same size and the same depth.
"""
img1 = cv2.merge((b,g,r))

#通过Numpy索引来获取才各个图像通道
b1 = img[:,:,0]
g1 = img[:,:,1]
r2 = img[:,:,2]
#可以通过Numoy索引来直接对通道赋值
img[:,:,2]=0
cv2.imshow("img[:,:,2]",img)
cv2.waitKey(2000)

"""
cv2.split() 是一个比较耗时的操作。只有真正需要时才用它，能用
Numpy 索引就尽量用。
"""