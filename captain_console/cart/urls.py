from django.urls import path
from . import views
from .views import (
    add_item_to_cart,
    delete_cart_item,
    get_order_details,
    checkout,
    process_payment,
    update_transaction_records,
    success
)


urlpatterns = [
    path('', views.get_user_pending_order, name="cart-index"),
    path(r'^add-to-cart/(?P<item_id>[-\w]+)/$', add_item_to_cart, name="add_to_cart"),
    path(r'^order-summary/$', get_order_details, name="order_summary"),
    path(r'^success/$', success, name='purchase_success'),
    path(r'^item/delete/(?P<item_id>[-\w]+)/$', delete_cart_item, name='delete_item'),
    path(r'^checkout/$', checkout, name='checkout'),
    path(r'^update-transaction/(?P<token>[-\w]+)/$', update_transaction_records,
        name='update_records')
]
