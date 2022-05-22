def execute_query(query,connection):
    '''execute query

    Args:
        query (str): query to be executed
        connection (connection object): 
    '''

    cursor = connection.cursor(buffered = True)
    cursor.execute(query)
    
    connection.commit()

    return cursor
