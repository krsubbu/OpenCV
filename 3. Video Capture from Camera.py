#importing openCV
import cv2

#Creating a VideoCapture Object
capture = cv2.VideoCapture(0)

#Looping till the camera gives images and till the time we want images from the camera
while(True):
    #Reading whether camera is sending data or not 
    #ret return "True" if data is received else return "False"
    #frame capture the image matrix
    ret,frame = capture.read();
    
    #Creating a window to show the video from the camera
    #cv2.namedWindow('Video',frame)
    cv2.imshow('Video',frame);
    
    #Creating a keyboard event to get out of the loop or close the camera
    key = cv2.waitKey(1)
    
    if(key == 27):
        break
#release the capture object to use the camera in other operation
#Very Important step...
capture.release();

#Destroying the window created
cv2.destroyAllWindows();
    