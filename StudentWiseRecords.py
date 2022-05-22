import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter.messagebox import askokcancel, showerror, showinfo, WARNING 
from DB_DownloadStudentRecords import download_student_records
from DB_DisplayRecords import display_records
from tkinter_custom_button import hover

ROOT = ''
Class= ''
def main(root, username):
    global ROOT
    global Class
    ROOT = root
    root.title("Student Details")
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
    TitleLabel["fg"] = "#000000"
    TitleLabel["justify"] = "center"
    TitleLabel["text"] = "Student Records (Class-wise)"
    TitleLabel.place(x=0,y=50,width=741,height=63)

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
    DownloadCSV["text"] = "Download Students Records"
    DownloadCSV.place(x=260,y=460,width=212,height=34)
    DownloadCSV["command"] = lambda : DownloadCSV_command(root, Class)
    hover(DownloadCSV,"#ff9900")

    SelectClassLabel=tk.Label(root)
    SelectClassLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times New Roman',size=16)
    SelectClassLabel["font"] = ft
    SelectClassLabel["fg"] = "#ffffff"
    SelectClassLabel["justify"] = "center"
    SelectClassLabel["text"] = "Select Class"
    SelectClassLabel.place(x=100,y=130,width=134,height=30)
    hover(DownloadCSV,"#f0f0f0")

    Class = ttk.Combobox(root, width = 27, textvariable = tk.StringVar())
    Class.place(x=250,y=125,width=250,height=40)
    Class['values'] = ('Choose Class', 'first_year', 'second_year', 'third_year', 'fourth_year')
    Class.bind("<<ComboboxSelected>>", get_selected_year)
    Class.current(0)

    

def Back_command(root, username):
    import AdminHome as adminhome
    adminhome.main(root, username) 


def Logout_command(root):
    answer = askokcancel( title='Logout Confirmation', message='Are you sure to logout ?', icon=WARNING)
    if answer :
        import Welcome as welcome
        welcome.main(root)

def DownloadCSV_command(root, Class):
    table_name = Class.get()
    print(table_name)
    if download_student_records(table_name) == True:
        messagebox.showinfo("Completed","The File has been downloaded in 'Downloads' Folder")
    else:
        messagebox.showerror("Failed","Oops! something went wrong. Unable to Download.")
def get_selected_year(event):
    selected_year = Class.get()
    #treev = ttk.Treeview(root, selectmode ='extended')
    treev = ttk.Treeview(ROOT, selectmode = 'browse', columns=(1, 2, 3, 4, 5), show='headings', height=20)
    treev.place(x=50,y=180,width= 650,height=270)
    
    # Constructing vertical scrollbar
    # with treeview
    verscrlbar = ttk.Scrollbar(ROOT, orient ="vertical", command = treev.yview)
    
    # Calling pack method w.r.to verical 
    # scrollbar
    verscrlbar.pack(side ='right', fill ='x')
    
    # Configuring treeview
    treev.configure(xscrollcommand = verscrlbar.set)
    
    # Assigning the width and anchor to the respective columns
    treev.column("1", width = 90, anchor ='c')
    treev.column("2", width = 90, anchor ='c')
    treev.column("3", width = 90, anchor ='c')
    treev.column("4", width = 90, anchor ='c')
    treev.column("5", width = 90, anchor ='c')
    
    # Assigning the heading names to the respective columns
    treev.heading("1", text ="PRN")
    treev.heading("2", text ="Name")
    treev.heading("3", text ="Email_ID")
    treev.heading("4", text ="Mobile_NO")
    treev.heading("5", text ="Roll_NO")
    student_records = display_records(selected_year)

    if student_records == False:
        messagebox.showerror('error!','Class does not exist!!')
    else:
        for record in student_records:
            prn, name, email_id, Mobile_NO, Roll_NO = record[0], record[1], record[2], record[3], record[4]
            treev.insert("", 'end', text ="L1", values =(prn, name, email_id, Mobile_NO, Roll_NO))
