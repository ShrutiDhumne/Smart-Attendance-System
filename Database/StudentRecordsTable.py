from MakeConnection import make_connection
from helper import execute_query

def create_student_table():
    '''create student records table if it doest not exist 
    '''

    create_table_query = f"CREATE TABLE IF NOT EXISTS {TABLE_NAME}(PRN_NO int PRIMARY KEY, STUDENT_NAME varchar(40), EMAIL_ID varchar(40))"
    execute_query(create_table_query,connection)

def add_student_record(PRN_NO, Student_Name, Email_ID):
    '''add student record into student record table

    Args:
        PRN_NO (int): PRN_NO of student
        Student_Name (str): Student Name 
    '''

    add_student_record_query = f"INSERT INTO {TABLE_NAME}(PRN_NO, STUDENT_NAME, EMAIL_ID) VALUES ({PRN_NO}, '{Student_Name}', '{Email_ID}')" 
    execute_query(add_student_record_query,connection)

connection = make_connection()
TABLE_NAME = 'STUDENT_RECORDS'
create_student_table()
add_student_record(220200160,"Abhijeet Gandhi","abhijeet.gandhi@mitaoe.ac.in")
add_student_record(220200161,"Sameer Patil","sameer.patil@mitaoe.ac.in")
add_student_record(220200162,"Atharva Joshi","atharva.joshi@mitaoe.ac.in")
add_student_record(220200163,"Shruti Dhumne","shruti.dhumne@mitaoe.ac.in")