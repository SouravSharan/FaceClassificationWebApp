import cv2
import numpy as np
from keras.models import load_model

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

model = load_model('whole_model.h5')
img = cv2.imread('./face.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

face = 0
kejriwal = 0
modi = 0

for (x,y,w,h) in faces:
    face +=1
    roi_color = img[y:y+h, x:x+w]
    roi_color = cv2.resize(roi_color, (300,300))
    cv2.imwrite("./" + str(face) + ".jpg", roi_color)
    roi_color = np.expand_dims(roi_color, axis=0)
    result = model.predict(roi_color, batch_size = 1, verbose = 0)
    print(result)
    res = [[]]
    res[0] = np.zeros_like(result[0])
    res[0][result[0].argmax()] = 1
    result = res
    print(result)
    if(result[0][0] == 1):
        kejriwal = 1
    if(result[0][1] == 1):
        modi = 1

if(face>0):
    print("faces: ", str(face))
    if(kejriwal>0):
        print("kejriwal: yes")
    if(modi>0):
        print("modi: yes")
else:
    print("faces: no")
    print("kejriwal: no")
    print("modi: no")
