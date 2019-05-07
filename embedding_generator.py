import cv2
import numpy as np
import face_recognition as fr 
import pandas as pd 

Names=['awad','ezzat','ibrahim','waly']

def generate_encodings_list(Name) :
    face_embeddings=[0]*25
    for count in range (25):
        face_dest=Name+"/Faces"+"/"+str(count)+'.jpg'
        face_img=cv2.imread(face_dest)
        # cv2.imshow('a',face_img)
        # cv2.waitKey(10)
        face_img=cv2.cvtColor(face_img,cv2.COLOR_BGR2RGB)
        face_embeddings[count]=fr.face_encodings(face_img)
    return face_embeddings

for i in Names : 
    csvpath=i+'/'+i+'.csv'
    embeddings=generate_encodings_list(i)
    embeddings=lst = [e for sl in embeddings for e in sl]
    print(np.shape(embeddings))
    np.savetxt(csvpath, embeddings, delimiter=",")