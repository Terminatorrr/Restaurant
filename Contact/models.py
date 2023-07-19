from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator


class Order(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True, default=None)
    email = models.EmailField(max_length=254, blank=True, null=True, default=None)
    phone = PhoneNumberField(blank=False, null=False)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True, default="11:00")
    booking = models.IntegerField(blank=True, null=True, default=1)
    status = models.BooleanField(blank=True, null=True, default=False)
    seats = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(22)])
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return  "%s %s %s %s" % (self.name, self.phone, self.date, self.seats)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


