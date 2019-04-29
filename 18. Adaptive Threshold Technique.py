#import cv2 and matplotlib
import cv2
from matplotlib import pyplot as plt

#Reading a image
img = cv2.imread('dave.jpg',0)

#Using different threshold operations
ret,thres1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
thres2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
thres3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

#Using matplotlib to display the images
titles = ['Original Image','Global Threshold','Adaptive Threshold','Gaussian Adaptive Threshold']
images = [img,thres1,thres2,thres2]

for i in xrange(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
plt.show()
    