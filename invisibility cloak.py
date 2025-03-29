import cv2
import time
import numpy as np

vVideo = cv2.VideoCapture("video.mp4")
time.sleep(1)
count = 0
background = 0
for i in range(60):
    return_value, background = vVideo.read()
    if return_value == False:
        continue

background = np.flip(background, axis = 1)
while vVideo.isOpened():
    return_value, image = vVideo.read()
    if not return_value:
        break
    count = count + 1
    img = np.flip(image, axis = 1)

    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lowerRed = np.array)