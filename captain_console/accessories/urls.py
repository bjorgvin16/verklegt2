from django.urls import path
from . import views
urlpatterns = [
    # http://localhost:8000/accessories...
    path('', views.index, name="accessories-index"),
    path('<int:id>', views.get_console_by_id, name="accessories-details"),
    path('desc/', views.order_by_desc, name="accessories-filter_desc"),
    path('lowhigh/', views.order_by_lowest_highest, name="accessories-lowest_highest"),
    path('highlow/', views.order_by_highest_lowest, name="accessories-highest_lowest")
]