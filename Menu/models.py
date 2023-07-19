from django.db import models

class DishCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(blank=True, default=True)
    def __str__(self):
        return  "%s" % (self.name)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Dish(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True, default=None)
    image = models.ImageField(upload_to=('dish_images/'),  blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    weight = models.DecimalField(max_digits=10, decimal_places=2, default=100)
    discount = models.IntegerField(default=0)
    alergic = models.CharField(max_length=128, blank=True, null=True, default=None)
    category = models.ForeignKey(DishCategory, blank=True, null=True, default=None, on_delete=models.SET_DEFAULT)
    description = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return  "%s %s" % (self.price, self.name)

    class Meta:
        verbose_name = 'Dish'
        verbose_name_plural = 'Dishes'





