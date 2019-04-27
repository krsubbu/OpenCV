#importing cv2
import cv2

#Reading two images
logo = cv2.imread('C:\Users\Subham\Documents\GitHub\OpenCV\logo.png')
dog = cv2.imread('C:\Users\Subham\Documents\GitHub\OpenCV\ex.jpg')

#Creating a roi of Logo size in Dog image
rows,cols,channels = logo.shape
roi = dog[:rows,:cols]

#Adding two same size images i.e roi and logo (REMEMBER we can add two images of same size only)
added = cv2.add(logo,roi)

#Replacing the logo part of image with the logo in the dog image
dog[:rows,:cols] = added

#Creating a window named 'Image' and showing it
cv2.namedWindow('Image',cv2.WINDOW_NORMAL)
cv2.imshow('Image',dog)

#Waiting for a keyboard event
cv2.waitKey(0)

#Destroy all windows
cv2.destroyAllWindows()