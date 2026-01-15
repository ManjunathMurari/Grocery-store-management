import mysql.connector

__connection = None

def get_sql_connection():
    global __connection
    # We create a new connection or return the existing one
    # Note: In your server.py, you are closing connections, 
    # so we should ensure this returns a fresh one if needed.
    return mysql.connector.connect(
        user='root',
        password='Manju@123', # Replace with your actual password
        host='127.0.0.1',
        database='grocery' # Changed from 'grocery_store' to 'grocery'
    )
