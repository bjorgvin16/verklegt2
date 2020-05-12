from .models import OrderItem, Order
from frontpage.models import Product
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def get_user_pending_order(request):
    ''' getting the order that a user has and hasn't payed for'''
    pass

@login_required
def delete_cart_item(request, item_id):
    '''deletes the item with the item id in the cart'''
    pass

@login_required
def add_item_to_cart(request, product_id):
    '''adds item with item_id to cart'''
    product = get_object_or_404(Product, product_id )
    order_item = OrderItem.objects.create(Item=product)


    pending_order = Order.objects.filter(user=request.user, is_ordered=False) #see if the user has any current orders
    if pending_order.exists():
        order = pending_order

        #check if the order item is in the cart already
        if order.items.filter(product_id=product_id).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)

    else:
        ordered_date = timezone.now()
        order= Order.objects.create(user=request.user)
        order.date_ordered = ordered_date
        order.items.add(order_item)

    context = {"item_id": product_id}
    return 0 #render(request, "cart/index.html", context)

@login_required
def process_payment():
    '''function for checkout basically'''
    pass

@login_required()
def get_order_details(request, **kwargs):
    ''' detailed information about the order'''
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'shopping_cart/order_summary.html', context)

@login_required
def checkout():
    '''let's go boys'''
    pass

@login_required
def update_transaction_records():
    pass


@login_required
def success():
    pass