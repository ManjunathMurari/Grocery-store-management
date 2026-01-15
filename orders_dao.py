

import mysql.connector
from datetime import datetime

def insert_order(connection, order):
    """Inserts a new order and its details into the database."""
    if not connection.is_connected():
        connection.reconnect()

    cursor = connection.cursor(buffered=True)
    try:
        # 1. Insert into orders table (Header)
        order_query = ("INSERT INTO orders (customer_name, total, datetime) VALUES (%s, %s, %s)")
        # Keys match the JS payload: 'customer_name' and 'grand_total'
        order_data = (order['customer_name'], order['grand_total'], datetime.now())
        cursor.execute(order_query, order_data)
        order_id = cursor.lastrowid

        # 2. Insert into order_details table (Line Items)
        order_details_query = ("INSERT INTO order_details (order_id, product_id, quantity, total_price) "
                               "VALUES (%s, %s, %s, %s)")
        
        order_details_data = []
        for detail in order['order_details']:
            order_details_data.append([
                order_id,
                int(detail['product_id']),
                float(detail['quantity']),
                float(detail['total_price'])
            ])
            
        cursor.executemany(order_details_query, order_details_data)
        
        connection.commit()
        return order_id
        
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        cursor.close()

def get_all_orders(connection):
    if not connection.is_connected():
        connection.reconnect()

    cursor = connection.cursor(buffered=True)
    query = ("SELECT order_id, customer_name, total, datetime FROM orders ORDER BY order_id DESC")
    cursor.execute(query)
    
    response = []
    for (order_id, customer_name, total, dt) in cursor:
        response.append({
            'order_id': order_id,
            'customer_name': customer_name,
            'total': float(total),
            'datetime': dt.strftime('%Y-%m-%d %I:%M %p') 
        })
        
    cursor.close()
    return response

def delete_order(connection, order_id):
    if not connection.is_connected():
        connection.reconnect()
        
    cursor = connection.cursor(buffered=True)
    try:
        # Delete children first to avoid Foreign Key errors
        cursor.execute("DELETE FROM order_details WHERE order_id = %s", (order_id,))
        cursor.execute("DELETE FROM orders WHERE order_id = %s", (order_id,))
        connection.commit()
        return order_id
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        cursor.close()

    return response
