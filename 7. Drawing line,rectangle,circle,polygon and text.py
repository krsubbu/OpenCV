#importing cv2 and numpy library
import cv2
import numpy as np

#Creating a blank canvas using numpy ones function
img = np.ones((512,512,3),np.uint8)

#Drawing a line(canvas_name,initial_coord,final_coord,colour,stroke)
img = cv2.line(img,(0,0),(512,512),(0,0,255),5)

#Drawing a rectangle(canvas_name,first_corner,diagnol_coord,colour,stroke)
img = cv2.rectangle(img,(100,100),(400,400),(0,255,0),3)

#Drawing a circle(canvas_name,center_coord,Radius,colour,stroke)
img = cv2.circle(img,(300,300),50,(120,70,50),2)

#Creating a list of coordinates for polygon
pts = np.array([[10,20],[40,50],[70,80],[100,240]],np.int32)
#Reshaping the array and storing the row and column in another layers
pts = pts.reshape((-1,1,2))
#using polylines(canvas_namae,[array of points],closed,colour)
img = cv2.polylines(img,[pts],True,(0,255,255))

#Putting text
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img,'Open CV',(10,500),font,2,(255,155,0),2,cv2.LINE_AA)

#Showing the canvas
cv2.imshow('Canvas',img)

#Waiting for an keyboard event to occur
cv2.waitKey(0) 

#Destroying all windows 
cv2.destroyAllWindows()