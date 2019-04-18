#importing cv2 library
import cv2

#Creating a VideoCapture object
capture = cv2.VideoCapture(0)

#Creating a video codec >>> don't know what it is
fourcc = cv2.VideoWriter_fourcc(*'XVID')

#Creating a VideoWriter object with ('outpupt name',codec,frameRate,(size))
out = cv2.VideoWriter('output.mp4',fourcc,20,(640,480))

while(True):
    #Reading the frame
    ret,frame = capture.read()
    
    #Flipping the frame horizontally
    frame = cv2.flip(frame,1)
    
    #Writing this frame to output.mp4
    out.write(frame)
    
    #Showing the video 
    cv2.imshow('Video Recording',frame)
    
    #Creating a keyboard event
    key = cv2.waitKey(1)
    
    if(key == 27):
        break
    
#Releasing the VideoCapture object
capture.release()

#Releasing the VideoWriter object
out.release()

#Destroying the windows
cv2.destroyAllWindows()
    