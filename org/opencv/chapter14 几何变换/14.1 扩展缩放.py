"""
14.1 扩展缩放
扩展缩放只是改变图像的尺寸大小。OpenCV 提供的函数cv2.resize()
可以实现这个功能。图像的尺寸可以自己手动设置，你也可以指定缩放因子。
我们可以选择使用不同的插值方法。在缩放时我们推荐使用cv2.INTER_AREA，在扩展时我们推荐使用v2.INTER_CUBIC（慢) 和v2.INTER_LINEAR。
默认情况下所有改变图像尺寸大小的操作使用的插值方法都是cv2.INTER_LINEAR。你可以使用下面任意一种方法改变图像的尺寸：
cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]]) → dst
Parameters:
    src – input image.
    dst – output image; it has the size dsize (when it is non-zero) or the size computed from src.size(), fx, and fy; the type of dst is the same as of src.
    dsize –output image size; if it equals zero, it is computed as:dsize = Size(round(fx*src.cols), round(fy*src.rows))}
        Either dsize or both fx and fy must be non-zero.
    fx –scale factor along the horizontal axis; when it equals 0, it is computed as (double)dsize.width/src.cols}
    fy –scale factor along the vertical axis; when it equals 0, it is computed as  (double)dsize.height/src.rows}
    interpolation –interpolation method:
        INTER_NEAREST - a nearest-neighbor interpolation
        INTER_LINEAR - a bilinear interpolation (used by default)
        INTER_AREA - resampling using pixel area relation. It may be a preferred method for image decimation, as it gives moire’-free results. But when the image is zoomed, it is similar to the INTER_NEAREST method.
        INTER_CUBIC - a bicubic interpolation over 4x4 pixel neighborhood
        INTER_LANCZOS4 - a Lanczos interpolation over 8x8 pixel neighborhood
"""
import cv2
import numpy as np

img = cv2.imread("../../../resource/img/1.jpg");
resImg = cv2.resize(img, None, 2, 2 ,cv2.INTER_CUBIC);
"""
Python 列表
List（列表） 是 Python 中使用最频繁的数据类型。
列表中值的切割也可以用到变量 [头下标:尾下标] ，就可以截取相应的列表，从左到右索引默认 0 开始，
从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。例如
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print list               # 输出完整列表
print list[0]            # 输出列表的第一个元素
print list[1:3]          # 输出第二个至第三个元素 
print list[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2       # 输出列表两次
print list + tinylist    # 打印组合的列表
"""
imgRows, imgCols = img.shape[:2]
resImgRows, resImgCols= resImg.shape[:2]
#python 强制类型转换 str()
cv2.imshow("img "+str(imgRows)+" * "+str(imgCols),img);
cv2.imshow("resImg "+str(resImgRows)+" * "+str(resImgCols),resImg);cv2.waitKey(3000);

#height = rows , width = cols
resImg2 = cv2.resize(img,(2*imgCols,2*imgRows),interpolation=cv2.INTER_CUBIC);
cv2.imshow("resImg2",resImg2);cv2.waitKey(3000);

cv2.destroyAllWindows();