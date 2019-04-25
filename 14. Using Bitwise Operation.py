#import numpy and cv2
import numpy as np
import cv2


#Opening two images
img1 = cv2.imread('C:\Users\Subham\Documents\GitHub\OpenCV\ex.jpg')
img2 = cv2.imread('C:\Users\Subham\Documents\GitHub\OpenCV\ex2.jpg')


rows,cols,channels = img2.shape
roi = img2[:rows,:cols]

#Using bitwise operation
img = cv2.bitwise_and(img1,roi)

#Creating a window named 'Image'
cv2.namedWindow('Image',cv2.WINDOW_NORMAL)

#Showing a image
cv2.imshow('Image',img)

#Waiting for a keyboard event to occur
cv2.waitKey(0)

#Destroying all windows
cv2.destroyAllWindows()
