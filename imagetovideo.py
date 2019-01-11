import cv2 as cv
import numpy as np
import os
from os.path import isfile ,  join
import locale


path_in  = './images/'
path_out = 'video.mp4'
fps = 23.0

frame_array = []
files = [int(f.split('.')[0]) for f in os.listdir(path_in)]
files.sort()



for i in range(len(files)):
	filename = path_in + '%d.jpg'%files[i]
	print filename
	img = cv.imread(filename)
	height , width , layers = img.shape
	size = (width,height)
	frame_array.append(img)


out = cv.VideoWriter(path_out , cv.VideoWriter_fourcc(*'mp4v') , fps , size)
for i in range(len(frame_array)):
	out.write(frame_array[i])
out.release()
