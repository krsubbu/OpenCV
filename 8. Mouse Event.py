#importing numpy and cv2 library
import numpy as np
import cv2

#Creating the draw_circle function 
def draw_circle(event,x,y,flag,param):
    #Calling the event mouse double click
    if(event == cv2.EVENT_LBUTTONDBLCLK):
            cv2.circle(img,(x,y),10,(255,150,0),5)
#Creating a black canvas
img = np.zeros((640,480,3),np.uint8)

#Creating a 'Canvas' named window 
cv2.namedWindow('Canvas')

#Creating a mouse event call back function calling draw_circle
cv2.setMouseCallback('Canvas',draw_circle)

while(1):
    #Creating a window 
    cv2.imshow('Canvas',img)
    #Creating a keyboard event
    key = cv2.waitKey(1)
    if(key == 27):
        break
    
#Destroying all window
cv2.destroyAllWindows()



        



