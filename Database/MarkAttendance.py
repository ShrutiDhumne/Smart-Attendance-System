from MakeConnection import make_connection
from helper import execute_query

def Instantiate_attendance_table(table_name):
    '''create attendance table if it doest not exist 

    Args:
        Class (str): class name (SCET, DSE)
        year (str): year (first,second)
        subject (str): subject name 
    '''
    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name}(PRN_NO int PRIMARY KEY)"
    #add_students_query = f"INSERT INTO {table_name} (PRN_NO) VALUES (220200160),(220200161),(220200162),(220200163)"
    execute_query(create_table_query,connection)
    #execute_query(add_students_query,connection)

def mark_attendance(table_name, date, attendance_list):
    ''' mark attendance of given class and date
    
    Args:
        table_name (str): attendance table name  
        date (str): date of attendance
        attendance_list (list): list of attendance
    '''
    Instantiate_attendance_table(table_name)
    add_column_query = f"ALTER TABLE {table_name} ADD COLUMN {date} int"
    execute_query(add_column_query,connection)

    for PRN_NO in attendance_list:
        fill_attendance_query = f"UPDATE {table_name} SET {date} = 1 WHERE PRN_NO = {PRN_NO}" 
        execute_query(fill_attendance_query,connection)

connection = make_connection() 