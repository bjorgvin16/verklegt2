from helpers.views import findTypeFromId
from .models import Cart, Order, OrderItem
from frontpage.models import Product
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required

#############       CART FUNCTIONS

@login_required
def clear_user_cart_data(request):
    data_to_delete = Cart.objects.filter(user=request.user)
    for data in data_to_delete:
        data.delete()
    return render(request, 'cart/index.html')

@login_required
def delete_cart_item(request, cart_id):
    '''deletes the item with the item id in the cart'''
    carts = Cart.objects.filter(user=request.user)
    if carts.exists():
        row = Cart.objects.get(id=cart_id)
        row.delete()
    if carts.exists():
        return get_cart_items(request)
    else:
        return render(request, 'cart/empty.html')

@login_required
def add_item_to_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        newrow = Cart(user=request.user, product=product, quantity=request.POST["quantity"])
        newrow.save()
        type = findTypeFromId(product_id)

        if type == "game":
            return redirect('/games/' + str(product_id))
        elif type == "console":
            return redirect('/consoles/' + str(product_id))
        elif type == "accessory":
            return redirect('/accessories/' + str(product_id))

@login_required()
def get_cart_items(request):
    carts = Cart.objects.filter(user=request.user)
    total_price = get_total_cart_price(request)
    if carts.exists():
        #get all the items for this cart
        context = {"carts": carts, "total_price": total_price}
        return render(request, 'cart/index.html', context)
    else:
        return render(request, 'cart/empty.html')


@login_required
def get_total_cart_price(request):
    total_sum = 0
    product_list = Cart.objects.filter(user=request.user)
    for cart in product_list:
        total_sum += cart.product.price
    print(total_sum)

    return total_sum

############           ORDER FUNCTIONS


@login_required
def add_products_to_order(request, order_id):
    product_list = Cart.objects.filter(user=request.user)
    order = Order.objects.get(order_id)

    for product in product_list:
        newrow = OrderItem(order=order, product=product)
        newrow.save()

    return render(request, 'frontpage/index.html')

@login_required
def create_order(request):
    newrow = Order(user=request.user)
    newrow.save()
    #return render(request, 'checkout/checkout.html')


