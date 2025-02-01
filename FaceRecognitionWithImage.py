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
img1 = cv2.imread("Assets/SRIHITHIMAGE.png",0)
images,labels = [np.array(lis,dtype = object) for lis in [images,labels]]     
labels = np.array(labels,dtype= np.int32)
model = cv2.face.LBPHFaceRecognizer_create()
model.train(images,labels)
face_detection = cv2.CascadeClassifier(Facexml)
face = face_detection.detectMultiScale(img1, 1.5,3)
for x,y,h,w in face:
 rectangle = cv2.rectangle(img1,(x,y), (x+w,y+h),(255,0,0), 1)
person = img1[y:y+h, x:x+w]
personresize = cv2.resize(person, (150,150))
prediction = model.predict(personresize)
if prediction[1] > 40:
  cv2.putText(img1, names[prediction[0]], (x,y-10), cv2.FONT_HERSHEY_COMPLEX,2,(255,0,0))
cv2.imshow("window1",img1)
cv2.waitKey(0)

