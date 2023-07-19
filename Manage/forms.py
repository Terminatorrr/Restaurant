from django import forms
from Menu.models import *

class ManageForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ("image", "name", "weight", "category", "price", "discount", "alergic", "description")


