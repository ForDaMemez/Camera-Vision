import cv2
import os
Facexml = "haarcascade_frontalface_default.xml"
datasets = "Data sets"
name = input("Enter your name ")
path = os.path.join(datasets, name)
if not os.path.isdir(path):
  os.mkdir(path)
face_detection = cv2.CascadeClassifier(Facexml)
facevid = cv2.VideoCapture(0)
count = 1
while facevid.isOpened():
  ret,img = facevid.read()
  img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  face = face_detection.detectMultiScale(img1, 1.5,3)
  print(face)
  for x,y,w,h in face:
    rectangle = cv2.rectangle(img,(x,y), (x+w,y+h),(255,0,0), 1)
    person = img1[y:y+h, x:x+w]
    #personresize = cv2.resize(person, (150,150))
    #os.chdir(path)
    cv2.imwrite(f"{path}/{count}.png",person)
    count = count + 1
  cv2.imshow("1", img)
  key = cv2.waitKey(5)
  if key == 27:
    break
  if count >= 31:
    break