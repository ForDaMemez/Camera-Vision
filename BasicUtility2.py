import cv2
import os
pika = cv2.imread("Assets/pika.png")
pikaHSV = cv2.cvtColor(pika,cv2.COLOR_BGR2HSV)
cv2.imshow("Window1", pikaHSV)
cv2.waitKey(0)
pikaGRAY = cv2.cvtColor(pika,cv2.COLOR_BGR2GRAY)
cv2.imshow("Window2", pikaGRAY)
cv2.waitKey(0)
pikaRGB = cv2.cvtColor(pika,cv2.COLOR_BGR2RGB)
cv2.imshow("Window3", pikaRGB)
cv2.waitKey(0)
#Canny Edge Detection = inbuilt edge checking command
pikaCED = cv2.Canny(pika,100,1000)
cv2.imshow("4", pikaCED)
cv2.waitKey(0)
pikaROT = cv2.rotate(pika,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("5", pikaROT)
cv2.waitKey(0)
print(pika.shape)
#row,column,number of colors
pikaROT2 = cv2.getRotationMatrix2D((200,200), 75,5)
PikaROT3 = cv2.warpAffine(pika,pikaROT2,(414, 418))
cv2.imshow("6", PikaROT3)
cv2.waitKey(0)