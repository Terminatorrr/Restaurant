# forms.py
from django import forms

class ReservationForm(forms.Form):
    date = forms.DateField()
    time = forms.TimeField()
    book = forms.IntegerField()
    seats = forms.IntegerField()
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
