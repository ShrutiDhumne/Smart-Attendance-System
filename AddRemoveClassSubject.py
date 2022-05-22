import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter.messagebox import askokcancel, showinfo, WARNING
from DB_AddRemoveClassSubject import  add_class, remove_class, add_subject, remove_subject

def main(root, username):
    #setting title
    root.title("Edit Class-Subject Data")
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
    BGLabel["borderwidth"] = "3px"
    ft = tkFont.Font(family='Times',size=10)
    BGLabel["font"] = ft
    BGLabel["justify"] = "center"
    BGLabel["text"] = "label"
    BGLabel.place(x=3,y=0,width=735,height=506)

    TitleLabel=tk.Label(root)
    TitleLabel["bg"] = "#00ced1"
    ft = tkFont.Font(family='Times',size=26)
    TitleLabel["font"] = ft
    TitleLabel["fg"] = "#000000"
    TitleLabel["justify"] = "center"
    TitleLabel["text"] = "Add / Remove Class and Subjects"
    TitleLabel.place(x=0,y=50,width=741,height=63)

    RemoveSubjects=tk.Button(root)
    RemoveSubjects["bg"] = "#90f090"
    RemoveSubjects["borderwidth"] = "3px"
    ft = tkFont.Font(family='Times',size=18)
    RemoveSubjects["font"] = ft
    RemoveSubjects["fg"] = "#000000"
    RemoveSubjects["justify"] = "center"
    RemoveSubjects["text"] = "Remove Subject"
    RemoveSubjects.place(x=460,y=330,width=200,height=45)
    RemoveSubjects["command"] = lambda : remove_subject_command(root, Class, Subject)

    Back=tk.Button(root)
    Back["bg"] = "#f0f0f0"
    ft = tkFont.Font(family='Times',size=10)
    Back["font"] = ft
    Back["fg"] = "#000000"
    Back["justify"] = "center"
    Back["text"] = "Back"
    Back.place(x=10,y=10,width=140,height=30)
    Back["command"] = lambda : Back_command(root, username)

    Logout=tk.Button(root)
    Logout["bg"] = "#f0f0f0"
    ft = tkFont.Font(family='Times',size=10)
    Logout["font"] = ft
    Logout["fg"] = "#000000"
    Logout["justify"] = "center"
    Logout["text"] = "Logout"
    Logout.place(x=590,y=10,width=140,height=30)
    Logout["command"] = lambda : Logout_command(root)

    RemoveClass=tk.Button(root)
    RemoveClass["bg"] = "#90f090"
    RemoveClass["borderwidth"] = "3px"
    ft = tkFont.Font(family='Times',size=18)
    RemoveClass["font"] = ft
    RemoveClass["fg"] = "#000000"
    RemoveClass["justify"] = "center"
    RemoveClass["text"] = "Remove Class"
    RemoveClass.place(x=90,y=330,width=200,height=45)
    RemoveClass["command"] = lambda : remove_class_command(root, Class)

    Divider=tk.Label(root)
    Divider["bg"] = "#90ee90"
    ft = tkFont.Font(family='Times',size=10)
    Divider["font"] = ft
    Divider["fg"] = "#333333"
    Divider["justify"] = "center"
    Divider["text"] = ""
    Divider.place(x=360,y=113,width=3,height=500)

    Class = ttk.Combobox(root, width = 27, textvariable = tk.StringVar())
    Class.place(x=80,y=180,width=220,height=45)
    Class['values'] = ('Enter Class',  'first_year','second_year','third_year','fourth_year')
    Class.current(0)

    SelectClassLabel=tk.Label(root)
    SelectClassLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=16)
    SelectClassLabel["font"] = ft
    SelectClassLabel.place(x=90,y=140,width=204,height=30)
    SelectClassLabel["fg"] = "#ffffff"
    SelectClassLabel["justify"] = "center"
    SelectClassLabel["text"] = "Select Class"

    Subject=tk.Entry(root)
    Subject["bg"] = "#393d49"
    Subject["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=14)
    Subject["font"] = ft
    Subject["fg"] = "#ffffff"
    Subject["justify"] = "center"
    Subject["text"] = ""
    Subject.place(x=460,y=180,width=215,height=45)

    SelectSubjectLabel=tk.Label(root)
    SelectSubjectLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=16)
    SelectSubjectLabel["font"] = ft
    SelectSubjectLabel["fg"] = "#ffffff"
    SelectSubjectLabel["justify"] = "center"
    SelectSubjectLabel["text"] = "Select Subject"
    SelectSubjectLabel.place(x=480,y=140,width=179,height=30)

    AddClassButton=tk.Button(root)
    AddClassButton["bg"] = "#90ee90"
    AddClassButton["borderwidth"] = "3px"
    ft = tkFont.Font(family='Times',size=18)
    AddClassButton["font"] = ft
    AddClassButton["fg"] = "#000000"
    AddClassButton["justify"] = "center"
    AddClassButton["text"] = "Add Class"
    AddClassButton.place(x=90,y=260,width=200,height=45)
    AddClassButton["command"] = lambda : add_class_command(root, Class)

    AddSubjectButton=tk.Button(root)
    AddSubjectButton["bg"] = "#90ee90"
    AddSubjectButton["borderwidth"] = "3px"
    ft = tkFont.Font(family='Times',size=16)
    AddSubjectButton["font"] = ft
    AddSubjectButton["fg"] = "#000000"
    AddSubjectButton["justify"] = "center"
    AddSubjectButton["text"] = "Add Subject"
    AddSubjectButton.place(x=460,y=260,width=200,height=45)
    AddSubjectButton["command"] = lambda : add_subject_command(root, Class, Subject)

def Back_command(root, username):
    import AdminHome as adminhome
    adminhome.main(root, username)

def Logout_command(root):
    answer = askokcancel( title='Logout Confirmation', message='Are You Sure to Logout ?', icon=WARNING)
    if answer :
        import Welcome as welcome
        welcome.main(root)

def CommitChanges_command(root):
    Status = 1
    if Status == 404 :
        messagebox.showerror("Something went wrong", "Oops ! : Changes couldn't be committed\nWait and try again")
    else :
        messagebox.showinfo("Saved", "Records added/modified successfully")
    main(root)

def remove_class_command(root, Class):
    result = remove_class(Class)

    if result == False:
        messagebox.showerror('error1',"Class does not exist!!")
    else:
        messagebox.showinfo('Successful','Class removed successfully')

def add_class_command(root, Class):
    result = add_class(Class)

    if result == False:
        messagebox.showerror('error1',"Class already exists!!")
    else:
        messagebox.showinfo('Successful','Class created successfully')

def add_subject_command(root, Class, subject):
    result = add_subject(Class, subject)

    if result == None:
        messagebox.showerror('error',"Class does not exists!!")
    elif result == False:
        messagebox.showerror('error',"subject already exists!!")
    else:
        messagebox.showinfo('Successful','subject added successfully')

def remove_subject_command(root, Class, subject):
    result = remove_subject(Class, subject)

    if result == False:
        messagebox.showerror('error1',"subject does not exists!!")
    else:
        messagebox.showinfo('Successful','subject removed successfully')

