from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path
from About import views

urlpatterns = [

    re_path(r'^about/', views.about, name='About'),
]
