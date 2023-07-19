from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path
from Menu import views

urlpatterns = [

    re_path(r'^menu/', views.menu, name='Menu'),
]
