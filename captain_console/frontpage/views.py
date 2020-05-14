from django.shortcuts import render
#from cart import Order
from users.models import ProductView
from helpers.views import buildContext
from consoles.models import Console
from games.models import Game
from accessories.models import Accessory
from .models import Product

def index(request):
    context = buildContext()
    context["consoles"] = Console.objects.all().order_by("-dateAdded")
    context["games"] = Game.objects.all().order_by("-dateAdded")
    return render(request, 'frontpage/index.html', context)

def get_all_products(request):
    context = buildContext()
    context["products"] = Product.objects.all().order_by("name")
    context["games"] = Game.objects.all()
    context["consoles"] = Console.objects.all()
    context["accessories"] = Accessory.objects.all()
    return render(request, 'frontpage/all_products.html', context)

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
    if request.user.is_authenticated:
        context["views"] = ProductView.objects.filter(user=request.user)
    context["consoles"] = Console.objects.all()
    context["game"] = Game.objects.all()
    return render(request, 'frontpage/index.html', context)
