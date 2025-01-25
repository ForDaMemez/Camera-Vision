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
      images.append(cv2.imread(path,0))
    id += 1
print(names)
#print(images)
print(labels)
images,labels = [np.array(lis,dtype = object) for lis in [images,labels]]     
labels = np.array(labels,dtype= np.int32)
model = cv2.face.LBPHFaceRecognizer_create()
model.train(images,labels)
face_detection = cv2.CascadeClassifier(Facexml)
facevid = cv2.VideoCapture(0)
while facevid.isOpened():
  ret,img = facevid.read()
  img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  face = face_detection.detectMultiScale(img1, 1.5,3)
  print(face)
  for x,y,w,h in face:
    rectangle = cv2.rectangle(img,(x,y), (x+w,y+h),(255,0,0), 1)
    person = img1[y:y+h, x:x+w]
    personresize = cv2.resize(person, (150,150))
    prediction = model.predict(personresize)
    print(prediction)
    if prediction[1] > 40:
      cv2.putText(img, names[prediction[0]], (x,y-10), cv2.FONT_HERSHEY_COMPLEX,2,(255,0,0))
    #os.chdir(path)
  cv2.imshow("1", img)
  key = cv2.waitKey(5)
  if key == 27:
    break