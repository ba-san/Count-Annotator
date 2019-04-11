import os
import cv2
import glob

folder = "images" #input images in this directory

PWD = "C:/Users/member/Documents/annotation_set/" #set current directory

files=glob.glob(PWD + folder + "/*")

path = PWD + folder + "_cropped"


if not os.path.exists(path):
	os.makedirs(path)


for fname in files:
	print(fname)
	img = cv2.imread(fname, cv2.IMREAD_COLOR)

	x=1
	y=1
	
	while y < img.shape[0]/300.0:
		while x < img.shape[1]/300.0:
			cropped = img[(y-1)*300:y*300, (x-1)*300:x*300]
			cv2.imwrite(os.path.join(path, os.path.basename(fname) + "_" + str(x) + "_" + str(y) + ".jpg"), cropped)
			x+=1
		x=1
		y+=1
			
