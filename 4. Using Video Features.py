#import cv2 library
import cv2

#create a VideoCapture Object
capture = cv2.VideoCapture(0)
ret = capture.set(3,480)
ret = capture.set(4,240)

while(True):
    #Reading the frame
    ret,frame = capture.read()
    
    #Showing each frame in a window named 'video'
    cv2.imshow('Video',frame)
    
    #Creating a keyboard event
    key = cv2.waitKey(1)
    
    #By pressing we quit the video
    if(key == 27):
        break
    
#Releasing the VideoCapture Object 
capture.release()
cv2.destroyAllWindows()

    
    
    
