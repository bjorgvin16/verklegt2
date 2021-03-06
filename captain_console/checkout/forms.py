from django import forms
from django_countries import Countries
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField

class ContactInfoForm(forms.Form):
    name = forms.CharField(max_length=255, label="Full name:")
    street_name = forms.CharField(max_length=255, label="Street Name:")
    house_number = forms.IntegerField(label="House Number:")
    city = forms.CharField(max_length=255, label="City:")
    zip = forms.IntegerField(label="ZIP-code/Postal code:")
    country = forms.ChoiceField(choices=Countries)

class PaymentInfoForm(forms.Form):
    cardholder = forms.CharField(max_length=255, label="Cardholder full name:")
    card_number = CardNumberField(label="Credit Card Number:")
    exp_date = CardExpiryField(label="Card Expiry Date:")
    cvc_code = SecurityCodeField(label="CVC/CVV Code:")
    #does this work??
