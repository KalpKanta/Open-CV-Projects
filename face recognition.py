import os
import cv2
import numpy as np

haar_file =  "haarcascade_frontalface_default.xml"
datasets = "datasets"
subdata = "Kalp"
path = os.path.join(datasets, subdata)
if not os.path.isdir(path):
    os.mkdir(path)
(width, height) = (130, 100)
face_cascade = cv2.CascadeClassifier(haar_file)
webcam = cv2.VideoCapture(0)
for i in range(30):
    (_, im) = webcam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    for (x,y,w,h) in faces:
        cv2.rectangle(im, (x,y), (x+w,y+h), (0, 0, 255), 5)
        face = gray[y:y+h, x:x+w]
        face_resize = cv2.resize(face, (width, height))
        cv2.imwrite("%s/%s.png"%(path, i+1), face_resize)
    cv2.imshow("open cv thing", im)
    key = cv2.waitKey(10)
    if key == 27:
        break