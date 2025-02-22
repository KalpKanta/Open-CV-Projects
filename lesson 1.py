import cv2

i = cv2.imread("pika.png", cv2.IMREAD_COLOR) 
#cv2.IMREAD_COLOR is used when you want to read the image in the color mode
#cv2.IMREAD_GRAYSCALE is used to convert the image into a black and white image
#cv2.IMREAD_UNCHANGED is used when you want to read the image without cahngin it

cv2.imshow("Pika", i)
cv2.waitKey(0)
cv2.destroyAllWindows()

i2 = cv2.imread("pika.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Pika2", i2)
cv2.imwrite("Pika3.png", i2)
cv2.waitKey(0)
cv2.destroyAllWindows()

i3 = cv2.imread("pika.png", cv2.IMREAD_COLOR)
B,G,R = cv2.split(i3)
cv2.imshow("blue saturation image", B)
cv2.imshow("green saturation image", G)
cv2.imshow("red saturation image", R)
cv2.waitKey(0)
cv2.destroyAllWindows()