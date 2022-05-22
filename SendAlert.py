import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter.messagebox import askokcancel, showinfo, WARNING

def main(root):
    
    root.title("Send Alert To")
    
    width=741
    height=509
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)

    image1 = Image.open("Dataset/BG2.png")
    image1 = image1.resize((735,500),Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image1)
    BGLabel=tk.Label(root,image=test)
    BGLabel.image=test
    BGLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=10)
    BGLabel["font"] = ft
    BGLabel["fg"] = "#333333"
    BGLabel["justify"] = "center"
    BGLabel["text"] = ""
    BGLabel.place(x=0,y=0,width=741,height=509)

    Back=tk.Button(root)
    Back["bg"] = "#ffffff"
    Back["borderwidth"] = "3px"
    ft = tkFont.Font(family='Times',size=12)
    Back["font"] = ft
    Back["fg"] = "#000000"
    Back["justify"] = "center"
    Back["text"] = "Back"
    Back.place(x=10,y=10,width=150,height=45)
    Back["command"] = lambda : Back_command(root)

    Logout=tk.Button(root)
    Logout["bg"] = "#ffffff"
    Logout["borderwidth"] = "3px"
    ft = tkFont.Font(family='Times',size=12)
    Logout["font"] = ft
    Logout["fg"] = "#000000"
    Logout["justify"] = "center"
    Logout["text"] = "Logout"
    Logout.place(x=580,y=10,width=150,height=45)
    Logout["command"] = lambda : Logout_command(root)

    Divider=tk.Label(root)
    Divider["bg"] = "#90ee90"
    ft = tkFont.Font(family='Times',size=10)
    Divider["font"] = ft
    Divider["fg"] = "#333333"
    Divider["justify"] = "center"
    Divider["text"] = ""
    Divider.place(x=0,y=130,width=741,height=3)

    TitleLabel=tk.Label(root)
    TitleLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=32)
    TitleLabel["font"] = ft
    TitleLabel["fg"] = "#ffffff"
    TitleLabel["justify"] = "center"
    TitleLabel["text"] = "Select Student"
    TitleLabel.place(x=0,y=60,width=741,height=65)

    SendAlert=tk.Button(root)
    SendAlert["bg"] = "#cc0000"
    ft = tkFont.Font(family='Times',size=16)
    SendAlert["font"] = ft
    SendAlert["fg"] = "#ffffff"
    SendAlert["justify"] = "center"
    SendAlert["text"] = "Send Email Alert"
    SendAlert.place(x=270,y=430,width=229,height=51)
    SendAlert["command"] = lambda : SendAlert_command(root)
    #
    X = 0; Y= 100; Xinc = 70; Yinc = 70
    for i in range(1,10) :
        for j in range (1,8) :
           btn = Button(root)
           btn.place(x = X+Xinc,y=Y+Yinc,width=50,height=50)
           X = X + Xinc
        Y = Y + Yinc


def Back_command(root):
    import Statisticspage as sp
    sp.main(root)


def Logout_command(root):
    answer = askokcancel( title='Logout Confirmation', message='Are You Sure to Logout ?', icon=WARNING)
    if answer :
        import Welcome as welcome
        welcome.main(root)


def SendAlert_command(root):
    print("command")
