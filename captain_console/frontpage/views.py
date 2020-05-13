from django.shortcuts import render
#from cart import Order
from .models import Product, Manufacturer
from helpers.views import buildContext
from consoles.models import Console
from games.models import Game

def index(request):
    context = buildContext()
    context["consoles"] = Console.objects.all()
    context["games"] = Game.objects.all()
    return render(request, 'frontpage/index.html', context)

def product_list(request):
    object_list = Product.objects.all()
    filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered = True)
    current_order_products = []
    if filtered_orders.exists():
        user_order = filtered_orders[0]
        user_order_items = user_order.items.all()
        current_order_products = [product.product for product in user_order_items]

        context = {
            'object_list': object_list,
            'current_order_products': current_order_products
        }

        return render(request, 'products/product_list.html', context) # need to redirect this