#importing cv2 library
import cv2

#Creating a VideoCapture object
capture = cv2.VideoCapture('first.mp4')

while(capture.isOpened()):
    #Reading the frames
    ret,frame = capture.read()
    
    #Seeing the video in a window named 'Video'
    cv2.imshow('Video',frame)
    
    #Creating a keyboard event
    key = cv2.waitKey(1)
    
    if(key == ord('q')):
        break

#Releasing the VideoCapture Object
capture.release()

#Destroying the windows
cv2.destroyAllWindows()