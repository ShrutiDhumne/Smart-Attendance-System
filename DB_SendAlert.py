from DB_GetAttendance import get_attendance
import pandas as pd
from DB_helper import execute_query
from DB_MakeConnection import make_connection
from Email4 import attendance_alert_mail

# This function will give you a list of PRN_NO having attendance < 75%

def get_student_PRN(subject_name):
    column_names, PRN_NO, attendance = get_attendance(subject_name)
    attendance_table = pd.DataFrame(attendance,columns = column_names)
    attendance_table["percentage"] = attendance_table.sum(axis=1)/len(column_names)*100 > 75
    attendance_table["PRN_NO"] = PRN_NO
 
    less_attendance = [j for i,j in zip(attendance_table["percentage"],attendance_table["PRN_NO"]) if i == False]
    return less_attendance

    #function call to send alert mail with less_attendance as argument

def send_alert(class_name, subject_name):

    try:
        print(class_name, subject_name)
        connection = make_connection()
        PRN_with_less_attendance = get_student_PRN(subject_name)
        print(PRN_with_less_attendance)
        for PRN in PRN_with_less_attendance:
            query = f'select student_name, email_id from {class_name} where PRN_NO={PRN}'
            result = execute_query(query, connection).fetchall()
            print(result[0][0])
            print(result[0][1])
            attendance_alert_mail(result[0][0],result[0][1],subject_name)
    except:
        return False
    return True

    

    