import cv2
import os
import numpy as np


subjects = ["", "kejriwal", "modi"]

def prepare_training_data(data_folder_path):
    dirs = os.listdir(data_folder_path)
    faces = []
    labels = []
    label = 1
    for dir_name in dirs:

        subject_dir_path = data_folder_path + "/" + dir_name
        subject_images_names = os.listdir(subject_dir_path)

        for image_name in subject_images_names:

            image_path = subject_dir_path + "/" + image_name
            image = cv2.imread(image_path)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            #cv2.imshow("Training on image...", cv2.resize(image, (400, 500)))
            #cv2.waitKey(100)

            faces.append(image)
            labels.append(label)
        label += 1

    #v2.destroyAllWindows()
    #cv2.waitKey(1)
    #cv2.destroyAllWindows()
    #print(faces, labels)
    return faces, labels

print("Preparing data...")
faces, labels = prepare_training_data("data_noresize")
print("Data prepared")

#print total faces and labels
print("Total faces: ", len(faces))
print("Total labels: ", len(labels))

face_recognizer = cv2.face.LBPHFaceRecognizer_create()

face_recognizer.train(faces, np.array(labels))

face_recognizer.write('LBPHres.yml')
