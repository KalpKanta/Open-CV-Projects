import os
import cv2
import numpy as np

haar_file =  "haarcascade_frontalface_default.xml"
datasets = "datasets"
subdata = "Kalp"
path = os.path.join(datasets, subdata)
if not os.path.isdir(path):
    os.mkdir(path)