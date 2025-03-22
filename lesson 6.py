import cv2
import os
from PIL import Image
path = "C:\\Users\\kalpv\\OneDrive\\Desktop\\Python Code - Jetlearn\\Images for Video"
os.chdir(path)
meanwidth = 0
meanheight = 0
for file in os.listdir('.'):
    if file.endswith('.png') or file.endswith('.jpeg') or file.endswith('.jpg'):
        image = Image.open(os.path.join(path, file))
        width, height = image.size
        meanwidth = meanwidth + width
        meanheight = meanheight + height

number_of_images = len(os.listdir('.'))
meanwidth = meanwidth//number_of_images
meanheight = meanheight//number_of_images

for file in os.listdir('.'):
    if file.endswith('.png') or file.endswith('.jpeg') or file.endswith('.jpg'):
        image = Image.open(os.path.join(path, file))
        width, height = image.size
        resized_img = image.resize((meanwidth, meanheight), Image.Resampling.LANCZOS)
        resized_img.save(file, "JPEG", quality = 95)

def creatingvid():
    vidname = "Cricket Video.avi"
    os.chdir(path)
    images = []

    for file in os.listdir('.'):
        if file.endswith('.png') or file.endswith('.jpeg') or file.endswith('.jpg'):
            images.append(file)
    frame = cv2.imread(os.path.join(path, images[0]))
    height, width, layers = frame.shape
    video = cv2.VideoWriter(vidname, 0, 1, (width, height))
    for image in images:
        video.write(cv2.imread(os.path.join(path, image)))
    cv2.destroyAllWindows()
    video.release()

creatingvid()