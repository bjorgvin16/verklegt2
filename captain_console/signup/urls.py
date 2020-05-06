from django.urls import path
from . import views
urlpatterns = [
    # http://localhost:8000/signup
    path('', views.index, name="signup-index"),

]