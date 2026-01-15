$(function () {
    // Load products and UOM list when the page opens
    loadProducts();

    $.get('http://127.0.0.1:5000/getUOM', function (response) {
        if (response) {
            var options = '<option value="">-- Select Unit --</option>';
            $.each(response, function (index, uom) {
                options += '<option value="' + uom.uom_id + '">' + uom.uom_name + '</option>';
            });
            $("#uoms").html(options);
        }
    });
});

function loadProducts() {
    $.get('http://127.0.0.1:5000/getProducts', function (response) {
        if (response) {
            var table = '';
            $.each(response, function (index, product) {
                table += '<tr>' +
                    '<td>' + product.name + '</td>' +
                    '<td>' + product.uom_name + '</td>' +
                    '<td>' + product.price_per_unit + ' Rs</td>' +
                    '<td><button class="btn btn-sm btn-danger delete-product" data-id="' + product.product_id + '">Delete</button></td>' +
                '</tr>';
            });
            $("#productsTable tbody").html(table);
        }
    });
}

// Logic for the Save Button
$("#saveProduct").on("click", function () {
    var data = {
        product_name: $("#name").val(),    
        uom_id: $("#uoms").val(),         
        price_per_unit: $("#price").val()  
    };

    if (!data.product_name || !data.uom_id || !data.price_per_unit) {
        alert("Please fill all fields!");
        return;
    }

    $.post('http://127.0.0.1:5000/insertProduct', {
        'data': JSON.stringify(data)
    }, function (response) {
        $("#productModal").modal('hide');
        $("#productForm")[0].reset();
        loadProducts(); // Refresh the table
    });
});

$(document).on("click", ".delete-product", function () {
    var id = $(this).data('id');
    if (confirm("Are you sure you want to delete this product?")) {
        $.post('http://127.0.0.1:5000/deleteProduct', { 'product_id': id }, function (response) {
            loadProducts();
        });
    }
});