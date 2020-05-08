from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/productsearch
    path('', views.index, name="productsearch-index"),
]