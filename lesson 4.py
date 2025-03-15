import cv2
#adding a line to the image
Pikachu = cv2.imread("pika.png", cv2.IMREAD_COLOR)
thic = 5
col = (0, 0, 0)
poss = (200, 320)
pose = (420, 690)
Image = cv2.line(Pikachu, poss, pose, col, thic)
cv2.imshow("Pika with line", Image)
cv2.waitKey()
cv2.destroyAllWindows()

#adding a rectangle to the image
Pikachu2 = cv2.imread("pika.png", cv2.IMREAD_COLOR)
#negative thickness fills the rectangle with the color
thic = -1
col = (255, 165, 0)
poss = (135, 150)
pose = (420, 390)
ImageR = cv2.rectangle(Pikachu2, poss, pose, col, thic)
cv2.imshow("Pikachu with rectangle", ImageR)
cv2.waitKey()
cv2.destroyAllWindows()

#adding a circle to the image
Pikachu3 = cv2.imread("pika.png", cv2.IMREAD_COLOR)
thic = 20
col = (255, 20, 150)
centerPos = (370, 340)
radius = 100
ImageC = cv2.circle(Pikachu3, centerPos, radius, col, thic)
cv2.imshow("Pikachu with circle", ImageC)
cv2.waitKey()
cv2.destroyAllWindows()

#adding text to the image
Pikachu4 = cv2.imread("pika.png", cv2.IMREAD_COLOR)
font = cv2.FONT_HERSHEY_TRIPLEX
font_thic = 2
color = (110, 230, 26)
cords = (120, 300)
font_scale = 1
ImageT = cv2.putText(Pikachu4, "Pikachu image", cords, font, font_scale, color, font_thic, cv2.LINE_AA)
cv2.imshow("Pikachu with circle", ImageT)
cv2.waitKey()
cv2.destroyAllWindows()