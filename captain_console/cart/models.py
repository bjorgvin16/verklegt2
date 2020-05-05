from django.db import models
from userprofile.models import User
from frontpage.models import Product

class Cart(models.Model):
    customerId = models.ForeignKey(User, on_delete=models.CASCADE)
    inuse = models.BooleanField()

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
    firsNname = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    streetName = models.CharField(max_length=255)
    houseNumber = models.IntegerField()
    zipCode = models.IntegerField()
    city = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)