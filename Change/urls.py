from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path
from Change import views

urlpatterns = [
    re_path(r'^change/(?P<dish_id>\w+)/$', views.change, name='change'),
]
