import cv2
import os
import numpy as np
import cv2
import os
import numpy as np
Carxml = "Assets/cars.xml"
Vid = "Assets/cars+cycle.avi"
vid1 = cv2.VideoCapture("Assets/cars+cycle.avi")
car_detection = cv2.CascadeClassifier(Carxml)
while vid1.isOpened():
  ret,img = vid1.read()
  vid2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  car = car_detection.detectMultiScale(vid2, 1.1,1)
  for x,y,h,w in car:
    rectangle = cv2.rectangle(img,(x,y), (x+w,y+h),(255,0,0), 1)
  cv2.imshow("window1",img)
  key = cv2.waitKey(30)
  if key == 27:
    break