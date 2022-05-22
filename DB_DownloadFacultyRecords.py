from DB_MakeConnection import make_connection
import pandas as pd
from DB_helper import execute_query

def download_faculty_records(table_name="faculty_records"):
    try :
        connection = make_connection()
 
        get_column_name_query  = f"SHOW COLUMNS from {table_name}"
        get_data_query  = f"select * from {table_name}"
        
        column_names  = execute_query(get_column_name_query ,connection).fetchall()
        data = execute_query(get_data_query, connection).fetchall()
        column_names = [column_name[0] for column_name in column_names]
        
        faculty_records = pd.DataFrame(data, columns=column_names)
        faculty_records.to_csv("Downloads/faculty_records.csv")
        return True
    except:
        return False

