from django.urls import path
from . import views

urlpatterns = [
    path('contact', views.checkout, name="checkout-contact"),
    path('payment', views.payment, name="checkout-payment"),
    path('review', views.review, name="checkout-review"),
    path('confirm', views.confirm, name="checkout-confirm"),
]