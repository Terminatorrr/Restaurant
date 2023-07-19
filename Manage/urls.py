from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path
from Manage import views

urlpatterns = [

    re_path(r'^manage/', views.manage, name='Manage'),
    re_path(r'^delete_dish/(?P<dish_id>\w+)/$', views.delete_dish, name='delete_dish'),
    re_path(r'^delete_order/(?P<order_id>\w+)/$', views.delete_orders, name='delete_orders'),
    re_path(r'^confirm_orders/(?P<order_id>\w+)/$', views.confirm_orders, name='confirm_orders'),
]
