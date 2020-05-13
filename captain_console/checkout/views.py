from django.shortcuts import render
from .forms import ContactInfoForm, PaymentInfoForm
from django.contrib.auth.decorators import login_required
from django_countries import Countries

@login_required
def checkout(request):
    '''let's go boys'''
    print('are you a product?')
    print("cause I'd like to check you out")
    context = {
        'contactform': ContactInfoForm,
        'paymentform': PaymentInfoForm,
        'countries': Countries
    }
    return render(request, 'checkout/checkout.html', context)
