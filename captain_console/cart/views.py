from .models import Cart
from frontpage.models import Product
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ContactInfoForm, PaymentInfoForm


@login_required
def delete_cart_item(request, product_id):
    '''deletes the item with the item id in the cart'''
    row = Cart.objects.get(request.user, product_id)
    row.delete()
    return render(request, 'cart/index.html')

@login_required
def add_item_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    newrow = Cart(user=request.user, product=product)
    newrow.save()
    return render(request, 'cart/index.html')

@login_required
def process_payment():
    '''function for checkout basically'''
    pass

@login_required()
def get_cart_items(request):
    cart = Cart.objects.filter(user=request.user)
    if cart.exists():
        #get all the items for this cart
        context = {"carts": Cart.objects.all()}
        return render(request, 'cart/index.html', context)
    else:
        return render(request, 'cart/empty.html')

@login_required
def checkout(request):
    '''let's go boys'''
    print('are you a product?')
    print("cause I'd like to check you out")
    context = {
        'contactform': ContactInfoForm,
        'paymentform': PaymentInfoForm,
    }
    return render(request, 'cart/checkout.html', context)


@login_required
def success(request):
    print('wow, so much success')
    print('this is so amazing')
    return render(request, 'cart/index.html')