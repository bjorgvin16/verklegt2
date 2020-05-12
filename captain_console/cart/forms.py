from django import forms
from django_countries.fields import CountryField
from . import validators

class ContactInfoForm(forms.Form):
    contact = forms.CharField(max_length=255)
    street_name = forms.CharField(max_length=255)
    house_number = forms.IntegerField()
    city = forms.CharField(max_length=255)
    zip = forms.IntegerField()
    country = CountryField()

class PaymentInfoForm(forms.Form):
    cardholder = forms.CharField(max_length=255)
    card_number = forms.CharField(validators=[validators.card_num_validator])
    exp_date = forms.CharField(max_length=5, validators=[validators.exp_date_validator])
    cvc_code = forms.IntegerField(min_value=100, max_value=999)
