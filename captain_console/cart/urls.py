from django.urls import path
from . import views
from .views import (
    add_item_to_cart,
    delete_cart_item,
    get_cart_items,
    checkout,
    process_payment,
    success
)


urlpatterns = [
    path('', views.get_cart_items, name="cart-index"),
    path('add-to-cart/<int:product_id>/', views.add_item_to_cart, name="cart-add_item_to_cart"), #    path('<int:id>', views.get_game_by_id, name="games-details"),
    path('get-cart-items/', views.get_cart_items, name="cart-get_cart_details" ),
    path('checkout/', views.checkout, name="cart-checkout"),
    path('success/', views.success, name="cart-success"),
    path('delete-item/<int:id>/', views.delete_cart_item, name="cart-delete_item")
]
