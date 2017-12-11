import cv2
import os

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

path = './images/'
path_face = './data_noresize/'

raw_data_folder = os.listdir(path)
print(raw_data_folder)

for i in range(3):
    folder = str(raw_data_folder[i])
    items = os.listdir(path + folder)
    for image in items:
        root,ext = os.path.splitext(image)
        print(image)
        if ext in ['.jpg']:
            try:
                img = cv2.imread(path + folder + "/" + image)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            except:
                continue
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                roi_color = img[y:y+h, x:x+w]
                #roi_color = cv2.resize(roi_color, (150,150))
                cv2.imwrite(path_face + folder + "/" + image, roi_color)
