from django import render, redirect
from django.contrib.auth import login_required


def get_user_pending_order():
    ''' getting the order that a user has and hasn't payed for'''
    pass

@login_required
def delete_item(request, item_id):
    '''deletes the item with the item id in the cart'''
    pass

@login_required
def add_item_to_cart(request, item_id):
    '''adds item with item_id to cart'''

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