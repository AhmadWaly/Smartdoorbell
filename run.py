import numpy as np 
import pandas as pd 
import face_recognition as fr 
from face_detector import Detect_face
import cv2


awad=pd.read_csv('awad.csv').values
ezzat=pd.read_csv('ezzat.csv').values
waly=pd.read_csv('waly.csv').values
ibrahim=pd.read_csv('ibrahim.csv').values


def distance(x,y):
    dist=np.linalg.norm(x-y)
    return dist
def Whosface (image):
    try:
        face_img=Detect_face(image) # this sometimes fail 
        face_img=cv2.cvtColor(face_img,cv2.COLOR_BGR2RGB)
        guest_encodings=np.array(fr.face_encodings(face_img))
    except:
        guest_encodings=np.array(fr.face_encodings(image))
    awad_flag=1
    ezzat_flag=1
    waly_flag=1
    ibrahim_flag=1
    #  
    '''
    this repition is for the sake of confirmation as the package not always output encondings similar for the same person :D
     i tried myself in this package more than 20 times 
    one time i have 2 different encodings in 2 different images with distance bigger than the threshold
     so this loops are for making sure that the person is the real person 
    '''
    for i in awad :
        if (distance(guest_encodings,i)<0.52):
            awad_flag+=1
            if (awad_flag>=10):
                return "AWAD"
    for i in waly :
        if (distance(guest_encodings,i)<0.52):
            waly_flag+=1
            if (waly_flag>=10):
                return "WALY"
    for i in ezzat :
        if (distance(guest_encodings,i)<0.52):
            ezzat_flag+=1
            if (ezzat_flag>=10):
                return "EZZAT"
    for i in ibrahim :
        if (distance(guest_encodings,i)<0.52):
            ibrahim_flag+=1
            if (ibrahim_flag>=10):
                return "IBRAHIM"
    return -1 #if strange
    

