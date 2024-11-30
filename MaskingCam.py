import cv2
import os
import numpy as np
myvideo = cv2.VideoCapture(0)
myvideo.read()
print(myvideo.read())
bg = 0
for i in range(100):
  ret,bg = myvideo.read()
while myvideo.isOpened():
  ret,img = myvideo.read()
  HSVvid = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
  lower_green = np.array([40,40,40])
  upper_green = np.array([100,255,255])
  mask = cv2.inRange(HSVvid,lower_green,upper_green)
  mask1 = cv2.bitwise_not(mask)
  result1 = cv2.bitwise_and(bg,bg,mask=mask)
  result2 = cv2.bitwise_and(img,img,mask=mask1)
  final = cv2.addWeighted(result1,1,result2,1,0)
  cv2.imshow("1", final)
  k = cv2.waitKey(5)
  if k == 27:
    break
