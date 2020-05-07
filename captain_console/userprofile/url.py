from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/userprofile
    path('', views.index, name="userprofile-index"),
]