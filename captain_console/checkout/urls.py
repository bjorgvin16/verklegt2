from django.urls import path
from . import views

urlpatterns = [
    path('contact', views.checkout, name="checkout-contact"),
    path('payment', views.payment, name="checkout-payment"),
]