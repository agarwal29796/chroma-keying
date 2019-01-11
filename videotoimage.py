import cv2 as cv

vidcap = cv.VideoCapture('movie.mp4')
success , image = vidcap.read() 
 
count =  0 
while success :
	cv.imwrite("images/%d.jpg"%count , image)
	success , image = vidcap.read()
	print('Read a new frame: ' , success)
	count += 1