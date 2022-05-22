from tkinter import *
from PIL import Image, ImageTk

def getImage(imagepath, w, h) :
    image1 = Image.open(imagepath)
    image1 = image1.resize((w,h), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image1)
    return test