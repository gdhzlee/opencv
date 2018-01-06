"""
13.1 颜色空间转换
在OpenCV 中有超过150 中进行颜色空间转换的方法。但是你以后就会发现我们经常用到的也就两种：BGR<->Gray 和BGR<->HSV。
cv2.cvtColor(src, code[, dst[, dstCn]]) → dst
Converts an image from one color space to another.
Parameters:
    src – input image: 8-bit unsigned, 16-bit unsigned ( CV_16UC... ), or single-precision floating-point.
    dst – output image of the same size and depth as src.
    code – color space conversion code (see the description below).
    dstCn – number of channels in the destination image; if the parameter is 0, the number of the channels is derived automatically from src and code .
BGR Gray 的转换，我们要使用的flag 就是cv2.COLOR_BGR2GRAY
BGR HSV 的转换，我们用的flag 就是cv2.COLOR_BGR2HSV
"""


"""
在OpenCV 的HSV 格式中，
H（色彩/色度）的取值范围是[0，179]，
S（饱和度）的取值范围[0，255]，
V（亮度）的取值范围[0，255]。
但是不同的软件使用的值可能不同。所以当你需要拿OpenCV 的HSV 值与其他软件的HSV 值进行对比时，一定要记得归一化。
"""
import cv2
flags = [i for i in dir(cv2) if i.startswith("COLOR_")]
print(flags)