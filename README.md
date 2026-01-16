# Grocery-store-management
"A Full-Stack Grocery Store Management System with a Flask REST API backend, MySQL database integration, and a dynamic jQuery frontend for managing inventory and processing customer orders."


🚀 How to Run the Project
Follow these steps to get the GSMS application running on your local machine:

1. Database Setup (MySQL)
Open your MySQL Workbench or terminal.

Create a database named grocery_store.

Import the SQL schema provided in the /database folder (or run your create_table scripts) to set up the products, uom, and orders tables.




2. Backend Setup (Flask)
Navigate to the backend folder in your terminal.

Install the required dependencies:

Bash

pip install flask flask-cors mysql-connector-python
Start the Flask server:

Bash

python server.py
The backend will now be running at http://127.0.0.1:5000.





3. Frontend Setup
Simply open index.html (or order.html) from the ui folder in any modern web browser.

Note: Ensure the Flask server is running first so the jQuery AJAX calls can successfully fetch your product data!
