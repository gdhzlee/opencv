import cv2;
import numpy as np;
import os
import sys
file = open("C:\\Users\\lee\\PycharmProjects\\opencv\\resource\\img\\7.png");
print(file.tell());

ScriptPath = os.path.split( os.path.realpath( sys.argv[0] ) )[0]
print(ScriptPath);
img = cv2.imread("../../../resource/img/7.png");
if img is None:
    print("找不到文件")
else:
    cv2.imshow(" ",img);cv2.waitKey(0);