from django.urls import path
from . import views
urlpatterns = [
    # mun vísa á http://localhost:8000/cart
    path('', views.index, name="cart-index"),
]