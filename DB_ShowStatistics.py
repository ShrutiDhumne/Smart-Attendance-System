from DB_GetAttendance import get_attendance
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def show_statistics(table_name):
    column_names, PRN_NO, attendance = get_attendance(table_name)
    attendance_table = pd.DataFrame(attendance, index=PRN_NO, columns = column_names)
    attendance_table.index.name = "PRN_Number"
    attendance_table["percentage"] = attendance_table.sum(axis=1)/len(column_names)*100
    print(attendance_table['percentage'])
    
    sns.barplot(x=attendance_table.index,y=attendance_table['percentage'])
    plt.show()

