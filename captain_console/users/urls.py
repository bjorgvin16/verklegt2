from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name="users-signup"),
    path("login/", views.login_user, name="users-login"),
    path('logout/', views.logoutUser, name="users-logout"),
    path('profile/', views.profile, name='users-profile')
]