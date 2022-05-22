from DB_MakeConnection import make_connection
import pandas as pd
from DB_helper import execute_query

def view_class_subject_data():
    connection = make_connection()
    query = 'show tables'
    tabels = execute_query(query, connection).fetchall()

    class_name, subject_name = [], []
    Class = ('first','second','third', 'fourth')

    for table in tabels:
        table_name = table[0]
        if table_name.decode().startswith(Class) and not table_name.decode().endswith('year'):
            class_name.append(table_name.decode().split("_")[0] + 'year')
            subject_name.append(table_name.decode().split("_")[2])
        
    print(class_name, subject_name)
    return class_name, subject_name

