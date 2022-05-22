import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk
from DB_MakeConnection import make_connection
from DB_helper import execute_query
import FacultyHome as facultyhome
from tkinter.messagebox import showinfo, WARNING, askokcancel
from tkinter import messagebox
import ForgotPassword
from tkinter_custom_button import hover

def main(root):

    root.title("Faculty Login")
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

    Divider = tk.Label(root)
    Divider["bg"] = "#90ee90"
    Divider["fg"] = "#ffffff"
    Divider["anchor"] = "center"
    Divider["justify"] = "center"
    Divider["text"] = ""
    Divider.place(x=0,y=150,width=741,height=2)

    TitleLabel=tk.Label(root)
    TitleLabel["anchor"] = "center"
    TitleLabel["bg"] = "#687bf7"
    ft = tkFont.Font(family='Times New Roman',size=26)
    TitleLabel["font"] = ft
    TitleLabel["fg"] = "#000000"
    TitleLabel["justify"] = "center"
    TitleLabel["text"] = "Faculty        Login"
    TitleLabel["relief"] = "flat"
    TitleLabel.place(x=10,y=10,width=722,height=125)

    UsernameLabel=tk.Label(root)
    UsernameLabel["bg"] = "#999999"
    ft = tkFont.Font(family='Times',size=14)
    UsernameLabel["font"] = ft
    UsernameLabel["fg"] = "#000000"
    UsernameLabel["justify"] = "center"
    UsernameLabel["text"] = "Username"
    UsernameLabel.place(x=150,y=190,width=156,height=43)

    ForgotPasswordButton=tk.Button(root)
    ForgotPasswordButton["bg"] = "#393d49"
    ForgotPasswordButton["borderwidth"] = 0
    ft = tkFont.Font(family='Times',size=14, weight="bold")
    ft.configure(underline=True)
    ForgotPasswordButton["font"] = ft
    ForgotPasswordButton["bd"] = 0
    ForgotPasswordButton["cursor"] = "hand2"
    ForgotPasswordButton["highlightcolor"] = "#393d49"
    ForgotPasswordButton["highlightbackground"] = "#393d49"
    ForgotPasswordButton["fg"] = "#1E90FF"
    ForgotPasswordButton["justify"] = "center"
    ForgotPasswordButton["text"] = "Change Password"
    ForgotPasswordButton.place(x=480,y=340,width=157,height=25)
    ForgotPasswordButton["command"] = lambda : ForgotPasswordButton_command(root, UsernameField.get())
    hover(ForgotPasswordButton,"#393d49")

    UsernameField=tk.Entry(root)
    UsernameField["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=14)
    UsernameField["font"] = ft
    UsernameField["fg"] = "#000000"
    UsernameField["justify"] = "center"
    UsernameField["text"] = ""
    UsernameField.place(x=350,y=190,width=288,height=39)

    PasswordLabel=tk.Label(root)
    PasswordLabel["bg"] = "#999999"
    ft = tkFont.Font(family='Times',size=14)
    PasswordLabel["font"] = ft
    PasswordLabel["fg"] = "#000000"
    PasswordLabel["justify"] = "center"
    PasswordLabel["text"] = "Password"
    PasswordLabel.place(x=150,y=260,width=158,height=42)

    PasswordField=tk.Entry(root, show = '*')
    PasswordField["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=14)
    PasswordField["font"] = ft
    PasswordField["fg"] = "#000000"
    PasswordField["justify"] = "center"
    PasswordField["text"] = ""
    PasswordField.place(x=350,y=260,width=288,height=40)

    BackButton=tk.Button(root)
    BackButton["bg"] = "#f0f0f0"
    ft = tkFont.Font(family='Times',size=14)
    BackButton["font"] = ft
    BackButton["fg"] = "#000000"
    BackButton["justify"] = "center"
    BackButton["text"] = "Back"
    #BackButton["border"] = "5px"
    BackButton.place(x=150,y=410,width=156,height=47)
    BackButton["command"] = lambda : BackButton_command(root)
    hover(BackButton,"#f0f0f0")

    SubmitButton=tk.Button(root)
    SubmitButton["bg"] = "#24a0ed"
    ft = tkFont.Font(family='Times',size=14)
    SubmitButton["font"] = ft
    SubmitButton["fg"] = "#000000"
    SubmitButton["cursor"] = "hand2"
    SubmitButton["justify"] = "center"
    SubmitButton["text"] = "Login"
    #SubmitButton["border"] = "5px"
    SubmitButton.place(x=350,y=410,width=188,height=47)
    SubmitButton["command"] = lambda : SubmitButton_command(root,  UsernameField.get(), PasswordField.get())
    SubmitButton.place(x=350,y=410,width=288,height=47)
    hover(SubmitButton)

def ForgotPasswordButton_command(root, email_id):
    connection = make_connection()
    print(email_id)

    try:
        query = f"select * from faculty_records where email_id = '{email_id}'" 
        result = execute_query(query,connection).fetchall()
        print(result)
        if len(result) < 1:
            messagebox.showerror("Error","Invalid Email_id!")
        else:
            ForgotPassword.main(root, 'F', email_id,'faculty_records')
    except:
        messagebox.showerror("Error","Invalid Email_id!") 
    

def BackButton_command(root) :
    import Welcome as welcome
    welcome.main(root)

def SubmitButton_command(root, email_id, password):
    connection = make_connection()
    valid_password = ''
    try:
        query = f"select password from faculty_records where email_id = '{email_id}'" 
        valid_password = execute_query(query, connection).fetchall()
        if password == valid_password[0][0]:
            facultyhome.main(root, email_id)
        else:
            messagebox.showerror("Error","Invalid Password!")
    except:
        messagebox.showerror("Error","Invalid Email_id!")

    

    
    


    