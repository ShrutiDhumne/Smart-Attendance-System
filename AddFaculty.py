import tkinter as tk
import Email4 as Email
import AdminHome as adminhome
from PIL import Image, ImageTk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter.messagebox import askokcancel, showinfo, WARNING
from DB_FacultyRecords import add_faculty_record

def main(root, username):

    root.title("Add Faculty")
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
    BGLabel["anchor"] = "center"
    BGLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=10)
    BGLabel["font"] = ft
    BGLabel["fg"] = "#333333"
    BGLabel["justify"] = "center"
    BGLabel["text"] = "label"
    BGLabel.place(x=0,y=0,width=741,height=508)

    TitleLabel=tk.Label(root)
    TitleLabel["bg"] = "#00ced1"
    ft = tkFont.Font(family='Times',size=28)
    TitleLabel["font"] = ft
    TitleLabel["fg"] = "#333333"
    TitleLabel["justify"] = "center"
    TitleLabel["text"] = "Add Faculty"
    TitleLabel.place(x=0,y=50,width=741,height=63)

    EnterEmail=tk.Entry(root)
    EnterEmail["bg"] = "#393d49"
    EnterEmail["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=12)
    EnterEmail["font"] = ft
    EnterEmail["fg"] = "#ffffff"
    EnterEmail["justify"] = "center"
    EnterEmail["text"] = "Email ID"
    EnterEmail.place(x=380,y=200,width=310,height=45)

    EnterName=tk.Entry(root)
    EnterName["bg"] = "#393d49"
    EnterName["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=12)
    EnterName["font"] = ft
    EnterName["fg"] = "#ffffff"
    EnterName["justify"] = "center"
    EnterName["text"] = "Name"
    EnterName.place(x=380,y=300,width=310,height=45)

    EnterEmailLabel=tk.Label(root)
    EnterEmailLabel["bg"] = "#999999"
    ft = tkFont.Font(family='Times',size=14)
    EnterEmailLabel["font"] = ft
    EnterEmailLabel["fg"] = "#000000"
    EnterEmailLabel["justify"] = "center"
    EnterEmailLabel["text"] = "Enter Faculty Email ID"
    EnterEmailLabel.place(x=90,y=200,width=250,height=45)

    EnterNameLabel=tk.Label(root)
    EnterNameLabel["bg"] = "#999999"
    ft = tkFont.Font(family='Times',size=14)
    EnterNameLabel["font"] = ft
    EnterNameLabel["fg"] = "#000000"
    EnterNameLabel["justify"] = "center"
    EnterNameLabel["text"] = "Faculty Name"
    EnterNameLabel.place(x=90,y=300,width=250,height=45)

    SendEmailOTP=tk.Button(root)
    SendEmailOTP["bg"] = "#90ee90"
    SendEmailOTP["borderwidth"] = "5px"
    ft = tkFont.Font(family='Times',size=14)
    SendEmailOTP["font"] = ft
    SendEmailOTP["fg"] = "#000000"
    SendEmailOTP["justify"] = "center"
    SendEmailOTP["text"] = "Generate and Send Credentials"
    SendEmailOTP.place(x=230,y=380,width=335,height=48)
    SendEmailOTP["command"] = lambda :  SendEmail_command(EnterEmail.get(), EnterName.get())

    Back=tk.Button(root)
    Back["bg"] = "#f0f0f0"
    ft = tkFont.Font(family='Times',size=12)
    Back["font"] = ft
    Back["fg"] = "#000000"
    Back["justify"] = "center"
    Back["text"] = "Back"
    Back.place(x=10,y=10,width=140,height=30)
    Back["command"] = lambda : Back_command(root, username)

    Logout=tk.Button(root)
    Logout["bg"] = "#f0f0f0"
    ft = tkFont.Font(family='Times',size=12)
    Logout["font"] = ft
    Logout["fg"] = "#000000"
    Logout["justify"] = "center"
    Logout["text"] = "Logout"
    Logout.place(x=590,y=10,width=140,height=30)
    Logout["command"] = lambda : Logout_command(root)


def SendEmail_command(email, name):
    Status = Email.Email_4(str(email), str(name))
    if Status == 404 :
        messagebox.showerror("Could not send Email", "Error : The Mail couldn't be sent\nPlease check the Email-ID or try again")
    else :
        result = add_faculty_record(name, email, Status, 'faculty_records')
        if result == False:
            messagebox.showerror("error","faculty already exist!!")
        else:
            messagebox.showinfo("Success", "OTP has been sent by email successfully")

def Back_command(root, username):
    adminhome.main(root, username)

def Logout_command(root):
    answer = askokcancel( title='Logout Confirmation', message='Are you sure to logout ?', icon=WARNING)
    if answer :
        import Welcome as welcome
        welcome.main(root)
