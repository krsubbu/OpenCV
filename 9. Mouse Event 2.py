#importing numpy and cv2 library
import numpy as np
import cv2

#Creating a variable to track for circle or rectangle
draw = False
mode = False

#Creating the draw_circle function 
def draw_circle(event,x,y,flag,param):
    
    #Calling the global variable by using keyword 'global'
    global draw,mode
    
    #Calling the event mouse left button click
    if(event == cv2.EVENT_LBUTTONDOWN):
        draw = True;
        
    #if left_button is true and mouse_move than draw otherwise not
    if(event == cv2.EVENT_MOUSEMOVE and draw):
        #mode variable is used to select between circle and rectangle
        if(mode):
            cv2.circle(img,(x,y),10,(255,150,0),5)
        else:
            cv2.rectangle(img,(x,y),(x+10,y+10),(0,0,255),4)
    
    #Preventing from drawing after mouse_click is released
    if(event == cv2.EVENT_LBUTTONUP):
        draw = False
        
#Creating a black canvas
img = np.zeros((640,480,3),np.uint8)

#Creating a 'Canvas' named window 
cv2.namedWindow('Canvas')

#Creating a mouse event call back function calling draw_circle
cv2.setMouseCallback('Canvas',draw_circle)

while(1):
    
    #Showing the canvas
    cv2.imshow('Canvas',img)
    
    #Creating a keyboard event
    key = cv2.waitKey(1)
    
    #Swapping between circle and rectangle
    if(key == ord('m')):
        mode = not mode
    elif(key == 27):
        break
    
#Destroying all windows    
cv2.destroyAllWindows()



        



