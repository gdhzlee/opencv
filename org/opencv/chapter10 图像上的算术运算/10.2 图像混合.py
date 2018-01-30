"""
10.2 图像混合
这其实也是加法，但是不同的是两幅图像的权重不同，这就会给人一种混
合或者透明的感觉。图像混合的计算公式如下：
g (x) = (1 -α) f0 (x) + αf1 (x)
通过修改α的值（0 -> 1），可以实现非常酷的混合。
cv2.addWeighted(src1, alpha, src2, beta, gamma[, dst[, dtype]]) → dst
dst = αimg1 + βimg2 +γ
Parameters:
    src1 – first input array.
    alpha – weight of the first array elements.
    src2 – second input array of the same size and channel number as src1.
    beta – weight of the second array elements.
    dst – output array that has the same size and number of channels as the input arrays.
    gamma – scalar added to each sum.
    dtype – optional depth of the output array; when both input arrays have the same depth, dtype can be set to -1, which will be equivalent to src1.depth().
"""
import cv2
import numpy as np

img1 = cv2.imread("../../../resource/img/1.jpg")
img2 = cv2.imread("../../../resource/img/2.jpg")

dst = cv2.addWeighted(img1,0.7,img2,0.3,0)

cv2.imshow("img1",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
