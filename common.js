// ui/js/common.js

// This file stores the backend API URLs to be used across all frontend scripts.
// If your Flask server port is different from 5000, update the port number below.

var productListApiUrl = 'http://127.0.0.1:5000/getProducts';
var uomListApiUrl = 'http://127.0.0.1:5000/getUOM';
var productSaveApiUrl = 'http://127.0.0.1:5000/insertProduct';
var productDeleteApiUrl = 'http://127.0.0.1:5000/deleteProduct';
var orderSaveApiUrl = 'http://127.0.0.1:5000/insertOrder';