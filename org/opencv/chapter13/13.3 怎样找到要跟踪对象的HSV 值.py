"""
13.3 怎样找到要跟踪对象的HSV 值

"""
import cv2
import numpy as np

#找到绿色的hsv值
green = np.uint8([[[0,255,0]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print(hsv_green)

