import mysql.connector

def get_all_products(connection):
    if not connection.is_connected():
        connection.reconnect()

    cursor = connection.cursor(buffered=True)
    # Correct query for the 'grocery' database
    query = (
        "SELECT products.product_id, products.name, products.uom_id, "
        "products.price_per_unit, uom.uom_name "
        "FROM products "
        "INNER JOIN uom ON products.uom_id = uom.uom_id"
    )
    
    cursor.execute(query)
    response = []
    
    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'product_id': product_id,
            'name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        })
    
    cursor.close()
    return response

def insert_new_product(connection, product):
    if not connection.is_connected():
        connection.reconnect()

    cursor = connection.cursor(buffered=True)
    query = ("INSERT INTO products (name, uom_id, price_per_unit) VALUES (%s, %s, %s)")
    
    # We use .get() and check multiple possible keys to prevent NULL errors
    name = product.get('product_name') or product.get('name')
    uom_id = product.get('uom_id')
    price = product.get('price_per_unit')

    data = (name, uom_id, price)
    
    try:
        cursor.execute(query, data)
        connection.commit()
        last_id = cursor.lastrowid
    except Exception as e:
        connection.rollback()
        print(f"Error occurred: {e}")
        raise e
    finally:
        cursor.close()
        
    return last_id

def delete_product(connection, product_id):
    if not connection.is_connected():
        connection.reconnect()

    cursor = connection.cursor(buffered=True)
    query = ("DELETE FROM products WHERE product_id = %s")
    
    try:
        cursor.execute(query, (product_id,))
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        cursor.close()
        
    return product_id
