from django.urls import path
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # http://localhost:8000/userprofile
    path('', views.index, name="users-index"),
    path('signup/', views.signup, name="users-signup"),
    path('login/', auth_views.LoginView.as_view(template_name = 'login/index.html'), name="users-login"),
    #path('login/', views.loginUser, name="users-login"),
    path('logout/', views.logoutUser, name="users-logout"),
]