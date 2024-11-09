import cv2
import os
pic = cv2.imread("Assets/people.jpeg")
picHSV = cv2.cvtColor(pic,cv2.COLOR_BGR2RGB)
picHSV = cv2.Canny(picHSV,10,100)
cv2.imshow("1",picHSV)
cv2.waitKey(0)