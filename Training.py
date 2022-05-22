#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import time
import cv2
import numpy as np
from PIL import Image
from threading import Thread


# In[4]:


def getImagesAndLabels(path):
    # path of all the files in the folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    # empty ID list
    Ids = []
    for imagePath in imagePaths:
        pilImage = Image.open(imagePath).convert('L')
        imageNp = np.array(pilImage, 'uint8')
        Id = int(os.path.split(imagePath)[1].split(".")[0])
        faces.append(imageNp)
        Ids.append(Id)
    return faces, Ids


# In[5]:


def counter_img(path):
    imgcounter = 1
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    for imagePath in imagePaths:
        print(str(imgcounter) + " Images Trained", end="\r")
        time.sleep(0.008)
        imgcounter += 1


# In[9]:


def TrainImages():
    try:
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        harcascadePath = "haarcascade_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        faces, Id = getImagesAndLabels("Train_dataset")
        Thread(target = recognizer.train(faces, np.array(Id))).start()
        Thread(target = counter_img("Train_dataset")).start()
        recognizer.save("Trainner.yml")
    except:
        return False
    return True
    



