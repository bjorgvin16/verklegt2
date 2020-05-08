from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/userprofile
    path('', views.index, name="users-index"),
    path('signup/', views.signup, name="users-signup"),
    path('login/', views.loginUser, name="users-login"),
    path('logout/', views.logoutUser, name="users-logout"),
]