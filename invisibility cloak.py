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
    lowerRed = np.array([100, 40, 40])
    upRed = np.array([100, 255, 255])
    mask1 = cv2.inRange(hsv_img, lowerRed, upRed)
    
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lowerRed = np.array([150, 40, 40])
    upRed = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv_img, lowerRed, upRed)

    mask1 = mask1 + mask2
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations = 1)
    mask1 =cv2.dilate(mask1, np.ones((3,3), np.uint8), iterations = 1)
    mask2 = cv2.bitwise_not(mask1)
    result1 = cv2.bitwise_and(background, background, mask = mask1)
    result2 = cv2.bitwise_and(img, img, mask = mask2)
    final_output = cv2.addWeighted(result1, 1, result2, 1, 0)
    cv2.imshow("Invisible mask", final_output)
    K = cv2.waitKey(10)
    if K == 27:
        break