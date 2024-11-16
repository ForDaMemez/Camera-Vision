import cv2
import os
import numpy as np
ghost = cv2.imread("Assets/ghost.png")
ghostGray = cv2.cvtColor(ghost,cv2.COLOR_BGR2GRAY)
Blurghost = cv2.GaussianBlur(ghostGray,(15,15),0,0)
circles = cv2.HoughCircles(Blurghost,cv2.HOUGH_GRADIENT, 1,20,param1 = 120, param2= 60, minRadius= 10, maxRadius= 100)
circles = np.uint16(np.around(circles))
print(circles[0,:])
for data in circles[0,:]:
  x,y,r = data[0],data[1],data[2]
  circle1 = cv2.circle(ghost,(x,y), r, (255,255,0), 6)
cv2.imshow("1", circle1)
cv2.waitKey(0)

#fruits = [["apple", "banana", "pear", "raspberry"]]
#print(fruits[0][:])