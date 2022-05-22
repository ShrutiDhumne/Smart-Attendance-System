import tkinter as tk
from tkinter import PhotoImage, ttk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter.messagebox import askokcancel, showinfo, WARNING
import FaceDetection as FD
from PIL import Image, ImageTk
from DB_StudentRecordsTable import add_student_record
from Email4 import Email_5
from tkinter_custom_button import hover

isFaceCaptured = None
def main(root, username):
    #setting title
    root.title("Add Student Data")
    #setting window size
    width=741
    height=539
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)

    image1 = Image.open("Dataset/BG2.png")
    image1 = image1.resize((741,539),Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image1)
    BGLabel=tk.Label(root,image=test)
    BGLabel.image = test
    BGLabel["borderwidth"] = "3px"
    ft = tkFont.Font(family='Times',size=10)
    BGLabel["font"] = ft
    BGLabel["justify"] = "center"
    BGLabel["text"] = "label"
    BGLabel.place(x=3,y=0,width=735,height=539)

    TitleLabel=tk.Label(root)
    TitleLabel["bg"] = "#00ced1"
    ft = tkFont.Font(family='Times',size=28)
    TitleLabel["font"] = ft
    TitleLabel["fg"] = "#000000"
    TitleLabel["justify"] = "center"
    TitleLabel["text"] = "Add / Edit Student Data"
    TitleLabel.place(x=0,y=50,width=741,height=63)

    Back=tk.Button(root)
    Back["bg"] = "#f0f0f0"
    ft = tkFont.Font(family='Times',size=12)
    Back["font"] = ft
    Back["fg"] = "#000000"
    Back["justify"] = "center"
    Back["text"] = "Back"
    Back.place(x=10,y=10,width=140,height=30)
    Back["command"] = lambda : Back_command(root, username)
    hover(Back,"#f0f0f0")

    Logout=tk.Button(root)
    Logout["bg"] = "#f0f0f0"
    ft = tkFont.Font(family='Times',size=12)
    Logout["font"] = ft
    Logout["fg"] = "#000000"
    Logout["justify"] = "center"
    Logout["text"] = "Logout"
    Logout.place(x=590,y=10,width=140,height=30)
    Logout["command"] = lambda : Logout_command(root)
    hover(Logout,"#f0f0f0")

    NameLabel=tk.Label(root)
    NameLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=16)
    NameLabel["font"] = ft
    NameLabel["fg"] = "#ffffff"
    NameLabel["justify"] = "center"
    NameLabel["text"] = "Name"
    NameLabel.place(x=320,y=150,width=70,height=25)

    PRNLabel=tk.Label(root)
    PRNLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=16)
    PRNLabel["font"] = ft
    PRNLabel["fg"] = "#ffffff"
    PRNLabel["justify"] = "center"
    PRNLabel["text"] = "PRN Number"
    PRNLabel.place(x=300,y=190,width=119,height=30)

    RollLabel=tk.Label(root)
    RollLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=16)
    RollLabel["font"] = ft
    RollLabel["fg"] = "#ffffff"
    RollLabel["justify"] = "center"
    RollLabel["text"] = "Roll Number"
    RollLabel.place(x=300,y=240,width=112,height=30)

    EnterName=tk.Entry(root)
    EnterName["bg"] = "#393d49"
    EnterName["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=14)
    EnterName["font"] = ft
    EnterName["fg"] = "#ffffff"
    EnterName["justify"] = "center"
    EnterName["text"] = ""
    EnterName.place(x=450,y=140,width=250,height=30)

    EnterPRN=tk.Entry(root)
    EnterPRN["bg"] = "#393d49"
    EnterPRN["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=14)
    EnterPRN["font"] = ft
    EnterPRN["fg"] = "#ffffff"
    EnterPRN["justify"] = "center"
    EnterPRN["text"] = ""
    EnterPRN.place(x=450,y=190,width=250,height=30)

    EnterRoll=tk.Entry(root)
    EnterRoll["bg"] = "#393d49"
    EnterRoll["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=14)
    EnterRoll["font"] = ft
    EnterRoll["fg"] = "#ffffff"
    EnterRoll["justify"] = "center"
    EnterRoll["text"] = ""
    EnterRoll.place(x=450,y=240,width=250,height=30)

    SelectClassLabel=tk.Label(root)
    SelectClassLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=16)
    SelectClassLabel["font"] = ft
    SelectClassLabel["fg"] = "#ffffff"
    SelectClassLabel["justify"] = "center"
    SelectClassLabel["text"] = "Select Class"
    SelectClassLabel.place(x=290,y=350,width=134,height=30)

    EnterEmailLabel=tk.Label(root)
    EnterEmailLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=16)
    EnterEmailLabel["font"] = ft
    EnterEmailLabel["fg"] = "#ffffff"
    EnterEmailLabel["justify"] = "center"
    EnterEmailLabel["text"] = "Enter Email"
    EnterEmailLabel.place(x=290,y=400,width=134,height=30)

    EnterEmail=tk.Entry(root)
    EnterEmail["bg"] = "#393d49"
    EnterEmail["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=14)
    EnterEmail["font"] = ft
    EnterEmail["fg"] = "#ffffff"
    EnterEmail["justify"] = "center"
    EnterEmail["text"] = ""
    EnterEmail.place(x=450,y=400,width=250,height=30)

    EnterMobileLabel=tk.Label(root)
    EnterMobileLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=16)
    EnterMobileLabel["font"] = ft
    EnterMobileLabel["fg"] = "#ffffff"
    EnterMobileLabel["justify"] = "center"
    EnterMobileLabel["text"] = "Enter Mobile"
    EnterMobileLabel.place(x=280,y=300,width=150,height=25)

    EnterMobile=tk.Entry(root)
    EnterMobile["bg"] = "#393d49"
    EnterMobile["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=14)
    EnterMobile["font"] = ft
    EnterMobile["fg"] = "#ffffff"
    EnterMobile["justify"] = "center"
    EnterMobile["text"] = ""
    EnterMobile.place(x=450,y=290,width=250,height=30)

    Done=tk.Button(root)
    Done["bg"] = "#90ee90"
    Done["borderwidth"] = "5px"
    ft = tkFont.Font(family='Times',size=16)
    Done["font"] = ft
    Done["fg"] = "#000000"
    Done["justify"] = "center"
    Done["text"] = "Done"
    Done.place(x=350,y=470,width=300,height=42)
    Done["command"] = lambda : Done_command(root, Class.get(), EnterPRN.get(), EnterName.get(), EnterEmail.get(), EnterMobile.get(), EnterRoll.get(), username)
    hover(Done,"#90ee90")

    AddImageLabel=tk.Label(root)
    ft = tkFont.Font(family='Times',size=16)
    AddImageLabel["font"] = ft
    AddImageLabel["fg"] = "#ffffff"
    AddImageLabel["bg"] = "#393d49"
    AddImageLabel["justify"] = "center"
    AddImageLabel["text"] = "Add Image"
    AddImageLabel.place(x=60,y=150,width=132,height=30)

    VDivider=tk.Label(root)
    VDivider["bg"] = "#90ee90"
    ft = tkFont.Font(family='Times',size=10)
    VDivider["font"] = ft
    VDivider["fg"] = "#333333"
    VDivider["justify"] = "center"
    VDivider["text"] = ""
    VDivider.place(x=225,y=113,width=3,height=426)

    image1 = Image.open("Dataset/Login3.png")
    image1 = image1.resize((140,152),Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image1)
    PhotoField=tk.Button(root, image = test)
    PhotoField.image=test
    PhotoField["bg"] = "#000000"
    ft = tkFont.Font(family='Times',size=14)
    PhotoField["font"] = ft
    PhotoField["fg"] = "#ffffff"
    PhotoField["justify"] = "center"
    PhotoField["text"] = "Photo"
    PhotoField.place(x=50,y=190,width=144,height=156)

    Capture=tk.Button(root)
    Capture["bg"] = "#ffd700"
    ft = tkFont.Font(family='Times',size=14)
    Capture["font"] = ft
    Capture["fg"] = "#000000"
    Capture["justify"] = "center"
    Capture["text"] = "Capture"
    Capture.place(x=60,y=370,width=118,height=41)
    Capture["command"] = lambda : Capture_command(root,EnterPRN.get(),PhotoField)
    hover(Capture,"#ffd700")

    Class = ttk.Combobox(root, width = 27, textvariable = tk.StringVar())
    Class.place(x=450,y=340,width=250,height=40)
    Class['values'] = ('Choose Class', 'first_year', 'second_year', 'third_year', 'fourth_year')
    Class.current(0)
    
def Back_command(root, username):
    import AdminHome as adminhome
    adminhome.main(root, username)

def Logout_command(root):
    answer = askokcancel( title='Logout Confirmation', message='Are You Sure to Logout ?', icon=WARNING)
    if answer :
        import Welcome as welcome
        welcome.main(root)

def Done_command(root, table_name, PRN_No, Name, Email_ID, Mobile_No, ROLL_No,username):
    global isFaceCaptured
    Status = 1
    if isFaceCaptured == None:
        messagebox.showerror("error!!", "Please capture the image")
    elif PRN_No != '' and Name !='' and Email_ID != '' and Mobile_No != '' and ROLL_No != '':
        print(table_name, PRN_No, Name, Email_ID, Mobile_No, ROLL_No)
        result  = add_student_record(table_name, PRN_No, Name, Email_ID, str(Mobile_No), ROLL_No)
        if result == False:
            messagebox.showerror('error','Student data already exists!!')
        else:
            messagebox.showinfo("Saved", "Student data added/modified successfully")
            Email_5(Email_ID, Name)
            import AddStudentData as refresh
            refresh.main(root, username)
    else :
        messagebox.showerror("error!!", "Please fill in all datails")


def Capture_command(root, prn, PhotoField):
    global isFaceCaptured
    isFaceCaptured = FD.captureImage(prn)
    if isFaceCaptured == True :
        image1 = Image.open("Train_Dataset/"+str(prn)+".2.jpg")
        image1 = image1.resize((140,152), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(image1)
        PhotoField.configure(image=test)
        PhotoField.image=test 

def PhotoField_command(root):
    print("command")
