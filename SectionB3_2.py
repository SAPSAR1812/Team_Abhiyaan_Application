import cv2 
import numpy as np

f=cv2.CascadeClassifier('fullbody.xml')
#Haar_cascade classifier downloaded from github:
#https://github.com/opencv/opencv/tree/master/data/haarcascades
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture('peds.mp4')
cap.set(3, frameWidth)
cap.set(4, frameHeight)

while True:
    try:
        success,img=cap.read()
        

        imgBlur = cv2.GaussianBlur(img, (7, 7), 1)
        imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)
        imgGray = cv2.equalizeHist(imgGray)
        #Blurring and converting the image to Grayscale for feature detection
        #Further pre-processing tends to reduce accuracy.
        peeps=f.detectMultiScale(imgGray,1.1,maxSize=(50,80))
        #Using detectMultiScale with the Trainer loaded in f
        for x,y,a,b in peeps:
            cv2.rectangle(img,(x,y),(x+a,y+b),(0,255,0),2)
            
        cv2.imshow('Vid',img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except:
         
         break
