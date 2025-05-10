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
webcam = cv2.VideoCapture(1)

while True:
    (_,im) = webcam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x,y), (x+w,y+h), (0, 0, 255), 5)
        face = gray[y:y+h, x:x+w]
        face_resize = cv2.resize(face, (width, height))
        prediction = model.predict(face_resize)
        cv2.rectangle(im, (x,y), (x+w,y+h), (0, 0, 255), 5)
        if prediction[1] < 500:
            cv2.putText(im, "%s-%.0f"%(names[prediction[0]], prediction[1]), (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255))
        else:
            cv2.putText(im, "Face is not recognised",(x -10, y - 10),cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255))
        cv2.imshow("Face", im)
        key = cv2.waitkey(0)