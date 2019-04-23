
import cv2
import numpy as np

drawing = True

ix,iy = -1,-1
erase= True






def paint(event,x,y,glags,param):
    global ix,iy,drawing,erase,trackbar

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if erase == False:
               cv2.circle(img,(x,y),2,(0,0,255),-1)

               def nothing(x):
                return()


               trackbar = np.zeros((300,512,3), np.uint8)
               cv2.namedWindow("trackbar")
               cv2.createTrackbar('R','trackbar',0,255,nothing)
               cv2.createTrackbar('G','trackbar',0,255,nothing)
               cv2.createTrackbar('B','trackbar',0,255,nothing)

            else:
               cv2.rectangle(img,(x,y),(ix,iy),(0,120,0),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False


img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',paint)

while(1):
        cv2.imshow('image',img)


        r = cv2.getTrackbarPos('R','trackbar')
        g = cv2.getTrackbarPos('G','trackbar')
        b = cv2.getTrackbarPos('B','trackbar')

        k = cv2.waitKey(1) & 0xFF
        if k == ord('m'):
             erase = not erase
        elif k == 27:
            break
cv2.destroyAllWindows()