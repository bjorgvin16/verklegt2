from django.urls import path
from . import views
urlpatterns = [
    # mun vísa á http://localhost:8000/consoles
    path('', views.index, name="consoles-index"),
]