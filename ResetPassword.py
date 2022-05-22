import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter.messagebox import askokcancel, showinfo, WARNING
from DB_MakeConnection import make_connection
from DB_helper import execute_query

def main(root, token, email_id, table_name):
    #setting title
    root.title("Reset Password")
    #setting window size
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
    BGLabel.image = test
    #BGLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=10)
    BGLabel["font"] = ft
    #BGLabel["fg"] = "#333333"
    BGLabel["justify"] = "center"
    BGLabel["text"] = ""
    BGLabel.place(x=3,y=0,width=735,height=506)

    TitleLabel=tk.Label(root)
    TitleLabel["anchor"] = "center"
    TitleLabel["bg"] = "#01aaed"
    TitleLabel["borderwidth"] = "5px"
    ft = tkFont.Font(family='Times',size=20)
    TitleLabel["font"] = ft
    TitleLabel["fg"] = "#ffffff"
    TitleLabel["justify"] = "center"
    TitleLabel["text"] = "Reset Password"
    TitleLabel.place(x=120,y=60,width=521,height=79)

    NewPasswordLabel=tk.Label(root)
    NewPasswordLabel["bg"] = "#999999"
    NewPasswordLabel["borderwidth"] = "3px"
    ft = tkFont.Font(family='Times',size=14)
    NewPasswordLabel["font"] = ft
    NewPasswordLabel["fg"] = "#000000"
    NewPasswordLabel["justify"] = "center"
    NewPasswordLabel["text"] = "New Password"
    NewPasswordLabel.place(x=120,y=240,width=165,height=45)

    ReEnterPasswordLabel=tk.Label(root)
    ReEnterPasswordLabel["bg"] = "#999999"
    ReEnterPasswordLabel["borderwidth"] = "3px"
    ft = tkFont.Font(family='Times',size=14)
    ReEnterPasswordLabel["font"] = ft
    ReEnterPasswordLabel["fg"] = "#000000"
    ReEnterPasswordLabel["justify"] = "center"
    ReEnterPasswordLabel["text"] = "Re-enter Password"
    ReEnterPasswordLabel.place(x=120,y=340,width=167,height=46)

    EnterNewPassword=tk.Entry(root, show = '*')
    EnterNewPassword["bg"] = "#000000"
    EnterNewPassword["borderwidth"] = "2px"
    ft = tkFont.Font(family='Times New Roman',size=14)
    EnterNewPassword["font"] = ft
    EnterNewPassword["fg"] = "#ffffff"
    EnterNewPassword["justify"] = "center"
    EnterNewPassword["text"] = ""
    EnterNewPassword.place(x=340,y=240,width=299,height=41)

    ConfirmPassword=tk.Entry(root, show = '*')
    ConfirmPassword["bg"] = "#000000"
    ConfirmPassword["borderwidth"] = "2px"
    ft = tkFont.Font(family='Times',size=14)
    ConfirmPassword["font"] = ft
    ConfirmPassword["fg"] = "#ffffff"
    ConfirmPassword["justify"] = "center"
    ConfirmPassword["text"] = ""
    ConfirmPassword.place(x=340,y=340,width=300,height=42)

    Done=tk.Button(root)
    Done["bg"] = "#009688"
    Done["borderwidth"] = "3px"
    ft = tkFont.Font(family='Times',size=14)
    Done["font"] = ft
    Done["fg"] = "#000000"
    Done["justify"] = "center"
    Done["text"] = "Done"
    Done.place(x=250,y=440,width=300,height=45)
    Done["command"] = lambda : Done_command(root, ConfirmPassword.get(), EnterNewPassword.get(), token, email_id, table_name)

    CheckVar1 = tk.IntVar()
    CheckVar2 = tk.IntVar()
    C1 = Checkbutton(root, variable = CheckVar1, onvalue = 1, offvalue = 0)
    C2 = Checkbutton(root, variable = CheckVar2, onvalue = 1, offvalue = 0)
    C1.grid(row=6, columnspan=3);   C2.grid(row=6, columnspan=3)
    C1["command"] = lambda : SHpassword(CheckVar1,EnterNewPassword)
    C2["command"] = lambda : SHpassword(CheckVar2,ConfirmPassword)
    C1.place(x=650,y=245,width=30,height=30)
    C2.place(x=650,y=345,width=30,height=30)

def SHpassword(C,P) :
    if C.get() == True :    P["show"] = ""
    else : P["show"] = "*"


def Done_command(root, C, N, token, email_id, table_name):
    from tkinter import messagebox
    from tkinter.messagebox import askokcancel, showinfo, WARNING
    if token == 'F' : string = 'Faculty'
    else : string = 'Admin'
    if C != N : 
        messagebox.showerror("Password does not match", "Error : The re-entered password does not match.")
    else :
        connection = make_connection()
        messagebox.showinfo("Success", string+" Password changed successfully !")
        query = f"update {table_name} set password='{C}' where email_id= '{email_id}'"
        execute_query(query,connection)
        if token == 'F':
            import FacultyLogin as FL
            FL.main(root)
        else :
            import AdminLogin as AL
            AL.main(root)