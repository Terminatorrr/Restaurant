from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path
from Reservation import views

app_name = 'Reservation'

urlpatterns = [
    re_path('save_data/', views.save_data, name='save_data'),
]
