import sqlite3

class ExecuteQuery:
    def __init__(self, db_name, query, params=None):
        self.db_name = db_name
        self.query = query
        self.params = params or ()
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        return self 

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()

    def execute(self):
        cursor = self.connection.cursor()
        cursor.execute(self.query, self.params)
        return cursor.fetchall()

query = "SELECT * FROM users WHERE age > ?"
params = (25,)

with ExecuteQuery('users.db', query, params) as executor:
    results = executor.execute() 
    print(results)  