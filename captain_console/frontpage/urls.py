from django.urls import path
from . import views
urlpatterns = [
    # mun vísa á http://localhost:8000/frontpage
    path('', views.index, name="frontpage-index"),
    path('search', views.index, name="search-index"),
]