import cv2
import os
import numpy as np
Facexml = "haarcascade_frontalface_default.xml"
datasets = "Data sets"
images,labels,names,id = ([], [], {}, 0)
for subdirs,dirs,files in os.walk(datasets):
  for subdir in dirs:
    names[id] = subdir
    subjectpath = os.path.join(datasets,subdir)
    images2 = os.listdir(subjectpath)
    for files in images2:
      path = subjectpath + "/" + files
      label = id
      labels.append(label)
      images.append(cv2.imread(path))
    id += 1
print(names)
print(images)
print(labels)
images,labels = [np.array(lis) for lis in [images,labels]]
model = cv2.face.LBPHFaceRecognizer_create()
model.train(images,labels)
"""face_detection = cv2.CascadeClassifier(Facexml)
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
    break"""