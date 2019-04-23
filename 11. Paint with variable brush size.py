#importing numpy and cv2 library
import numpy as np
import cv2

#Creating a variable to track for circle and their colour
draw = False
show = True
r=0
g=0
b=0
s=0

#Defining callback function
def nothing(x):
    pass

#Function for drawing circle
def draw_circle(event,x,y,flag,param):
    
    #Calling the global variable by using keyword 'global'
    global draw,r,g,b,s
    
    #Calling the event mouse left button click
    if(event == cv2.EVENT_LBUTTONDOWN):
        draw = True;
        
    #if left_button is true and mouse_move than draw otherwise not
    if(event == cv2.EVENT_MOUSEMOVE and draw):
            cv2.circle(img,(x,y),s,(b,g,r),-1)
    
    #Preventing from drawing after mouse_click is released
    if(event == cv2.EVENT_LBUTTONUP):
        draw = False
               
#Creating a canvas
img = np.zeros((350,512,3),np.uint8)
cv2.namedWindow('paint')

#Creating the trackbar
cv2.createTrackbar('R','paint',0,255,nothing)
cv2.createTrackbar('G','paint',0,255,nothing)
cv2.createTrackbar('B','paint',0,255,nothing)
cv2.createTrackbar('S','paint',0,255,nothing)

#Creating a MouseCallback 
cv2.setMouseCallback('paint',draw_circle)

while(1):
    cv2.imshow('paint',img)
    
    key = cv2.waitKey(1)
    if(key == 27):
        break
    
    #Calling the trackbar_callback function
    r = cv2.getTrackbarPos('R','paint')
    g = cv2.getTrackbarPos('G','paint')
    b = cv2.getTrackbarPos('B','paint')
    s = cv2.getTrackbarPos('S','paint')
    
#Destroying all windows    
cv2.destroyAllWindows()