from django.urls import path
from . import views
urlpatterns = [
    # mun vísa á http://localhost:8000/frontpage
    path('', views.index, name="frontpage-index"),
    path('search', views.index, name="search-index"),
    path('get_all_products/', views.get_all_products, name="all-products"),
    path('desc/', views.order_by_desc, name="products-filter_desc"),
    path('lowhigh/', views.order_by_lowest_highest, name="products-lowest_highest"),
    path('highlow/', views.order_by_highest_lowest, name="products-highest_lowest"),
]