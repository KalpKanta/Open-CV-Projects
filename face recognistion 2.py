import cv2
import numpy
import os

haar = "haarcascade_frontalface_default.xml"
datasets = "datasets"
print("Capturing face")
(images, labels, names, id) = ([], [], {}, 0)
for (subdirs, dirs, files) in os.walk(datasets):
    for subdir in dirs:
        names[id] = subdir
        path = os.path.join(datasets, subdir)
        for filename in os.listdir(path):
            path2 = path + "/" + filename
            label = id
            images.append(cv2.imread(path2, 0))
            labels.append(label)
        id += 1
(width, height) = (130, 100)
(images, labels) = [numpy.array(lis) for lis in [images, labels]]
model = cv2.face.LBPHFaceRecognizer_create()
model.train(images, labels)
print("Model trained successfully")

face_cascade = cv2.CascadeClassifier(haar)
webcam = cv2.VideoCapture(0)
