import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkcalendar import DateEntry
import datetime
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter.messagebox import askokcancel, showinfo, WARNING

def main(root, class_name, subject_name):
   
    root.title("Timely Stats")
   
    width=741
    height=509
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)

    image1 = Image.open("Dataset/BG.jpg")
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
    Back["command"] = lambda : Back_command(root, class_name, subject_name)

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
    Divider.place(x=0,y=140,width=741,height=3)

    Title=tk.Label(root)
    Title["bg"] = "#1f93ff"
    ft = tkFont.Font(family='Times',size=32)
    Title["font"] = ft
    Title["fg"] = "#ffffff"
    Title["justify"] = "center"
    Title["text"] = "Statistics"
    Title.place(x=0,y=65,width=741,height=65)

    Show=tk.Button(root)
    Show["bg"] = "#ffd700"
    Show["borderwidth"] = "5px"
    ft = tkFont.Font(family='Times',size=14)
    Show["font"] = ft
    Show["fg"] = "#000000"
    Show["justify"] = "center"
    Show["text"] = "Show"
    Show.place(x=470,y=160,width=102,height=45)
    Show["command"] = lambda : Show_command(root)

    EnterDate = DateEntry(root, width=27, background='brown', foreground='white', date_pattern='dd/mm/Y')
    EnterDate["borderwidth"] = 3
    EnterDate.place(x=200,y=160,width=246,height=45)
    #EnterDate["show"] = "E"

    SelectDateLabel=tk.Label(root)
    SelectDateLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=18)
    SelectDateLabel["font"] = ft
    SelectDateLabel["fg"] = "#ffffff"
    SelectDateLabel["justify"] = "center"
    SelectDateLabel["text"] = "Select Date :"
    SelectDateLabel.place(x=40,y=170,width=154,height=30)

    SendAlertTo=tk.Button(root)
    SendAlertTo["bg"] = "#cc0000"
    ft = tkFont.Font(family='Times',size=14)
    SendAlertTo["font"] = ft
    SendAlertTo["fg"] = "#ffffff"
    SendAlertTo["justify"] = "center"
    SendAlertTo["text"] = "Send Alert To"
    SendAlertTo.place(x=595,y=160,width=120,height=45)
    SendAlertTo["command"] = lambda : SendAlertTo_command(root)

def Back_command(root, class_name, table_name):
    import FacultyMenu as FH
    FH.main(root, class_name, table_name)


def Logout_command(root):
    answer = askokcancel( title='Logout Confirmation', message='Are You Sure to Logout ?', icon=WARNING)
    if answer :
        import Welcome as welcome
        welcome.main(root)

def Show_command(root):
    print("command")

def SendAlertTo_command(root):
    import SendAlert as SA
    SA.main(root)
