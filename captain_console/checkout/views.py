from django.shortcuts import render
from .forms import ContactInfoForm, PaymentInfoForm
from django.contrib.auth.decorators import login_required
from cart.models import Cart, Order, OrderItem
from django.utils import timezone
from django_countries import countries

@login_required
def checkout(request):

    # Checks if user has filled out contactform before
    if 'contactinfo' in request.session:

        # Checks if user is making a post request (submitting the form)
        if request.method == 'POST':
            # Then updates the form with the input data and saves it to the session
            form = ContactInfoForm(data=request.POST)
            request.session['contactinfo'] = {
                'name': form['name'].value(),
                'street_name': form['street_name'].value(),
                'house_number': form['house_number'].value(),
                'city': form['house_number'].value(),
                'zip': form['zip'].value(),
                'country': form['country'].value(),
            }

        # If its a get request (navigating between forms) populate form with data from session
        else:
            form = ContactInfoForm(
                data=request.session['contactinfo']
            )

        context = {
            'contactform': form,
        }

    # If data is not in session
    else:
        # and if request is a post request
        if request.method == 'POST':
            # Save the data to the session and update the form
            form = ContactInfoForm(data=request.POST)
            request.session['contactinfo'] = {
                'name': form['name'].value(),
                'street_name': form['street_name'].value(),
                'house_number': form['house_number'].value(),
                'city': form['house_number'].value(),
                'zip': form['zip'].value(),
                'country': form['country'].value(),
            }
        # If its a get request, fetch a blank form
        else:
            form = ContactInfoForm

        context = {
            'contactform': form,
        }

    return render(request, 'checkout/checkout.html', context)

def payment(request):

    # If payment info exists in session
    if 'paymentinfo' in request.session:
        # And request is a post request
        if request.method == 'POST':
            # Update form and data in the session
            form = PaymentInfoForm(request.POST)
            request.session['paymentinfo'] = {
                'cardholder': form['cardholder'].value(),
                'card_number': form['card_number'].value(),
                'exp_date': form['exp_date'].value(),
                'cvc_code': form['cvc_code'].value(),
            }
        # If request is a get request (navigatin between forms), populate form with data from session
        else:
            form = PaymentInfoForm(
                data=request.session['paymentinfo']
            )
        context = {
            'paymentform': form,
        }
    # If data does not exist in session,
    else:
        if request.method == 'POST':
            # But request is a post request, update form and session data
            form = PaymentInfoForm(request.POST)
            request.session['paymentinfo'] = {
                'cardholder': form['cardholder'].value(),
                'card_number': form['card_number'].value(),
                'exp_date': form['exp_date'].value(),
                'cvc_code': form['cvc_code'].value(),
            }
        # If request is a get request, fetch a blank form
        else:
            form = PaymentInfoForm

        context = {
            'paymentform': form,
        }
    return render(request, 'checkout/payment.html', context)


def review(request):
    cart = Cart.objects.filter(user=request.user)
    total_sum = get_total_cart_price(request)
    # If data from both checkout forms exist in session, let user review
    if 'paymentinfo' in request.session and 'contactinfo' in request.session:

        # Get name of country instead of country code
        country = dict(countries)[request.session["contactinfo"]["country"]]
        context = {
            "cart": cart,
            "total_sum": total_sum,
            "name": request.session["contactinfo"]["name"],
            "street": request.session["contactinfo"]["street_name"],
            "house_num": request.session["contactinfo"]["house_number"],
            "city": request.session["contactinfo"]["city"],
            "zip": request.session["contactinfo"]["zip"],
            "country": country,
            "cardholder": request.session["paymentinfo"]["cardholder"],
            "card": request.session["paymentinfo"]["card_number"][-4:],
            "exp_date": request.session["paymentinfo"]["exp_date"],
            "not_filled": False, # Set not_filled to False
        }
    else:
        # If one or neither forms exist in session, set not_filled
        context = {
            "not_filled": True,
        }
    return render(request, 'checkout/review.html', context)


def get_total_cart_price(request):
    total_sum = 0
    product_list = Cart.objects.filter(user=request.user)
    for cart in product_list:
        total_sum += cart.product.price
    return total_sum

def confirm(request):
    # create the order for the orderID - userID table
    newrow = Order(
        user=request.user,
        orderDate = timezone.now(),
        firstName = request.session["contactinfo"]["name"],
        lastName =request.session["contactinfo"]["name"],
        streetName =request.session["contactinfo"]["street_name"],
        houseNumber =request.session["contactinfo"]["house_number"],
        zipCode =request.session["contactinfo"]["zip"],
        city =request.session["contactinfo"]["city"],
        country =request.session["contactinfo"]["country"]
        )
    newrow.save()
    order_id = newrow.id

    #create an OrderItem with all the information for an order
    cart_list = Cart.objects.filter(user=request.user) # list of Carts
    order = Order.objects.get(id=order_id)
    for cart in cart_list:
        newrow = OrderItem(order=order, product=cart.product, quantity=cart.quantity) # how to do quantity big brain plz
        newrow.save()

    #clear the cart
    for data in cart_list:
        data.delete()

    #clear the user contact and payment data from sessions
    request.session.pop('contactinfo')
    request.session.pop('paymentinfo')
    return render(request, 'checkout/confirm.html')
