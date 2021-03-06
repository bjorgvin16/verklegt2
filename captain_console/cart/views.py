from helpers.views import findTypeFromId
from .models import Cart
from frontpage.models import Product
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required

#CART FUNCTIONS

@login_required
def clear_user_cart_data(request):
    data_to_delete = Cart.objects.filter(user=request.user)

    for data in data_to_delete:
        data.delete()
    return render(request, 'cart/empty.html')

@login_required
def delete_cart_item(request, cart_id):
    '''deletes the item with the item id in the cart'''
    carts = Cart.objects.filter(user=request.user)
    row = Cart.objects.get(id=cart_id)
    product = row.product

    #updates the quantity
    quantity = row.quantity
    row.product.leftInStock += quantity
    row.product.save()

    #actually deletes the cart item
    row.delete()

    #sending the user back to their cart or an empty cart
    if carts.exists():
        return get_cart_items(request)
    else:
        return render(request, 'cart/empty.html')

@login_required
def add_item_to_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)

        #if the product is already in the user's cart
        if Cart.objects.filter(user=request.user, product=product).exists():
            cart = Cart.objects.get(user=request.user, product=product)
            cart.quantity += int(request.POST["quantity"])
            cart.save()
        else:
            # create new cartObject if product is not already in the cart
            newrow = Cart(user=request.user, product=product, quantity=request.POST["quantity"])
            newrow.save()

        #update the left in stock of the product
        product.leftInStock -= int(request.POST["quantity"])
        product.save()

        #redirects to the correct detail view depending on product type
        type = findTypeFromId(product_id)
        if type == "game":
            return redirect('/games/' + str(product_id))
        elif type == "console":
            return redirect('/consoles/' + str(product_id))
        elif type == "accessory":
            return redirect('/accessories/' + str(product_id))

@login_required()
def get_cart_items(request):
    cart = Cart.objects.filter(user=request.user)
    total_price = get_total_cart_price(request)
    if cart.exists():
        #get all the items for this cart
        context = {"cart": cart, "total_price": total_price}
        return render(request, 'cart/index.html', context)
    else:
        return render(request, 'cart/empty.html')


@login_required
def get_total_cart_price(request):
    total_sum = 0
    product_list = Cart.objects.filter(user=request.user)
    for cart in product_list:
        total_sum += (cart.product.price * cart.quantity)

    return total_sum



