from DB_MakeConnection import make_connection
from DB_helper import execute_query

def add_class(Class):
    table_name = Class.get()
    connection = make_connection()

    try:
        create_table_query = f"CREATE TABLE {table_name}(PRN_NO int PRIMARY KEY, STUDENT_NAME varchar(40), EMAIL_ID varchar(40), Mobile_No BIGINT, ROLL_No INT)"
        execute_query(create_table_query,connection)
    except:
        print('yes')
        return False

    return True

def remove_class(Class):

    table_name = Class.get()
    connection = make_connection()

    subject_tables_query = "Show tables"
    subject_tables = execute_query(subject_tables_query,connection).fetchall()

    count =0 

    for table in subject_tables:
        if table[0].startswith(table_name):
            count+=1
            remove_table_query  = f"DROP TABLE {table[0]}"
            execute_query(remove_table_query, connection)

    if count == 0:
        return False
    return True
    
def add_subject(Class, subject):

    table_name = Class.get() +"_"+ subject.get()
    connection = make_connection()

    try:
        get_prn_no = f"select PRN_NO from {Class.get()}"
        PRN_NO = execute_query(get_prn_no,connection).fetchall()
    except:
        return None

    try:
        create_subject_table_query  = f"CREATE TABLE {table_name} (PRN_NO INT)"
        execute_query(create_subject_table_query, connection)
    except:
        return False

    for PRN in PRN_NO:
        print(PRN)
        insert_prn_into_subject_table = f"Insert into {table_name} values ({PRN[0]})"
        execute_query(insert_prn_into_subject_table,connection)

    return True

def remove_subject(Class, subject):

    table_name = Class.get() + "_" + subject.get()
    connection = make_connection()

    try:
        remove_table_query  = f"DROP TABLE {table_name}"
        execute_query(remove_table_query, connection)
    except:
        return False

    return True
    
