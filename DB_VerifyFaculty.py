from DB_MakeConnection import make_connection
from DB_helper import execute_query

def verify_faculty(email_id, password):
    connection = make_connection()

    try:
        query = f"select password from {faculty_records} where email_id = '{email_id}'" 