from django.shortcuts import render
from .forms import ContactInfoForm, PaymentInfoForm
from django.contrib.auth.decorators import login_required
from cart.models import Cart
import django_countries
from cart.views import add_products_to_order, create_order, clear_user_cart_data


@login_required
def checkout(request):
    '''let's go boys'''
    if 'contactinfo' in request.session:
        if request.method == 'POST':
            form = ContactInfoForm(data=request.POST)
            request.session['contactinfo'] = {
                'name': form['name'].value(),
                'street_name': form['street_name'].value(),
                'house_number': form['house_number'].value(),
                'city': form['house_number'].value(),
                'zip': form['zip'].value(),
                'country': form['country'].value(),
            }

        else:
            form = ContactInfoForm(
                data=request.session['contactinfo']
            )

        context = {
            'contactform': form,
        }

    else:
        if request.method == 'POST':
            form = ContactInfoForm(data=request.POST)
            request.session['contactinfo'] = {
                'name': form['name'].value(),
                'street_name': form['street_name'].value(),
                'house_number': form['house_number'].value(),
                'city': form['house_number'].value(),
                'zip': form['zip'].value(),
                'country': form['country'].value(),
            }
        else:
            form = ContactInfoForm

        context = {
            'contactform': form,
        }

    return render(request, 'checkout/checkout.html', context)

def payment(request):
    '''let's go boys'''
    if 'paymentinfo' in request.session:
        if request.method == 'POST':
            form = PaymentInfoForm(request.POST)
            request.session['paymentinfo'] = {
                'cardholder': form['cardholder'].value(),
                'card_number': form['card_number'].value(),
                'exp_date': form['exp_date'].value(),
                'cvc_code': form['cvc_code'].value(),
            }
        else:
            form = PaymentInfoForm(
                data=request.session['paymentinfo']
            )
        context = {
            'paymentform': form,
        }
    else:
        if request.method == 'POST':
            form = PaymentInfoForm(request.POST)
            request.session['paymentinfo'] = {
                'cardholder': form['cardholder'].value(),
                'card_number': form['card_number'].value(),
                'exp_date': form['exp_date'].value(),
                'cvc_code': form['cvc_code'].value(),
            }
        else:
            form = PaymentInfoForm

        context = {
            'paymentform': form,
        }
    return render(request, 'checkout/payment.html', context)


def review(request):
    carts = Cart.objects.filter(user=request.user)
    total_sum = get_total_cart_price(request)
    if carts.exists():
        #get all the items for this cart
        context = {
            "carts": carts,
            "total_sum": total_sum,
            "name": request.session["contactinfo"]["name"],
            "street": request.session["contactinfo"]["street_name"],
            "house_num": request.session["contactinfo"]["house_number"],
            "city": request.session["contactinfo"]["city"],
            "zip": request.session["contactinfo"]["zip"],
            "country": request.session["contactinfo"]["country"],
            "cardholder": request.session["paymentinfo"]["cardholder"],
            "card": request.session["paymentinfo"]["card_number"][-4:],
            "exp_date": request.session["paymentinfo"]["exp_date"],
        }
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
    # create the order
    newrow = Order(user=request.user)
    newrow.save()

    #
    request.session.pop('contactinfo')
    request.session.pop('paymentinfo')
    return render(request, 'checkout/confirm.html')


def something(request):
    #move everything into an order
    #clear the cart
    #process the payment
    pass