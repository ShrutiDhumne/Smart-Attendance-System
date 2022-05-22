from DB_MakeConnection import make_connection
from DB_helper import execute_query

def create_faculty_table(TABLE_NAME, connection):
    '''create faculty records table if it doest not exist 
    '''

    create_table_query = f"CREATE TABLE IF NOT EXISTS {TABLE_NAME}(Name varchar(30), email_id varchar(30) PRIMARY KEY, password varchar(20))"
    execute_query(create_table_query, connection)

def add_faculty_record(Name, email_id, password, TABLE_NAME):
    '''add faculty record into faculty record table

    Args:
        Name (str): Name of Faculty
        email_id (str): Email-id of Faculty
        password: password for software login 
    ''' 
    
    connection = make_connection()
    create_faculty_table(TABLE_NAME, connection)
    try:
        add_faculty_record_query = f"""INSERT INTO {TABLE_NAME}(Name, email_id, password) VALUES ("{Name}", "{email_id}", "{password}")""" 
        execute_query(add_faculty_record_query,connection)
    except:
        return False
    return True

