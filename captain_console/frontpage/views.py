from django.shortcuts import render
#from cart import Order
from .models import Product, Manufacturer


def index(request):
    return render(request, 'frontpage/index.html')

def filter_products(request):
    context = {
        "product": Product.objects.all().order_by("name"),
        "manufacturers": Manufacturer.objects.all()
    }
    return render(request, "navigation.html", context)

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