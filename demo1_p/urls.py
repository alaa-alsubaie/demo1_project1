"""demo1_p URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from demo1 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('resturant_info/',views.resturant_info ,name='resturant_info'),
    path('ListApiView/',views.ListApiView.as_view() ,name='ListApiView'),
    path('DetailApiView/<int:x>/',views.DetailApiView.as_view() ,name='DetailApiView'),
    path('UpdateApiView/<int:x>/',views.UpdateApiView.as_view() ,name='UpdateApiView'),
    path('DeleteView/<int:x>/',views.DeleteView.as_view() ,name='DeleteView'),
]
