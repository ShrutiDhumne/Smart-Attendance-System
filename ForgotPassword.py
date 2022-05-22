from email.message import EmailMessage
import tkinter as tk
import tkinter.font as tkFont
from tkinter import * 
import tkinter.ttk as ttk
from tkinter.ttk import Progressbar
import time
from tkinter import messagebox
from tkinter.messagebox import askokcancel, showinfo, WARNING
import GetImage as GM
from DB_MakeConnection import make_connection
import Email4 as email
from tkinter_custom_button import hover

OTP = ''
spam = 0

def main(root, token, email_id, table_name) :
    
    root.title("Forgot Password")
    width=741
    height=509
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)

    test = GM.getImage('Dataset/BG2.png',735,503)
    BGLabel=tk.Label(root,image=test)
    BGLabel.image=test
    #BGLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=10)
    BGLabel["font"] = ft
    #BGLabel["fg"] = "#333333"
    BGLabel["justify"] = "center"
    BGLabel["text"] = ""
    BGLabel.place(x=3,y=0,width=735,height=506)

    TitleLabel=tk.Label(root)
    TitleLabel["bg"] = "#da4242"
    ft = tkFont.Font(family='Times',size=28)
    TitleLabel["font"] = ft
    TitleLabel["fg"] = "#ffffff"
    TitleLabel["justify"] = "center"
    TitleLabel["text"] = "Forgot Password ? "
    TitleLabel.place(x=3,y=70,width=735,height=70)
    
    Back=tk.Button(root)
    Back.image=test
    Back["borderwidth"] = "4px"
    ft = tkFont.Font(family='Times',size=12)
    Back["font"] = ft
    Back["bg"] = "#f0f0f0"
    Back["fg"] = "#000000"
    Back["justify"] = "center"
    Back["text"] = "Back"
    Back.place(x=10,y=15,width=158,height=40)
    Back["command"] = lambda : Back_command(root,token)
    hover(Back)

    TitleLabel2=tk.Label(root)
    TitleLabel2["bg"] = "#00ced1"
    ft = tkFont.Font(family='Times',size=26)
    TitleLabel2["font"] = ft
    TitleLabel2["fg"] = "#000000"
    TitleLabel2["justify"] = "center"
    TitleLabel2["text"] = "Verify Yourself"
    TitleLabel2.place(x=170,y=150,width=420,height=45)

    SendOTP=tk.Button(root)
    SendOTP["bg"] = "#009655"
    SendOTP["borderwidth"] = "4px"
    ft = tkFont.Font(family='Times',size=14)
    SendOTP["font"] = ft
    SendOTP["fg"] = "#000000"
    SendOTP["justify"] = "center"
    SendOTP["text"] = "Send OTP"
    SendOTP.place(x=240,y=240,width=285,height=51)
    SendOTP["command"] = lambda : SendOTP_command(root, email_id)
    hover(SendOTP,"#009655")

    Validate=tk.Button(root)
    Validate["bg"] = "#009655"
    Validate["borderwidth"] = "5px"
    ft = tkFont.Font(family='Times',size=14)
    Validate["font"] = ft
    Validate["fg"] = "#000000"
    Validate["justify"] = "center"
    Validate["text"] = "Validate OTP"
    Validate.place(x=240,y=440,width=285,height=51)
    Validate["command"] = lambda : Validate_command(root,token,EnterOTP.get(),email_id, table_name)
    hover(Validate,"#009655")

    EnterOTP=tk.Entry(root)
    EnterOTP["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=16)
    EnterOTP["bg"] = "#000000"
    EnterOTP["font"] = ft
    EnterOTP["fg"] = "#1f93ff"
    EnterOTP["justify"] = "center"
    EnterOTP["text"] = ""
    EnterOTP.place(x=300,y=340,width=290,height=45)

    EnterOTPLabel=tk.Label(root)
    EnterOTPLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=14)
    EnterOTPLabel["font"] = ft
    EnterOTPLabel["fg"] = "#ffffff"
    EnterOTPLabel["justify"] = "center"
    EnterOTPLabel["text"] = "Enter OTP :"
    EnterOTPLabel.place(x=170,y=340,width=115,height=45)

def Back_command(root, token):
    if token == 'F' :
        import FacultyLogin as facultylogin
        facultylogin.main(root)
    elif token == 'A' :
        import AdminLogin as adminlogin
        adminlogin.main(root)
    global spam;    spam = 0

def Validate_command(root, token, otp, email_id, table_name):
    ttk.Style().configure("grey.Horizontal.TProgressbar", background='green')
    progress = Progressbar(root, orient = HORIZONTAL, length = 100, style = "grey.Horizontal.TProgressbar", mode = 'determinate')
    progress.grid(column=0, row=0)
    progress.place(x=200, y=25, width=350, height=30)
    for i in range(1,99):
        progress['value'] = i
        root.update_idletasks()
        time.sleep(0.01)
        progress['value'] = i+1
    progress.lower()
    global OTP
    if str(OTP) == str(otp) and str(OTP) != '' :
        import ResetPassword as rp
        rp.main(root, token, email_id, table_name)
    else :
        messagebox.showerror("OTP Verification Failed", "Wrong : Incorrect OTP\nTry Again")
        global spam
        spam = spam + 1       
        if spam == 5 :  Spamcall(root)

def Spamcall(root) :
    test = GM.getImage("dataset/oops.jpg",675,450)
    oops = tk.Label(root,image=test)
    oops.image = test;  oops["justify"] = "center"
    oops.place(x=40,y=70)

def UsingEmail_command(E,EnterContact):
    if E == 1 :
        EnterContact["text"] = "Enter Email ID :"
    
def UsingMobile_command(M,EnterContact):
    if M == 2 :
        EnterContact["text"] = "Enter Mobile :"

def SendOTP_command(root,email_id):
    connection = make_connection()
    global OTP
    OTP = email.Email_4(str(email_id),str(email_id))
    messagebox.showinfo('successful',f"OTP sent successfully to {email_id}")
