from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/cart...
    path('', views.get_cart_items, name="cart-index"),
    path('add-to-cart/<int:product_id>/', views.add_item_to_cart, name="cart-add_item_to_cart"),
    path('delete-item/<int:cart_id>/', views.delete_cart_item, name="cart-delete_item"),
    path('clear-cart/', views.clear_user_cart_data, name="clear-cart")
]
