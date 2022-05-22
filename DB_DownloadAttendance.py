import pandas as pd
from DB_GetAttendance import get_attendance, get_daily_attendance

def download_attendance(table_name):
    try:
        column_names, PRN_NO, attendance = get_attendance(table_name)
        attendance_table = pd.DataFrame(attendance, index=PRN_NO, columns = column_names).fillna(0)
        attendance_table.index.name = "PRN_Number"
        attendance_table["total_attendance"] = attendance_table.sum(axis=1)
        attendance_table.to_csv("Downloads/"+table_name+"_attendance.csv")
        return True
    except:
        return False       

def download_daily_attendance(table_name, date):
    PRN_NO, attendance = get_daily_attendance(table_name, date)
    attendance_table = pd.DataFrame(attendance, index=PRN_NO, columns = [str(date)]).fillna(0)
    attendance_table.index.name = "PRN_Number"

    attendance_table.to_csv("Downloads/"+table_name+"_"+date+"_attendance.csv")
    return True



