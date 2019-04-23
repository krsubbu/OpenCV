#importing numpy and cv2
import numpy as np
import cv2

#opening an image
img = cv2.imread('C:\Users\Subham\Documents\GitHub\OpenCV\ex.jpg',-1)

#Accesing any pixel of image 
px = img[100,100,0]
print(px)

#Setting particular pixel colour to white
img[100,100] = [255,255,255]

#Using numpy function to grab and set pixel value
print(img.item(100,100,0))
img.itemset((100,100,0),100)
print(img.item(100,100,0))

#using shape,size and dtype fucntion to know about image properties
print(img.shape)
print(img.size)
print(img.dtype)

#Using cv2 function to split b,g,r channel into separate layer and merge them
b,g,r = cv2.split(img)
print(b)
img = cv2.merge((b,g,r))

#Another way to grab b,g,r channel 
b = img[:,:,0]
print(b)
#Setting all red value to 0
r = img[:,:,2] = 0

#Copying a part of image to another place
copy = img[1163:2079,569:1300]
img[1733:2649,2154:2885] = copy

#Showing the image in a window named 'Image'
cv2.namedWindow('Image',cv2.WINDOW_NORMAL)
cv2.imshow('Image',img)

#Waiting for a keyboard operation
cv2.waitKey(0)

#Destroying all the windows
cv2.destroyAllWindows()