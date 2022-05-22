import tkinter as tk
import tkinter.font as tkFont
from tkinter import PhotoImage, ttk
from tkinter import messagebox
from tkinter.messagebox import askokcancel, showinfo, WARNING
from PIL import Image, ImageTk
from DB_GetSubjects import get_subjects
from tkinter_custom_button import hover

SelectClass, SelectSubject='',''
table_name=''
def main(root, username):

    root.title("Faculty Home")
    global SelectClass
    global SelectSubject
    
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

    TitleLabel=tk.Label(root)
    TitleLabel["bg"] = "#000000"
    ft = tkFont.Font(family='Times New Roman',size=45)
    TitleLabel["font"] = ft
    TitleLabel["fg"] = "#ffffff"
    TitleLabel["justify"] = "center"
    TitleLabel["text"] = "Welcome"
    TitleLabel.place(x=213,y=50,width=289,height=75)

    Divider=tk.Label(root)
    Divider["bg"] = "#90ee90"
    ft = tkFont.Font(family='Times',size=10)
    Divider["font"] = ft
    Divider["fg"] = "#333333"
    Divider["justify"] = "center"
    Divider["text"] = ""
    Divider.place(x=3,y=140,width=735,height=3)

    SelectClass = ttk.Combobox(root, width = 27, textvariable = tk.StringVar())
    SelectClass.place(x=360,y=180,width=265,height=45)
    SelectClass['values'] = ('Choose Class', 'first_year', 'second_year', 'third_year', 'fourth_year')
    SelectClass.current(0)
    SelectClass.bind('<<ComboboxSelected>>',get_valid_subjects)

    SelectSubject = ttk.Combobox(root, width = 27, textvariable = tk.StringVar())
    SelectSubject.place(x=360,y=270,width=265,height=45)
    SelectSubject.bind("<<ComboboxSelected>>", get_table_name)


    Next=tk.Button(root)
    Next["bg"] = "#3af0ed"
    Next["borderwidth"] = "2px"
    ft = tkFont.Font(family='Times',size=14)
    Next["font"] = ft
    Next["fg"] = "#000000"
    Next["justify"] = "center"
    Next["text"] = "NEXT"
    Next.place(x=220,y=380,width=320,height=50)
    Next["command"] = lambda : Next_command(root,table_name, username)
    hover(Next,"#3af0ed")

    SelectClassLabel=tk.Label(root)
    SelectClassLabel["bg"] = "#000000"
    ft = tkFont.Font(family='Times',size=18)
    SelectClassLabel["font"] = ft
    SelectClassLabel["fg"] = "#ffffff"
    SelectClassLabel["justify"] = "center"
    SelectClassLabel["text"] = "Select Class"
    SelectClassLabel.place(x=170,y=180,width=134,height=45)

    SelectSubjectLabel=tk.Label(root)
    ft = tkFont.Font(family='Times',size=18)
    SelectSubjectLabel["bg"] = "#000000"
    SelectSubjectLabel["font"] = ft
    SelectSubjectLabel["fg"] = "#ffffff"
    SelectSubjectLabel["justify"] = "center"
    SelectSubjectLabel["text"] = "Select Subject"
    SelectSubjectLabel.place(x=160,y=270,width=160,height=45)

    ChangePassword=tk.Button(root)
    ChangePassword["bg"] = "#00ced1"
    ChangePassword["borderwidth"] = "5px"
    ft = tkFont.Font(family='Times',size=14)
    ChangePassword["font"] = ft
    ChangePassword["fg"] = "#000000"
    ChangePassword["justify"] = "center"
    ChangePassword["text"] = "Change Password"
    ChangePassword.place(x=580,y=60,width=153,height=44)
    ChangePassword["command"] = lambda : change_password(root, 'F', username, 'faculty_records')
    hover(ChangePassword,"#00ced1")

    Logout=tk.Button(root)
    Logout["bg"] = "#00ced1"
    Logout["borderwidth"] = "5px"
    ft = tkFont.Font(family='Times',size=14)
    Logout["font"] = ft
    Logout["fg"] = "#000000"
    Logout["justify"] = "center"
    Logout["text"] = "Logout"
    Logout.place(x=580,y=10,width=153,height=44)
    Logout["command"] = lambda : Logout_command(root)
    hover(Logout,"#00ced1")

def Next_command(root, table_name, username):
    if SelectClass.get() == '' or SelectClass.get() == 'Choose Class':
        messagebox.showerror('error','please select class name')
    elif SelectSubject.get() == '' or SelectSubject.get() == "Choose Subject":
        messagebox.showerror('error','please select subject name')
    else:
        import FacultyMenu as FM
        FM.main(root,table_name,SelectClass.get(), SelectSubject.get().split('_')[-1], username)

def get_table_name(event):
    global SelectSubject
    global table_name
    subject = SelectSubject.get()
    table_name = subject

def get_valid_subjects(event):
    global SelectClass
    global SelectSubject
    Class = SelectClass.get()
    valid_subjects = ['Choose Subject']
    valid_subjects.extend(get_subjects(str(Class)))
    print(tuple(valid_subjects))
    print(type(SelectSubject))
    SelectSubject['values'] = tuple(valid_subjects)
    SelectSubject.current(0)

def Logout_command(root):
    answer = askokcancel( title='Logout Confirmation', message='Are You Sure to Logout ?', icon=WARNING)
    if answer :
        import Welcome as welcome
        welcome.main(root)

        
def change_password(root, token, username, table_name):
    import ChangePassword as cp
    print(username)
    cp.main(root,token,username,table_name)

