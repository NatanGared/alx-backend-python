import mysql.connector

def paginate_users(page_size, offset):
    connection = mysql.connector.connect(
            host='127.0.1.1',         
            user='buna',     
            password='tolosa',
            database='ALX_prodev'     
        )
    
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    
    return rows

def lazy_paginate(page_size):
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size