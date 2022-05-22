from DB_MakeConnection import make_connection
from DB_helper import execute_query


def display_records(table_name='faculty_records'):

    try:
        connection = make_connection()
        query = f'SELECT * FROM {table_name}' 
        faculty_records = execute_query(query,connection).fetchall()
    except:
        return False
    return faculty_records

