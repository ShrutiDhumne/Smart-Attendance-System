import pandas as pd
from GetAttendance import get_attendance

def download_attendance(table_name="scet_first_year_ml"):
    column_names, PRN_NO, attendance = get_attendance(table_name)
    attendance_table = pd.DataFrame(attendance, index=PRN_NO, columns = column_names).fillna(0)
    attendance_table["total_attendance"] = attendance_table.sum(axis=1)

    attendance_table.to_csv(table_name+" attendance.csv")



