from django import forms
from Menu.models import Dish

class ChangeForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ("image", "name", "weight", "category", "price", "discount", "alergic", "description")
        # """name = forms.CharField(required=True,initial= change.dishes.name )
        # category = forms.ChoiceField(required=True,initial= change.dishes.category )
        # price = forms.DecimalField(required=True,initial= change.dishes.price )
        # discount = forms.IntegerField(required=True,initial= change.dishes.discount )
        # description = forms.Textarea(required=True,initial= change.dishes.description )"""
