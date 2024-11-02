import cv2
import os
pic = cv2.imread("Assets/Everest.jpeg")
Medpic = cv2.medianBlur(pic, 5)
cv2.imshow("Window1", Medpic)
cv2.waitKey(0)
pic2 = cv2.imread("Assets/Everest.jpeg")
add1 = cv2.addWeighted(pic,3,pic2,3,1)
cv2.imshow("Window2", add1)
cv2.waitKey(0)