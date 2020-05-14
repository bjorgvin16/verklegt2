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
        print(form['country'].value())
    print('are you a product?')
    print("cause I'd like to check you out")
    context = {
        'contactform': ContactInfoForm,
    }
    return render(request, 'checkout/checkout.html', context)

def payment(request):
    '''let's go boys'''

    print('are you a payment product?')
    print("cause I'd like to pay you out")
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