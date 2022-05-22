from DB_MakeConnection import make_connection 
from DB_helper import execute_query
def get_subjects(Class):

    subject_tables = []
    connection = make_connection()
    get_subjects_query = "SHOW tables"
    tables = execute_query(get_subjects_query, connection).fetchall()
    for i in tables:
        if i[0].decode().startswith(Class.lower()) and not i[0].decode().endswith('year'):
            subject_tables.append(i[0].decode())

    return subject_tables
    