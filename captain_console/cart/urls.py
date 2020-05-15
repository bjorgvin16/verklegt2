from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_cart_items, name="cart-index"),
    path('add-to-cart/<int:product_id>/', views.add_item_to_cart, name="cart-add_item_to_cart"),
    #path('success/', views.success, name="cart-success"),
    path('delete-item/<int:cart_id>/', views.delete_cart_item, name="cart-delete_item"),
    #path('create-order/', views.create_order, name="cart-create_order"),
]
