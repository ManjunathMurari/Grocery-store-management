var allProducts = [];

$(function () {
    // 1. Fetch products to populate the dropdown
    $.get(productListApiUrl, function (response) {
        if(response) {
            allProducts = response;
            var options = '<option value="">-- Select Product --</option>';
            $.each(allProducts, function(index, product) {
                options += '<option value="'+ product.product_id +'">'+ product.name +'</option>';
            });
            $("#productList").html(options);
        }
    });
});

// 2. Update price field when product is selected
$("#productList").change(function () {
    var productId = $(this).val();
    var product = allProducts.find(p => p.product_id == productId);
    $("#productPrice").val(product ? product.price_per_unit : "");
});

// 3. Add Item to Table
$("#addOrderRow").click(function () {
    var productId = $("#productList").val();
    var name = $("#productList option:selected").text();
    var price = parseFloat($("#productPrice").val());
    var qty = parseFloat($("#productQty").val());
    var total = price * qty;

    if(!productId || isNaN(qty)) return alert("Please select product and quantity");

    var row = `<tr data-id="${productId}" data-total="${total}">
                <td>${name}</td>
                <td>${price.toFixed(2)}</td>
                <td>${qty}</td>
                <td>${total.toFixed(2)}</td>
                <td><button class="btn btn-danger btn-sm remove-row">X</button></td>
               </tr>`;
    
    $("#orderTable tbody").append(row);
    calculateGrandTotal();
});

// 4. Calculate Grand Total
function calculateGrandTotal() {
    var grandTotal = 0;
    $("#orderTable tbody tr").each(function() {
        grandTotal += parseFloat($(this).data("total"));
    });
    $("#grandTotal").text(grandTotal.toFixed(2));
}

// 5. Remove Row
$(document).on("click", ".remove-row", function () {
    $(this).closest("tr").remove();
    calculateGrandTotal();
});

// 6. Save Order to Backend
$("#saveOrder").click(function () {
    var orderDetails = [];
    $("#orderTable tbody tr").each(function() {
        orderDetails.push({
            product_id: $(this).data("id"),
            quantity: $(this).find("td:eq(2)").text(),
            total_price: $(this).data("total")
        });
    });

    var requestPayload = {
        customer_name: $("#customerName").val(),
        grand_total: $("#grandTotal").text(),
        order_details: orderDetails
    };

    if(!requestPayload.customer_name || orderDetails.length === 0) return alert("Details missing!");

    $.post(orderSaveApiUrl, { 'data': JSON.stringify(requestPayload) }, function (response) {
        alert("Order Saved Successfully! Order ID: " + response.order_id);
        location.reload();
    });
});