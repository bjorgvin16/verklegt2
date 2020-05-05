from django.urls import path
from . import views
urlpatterns = [
    # http://localhost:8000/games
    path('', views.index, name="games-index"),

]