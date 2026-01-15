import mysql.connector

def get_uoms(connection):
    # 1. Check if connection is alive. If not, reconnect.
    if not connection.is_connected():
        connection.reconnect()

    cursor = connection.cursor(buffered=True)
    query = ("SELECT * FROM uom")
    cursor.execute(query)
    
    response = []
    for (uom_id, uom_name) in cursor:
        response.append({
            'uom_id': uom_id,
            'uom_name': uom_name
        })
        
    cursor.close()
    return response
