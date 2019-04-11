# Count-Annotator

You can prepare annotation images for counting and csv file which contains each point's location.  
This can be worked on both Linux and Windows.  
<img src="https://user-images.githubusercontent.com/44015510/55924149-97272500-5c43-11e9-95bf-96e7de80151a.png" width="600">


<img src="https://user-images.githubusercontent.com/44015510/55922933-524cbf80-5c3e-11e9-9c02-d4d5d7196183.png" width="300"><img src="https://user-images.githubusercontent.com/44015510/55923063-dc952380-5c3e-11e9-8c8b-8e0b6913d3a5.png" width="300">

## Set up
You are recommended to use Python3.7.  
download this repository.  
``` 
git clone https://github.com/ba-san/Count-Annotator.git  
``` 
install packages.  
``` 
pip install -r requirements.txt    
``` 

## How to use
### making videos to images
1. Go to the root directory.  
2. setting path and frame of video2img.py  
Most of this script is owe to [this page](https://note.nkmk.me/python-opencv-video-to-still-image/).  
``` 
save_frame_range('./videos/pocari_cm.mp4', #input video
                 0, 10000000000, 100, # start, end, frame
                 './images/', 'pocari_cm') #output directory and output images' prefix
``` 

### annotation
1. Go to the root directory.  
2. setting path of annotation.py
``` 
folder = "images" #input images in this directory

PWD = "C:/Users/member/Documents/annotation_set/" #set current directory
``` 
3. You can also change the size of cropped images here.  
``` 
	while y < img.shape[0]/300.0:
		while x < img.shape[1]/300.0:
							
			cropped = img[(y-1)*300:y*300, (x-1)*300:x*300]
``` 
In this case, cropped images' size is 300px x 300px.  

## Output
You can get both csv file and annotated images.  
