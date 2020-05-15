$(document).ready(function(){
    $('.addtocart').on('click',function(e) {
        e.preventDefault();
        var product_id = $('.addtocart').val(data.data)
        $.ajax({
            url: 'cart/add-to-cart/' + product_id,
            type: 'POST',
            success: function(resp) {

            },
            error : function(xhr, status, error) {
                //TODO: this
                console.log(error);
            }
        })
    });

});





$(document).ready(function() {
    $('.add-to-cart').on('click', function(e) {
        //var id = {{product_id}}
        e.preventDefault();
        $.ajax({
            url: 'cart/add-to-cart/' + id, // tharf alvurur id herna
            type: 'POST',
            success: function(resp) {

            },
            error: function (xhr, status, error) {
                //TODO:this?
                console.error(error);
            }
        })
    });
});