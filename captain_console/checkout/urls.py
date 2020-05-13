from django.urls import path
from . import views

urlpatterns = [
    path('checkout/contact', views.checkout, name="checkout-contact"),
]