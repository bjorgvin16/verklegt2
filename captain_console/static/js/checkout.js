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

$(document).ready(function() {
    $('#payment-next').on('click', function(e) {
        e.preventDefault();
        $.ajax({
            url: 'checkout/review',
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

$(document).ready(function() {
    $('#payment-prev').on('click', function(e) {
        e.preventDefault();
        $.ajax({
            url: 'checkout/contact',
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

$(document).ready(function() {
    $('#review-prev').on('click', function(e) {
        e.preventDefault();
        $.ajax({
            url: 'checkout/payment',
            type: 'GET',
            success: function(resp) {

            },
            error: function (xhr, status, error) {
                //TODO:this? idfk
                console.error(error);
            }
        })
    });
});