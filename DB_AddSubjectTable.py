from DB_MakeConnection import make_connection
from DB_helper import execute_query

def add_subject_table(Class, subject):

    table_name = Class.get() +"_"+ subject.get()
    Connection = make_connection()

    get_prn_no = f"select PRN_NO from {Class.get()}"
    PRN_NO = execute_query(get_prn_no,Connection).fetchall()

    create_subject_table_query  = f"CREATE TABLE IF NOT EXISTS {table_name} (PRN_NO INT)"
    execute_query(create_subject_table_query, Connection)

    for PRN in PRN_NO:
        print(PRN)
        insert_prn_into_subject_table = f"Insert into {table_name} values ({PRN[0]})"
        execute_query(insert_prn_into_subject_table,Connection)
    



    
