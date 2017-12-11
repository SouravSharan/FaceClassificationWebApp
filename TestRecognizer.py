import cv2
import os
import numpy as np


def classifier(filename):
    THRESHOLD = 50
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.read('LBPHres.yml')
    face_recognizer.setThreshold(THRESHOLD)

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    img = cv2.imread('./images/input/' + filename)
    #print('file name: ./images/' + filename)
    #cv2.imshow("a", img)
    #cv2.waitKey(1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    ret = [0,0,0]
    for (x,y,w,h) in faces:
        ret[0] += 1
        roi_gray = gray[y:y+h, x:x+w]
        #roi_gray = cv2.resize(roi_gray, (150,150))
        result, confidence = face_recognizer.predict(roi_gray)
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        print(result, confidence)
        font = cv2.FONT_HERSHEY_SIMPLEX
        if(result == 1):
            cv2.putText(img,"Arvind Kejriwal",(x,y), font, 1,(255,0,0),2,cv2.LINE_AA)
            ret[1] = 1
        elif(result == 2):
            cv2.putText(img,"Narendra Modi",(x,y), font, 1,(255,0,0),2,cv2.LINE_AA)
            ret[2] = 1
    img = cv2.resize(img, (530,530))
    cv2.imwrite("./images/output/out" + filename, img)
    return ret
