from django.urls import path
from . import views
urlpatterns = [
    # mun vísa á http://localhost:8000/products
    path('', views.index, name="games-index"),
]