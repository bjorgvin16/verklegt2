from django.urls import path
from . import views
urlpatterns = [
    # mun vísa á http://localhost:8000/signup
    path('', views.index, name="signup-index"),
]