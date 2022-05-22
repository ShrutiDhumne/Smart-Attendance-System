import Attendancepage
import Statisticspage
import facultyoptionsmenu
import tkinter as tk
import tkinter.font as tkFont
class App:
    def __init__(self, root):
        #setting title
        root.title("Smart Attendance System Faculty Page")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        root.configure(bg='black')
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        WelcomeLbl=tk.Label(root)
        ft = tkFont.Font(family='Times',size=38)

        WelcomeLbl["font"] = ft
        WelcomeLbl["fg"] = "#ffffff"
        WelcomeLbl["bg"] = "#000000"
        WelcomeLbl["justify"] = "center"
        WelcomeLbl["text"] = "Welcome"
        WelcomeLbl.place(x=190,y=50,width=200,height=50)

        Selectclasslbl=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        Selectclasslbl["font"] = ft
        Selectclasslbl["bg"] = "#000000"
        Selectclasslbl["fg"] = "#FFFFFF"
        Selectclasslbl["justify"] = "center"
        Selectclasslbl["text"] = "Select class"
        Selectclasslbl.place(x=150,y=160,width=70,height=25)

        Classlist=tk.Listbox(root)
        Classlist["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        Classlist["font"] = ft
        Classlist["fg"] = "#000000"
        Classlist["justify"] = "center"
        Classlist.place(x=250,y=160,width=200,height=25)

        selectsubjectlbl=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        selectsubjectlbl["font"] = ft
        selectsubjectlbl["fg"] = "#ffffff"
        selectsubjectlbl["bg"] = "#000000"
        selectsubjectlbl["justify"] = "center"
        selectsubjectlbl["text"] = "Select Subject"
        selectsubjectlbl.place(x=130,y=200,width=100,height=30)

        Subjectlist=tk.Listbox(root)
        Subjectlist["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        Subjectlist["font"] = ft
        Subjectlist["fg"] = "#000000"
        Subjectlist["justify"] = "center"
        Subjectlist.place(x=250,y=200,width=200,height=25)

        Nexttoclassbtn=tk.Button(root)
        Nexttoclassbtn["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        Nexttoclassbtn["font"] = ft
        Nexttoclassbtn["fg"] = "#000000"
        Nexttoclassbtn["justify"] = "center"
        Nexttoclassbtn["text"] = "Next"
        Nexttoclassbtn.place(x=260,y=270,width=70,height=25)
        Nexttoclassbtn["command"]=self.Nexttoclassbtn_command

        Logoutbtn=tk.Button(root)
        ft = tkFont.Font(family='Times',size=10)
        Logoutbtn["bg"] = "#efefef"
        Logoutbtn["font"] = ft
        Logoutbtn["fg"] = "#000000"
        Logoutbtn["justify"] = "center"
        Logoutbtn["text"] = "Logout"
        Logoutbtn.place(x=510,y=10,width=70,height=25)
        Logoutbtn["command"] = self.Logoutbtn_command

    def Nexttoclassbtn_command(self):
        print("Next to faculty options menu")
        root.destroy()

    def Logoutbtn_command(self):
        print("Logout")
        root.destroy()

if __name__ == "__main__":
     root = tk.Tk()
     app = App(root)
     root.mainloop()

     facultyroot = tk.Tk()
     facultyclass = facultyoptionsmenu.facultyclass(facultyroot)
     facultyroot.mainloop()



