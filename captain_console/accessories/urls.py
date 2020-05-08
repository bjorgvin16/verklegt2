from django.urls import path
from . import views
urlpatterns = [
    # mun vísa á http://localhost:8000/accessories
    path('', views.index, name="accessories-index"),
    path('<int:id>', views.get_console_by_id, name="accessories-details"),
    path('desc/', views.order_by_desc, name="filter_desc"),
    path('lowhigh/', views.order_by_lowest_highest, name="lowest_highest"),
    path('highlow/', views.order_by_highest_lowest, name="highest_lowest")
]