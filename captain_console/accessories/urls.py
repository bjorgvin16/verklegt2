from django.urls import path
from . import views
urlpatterns = [
    # mun vísa á http://localhost:8000/accessories
    path('', views.index, name="accessories-index"),
    path('<int:id>', views.get_console_by_id, name="accessories-details"),
]