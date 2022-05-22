import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter.messagebox import askokcancel, showinfo, WARNING
from PIL import Image, ImageTk
from Training import TrainImages
from ChangePassword import main
from tkinter_custom_button import hover
from DB_ClassSubjectsData import view_class_subject_data
import ClassWiseData

def main (root, username):
    #setting title
    root.title("Admin Home")
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

    AdminHomeLabel=tk.Label(root)
    AdminHomeLabel["bg"] = "#000000"
    ft = tkFont.Font(family='Times',size=28)
    AdminHomeLabel["font"] = ft
    AdminHomeLabel["fg"] = "#ffffff"
    AdminHomeLabel["justify"] = "center"
    AdminHomeLabel["text"] = "Admin Home"
    AdminHomeLabel.place(x=240,y=40,width=289,height=75)

    AddFaculty=tk.Button(root)
    AddFaculty["bg"] = "#ff9900"
    AddFaculty["borderwidth"] = "5px"
    ft = tkFont.Font(family='Times',size=16)
    AddFaculty["font"] = ft
    AddFaculty["fg"] = "#000000"
    AddFaculty["justify"] = "center"
    AddFaculty["text"] = "Add Faculty"
    AddFaculty.place(x=160,y=180,width=200,height=50)
    AddFaculty["command"] = lambda : AddFaculty_command(root, username)
    hover(AddFaculty,"#ff9900")

    ClassSubjectsData=tk.Button(root)
    ClassSubjectsData["bg"] = "#ff9900"
    ClassSubjectsData["borderwidth"] = "5px"
    ft = tkFont.Font(family='Times',size=16)
    ClassSubjectsData["font"] = ft
    ClassSubjectsData["fg"] = "#000000"
    ClassSubjectsData["justify"] = "center"
    ClassSubjectsData["text"] = "Class-wise Data"
    ClassSubjectsData.place(x=420,y=250,width=200,height=50)
    ClassSubjectsData["command"] = lambda : ClassWiseData.main(root, username)
    hover(ClassSubjectsData,"#ff9900")

    Train_data=tk.Button(root)
    Train_data["bg"] = "#ff9900"
    Train_data["borderwidth"] = "5px"
    ft = tkFont.Font(family='Times',size=16)
    Train_data["font"] = ft
    Train_data["fg"] = "#000000"
    Train_data["justify"] = "center"
    Train_data["text"] = "Train data"
    Train_data.place(x=160,y=400,width=200,height=50)
    Train_data["command"] = lambda : Training(root)
    hover(Train_data,"#ff9900")

    AddStudent=tk.Button(root)
    AddStudent["bg"] = "#ff9900"
    AddStudent["borderwidth"] = "5px"
    ft = tkFont.Font(family='Times',size=16)
    AddStudent["font"] = ft
    AddStudent["fg"] = "#000000"
    AddStudent["justify"] = "center"
    AddStudent["text"] = "Add Student"
    AddStudent.place(x=160,y=320,width=200,height=50)
    AddStudent["command"] = lambda : AddStudent_command(root, username)
    hover(AddStudent,"#ff9900")

    ClassSubjects=tk.Button(root)
    ClassSubjects["bg"] = "#ff9900"
    ClassSubjects["borderwidth"] = "5px"
    ft = tkFont.Font(family='Times',size=16)
    ClassSubjects["font"] = ft
    ClassSubjects["fg"] = "#000000"
    ClassSubjects["justify"] = "center"
    ClassSubjects["text"] = "Class and Subjects"
    ClassSubjects.place(x=160,y=250,width=200,height=50)
    ClassSubjects["command"] = lambda : ClassSubjects_command(root, username)
    hover(ClassSubjects,"#ff9900")

    FacultywiseData=tk.Button(root)
    FacultywiseData["bg"] = "#ff9900"
    FacultywiseData["borderwidth"] = "5px"
    ft = tkFont.Font(family='Times',size=16)
    FacultywiseData["font"] = ft
    FacultywiseData["fg"] = "#000000"
    FacultywiseData["justify"] = "center"
    FacultywiseData["text"] = "Faculty-Wise Data"
    FacultywiseData.place(x=420,y=180,width=200,height=50)
    FacultywiseData["command"] = lambda : FacultywiseData_command(root, username)
    hover(FacultywiseData,"#ff9900")

    StudentwiseData=tk.Button(root)
    StudentwiseData["bg"] = "#ff9900"
    StudentwiseData["borderwidth"] = "5px"
    ft = tkFont.Font(family='Times',size=16)
    StudentwiseData["font"] = ft
    StudentwiseData["fg"] = "#000000"
    StudentwiseData["justify"] = "center"
    StudentwiseData["text"] = "Student-wise Data"
    StudentwiseData.place(x=420,y=320,width=200,height=50)
    StudentwiseData["command"] = lambda : StudentwiseData_command(root, username)
    hover(StudentwiseData,"#ff9900")

    RemoveRecords=tk.Button(root)
    RemoveRecords["bg"] = "#ff9900"
    RemoveRecords["borderwidth"] = "5px"
    ft = tkFont.Font(family='Times',size=16)
    RemoveRecords["font"] = ft
    RemoveRecords["fg"] = "#000000"
    RemoveRecords["justify"] = "center"
    RemoveRecords["text"] = "Remove Records"
    RemoveRecords.place(x=420,y=400,width=200,height=50)
    RemoveRecords["command"] = lambda : RemoveRecords_command(root, username)
    hover(RemoveRecords,"#ff9900")

    Divider=tk.Label(root)
    Divider["bg"] = "#90f090"
    ft = tkFont.Font(family='Times',size=10)
    Divider["font"] = ft
    Divider["fg"] = "#333333"
    Divider["justify"] = "center"
    Divider["text"] = ""
    Divider.place(x=3,y=140,width=735,height=2)

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

    ChangePassword=tk.Button(root)
    ChangePassword["bg"] = "#00ced1"
    ChangePassword["borderwidth"] = "5px"
    ft = tkFont.Font(family='Times',size=14)
    ChangePassword["font"] = ft
    ChangePassword["fg"] = "#000000"
    ChangePassword["justify"] = "center"
    ChangePassword["text"] = "Change Password"
    ChangePassword.place(x=580,y=60,width=153,height=44)
    ChangePassword["command"] = lambda : change_password(root, 'A', username, 'admin')
    hover(ChangePassword,"#00ced1")

def AddFaculty_command(root, username):
    import AddFaculty as addfaculty
    addfaculty.main(root, username)

def AddStudent_command(root, username):
    import AddStudentData as addstudent
    addstudent.main(root, username)


def ClassSubjects_command(root, username):
    import AddRemoveClassSubject as classsubject
    classsubject.main(root, username)


def FacultywiseData_command(root, username):
    import FacultyWiseRecords as facultydata
    facultydata.main(root, username)


def StudentwiseData_command(root, username):
    import StudentWiseRecords as studentdata
    studentdata.main(root, username)

def RemoveRecords_command(root, username) :
    import RemoveRecords as RR
    RR.main(root, username)

def Logout_command(root):
    answer = askokcancel( title='Logout Confirmation', message='Are You Sure to Logout ?', icon=WARNING)
    if answer :
        import Welcome as welcome
        welcome.main(root)

def Training(root):
    if TrainImages() == False:
        messagebox.showerror('error','Training Failed please contact support team!')
    else:
        messagebox.showinfo('successfull','Training Successful')

def change_password(root, token, username, table_name):
    import ChangePassword as cp
    print(username)
    cp.main(root,token,username,table_name)


