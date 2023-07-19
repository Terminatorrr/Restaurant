from django.shortcuts import render
from .models import *


def menu(request):

    products_fast_food = Dish.objects.filter(category__id=6)
    products_salat = Dish.objects.filter(category__id=7)
    products_meet = Dish.objects.filter(category__id=8)
    products_side_dishes = Dish.objects.filter(category__id=9)
    products_drinks = Dish.objects.filter(category__id=10)
    return render(request, 'Menus/Menus.html', locals())
