import tkinter as tk
from tkinter import Frame, ttk
from tkinter.constants import BOTTOM, FALSE, LEFT
import tkinter.font as tkFont
from PIL import Image, ImageTk
  
 
def FacultyLoginButton_command(root):
    import FacultyLogin as facultylogin
    facultylogin.main(root)

def AdminLoginButton_command(root):
    import AdminLogin as adminlogin
    adminlogin.main(root)


def main(root):
    
    root.title("Tech Aspires : Welcome")
    for k in root.winfo_children() :
        k.destroy()
    width=741
    height=509
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)

    image1 = Image.open("dataset\BG2.png")
    image1 = image1.resize((735,500),Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image1)
    BGLabel=tk.Label(root, image = test)
    BGLabel.image = test
    BGLabel["anchor"] = "center"
    #BGLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times New Roman',size=10)
    BGLabel["font"] = ft
    #BGLabel["fg"] = "#333333"
    BGLabel["justify"] = "center"
    BGLabel["text"] = "label"
    BGLabel.place(x=3,y=0,width=735,height=505)
    
    
    TitleLabel1=tk.Label(root)
    #TitleLabel1["activeforeground"] = "#01aaed"
    TitleLabel1["anchor"] = "center"
    #TitleLabel1["bg"] = "#5fb878"
    TitleLabel1["bg"] = "#000000"
    TitleLabel1["borderwidth"] = "2px"
    ft = tkFont.Font(family='Times',size=20)
    TitleLabel1["font"] = ft
    TitleLabel1["fg"] = "#fff0ff"
    TitleLabel1["justify"] = "center"
    TitleLabel1["text"] = "   Welcome to MIT Academy of Engineering  "
    TitleLabel1["relief"] = "sunken"
    TitleLabel1.place(x=3,y=0,width=735,height=95)

    TitleLabel2=tk.Label(root)
    TitleLabel2["activebackground"] = "#fad400"
    #TitleLabel2["bg"] = "#90ee90"
    TitleLabel2["bg"] = "#000000"
    ft = tkFont.Font(family='Times',size=16)
    TitleLabel2["font"] = ft
    TitleLabel2["fg"] = "#ffffff"
    TitleLabel2["justify"] = "center"
    TitleLabel2["text"] = "Facial Recognition Attendance System"
    TitleLabel2.place(x=100,y=100,width=550,height=43)

    image1 = Image.open("dataset\\faculty.png")
    image1 = image1.resize((150,152),Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image1)
    FacultyLoginButton=tk.Button(root, image=test, compound=LEFT, command = lambda : FacultyLoginButton_command(root))
    FacultyLoginButton.image=test
    FacultyLoginButton["bg"] = "#f0f0f0"
    FacultyLoginButton["borderwidth"] = "5px"
    ft = tkFont.Font(family='Times',size=15)
    FacultyLoginButton["font"] = ft
    FacultyLoginButton["fg"] = "#000000"
    FacultyLoginButton["justify"] = "center"
    FacultyLoginButton["text"] = "Faculty \n Login"
    FacultyLoginButton.place(x=100,y=200,width=250,height=150)

    image1 = Image.open("dataset\\admin6.png")
    image1 = image1.resize((140,152),Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image1)
    AdminLoginButton=tk.Button(root, image=test, compound=LEFT, command = lambda : AdminLoginButton_command(root))
    AdminLoginButton.image=test
    AdminLoginButton["bg"] = "#f0f0f0"
    AdminLoginButton["borderwidth"] = "5px"
    ft = tkFont.Font(family='Times',size=15)
    AdminLoginButton["font"] = ft
    AdminLoginButton["fg"] = "#000000"
    AdminLoginButton["justify"] = "center"
    AdminLoginButton["text"] = "  Admin \n  Login"
    AdminLoginButton.place(x=400,y=200,width=250,height=150)
    
    def on_enter(e):
        FacultyLoginButton['background'] = '#329da8'
    def on_leave(e):
        AdminLoginButton['background'] = 'SystemButtonFace'
    def on_leave2(e):
        FacultyLoginButton['background'] = 'SystemButtonFace'
    def on_enter2(e):
        AdminLoginButton['background'] = '#329da8'
    FacultyLoginButton.bind("<Enter>", on_enter)
    AdminLoginButton.bind("<Leave>", on_leave)
    FacultyLoginButton.bind("<Leave>", on_leave2)
    AdminLoginButton.bind("<Enter>", on_enter2)
    

    