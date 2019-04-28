#importing numpy and opencv
import numpy as np
import cv2

#Creating a videoCapture object
video = cv2.VideoCapture(0)

while(True):
    #Reading each frame from webcam
    ret,frame = video.read()
    
    #Converting each frame in a hsv image
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    #Define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    
    #Checking each frame for blue colour range
    mask = cv2.inRange(hsv,lower_blue,upper_blue)
    
    #Bitwise this frame with the original one so we can track the image
    res = cv2.bitwise_and(frame,frame,mask = mask)
    
    #Showing each frame in a window
    cv2.imshow('Original',frame)
    cv2.imshow('Mask',mask)
    cv2.imshow('Bitwise_And',res)
    
    #Creating a keyboard event
    if(cv2.waitKey(1) == 27):
        break
    
#Releasing videoCaputre object
video.release()

#Destroying all windows created
cv2.destroyAllWindows()