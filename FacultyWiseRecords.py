import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter.messagebox import askokcancel, showinfo, WARNING 
from DB_DownloadFacultyRecords import download_faculty_records
from DB_DisplayRecords import display_records
from tkinter_custom_button import hover

def main(root, username):
    
    root.title("Faculty Details")
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

    FacultyRecordsLabel=tk.Label(root)
    FacultyRecordsLabel["bg"] = "#00ced1"
    ft = tkFont.Font(family='Times',size=28)
    FacultyRecordsLabel["font"] = ft
    FacultyRecordsLabel["fg"] = "#000000"
    FacultyRecordsLabel["justify"] = "center"
    FacultyRecordsLabel["text"] = "Faculty -wise Records"
    FacultyRecordsLabel.place(x=0,y=50,width=741,height=63)

    Back=tk.Button(root)
    Back["bg"] = "#f0f0f0"
    ft = tkFont.Font(family='Times',size=14)
    Back["font"] = ft
    Back["fg"] = "#000000"
    Back["justify"] = "center"
    Back["text"] = "Back"
    Back.place(x=10,y=10,width=140,height=30)
    Back["command"] = lambda : Back_command(root, username)
    hover(Back,"#f0f0f0")

    Logout=tk.Button(root)
    Logout["bg"] = "#f0f0f0"
    ft = tkFont.Font(family='Times',size=14)
    Logout["font"] = ft
    Logout["fg"] = "#000000"
    Logout["justify"] = "center"
    Logout["text"] = "Logout"
    Logout.place(x=590,y=10,width=140,height=30)
    Logout["command"] = lambda : Logout_command(root)
    hover(Logout,"#f0f0f0")

    DownloadCSV=tk.Button(root)
    DownloadCSV["bg"] = "#ff9900"
    DownloadCSV["borderwidth"] = "4px"
    ft = tkFont.Font(family='Times',size=12)
    DownloadCSV["font"] = ft
    DownloadCSV["fg"] = "#000000"
    DownloadCSV["justify"] = "center"
    DownloadCSV["text"] = "Download Faculty Records"
    DownloadCSV.place(x=260,y=450,width=212,height=34)
    DownloadCSV["command"] = lambda :  DownloadCSV_command(root)
    hover(DownloadCSV,"#ff9900")

    #treev = ttk.Treeview(root, selectmode ='extended')
    faculty_records = display_records('faculty_records')
    treev = ttk.Treeview(root, selectmode = 'browse', columns=(1, 2, 3), show='headings', height=20)
    treev.place(x=50,y=150,width= 650,height=280)
    
    # Constructing vertical scrollbar
    # with treeview
    verscrlbar = ttk.Scrollbar(root, orient ="vertical", command = treev.yview)
    
    # Calling pack method w.r.to verical 
    # scrollbar
    verscrlbar.pack(side ='right', fill ='x')
    
    # Configuring treeview
    treev.configure(xscrollcommand = verscrlbar.set)
    
    # Assigning the width and anchor to the respective columns
    treev.column("1", width = 90, anchor ='c')
    treev.column("2", width = 90, anchor ='c')
    treev.column("3", width = 90, anchor ='c')
    
    # Assigning the heading names to the respective columns
    treev.heading("1", text ="Name")
    treev.heading("2", text ="Email")
    treev.heading("3", text ="Password")
    
    # Inserting the items and their features to the columns built
    for record in faculty_records:
        name, email_id, password = record[0], record[1], record[2]
        treev.insert("", 'end', text ="L1", values =(name, email_id, password))

def Back_command(root, username):
    import AdminHome as adminhome
    adminhome.main(root, username) 

def Logout_command(root):
    answer = askokcancel( title='Logout Confirmation', message='Are you sure to logout ?', icon=WARNING)
    if answer :
        import Welcome as welcome
        welcome.main(root)

def DownloadCSV_command(root):
    if download_faculty_records() == True:
        messagebox.showinfo("Completed","The File has been downloaded in 'Downloads' Folder")
    else:
        messagebox.showerror("Failed","Unable to download.")