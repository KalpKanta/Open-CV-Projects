import cv2
import numpy
import os

v = cv2.VideoCapture("cars.mp4")
haar = "cars.xml"
carcascade = cv2.CascadeClassifier(haar)

while True:
    ret, frames = v.read()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    car = carcascade.detectMultiScale(gray, 1.1, 1)

    for (x,y,w,h) in car:
        cv2.rectangle(frames, (x,y), (x+w,y+h), (0, 0, 255), 5)

    cv2.imshow("Frame", frames)
    key = cv2.waitKey(10)
    if key == 27:
        break