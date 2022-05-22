#!/usr/bin/env python
# coding: utf-8

# In[7]:


import cv2
import os
import numpy as np
from PIL import Image
import pickle
import pandas as pd


# In[55]:


def recognize_attendence():
    attendance = set()
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("Trainner.yml")
    harcascadePath = "haarcascade_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    font = cv2.FONT_HERSHEY_SIMPLEX
    # start realtime video capture
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(3, 640) 
    cam.set(4, 480) 
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    while True:
        ret, im = cam.read()
        #im = cv2.imread("Train_Dataset/220200160.0.jpg")
        cv2.putText(im,'Press X to Exit',(5,22),font, 1, (128,0,0), 2)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5,minSize = (int(minW), int(minH)),flags = cv2.CASCADE_SCALE_IMAGE)
        for(x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x+w, y+h), (10, 200, 255), 2)
            Id, conf = recognizer.predict(gray[y:y+h, x:x+w])
            tt = str(Id)
            '''
            cv2.putText(im, str(tt), (x+5,y-5), font, 1, (255, 255, 255), 2)
            cv2.imshow('Attendance', im)
            attendance.add(Id)
            
            '''
            if (100-conf)>50:                                           
                cv2.putText(im, str(tt), (x+5,y-5), font, 1, (255, 255, 255), 2)
                cv2.imshow('Attendance', im)
                attendance.add(Id)
            else:
                cv2.putText(im,"Not Found",(x+5,y-5), font, 1, (255, 255, 255), 2)   
                cv2.imshow('Attendance', im)
        if (cv2.waitKey(1) == ord('x')):
            break
    cam.release()
    cv2.destroyAllWindows()
    return attendance
