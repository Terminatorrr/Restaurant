from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path
from FirstPage import views

urlpatterns = [

    re_path(r'^$', views.Firstpage, name='First_page'),
]
