import mysql.connector

#host='b1d548joznqwkwny7elp-mysql.services.clever-cloud.com', user='uprrqljln2zkcgtq', password='UBKHGqi4XGkGAb1Zy4En', database='bmdimdcqducjlo3jzyii'
def make_connection(host='localhost', user='root', password='', database='Smart_Attendance_System'):
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

