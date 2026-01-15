

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from sql_connection import get_sql_connection
import products_dao
import orders_dao
import uom_dao

app = Flask(__name__)
# CORS allows your HTML files to talk to this Python server
CORS(app)

@app.route('/getUOM', methods=['GET'])
def get_uom():
    connection = get_sql_connection()
    try:
        response = uom_dao.get_uoms(connection)
        return jsonify(response)
    finally:
        connection.close()

@app.route('/getProducts', methods=['GET'])
def get_products():
    connection = get_sql_connection()
    try:
        response = products_dao.get_all_products(connection)
        return jsonify(response)
    finally:
        connection.close()

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    connection = get_sql_connection()
    try:
        product_id = products_dao.insert_new_product(connection, request_payload)
        return jsonify({'product_id': product_id})
    finally:
        connection.close()

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    connection = get_sql_connection()
    try:
        product_id = request.form['product_id']
        return_id = products_dao.delete_product(connection, product_id)
        return jsonify({'product_id': return_id})
    finally:
        connection.close()

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    connection = get_sql_connection()
    try:
        response = orders_dao.get_all_orders(connection)
        return jsonify(response)
    finally:
        connection.close()

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    connection = get_sql_connection()
    try:
        order_id = orders_dao.insert_order(connection, request_payload)
        return jsonify({'order_id': order_id})
    finally:
        connection.close()

@app.route('/deleteOrder', methods=['POST'])
def delete_order():
    connection = get_sql_connection()
    try:
        order_id = request.form['order_id']
        orders_dao.delete_order(connection, order_id)
        return jsonify({'order_id': order_id})
    finally:
        connection.close()

if __name__ == "__main__":
    print("Starting Grocery Store Server...")
    app.run(port=5000, debug=True)
