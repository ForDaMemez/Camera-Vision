import cv2
import os
import numpy as np
Eye_xml = "Assets\haarcascade_eye.xml"
vid1 = cv2.imread("Assets/SRIHITHIMAGE.png")
eye_detection = cv2.CascadeClassifier(Eye_xml)
"""while vid1.isOpened():
  ret,img = vid1.read()
  grayvid = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  eye = eye_detection.detectMultiScale(grayvid,1.9,1)
  for x,y,w,h in eye:
    rectangle = cv2.rectangle(img,(x,y), (x+w,y+h),(255,0,0), 1)
  cv2.imshow("1", img)
  key = cv2.waitKey(30)
  if key == 27:
    break
"""
img2 = cv2.cvtColor(vid1,cv2.COLOR_BGR2GRAY)
eye = eye_detection.detectMultiScale(img2,1.9,1)
for x,y,w,h in eye:
  rectangle = cv2.rectangle(img2,(x,y), (x+w,y+h),(255,0,0), 1)
cv2.imshow("1",img2)
cv2.waitKey(0)
