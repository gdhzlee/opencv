import cv2;
import numpy as np;

img = cv2.imread("../../../resource/img/7.png");
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
ret, thresh = cv2.threshold(hsv, 127, 255, cv2.THRESH_BINARY);

image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE);
#todo 为什么epsilon的值越小就，画出来的轮廓越多
epsilon = 0.1*cv2.arcLength(contours[0], True);
approx = cv2.approxPolyDP(contours[0], epsilon, True);

img = cv2.drawContours(img, approx, -1, (0, 255, 0), 3);
cv2.imshow("img", img);cv2.waitKey(0);
