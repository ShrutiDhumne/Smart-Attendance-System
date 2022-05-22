import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter.messagebox import askokcancel, showinfo, WARNING 
from DB_RemoveRecords import remove_records
from tkinter_custom_button import hover

def main(root, username):
    #setting title
    root.title("Delete Records Permanently")
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
    TitleLabel["text"] = "Remove Student or Faculty"
    TitleLabel.place(x=0,y=50,width=741,height=63)

    SelectOrRemove=tk.Button(root)
    SelectOrRemove["bg"] = "#90f090"
    SelectOrRemove["borderwidth"] = "3px"
    ft = tkFont.Font(family='Times',size=16)
    SelectOrRemove["font"] = ft
    SelectOrRemove["fg"] = "#000000"
    SelectOrRemove["justify"] = "center"
    SelectOrRemove["text"] = "Remove Faculty"
    SelectOrRemove.place(x=460,y=380,width=215,height=45)
    SelectOrRemove["command"] = lambda : SelectToRemove_command(root, FacultyEntry.get(), 'faculty_records')
    hover(SelectOrRemove,"#90f090")

    Back=tk.Button(root)
    Back["bg"] = "#f0f0f0"
    ft = tkFont.Font(family='Times',size=10)
    Back["font"] = ft
    Back["fg"] = "#000000"
    Back["justify"] = "center"
    Back["text"] = "Back"
    Back.place(x=10,y=10,width=140,height=30)
    Back["command"] = lambda : Back_command(root, username)
    hover(Back,"#f0f0f0")

    Logout=tk.Button(root)
    Logout["bg"] = "#f0f0f0"
    ft = tkFont.Font(family='Times',size=10)
    Logout["font"] = ft
    Logout["fg"] = "#000000"
    Logout["justify"] = "center"
    Logout["text"] = "Logout"
    Logout.place(x=590,y=10,width=140,height=30)
    Logout["command"] = lambda : Logout_command(root)
    hover(Logout,"#f0f0f0")

    SelectToRemove=tk.Button(root)
    SelectToRemove["bg"] = "#90f090"
    SelectToRemove["borderwidth"] = "3px"
    ft = tkFont.Font(family='Times',size=16)
    SelectToRemove["font"] = ft
    SelectToRemove["fg"] = "#000000"
    SelectToRemove["justify"] = "center"
    SelectToRemove["text"] = "Remove Student"
    SelectToRemove.place(x=80,y=380,width=215,height=45)
    SelectToRemove["command"] = lambda : SelectToRemove_command(root, StudentEntry.get(), Class.get())
    hover(SelectToRemove,"#90f090")

    Divider=tk.Label(root)
    Divider["bg"] = "#90ee90"
    ft = tkFont.Font(family='Times',size=10)
    Divider["font"] = ft
    Divider["fg"] = "#333333"
    Divider["justify"] = "center"
    Divider["text"] = ""
    Divider.place(x=370,y=113,width=3,height=500)

    StudentEntry=tk.Entry(root)
    StudentEntry["bg"] = "#ffffff"
    StudentEntry["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=14)
    StudentEntry["font"] = ft
    StudentEntry["fg"] = "#000000"
    StudentEntry["justify"] = "center"
    StudentEntry["text"] = ""
    StudentEntry.place(x=80,y=300,width=215,height=45)

    EnterPRNLabel=tk.Label(root)
    EnterPRNLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=16)
    EnterPRNLabel["font"] = ft
    EnterPRNLabel["fg"] = "#ffffff"
    EnterPRNLabel["justify"] = "center"
    EnterPRNLabel["text"] = "Enter Student PRN"
    EnterPRNLabel.place(x=80,y=265,width=215,height=30)

    Class = ttk.Combobox(root, width = 27, textvariable = tk.StringVar())
    Class.place(x=80,y=210,width=220,height=45)
    Class['values'] = ('Enter Class', 'first_year','second_year','third_year','fourth_year')
    Class.current(0)

    SelectClassLabel=tk.Label(root)
    SelectClassLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=16)
    SelectClassLabel["font"] = ft
    SelectClassLabel.place(x=80,y=170,width=215,height=30)
    SelectClassLabel["fg"] = "#ffffff"
    SelectClassLabel["justify"] = "center"
    SelectClassLabel["text"] = "Select Class"

    FacultyEntry=tk.Entry(root)
    FacultyEntry["bg"] = "#ffffff"
    FacultyEntry["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=14)
    FacultyEntry["font"] = ft
    FacultyEntry["fg"] = "#000000"
    FacultyEntry["justify"] = "center"
    FacultyEntry["text"] = ""
    FacultyEntry.place(x=460,y=210,width=215,height=45)

    EnterEmailLabel=tk.Label(root)
    EnterEmailLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=16)
    EnterEmailLabel["font"] = ft
    EnterEmailLabel["fg"] = "#ffffff"
    EnterEmailLabel["justify"] = "center"
    EnterEmailLabel["text"] = "Enter Faculty Email"
    EnterEmailLabel.place(x=460,y=170,width=215,height=30)

def SelectOrRemove_command(root):
    print("command")


def Back_command(root, username):
    import AdminHome as ah
    ah.main(root, username)


def Logout_command(root):
    answer = askokcancel( title='Logout Confirmation', message='Are you sure to logout ?', icon=WARNING)
    if answer :
        import Welcome as welcome
        welcome.main(root)

def SelectToRemove_command(root, ID_to_remove, table_name):
    print(ID_to_remove)
    print(table_name)

    if table_name == 'Enter Class':
        messagebox.showerror('error!!','Please select class name')
    elif ID_to_remove == '' and table_name != 'faculty_records':
        messagebox.showerror('error!!','Please Enter PRN number')
    elif ID_to_remove == '':
        messagebox.showerror('error!!','please Enter Faculty Email ID')
    elif remove_records(ID_to_remove, table_name) == False:
        messagebox.showerror('error!!','Record does not exist!!')
    else:
        messagebox.showinfo('successful','Record deleted successfully')