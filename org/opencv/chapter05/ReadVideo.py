import cv2
import numpy as np

videoCapture = cv2.VideoCapture("../../../resource/video/1.mp4")

while True:
    grab = videoCapture.grab()
    print(grab)
    if grab:
        ref, frame = videoCapture.retrieve()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # print(frame)
        # print(_)
        cv2.imwrite("D:/s.jpg", image)
        cv2.imshow("frame",image)
        cv2.waitKey(1)

