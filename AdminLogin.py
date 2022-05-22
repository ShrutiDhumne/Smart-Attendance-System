import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk
import AdminHome as adminhome
from DB_MakeConnection import make_connection
from tkinter.messagebox import showinfo, WARNING, askokcancel
from tkinter import messagebox
from DB_helper import execute_query
from DB_MakeConnection import make_connection
from tkinter_custom_button import hover

def main(root):

    root.title("Admin Login")
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
    TitleLabel["bg"] = "lightblue"
    TitleLabel["cursor"] = "man"
    ft = tkFont.Font(family='Times',size=26)
    TitleLabel["font"] = ft
    TitleLabel["fg"] = "#000000"
    TitleLabel["justify"] = "center"
    TitleLabel["text"] = "Admin        Login"
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
    ft = tkFont.Font(family='Times',size=12, weight="bold")
    ft.configure(underline=True)
    ForgotPasswordButton["font"] = ft
    ForgotPasswordButton["cursor"] = "hand2"
    ForgotPasswordButton["bd"] = 0
    ForgotPasswordButton["highlightcolor"] = "#ffffff"
    ForgotPasswordButton["highlightbackground"] = "#393d49"
    ForgotPasswordButton["fg"] = "#1E90FF"
    ForgotPasswordButton["justify"] = "center"
    ForgotPasswordButton["text"] = "Change Password"
    ForgotPasswordButton.place(x=480,y=340,width=157,height=25)
    ForgotPasswordButton["command"] = lambda : ForgotPasswordButton_command(root, EnterEmail.get())
    hover(ForgotPasswordButton,"#393d49")

    EnterEmail=tk.Entry(root)
    EnterEmail["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=14)
    EnterEmail["font"] = ft
    EnterEmail["bg"] = "#393d49"
    EnterEmail['border'] = "3px"
    EnterEmail["fg"] = "#ffffff"
    EnterEmail["justify"] = "center"
    EnterEmail["text"] = ""
    EnterEmail.place(x=350,y=190,width=288,height=39)

    PasswordLabel=tk.Label(root)
    PasswordLabel["bg"] = "#999999"
    ft = tkFont.Font(family='Times',size=14)
    PasswordLabel["font"] = ft
    PasswordLabel["fg"] = "#000000"
    PasswordLabel["justify"] = "center"
    PasswordLabel["text"] = "Password"
    PasswordLabel.place(x=150,y=260,width=158,height=42)

    EnterPassword=tk.Entry(root, show='*')
    EnterPassword["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=14)
    EnterPassword['border'] = "3px"
    EnterPassword["bg"] = "#393d49"
    EnterPassword["font"] = ft
    EnterPassword["fg"] = "#ffffff"
    EnterPassword["justify"] = "center"
    EnterPassword["text"] = ""
    EnterPassword.place(x=350,y=260,width=288,height=40)

    Back=tk.Button(root)
    Back["bg"] = "#f0f0f0"
    #Back["borderwidth"] = "5px"
    ft = tkFont.Font(family='Times',size=15)
    Back["font"] = ft
    Back["fg"] = "#000000"
    Back["justify"] = "center"
    Back["text"] = "Back"
    Back.place(x=150,y=410,width=156,height=47)
    Back["command"] = lambda : Back_command(root)
    hover(Back,"#f0f0f0")

    Submit=tk.Button(root)
    Submit["bg"] = "#24a0ed"
    Submit["borderwidth"] = "5px"
    ft = tkFont.Font(family='Times',size=15)
    Submit["font"] = ft
    Submit["fg"] = "#000000"
    Submit["justify"] = "center"
    Submit["text"] = "Login"
    Submit.place(x=350,y=410,width=288,height=47)
    Submit["command"] = lambda : Submit_command(root, EnterEmail.get(), EnterPassword.get())
    hover(Submit)

def ForgotPasswordButton_command(root, email_id):
    
    connection = make_connection()
    print(email_id)
    try:
        query = f"select * from admin where email_id = '{email_id}'" 
        result = execute_query(query,connection).fetchall()
        print(result)
        if len(result) < 1:
            messagebox.showerror("Error","Invalid Email_id!")
        else:
            query = f"select password from admin where email_id = '{email_id}'" 
            valid_password = execute_query(query, connection).fetchall()
            import ForgotPassword as forgotpassword
            forgotpassword.main(root, 'A', email_id, 'admin')
    except:
        messagebox.showerror("Error","Invalid Email_id!")


def Back_command(root):
    import Welcome as welcome
    welcome.main(root)


def Submit_command(root, username, password):
    connection = make_connection()
    valid_password = ''
    
    
    try:
        query = f"select password from admin where email_id = '{username}'" 
        valid_password = execute_query(query, connection).fetchall()
        if password == valid_password[0][0]:
            adminhome.main(root, username)
        else:
            messagebox.showerror("Error","Invalid Password!")
    except:
        messagebox.showerror("Error","Invalid username!")

