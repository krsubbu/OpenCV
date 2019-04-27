#import numpy and cv2
import numpy as np
import cv2

#Reading two images
img1 = cv2.imread('C:\Users\Subham\Documents\GitHub\OpenCV\ex.jpg')
img2 = cv2.imread('C:\Users\Subham\Documents\GitHub\OpenCV\ex2.jpg')

print(img1.shape)
print(img2.shape)
#Adding two images using cv2.add() function
img = cv2.add(img1,img2)

#Creating a window named 'Image' and showing it
cv2.namedWindow('Image',cv2.WINDOW_NORMAL)
cv2.imshow('Image',img)

#Waiting for a keyboard event
cv2.waitKey(0)

#Destroy all windows
cv2.destroyAllWindows()


#A Q
#A QUICK FOX JUMPS OVER THE LAZY DOG
#a quivk foc jimps pber yje ;axu fog