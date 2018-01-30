import cv2;
import numpy as np

img = cv2.imread("../../../resource/img/3.jpg");
HSV = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
# cv2.imshow("imggray", HSV);cv2.waitKey(0);
ret, image = cv2.threshold(HSV, 127, 255, cv2.THRESH_BINARY);
# cv2.imshow("imgthreshold", image);cv2.waitKey(0);

image1 = image.copy();
image1, contours, hierarchy = cv2.findContours(image1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE);

cnt = contours[0];
max_area = cv2.contourArea(cnt);
for cont in contours:
    if cv2.contourArea(cont) > max_area:
        cnt = cont;
        max_area = cv2.contourArea(cnt);
        print(max_area);

epsilon = 0.1*cv2.arcLength(cnt, True);
approx = cv2.approxPolyDP(cnt, epsilon, True);

background1 = np.zeros((500,500), dtype = np.uint8);
background1[0:500, 0:500] = 255;
background1 = cv2.drawContours(background1, [cnt], -1,(0,255,0),1);
cv2.imshow("cnt",background1);
background1 = cv2.drawContours(background1, [approx], -1, (0, 255, 0), 1);
# cv2.imshow("cnt+approx", background1);cv2.waitKey(0);

#和下面的一样
# background2 = np.zeros((500,500), dtype=np.uint8);
# background2[0:500,0:500] = 255;
# for con in contours:
#     background2 = cv2.drawContours(background2, con, -1, (0, 255,0), 1);
# cv2.imshow("contour",background2);cv2.waitKey(3000);

background3 = np.zeros((500,500), dtype=np.uint8);
background3[0:500,0:500] = 255;
background3 = cv2.drawContours(background3,contours,-1,(0,255,0),1);
cv2.imshow("contours",background3);cv2.waitKey(3000);