import cv2, os
pic1 = cv2.imread("Assets\opencv.png")
print(pic1[50,29])
pic1[50,29] = (0,0,255)
cv2.imshow("window1", pic1)
cv2.waitKey(0)
pic1_gray = cv2.imread("Assets\opencv.png", 0)
cv2.imshow("window2", pic1_gray)
cv2.waitKey(0)
# There are 3 parameters to read an image - 
#cv2.IMREAD_COLOR (1) => Specify to load the image in color
#cv2.IMREAD_GRAYSCALE (0) => Specify to load the image in grayscale / black & white
#cv2.IMREAD_UNCHANGED (-1) => Specify to load the image unchanged
os.chdir("C:/Users/phani/OneDrive/Test2")
cv2.imwrite("graysc.png",pic1_gray)
B,G,R = cv2.split(pic1)
cv2.imshow("windowBlue", B)
cv2.waitKey(0)
os.chdir("C:/Users/phani/OneDrive/Camera vision project")
print(B)
print(G)
merge1 = cv2.merge([R,G,B])
cv2.imshow("winodw 3", merge1)
cv2.waitKey(0)