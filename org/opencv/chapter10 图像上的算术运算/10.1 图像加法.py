"""
10.1 图像加法
你可以使用函数cv2.add() 将两幅图像进行加法运算，当然也可以直接使
用numpy，res=img1+img。两幅图像的大小，类型必须一致，或者第二个
图像可以使一个简单的标量值。

OpenCV 中的加法与Numpy 的加法是有所不同的。OpenCV 的加法
是一种饱和操作，而Numpy 的加法是一种模操作。
饱和加是一种特殊的加法运算。它预先设定一个上限Max.对两个数字进行加法操作时，如果最终的结果>Max，则运算结果取Max.

"""
import cv2
import numpy as np

x = np.uint8([255])
y = np.uint8([10])

print(cv2.add(x, y))
print(x+y)

img = cv2.imread("../../../resource/img/1.jpg")
cv2.imshow("img1",cv2.add(img,img))
cv2.imshow("img2",img+img)
cv2.waitKey(8000)

#这种差别在你对两幅图像进行加法时会更加明显。OpenCV 的结果会更好一点。所以我们尽量使用OpenCV 中的函数。
