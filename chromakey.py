import cv2
import numpy as np
import math
from PIL import Image


key_color = (149,44,21)
tolerance = [50,130]
[y_key , cb_key ,cr_key] = key_color 
# print key_color 
[tola , tolb] = tolerance


def colorclose(arr):
	y , cb_p , cr_p = arr
	temp = math.sqrt((cb_key-cb_p)**2 + (cr_key - cr_p)**2)
	if temp < 100  :
		z = 0.0
	# elif temp < tolb:
		# z = ((temp-tola)/(tolb - tola))
	else:
		z = 1.0
	return 255.0*z

def result(foreground , backgronud):
	forycbcr = cv2.cvtColor(foreground, cv2.COLOR_BGR2YCrCb)
	alpha = np.apply_along_axis(colorclose , 2, forycbcr)
	alpha = np.uint8(255-255*(alpha/255))
	alpha = cv2.cvtColor(alpha, cv2.COLOR_GRAY2BGR)

	# alpha = np.uint8(alpha)
	# alpha = np.uint8(255-255*(alpha/255))

	# cv2.imshow("a", alpha)
	# cv2.waitKey(0)

	alpha = alpha.astype(float)/255
	foreground = foreground.astype(float)
	backgronud = backgronud.astype(float)

	foreground = cv2.multiply(1.0 - alpha, foreground)
	backgronud = cv2.multiply(alpha , backgronud)

	outImage = cv2.add(foreground , backgronud)
	return  outImage


vidcap1 = cv2.VideoCapture('jets.mp4')
vidcap2 = cv2.VideoCapture('back.mp4')
frame_array = []
fps = 15.0


success1 , image1 = vidcap1.read() 
success2 , image2 = vidcap2.read() 
count = 0
while success1 and success2 and count < 250:
	image1 = cv2.resize(image1 , (800,600), interpolation = cv2.INTER_AREA)
	image2 = cv2.resize(image2 , (800,600), interpolation = cv2.INTER_AREA)	
	result_img = result(image1 , image2)
	count = count+1
	
	# cv2.imshow("z" , result_img)
	# cv2.waitKey(0)

	print "merged %d frames" %count
	frame_array.append(result_img)

	success1 , image1 = vidcap1.read()
	success2 , image2 = vidcap2.read()
out = cv2.VideoWriter("merged.mp4", cv2.VideoWriter_fourcc(*'mp4v') , fps , (800,600))
for i in range(len(frame_array)):
	out.write(frame_array[i].astype(np.uint8))
out.release()
