#import numpy and cv2 library
import numpy as np
import cv2

#Callback Function doing nothing 
def nothing(x):
    pass

#Creating a canvas
img = np.zeros((350,512,3),np.uint8)
cv2.namedWindow('RGB Color Selector')

#Creating the trackbar with createTrackbar('name',window,value,end_value,callback)
cv2.createTrackbar('R','RGB Color Selector',0,255,nothing)
cv2.createTrackbar('G','RGB Color Selector',0,255,nothing)
cv2.createTrackbar('B','RGB Color Selector',0,255,nothing)

#Creating a switch
cv2.createTrackbar('Switch','RGB Color Selector',0,1,nothing)

while(1):
    #Showing the canvas in window
    cv2.imshow('RGB Color Selector',img)
    
    #Creating a keyboard event
    key = cv2.waitKey(1)
    if(key == 27):
        break
    
    #Reading the tracker position and storing it in a variable
    r = cv2.getTrackbarPos('R','RGB Color Selector')
    g = cv2.getTrackbarPos('G','RGB Color Selector')
    b = cv2.getTrackbarPos('B','RGB Color Selector')
    s = cv2.getTrackbarPos('Switch','RGB Color Selector')
    
    if(s==0):
        img[:] = [0,0,0]
    else:    #Updating the canvas
        img[:]=[b,g,r]
    
#Destroying the window
cv2.destroyAllWindows()
