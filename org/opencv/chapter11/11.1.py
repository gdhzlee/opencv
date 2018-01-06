"""
使用oepncv检测程序效率
cv2.getTickCount
函数返回从参考点到这个函数被执行的时钟数。所以当你在一个函数执行前后都调用它的话，你就会得到这个函数的执行时间（时钟数）。
cv2.getTickFrequency
返回时钟频率，或者说每秒钟的时钟数。所以你可以按照下面的方式得到一个函数运行了多少秒：
"""
import cv2

e1 = cv2.getTickCount();
for i in range(0,100,1):  #range([start,]stop[,step]) start默认为0。stop默认为1
    print(i)
    cv2.waitKey(500)
e2 = cv2.getTickCount();
print(e1)
print(e2)
print((e2-e2)/cv2.getTickFrequency())

"""
cv2.medianBlur(src, ksize[, dst]) → dst 
Blurs an image using the median filter.中值滤波消除噪点
Parameters:	
    src – input 1-, 3-, or 4-channel image; when ksize is 3 or 5, the image depth should be CV_8U, CV_16U, or CV_32F, for larger aperture sizes, it can only be CV_8U.
    dst – destination array of the same size and type as src.
    ksize – aperture linear size; it must be odd奇数 and greater than 1, for example: 3, 5, 7 ...
"""
img1 = cv2.imread("C:\\Users\\lee\\Desktop\\1.jpg")

el = cv2.getTickCount()
for i in range(5,49,2):
    img1 = cv2.medianBlur(img1,i)
e2 = cv2.getTickCount()
print((e2-e1)/cv2.getTickFrequency())

"""
你也可以中time 模块实现上面的功能。但是要用的函数是
time.time() 而不是cv2.getTickCount。比较一下这两个结果的差别吧。
"""

"""
OpenCV 中的很多函数都被优化过（使用SSE2，AVX 等）。也包含一些
没有被优化的代码。如果我们的系统支持优化的话要尽量利用只一点。在编译时
优化是被默认开启的。因此OpenCV 运行的就是优化后的代码，如果你把优化
关闭的话就只能执行低效的代码了。你可以使用函数cv2.useOptimized()
来查看优化是否被开启了，使用函数cv2.setUseOptimized() 来开启优化。
让我们来看一个简单的例子吧。
"""

