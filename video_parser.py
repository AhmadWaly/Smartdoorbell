# this file for parsing videos to images to make a data set for each one of us 

import cv2 
import numpy as np


Names=['awad','ezzat','magdy','waly','ibrahim']
file_dest= [name+'/'+name + '.mp4' for name in Names]

cap=[cv2.VideoCapture(path) for path in file_dest]

for x in range(len(Names)):
    i=0
    count=0
    while True:
        # Capture frame-by-frame
        ret, frame = cap[x].read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        if count%10==0 :
            imagename=Names[x]+'/'+Names[x]+str(i)+'.jpg'
            cv2.imwrite(imagename,frame)
            i+=1
        count+=1