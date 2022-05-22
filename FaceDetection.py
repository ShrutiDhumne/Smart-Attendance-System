#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2 as cv
import os
import pandas as pd
import datetime


# In[2]:


def captureImage(prn):
    i =0
    font = cv.FONT_HERSHEY_SIMPLEX
    while(i<3):
        cam = cv.VideoCapture(0)
        harcascadePath = "haarcascade_default.xml"
        detector = cv.CascadeClassifier(harcascadePath)
        while(True):
            ret, img = cam.read()
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            cv.putText(img,'Image '+str(i+1)+' --> Press X to Capture',(5,22),font, 1, (128,0,0), 2)
            faces = detector.detectMultiScale(gray, 1.3, 5, minSize=(30,30),flags = cv.CASCADE_SCALE_IMAGE)
            for(x,y,w,h) in faces:
                cv.rectangle(img, (x, y), (x+w, y+h), (10, 159, 255), 2)
                cv.imwrite("Train_Dataset/"+str(prn)+"."+str(i)+".jpg", gray[y:y+h, x:x+w])
                cv.imshow('frame', img)
            if cv.waitKey(100) & 0xFF == ord('x'):
                break
        cam.release()
        cv.destroyAllWindows()
        i+=1

        
    return True