import cv2

bg1 = cv2.imread("jetlearn background1.jpg", cv2.IMREAD_COLOR)
bg2 = cv2.imread("jetlearn background2.jpg", cv2.IMREAD_COLOR)
bg3 = cv2.addWeighted(bg1, 0.5, bg2, 0.5, 1)   #the addition of the two images
cv2.imshow("Background 1", bg1)
cv2.imshow("Background 2", bg2)
cv2.imshow("Background 3", bg3)
cv2.waitKey()
cv2.destroyAllWindows()

bigstar = cv2.imread("jetlearn big star.jpg", cv2.IMREAD_COLOR)
star = cv2.imread("jetlearn star.jpg", cv2.IMREAD_COLOR)
star2 = cv2.subtract(bigstar, star)     # subtracting the star from the big star
cv2.imshow("Big star", bigstar)
cv2.imshow("Star", star)
cv2.imshow("Big star - Star", star2)
cv2.waitKey()
cv2.destroyAllWindows() 

# resizing inages
pika = cv2.imread("pika.png", cv2.IMREAD_COLOR)
cv2.imshow("Pika", pika)
pika2 = cv2.resize(pika, [600, 900])
cv2.imshow("Pika resized", pika2)
cv2.waitKey()
cv2.destroyAllWindows()

#eroding the images
import numpy as np
pika3 = cv2.imread("pika.png", cv2.IMREAD_COLOR)
cv2.imshow("Pika3", pika)
kernel = np.ones([5, 5], np.uint8)
eroded_image = cv2.erode(pika3, kernel)
cv2.imshow("Eroded image", eroded_image)
cv2.waitKey()
cv2.destroyAllWindows()

#bordering the image
pika4 = cv2.imread("pika.png", cv2.IMREAD_COLOR)
cv2.imshow("Pikachu", pika4)
bordered_img = cv2.copyMakeBorder(pika4, 20 ,20, 20 ,20, cv2.BORDER_CONSTANT, value = 1) #top, bottom, left, right
cv2.imshow("Bordered image", bordered_img)
cv2.waitKey()
cv2.destroyAllWindows()

#bordering the image
pika4 = cv2.imread("pika.png", cv2.IMREAD_COLOR)
cv2.imshow("Pikachu", pika4)
rbordered_img = cv2.copyMakeBorder(pika4, 20 ,20, 20 ,20, cv2.BORDER_REFLECT, value = 1) #top, bottom, left, right
cv2.imshow(" Reflected Bordered image", rbordered_img)
cv2.waitKey()
cv2.destroyAllWindows()