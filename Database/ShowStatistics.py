from GetAttendance import get_attendance
import pandas as pd
import matplotlib.pyplot as plt

def show_statistics(table_name="scet_first_year_ml"):
    column_names, PRN_NO, attendance = get_attendance(table_name)
    attendance_table = pd.DataFrame(attendance, index=PRN_NO, columns = column_names)
    attendance_table["percentage"] = (attendance_table.sum(axis=1)/len(column_names))*100

    plt.bar(x = attendance_table.index, height=attendance_table['percentage'],tick_label=PRN_NO)
    plt.title("attendance statistics of "+table_name)
    plt.xlabel("PRN_NO")
    plt.ylabel("Attendance Percentage")
    plt.show()

show_statistics()
