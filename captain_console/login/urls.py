from django.urls import path
from . import views
urlpatterns = [
    # mun vísa á http://localhost:8000/login
    path('', views.index, name="login-index"),
]