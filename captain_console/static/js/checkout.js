$(document).ready(function() {
    $('#contact-next').on('click', function(e) {
        e.preventDefault();
        $.ajax({
            url: 'checkout/payment',
            type: 'POST',
            success: function(resp) {

            },
            error: function (xhr, status, error) {
                //TODO:this? idfk
                console.error(error);
            }
        })
    });
});