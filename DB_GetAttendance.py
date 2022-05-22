from DB_MakeConnection import make_connection
from DB_helper import execute_query

def get_attendance(table_name):
    connection = make_connection()
    
    get_column_name_query  = f"DESCRIBE {table_name}"
    get_data_query  = f"select * from {table_name}"

    column_names  = execute_query(get_column_name_query ,connection).fetchall()[1:]
    data = execute_query(get_data_query, connection).fetchall()

    column_names = [i[0] for i  in column_names]
    PRN_NO = [i[0] for i in data]
    attendance = [i[1:] for i in data]


    return column_names, PRN_NO, attendance

def get_daily_attendance(table_name, date):
    connection = make_connection()

    get_data_query = f"select PRN_NO, {date} from {table_name}"
    data = execute_query(get_data_query,connection).fetchall()
    print(data)

    PRN_NO = [i[0] for i in data]
    attendance = [i[1:] for i in data]

    return PRN_NO, attendance

