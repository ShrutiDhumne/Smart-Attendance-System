from DB_MakeConnection import make_connection
import pandas as pd
from DB_helper import execute_query

def remove_records(ID_to_remove, table_name):
    connection = make_connection()

    if table_name == 'faculty_records':
        remove_query = f"delete from {table_name} where email_id = '{ID_to_remove}'"
    else:
        remove_query = f'delete from {table_name} where prn_no = {ID_to_remove}'
    if execute_query(remove_query, connection).rowcount == 0:
        return False
    else:
        return True
