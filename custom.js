$(function () {
    // 1. Manage Products Table
    if ($("table#productTable").length > 0) {
        $.get('http://127.0.0.1:5000/getProducts', function (response) {
            if (response) {
                var table = '';
                $.each(response, function(index, product) {
                    table += '<tr data-id="'+ product.product_id +'">' +
                        '<td>' + product.name + '</td>' +
                        '<td>' + product.uom_name + '</td>' +
                        '<td>' + product.price_per_unit + ' Rs</td>' +
                        '<td><button class="btn btn-sm btn-danger delete-product">Delete</button></td></tr>';
                });
                $("table#productTable tbody").empty().html(table);
            }
        });
    }

    // 2. Load UOM Dropdown (Fixes the 404 error)
    if ($("#uoms").length > 0) {
        $.get('http://127.0.0.1:5000/getUOM', function (response) {
            if (response) {
                var options = '<option value="">--Select Unit--</option>';
                $.each(response, function (index, uom) {
                    options += '<option value="' + uom.uom_id + '">' + uom.uom_name + '</option>';
                });
                $("#uoms").empty().html(options);
            }
        });
    }

    // 3. Save New Product
    $("#saveProduct").on("click", function () {
        var data = {
            name: $("#name").val(),
            uom_id: $("#uoms").val(),
            price_per_unit: $("#price").val()
        };
        $.post('http://127.0.0.1:5000/insertProduct', {data: JSON.stringify(data)}, function () {
            location.reload();
        });
    });

    // 4. Delete Product
    $(document).on("click", ".delete-product", function () {
        var tr = $(this).closest('tr');
        if (confirm("Delete this product?")) {
            $.post('http://127.0.0.1:5000/deleteProduct', {product_id: tr.data('id')}, function () {
                location.reload();
            });
        }
    });

    // 5. Save Order Logic
    $("#saveOrder").on("click", function () {
        var customerName = $("#customerName").val();
        var grandTotal = $("#grandTotal").text().replace(/[^\d.]/g, ''); 
        
        if(!customerName || $("table#orderTable tbody tr").length === 0) {
            alert("Please enter customer name and add items.");
            return;
        }

        var orderDetails = [];
        $("table#orderTable tbody tr").each(function () {
            var row = $(this);
            orderDetails.push({
                product_id: row.find('.product-id').val(),
                quantity: row.find('.product-qty').val(),
                total_price: row.find('.product-total').text().replace(/[^\d.]/g, '')
            });
        });

        var requestPayload = {
            customer_name: customerName,
            grand_total: grandTotal,
            order_details: orderDetails
        };

        $.post('http://127.0.0.1:5000/insertOrder', {'data': JSON.stringify(requestPayload)}, function (response) {
            alert("Order Saved! ID: " + response.order_id);
            window.location.href = 'index.html';
        });
    });
});