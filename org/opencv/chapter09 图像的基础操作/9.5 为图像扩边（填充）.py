"""
9.5 为图像扩边（填充）
如果你想在图像周围创建一个边，就像相框一样，你可以使用cv2.copyMakeBorder()
函数。这经常在卷积运算或0 填充时被用到。这个函数包括如下参数：
Python: cv2.copyMakeBorder(src, top, bottom, left, right, borderType[, dst[, value]]) → dst
    Parameters:
    src – Source image.
    dst – Destination image of the same type as src and the size Size(src.cols+left+right, src.rows+top+bottom) .
    top –
    bottom –
    left –
    right – Parameter specifying how many pixels in each direction from the source image rectangle to extrapolate. For example, top=1, bottom=1, left=1, right=1 mean that 1 pixel-wide border needs to be built.
    borderType – Border type. See borderInterpolate() for details.
    value – Border value if borderType==BORDER_CONSTANT .
    • src 输入图像
    • top, bottom, left, right 对应边界的像素数目。
    • borderType 要添加那种类型的边界，类型如下
        – cv2.BORDER_CONSTANT 添加有颜色的常数值边界，还需要下一个参数（value）。
        – cv2.BORDER_REFLECT 边界元素的镜像。比如: fedcba|abcdefgh|hgfedcb
        – cv2.BORDER_REFLECT_101 or cv2.BORDER_DEFAULT跟上面一样，但稍作改动。例如: gfedcb|abcdefgh|gfedcba
        – cv2.BORDER_REPLICATE 重复最后一个元素。例如: aaaaaabcdefgh|hhhhhhh
        – cv2.BORDER_WRAP 不知道怎么说了, 就像这样: cdefgh|abcdefgh|abcdefg
    • value 边界颜色，如果边界的类型是cv2.BORDER_CONSTANT
"""
import cv2
import numpy as np
#Matplotlib 是一个 Python 的 2D绘图库，它以各种硬拷贝格式和跨平台的交互式环境生成出版质量级别的图形。
from matplotlib import pyplot as plt

BLUE = [255,0,0]
img = cv2.imread("../../../resource/img/1.jpg")

replicate = cv2.copyMakeBorder(img,50,50,50,50,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img,50,50,50,50,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img,50,50,50,50,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img,50,50,50,50,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img,50,50,50,50,cv2.BORDER_CONSTANT,value=BLUE)

plt.subplot(231),plt.imshow(img,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()