import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter.messagebox import askokcancel, showinfo, WARNING
from DB_ShowStatistics import show_statistics
from DB_DownloadAttendance import download_attendance
from DB_SendAlert import send_alert
from datetime import date
from tkinter_custom_button import hover

class_name = ""
subject_name =""
def main(root, Table_name, class_name, subject_name, username):
    
    print(Table_name,class_name,subject_name)
    root.title("Faculty Panel")
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

    Title=tk.Label(root)
    Title["bg"] = "#00ced1"
    ft = tkFont.Font(family='Times',size=32)
    Title["font"] = ft
    Title["fg"] = "#333333"
    Title["justify"] = "center"
    Title["text"] = f"{(class_name.capitalize())} : {subject_name}"
    Title.place(x=3,y=75,width=735,height=75)

    TakeAttendance=tk.Button(root)
    TakeAttendance["activebackground"] = "#00ced1"
    TakeAttendance["bg"] = "#ff9900"
    TakeAttendance["borderwidth"] = "5px"
    ft = tkFont.Font(family='Times',size=17)
    TakeAttendance["font"] = ft
    TakeAttendance["fg"] = "#000000"
    TakeAttendance["justify"] = "center"
    TakeAttendance["text"] = "Take Attendance"
    TakeAttendance.place(x=130,y=250,width=220,height=80)
    TakeAttendance["command"] = lambda : TakeAttendance_command(root, Table_name, class_name, subject_name, username)
    hover(TakeAttendance,"#ff9900")

    Statistics=tk.Button(root)
    Statistics["bg"] = "#ff9900"
    Statistics["activebackground"] = "#00ced1"
    Statistics["borderwidth"] = "5px"
    ft = tkFont.Font(family='Times',size=17)
    Statistics["font"] = ft
    Statistics["fg"] = "#000000"
    Statistics["justify"] = "center"
    Statistics["text"] = "Monthly Statistics"
    Statistics.place(x=430,y=250,width=220,height=80)
    Statistics["command"] = lambda : show_statistics(Table_name)
    hover(Statistics,"#ff9900")

    Divider=tk.Label(root)
    Divider["bg"] = "#90ee90"
    ft = tkFont.Font(family='Times',size=10)
    Divider["font"] = ft
    Divider["fg"] = "#333333"
    Divider["justify"] = "center"
    Divider["text"] = ""
    Divider.place(x=0,y=170,width=741,height=3)

    Download=tk.Button(root)
    Download["bg"] = "#ff9900"
    Download["borderwidth"] = "5px"
    ft = tkFont.Font(family='Times',size=17)
    Download["font"] = ft
    Download["cursor"] = "hand2"
    Download["fg"] = "#000000"
    Download["justify"] = "center"
    Download["text"] = "Download"
    Download.place(x=130,y=380,width=220,height=80)
    Download["command"] = lambda : save_attendance(Table_name)
    hover(Download,"#ff9900")

    Alert=tk.Button(root)
    Alert["bg"] = "#ff9900"
    Alert["borderwidth"] = "5px"
    ft = tkFont.Font(family='Times',size=17)
    Alert["font"] = ft
    Alert["fg"] = "#000000"
    Alert["justify"] = "center"
    Alert["text"] = "Send Alert"
    Alert.place(x=430,y=380,width=220,height=80)
    Alert["command"] = lambda : send_alert_mail(class_name, Table_name)
    hover(Alert,"#ff9900")
    
    Back=tk.Button(root)
    Back["bg"] = "#ffffff"
    Back["borderwidth"] = "2px"
    ft = tkFont.Font(family='Times',size=13)
    Back["font"] = ft
    Back["fg"] = "#000000"
    Back["justify"] = "center"
    Back["text"] = "Back"
    Back.place(x=10,y=10,width=150,height=45)
    Back["command"] = lambda : Back_command(root, username)
    hover(Back,"#f0f0f0")

    Logout=tk.Button(root)
    Logout["bg"] = "#ffffff"
    Logout["borderwidth"] = "2px"
    ft = tkFont.Font(family='Times',size=12)
    Logout["font"] = ft
    Logout["fg"] = "#000000"
    Logout["justify"] = "center"
    Logout["text"] = "Logout"
    Logout.place(x=580,y=10,width=150,height=45)
    Logout["command"] = lambda : Logout_command(root)
    hover(Logout,"#f0f0f0")

def TakeAttendance_command(root, Table_name, class_name, subject_name, username):
    import AttendancePage as AP
    AP.main(root,Table_name, class_name, subject_name, username)

def Statistics_command(root):
    import Statisticspage as SP
    SP.main(root, class_name, subject_name)

def Back_command(root, username):
    import FacultyHome as FH
    FH.main(root, username)


def Logout_command(root):
    answer = askokcancel( title='Logout Confirmation', message='Are You Sure to Logout ?', icon=WARNING)
    if answer :
        import Welcome as welcome
        welcome.main(root)

def save_attendance(table_name):
    result = download_attendance(table_name)
    if result == True:
        messagebox.showinfo("success", "Attendace downloaded successfully!!")
    else:
        messagebox.showerror("error","please contact support team!")

def send_alert_mail(class_name, subject_name):

    if send_alert(class_name,subject_name) == False:
        messagebox.showerror("error","error occurred please contact support team")
    else:
        messagebox.showinfo("successfull",'Mail sent successfully')
