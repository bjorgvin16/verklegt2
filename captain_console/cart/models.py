from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from users.models import Profile
from frontpage.models import Product
from django.utils import timezone

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    orderDate = models.DateTimeField(default=timezone.now)
    claimType = models.CharField(max_length=255)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    streetName = models.CharField(max_length=255)
    houseNumber = models.IntegerField()
    zipCode = models.IntegerField()
    city = models.CharField(max_length=255)
    country = CountryField()

class OrderItem(models.Model):
    order = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    #def get_cart_items(self):
    #    return self.items.all()

    #def get_cart_total(self):
    #    return sum([item.product.price for item in self.items.all()])