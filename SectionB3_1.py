import cv2
import numpy as np

img=cv2.imread('abhiyaan_opencv_qn1.png')
"""
#Selecting cone image using selectROI function and saving it

b = cv2.selectROI("Tracking",img, False)
x,y,a,b=int(b[0]),int(b[1]),int(b[2]),int(b[3])
cv2.imwrite('cone.jpg',img[y:y+b,x:x+a]

"""
i=cv2.imread('cone.jpg')

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
hsvt=cv2.cvtColor(i,cv2.COLOR_BGR2HSV)
#Converting image and object into hsv
I = cv2.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )
M = cv2.calcHist([hsvt],[0, 1], None, [180, 256], [0, 180, 0, 256] )
cv2.normalize(M,M,0,255,cv2.NORM_MINMAX)
#Histogram Backprojection to identify colours 
dst=cv2.calcBackProject([hsv],[0,1],M,[0,180,0,256],1)
disc=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
#Function to get elliptical shaped 5*5 kernel
cv2.filter2D(dst,-1,disc,dst)
#Convolving image with kernel obtained earlier
ret,thresh = cv2.threshold(dst,30,255,cv2.THRESH_TOZERO)

#Using threshold to limit the number of pixels that have intensities above 30
#It is used to classify pixels as black or white
imgBlur = cv2.GaussianBlur(thresh, (7, 7), 1)
kernel = np.ones((5, 5))
imgCanny = cv2.Canny(imgBlur,20,20)
#Used for edge-linking. The two thresholds are varied through trial and error.
imgDil = cv2.dilate(imgCanny, kernel, iterations=1)
contours,h= cv2.findContours(imgDil, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2:]
#Finding contours in image. Using No chain approximation to obtain a more
#defined contour line.
for cnt in contours:
    area=cv2.contourArea(cnt)
    #Removing contours that are small and inconsequential
    if(area>350):
        p,q,r,s=cv2.boundingRect(cnt)
        #Constructing a bounding rectangle to the contour line
        cv2.rectangle(img,(p,q),(p+r,q+s),(0,255,0),5)
cv2.imshow('final',img)    

