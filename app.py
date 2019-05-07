from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import base64
import json
import numpy as np
import cv2
import face_recognition as fr 
from run import *

awad=pd.read_csv('awad.csv').values
ezzat=pd.read_csv('ezzat.csv').values
waly=pd.read_csv('waly.csv').values
ibrahim=pd.read_csv('ibrahim.csv').values


#this function takes the image from the response as a b64 string and return it as a cv2 image
def data_uri_to_cv2_img(uri):
    encoded_data = uri.split(',')[1]
    nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img





app = Flask(__name__)
app.config['DEBUG'] = True
basedir = os.path.abspath(os.path.dirname(__file__))

CORS(app)

@app.route("/",methods=['GET'])

@app.route("/login", methods=['POST','GET'])
def login():
    image=request.json.get('image')
    image=data_uri_to_cv2_img(image)
    person=Whosface(image)
    if person == -1 : 
        return jsonify({'type': 'error','title':'STRANGER ON THE DOOR','body':'DOOR IS LOCKED'})
    else :
        title=person + " ON THE DOOR"
        body = 'DOOR OPENS FOR'+ person
        return jsonify({'type': 'error','title':title,'body':body})

    
