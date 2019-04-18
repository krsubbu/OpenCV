#importing cv2
import cv2

#Opening Image and storing it in variable named 'image'
image = cv2.imread('C:\Users\Subham\Desktop\Python programming\extra files\ex.jpg',0)

#Allowing window to resize
cv2.namedWindow('Image',cv2.WINDOW_NORMAL)

#Showing image in a window named 'Image'
cv2.imshow('Image',image)

#Waiting for any key operation to happen
key = cv2.waitKey(0)

#Writing the condition to save the file and then destroy all windows
#chr(key) convert the ASCII value to charachter
if(chr(key)== 's'):
    cv2.imwrite('black&white.jpg',image)
    cv2.destroyAllWindows();
    
#Another event for only closing operation
if(key == 27):
    cv2.destroyAllWindows();
