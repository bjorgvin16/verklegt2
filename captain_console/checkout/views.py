from django.shortcuts import render
from .forms import ContactInfoForm, PaymentInfoForm
from django.contrib.auth.decorators import login_required
from django_countries import Countries
from cart.models import Cart
from cart.views import add_products_to_order, create_order, clear_user_cart_data


@login_required
def checkout(request):
    '''let's go boys'''
    if request.method == 'POST':
        form = ContactInfoForm(request.POST)
        request.session['contactinfo'] = {
            'name': form['contact'].value(),
            'street': form['street_name'].value(),
            'house_num': form['house_number'].value(),
            'city': form['house_number'].value(),
            'zip': form['zip'].value(),
            'country': form['country'].value(),
        }

        context = {
            'contactform': form,
        }

    else:
        context = {
            'contactform': ContactInfoForm,
        }
    return render(request, 'checkout/checkout.html', context)

def payment(request):
    '''let's go boys'''
    if request.method == 'POST':
        form = PaymentInfoForm(request.POST)
        request.session['paymentinfo'] = {
            'cardholder': form['cardholder'].value(),
            'card': form['card_number'].value(),
            'exp-date': form['exp_date'].value(),
            'cvc': form['cvc_code'].value(),
        }
        context = {
            'paymentform': form,
        }

    else:
        context = {
            'paymentform': PaymentInfoForm,
        }
    return render(request, 'checkout/payment.html', context)


def review(request):
    carts = Cart.objects.filter(user=request.user)
    total_sum = get_total_cart_price(request)
    if carts.exists():
        #get all the items for this cart
        context = {"carts": carts, "total_sum": total_sum}
        return render(request, 'checkout/review.html', context)
    else:
        return 0

def get_total_cart_price(request):
    total_sum = 0
    product_list = Cart.objects.filter(user=request.user)
    for cart in product_list:
        total_sum += cart.product.price
    return total_sum

def confirm(request):
    create_order(request)
    add_products_to_order(request)
    clear_user_cart_data(request)
    pass


def something(request):
    #move everything into an order
    #clear the cart
    #process the payment
    pass