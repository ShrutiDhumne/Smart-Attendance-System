from DB_MakeConnection import make_connection
from DB_helper import execute_query

def create_student_table(table_name, connection):
    '''create student records table if it doest not exist 
    '''

    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name}(PRN_NO int PRIMARY KEY, STUDENT_NAME varchar(40), EMAIL_ID varchar(40), Mobile_No BIGINT, ROLL_No INT)"
    execute_query(create_table_query,connection)

def add_student_record(table_name, PRN_NO, Student_Name, Email_ID, Mobile_No, ROLL_No):
    '''add student record into student record table

    Args:
        PRN_NO (int): PRN_NO of student
        Student_Name (str): Student Name 
    '''
    connection = make_connection()
    create_student_table(table_name, connection)
    print(table_name)

    add_student_record_query = f"INSERT INTO {table_name} VALUES ({PRN_NO}, '{Student_Name}', '{Email_ID}', '{Mobile_No}', {ROLL_No})" 
    execute_query(add_student_record_query,connection)

    subject_tables_query = "show tables"
    subject_tables = execute_query(subject_tables_query,connection).fetchall() 


    for table in subject_tables:
        if table[0].decode().startswith(table_name+"_"):
            print(table[0].decode())
            print(PRN_NO)
            add_student_record_query  = f"INSERT INTO {table[0].decode()} (PRN_NO) values ({PRN_NO})"
            execute_query(add_student_record_query, connection)

    '''try:
        add_student_record_query = f"INSERT INTO {table_name} VALUES ({PRN_NO}, '{Student_Name}', '{Email_ID}', {Mobile_No}, {ROLL_No})" 
        execute_query(add_student_record_query,connection)
    except:
        return False'''
    return True