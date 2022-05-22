import tkinter as tk
from tkinter.constants import LEFT
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter.messagebox import askokcancel, showinfo, WARNING
from Recognition import recognize_attendence
from DB_MarkAttendance import mark_attendance
from datetime import date
from DB_DownloadAttendance import download_daily_attendance
from PIL import Image, ImageTk
from tkinter_custom_button import hover

attendance_list = []
def main(root, table_name,class_name, subject_name, username):
    
    root.title("Conduct Attendance")
    
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
    #BGLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=10)
    BGLabel["font"] = ft
    BGLabel["justify"] = "center"
    BGLabel["text"] = ""
    BGLabel.place(x=3,y=0,width=735,height=506)

    Back=tk.Button(root)
    Back["bg"] = "#f0f0f0"
    Back["borderwidth"] = "3px"
    ft = tkFont.Font(family='Times',size=13)
    Back["font"] = ft
    Back["fg"] = "#000000"
    Back["justify"] = "center"
    Back["text"] = "Back"
    Back.place(x=10,y=10,width=150,height=45)
    Back["command"] = lambda : Back_command(root, table_name,class_name, subject_name, username)
    hover(Back,"#f0f0f0")

    Logout=tk.Button(root)
    Logout["bg"] = "#f0f0f0"
    Logout["borderwidth"] = "3px"
    ft = tkFont.Font(family='Times',size=13)
    Logout["font"] = ft
    Logout["fg"] = "#000000"
    Logout["justify"] = "center"
    Logout["text"] = "Logout"
    Logout.place(x=580,y=10,width=150,height=45)
    Logout["command"] = lambda : Logout_command(root)
    hover(Logout,"#f0f0f0")

    Divider=tk.Label(root)
    Divider["bg"] = "#90ee90"
    ft = tkFont.Font(family='Times',size=10)
    Divider["font"] = ft
    Divider["fg"] = "#333333"
    Divider["justify"] = "center"
    Divider["text"] = ""
    Divider.place(x=0,y=170,width=741,height=3)

    Title=tk.Label(root)
    Title["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=32)
    Title["font"] = ft
    Title["fg"] = "#ffffff"
    Title["justify"] = "center"
    Title["text"] = "Attendance Panel"
    Title.place(x=0,y=75,width=741,height=75)

    image1 = Image.open("Dataset/start.png")
    image1 = image1.resize((150,150),Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image1)
    Start=tk.Button(root, image = test, compound=LEFT)
    Start.image=test
    Start["bg"] = "#22ee33"
    Start["borderwidth"] = "5px"
    ft = tkFont.Font(family='Times',size=18)
    Start["font"] = ft
    Start["fg"] = "#000000"
    Start["justify"] = "center"
    Start["text"] = "Start\nAttendance"
    Start.place(x=50,y=200,width=300,height=150)
    Start["command"] = lambda : attendance()
    hover(Start,"#22ee33")

    image1 = Image.open("Dataset/stop.png")
    image1 = image1.resize((150,150),Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image1)
    Stop=tk.Button(root, image = test, compound=LEFT)
    Stop.image=test
    today = date.today()
    Stop["bg"] = "#cc0001"
    Stop["borderwidth"] = "5px"
    ft = tkFont.Font(family='Times',size=18)
    Stop["font"] = ft
    Stop["fg"] = "#ffffff"
    Stop["justify"] = "center"
    Stop["text"] = "Save & Stop"
    Stop.place(x=400,y=200,width=300,height=150)
    Stop["command"] = lambda : fill_attendance(table_name)
    hover(Stop,"#cc0011")

    image1 = Image.open("Dataset/download.png")
    image1 = image1.resize((100,100),Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image1)
    Download=tk.Button(root, image = test, compound=LEFT)
    Download.image=test
    Download["bg"] = "#ffd700"
    Download["borderwidth"] = "5px"
    ft = tkFont.Font(family='Times',size=14)
    Download["font"] = ft
    Download["fg"] = "#000000"
    Download["justify"] = "center"
    Download["text"] = "Download Today's Attendance"
    Download.place(x=180,y=390,width=400,height=100)
    Download["command"] = lambda : save_attendance(table_name)
    hover(Download,"#ffd700")

def attendance():
    global attendance_list
    attendance_list = list(recognize_attendence())


def Back_command(root,table_name, class_name, subject_name,username):
    import FacultyMenu as FM
    FM.main(root, table_name,class_name, subject_name,username)

def Logout_command(root):
    answer = askokcancel( title='Logout Confirmation', message='Are You Sure to Logout ?', icon=WARNING)
    if answer :
        import Welcome as welcome
        welcome.main(root)


def Start_command(root):
    pass

def Stop_command(root):
    print("command")


def save_attendance(table_name):
    result = download_daily_attendance(table_name,date.today().strftime("%d_%m_%Y"))

    if result == True:
        messagebox.showinfo("success", "Attendace downloaded successfully!!")
    else:
        messagebox.showerror("error","please contact support team!")



def fill_attendance(table_name):
    result = mark_attendance(table_name,date.today().strftime("%d_%m_%Y"), attendance_list)
    if result == True:
        messagebox.showinfo("success", "Attendace marked successfully!!")
    else:
        messagebox.showerror("error","please contact support team!")
