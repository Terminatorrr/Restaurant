from django.contrib import admin
from .models import *


class DishAdmin(admin.ModelAdmin):
    #list_display = ["name", "email"]
    list_display = [field.name for field in Dish._meta.fields]
    class Meta:
        model = Dish

admin.site.register(Dish, DishAdmin)




class DishCategoryAdmin(admin.ModelAdmin):
    #list_display = ["name", "email"]
    list_display = [field.name for field in DishCategory._meta.fields]

    class Meta:
        model = DishCategory

admin.site.register(DishCategory, DishCategoryAdmin)
