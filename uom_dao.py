def get_uoms(connection):
    cursor = connection.cursor(buffered=True)
    query = ("SELECT * FROM uom")
    cursor.execute(query)
    response = []
    for (uom_id, uom_name) in cursor:
        response.append({'uom_id': uom_id, 'uom_name': uom_name})
    cursor.close()
    return response