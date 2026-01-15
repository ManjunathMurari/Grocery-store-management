
import mysql.connector

__connection = None

def get_sql_connection():
    global __connection
    # Update password if yours is different
    __connection = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='Manju@123',
        database='grocery'
    )
    return __connection