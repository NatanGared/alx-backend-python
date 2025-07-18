import mysql.connector

def stream_user_ages():
    connection = mysql.connector.connect(
            host='127.0.1.1',         
            user='buna',     
            password='tolosa',
            database='ALX_prodev'     
        )
    
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")
    
    for (age,) in cursor:
        yield age
    
    cursor.close()
    connection.close()

def calculate_average_age():
    total_age = 0
    count = 0
    
    for age in stream_user_ages():
        total_age += age
        count += 1
    
    if count == 0:
        return 0 
    
    return total_age / count

if __name__ == "__main__":
    average_age = calculate_average_age()
    print(f"Average age of users: {average_age:.2f}")