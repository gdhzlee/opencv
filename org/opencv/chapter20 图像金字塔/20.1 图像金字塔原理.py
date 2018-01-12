"""
20.1 图像金字塔原理
一般情况下，我们要处理是一副具有固定分辨率的图像。但是有些情况下，我们需要对同一图像的不同分辨率的子图像进行处理。
比如，我们要在一幅图像中查找某个目标，比如脸，我们不知道目标在图像中的尺寸大小。这种情况下，
我们需要创建创建一组图像，这些图像是具有不同分辨率的原始图像。我们把这组图像叫做图像金字塔（简单来说就是同一图像的不同分辨率的子图集
合）。如果我们把最大的图像放在底部，最小的放在顶部，看起来像一座金字塔，故而得名图像金字塔。
有两类图像金字塔：高斯金字塔和拉普拉斯金字塔。
高斯金字塔的顶部是通过将底部图像中的连续的行和列去除得到的。顶部图像中的每个像素值等于下一层图像中5 个像素的高斯加权平均值。
这样操作一次一个MxN 的图像就变成了一个M/2xN/2 的图像。所以这幅图像的面积就变为原来图像面积的四分之一。这被称为Octave。
连续进行这样的操作我们就会得到一个分辨率不断下降的图像金字塔。我们可以使用函数cv2.pyrDown() 和cv2.pyrUp() 构建图像金字塔。

"""
import cv2
import numpy as np

"""
函数cv2.pyrDown() 从一个高分辨率大尺寸的图像向上构建一个金子塔（尺寸变小，分辨率降低）。
pyrDown(InputArray src, OutputArray dst, Stream& stream=Stream::Null())  
    src – Source image.
    dst – Destination image. Will have Size((src.cols+1)/2, (src.rows+1)/2) size and the same type as src .
因为一旦使用cv2.pyrDown()，图像的分辨率就会降低，信息就会被丢失。
"""
img = cv2.imread("C:\\Users\\lee\\Desktop\\1.jpg",0);
for i in range(4):
    img = cv2.pyrDown(img);
    cv2.imshow("img"+str(i),img);
    cv2.waitKey(1000);
cv2.destroyAllWindows();

"""
函数cv2.pyrUp() 从一个低分辨率小尺寸的图像向下构建一个金子塔（尺寸变大，但分辨率不会增加）。
pyrUp(InputArray src, OutputArray dst, Stream& stream=Stream::Null())
    src – Source image.
    dst – Destination image. Will have Size(src.cols*2, src.rows*2) size and the same type as src .
"""
img = cv2.imread("C:\\Users\\lee\\Desktop\\1.jpg",0);
for i in range(5):
    img = cv2.pyrUp(img);
    cv2.imshow("img"+str(i),img);
    cv2.waitKey(1000);
cv2.destroyAllWindows();


#拉普拉斯金字塔可以有高斯金字塔计算得来 Li = Gi - PyrUp(Gi+1)   i+1 为下标
#拉普拉金字塔的图像看起来就像边界图，其中很多像素都是0。他们经常被用在图像压缩中。
