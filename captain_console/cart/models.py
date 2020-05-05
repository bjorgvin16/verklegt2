from django.db import models
from userprofile.models import User
from frontpage.models import Product

class Cart(models.Model):
    customerId = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField()

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Country(models.Model):
    name = models.CharField(max_length=255)

class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    orderDate = models.DateField()
    claimType = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    streetname = models.CharField(max_length=255)
    housenumber = models.IntegerField()
    zipcode = models.IntegerField()
    city = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)