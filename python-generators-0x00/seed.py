import mysql.connector
import csv
import uuid

def connect_db():
    """Connect to the MySQL server."""
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='buna',  
            password='tolosa'  
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_database(connection):
    """Create the ALX_prodev database if it does not exist."""
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    cursor.close()
    print("Database ALX_prodev created successfully.")

def connect_to_prodev():
    """Connect to the ALX_prodev database."""
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='buna', 
            password='Tolosa',  
            database='ALX_prodev'
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_table(connection):
    """Create the user_data table if it does not exist."""
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id CHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL(3, 0) NOT NULL
        )
    """)
    cursor.close()
    print("Table user_data created successfully.")

def insert_data(connection, csv_file):
    """Insert data from a CSV file into the user_data table."""
    cursor = connection.cursor()
    
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            user_id = str(uuid.uuid4())
            name = row['name']
            email = row['email']
            age = row['age']
            cursor.execute("""
                INSERT INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE name = VALUES(name), email = VALUES(email), age = VALUES(age)
            """, (user_id, name, email, age))
    
    connection.commit()
    cursor.close()
    print("Data inserted successfully.")

