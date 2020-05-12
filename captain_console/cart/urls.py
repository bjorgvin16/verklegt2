from django.urls import path
from . import views
from .views import (
    add_item_to_cart,
    delete_cart_item,
    get_order_details,
    checkout,
    process_payment,
    update_order_records,
    success
)


urlpatterns = [
    path('', views.get_user_pending_order, name="cart-index"),
    path('add-to-cart/<int:id>/', views.add_item_to_cart, name="cart-add_item_to_cart"),
    path('get-order-details/', views.get_order_details, name="cart-get_order_details" ),
    path('checkout/', views.checkout, name="cart-checkout"),
    path('success/', views.success, name="cart-success"),
    path('delete-item/<int:id>/', views.delete_cart_item, name="cart-delete_item")

    #path(r'^add-to-cart/(?P<item_id>[-\w]+)/$', add_item_to_cart, name="add_to_cart"),
    #path(r'^order-summary/$', get_order_details, name="order_summary"),
    #path(r'^success/$', success, name='purchase_success'),
    #path(r'^item/delete/(?P<item_id>[-\w]+)/$', delete_cart_item, name='delete_item'),
    #path(r'^checkout/$', checkout, name='checkout'),
    #path(r'^update-transaction/(?P<token>[-\w]+)/$', update_transaction_records,
    #    name='update_records')
]
