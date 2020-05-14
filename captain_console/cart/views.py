from .models import Cart, Order, OrderItem
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
def clear_cart(request):
    pass


@login_required
def get_products_for_order(request):
    product_list = Cart.objects.filter(user=request.user)
    return product_list

@login_required
def add_products_to_order(request, order_id):
    product_list = get_products_for_order(order_id)
    order = Order.objects.get(order_id)

    for product in product_list:
        newrow = OrderItem(order=order, product=product)
        newrow.save()

@login_required
def create_order(request):
    #should be made when user is created and then again after each checkout
    newrow = Order(user=request.user)
    newrow.save()
    return render(request, 'checkout/checkout.html')


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

