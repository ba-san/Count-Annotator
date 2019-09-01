import os
import cv2
import glob
import csv
import pandas as pd
import mouseevent
import copy
import linecache, shutil

folder = "images" #input images in this directory

PWD = os.getcwd() + '/'

files=glob.glob(PWD + folder + "/*")

path = PWD + folder + "_cropped"

s = 0
k = 0
cnt = 0
pcnt = 1
tpcnt = 1
new_frame = 0

if not os.path.exists(path):
	os.makedirs(path)
	s = 1
	
print("INSTRUCTION")
print("  C   -- count person")
print("  E   -- stop annotationg")
print("  B   -- go back ONLY ONE act")
print(" Esc  -- clear image and start it again")
print("Enter -- go to next\n")

csvpath = os.path.join(path, folder) + '.csv'

for fname in files:

	img = cv2.imread(fname)
	
	x=1
	y=1

	
	if s == 0: #continue

		right = os.path.basename(fname[-10:-4])
		lastrow = sum(1 for i in open(csvpath)) # http://hk29.hatenablog.jp/entry/2018/05/01/152759
		#lastrow_sen = linecache.getline(os.path.join(path, folder) + '.csv', lastrow)
		last = glob.glob(path + "/LAST_*")
		last = ','.join(last)
		left = os.path.basename(last[-18:-12])

		if new_frame == 0:
			if not left == right:
				continue;

		new_frame = 0


		ent = 0
		if k == 0: #start from previous
			lastrow = sum(1 for i in open(csvpath)) # http://hk29.hatenablog.jp/entry/2018/05/01/152759
			#lastrow_sen = linecache.getline(os.path.join(path, folder) + '.csv', lastrow)
			last = glob.glob(path + "/LAST_*")
			last = ','.join(last)
			
			lastimg = cv2.imread(last)
			y = int(last[-5])
			x = int(last[-7])
			tpcnt = int(lastrow) - 1

			
		elif k == 1: #continue to next frame
			x = 1
			y = 1
			tpcnt = int(lastrow) -1

	elif s == 1: #new
		df = pd.DataFrame(columns=['image', 'x', 'y'])
		df.to_csv(csvpath)
		ent = 1
	
	while y < img.shape[0]/300.0 + 1:
		while x < img.shape[1]/300.0 + 1:
							
			cropped = img[(y-1)*300:y*300, (x-1)*300:x*300]
			cv2.imwrite(os.path.join(path, os.path.basename(fname) + "_" + str(x) + "_" + str(y) + ".jpg"), cropped)
			window_name = os.path.join(path, os.path.basename(fname) + "_" + str(x) + "_" + str(y) + ".jpg")
			if s==0 and cnt==0:  #only for first image when you start from continue
				cnt=1
				last = glob.glob(path + "/LAST_*")
				last = ','.join(last)
				resized_cropped = cv2.imread(last)
				resized_cropped = cv2.resize(resized_cropped, (900, 900))
				resized_previous = cv2.imread(path + "/PREVIOUS.jpg")
				os.remove(last)
			
			else:	
				resized_cropped = cv2.resize(cropped, (900, 900))
				
			if s==1:
				resized_previous = copy.copy(resized_cropped)
			
			print(window_name)
			cv2.imshow(window_name, resized_cropped)
			mouseData = mouseevent.mouseParam(window_name)
			
			
			while True:
				k = cv2.waitKey(0) # waiting input
				
				## checking people
				if k==99: #input 'c'. 
					print(mouseData.getPos())
					resized_previous = copy.copy(resized_cropped) #pass by value
					resized_cropped = cv2.circle(resized_cropped, mouseData.getPos(), 5, (0, 0, 255), -1)
					a, b = mouseData.getPos()
					cv2.imshow(window_name, resized_cropped)
					lastrow = sum(1 for i in open(csvpath))
					tpcnt = int(lastrow)
					print('You have counted {} people in this directory.\nThis time, you have counted {} people. Press E to stop.'.format(tpcnt, pcnt))
					pcnt+=1
					df = pd.read_csv(csvpath, index_col=0)
					series = pd.Series([os.path.join(path, os.path.basename(fname) + "_" + str(x) + "_" + str(y) + ".jpg"), int(a/3.0+0.5), int(b/3.0+0.5)], index=df.columns)
					df = df.append(series, ignore_index=True)
					df.to_csv(csvpath)
					if ent == 1:
						ent=0
					
				## go back the previous
				elif k==98: # input 'b'. See http://d.hatena.ne.jp/tosh914/20121120/1353415648
					lastrow = sum(1 for i in open(csvpath))
					lastrow_sen = linecache.getline(os.path.join(path, folder) + '.csv', lastrow)
					imgname = lastrow_sen.split(",")
					
					if ent == 0:
						resized_cropped = resized_previous
						cv2.imshow(window_name, resized_cropped)
						lastrow = sum(1 for i in open(csvpath)) - 2
						df = pd.read_csv(csvpath, index_col=0)
						df = df.drop(int(lastrow), axis=0)
						df.to_csv(csvpath)
						pcnt-=1
						lastrow = sum(1 for i in open(csvpath))
						ent = 1
				
				## go next image by enter key	
				elif k==13:
					cv2.imwrite(os.path.join(path, os.path.basename(fname) + "_" + str(x) + "_" + str(y) + "annotated.jpg"), resized_cropped)
					resized_previous = copy.copy(resized_cropped)
					ent = 1
					break;
					
				## clear screen by esc
				elif k==27:
					resized_cropped = cv2.resize(cropped, (900, 900))
					cv2.imshow(window_name, resized_cropped)
					df = pd.read_csv(csvpath, index_col=0)
					for i in range(len(df)): # http://www.kisse-logs.com/2017/04/11/python-dataframe-drop/
						if df.loc[i, 'image'] == os.path.join(path, os.path.basename(fname) + "_" + str(x) + "_" + str(y) + ".jpg"):
							df = df.drop(i)
					df.to_csv(csvpath)
					
				## end annotation
				elif k==101: # input 'e'
					cv2.imwrite(os.path.join(path, "LAST_" + os.path.basename(fname) + "_" + str(x) + "_" + str(y) + ".jpg"), resized_cropped)
					cv2.imwrite(path + "/PREVIOUS.jpg", resized_previous)
					exit()
					
			cv2.destroyAllWindows()		
			x+=1
			
		x=1
		y+=1
		
	k=1
	new_frame = 1
