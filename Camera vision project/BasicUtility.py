import cv2
import os
star = cv2.imread("Assets\star addition.jpeg")
dia = cv2.imread("Assets\diamond addition.jpeg")
# Arithmetic Operation on Images
# Pixel values are directly added / subtarcted for 2 images
# make sure that the 2 images are of same size
add1 = cv2.addWeighted(star,0.7,dia,0.7,1)
cv2.imshow("window1", add1)
cv2.waitKey(0)
sub1 = cv2.subtract(star,dia)
cv2.imshow("window2", sub1)
cv2.waitKey(0)
#Image Resizing
pika = cv2.imread("Assets\pika.png")
pika2 = cv2.resize(pika,(200,200))
os.chdir("C:/Users/phani/OneDrive/Camera vision project")
cv2.imwrite("pikaResize.png", pika2)
cv2.imshow("window 2", pika2)
cv2.waitKey(0)
#Bluring of an image
# Gaussian Blur - used mostly in machine learning preprocessing steps
# Median Blur - used in digital processing preserves edges but removes noise
# Bilateral Blur - only sharp edges are preserved here
tiger = cv2.imread("Assets\salt and pepper grains.jpeg")
scene = cv2.imread("C:/Users/phani/OneDrive/Camera vision project/Assets/bilateral.jpg")
GausPika = cv2.GaussianBlur(pika,(99,99),0,0)
#Only odd numbers
cv2.imshow("window 3", GausPika)
cv2.waitKey(0)
MedTiger = cv2.medianBlur(tiger,5)
cv2.imshow("window 4", MedTiger)
cv2.waitKey(0)
BilScene = cv2.bilateralFilter(scene,99,95,1)
cv2.imshow("window 5", BilScene)
cv2.waitKey(0)
