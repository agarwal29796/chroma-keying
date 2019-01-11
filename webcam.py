import cv2 as cv
cam = cv.VideoCapture(0)

cv.namedWindow("test")

img_counter = 0 

while True : 
	ret , frame = cam.read()
	cv.imshow("test",frame)
	if not ret :
		break
	k = cv.waitKey(1)
	if k%256 == 27:
		print "Escape hit , closing"
		break
	elif k%256 == 32 :
		print "image is captured and saved into ./cam folder"
		cv.imwrite("./cam/%d.png"%img_counter,  frame)
		img_counter = img_counter + 1
cam.release()
cv.destroyAllWindows()