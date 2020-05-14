from .models import Cart
from frontpage.models import Product
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from checkout.forms import ContactInfoForm, PaymentInfoForm
from django_countries import Countries
import datetime

@login_required
def delete_cart_item(request, cart_id):
    '''deletes the item with the item id in the cart'''
    row = Cart.objects.get(id=cart_id)
    row.delete()
    return render(request, 'cart/index.html')

@login_required
def add_item_to_cart(request, product_id):
    print('I was here')
    # if request.method == 'POST'
    product = get_object_or_404(Product, pk=product_id)
    newrow = Cart(user=request.user, product=product)
    newrow.save()
    return render(request, 'frontpage/index.html')

@login_required
def add_products_to_order(request):
    '''adding orders'''
    pass


@login_required()
def get_cart_items(request):
    carts = Cart.objects.filter(user=request.user)
    if carts.exists():
        #get all the items for this cart
        context = {"carts": carts}
        return render(request, 'cart/index.html', context)
    else:
        return render(request, 'cart/empty.html')

@login_required
def success(request):
    print('wow, so much success')
    print('this is so amazing')
    return render(request, 'cart/index.html')

