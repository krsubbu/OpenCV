#importing cv2
import cv2

#Opening Image and storing it in variable named 'image'
image = cv2.imread('C:\Users\Subham\Desktop\Python programming\extra files\ex.jpg',1)

#Allowing window to resize
cv2.namedWindow('Image',cv2.WINDOW_NORMAL)

#Showing image in a window named 'Image'
cv2.imshow('Image',image)

#Waiting for any key operation to happen
cv2.waitKey(0)

#Destroying all windows created
cv2.destroyAllWindows();
