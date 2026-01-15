import mysql.connector

__cnx = None

def get_sql_connection():
    global __cnx
    # Only create a new connection if it doesn't already exist
    if __cnx is None:
        __cnx = mysql.connector.connect(
            user='root', 
            password='root', # Replace with your MySQL password
            host='127.0.0.1',
            database='grocery_store'
        )
    return __cnx