import cv2
import os
import numpy as np
image1 = cv2.imread("Assets/ghost.png")
#Negative thickness values fill in the circle, but positive values just draw the outline
circle = cv2.circle(image1,(256,256), 30,(255,0,255),-2)
cv2.imshow("1", circle)
cv2.waitKey(0)
image2 = cv2.imread("Assets/ghost.png")
line = cv2.line(image2,(150,150),(250,250),(255,0,255),2)
cv2.imshow("2",line)
cv2.waitKey(0)
image3 = cv2.imread("Assets/ghost.png")
rectangle = cv2.rectangle(image3,(100,100), (350,350),(255,0,0), -5)
cv2.imshow("3", rectangle)
cv2.waitKey(0)
image4 = cv2.imread("Assets/ghost.png")
points = np.array([[200,200],[250,250],[200,350]])
#fillPoly for filled in polygon and polyLines for outline of a polygon
polygon = cv2.polylines(image4,[points],True, (0,0,0),3)
cv2.imshow("4", polygon)
cv2.waitKey(0)
image5 = cv2.imread("Assets/ghost.png")
arrowhead = cv2.arrowedLine(image5,(350,350), (450,450), (0,0,0), 5)
cv2.imshow("5", arrowhead)
cv2.waitKey(0)