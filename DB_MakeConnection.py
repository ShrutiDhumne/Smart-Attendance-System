import mysql.connector
#host='localhost', user='root', password='', database='Smart_Attendance_System'
def make_connection(host = "remotemysql.com", user="o67DNqMxP5", password="JHs8dXYWg4", database="o67DNqMxP5"):
    '''make connection with the database

    Args:
        host(str) : host of the database
        user(str) : username of the database
        password(str) : password of the database
    
    Returns:
        <mysql.connector.connection.MySQLConnection object>

    '''
    connection = mysql.connector.connect(
        host = host,
        user = user,
        password = password,
        database = database
    )
    return connection