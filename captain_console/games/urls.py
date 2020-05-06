from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/games
    path('', views.index, name="games-index"),
    path('<int:id>', views.get_game_by_id, name="games-details"),
]