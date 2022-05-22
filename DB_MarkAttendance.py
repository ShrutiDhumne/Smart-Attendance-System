from DB_MakeConnection import make_connection
from DB_helper import execute_query

def Instantiate_attendance_table(table_name):
    '''create attendance table if it doest not exist 

    Args:
        Class (str): class name (SCET, DSE)
        year (str): year (first,second)
        subject (str): subject name 
    '''
    try:
        connection = make_connection()
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name}(PRN_NO int PRIMARY KEY)"
        print(execute_query(create_table_query,connection))
    except:
        return


def mark_attendance(table_name, date, attendance_list):
    ''' mark attendance of given class and date
    
    Args:
        table_name (str): attendance table name  
        date (str): date of attendance
        attendance_list (list): list of attendance
    '''
    connection = make_connection() 
    Instantiate_attendance_table(table_name)
    add_column_query = f"ALTER TABLE {table_name} ADD COLUMN {date} int DEFAULT 0"
    execute_query(add_column_query,connection)

    print(attendance_list)
    for PRN_NO in attendance_list:
        print(PRN_NO)
        fill_attendance_query = f"UPDATE {table_name} SET {date} = 1 WHERE PRN_NO = {PRN_NO}" 
        execute_query(fill_attendance_query,connection)

    return True


