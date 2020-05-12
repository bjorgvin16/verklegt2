from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/games
    path('', views.index, name="games-index"),
    path('<int:id>', views.get_game_by_id, name="games-details"),
    path('desc/', views.order_by_desc, name="games-filter_desc"),
    path('lowhigh/', views.order_by_lowest_highest, name="games-lowest_highest"),
    path('highlow/', views.order_by_highest_lowest, name="games-highest_lowest"),
    path('manufacturers/<int:manufacturerid>/', views.get_manufacturer_by_id, name="games-manufacturer")
]