from django import forms
from phonenumber_field.formfields import PhoneNumberField


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    phone = PhoneNumberField()
    date = forms.DateField()
    time = forms.TimeField()
    booking = forms.PositiveIntegerField()
    seats = forms.PositiveIntegerField(required=True)

