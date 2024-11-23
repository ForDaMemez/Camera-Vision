import cv2
import os
from PIL import Image
os.chdir("C:/Users/phani/OneDrive/Camera vision project/Assets/Waterfall images")
path = "C:/Users/phani/OneDrive/Camera vision project/Assets/Waterfall images"
images = os.listdir(".")
for file in images:
  #img = Image.open(path + "/" + file)
  img = cv2.imread(os.path.join(path,file))
  images2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  cv2.imwrite(file, images2)
sumw = 0
sumh = 0
for file in images:
  #img = Image.open(path + "/" + file)
  img = Image.open(os.path.join(path,file))
  w,h = img.size
  sumw = sumw + w
  sumh = sumh + h
sumw = sumw//len(images)
sumh = sumh//len(images)
print(sumw, sumh)
for file in images:
  img2 = Image.open(os.path.join(path,file))
  img2_Resize = img2.resize((sumw,sumh))
  img2_Resize.save(file,"JPEG",quality = 95)
video_name = "Waterfall video.avi"
video = cv2.VideoWriter(video_name,0,1,(sumw,sumh))
for file in images:
  video.write(cv2.imread(os.path.join(path,file)))
video.release()