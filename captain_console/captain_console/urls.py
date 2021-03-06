"""captain_console URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import (handler400, handler403, handler404, handler500)
from django.conf.urls.static import static


# for a custom error pages
handler400 = 'captain_console.views.bad_request'
handler403 = 'captain_console.views.permission_denied'
handler404 = 'captain_console.views.page_not_found'
handler500 = 'captain_console.views.server_error'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('games/', include('games.urls')),
    path('consoles/', include('consoles.urls')),
    path('accessories/', include('accessories.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('users/', include('users.urls')),
    path('productsearch/', include('productsearch.urls')),
    path('', include('frontpage.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)