"""

In global thresholding, we used an arbitrary随意的 value for threshold value, right?
So, how can we know a value we selected is good or not? Answer is, trial and error method.
But consider a bimodal双峰 image (In simple words, bimodal image is an image whose histogram has two peaks).
For that image, we can approximately take a value in the middle of those peaks as threshold value, right ?
That is what Otsu binarization does. So in simple words, it automatically calculates a threshold value from image histogram for a bimodal image.
(For images which are not bimodal, binarization won’t be accurate.)
For this, our cv2.threshold() function is used, but pass an extra flag, cv2.THRESH_OTSU. For threshold value, simply
pass zero. Then the algorithm finds the optimal threshold value and returns you as the second output, retVal. If
Otsu thresholding is not used, retVal is same as the threshold value you used.
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("C:\\Users\\lee\\Desktop\\1.jpg",0);
ret1, th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret2, th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU);

blur = cv2.GaussianBlur(img,(5,5),0)
ret3, th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU);

images = [img, 0, th1,
img, 0, th2,
blur, 0, th3]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
'Original Noisy Image','Histogram',"Otsu's Thresholding",
'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])

plt.show();