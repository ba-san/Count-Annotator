# Count-Annotator

You can prepare annotation images for counting and csv file which contains each point's location.  
This can be worked both on both Linux and Windows.  

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
``` 
save_frame_range('./videos/pocari_cm.mp4',
                 0, 10000000000, 100, # start, end, frame
                 './images/', 'pocari_cm')
``` 

### annotation
1. Go to the root directory.  
2. setting path of annotation.py
``` 
folder = "images" #input images in this directory

PWD = "C:/Users/member/Documents/annotation_set/" #set current directory
``` 

## Output
You can get both csv file and annotated images.  
