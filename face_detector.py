#face detection using image processing  only


import cv2 
import numpy as np

Names=['awad','ezzat','waly','ibrahim']

# file_dest= [name+'/'+name + '.mp4' for name in Names]

def Detect_face(img):
    img_YCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb) 
    YCrCb_mask = cv2.inRange(img_YCrCb, (0, 135, 85), (255,180,135))
    YCrCb_mask = cv2.morphologyEx(YCrCb_mask, cv2.MORPH_OPEN, np.ones((5,5), np.uint8))
    global_mask=cv2.medianBlur(YCrCb_mask,5)
    #global_mask = cv2.GaussianBlur(YCrCb_mask, (3, 3), 0)
    global_mask = cv2.morphologyEx(global_mask, cv2.MORPH_OPEN, np.ones((4,4), np.uint8))
    global_mask = cv2.morphologyEx(global_mask, cv2.MORPH_CLOSE, np.ones((15,15), np.uint8))

    kernel_circle=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(10,10))
    erosion_circle1 = cv2.erode(global_mask,kernel_circle,iterations = 15)
    erosion_circle1= cv2.morphologyEx(erosion_circle1, cv2.MORPH_OPEN, kernel_circle)

    #num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(dilation, 8, cv2.CV_32S)
    #print("Number of circles",num_labels)
    #for i in range (num_labels):
    #    cv2.putText(erosion_circle1,str(i+1),(int(centroids[i][0]),int(centroids[i][1])),cv2.FONT_HERSHEY_SIMPLEX,0.5,(200,255, 0), lineType=cv2.LINE_AA)
    n_labels, img_labeled, lab_stats, X = cv2.connectedComponentsWithStats(erosion_circle1, connectivity=8, ltype=cv2.CV_32S)
    largest_obj_lab = np.argmax(lab_stats[1:, 4]) + 1
    largest_mask = np.zeros(erosion_circle1.shape, dtype=np.uint8)
    largest_mask[img_labeled == largest_obj_lab] = 255
    dilation = cv2.dilate(largest_mask,kernel_circle,iterations=20)
    face = cv2.bitwise_and(img, img, mask = dilation)
    return face




for i in range(len(Names)):
    Name=Names[i]
#     print(Name)
    for count in range (25):
        
        # print(count)
        image_dest=Name+'/'+Name+str(count)+'.jpg'
        faces_dest=Name+'/'+'Faces'+'/'+str(count)+'.jpg'
        img=cv2.imread(image_dest)
        # cv2.imshow('image',img)
        # cv2.waitKey(10)
        face_image=Detect_face(img)
        cv2.imwrite(faces_dest,face_image)
    






#x=cv2.waitKey(0)
#cv2.destroyAllWindows()

