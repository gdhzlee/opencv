"""
21.1 初识轮廓
轮廓可以简单认为成将连续的点（连着边界）连在一起的曲线，具有相同的颜色或者灰度。轮廓在形状分析和物体的检测和识别中很有用。

• 为了更加准确，要使用二值化图像。在寻找轮廓之前，要进行阈值化处理或者Canny 边界检测。
    cv2.threshold(img, 127, 255, cv2.THRESH_BINARY )
    cv2.Canny(img, minVal, maxVal , )
• 查找轮廓的函数会修改原始图像。如果你在找到轮廓之后还想使用原始图像的话，你应该将原始图像存储到其他变量中。
• 在OpenCV 中，查找轮廓就像在黑色背景中找白色物体。你应该记住，要找的物体应该是白色而背景应该是黑色。

cv2.drawContours(image, contours, contourIdx, color[, thickness[, lineType[, hierarchy[, maxLevel[, offset]]]]]) → image

"""