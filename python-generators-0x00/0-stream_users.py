import mysql.connector

def stream_users():
    
    connection = mysql.connector.connect(
        host='127.0.1.1',         
        user='buna',     
        password='tolosa',
        database='ALX_prodev'     
    )
    
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM user_data")
    
    for row in cursor:
        yield row
    
    cursor.close()
    connection.close()