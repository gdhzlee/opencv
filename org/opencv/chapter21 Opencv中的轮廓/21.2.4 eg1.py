import cv2
import numpy as np

#创建一个500x500的黑色图像
img = np.zeros((500,500),np.uint8);
#在图像[100:200,100:200]处画一个白色方块
img[100:200,100:200] = 255;
img = cv2.imread("../../../resource/img/3.jpg",0);

#二值化处理
ret, thresh = cv2.threshold(img, 127, 255, 0);
# cv2.imshow("img", thresh);cv2.waitKey(3000);

image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE);
# cv2.imshow("image",image);cv2.waitKey(3000);
color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR);
# cv2.imshow("color",color);cv2.waitKey(3000);
img = cv2.drawContours(color, contours, -1, (0, 255, 0), 2);
cv2.imshow("img",img);cv2.waitKey(3000);