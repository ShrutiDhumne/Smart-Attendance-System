def Email_4 (FacultyEmail, FacultyName) :
    from os import name
    import smtplib
    from email.message import EmailMessage
    import imghdr
     
    try : 
        OTP = ''
        import random
        for i in range(0,6) :
            OTP = OTP + str(random.randint(1,9))

        msg = EmailMessage()
        msg['Subject'] = 'Faculty Authentication'
        msg['To'] = FacultyEmail #"sameer.patil@mitaoe.ac.in"
        msg['From'] = "techaspires.mit@gmail.com"
        msg.set_content('Hello People. \nWelcome to MIT Facial Attendance Management System !')

        msg.add_alternative("""\
            <!DOCTYPE html>
            <body>
                <img src="https://mitaoe.ac.in/BTECH-2021/assets/images/logo-color-1.png" width="400" height="100"/>
                <h1>Welcome to MIT Smart Attendance System
                </h1>
                <h3>Dear {}, your system generated password is  : {} <br>Use this password to login and access your account<br>You may change this password later if you wish.
                </h3>
                <img src="https://analyticsindiamag.com/wp-content/uploads/2020/10/face.jpg" width="300" height="200"/>
            </body>
            </html>
            """.format(FacultyName, OTP), subtype = "html")

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp :
            smtp.login("techaspires.mit@gmail.com", "techaspires.mitaoe.ac.in")
            smtp.send_message(msg)
        
        return int(OTP)
    except : 
        return 404

def Email_5 (Student_Email, Student_Name) :
    from os import name
    import smtplib
    from email.message import EmailMessage
    import imghdr
    
    try : 
        OTP = ''
        import random
        for i in range(0,6) :
            OTP = OTP + str(random.randint(1,9))

        msg = EmailMessage()
        msg['Subject'] = 'Student Registration Confirmation'
        msg['To'] = Student_Email #"sameer.patil@mitaoe.ac.in"
        msg['From'] = "techaspires.mit@gmail.com"
        msg.set_content('Hello People. \nWelcome to MIT Facial Attendance Management System !')

        msg.add_alternative("""\
            <!DOCTYPE html>
            <body>
                <img src="https://mitaoe.ac.in/BTECH-2021/assets/images/logo-color-1.png" width="400" height="100"/>
                <h1>Welcome to MIT Smart Attendance System
                </h1>
                <h3>Dear {} you are succesfully registered for Smart Attendance System
                </h3>
                <img src="https://analyticsindiamag.com/wp-content/uploads/2020/10/face.jpg" width="300" height="200"/>
            </body>
            </html>
            """.format(Student_Name), subtype = "html")

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp :
            smtp.login("techaspires.mit@gmail.com", "techaspires.mitaoe.ac.in")
            smtp.send_message(msg)
        
        return int(OTP)
    except : 
        return 404

def attendance_alert_mail(student_name, student_email_id, subject_name):
    from os import name
    import smtplib
    from email.message import EmailMessage
    import imghdr
    
    OTP = ''
    import random
    for i in range(0,6) :
        OTP = OTP + str(random.randint(1,9))

    msg = EmailMessage()
    msg['Subject'] = '!! Attendance Alert !!'
    msg['To'] = student_email_id #"sameer.patil@mitaoe.ac.in"
    msg['From'] = "techaspires.mit@gmail.com"
    msg.set_content('Attendance Notice !!')

    msg.add_alternative("""\
        <!DOCTYPE html>
        <body>
            <img src="https://mitaoe.ac.in/BTECH-2021/assets/images/logo-color-1.png" width="400" height="100"/>
            <font color='red'>
            <h1>!!! Attendance Alert !!!
            </h1>
            </font>
            <h3>Dear {}, This is to inform you that your attendance of subject {} is less than 75%, don't miss out the furthur lectures!!! 
            </h3>
            <img src="https://analyticsindiamag.com/wp-content/uploads/2020/10/face.jpg" width="300" height="200"/>
        </body>
        </html>
        """.format(student_name, subject_name), subtype = "html")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp :
        smtp.login("techaspires.mit@gmail.com", "techaspires.mitaoe.ac.in")
        smtp.send_message(msg)
    
    return int(OTP)


        