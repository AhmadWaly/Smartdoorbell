To run the project you have to install :-

-flask

-flask_cors

-face_recognition

then open terminal at project directory and type 

: -export FLASK_APP=app.py

-flask run 

then open another terminal from dist directory and type : -http-server -o 

####################################################################################


Smart Doorbell 

Introduction :-
	The objective of this project is to build a system for a doorbell to recognize the house owners and unlocks the door for them while not allowing strangers and send their picture to the owners 

####Project approach :-####

-DETECTING FACE USING DIGITAL IMAGE PROCESSING :
We used digital image processing to detect faces and live all the other pixels black using the approach presented in (Face and Facial Component Detection by Using Image Characteristic) paper .

Simply the approach is applied to each and every pixel of the image.
The RGB image value is converted to HSV as well as YCbCr value, the HSV and YCbCr value of each pixel is compared to the standard values of a skin pixel and the decision is made whether the pixel is a skin pixel or not depending on whether the values lie in a range of predefined threshold values for each parameter.

-then passing the image with detected face to the FACENET to generate the face 128-d encodings then by comparing the new encodings with saved encodings on the database using euclidean distance with threshold 0.5 you will know if the person is a stranger or if it was one of the owners 








